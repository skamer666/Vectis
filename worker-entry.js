// Point d'entree reel du Worker Cloudflare (voir wrangler.toml : main =
// "worker-entry.js"), a la place du fichier genere dist/_worker.js/index.js
// directement -- necessaire pour ajouter un gestionnaire "scheduled" (Cron
// Trigger), que `wrangler pages functions build` ne genere pas (cette
// commande ne produit qu'un gestionnaire "fetch" a partir de functions/).
//
// dist/_worker.js/index.js est regenere a chaque build (voir
// CLOUDFLARE_MIGRATION.md) : ce fichier-ci n'est PAS regenere, il importe
// simplement le resultat du build et y ajoute le seul morceau que Pages
// Functions ne sait pas produire.
//
// Ajoute le 01.09.2026 suite a l'arret complet de Vercel (decision de
// Gregoire Giuliano) : le cron quotidien de relance avis
// (envoi_review_reminders, ex-api/send-review-reminders.js sous Vercel) doit
// desormais tourner ici. Contrairement au cron Vercel, aucun jeton de
// securite n'est necessaire : un Cron Trigger Cloudflare ne peut pas etre
// declenche par une requete HTTP externe, uniquement par la planification
// configuree dans [triggers] (wrangler.toml).
import worker from "./dist/_worker.js/index.js";
import { runReviewReminders } from "./functions/api/_scheduled-review-reminders.js";

const CANONICAL_HOST = "www.legatis.ch";

// Ajoute le 02.09.2026 : ni Vercel (avant) ni le zone-level Cloudflare
// "Always Use HTTPS" (jamais active ici) ne consolidaient les 4 variantes
// d'hote (http/https x legatis.ch/www.legatis.ch) vers une seule -- verifie
// via curl, les 4 renvoyaient un 200 identique. La balise <link canonical>
// limite le risque de contenu duplique aux yeux de Google mais un vrai 301
// est le signal le plus fort et evite de gaspiller le budget de crawl sur
// 73000+ pages en double. Ne touche jamais les hotes *.workers.dev
// (previews / `wrangler deploy` sans domaine custom) : seuls les deux hotes
// legatis.ch reels sont concernes.
function canonicalRedirect(request) {
  const url = new URL(request.url);
  const isApex = url.hostname === "legatis.ch";
  const isWwwInsecure = url.hostname === CANONICAL_HOST && url.protocol !== "https:";
  if (!isApex && !isWwwInsecure) return null;
  url.hostname = CANONICAL_HOST;
  url.protocol = "https:";
  url.port = "";
  return Response.redirect(url.toString(), 301);
}

export default {
  async fetch(request, env, ctx) {
    return canonicalRedirect(request) || worker.fetch(request, env, ctx);
  },
  async scheduled(event, env, ctx) {
    ctx.waitUntil(runReviewReminders());
  },
};
