# Migration Vercel -> Cloudflare Pages

Contexte : le plan Hobby Vercel a ete depasse plusieurs fois cet aout (quota
edge requests le 21-24/08, puis limite de 12 fonctions serverless le 23-28/08
qui a fait echouer TOUS les deploiements pendant 5 jours). Ce document
explique ce qui a ete change dans ce depot pour rendre la migration possible,
et les etapes qu'il reste a faire cote compte Cloudflare (creation du projet,
variables d'environnement, DNS) -- ces etapes demandent l'acces au compte de
Greg et ne peuvent pas etre faites depuis ce depot seul.

**Rien n'a ete deploye ni bascule.** Ce patch prepare le code ; le site
continue de tourner sur Vercel tant que le DNS n'est pas change (derniere
etape, volontairement separee et non automatique).

## Ce qui a change dans le code

- `functions/api/*.js` (nouveau) : portage des 10 fonctions serverless de
  `api/*.js` (inchange, reste utilise par Vercel) vers la convention
  Cloudflare Pages Functions. `api/*.js` n'est PAS supprime -- les deux
  cohabitent, seul `api/` est lu par Vercel et seul `functions/` est lu par
  Cloudflare, aucun conflit.
- `wrangler.toml` (nouveau) : declare `nodejs_compat` (necessaire pour que
  `process.env`, `Buffer` et `node:crypto` fonctionnent dans les fonctions
  portees) et `pages_build_output_dir = "dist"`.
- `build.py` : ajoute `gen_cloudflare_files()`, appelee juste apres
  `gen_robots()` dans le pipeline complet. Genere `dist/_headers` et
  `dist/_redirects`, l'equivalent Cloudflare Pages des sections
  `headers`/`redirects` de `vercel.json` (Cloudflare ne lit pas
  `vercel.json`). Verifie ligne a ligne contre `vercel.json` -- memes
  en-tetes de securite, meme CSP, mêmes regles de cache, meme redirection
  permanente `/` -> `/fr/`.

## Pourquoi le portage n'est pas une simple recopie

Les fonctions Vercel utilisaient l'API Node classique `(req, res)` ; les
fonctions Cloudflare Pages utilisent l'API Workers standard (`Request`/
`Response`). Plutot que de reecrire la logique metier de chaque fonction
(authentification admin, upload de documents d'identite, emails
transactionnels...) -- ce qui aurait multiplie le risque d'introduire un bug
de securite en le traduisant -- un petit adaptateur (`functions/api/_shim.js`)
reconstruit une interface `(req, res)` compatible par-dessus l'API Workers.
Le corps de chaque fonction portee est donc quasi identique a l'original
Vercel ; seuls les `require`/`module.exports` sont devenus `import`/`export`,
et la lecture des fichiers JSON generes par `build.py`
(`verification_contacts.json`, `contract_content.json`) est devenue un
import statique plutot qu'une lecture disque (les Workers Cloudflare n'ont
aucun systeme de fichiers a l'execution, meme avec `nodejs_compat`).

**Verification deja faite depuis cette session** (sans compte Cloudflare) :
`python3 build.py all` a ete execute en local -- `dist/_headers`,
`dist/_redirects`, `data/verification_contacts.json` et
`data/contract_content.json` sont bien generes. Les 12 fichiers de
`functions/api/` ont ensuite ete passes dans `esbuild --bundle` (le meme
bundler qu'utilise Cloudflare en interne) : les 12 bundlent sans la moindre
erreur, imports JSON compris. C'est une forte indication que l'import
statique fonctionnera reellement sur Cloudflare, mais ce n'est PAS une
certitude absolue : Cloudflare pourrait en theorie bundler `functions/` avant
la fin de `buildCommand` (aucune documentation Cloudflare consultee ne
tranche explicitement ce point, malgre plusieurs recherches). **C'est le
point n°1 a verifier sur le premier deploiement preview** (voir plus bas) --
si ca casse, ce sera un echec de build EXPLICITE ("module not found"), pas un
bug silencieux, et un plan de repli est documente en bas de ce fichier.

## Etapes cote compte Cloudflare (a faire par Greg)

### 1. Creer le projet Pages

Dashboard Cloudflare -> Workers & Pages -> Create -> Pages -> Connect to Git
-> selectionner `skamer666/Vectis`.

Build settings :
- Framework preset : None
- Build command : `python3 -m pip install -r requirements.txt --break-system-packages 2>/dev/null || python3 -m pip install -r requirements.txt; python3 build.py all`
- Build output directory : `dist`

### 2. Variables d'environnement / secrets

Settings -> Environment variables, pour l'environnement Production (et
Preview si vous voulez tester les endpoints API sur les previews) :

