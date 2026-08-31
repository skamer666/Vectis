// Adaptateur Cloudflare Pages Functions -> interface (req, res) a la Vercel
// Serverless Functions, pour porter les handlers existants (ecrits pour
// Vercel) avec le minimum de reecriture de leur logique metier.
//
// Pourquoi ce fichier existe : chaque fonction api/*.js de ce depot est
// ecrite contre l'API Node "(req, res)" de Vercel (req.method, req.query,
// req.headers[...], req.body deja lu, res.status().json(), res.setHeader(),
// res.end(), res.writeHead() pour verification-confirm.js). Cloudflare Pages
// Functions utilise au contraire l'API Workers standard : un handler
// onRequestGet/onRequestPost/onRequest(context) qui recoit une Request Fetch
// API et doit renvoyer une Response. Plutot que de reecrire le corps (souvent
// long et sensible : auth admin, upload de documents d'identite, emails
// transactionnels...) de chacune des 10 fonctions, ce shim traduit une seule
// fois l'interface : le corps de chaque fonction reste quasi identique a
// l'original Vercel, seul l'export change (voir le bas de chaque fichier
// api/*.js porte : `export const onRequestPost = wrapVercelHandler(handler)`
// au lieu de `module.exports = handler`).
//
// process.env.X continue de fonctionner tel quel dans le code porte grace au
// flag de compatibilite "nodejs_compat" (+ compatibility_date >= 2025-04-01)
// declare dans wrangler.toml a la racine du depot -- Cloudflare peuple alors
// process.env depuis les variables d'environnement / secrets du projet Pages,
// exactement comme Vercel. Aucun code n'a donc besoin de lire `context.env`
// directement (mais il reste transmis en 3e argument si un jour necessaire).

export function wrapVercelHandler(handler) {
  return async (context) => {
    const { request, env } = context;
    const url = new URL(request.url);

    const headers = {};
    for (const [key, value] of request.headers.entries()) {
      headers[key] = value;
    }

    const query = {};
    for (const [key, value] of url.searchParams.entries()) {
      query[key] = value;
    }

    // Les handlers originaux font eux-memes `typeof body === "string" ?
    // JSON.parse(body) : ...` -- on leur transmet donc le texte brut, jamais
    // pre-parse ici, pour ne rien changer a leur logique de validation.
    let rawBody = null;
    if (request.method !== "GET" && request.method !== "HEAD") {
      rawBody = await request.text();
    }

    const req = {
      method: request.method,
      headers,
      query,
      body: rawBody,
      url: request.url,
    };

    let statusCode = 200;
    const resHeaders = new Headers();
    let responseBody = null;

    const res = {
      setHeader(key, value) {
        resHeaders.set(key, value);
        return res;
      },
      status(code) {
        statusCode = code;
        return res;
      },
      json(obj) {
        responseBody = JSON.stringify(obj);
        if (!resHeaders.has("Content-Type")) {
          resHeaders.set("Content-Type", "application/json");
        }
        return res;
      },
      end(body) {
        if (body !== undefined && body !== null) responseBody = body;
        return res;
      },
      // Utilise par verification-confirm.js pour la redirection 302 vers la
      // page statique localisee /xx/identite-confirmee/?status=...
      writeHead(code, hdrs) {
        statusCode = code;
        if (hdrs) {
          for (const [key, value] of Object.entries(hdrs)) resHeaders.set(key, value);
        }
        return res;
      },
    };

    await handler(req, res, env);

    return new Response(responseBody, { status: statusCode, headers: resHeaders });
  };
}
