// Fonction serverless Vercel : Greg valide ou refuse une soumission de
// profil avocat (bio / photo / liens / coordonnees affichees) depuis la
// section "Profils en attente" de /interne/verification-avocats/.
//
// POST { id, decision: "approved" | "rejected" }, header x-admin-token.
//
// Contrairement a verification-decide.js, il n'y a ici AUCUN document
// sensible a supprimer : la photo vit dans le bucket public lawyer-photos
// et le reste (bio, liens, coordonnees) n'est pas une piece d'identite --
// rien n'est efface, on se contente de changer le statut. La ligne reste
// en base (historique append-only) : c'est elle qui, une fois approuvee,
// devient la source affichee publiquement sur la fiche (voir le widget de
// profil sur avocat.html, qui ne lit que status='approved').
//
// Une fois approuvee, une soumission plus ancienne du meme avocat n'est
// jamais effacee non plus -- le widget public prend simplement la plus
// recente approuvee (order=submitted_at.desc&limit=1), donc les anciennes
// versions restent en historique mais cessent d'etre affichees.

const lib = require("./_verification-lib");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
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

  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch (e) {
      res.status(400).json({ error: "invalid_json" });
      return;
    }
  }
  const id = body && body.id;
  const decision = body && body.decision;
  if (!id || !["approved", "rejected"].includes(decision)) {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  try {
    const rows = await lib.supabaseSelect(
      "lawyer_profile_submissions",
      `id=eq.${encodeURIComponent(id)}&select=id,status`
    );
    const row = rows[0];
    if (!row) {
      res.status(404).json({ error: "not_found" });
      return;
    }
    if (row.status !== "pending") {
      res.status(409).json({ error: "already_decided" });
      return;
    }

    await lib.supabasePatch("lawyer_profile_submissions", id, {
      status: decision,
      decided_at: new Date().toISOString(),
      decided_by: "greg",
    });

    res.status(200).json({ ok: true });
  } catch (err) {
    res.status(502).json({ error: "decide_failed", detail: String(err.message || err) });
  }
};