| Nom | Requis | Valeur |
|---|---|---|
| `SUPABASE_SERVICE_ROLE_KEY` | Oui | la meme que sur Vercel |
| `ADMIN_EMAILS` | Oui (pour /interne/*) | la meme que sur Vercel |
| `RESEND_API_KEY` | Optionnel | la meme que sur Vercel |
| `RESEND_FROM_EMAIL` | Optionnel | la meme que sur Vercel |

Toutes marquees "secret" (chiffrees), pas juste "variable", memes valeurs
que dans Vercel -> Settings -> Environment Variables.

### 3. Compatibility flags

`wrangler.toml` declare deja `nodejs_compat` + `compatibility_date`. Par
securite, verifiez aussi Settings -> Functions -> Compatibility flags dans le
dashboard Cloudflare : si `nodejs_compat` n'y apparait pas automatiquement
apres le premier deploiement, l'ajouter manuellement pour Production ET
Preview (sinon `process.env`/`Buffer`/`node:crypto` ne fonctionnent pas et
toutes les fonctions api/* echouent en 500).

### 4. Premier deploiement (preview, PAS le domaine final)

Une fois le projet cree, Cloudflare deploie automatiquement sur une URL du
type `vectis-repo.pages.dev`. **Ne touchez pas encore au DNS de legatis.ch.**

Verifications a faire sur cette URL preview, dans l'ordre :

1. La page d'accueil se charge (`/fr/`), une fiche avocat se charge.
2. `/api/verification-request` -- LE POINT CRITIQUE : remplir le formulaire
   sur `/fr/verifier-mon-identite/` avec un vrai email publie (ou utiliser le
   compte de test GE + `/api/reset-test-account` pour rejouer le parcours).
   Si ca repond `{"error":"contacts_unavailable"}` ou une 500, c'est le
   signal que l'import statique de `verification_contacts.json` n'a pas
   fonctionne -- voir "Plan de repli" ci-dessous avant d'aller plus loin.
3. `/interne/verification-avocats/` avec un compte admin (email dans
   `ADMIN_EMAILS`) -- verifie `checkAdminAuth` et donc `process.env` cote
   Cloudflare.
4. Un envoi d'avis (`/fr/avis/...`) et une capture de lead -- verifient les
   deux fonctions autonomes (review-submit, lead-capture) qui ne dependent
   pas de _verification-lib.js.
5. Verifier les en-tetes de reponse (`curl -I`) : CSP, X-Frame-Options,
   Cache-Control presents et corrects sur une page HTML et sur un fichier
   sous `/static/`.
6. Verifier que `/` redirige bien en 301 vers `/fr/`.

### 5. DNS -- uniquement une fois tout verifie ci-dessus

Cloudflare Pages -> Custom domains -> ajouter `legatis.ch` et `www.legatis.ch`.
Si le domaine est deja sur Cloudflare (nameservers), l'ajout cree/ajuste les
enregistrements DNS automatiquement. Sinon, suivre les enregistrements CNAME
que Cloudflare propose.

Recommandation : garder le projet Vercel intact (ne pas le supprimer) le
temps de confirmer que Cloudflare tient la charge -- le DNS peut etre
repointe vers Vercel en quelques minutes en cas de probleme serieux.

## Plan de repli si l'import statique des fichiers JSON ne fonctionne pas

Si le build Cloudflare echoue sur l'import de `verification_contacts.json`
ou `contract_content.json` (etape 4.2 ci-dessus), la cause la plus probable
est un ordre de build different de ce qui a ete verifie en local. Solution :
remplacer la lecture fichier par une lecture Supabase, exactement comme le
reste de l'application (deja le cas pour toutes les autres donnees
serveur) :

1. Ajouter une table `verification_contacts` (canton, avocat_slug, email,
   telephone) dans Supabase, remplie par un petit script Python appele a la
   fin de `gen_verification_contacts()` dans `build.py` (upsert via l'API
   REST Supabase, meme service_role key).
2. Remplacer `loadContacts()`/`loadContractContent()` dans
   `functions/api/_verification-lib.js` par un appel `supabaseSelect(...)`
   (async -- `verification-request.js` et `admin-list.js` font deja
   `await lib.loadContacts()`-style dans un try/catch, l'ajout d'un `await`
   suffit).

Cette alternative n'a pas ete implementee dans ce patch pour ne pas
complexifier une migration qui, sur la base de la verification esbuild
ci-dessus, a de bonnes chances de fonctionner telle quelle -- mais elle est
documentee ici pour ne pas repartir de zero si le point 4.2 echoue.
