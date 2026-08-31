// Fonction Cloudflare Pages : enregistre l'interet d'un avocat pour
// l'offre "site web gratuit" (voir website_offer_content.py pour le texte
// de l'offre et du contrat). Fusion de deux fonctions auparavant separees
// (website-offer-decision.js et lawyer-website-offer.js) pour rester sous
// la limite de 12 fonctions serverless du plan Hobby Vercel -- deux flux
// distincts, selectionnes par body.flow. Fusion conservee lors du portage
// Cloudflare (pas de raison de la defaire).
//
// POST { flow: "signup" | "profile", ... }
//
// flow="signup" -- reponse a l'offre presentee juste apres la creation du
// compte (templates/verification_demande.html), AVANT validation de
// l'identite par Greg. Body : { flow, id, interested, contract_version? }.
//   id          -- identifiant de la ligne verification_requests deja creee
//                   par api/verification-request.js. Pas un secret, mais un
//                   UUID v4 non enumerable. Aucune authentification requise :
//                   appele par le navigateur du demandeur juste apres sa
//                   propre soumission, avec un id qu'il vient de recevoir.
//                   Ne permet de modifier que les 3 colonnes free_website_*
//                   d'une ligne encore 'pending'.
//   interested  -- true si l'avocat accepte le contrat, false s'il decline.
//   contract_version -- OBLIGATOIRE si interested=true, doit correspondre
//                   exactement a EXPECTED_CONTRACT_VERSION.
//
// flow="profile" -- demande depuis l'espace avocat DEJA CONNECTE
// (templates/mon_profil.html), une fois l'identite validee et le compte
// actif -- couvre le cas ou l'offre n'avait pas ete prise a la creation du
// compte. Body : { flow, contract_version, lang }, header
// Authorization: Bearer <token Supabase Auth de l'avocat connecte> --
// revalide aupres de Supabase (getLawyerAccount), jamais fait confiance au
// contenu du token sans verification. Enregistre dans website_offer_requests
// (voir supabase_schema.sql).
//
// Dans les deux cas, quand l'offre est acceptee : deux emails best-effort
// (ne bloquent jamais la reponse, ne font jamais echouer la demande si
// Resend est absent ou en erreur) : au Client, une copie complete du
// contrat qu'il vient d'accepter (data/contract_content.json) ; a Greg
// (ADMIN_NOTIFY_EMAIL), notification qu'un avocat veut le site gratuit.
//
// IMPORTANT (non-juridique) : voir l'avertissement en tete de
// website_offer_content.py -- ce contrat est un premier jet a faire relire
// par un avocat suisse avant toute utilisation reelle.
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
import { wrapVercelHandler } from "./_shim.js";
import * as lib from "./_verification-lib.js";

// Doit rester synchronisee avec CONTRACT_VERSION dans website_offer_content.py.
const EXPECTED_CONTRACT_VERSION = "2026-08-20-v1";
const ALLOWED_LANGS = ["fr", "de", "it", "en"];

async function handleSignupFlow(body, res) {
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
      `id=eq.${encodeURIComponent(id)}&select=id,status,free_website_interest,lang,canton,avocat_nom,avocat_url,account_email`
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

    // Best-effort, apres la reponse : ce bloc ne doit plus jamais toucher
    // `res`, meme en cas d'erreur synchrone, sous peine de crash
    // ERR_HTTP_HEADERS_SENT -- d'ou son propre try/catch.
    if (interested) {
      try {
        const lang = row.lang || "fr";
        Promise.all([
          lib.sendContractToClient(row.account_email, row.avocat_nom || "", lang),
          lib.notifyAdminFreeWebsiteInterest({
            eventLabel: "acceptée à la création du compte",
            avocatNom: row.avocat_nom || "",
            canton: row.canton || "",
            avocatUrl: row.avocat_url || "",
            accountEmail: row.account_email || "",
          }),
        ]).catch(function () {});
      } catch (e) {
        // ignore -- best-effort, voir commentaire ci-dessus.
      }
    }
  } catch (err) {
    res.status(502).json({ error: "decision_failed", detail: String(err.message || err) });
  }
}

async function handleProfileFlow(body, req, res) {
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

    // Best-effort, apres la reponse -- meme precaution que handleSignupFlow.
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
}

async function handler(req, res) {
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

  const flow = body && body.flow;
  if (flow === "signup") {
    await handleSignupFlow(body, res);
    return;
  }
  if (flow === "profile") {
    await handleProfileFlow(body, req, res);
    return;
  }
  res.status(400).json({ error: "invalid_flow" });
}

export const onRequest = wrapVercelHandler(handler);
