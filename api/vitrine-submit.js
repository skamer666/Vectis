// Fonction serverless Vercel : reception du formulaire de demande de vitrine
// avocat (templates/vitrine_demande.html). Ecrit la soumission et la photo
// directement dans le depot GitHub (data/vitrines/pending/, static/vitrines/photos/)
// via l'API GitHub Contents. Rien n'est publie automatiquement : chaque
// soumission attend une revision manuelle (page /interne/vitrines-en-attente/)
// avant d'etre deplacee vers data/vitrines/approved/ par Greg.
//
// Variables d'environnement requises (a definir dans Vercel, jamais dans le
// code) :
//   GITHUB_TOKEN       -- jeton avec droit d'ecriture sur le depot
//   GITHUB_REPO        -- "skamer666/Vectis"
//   GITHUB_BRANCH      -- "main" (optionnel, defaut "main")

const ALLOWED_TEMPLATES = ["prestige", "moderne", "chaleureux"];
const ALLOWED_ACCENTS = ["bordeaux", "encre", "sapin", "ardoise"];
const ALLOWED_FRAMES = ["cercle", "carre-arrondi", "plein-cadre"];
const ALLOWED_FONTS = ["classique", "elegant", "contemporain"];
const ALLOWED_LANGS = ["fr", "de", "it", "en"];
const MAX_PHOTO_BYTES = 2 * 1024 * 1024;
const MAX_FIELD_LEN = 3000;

function isHttpUrl(s) {
  return typeof s === "string" && /^https?:\/\//.test(s);
}

function isVideoUrl(s) {
  return typeof s === "string" && /^https?:\/\/(www\.)?(youtube\.com|youtu\.be|vimeo\.com)\//.test(s);
}

function slugify(text) {
  return (text || "")
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 60) || "x";
}

function truncate(s, n) {
  return (typeof s === "string" ? s : "").slice(0, n);
}

function isEmail(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
}

async function githubRequest(path, options) {
  const repo = process.env.GITHUB_REPO;
  const token = process.env.GITHUB_TOKEN;
  const url = `https://api.github.com/repos/${repo}/contents/${path}`;
  return fetch(url, {
    ...options,
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: "application/vnd.github+json",
      "Content-Type": "application/json",
      "User-Agent": "legatis-vitrine-intake",
      ...(options && options.headers ? options.headers : {}),
    },
  });
}

async function getExistingSha(path, branch) {
  const res = await githubRequest(`${path}?ref=${branch}`, { method: "GET" });
  if (res.status === 200) {
    const json = await res.json();
    return json.sha;
  }
  return null;
}

async function putFile(path, base64Content, message, branch) {
  const sha = await getExistingSha(path, branch);
  const body = { message, content: base64Content, branch };
  if (sha) body.sha = sha;
  const res = await githubRequest(path, { method: "PUT", body: JSON.stringify(body) });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`GitHub write failed for ${path}: ${res.status} ${text.slice(0, 300)}`);
  }
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
  if (!process.env.GITHUB_TOKEN || !process.env.GITHUB_REPO) {
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
  if (!body || typeof body !== "object") {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  const lang = ALLOWED_LANGS.includes(body.lang) ? body.lang : "fr";
  const registryMatch = body.registry_match || {};
  const nom = truncate(registryMatch.nom, 200);
  const code = truncate(registryMatch.code, 4).toUpperCase();
  const regSlug = truncate(registryMatch.slug, 200);
  const ville = truncate(registryMatch.ville, 120);

  if (!nom || !code || !regSlug) {
    res.status(400).json({ error: "missing_registry_match" });
    return;
  }
  if (!isEmail(body.contact_email)) {
    res.status(400).json({ error: "invalid_email" });
    return;
  }
  const template = ALLOWED_TEMPLATES.includes(body.template) ? body.template : "prestige";
  const accentColor = ALLOWED_ACCENTS.includes(body.accent_color) ? body.accent_color : "bordeaux";

  const specialites = Array.isArray(body.specialites) ? body.specialites.slice(0, 20).map((s) => truncate(s, 60)) : [];
  const distinctions = Array.isArray(body.distinctions) ? body.distinctions.slice(0, 15).map((s) => truncate(s, 200)) : [];
  const galerie = Array.isArray(body.galerie)
    ? body.galerie.filter(isHttpUrl).slice(0, 4).map((s) => truncate(s, 500))
    : [];
  const photoFrame = ALLOWED_FRAMES.includes(body.photo_frame) ? body.photo_frame : "cercle";
  const styleTitres = ALLOWED_FONTS.includes(body.style_titres) ? body.style_titres : "classique";
  const videoUrl = isVideoUrl(body.video_url) ? truncate(body.video_url, 300) : "";
  const rdvUrl = isHttpUrl(body.rdv_url) ? truncate(body.rdv_url, 300) : "";

  const photoDataUrl = body.photo_data_url;
  if (!photoDataUrl || typeof photoDataUrl !== "string" || !photoDataUrl.startsWith("data:image/")) {
    res.status(400).json({ error: "missing_photo" });
    return;
  }
  const match = photoDataUrl.match(/^data:image\/(jpeg|png);base64,(.+)$/);
  if (!match) {
    res.status(400).json({ error: "unsupported_photo_format" });
    return;
  }
  const ext = match[1] === "jpeg" ? "jpg" : "png";
  const base64Photo = match[2];
  const approxBytes = base64Photo.length * 0.75;
  if (approxBytes > MAX_PHOTO_BYTES) {
    res.status(400).json({ error: "photo_too_large" });
    return;
  }

  const baseSlug = slugify(`${nom}-${code}`);
  const uniqueSuffix = Date.now().toString(36);
  const slug = `${baseSlug}-${uniqueSuffix}`;
  const photoFilename = `${slug}.${ext}`;
  const branch = process.env.GITHUB_BRANCH || "main";

  const submission = {
    slug,
    submitted_at: new Date().toISOString(),
    status: "pending",
    registry_match: { nom, code, slug: regSlug, ville, verified: false },
    template,
    locked: { nom_complet: nom, canton: code, ville },
    free: {
      photo_filename: photoFilename,
      role_titre: truncate(body.role_titre, 150),
      accroche: truncate(body.accroche, 200),
      bio: truncate(body.bio, MAX_FIELD_LEN),
      citation: truncate(body.citation, 300),
      specialites,
      site_web: truncate(body.site_web, 300),
      linkedin: truncate(body.linkedin, 300),
      instagram: truncate(body.instagram, 300),
      accent_color: accentColor,
      distinctions,
      photo_frame: photoFrame,
      style_titres: styleTitres,
      adresse: truncate(body.adresse, 200),
      horaires: truncate(body.horaires, 150),
      whatsapp: truncate(body.whatsapp, 60),
      rdv_url: rdvUrl,
      video_url: videoUrl,
      galerie,
    },
    contact_email: body.contact_email,
    contact_phone: truncate(body.contact_phone, 60),
    lang,
  };

  try {
    await putFile(
      `static/vitrines/photos/${photoFilename}`,
      base64Photo,
      `Vitrine: nouvelle photo pour ${nom} (${slug})`,
      branch
    );
    const submissionBase64 = Buffer.from(JSON.stringify(submission, null, 2), "utf-8").toString("base64");
    await putFile(
      `data/vitrines/pending/${slug}.json`,
      submissionBase64,
      `Vitrine: nouvelle demande de ${nom} (${slug})`,
      branch
    );
  } catch (err) {
    res.status(502).json({ error: "github_write_failed", detail: String(err.message || err) });
    return;
  }

  res.status(200).json({ ok: true, slug });
};
