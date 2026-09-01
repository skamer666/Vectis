// Fonction serverless Vercel : relance quotidienne des leads (formulaire
// "recevoir cette selection par email", api/lead-capture.js) qui ont
// explicitement coche la case "je veux bien etre recontacte pour donner mon
// avis" -- voir supabase_schema.sql pour le detail du consentement et la
// discussion avec Gregoire Giuliano du 01.09.2026 sur pourquoi cette case
// existe (jamais de reutilisation d'un email collecte a une autre fin sans
// consentement explicite et dedie).
//
// Declenchee par Vercel Cron (voir "crons" dans vercel.json), jamais par un
// visiteur : Vercel ajoute automatiquement l'en-tete
// "Authorization: Bearer $CRON_SECRET" a ses propres appels quand la
// variable d'environnement CRON_SECRET est definie -- c'est la seule
// protection de cet endpoint, et volontairement stricte (fail CLOSED, pas
// fail open comme le reste du depot) : contrairement a un echec de
// rate-limiting ou d'analytics, un appel non autorise ici enverrait de vrais
// emails a de vraies personnes, donc mieux vaut refuser que laisser passer
// en cas de doute.
//
// Chaque lead n'est relance qu'une seule fois (review_reminder_sent_at ne
// passe a une valeur qu'apres un envoi Resend reussi ; en cas d'echec, la
// ligne reste eligible et sera retentee au prochain run plutot que perdue).
//
// Variables d'environnement requises :
//   SUPABASE_SERVICE_ROLE_KEY, RESEND_API_KEY, CRON_SECRET
const lib = require("./_verification-lib");

const REMINDER_DELAY_DAYS = 5;
const BATCH_LIMIT = 50;
const BASE_DOMAIN = "https://legatis.ch";

const SUBJECTS = {
  fr: "Votre avis sur Legatis ?",
  de: "Ihre Bewertung auf Legatis?",
  it: "La vostra recensione su Legatis?",
  en: "Your review on Legatis?",
};

function body(lang, pageUrl) {
  const link = pageUrl.startsWith("http") ? pageUrl : `${BASE_DOMAIN}${pageUrl}`;
  const texts = {
    fr: {
      text: `Bonjour,\n\nIl y a quelques jours, vous avez consulté une fiche sur Legatis et accepté d'être recontacté(e) pour partager votre avis. Si vous avez contacté cet avocat ou cette étude, votre retour aiderait d'autres personnes dans la même situation.\n\nLaisser un avis : ${link}\n\nSi vous n'avez pas donné suite, ignorez simplement cet email.\n\nL'équipe Legatis`,
      cta: "Laisser un avis",
    },
    de: {
      text: `Guten Tag\n\nVor einigen Tagen haben Sie ein Profil auf Legatis angesehen und zugestimmt, für eine Bewertung erneut kontaktiert zu werden. Falls Sie diese Anwältin bzw. diesen Anwalt kontaktiert haben, würde Ihre Rückmeldung anderen in derselben Situation helfen.\n\nBewertung abgeben: ${link}\n\nFalls Sie keinen Kontakt aufgenommen haben, ignorieren Sie diese E-Mail einfach.\n\nDas Legatis-Team`,
      cta: "Bewertung abgeben",
    },
    it: {
      text: `Gentile utente,\n\nAlcuni giorni fa avete consultato una scheda su Legatis e accettato di essere ricontattati per lasciare una recensione. Se avete contattato questo avvocato o studio, il vostro riscontro aiuterebbe altre persone nella stessa situazione.\n\nLasciare una recensione: ${link}\n\nSe non avete dato seguito, ignorate semplicemente questa email.\n\nIl team Legatis`,
      cta: "Lasciare una recensione",
    },
    en: {
      text: `Hello,\n\nA few days ago you looked at a listing on Legatis and agreed to be contacted again to leave a review. If you got in touch with this lawyer or firm, your feedback would help others in the same situation.\n\nLeave a review: ${link}\n\nIf you didn't follow up, simply ignore this email.\n\nThe Legatis team`,
      cta: "Leave a review",
    },
  };
  const t = texts[lang] || texts.fr;
  const btnStyle = "display:inline-block;padding:12px 24px;background:#111;color:#fff;text-decoration:none;border-radius:6px;font-weight:600;";
  const html = `<p>${lib.escapeHtml(t.text.split("\n\n")[0])}</p><p>${lib.escapeHtml(t.text.split("\n\n")[1])}</p><p><a href="${link}" style="${btnStyle}">${t.cta}</a></p>`;
  return { text: t.text, html };
}

module.exports = async function handler(req, res) {
  const expected = process.env.CRON_SECRET;
  const given = (req.headers["authorization"] || "").replace(/^Bearer\s+/i, "");
  if (!expected || !given || !lib.safeEqual(given, expected)) {
    res.status(401).json({ error: "unauthorized" });
    return;
  }
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) {
    res.status(500).json({ error: "server_not_configured" });
    return;
  }

  const cutoff = new Date(Date.now() - REMINDER_DELAY_DAYS * 24 * 3600 * 1000).toISOString();
  let leads;
  try {
    leads = await lib.supabaseSelect(
      "leads",
      `select=id,email,page_url,lang&review_reminder_consent=eq.true&review_reminder_sent_at=is.null&created_at=lt.${encodeURIComponent(cutoff)}&limit=${BATCH_LIMIT}`
    );
  } catch (e) {
    res.status(502).json({ error: "supabase_read_failed", detail: String(e.message || e) });
    return;
  }

  let sent = 0;
  let failed = 0;
  for (const lead of leads) {
    const lang = ["fr", "de", "it", "en"].includes(lead.lang) ? lead.lang : "fr";
    const { text, html } = body(lang, lead.page_url);
    const ok = await lib.sendEmail(lead.email, SUBJECTS[lang], text, html).catch(function () {
      return false;
    });
    if (ok) {
      try {
        await lib.supabasePatch("leads", lead.id, { review_reminder_sent_at: new Date().toISOString() });
        sent++;
      } catch (e) {
        // Email parti mais marquage echoue : au pire un doublon sera envoye
        // au prochain run, jamais une perte silencieuse d'un lead consentant.
        failed++;
      }
    } else {
      failed++;
    }
  }

  res.status(200).json({ ok: true, processed: leads.length, sent, failed });
};
