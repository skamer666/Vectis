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
async function checkAdminAuth(req) {
  const authHeader = req.headers["authorization"] || "";
  const match = /^Bearer\s+(.+)$/i.exec(authHeader);
  if (!match) return false;
  const token = match[1].trim();
  if (!token) return false;

  const adminEmails = String(process.env.ADMIN_EMAILS || "")
    .split(",")
    .map((e) => e.trim().toLowerCase())
    .filter(Boolean);
  if (!adminEmails.length) return false;

  try {
    const resp = await fetch(`${SUPABASE_URL}/auth/v1/user`, {
      headers: {
        Authorization: `Bearer ${token}`,
        apikey: process.env.SUPABASE_SERVICE_ROLE_KEY,
      },
    });
    if (!resp.ok) return false;
    const user = await resp.json();
    const email = String(user && user.email ? user.email : "").toLowerCase();
    return !!email && adminEmails.includes(email);
  } catch (e) {
    return false;
  }
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

module.exports = {
  SUPABASE_URL,
  BUCKET,
  MIME_EXT,
  loadContacts,
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
  sendEmail,
  adminCreateUser,
  adminConfirmUser,
  adminDeleteUser,
};
