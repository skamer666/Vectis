// Fonction serverless Vercel : Greg valide ou refuse une demande de
// verification d'identite depuis /interne/verification-avocats/ (paliers
// telephone et document -- le palier email est auto-approuve par
// verification-confirm.js).
//
// POST { id, decision: "approved" | "rejected" }, header x-admin-token.
//
// Point critique de securite / vie privee : quelle que soit la decision, la
// carte de legitimation/brevet et le selfie (palier document) sont
// SUPPRIMES IMMEDIATEMENT du bucket prive, dans la meme requete que la
// decision -- jamais une etape separee que Greg pourrait oublier de faire.
// Les colonnes document_path/selfie_path sont ensuite mises a null : plus
// aucune trace du chemin de stockage ne subsiste en base une fois la
// decision prise.
//
// Le mot de passe du compte a deja ete choisi des la demande initiale (voir
// verification-request.js) et le compte Supabase Auth correspondant existe
// deja, mais bloque (email_confirm=false). En cas d'approbation, on
// l'active reellement (email_confirm=true) et on cree le lien
// lawyer_accounts -- l'avocat peut alors se connecter immediatement avec le
// mot de passe qu'il a deja choisi, sans etape supplementaire. En cas de
// refus, le compte pre-cree est SUPPRIME pour liberer l'adresse email en
// vue d'une nouvelle tentative.

const lib = require("./_verification-lib");

const LOGIN_SEGMENTS = {
  fr: "connexion",
  de: "anmelden",
  it: "accesso",
  en: "login",
};
const BASE_DOMAIN = "https://legatis.ch";
const EMAIL_SUBJECTS = {
  fr: "Votre identité est confirmée sur Legatis",
  de: "Ihre Identität wurde auf Legatis bestätigt",
  it: "La vostra identità è confermata su Legatis",
  en: "Your identity is confirmed on Legatis",
};

// Personnalise avec le nom de l'avocat/etude (row.avocat_nom) et traduit
// reellement le corps du message dans les 4 langues -- avant ce correctif,
// seul le sujet etait traduit, le corps restait toujours en francais quel
// que soit lang (bug decouvert lors de la revue du 2026-08-23).
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

// Meme contenu que approvalEmailBody mais en HTML, avec un vrai bouton
// <a href> -- sans ca, le lien de connexion apparait comme du texte brut
// non cliquable dans la plupart des clients mail (voir sendVerificationEmail
// dans verification-request.js pour le meme correctif sur le mail initial).
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

module.exports = async function handler(req, res) {
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
  const id = body && body.id;
  const decision = body && body.decision;
  if (!id || !["approved", "rejected"].includes(decision)) {
    res.status(400).json({ error: "invalid_body" });
    return;
  }

  try {
    const rows = await lib.supabaseSelect(
      "verification_requests",
      `id=eq.${encodeURIComponent(id)}&select=id,status,method,lang,canton,avocat_slug,avocat_nom,avocat_url,account_email,pending_user_id,document_path,selfie_path,marketing_consent`
    );
    const row = rows[0];
    if (!row) {
      res.status(404).json({ error: "not_found" });
      return;
    }
    if (row.status !== "pending") {
      res.status(409).json({ error: "already_decided" });
      return;
    }

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
      // Refuse : le compte pre-cree n'a jamais ete actif, on le supprime
      // pour liberer l'adresse email pour une eventuelle nouvelle demande.
      await lib.adminDeleteUser(row.pending_user_id);
    }

    await lib.supabasePatch("verification_requests", id, patch);

    res.status(200).json({ ok: true });
  } catch (err) {
    res.status(502).json({ error: "decide_failed", detail: String(err.message || err) });
  }
};
