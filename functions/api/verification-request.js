// Fonction Cloudflare Pages : reception du formulaire de verification
// d'identite ET de creation de compte (templates/verification_demande.html).
// Depuis cette version, le mot de passe est choisi des cette premiere etape
// -- "creer son compte" est la toute premiere chose que fait un avocat qui
// revendique une fiche, avant meme que son identite ne soit confirmee. Le
// compte Supabase Auth correspondant est cree tout de suite mais reste
// bloque (email_confirm=false) : voir adminCreateUser/adminConfirmUser dans
// _verification-lib.js. Il n'est jamais actif tant que l'identite n'a pas
// ete confirmee (lien email clique, ou decision de Greg).
//
// Le PALIER de verification (email/telephone/document) n'est plus impose
// automatiquement au demandeur : on affiche toujours toutes les options
// disponibles (email si connu, telephone si connu, document dans tous les
// cas) et c'est le demandeur qui choisit -- utile s'il pense que l'email ou
// le telephone enregistre est errone. Seule contrainte imposee cote
// serveur (jamais cote client) : pour choisir le palier email, l'email de
// compte fourni doit correspondre EXACTEMENT a celui deja publie pour cette
// fiche (source de verite : data/verification_contacts.json, importe
// statiquement -- voir _verification-lib.js et CLOUDFLARE_MIGRATION.md)
// -- sinon ce n'est plus un canal de confiance et la demande est refusee (le
// client doit alors choisir telephone ou document).
//
// Palier document : upload direct du navigateur vers ce endpoint (fichiers
// en base64 dans le JSON, 8 Mo max chacun avant encodage) puis relai vers
// le bucket prive verification-documents via la service_role key -- jamais
// d'ecriture directe navigateur -> Supabase Storage avec une cle publique.
//
// Consentement email marketing : case a cocher FACULTATIVE et decochee par
// defaut sur le formulaire, distincte du consentement d'identite/creation
// de compte (qui reste obligatoire). Stockee ici (marketing_consent) puis
// recopiee sur la ligne lawyer_accounts au moment de l'activation du
// compte (verification-confirm.js / admin-decide.js kind=verification) -- c'est cette
// derniere qui fait foi une fois le compte actif.
//
// Variables d'environnement requises :
//   SUPABASE_SERVICE_ROLE_KEY  -- deja utilisee par review-submit.js
//   RESEND_API_KEY             -- optionnelle. Si absente, la demande reste
//                                  'pending' (palier email inclus) et Greg
//                                  peut la valider a la main depuis la page
//                                  interne /interne/verification-avocats/ ;
//                                  rien ne casse, aucun email n'est perdu.
//   RESEND_FROM_EMAIL          -- optionnelle, defaut ci-dessous. Doit être
//                                  un domaine verifie sur Resend pour que
//                                  l'envoi reussisse reellement.
//
// Notification admin : chaque demande (quel que soit le palier) envoie aussi
// un email a ADMIN_NOTIFY_EMAIL (Greg) via notifyAdminNewRequest() -- best
// effort comme tout envoi d'email ici, ne bloque jamais la demande.
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
// Buffer importe explicitement depuis node:buffer (fourni par nodejs_compat,
// voir wrangler.toml) pour decoder les fichiers base64 -- meme API que sous
// Node/Vercel, aucun changement de comportement.
import { wrapVercelHandler } from "./_shim.js";
import * as lib from "./_verification-lib.js";
import { checkRateLimit, clientIp } from "./_rate-limit.js";
import { Buffer } from "node:buffer";

const ALLOWED_LANGS = ["fr", "de", "it", "en"];
const ALLOWED_METHODS = ["email", "phone", "document"];
const MAX_FILE_BYTES = 8 * 1024 * 1024;
const TOKEN_TTL_HOURS = 48;
const MIN_PASSWORD_LENGTH = 8;
const BASE_DOMAIN = "https://legatis.ch";

