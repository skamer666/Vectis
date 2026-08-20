// Fonction serverless Vercel : reception du formulaire de verification
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
// fiche (source de verite : data/verification_contacts.json) -- sinon ce
// n'est plus un canal de confiance et la demande est refusee (le client
// doit alors choisir telephone ou document).
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
// compte (verification-confirm.js / verification-decide.js) -- c'est cette
// derniere qui fait foi une fois le compte actif.
//
// Variables d'environnement requises (Vercel, jamais dans le code) :
//   SUPABASE_SERVICE_ROLE_KEY  -- deja utilisee par review-submit.js
//   RESEND_API_KEY             -- optionnelle. Si absente, la demande reste
//                                  'pending' (palier email inclus) et Greg
//                                  peut la valider a la main depuis la page
//                                  interne /interne/verification-avocats/ ;
//                                  rien ne casse, aucun email n'est perdu.
//   RESEND_FROM_EMAIL          -- optionnelle, defaut ci-dessous. Doit être
//                                  un domaine verifie sur Resend pour que
//                                  l'envoi reussisse reellement.

const lib = require("./_verification-lib");

const ALLOWED_LANGS = ["fr", "de", "it", "en"];
const ALLOWED_METHODS = ["email", "phone", "document"];
const MAX_FILE_BYTES = 8 * 1024 * 1024;
const TOKEN_TTL_HOURS = 48;
const MIN_PASSWORD_LENGTH = 8;
const BASE_DOMAIN = "https://legatis.ch";

function truncate(s, n) {
  return (typeof s === "string" ? s.trim() : "").slice(0, n);
}

function isEmail(s) {
  return typeof s === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s);
}

function normalizeEmail(s) {
  return (s || "").trim().toLowerCase();
}

function sendVerificationEmail(toEmail, link, lang) {
  const subjects = {
    fr: "Confirmez votre identité sur Legatis",
    de: "Bestätigen Sie Ihre Identität auf Legatis",
    it: "Confermate la vostra identità su Legatis",
    en: "Confirm your identity on Legatis",
  };
  const bodies = {
    fr: `Cliquez sur ce lien pour confirmer votre identité et activer votre compte (valable ${TOKEN_TTL_HOURS}h) : ${link}`,
    de: `Klicken Sie auf diesen Link, um Ihre Identität zu bestätigen und Ihr Konto zu aktivieren (gültig ${TOKEN_TTL_HOURS}h): ${link}`,
    it: `Cliccate su questo link per confermare la vostra identità e attivare il vostro account (valido ${TOKEN_TTL_HOURS}h): ${link}`,
    en: `Click this link to confirm your identity and activate your account (valid ${TOKEN_TTL_HOURS}h): ${link}`,
  };
  return lib.sendEmail(toEmail, subjects[lang] || subjects.fr, bodies[lang] || bodies.fr);
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
      const sent = await sendVerificationEmail(accountEmail, link, lang);
      if (sent) {
        await lib.supabasePatch("verification_requests", inserted.id, { email_sent: true });
      }
      res.status(200).json({ ok: true, method: "email", id: inserted.id });
      return;
    }

    if (method === "phone") {
      const insertedPhone = await lib.supabaseInsert("verification_requests", {
        ...baseRow,
        contact_note: truncate(body.note, 300) || null,
      });
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

    res.status(200).json({ ok: true, method: "document", id: inserted.id });
  } catch (err) {
    // La ligne verification_requests n'a pas pu etre ecrite correctement :
    // on nettoie le compte pre-cree pour ne pas laisser une adresse email
    // bloquee sans aucune demande associee.
    await lib.adminDeleteUser(authUser.id).catch(function () {});
    res.status(502).json({ error: "write_failed", detail: String(err.message || err) });
  }
};
