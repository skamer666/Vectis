// Helpers partages entre les fonctions serverless api/verification-*.js.
// Prefixe "_" : Vercel n'en fait jamais une route HTTP (voir convention
// "underscore files" des Serverless Functions), ce fichier n'est donc
// accessible qu'en require() depuis les autres fonctions du dossier api/.
//
// Regroupe : la lecture de data/verification_contacts.json (email/telephone
// REELS par fiche, source de verite server-side, jamais exposee au client
// autrement que via des booleens -- voir gen_verification_contacts() dans
// build.py) et les appels a l'API REST Supabase (table + storage), toujours
// avec la service_role key, jamais la cle anon.

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const SUPABASE_URL = "https://qjiyxhsnrzahdmdvzsqi.supabase.co";
const BUCKET = "verification-documents";

let _contacts = null;
function loadContacts() {
  if (_contacts) return _contacts;
  const p = path.join(__dirname, "..", "data", "verification_contacts.json");
  _contacts = JSON.parse(fs.readFileSync(p, "utf-8"));
  return _contacts;
}

// data/contract_content.json : genere par build.py (gen_contract_export())
// a partir de website_offer_content.CONTRACT -- utilise par
// website-offer-decision.js pour envoyer au Client une copie du contrat
// "site web gratuit" qu'il vient d'accepter.
let _contractContent = null;
function loadContractContent() {
  if (_contractContent) return _contractContent;
  const p = path.join(__dirname, "..", "data", "contract_content.json");
  _contractContent = JSON.parse(fs.readFileSync(p, "utf-8"));
  return _contractContent;
}

function serviceHeaders(extra) {
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  return Object.assign(
    {
      apikey: key,
      Authorization: `Bearer ${key}`,
    },
    extra || {}
  );
}

async function supabaseInsert(table, row) {
  const resp = await fetch(`${SUPABASE_URL}/rest/v1/${table}`, {
    method: "POST",
    headers: serviceHeaders({ "Content-Type": "application/json", Prefer: "return=representation" }),
    body: JSON.stringify(row),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Supabase insert failed: ${resp.status} ${text.slice(0, 300)}`);
  }
  const rows = await resp.json();
  return rows[0];
}

async function supabasePatch(table, id, patch) {
  const resp = await fetch(`${SUPABASE_URL}/rest/v1/${table}?id=eq.${encodeURIComponent(id)}`, {
    method: "PATCH",
    headers: serviceHeaders({ "Content-Type": "application/json", Prefer: "return=minimal" }),
    body: JSON.stringify(patch),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Supabase patch failed: ${resp.status} ${text.slice(0, 300)}`);
  }
}

async function supabaseSelect(table, query) {
  const resp = await fetch(`${SUPABASE_URL}/rest/v1/${table}?${query}`, {
    headers: serviceHeaders(),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Supabase select failed: ${resp.status} ${text.slice(0, 300)}`);
  }
  return resp.json();
}

// `query` doit inclure le(s) filtre(s) (ex. "id=eq.<uuid>") -- pas de DELETE
// sans filtre expose ici, pour rendre un appel accidentellement non filtre
// impossible a exprimer avec cette fonction.
async function supabaseDelete(table, query) {
  const resp = await fetch(`${SUPABASE_URL}/rest/v1/${table}?${query}`, {
    method: "DELETE",
    headers: serviceHeaders({ Prefer: "return=minimal" }),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Supabase delete failed: ${resp.status} ${text.slice(0, 300)}`);
  }
}