// Adresse perso de Greg (voir aussi account_content.py error_generic) --
// notifiee sur CHAQUE demande de verification, quel que soit le palier, pour
// qu'il ne depende pas de consulter /interne/verification-avocats/ a
// intervalles reguliers pour savoir qu'une demande est arrivee. Palier email
// = deja auto-traite si l'avocat clique le lien (rien a faire, note dans le
// mail) ; phone/document = attend une action de sa part.
const ADMIN_NOTIFY_EMAIL = "gregoiregiuliano@hotmail.com";
const ADMIN_URL = `${BASE_DOMAIN}/interne/verification-avocats/`;
const METHOD_LABELS_FR = { email: "email (auto-validé si le lien est cliqué)", phone: "téléphone (à rappeler)", document: "document (à examiner)" };

// Toutes les valeurs interpolees dans les corps HTML ci-dessous (nom,
// numero, notes libres...) viennent du registre officiel ou d'un champ
// texte saisi par le demandeur -- jamais garanties exemptes de caracteres
// HTML. echappees systematiquement avant insertion dans un corps HTML.
function escapeHtml(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}

function notifyAdminNewRequest({ method, avocatNom, canton, avocatUrl, accountEmail, telephone, note }) {
  const subject = `Nouvelle demande de vérification - ${avocatNom} (${canton})`;
  const ficheUrl = `${BASE_DOMAIN}${avocatUrl}`;
  let body = `Palier : ${METHOD_LABELS_FR[method] || method}\nFiche : ${ficheUrl}\nEmail du compte : ${accountEmail}`;
  let html = `<p>Palier : ${escapeHtml(METHOD_LABELS_FR[method] || method)}</p><p>Fiche : <a href="${ficheUrl}">${escapeHtml(ficheUrl)}</a></p><p>Email du compte : ${escapeHtml(accountEmail)}</p>`;
  if (method === "phone") {
    body += `\nNuméro à appeler (déjà publié sur la fiche) : ${telephone || "(inconnu)"}`;
    html += `<p>Numéro à appeler (déjà publié sur la fiche) : ${escapeHtml(telephone || "(inconnu)")}</p>`;
    if (note) {
      body += `\nDisponibilités indiquées : ${note}`;
      html += `<p>Disponibilités indiquées : ${escapeHtml(note)}</p>`;
    }
  }
  body += `\n\nÀ traiter sur ${ADMIN_URL}`;
  html += `<p>À traiter sur <a href="${ADMIN_URL}">${escapeHtml(ADMIN_URL)}</a></p>`;
  // Best-effort, comme tous les envois d'email de ce depot (voir sendEmail) :
  // ne doit jamais faire echouer la demande elle-meme si Resend est absent
  // ou en erreur -- la ligne verification_requests reste de toute facon
  // consultable sur la page interne.
  return lib.sendEmail(ADMIN_NOTIFY_EMAIL, subject, body, html).catch(function () { return false; });
}

function truncate(s, n) {
  return (typeof s === "string" ? s.trim() : "").slice(0, n);
}

function isEmail(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
}

function normalizeEmail(s) {
  return (s || "").trim().toLowerCase();
}

