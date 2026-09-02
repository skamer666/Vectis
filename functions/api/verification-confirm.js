// Fonction Cloudflare Pages : point d'atterrissage du lien de confirmation
// envoye par email (palier email de la cascade de verification d'identite).
// GET /api/verification-confirm?rid=<id>&token=<raw>&lang=<lang>
//
// Verifie le jeton (compare au hash stocke en base, en temps constant),
// verifie l'expiration et le statut, puis active REELLEMENT le compte
// pre-cree lors de la demande (verification-request.js) : bascule
// email_confirm=true sur l'utilisateur Supabase Auth deja cree, et cree le
// lien lawyer_accounts (fiche <-> compte). Aucune intervention de Greg
// necessaire pour ce palier -- c'est tout le principe : seul quelqu'un
// ayant acces a la boite mail DEJA enregistree pour cette fiche peut avoir
// recu ce lien. Redirige ensuite vers la page statique localisee
// /verification-confirmee/ avec ?status=ok|expired|error pour l'affichage
// -- cette fonction ne rend jamais de HTML elle-meme.
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
// res.writeHead(302, {Location}) reste utilisable tel quel (voir _shim.js).
import { wrapVercelHandler } from "./_shim.js";
import * as lib from "./_verification-lib.js";

const ALLOWED_LANGS = ["fr", "de", "it", "en"];
const SEGMENTS = {
  fr: "identite-confirmee",
  de: "identitaet-bestaetigt",
  it: "identita-confermata",
  en: "identity-confirmed",
};

function redirectTo(res, lang, status) {
  const seg = SEGMENTS[lang] || SEGMENTS.fr;
  res.writeHead(302, { Location: `/${lang}/${seg}/?status=${status}` });
  res.end();
}

async function handler(req, res) {
  const lang = ALLOWED_LANGS.includes(req.query.lang) ? req.query.lang : "fr";

  if (req.method !== "GET") {
    res.status(405).json({ error: "method_not_allowed" });
    return;
  }
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) {
    redirectTo(res, lang, "error");
    return;
  }

  const rid = req.query.rid;
  const token = req.query.token;
  if (!rid || !token) {
    redirectTo(res, lang, "error");
    return;
  }

  try {
    const rows = await lib.supabaseSelect(
      "verification_requests",
      `id=eq.${encodeURIComponent(rid)}&select=id,status,method,token_hash,token_expires_at,pending_user_id,canton,avocat_slug,avocat_nom,avocat_url,marketing_consent,marketing_consent_ip`
    );
    const row = rows[0];
    if (!row || row.method !== "email" || !row.token_hash || !row.pending_user_id) {
      redirectTo(res, lang, "error");
      return;
    }
    if (row.status !== "pending") {
      // Deja traitee (approuvee ou refusee) : lien deja utilise.
      redirectTo(res, lang, "expired");
      return;
    }
    if (new Date(row.token_expires_at).getTime() < Date.now()) {
      redirectTo(res, lang, "expired");
      return;
    }
    if (!lib.safeEqual(lib.hashToken(token), row.token_hash)) {
      redirectTo(res, lang, "error");
      return;
    }

    await lib.adminConfirmUser(row.pending_user_id);
    await lib.supabaseInsert("lawyer_accounts", {
      user_id: row.pending_user_id,
      canton: row.canton,
      avocat_slug: row.avocat_slug,
      avocat_nom: row.avocat_nom,
      avocat_url: row.avocat_url,
      marketing_consent: !!row.marketing_consent,
      marketing_consent_ip: row.marketing_consent ? row.marketing_consent_ip : null,
    });
    await lib.supabasePatch("verification_requests", row.id, {
      status: "approved",
      decided_at: new Date().toISOString(),
      decided_by: "auto-email",
      token_hash: null,
    });
    redirectTo(res, lang, "ok");
  } catch (e) {
    redirectTo(res, lang, "error");
  }
}

export const onRequest = wrapVercelHandler(handler);
