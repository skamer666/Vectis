// Fonction Cloudflare Pages : Greg valide ou refuse un element en attente
// de moderation depuis /interne/verification-avocats/. Fusion de deux
// fonctions auparavant separees (verification-decide.js et
// profile-decide.js) pour rester sous la limite de 12 fonctions serverless
// du plan Hobby Vercel -- meme logique, juste selectionnee par body.kind.
// Fusion conservee lors du portage Cloudflare (pas de raison de la defaire).
//
// POST { kind: "verification" | "profile", id, decision: "approved" | "rejected" },
// authentification admin (checkAdminAuth).
//
// kind=verification -- demande de verification d'identite
// (verification_requests, paliers telephone et document -- le palier email
// est auto-approuve par verification-confirm.js). Point critique de
// securite / vie privee : quelle que soit la decision, la carte de
// legitimation/brevet et le selfie (palier document) sont SUPPRIMES
// IMMEDIATEMENT du bucket prive, dans la meme requete que la decision.
// En cas d'approbation : active le compte Supabase Auth deja pre-cree
// (email_confirm=true) et cree le lien lawyer_accounts. En cas de refus :
// le compte pre-cree est supprime pour liberer l'adresse email.
//
// kind=profile -- soumission de profil avocat (lawyer_profile_submissions).
// Aucun document sensible a supprimer : on se contente de changer le
// statut, la ligne reste en base (historique append-only).
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
import { wrapVercelHandler } from "./_shim.js";
import * as lib from "./_verification-lib.js";

const LOGIN_SEGMENTS = { fr: "connexion", de: "anmelden", it: "accesso", en: "login" };
const BASE_DOMAIN = "https://legatis.ch";
const EMAIL_SUBJECTS = {
  fr: "Votre identité est confirmée sur Legatis",
  de: "Ihre Identität wurde auf Legatis bestätigt",
  it: "La vostra identità è confermata su Legatis",
  en: "Your identity is confirmed on Legatis",
};

function approvalEmailBody(lang, nom, loginLink) {
  if (lang === "de") {
    return `Guten Tag ${nom}\n\nIhre Identität wurde bestätigt: Ihr Legatis-Konto ist ab sofort aktiv.\n\nSie können sich jetzt mit dem von Ihnen gewählten Passwort anmelden:\n${loginLink}\n\nFreundliche Grüsse\nDas Legatis-Team`;
  }
  if (lang === "it") {
    return `Gentile ${nom}\n\nLa vostra identità è stata confermata: il vostro account Legatis è ora attivo.\n\nPotete accedere fin da subito con la password che avete scelto:\n${loginLink}\n\nCordiali saluti\nIl team Legatis`;
  }
  if (lang === "en") {
    return `Hello ${nom}\n\nYour identity has been confirmed: your Legatis account is now active.\n\nYou can log in right away with the password you chose:\n${loginLink}\n\nBest regards,\nThe Legatis team`;
  }
  return `Bonjour ${nom}\n\nVotre identité a été confirmée : votre compte Legatis est désormais actif.\n\nVous pouvez vous connecter dès maintenant avec le mot de passe que vous avez choisi :\n${loginLink}\n\nCordialement,\nL'équipe Legatis`;
}

function escapeHtml(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}

function approvalEmailHtml(lang, nom, loginLink) {
  const btnStyle = "display:inline-block;padding:12px 24px;background:#111;color:#fff;text-decoration:none;border-radius:6px;font-weight:600;";
  const safeName = escapeHtml(nom);
  const safeLink = escapeHtml(loginLink);
  const ctaLabels = { fr: "Se connecter", de: "Anmelden", it: "Accedere", en: "Log in" };
  if (lang === "de") {
    return `<p>Guten Tag ${safeName}</p><p>Ihre Identität wurde bestätigt: Ihr Legatis-Konto ist ab sofort aktiv.</p><p><a href="${loginLink}" style="${btnStyle}">${ctaLabels.de}</a></p><p>Oder kopieren Sie diesen Link in Ihren Browser: <a href="${loginLink}">${safeLink}</a></p><p>Freundliche Grüsse<br>Das Legatis-Team</p>`;
  }
  if (lang === "it") {
    return `<p>Gentile ${safeName}</p><p>La vostra identità è stata confermata: il vostro account Legatis è ora attivo.</p><p><a href="${loginLink}" style="${btnStyle}">${ctaLabels.it}</a></p><p>Oppure copiate questo link nel vostro browser: <a href="${loginLink}">${safeLink}</a></p><p>Cordiali saluti<br>Il team Legatis</p>`;
  }
  if (lang === "en") {
    return `<p>Hello ${safeName}</p><p>Your identity has been confirmed: your Legatis account is now active.</p><p><a href="${loginLink}" style="${btnStyle}">${ctaLabels.en}</a></p><p>Or copy this link into your browser: <a href="${loginLink}">${safeLink}</a></p><p>Best regards,<br>The Legatis team</p>`;
  }
  return `<p>Bonjour ${safeName}</p><p>Votre identité a été confirmée : votre compte Legatis est désormais actif.</p><p><a href="${loginLink}" style="${btnStyle}">${ctaLabels.fr}</a></p><p>Ou copiez ce lien dans votre navigateur : <a href="${loginLink}">${safeLink}</a></p><p>Cordialement,<br>L'équipe Legatis</p>`;
}