async function storageUpload(objectPath, buffer, mime) {
  const resp = await fetch(`${SUPABASE_URL}/storage/v1/object/${BUCKET}/${objectPath}`, {
    method: "POST",
    headers: serviceHeaders({ "Content-Type": mime, "x-upsert": "false" }),
    body: buffer,
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Storage upload failed: ${resp.status} ${text.slice(0, 300)}`);
  }
}

// `bucket` optionnel (par defaut BUCKET = "verification-documents") : garde
// la compatibilite avec les appels existants (documents/selfies) tout en
// permettant de nettoyer d'autres buckets prives/publics (ex. "lawyer-photos"
// depuis api/reset-test-account.js).
async function storageDelete(objectPaths, bucket) {
  const paths = objectPaths.filter(Boolean);
  if (!paths.length) return;
  const resp = await fetch(`${SUPABASE_URL}/storage/v1/object/${bucket || BUCKET}`, {
    method: "DELETE",
    headers: serviceHeaders({ "Content-Type": "application/json" }),
    body: JSON.stringify({ prefixes: paths }),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Storage delete failed: ${resp.status} ${text.slice(0, 300)}`);
  }
}

async function storageSignedUrl(objectPath, expiresInSeconds) {
  const resp = await fetch(`${SUPABASE_URL}/storage/v1/object/sign/${BUCKET}/${objectPath}`, {
    method: "POST",
    headers: serviceHeaders({ "Content-Type": "application/json" }),
    body: JSON.stringify({ expiresIn: expiresInSeconds }),
  });
  if (!resp.ok) return null;
  const data = await resp.json();
  return data.signedURL ? `${SUPABASE_URL}/storage/v1${data.signedURL}` : null;
}

function randomToken() {
  return crypto.randomBytes(32).toString("hex");
}

function hashToken(rawToken) {
  return crypto.createHash("sha256").update(rawToken).digest("hex");
}

// Comparaison en temps constant : evite qu'un attaquant deduise le hash
// stocke bit par bit en mesurant le temps de reponse (timing attack) sur
// l'endpoint public api/verification-confirm.js.
function safeEqual(a, b) {
  const bufA = Buffer.from(a || "", "utf-8");
  const bufB = Buffer.from(b || "", "utf-8");
  if (bufA.length !== bufB.length) return false;
  return crypto.timingSafeEqual(bufA, bufB);
}

const MIME_EXT = {
  "image/jpeg": "jpg",
  "image/png": "png",
  "application/pdf": "pdf",
};

const DEFAULT_FROM = "Legatis <verification@legatis.ch>";

