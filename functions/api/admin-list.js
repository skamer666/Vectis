// Fonction Cloudflare Pages : liste les elements en attente de moderation
// pour la page interne /interne/verification-avocats/
// (templates/verification_review.html). Fusion de deux fonctions
// auparavant separees (verification-list.js et profile-list.js) pour
// rester sous la limite de 12 fonctions serverless du plan Hobby Vercel --
// meme logique, juste selectionnee par ?kind=verification|profile. Portage
// vers Cloudflare Pages : la fusion est conservee (aucune raison de la
// defaire, Cloudflare Pages n'a pas de limite de nombre de fonctions
// comparable de toute facon, mais ca reste 1 seul fichier a maintenir).
//
// GET /api/admin-list?kind=verification|profile, header x-admin-token.
//
// kind=verification -- demandes de verification d'identite
// (verification_requests). Documents/selfies (palier document) renvoyes
// via URL signee, valable quelques minutes seulement.
//
// kind=profile -- soumissions de profil avocat (lawyer_profile_submissions,
// bio/photo/liens/coordonnees). Photos dans un bucket PUBLIC : URL directe,
// pas besoin de signature.
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
import { wrapVercelHandler } from "./_shim.js";
import * as lib from "./_verification-lib.js";

const SIGNED_URL_TTL_SECONDS = 300;

async function listVerification() {
  const rows = await lib.supabaseSelect(
    "verification_requests",
    "status=eq.pending&order=created_at.asc&select=id,created_at,method,canton,avocat_slug,avocat_nom,avocat_url,account_email,contact_note,document_path,selfie_path,email_sent,free_website_interest"
  );

  let contacts = {};
  try {
    contacts = lib.loadContacts();
  } catch (e) {
    contacts = {};
  }

  const out = [];
  for (const row of rows) {
    const entry = {
      id: row.id,
      created_at: row.created_at,
      method: row.method,
      canton: row.canton,
      nom_complet: row.avocat_nom,
      url: row.avocat_url,
      account_email: row.account_email,
      contact_note: row.contact_note,
      email_sent: row.email_sent,
      free_website_interest: row.free_website_interest,
    };
    if (row.method === "phone") {
      const known = contacts[`${row.canton}/${row.avocat_slug}`] || {};
      entry.telephone = known.telephone || null;
    }
    if (row.method === "document") {
      if (row.document_path) {
        entry.document_signed_url = await lib.storageSignedUrl(row.document_path, SIGNED_URL_TTL_SECONDS);
      }
      if (row.selfie_path) {
        entry.selfie_signed_url = await lib.storageSignedUrl(row.selfie_path, SIGNED_URL_TTL_SECONDS);
      }
    }
    out.push(entry);
  }

  return { requests: out };
}

async function listProfile() {
  const rows = await lib.supabaseSelect(
    "lawyer_profile_submissions",
    "status=eq.pending&order=submitted_at.asc&select=id,submitted_at,canton,avocat_slug,bio,photo_path,display_email,display_telephone,links"
  );
  const out = rows.map((row) => ({
    id: row.id,
    submitted_at: row.submitted_at,
    canton: row.canton,
    avocat_slug: row.avocat_slug,
    bio: row.bio,
    display_email: row.display_email,
    display_telephone: row.display_telephone,
    links: row.links,
    photo_url: row.photo_path ? `${lib.SUPABASE_URL}/storage/v1/object/public/lawyer-photos/${row.photo_path}` : null,
  }));
  return { submissions: out };
}

async function handler(req, res) {
  if (req.method !== "GET") {
    res.status(405).json({ error: "method_not_allowed" });
    return;
  }
  if (!(await lib.checkAdminAuth(req))) {
    res.status(401).json({ error: "unauthorized" });
    return;
  }
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) {
    res.status(500).json({ error: "server_not_configured" });
    return;
  }

  const kind = req.query.kind;
  if (kind !== "verification" && kind !== "profile") {
    res.status(400).json({ error: "invalid_kind" });
    return;
  }

  try {
    const payload = kind === "verification" ? await listVerification() : await listProfile();
    res.status(200).json(payload);
  } catch (err) {
    res.status(502).json({ error: "list_failed", detail: String(err.message || err) });
  }
}

export const onRequest = wrapVercelHandler(handler);
