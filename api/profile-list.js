// Fonction serverless Vercel : liste les soumissions de profil avocat
// (photo, bio, coordonnees affichees, liens) en attente de moderation, pour
// la section "Profils en attente" de la page interne
// /interne/verification-avocats/.
//
// Protegee par le meme jeton administrateur que les fonctions
// verification-list.js / verification-decide.js (header x-admin-token).
// Contrairement aux documents d'identite, les photos de profil vivent dans
// un bucket PUBLIC (contenu non sensible destine a devenir public une fois
// approuve) : pas besoin d'URL signee, une URL publique directe suffit.

const lib = require("./_verification-lib");

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
    res.status(200).json({ submissions: out });
  } catch (err) {
    res.status(502).json({ error: "list_failed", detail: String(err.message || err) });
  }
};
