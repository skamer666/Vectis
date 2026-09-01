// Fonction Cloudflare Pages : reception du formulaire d'avis
// (templates/avis_demande.html). Insere l'avis dans Supabase (table
// `reviews`, voir supabase_schema.sql) avec status='pending'. Rien n'est
// publie automatiquement : chaque avis attend une revision manuelle par
// Greg directement dans Supabase -> Table Editor (changer `status` en
// 'approved') avant d'apparaitre sur le site.
//
// Variable d'environnement requise :
//   SUPABASE_SERVICE_ROLE_KEY  -- cle secrete service_role/secret (contourne
//                                  RLS pour permettre l'insertion depuis le
//                                  serveur ; jamais exposee cote client)
//
// L'URL du projet n'est pas un secret (elle est deja publique dans
// supabase_config.py, utilisee cote client par le widget d'avis) : elle est
// donc codee en dur ci-dessous plutot que de dependre d'une deuxieme
// variable d'environnement qu'on pourrait oublier de renseigner.
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
import { wrapVercelHandler } from "./_shim.js";
import { checkRateLimit } from "./_rate-limit.js";

const SUPABASE_URL = "https://qjiyxhsnrzahdmdvzsqi.supabase.co";

const MAX_BODY_LEN = 3000;
const MAX_TITLE_LEN = 140;
const MAX_NAME_LEN = 100;
const ALLOWED_LANGS = ["fr", "de", "it", "en"];

function truncate(s, n) {
  return (typeof s === "string" ? s.trim() : "").slice(0, n);
}

function isEmail(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
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
    res.status(500).json({ error: "server_not_configured" });
    return;
  }

  // 5 avis / heure par IP.
  if (!(await checkRateLimit(req, "review-submit", 5, 3600))) {
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

  // Honeypot anti-spam : champ cache cote formulaire, tout humain le laisse
  // vide, seuls les bots remplissent tous les champs d'un formulaire.
  if (truncate(body.website, 50)) {
    res.status(200).json({ ok: true, slug: "ignored" });
    return;
  }

  const lang = ALLOWED_LANGS.includes(body.lang) ? body.lang : "fr";
  const registryMatch = body.registry_match || {};
  const avocatNom = truncate(registryMatch.nom, 200);
  const cantonCode = truncate(registryMatch.code, 4).toUpperCase();
  const avocatSlug = truncate(registryMatch.slug, 200);

  if (!avocatNom || !cantonCode || !avocatSlug) {
    res.status(400).json({ error: "missing_registry_match" });
    return;
  }

  const rating = Number.parseInt(body.rating, 10);
  if (!Number.isInteger(rating) || rating < 1 || rating > 5) {
    res.status(400).json({ error: "invalid_rating" });
    return;
  }

  const reviewBody = truncate(body.body, MAX_BODY_LEN);
  if (!reviewBody) {
    res.status(400).json({ error: "missing_body" });
    return;
  }

  if (!isEmail(body.contact_email)) {
    res.status(400).json({ error: "invalid_email" });
    return;
  }

  const row = {
    canton_code: cantonCode,
    avocat_slug: avocatSlug,
    avocat_nom: avocatNom,
    rating: rating,
    title: truncate(body.title, MAX_TITLE_LEN) || null,
    body: reviewBody,
    reviewer_name: truncate(body.reviewer_name, MAX_NAME_LEN) || null,
    reviewer_email: body.contact_email,
    lang: lang,
    // `status` volontairement absent : la colonne a un DEFAULT 'pending' en
    // base, le client ne doit jamais pouvoir choisir son propre statut.
  };

  try {
    const resp = await fetch(`${SUPABASE_URL}/rest/v1/reviews`, {
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
}

export const onRequest = wrapVercelHandler(handler);