function sendVerificationEmail(toEmail, nom, link, lang) {
  const subjects = {
    fr: "Confirmez votre identité sur Legatis",
    de: "Bestätigen Sie Ihre Identität auf Legatis",
    it: "Confermate la vostra identità su Legatis",
    en: "Confirm your identity on Legatis",
  };
  // Personnalise (nom de l'avocat/etude) et explique en une phrase POURQUOI
  // ce mail arrive, avant le lien -- un lien nu sans contexte ni signature
  // ressemble a du phishing, surtout pour un premier contact avec Legatis.
  const bodies = {
    fr: `Bonjour ${nom}\n\nVous avez demandé à créer votre compte Legatis pour votre fiche sur l'annuaire. Cliquez sur ce lien pour confirmer votre identité et activer votre compte (valable ${TOKEN_TTL_HOURS}h) :\n${link}\n\nSi vous n'êtes pas à l'origine de cette demande, ignorez simplement cet email.\n\nCordialement,\nL'équipe Legatis`,
    de: `Guten Tag ${nom}\n\nSie haben beantragt, Ihr Legatis-Konto für Ihren Eintrag im Verzeichnis zu erstellen. Klicken Sie auf diesen Link, um Ihre Identität zu bestätigen und Ihr Konto zu aktivieren (gültig ${TOKEN_TTL_HOURS}h):\n${link}\n\nFalls Sie diese Anfrage nicht gestellt haben, ignorieren Sie diese E-Mail einfach.\n\nFreundliche Grüsse\nDas Legatis-Team`,
    it: `Gentile ${nom}\n\nAvete richiesto di creare il vostro account Legatis per la vostra scheda sull'annuario. Cliccate su questo link per confermare la vostra identità e attivare il vostro account (valido ${TOKEN_TTL_HOURS}h):\n${link}\n\nSe non siete voi all'origine di questa richiesta, ignorate semplicemente questa email.\n\nCordiali saluti\nIl team Legatis`,
    en: `Hello ${nom}\n\nYou requested to create your Legatis account for your directory listing. Click this link to confirm your identity and activate your account (valid ${TOKEN_TTL_HOURS}h):\n${link}\n\nIf you didn't make this request, simply ignore this email.\n\nBest regards,\nThe Legatis team`,
  };
  // Version HTML avec un vrai bouton <a href> -- la version texte seule
  // (bodies ci-dessus) fait apparaitre le lien comme du texte brut non
  // cliquable dans la plupart des clients mail. Le lien est aussi repete
  // en clair sous le bouton pour les clients qui n'affichent pas le HTML.
  const btnStyle = "display:inline-block;padding:12px 24px;background:#111;color:#fff;text-decoration:none;border-radius:6px;font-weight:600;";
  const safeName = escapeHtml(nom);
  const safeLink = escapeHtml(link);
  const ctaLabels = { fr: "Confirmer mon identité", de: "Identität bestätigen", it: "Confermare la mia identità", en: "Confirm my identity" };
  const htmlBodies = {
    fr: `<p>Bonjour ${safeName}</p><p>Vous avez demandé à créer votre compte Legatis pour votre fiche sur l'annuaire. Cliquez sur le bouton ci-dessous pour confirmer votre identité et activer votre compte (valable ${TOKEN_TTL_HOURS}h) :</p><p><a href="${link}" style="${btnStyle}">${ctaLabels.fr}</a></p><p>Ou copiez ce lien dans votre navigateur : <a href="${link}">${safeLink}</a></p><p>Si vous n'êtes pas à l'origine de cette demande, ignorez simplement cet email.</p><p>Cordialement,<br>L'équipe Legatis</p>`,
    de: `<p>Guten Tag ${safeName}</p><p>Sie haben beantragt, Ihr Legatis-Konto für Ihren Eintrag im Verzeichnis zu erstellen. Klicken Sie auf die Schaltfläche unten, um Ihre Identität zu bestätigen und Ihr Konto zu aktivieren (gültig ${TOKEN_TTL_HOURS}h):</p><p><a href="${link}" style="${btnStyle}">${ctaLabels.de}</a></p><p>Oder kopieren Sie diesen Link in Ihren Browser: <a href="${link}">${safeLink}</a></p><p>Falls Sie diese Anfrage nicht gestellt haben, ignorieren Sie diese E-Mail einfach.</p><p>Freundliche Grüsse<br>Das Legatis-Team</p>`,
    it: `<p>Gentile ${safeName}</p><p>Avete richiesto di creare il vostro account Legatis per la vostra scheda sull'annuario. Cliccate sul pulsante qui sotto per confermare la vostra identità e attivare il vostro account (valido ${TOKEN_TTL_HOURS}h):</p><p><a href="${link}" style="${btnStyle}">${ctaLabels.it}</a></p><p>Oppure copiate questo link nel vostro browser: <a href="${link}">${safeLink}</a></p><p>Se non siete voi all'origine di questa richiesta, ignorate semplicemente questa email.</p><p>Cordiali saluti<br>Il team Legatis</p>`,
    en: `<p>Hello ${safeName}</p><p>You requested to create your Legatis account for your directory listing. Click the button below to confirm your identity and activate your account (valid ${TOKEN_TTL_HOURS}h):</p><p><a href="${link}" style="${btnStyle}">${ctaLabels.en}</a></p><p>Or copy this link into your browser: <a href="${link}">${safeLink}</a></p><p>If you didn't make this request, simply ignore this email.</p><p>Best regards,<br>The Legatis team</p>`,
  };
  return lib.sendEmail(toEmail, subjects[lang] || subjects.fr, bodies[lang] || bodies.fr, htmlBodies[lang] || htmlBodies.fr);
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

  // 5 demandes / 15 min par IP : cree un compte + envoie des emails, action
  // rare pour un utilisateur legitime.
  if (!(await checkRateLimit(req, "verification-request", 5, 900))) {
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

  // Honeypot anti-spam, meme principe que review-submit.js.
  if (truncate(body.website, 50)) {
    res.status(200).json({ ok: true, method: "ignored" });
    return;
  }

  const lang = ALLOWED_LANGS.includes(body.lang) ? body.lang : "fr";
  const registryMatch = body.registry_match || {};
  const avocatNom = truncate(registryMatch.nom, 200);
  const canton = truncate(registryMatch.code, 4).toUpperCase();
  const avocatSlug = truncate(registryMatch.slug, 200);
  const avocatUrl = truncate(registryMatch.url, 400);

  if (!avocatNom || !canton || !avocatSlug || !avocatUrl) {
    res.status(400).json({ error: "missing_registry_match" });
    return;
  }

  const accountEmail = normalizeEmail(body.account_email);
  if (!isEmail(accountEmail)) {
    res.status(400).json({ error: "invalid_account_email" });
    return;
  }
  const password = typeof body.password === "string" ? body.password : "";
  if (password.length < MIN_PASSWORD_LENGTH) {
    res.status(400).json({ error: "password_too_short" });
    return;
  }

  const method = ALLOWED_METHODS.includes(body.method) ? body.method : null;
  if (!method) {
    res.status(400).json({ error: "invalid_method" });
    return;
  }

  // Consentement facultatif pour les emails Legatis hors creation de
  // compte (actualites, conseils, etc.) -- distinct du consentement
  // d'identite/creation de compte, jamais coche par defaut cote client.
  const marketingConsent = body.marketing_consent === true;
  // IP au moment du consentement (preuve, voir supabase_schema.sql) --
  // uniquement si la case est cochee, meme principe de minimisation que
  // review_reminder_consent_ip dans lead-capture.js.
  const marketingConsentIp = marketingConsent ? clientIp(req) : null;

  let contacts;
  try {
    contacts = lib.loadContacts();
  } catch (e) {
    res.status(500).json({ error: "contacts_unavailable" });
    return;
  }
  const known = contacts[`${canton}/${avocatSlug}`] || {};

  // Le palier choisi doit rester possible : email seulement si un email est
  // deja publie ET que celui fourni pour le compte correspond exactement
  // (canal de confiance) ; telephone seulement si un numero est deja
  // publie (on appelle toujours ce numero-la, jamais un autre) ; document
  // est toujours disponible, y compris quand un email/telephone est connu
  // -- le demandeur peut prefer cette voie s'il pense que ses coordonnees
  // enregistrees sont erronees.
  if (method === "email") {
    if (!known.email || normalizeEmail(known.email) !== accountEmail) {
      res.status(400).json({ error: "email_mismatch" });
      return;
    }
  } else if (method === "phone") {
    if (!known.telephone) {
      res.status(400).json({ error: "method_unavailable" });
      return;
    }
  }

  // Compte pre-cree mais bloque (email_confirm=false) : Supabase securise
  // le mot de passe des cette etape, nous ne le stockons jamais nous-memes.
  // Il ne devient utilisable qu'a la confirmation de l'identite.
  let authUser;
  try {
    authUser = await lib.adminCreateUser(accountEmail, password);
  } catch (e) {
    if (e.alreadyRegistered) {
      res.status(409).json({ error: "email_already_registered" });
      return;
    }
    res.status(502).json({ error: "account_precreate_failed", detail: String(e.message || e) });
    return;
  }

  const baseRow = {
    method,
    canton,
    avocat_slug: avocatSlug,
    avocat_nom: avocatNom,
    avocat_url: avocatUrl,
    lang,
    account_email: accountEmail,
    pending_user_id: authUser.id,
    marketing_consent: marketingConsent,
    marketing_consent_ip: marketingConsentIp,
  };

  try {
    if (method === "email") {
      const rawToken = lib.randomToken();
      const expiresAt = new Date(Date.now() + TOKEN_TTL_HOURS * 3600 * 1000).toISOString();
      const inserted = await lib.supabaseInsert("verification_requests", {
        ...baseRow,
        token_hash: lib.hashToken(rawToken),
        token_expires_at: expiresAt,
      });
      const link = `${BASE_DOMAIN}/api/verification-confirm?rid=${inserted.id}&token=${rawToken}&lang=${lang}`;
      const sent = await sendVerificationEmail(accountEmail, avocatNom, link, lang);
      if (sent) {
        await lib.supabasePatch("verification_requests", inserted.id, { email_sent: true });
      }
      await notifyAdminNewRequest({ method, avocatNom, canton, avocatUrl, accountEmail });
      res.status(200).json({ ok: true, method: "email", id: inserted.id });
      return;
    }

    if (method === "phone") {
      const contactNote = truncate(body.note, 300) || null;
      const insertedPhone = await lib.supabaseInsert("verification_requests", {
        ...baseRow,
        contact_note: contactNote,
      });
      await notifyAdminNewRequest({ method, avocatNom, canton, avocatUrl, accountEmail, telephone: known.telephone, note: contactNote });
      res.status(200).json({ ok: true, method: "phone", id: insertedPhone.id });
      return;
    }

    // method === "document"
    const docMime = body.document_mime;
    const selfieMime = body.selfie_mime;
    if (!lib.MIME_EXT[docMime] || !lib.MIME_EXT[selfieMime] || selfieMime === "application/pdf") {
      await lib.adminDeleteUser(authUser.id);
      res.status(400).json({ error: "invalid_file_type" });
      return;
    }
    if (typeof body.document_base64 !== "string" || typeof body.selfie_base64 !== "string") {
      await lib.adminDeleteUser(authUser.id);
      res.status(400).json({ error: "missing_files" });
      return;
    }
    const docBuffer = Buffer.from(body.document_base64, "base64");
    const selfieBuffer = Buffer.from(body.selfie_base64, "base64");
    if (docBuffer.length > MAX_FILE_BYTES || selfieBuffer.length > MAX_FILE_BYTES) {
      await lib.adminDeleteUser(authUser.id);
      res.status(400).json({ error: "file_too_large" });
      return;
    }
    if (!docBuffer.length || !selfieBuffer.length) {
      await lib.adminDeleteUser(authUser.id);
      res.status(400).json({ error: "missing_files" });
      return;
    }

    const inserted = await lib.supabaseInsert("verification_requests", baseRow);

    const docPath = `${inserted.id}/document.${lib.MIME_EXT[docMime]}`;
    const selfiePath = `${inserted.id}/selfie.${lib.MIME_EXT[selfieMime]}`;
    await lib.storageUpload(docPath, docBuffer, docMime);
    await lib.storageUpload(selfiePath, selfieBuffer, selfieMime);
    await lib.supabasePatch("verification_requests", inserted.id, {
      document_path: docPath,
      selfie_path: selfiePath,
    });

    await notifyAdminNewRequest({ method, avocatNom, canton, avocatUrl, accountEmail });
    res.status(200).json({ ok: true, method: "document", id: inserted.id });
  } catch (err) {
    // La ligne verification_requests n'a pas pu etre ecrite correctement :
    // on nettoie le compte pre-cree pour ne pas laisser une adresse email
    // bloquee sans aucune demande associee.
    await lib.adminDeleteUser(authUser.id).catch(function () {});
    res.status(502).json({ error: "write_failed", detail: String(err.message || err) });
  }
}

export const onRequest = wrapVercelHandler(handler);
