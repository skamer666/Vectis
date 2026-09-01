// Fonction Cloudflare Pages : reception des evenements d'analytics "maison"
// (static/js/analytics.js, appele sur toutes les pages via templates/base.html).
// Insere une ligne dans Supabase (table `analytics_events`, voir
// supabase_schema.sql) pour chaque evenement -- pageview, fin de page
// (duree + profondeur de defilement), et evenements personnalises (soumission
// de formulaire, clic favori/comparer, etc.) declenches via
// window.legatisTrack(...).
//
// Objectif : mesurer l'engagement (temps sur page, pages par session, taux
// de retour) sans dependre d'un outil tiers et sans jamais stocker de
// donnee personnelle identifiante -- voir le commentaire en tete de la
// section analytics_events dans supabase_schema.sql pour le detail des
// choix de confidentialite (pas d'IP, pas de cookie, pas d'URL de referrer
// complete, pas d'empreinte navigateur detaillee).
//
// Appele tres frequemment (une fois par page vue au minimum) : ce fichier
// reste volontairement autonome et minimal, sans dependance sur
// _verification-lib.js (meme principe que lead-capture.js / review-submit.js).
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
// process.env.SUPABASE_SERVICE_ROLE_KEY continue de fonctionner tel quel
// (flag nodejs_compat, wrangler.toml) -- variable d'environnement requise,
// identique a celle utilisee sous Vercel.
import { wrapVercelHandler } from "./_shim.js";
import { checkRateLimit } from "./_rate-limit.js";

const SUPABASE_URL = "https://qjiyxhsnrzahdmdvzsqi.supabase.co";

const ALLOWED_EVENT_TYPES = [
  "pageview",
  "pageview_end",
  "lead_submit",
  "favorite_add",
  "compare_add",
  "outbound_click",
  "calculator_complete",
  "review_submit",
  "verification_submit",
  "website_offer_decision",
  "custom",
];
const ALLOWED_LANGS = ["fr", "de", "it", "en"];
const ALLOWED_DEVICE_TYPES = ["mobile", "tablet", "desktop"];
const MAX_PATH_LEN = 400;
const MAX_DOMAIN_LEN = 200;
const MAX_ID_LEN = 100;
const MAX_META_JSON_LEN = 2000;

function truncate(s, n) {
  return (typeof s === "string" ? s.trim() : "").slice(0, n);
}

async function handler(req, res) {
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
    // Ne casse jamais la navigation : l'analytics est un a-cote, pas un
    // service critique. On repond simplement "pas configure" sans bruit.
    res.status(200).json({ ok: false, reason: "not_configured" });
    return;
  }

  // 300 evenements / 10 min par IP : seuil volontairement large (un vrai
  // visiteur actif peut declencher beaucoup d'evenements -- pageview, fin de
  // page, clics -- en naviguant plusieurs fiches), juste pour couper un
  // flood/DoS applicatif evident. Meme philosophie que ci-dessus : jamais
  // d'erreur visible cote client, on repond 200 en silence.
  if (!(await checkRateLimit(req, "track", 300, 600))) {
    res.status(200).json({ ok: false, reason: "rate_limited" });
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
  if (!body || typeof body !== "object") {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  const eventType = ALLOWED_EVENT_TYPES.includes(body.event_type) ? body.event_type : null;
  const path = truncate(body.path, MAX_PATH_LEN);
  const sessionId = truncate(body.session_id, MAX_ID_LEN);
  const visitorId = truncate(body.visitor_id, MAX_ID_LEN);
  if (!eventType || !path || !sessionId || !visitorId) {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  const lang = ALLOWED_LANGS.includes(body.lang) ? body.lang : null;
  const deviceType = ALLOWED_DEVICE_TYPES.includes(body.device_type) ? body.device_type : null;
  const canton = truncate(body.canton, 4).toUpperCase() || null;
  const referrerDomain = truncate(body.referrer_domain, MAX_DOMAIN_LEN) || null;

  let meta = null;
  if (body.meta && typeof body.meta === "object") {
    const metaJson = JSON.stringify(body.meta).slice(0, MAX_META_JSON_LEN);
    try {
      meta = JSON.parse(metaJson);
    } catch (e) {
      meta = null;
    }
  }

  const row = {
    event_type: eventType,
    path,
    lang,
    canton,
    referrer_domain: referrerDomain,
    device_type: deviceType,
    session_id: sessionId,
    visitor_id: visitorId,
    meta,
  };

  try {
    const resp = await fetch(`${SUPABASE_URL}/rest/v1/analytics_events`, {
      method: "POST",
      headers: {
        apikey: process.env.SUPABASE_SERVICE_ROLE_KEY,
        Authorization: `Bearer ${process.env.SUPABASE_SERVICE_ROLE_KEY}`,
        "Content-Type": "application/json",
        Prefer: "return=minimal",
      },
      body: JSON.stringify(row),
    });
    if (!resp.ok) {
      const text = await resp.text();
      throw new Error(`Supabase insert failed: ${resp.status} ${text.slice(0, 300)}`);
    }
  } catch (err) {
    // Toujours 200 cote client : un echec d'analytics ne doit jamais
    // generer d'erreur visible ni de retry agressif depuis le navigateur.
    res.status(200).json({ ok: false, error: "write_failed" });
    return;
  }

  res.status(200).json({ ok: true });
}

export const onRequest = wrapVercelHandler(handler);
