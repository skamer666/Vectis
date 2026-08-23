// Fonction serverless Vercel : un avocat DEJA CONNECTE (compte actif, apres
// verification d'identite) demande l'offre "site web gratuit" depuis son
// espace /mon-profil/ -- voir website_offer_content.py pour le texte du
// contrat et api/website-offer-decision.js pour le meme parcours au moment
// de la creation du compte (avant validation de l'identite). Ce fichier-ci
// couvre le cas ou l'avocat n'avait pas pris l'offre a ce moment-la (ou
// veut la redemander), une fois son compte pleinement actif.
//
// POST { contract_version, lang }, header Authorization: Bearer <token
// Supabase Auth de l'avocat connecte> -- revalide aupres de Supabase (voir
// getLawyerAccount dans _verification-lib.js), jamais fait confiance au
// contenu du token sans verification. Le canton/avocat_slug/avocat_nom/
// avocat_url et l'email du compte viennent TOUJOURS de lawyer_accounts /
// Supabase Auth cote serveur, jamais d'une valeur envoyee par le client --
// un avocat ne peut demander l'offre que pour SA propre fiche.
//
// contract_version -- doit correspondre exactement a EXPECTED_CONTRACT_VERSION
// (meme constante que website-offer-decision.js, dupliquee ici pour la
// meme raison : eviter qu'une acceptation soit enregistree pour une version
// du contrat qui ne correspond pas a celle reellement affichee/parcourue).
//
// Enregistre la demande dans website_offer_requests (voir
// supabase_schema.sql) puis envoie, best-effort, les 2 memes emails que
// website-offer-decision.js : la copie du contrat au Client, et une
// notification a Greg.

const lib = require("./_verification-lib");

const EXPECTED_CONTRACT_VERSION = "2026-08-20-v1";
const ALLOWED_LANGS = ["fr", "de", "it", "en"];

module.exports = async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");

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
  const lang = ALLOWED_LANGS.includes(body && body.lang) ? body.lang : "fr";
  if (!body || body.contract_version !== EXPECTED_CONTRACT_VERSION) {
    res.status(400).json({ error: "contract_version_mismatch" });
    return;
  }

  const lawyer = await lib.getLawyerAccount(req);
  if (!lawyer) {
    res.status(401).json({ error: "unauthorized" });
    return;
  }

  try {
    await lib.supabaseInsert("website_offer_requests", {
      user_id: lawyer.user_id,
      canton: lawyer.canton,
      avocat_slug: lawyer.avocat_slug,
      avocat_nom: lawyer.avocat_nom,
      avocat_url: lawyer.avocat_url,
      account_email: lawyer.email,
      lang,
      contract_version: EXPECTED_CONTRACT_VERSION,
    });

    res.status(200).json({ ok: true });

    // Best-effort, apres la reponse -- meme precaution que
    // website-offer-decision.js : ce bloc ne doit plus jamais toucher `res`.
    try {
      Promise.all([
        lib.sendContractToClient(lawyer.email, lawyer.avocat_nom || "", lang),
        lib.notifyAdminFreeWebsiteInterest({
          eventLabel: "demandée depuis l'espace avocat",
          avocatNom: lawyer.avocat_nom || "",
          canton: lawyer.canton || "",
          avocatUrl: lawyer.avocat_url || "",
          accountEmail: lawyer.email || "",
        }),
      ]).catch(function () {});
    } catch (e) {
      // ignore -- best-effort, voir commentaire ci-dessus.
    }
  } catch (err) {
    res.status(502).json({ error: "request_failed", detail: String(err.message || err) });
  }
};
