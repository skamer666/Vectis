// Fonction serverless Vercel : enregistre la reponse de l'avocat a l'offre
// "site web gratuit" presentee juste apres la creation de son compte (voir
// templates/verification_demande.html, ecran affiche entre la soumission
// du formulaire de verification et la validation de l'identite par Greg --
// website_offer_content.py pour le texte de l'offre et du contrat).
//
// POST { id, interested: true|false, contract_version? }
//   id               -- identifiant de la ligne verification_requests deja
//                        creee par api/verification-request.js (renvoye
//                        dans sa reponse). Sert uniquement a savoir a
//                        quelle demande rattacher la reponse -- ce n'est
//                        pas un secret, mais un UUID v4 non enumerable.
//   interested       -- true si l'avocat clique "Je veux un site GRATUIT"
//                        puis accepte le contrat, false s'il decline
//                        (des l'ecran d'offre, ou depuis l'ecran de
//                        contrat sans l'accepter).
//   contract_version -- OBLIGATOIRE si interested=true. Doit correspondre
//                        exactement a CONTRACT_VERSION (website_offer_content.py,
//                        dupliquee ci-dessous cote serveur) : evite qu'une
//                        acceptation soit enregistree pour une version du
//                        contrat qui ne correspond pas a celle reellement
//                        affichee/parcourue par le client.
//
// Aucune authentification requise : ce endpoint est appele par le
// navigateur du demandeur juste apres sa propre soumission, avec un id
// qu'il vient de recevoir. Il ne permet de modifier que les 3 colonnes
// free_website_* d'une ligne encore 'pending' -- jamais le statut de la
// demande de verification elle-meme, jamais les autres colonnes.
//
// IMPORTANT (non-juridique) : voir l'avertissement en tete de
// website_offer_content.py -- ce contrat est un premier jet a faire
// relire par un avocat suisse avant toute utilisation reelle.

const lib = require("./_verification-lib");

// Doit rester synchronisee avec CONTRACT_VERSION dans website_offer_content.py.
const EXPECTED_CONTRACT_VERSION = "2026-08-20-v1";

module.exports = async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.status(204).end();
    return;
  }
  if (req.method !== "POST") {
    res.status(405).json({ error: "method_not_allowed" });
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
  const interested = body && body.interested === true;
  if (!id || typeof id !== "string") {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  if (interested && body.contract_version !== EXPECTED_CONTRACT_VERSION) {
    res.status(400).json({ error: "contract_version_mismatch" });
    return;
  }

  try {
    const rows = await lib.supabaseSelect(
      "verification_requests",
      `id=eq.${encodeURIComponent(id)}&select=id,status,free_website_interest`
    );
    const row = rows[0];
    if (!row) {
      res.status(404).json({ error: "not_found" });
      return;
    }
    // On accepte quand meme d'ecraser une reponse deja enregistree (par
    // exemple si l'avocat revient en arriere et change d'avis avant que
    // Greg ne traite la demande) tant que celle-ci est encore 'pending'.
    if (row.status !== "pending") {
      res.status(409).json({ error: "already_decided" });
      return;
    }

    const patch = {
      free_website_interest: interested,
      free_website_contract_accepted_at: interested ? new Date().toISOString() : null,
      free_website_contract_version: interested ? EXPECTED_CONTRACT_VERSION : null,
    };
    await lib.supabasePatch("verification_requests", id, patch);

    res.status(200).json({ ok: true });
  } catch (err) {
    res.status(502).json({ error: "decision_failed", detail: String(err.message || err) });
  }
};