// Envoi d'email generique via Resend. Degrade gracieusement : si
// RESEND_API_KEY n'est pas configuree (variable d'environnement Vercel,
// jamais dans le code), la fonction retourne simplement false -- aucune
// exception, rien ne casse. Utilise pour le lien de confirmation email
// (verification-request.js) et pour le lien de creation de compte
// (verification-decide.js, verification-confirm.js indirectement via la
// page de confirmation).
//
// `html` est optionnel : sans lui, Resend n'envoie que la version texte, et
// certains clients mail affichent alors l'URL comme du texte brut au lieu
// d'un vrai lien cliquable. Des que le message contient un lien (lien de
// confirmation, lien de connexion...), l'appelant doit fournir `html` avec
// un <a href> reel -- `text` reste toujours envoye en parallele comme
// version de repli pour les clients qui l'exigent.
async function sendEmail(toEmail, subject, text, html) {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey || !toEmail) return false;
  try {
    const payload = {
      from: process.env.RESEND_FROM_EMAIL || DEFAULT_FROM,
      to: [toEmail],
      subject,
      text,
    };
    if (html) payload.html = html;
    const resp = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${apiKey}`, "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    return resp.ok;
  } catch (e) {
    return false;
  }
}

function checkAdminToken(req) {
  const expected = process.env.VERIFICATION_ADMIN_TOKEN;
  const given = req.headers["x-admin-token"];
  return !!expected && !!given && safeEqual(String(given), String(expected));
}

// -- Connexion admin (vrai compte, remplace le jeton partage) --------------
//
// Demande de Greg le 20/08/2026 : le panneau admin (pages /interne/*) doit
// se deverrouiller avec un vrai compte (email + mot de passe), pas un jeton
// unique copie-colle. On reutilise Supabase Auth exactement comme pour les
// comptes avocat (voir templates/connexion.html) plutot que d'inventer un
// systeme separe : le client se connecte cote client avec la cle anon
// (POST {SUPABASE_URL}/auth/v1/token?grant_type=password), recupere un
// access_token, et l'envoie ensuite en "Authorization: Bearer <token>" sur
// chaque appel admin. Ici, cote serveur, on ne fait JAMAIS confiance au
// contenu du token sans le revalider aupres de Supabase (GET /auth/v1/user
// avec ce token) -- ca confirme a la fois que le token est authentique et
// n'est pas expire/revoque, et ca renvoie l'email associe. On accepte
// ensuite uniquement les emails listes dans ADMIN_EMAILS (liste blanche
// separee par des virgules) : avoir un compte Supabase Auth valide ne
// suffit pas a etre admin, seuls des comptes explicitement autorises le
// sont (ex: un avocat qui active son propre compte ne doit jamais pouvoir
// se servir de son token pour acceder au panneau admin).
// Revalide un token Supabase Auth (jamais fait confiance a son contenu sans
// verification aupres de Supabase) et renvoie {id, email} de l'utilisateur
// authentifie, ou null si le token est absent/invalide/expire. Partage par
// checkAdminAuth ci-dessous (qui filtre ensuite par ADMIN_EMAILS) et par
// getLawyerAccount (qui filtre par lawyer_accounts.user_id) -- factorise
// pour que la revalidation aupres de Supabase ne soit ecrite qu'une fois.
async function getAuthUser(req) {
  const authHeader = req.headers["authorization"] || "";
  const match = /^Bearer\s+(.+)$/i.exec(authHeader);
  if (!match) return null;
  const token = match[1].trim();
  if (!token) return null;

  try {
    const resp = await fetch(`${SUPABASE_URL}/auth/v1/user`, {
      headers: {
        Authorization: `Bearer ${token}`,
        apikey: process.env.SUPABASE_SERVICE_ROLE_KEY,
      },
    });
    if (!resp.ok) return null;
    const user = await resp.json();
    if (!user || !user.id) return null;
    return { id: user.id, email: String(user.email || "").toLowerCase() };
  } catch (e) {
    return null;
  }
}

async function checkAdminAuth(req) {
  const adminEmails = String(process.env.ADMIN_EMAILS || "")
    .split(",")
    .map((e) => e.trim().toLowerCase())
    .filter(Boolean);
  if (!adminEmails.length) return false;

  const user = await getAuthUser(req);
  return !!user && !!user.email && adminEmails.includes(user.email);
}

// Authentifie un avocat (pas Greg) : revalide son token aupres de Supabase
// puis verifie qu'un compte avocat actif existe bien pour cet utilisateur
// (lawyer_accounts.user_id) -- voir supabase_schema.sql. Renvoie la ligne
// lawyer_accounts (canton, avocat_slug, avocat_nom, avocat_url) + l'email du
// compte, ou null si le token est invalide ou si l'utilisateur n'a pas
// (encore) de compte avocat actif. Utilise par api/lawyer-website-offer.js.
async function getLawyerAccount(req) {
  const user = await getAuthUser(req);
  if (!user) return null;
  const rows = await supabaseSelect(
    "lawyer_accounts",
    `user_id=eq.${encodeURIComponent(user.id)}&select=canton,avocat_slug,avocat_nom,avocat_url`
  );
  const row = rows[0];
  if (!row) return null;
  return Object.assign({}, row, { user_id: user.id, email: user.email });
}

// -- Comptes avocat : creation "en attente" au moment de la demande --------
//
// Le mot de passe est desormais choisi des la demande de verification (voir
// api/verification-request.js), pas apres coup via un lien separe. Pour ne
// JAMAIS avoir a stocker ce mot de passe nous-memes (ni en clair ni hache
// maison), on cree tout de suite le compte Supabase Auth correspondant,
// mais avec email_confirm=false : Supabase gere et securise le mot de passe
// des cette premiere requete, et le compte reste inutilisable (connexion
// refusee) tant que email_confirm n'est pas passe a true. C'est cette
// bascule qui fait office de "creation reelle" du compte, uniquement au
// moment ou l'identite est confirmee (lien email clique, ou decision de
// Greg) -- voir adminConfirmUser ci-dessous, appelee depuis
// verification-confirm.js et verification-decide.js. Si la demande est
// refusee, adminDeleteUser libere l'adresse pour une nouvelle tentative.

async function adminCreateUser(email, password) {
  const resp = await fetch(`${SUPABASE_URL}/auth/v1/admin/users`, {
    method: "POST",
    headers: serviceHeaders({ "Content-Type": "application/json" }),
    body: JSON.stringify({ email, password, email_confirm: false }),
  });
  if (!resp.ok) {
    const text = await resp.text();
    const alreadyRegistered = resp.status === 422 || /already.*registered/i.test(text);
    const err = new Error(`Auth admin create failed: ${resp.status} ${text.slice(0, 300)}`);
    err.alreadyRegistered = alreadyRegistered;
    throw err;
  }
  return resp.json();
}

async function adminConfirmUser(userId) {
  const resp = await fetch(`${SUPABASE_URL}/auth/v1/admin/users/${encodeURIComponent(userId)}`, {
    method: "PUT",
    headers: serviceHeaders({ "Content-Type": "application/json" }),
    body: JSON.stringify({ email_confirm: true }),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error(`Auth admin confirm failed: ${resp.status} ${text.slice(0, 300)}`);
  }
}

async function adminDeleteUser(userId) {
  if (!userId) return;
  const resp = await fetch(`${SUPABASE_URL}/auth/v1/admin/users/${encodeURIComponent(userId)}`, {
    method: "DELETE",
    headers: serviceHeaders(),
  });
  // 404 = deja supprime / jamais cree -- pas une erreur pour un appel de
  // nettoyage. On ne fait jamais echouer la decision de Greg pour ca.
  if (!resp.ok && resp.status !== 404) {
    const text = await resp.text();
    throw new Error(`Auth admin delete failed: ${resp.status} ${text.slice(0, 300)}`);
  }
}

// -- Offre "site web gratuit" : email du contrat au Client + notification a
// Greg -- partages entre website-offer-decision.js (acceptation juste apres
// la creation du compte) et lawyer-website-offer.js (demande depuis l'espace
// avocat une fois connecte, voir templates/mon_profil.html) pour ne jamais
// dupliquer le texte de ces emails dans 4 langues a deux endroits.

const SITE_BASE_DOMAIN = "https://legatis.ch";
const ADMIN_NOTIFY_EMAIL = "gregoiregiuliano@hotmail.com";
const ADMIN_VERIFICATION_URL = `${SITE_BASE_DOMAIN}/interne/verification-avocats/`;

function escapeHtml(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}

const CONTRACT_EMAIL_STRINGS = {
  fr: {
    subject: "Votre contrat Legatis - Site internet gratuit",
    intro: (nom) => `Bonjour ${nom}\n\nVous avez accepté notre offre de création gratuite de votre site internet professionnel. Vous trouverez ci-dessous une copie complète du contrat que vous venez d'accepter, pour vos archives.\n\nNous revenons vers vous prochainement pour démarrer la création de votre site.\n\nCordialement,\nL'équipe Legatis`,
  },
  de: {
    subject: "Ihr Legatis-Vertrag - Kostenlose Website",
    intro: (nom) => `Guten Tag ${nom}\n\nSie haben unser Angebot zur kostenlosen Erstellung Ihrer professionellen Website angenommen. Nachfolgend finden Sie eine vollständige Kopie des Vertrags, den Sie soeben akzeptiert haben, für Ihre Unterlagen.\n\nWir melden uns in Kürze bei Ihnen, um mit der Erstellung Ihrer Website zu beginnen.\n\nFreundliche Grüsse\nDas Legatis-Team`,
  },
  it: {
    subject: "Il vostro contratto Legatis - Sito internet gratuito",
    intro: (nom) => `Gentile ${nom}\n\nAvete accettato la nostra offerta di creazione gratuita del vostro sito internet professionale. Di seguito trovate una copia completa del contratto che avete appena accettato, per i vostri archivi.\n\nVi ricontatteremo a breve per avviare la creazione del vostro sito.\n\nCordiali saluti\nIl team Legatis`,
  },
  en: {
    subject: "Your Legatis contract - Free website",
    intro: (nom) => `Hello ${nom}\n\nYou have accepted our offer to build your professional website free of charge. Below is a complete copy of the contract you just accepted, for your records.\n\nWe will get back to you shortly to start building your website.\n\nBest regards,\nThe Legatis team`,
  },
};

function contractPlainText(contract) {
  const lines = [contract.title, "", contract.parties_label, ""];
  contract.preamble.forEach(function (p) { lines.push(p, ""); });
  contract.articles.forEach(function (a) {
    lines.push(a.heading, "");
    a.paragraphs.forEach(function (p) { lines.push(p, ""); });
  });
  return lines.join("\n");
}

function contractHtml(contract) {
  let html = `<h2>${escapeHtml(contract.title)}</h2><p>${escapeHtml(contract.parties_label)}</p>`;
  contract.preamble.forEach(function (p) { html += `<p>${escapeHtml(p)}</p>`; });
  contract.articles.forEach(function (a) {
    html += `<h3>${escapeHtml(a.heading)}</h3>`;
    a.paragraphs.forEach(function (p) { html += `<p>${escapeHtml(p)}</p>`; });
  });
  return html;
}

function sendContractToClient(accountEmail, nom, lang) {
  const strings = CONTRACT_EMAIL_STRINGS[lang] || CONTRACT_EMAIL_STRINGS.fr;
  const { contract } = loadContractContent();
  const c = contract[lang] || contract.fr;
  const intro = strings.intro(nom || "");
  const text = `${intro}\n\n----------\n\n${contractPlainText(c)}`;
  const html = `<p>${escapeHtml(intro).replace(/\n/g, "<br>")}</p><hr>${contractHtml(c)}`;
  return sendEmail(accountEmail, strings.subject, text, html).catch(function () { return false; });
}

// eventLabel : courte description en francais de l'origine de la demande
// (ex. "acceptée à la création du compte" ou "demandée depuis l'espace
// avocat"), affichee dans l'email a Greg pour qu'il sache d'ou ca vient.
function notifyAdminFreeWebsiteInterest({ eventLabel, avocatNom, canton, avocatUrl, accountEmail }) {
  const subject = `Site gratuit ${eventLabel} - ${avocatNom} (${canton})`;
  const ficheUrl = `${SITE_BASE_DOMAIN}${avocatUrl}`;
  const text = `${avocatNom} (${canton}) : offre de site internet gratuit ${eventLabel}.\n\nFiche : ${ficheUrl}\nEmail du compte : ${accountEmail}\n\nÀ traiter sur ${ADMIN_VERIFICATION_URL}`;
  const html = `<p>${escapeHtml(avocatNom)} (${escapeHtml(canton)}) : offre de site internet gratuit ${escapeHtml(eventLabel)}.</p><p>Fiche : <a href="${ficheUrl}">${escapeHtml(ficheUrl)}</a></p><p>Email du compte : ${escapeHtml(accountEmail)}</p><p>À traiter sur <a href="${ADMIN_VERIFICATION_URL}">${escapeHtml(ADMIN_VERIFICATION_URL)}</a></p>`;
  return sendEmail(ADMIN_NOTIFY_EMAIL, subject, text, html).catch(function () { return false; });
}

module.exports = {
  SUPABASE_URL,
  BUCKET,
  MIME_EXT,
  loadContacts,
  loadContractContent,
  supabaseInsert,
  supabasePatch,
  supabaseSelect,
  supabaseDelete,
  storageUpload,
  storageDelete,
  storageSignedUrl,
  randomToken,
  hashToken,
  safeEqual,
  checkAdminToken,
  checkAdminAuth,
  getAuthUser,
  getLawyerAccount,
  sendEmail,
  escapeHtml,
  sendContractToClient,
  notifyAdminFreeWebsiteInterest,
  adminCreateUser,
  adminConfirmUser,
  adminDeleteUser,
};