async function decideVerification(id, decision) {
  const rows = await lib.supabaseSelect(
    "verification_requests",
    `id=eq.${encodeURIComponent(id)}&select=id,status,method,lang,canton,avocat_slug,avocat_nom,avocat_url,account_email,pending_user_id,document_path,selfie_path,marketing_consent,marketing_consent_ip`
  );
  const row = rows[0];
  if (!row) return { status: 404, body: { error: "not_found" } };
  if (row.status !== "pending") return { status: 409, body: { error: "already_decided" } };

  await lib.storageDelete([row.document_path, row.selfie_path]);

  const patch = {
    status: decision,
    decided_at: new Date().toISOString(),
    decided_by: "greg",
    document_path: null,
    selfie_path: null,
  };

  if (decision === "approved") {
    await lib.adminConfirmUser(row.pending_user_id);
    await lib.supabaseInsert("lawyer_accounts", {
      user_id: row.pending_user_id,
      canton: row.canton,
      avocat_slug: row.avocat_slug,
      avocat_nom: row.avocat_nom,
      avocat_url: row.avocat_url,
      marketing_consent: !!row.marketing_consent,
      marketing_consent_ip: row.marketing_consent ? row.marketing_consent_ip : null,
    });
    const lang = row.lang || "fr";
    const seg = LOGIN_SEGMENTS[lang] || LOGIN_SEGMENTS.fr;
    const loginLink = `${BASE_DOMAIN}/${lang}/${seg}/`;
    const subject = EMAIL_SUBJECTS[lang] || EMAIL_SUBJECTS.fr;
    const emailBody = approvalEmailBody(lang, row.avocat_nom || "", loginLink);
    const emailHtml = approvalEmailHtml(lang, row.avocat_nom || "", loginLink);
    const sent = await lib.sendEmail(row.account_email, subject, emailBody, emailHtml);
    patch.email_sent = !!sent;
  } else {
    await lib.adminDeleteUser(row.pending_user_id);
  }

  await lib.supabasePatch("verification_requests", id, patch);
  return { status: 200, body: { ok: true } };
}

async function decideProfile(id, decision) {
  const rows = await lib.supabaseSelect("lawyer_profile_submissions", `id=eq.${encodeURIComponent(id)}&select=id,status`);
  const row = rows[0];
  if (!row) return { status: 404, body: { error: "not_found" } };
  if (row.status !== "pending") return { status: 409, body: { error: "already_decided" } };

  await lib.supabasePatch("lawyer_profile_submissions", id, {
    status: decision,
    decided_at: new Date().toISOString(),
    decided_by: "greg",
  });
  return { status: 200, body: { ok: true } };
}

async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "method_not_allowed" });
    return;
  }
  if (!(await lib.checkAdminAuth(req))) {
    res.status(401).json({ error: "unauthorized" });
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
  const kind = body && body.kind;
  const id = body && body.id;
  const decision = body && body.decision;
  if ((kind !== "verification" && kind !== "profile") || !id || !["approved", "rejected"].includes(decision)) {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  try {
    const result = kind === "verification" ? await decideVerification(id, decision) : await decideProfile(id, decision);
    res.status(result.status).json(result.body);
  } catch (err) {
    res.status(502).json({ error: "decide_failed", detail: String(err.message || err) });
  }
}

export const onRequest = wrapVercelHandler(handler);
