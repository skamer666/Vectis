// Fonction serverless Vercel : liste les demandes de verification
// d'identite en attente, pour la page interne
// /interne/verification-avocats/ (templates/verification_review.html).
//
// Protegee par un jeton partage (header x-admin-token, compare en temps
// constant a la variable d'environnement Vercel VERIFICATION_ADMIN_TOKEN --
// une longue chaine aleatoire que Greg genere et garde pour lui, jamais un
// compte tiers). Sans ce jeton, aucune donnee n'est renvoyee : ni les
// demandes elles-memes, ni les liens vers les documents. Les URLs vers les
// documents/selfies sont signees et valables quelques minutes seulement --
// jamais de lien permanent ni de bucket public.

const lib = require("./_verification-lib");

const SIGNED_URL_TTL_SECONDS = 300;

module.exports = async function handler(req, res) {
  if (req.method !== "GET") {
    res.status(405).json({ error: "method_not_allowed" });
    return;
  }
  if (!lib.checkAdminToken(req)) {
    res.status(401).json({ error: "unauthorized" });
    return;
  }
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) {
    res.status(500).json({ error: "server_not_configured" });
    return;
  }

  try {
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

    res.status(200).json({ requests: out });
  } catch (err) {
    res.status(502).json({ error: "list_failed", detail: String(err.message || err) });
  }
};
