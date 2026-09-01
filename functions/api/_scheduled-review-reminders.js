// Portage Cloudflare Workers (Cron Trigger, voir wrangler.toml [triggers] et
// worker-entry.js a la racine du depot) du cron Vercel equivalent,
// api/send-review-reminders.js -- meme logique, meme regle de non-fabrication
// et memes conditions d'eligibilite (voir supabase_schema.sql pour le detail
// du consentement).
//
// Contrairement a la version Vercel, aucune verification de jeton n'est
// necessaire ici : un Cron Trigger Cloudflare declenche directement la
// fonction "scheduled" du Worker (voir worker-entry.js), jamais via une URL
// HTTP publique -- il n'existe simplement aucun moyen pour un visiteur de
// declencher cette fonction depuis l'exterieur.
import { supabaseSelect, supabasePatch, sendEmail, escapeHtml } from "./_verification-lib.js";

const REMINDER_DELAY_DAYS = 5;
const BATCH_LIMIT = 50;
const BASE_DOMAIN = "https://legatis.ch";

const SUBJECTS = {
  fr: "Votre avis sur Legatis ?",
  de: "Ihre Bewertung auf Legatis?",
  it: "La vostra recensione su Legatis?",
  en: "Your review on Legatis?",
};

function reminderBody(lang, pageUrl) {
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
  const html = `<p>${escapeHtml(t.text.split("\n\n")[0])}</p><p>${escapeHtml(t.text.split("\n\n")[1])}</p><p><a href="${link}" style="${btnStyle}">${t.cta}</a></p>`;
  return { text: t.text, html };
}

export async function runReviewReminders() {
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) return { ok: false, reason: "not_configured" };

  const cutoff = new Date(Date.now() - REMINDER_DELAY_DAYS * 24 * 3600 * 1000).toISOString();
  let leads;
  try {
    leads = await supabaseSelect(
      "leads",
      `select=id,email,page_url,lang&review_reminder_consent=eq.true&review_reminder_sent_at=is.null&created_at=lt.${encodeURIComponent(cutoff)}&limit=${BATCH_LIMIT}`
    );
  } catch (e) {
    return { ok: false, reason: "supabase_read_failed", detail: String(e.message || e) };
  }

  let sent = 0;
  let failed = 0;
  for (const lead of leads) {
    const lang = ["fr", "de", "it", "en"].includes(lead.lang) ? lead.lang : "fr";
    const { text, html } = reminderBody(lang, lead.page_url);
    const ok = await sendEmail(lead.email, SUBJECTS[lang], text, html).catch(() => false);
    if (ok) {
      try {
        await supabasePatch("leads", lead.id, { review_reminder_sent_at: new Date().toISOString() });
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

  return { ok: true, processed: leads.length, sent, failed };
}
