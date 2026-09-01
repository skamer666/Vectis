// Rate limiting minimal, partage par les 4 endpoints publics les plus
// exposes au spam/abus (verification-request, lead-capture, review-submit,
// track). Fichier volontairement separe de _verification-lib.js : ces 4
// endpoints restent autonomes (voir leur en-tete), seul ce petit helper leur
// est commun, pour ne pas les faire dependre de la lib plus lourde.
//
// Implemente via l'appel a la fonction Postgres check_rate_limit() (voir
// supabase_schema.sql) plutot qu'un compteur en memoire : un compteur en
// memoire ne survit pas a un redemarrage/eviction d'instance serverless, et
// n'est pas partage entre les instances qui traitent des requetes en
// parallele -- un attaquant determine passerait au travers en quelques
// requetes. La fonction Postgres est atomique et partagee par construction.
//
// Fail-open deliberement : si Supabase est indisponible ou que l'appel RPC
// echoue pour une raison quelconque, la requete est laissee passer plutot
// que bloquee -- ce garde-fou anti-abus ne doit jamais devenir un point de
// panne qui casse une fonctionnalite reelle (creation de compte, avis...).
const SUPABASE_URL = "https://qjiyxhsnrzahdmdvzsqi.supabase.co";

function clientIp(req) {
  const cf = req.headers["cf-connecting-ip"];
  if (cf) return cf;
  const xff = req.headers["x-forwarded-for"];
  if (xff) return String(xff).split(",")[0].trim();
  return req.headers["x-real-ip"] || "unknown";
}

// endpoint : nom court identifiant l'appelant (ex. "verification-request").
// maxRequests/windowSeconds : seuil applique par IP. Retourne true si la
// requete est autorisee, false si elle doit etre refusee (429).
async function checkRateLimit(req, endpoint, maxRequests, windowSeconds) {
  const key = `${endpoint}:${clientIp(req)}`;
  try {
    const resp = await fetch(`${SUPABASE_URL}/rest/v1/rpc/check_rate_limit`, {
      method: "POST",
      headers: {
        apikey: process.env.SUPABASE_SERVICE_ROLE_KEY,
        Authorization: `Bearer ${process.env.SUPABASE_SERVICE_ROLE_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ p_key: key, p_max: maxRequests, p_window_seconds: windowSeconds }),
    });
    if (!resp.ok) return true;
    return await resp.json();
  } catch (e) {
    return true;
  }
}

module.exports = { checkRateLimit };
