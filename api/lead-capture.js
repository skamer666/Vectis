// Fonction serverless Vercel : capture d'email discrete (lead magnet) sur
// les pages a forte intention (fiches avocat / etude). Insere la demande
// dans Supabase (table `leads`, voir supabase_schema.sql) avec
// status='pending'. Contrairement aux avis, aucune moderation n'est requise
// avant envoi -- mais aucun envoi d'email n'est automatise ici : Greg recoit
// (ou consulte) les leads dans Supabase -> Table Editor et gere l'envoi
// manuellement ou via une automatisation ulterieure (ex: Zapier/Make sur la
// table, ou une tache planifiee).
//
// Variables d'environnement requises (Vercel) :
//   SUPABASE_SERVICE_ROLE_KEY  -- identique a celle utilisee par
//                                  review-submit.js (cle secrete service_role)
const { checkRateLimit } = require("./_rate-limit");

const SUPABASE_URL = "https://qjiyxhsnrzahdmdvzsqi.supabase.co";

const MAX_URL_LEN = 500;
const MAX_TITLE_LEN = 200;
const ALLOWED_LANGS = ["fr", "de", "it", "en"];

function truncate(s, n) {
  return (typeof s === "string" ? s.trim() : "").slice(0, n);
}

function isEmail(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
}

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

  // 10 demandes / 15 min par IP.
  if (!(await checkRateLimit(req, "lead-capture", 10, 900))) {
    res.status(429).json({ error: "rate_limited" });
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

  // Honeypot anti-spam : champ cache cote formulaire (.lead-capture-hp).
  if (truncate(body.website, 50)) {
    res.status(200).json({ ok: true, slug: "ignored" });
    return;
  }

  if (!isEmail(body.email)) {
    res.status(400).json({ error: "invalid_email" });
    return;
  }

  const lang = ALLOWED_LANGS.includes(body.lang) ? body.lang : "fr";

  const row = {
    email: body.email.trim(),
    page_url: truncate(body.page_url, MAX_URL_LEN),
    page_title: truncate(body.page_title, MAX_TITLE_LEN),
    lang: lang,
    // Case a cocher facultative et decochee par defaut sur le formulaire :
    // voir supabase_schema.sql pour le detail du consentement et
    // send-review-reminders.js pour l'utilisation de ce champ.
    review_reminder_consent: body.review_reminder_consent === true,
  };

  try {
    const resp = await fetch(`${SUPABASE_URL}/rest/v1/leads`, {
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
    res.status(502).json({ error: "supabase_write_failed", detail: String(err.message || err) });
    return;
  }

  res.status(200).json({ ok: true });
};
