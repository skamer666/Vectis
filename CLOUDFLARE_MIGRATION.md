# Migration Vercel -> Cloudflare

**Mise a jour du 01.09.2026 : migration terminee, Vercel completement
arrete.** Le DNS de legatis.ch pointe sur Cloudflare depuis le 31.08.2026
(voir la mise a jour precedente), et Gregoire Giuliano a confirme le
01.09.2026 vouloir arreter Vercel completement plutot que de le garder comme
filet de secours. En consequence :
- `api/*.js`, `vercel.json` et le compte/projet Vercel n'ont plus de role
  actif -- `api/*.js` a ete supprime de ce depot (voir le commit du
  01.09.2026), `functions/api/*.js` (Cloudflare) est desormais la seule
  version qui existe.
- Le cron quotidien de relance avis, qui tournait sur Vercel Cron
  (`api/send-review-reminders.js` + `crons` dans `vercel.json`, tous deux
  supprimes), tourne desormais sur un Cron Trigger Cloudflare natif. Ca a
  demande un ajout que Pages Functions ne sait pas produire tout seul (un
  gestionnaire `scheduled`, distinct du gestionnaire `fetch` genere par
  `wrangler pages functions build`) : voir `worker-entry.js` a la racine du
  depot (nouveau point d'entree du Worker, remplace la reference directe a
  `dist/_worker.js/index.js` dans `wrangler.toml`) et
  `functions/api/_scheduled-review-reminders.js` (logique du cron, portage
  Cloudflare de l'ancien `api/send-review-reminders.js`). Aucune verification
  de jeton necessaire ici (contrairement a la version Vercel) : un Cron
  Trigger ne peut pas etre appele depuis une URL publique.
- Aucun changement cote dashboard Cloudflare (build command, deploy command,
  variables d'environnement) : `wrangler deploy` lit `main` dans
  `wrangler.toml`, quel que soit ce vers quoi il pointe. Seul ajout reel :
  le Cron Trigger doit apparaitre automatiquement dans Workers & Pages ->
  legatis -> Triggers apres le prochain deploiement (a verifier par Greg).

**Mise a jour du 31.08.2026, apres le premier vrai deploiement.** Le titre
d'origine de ce document ("Cloudflare Pages") s'est revele inexact : malgre
le chemin suivi dans le dashboard ("Workers & Pages -> Create -> Pages ->
Connect to Git"), la ressource creee est un vrai **Worker** (visible sous
`/workers/services/view/legatis/...`), pas un projet Cloudflare Pages
classique. `wrangler pages deploy` echoue avec "The Pages project legatis
does not exist". Le dossier `functions/api/*.js` reste ecrit selon la
convention Pages Functions (aucune reecriture necessaire), mais il est
desormais compile en un script Worker unique via la commande officielle
`wrangler pages functions build`, prevue pour exactement ce cas de figure.
Voir "Ce qui a change dans le code" et l'etape 1 ci-dessous pour le detail.

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
- `wrangler.toml` : declare `nodejs_compat` (necessaire pour que
  `process.env`, `Buffer` et `node:crypto` fonctionnent dans les fonctions
  portees), `main = "worker-entry.js"` (wrapper statique du depot qui importe
  le script Worker compile, voir ci-dessous et la mise a jour du 01.09.2026),
  `[triggers] crons` (cron de relance avis) et `[assets] directory = "dist"`
  (le site statique). PAS `pages_build_output_dir` (reserve aux vrais projets
  Pages, absent ici).
- `build.py` : ajoute `gen_cloudflare_files()`, appelee juste apres
  `gen_robots()` dans le pipeline complet. Genere `dist/_headers`,
  `dist/_redirects` (equivalent Cloudflare des sections `headers`/
  `redirects` de `vercel.json`, verifie ligne a ligne -- memes en-tetes de
  securite, meme CSP, memes regles de cache, meme redirection permanente
  `/` -> `/fr/`) et `dist/.assetsignore` (exclut `_worker.js/` du service
  de fichiers statiques, sinon Cloudflare tenterait de servir le bundle JS
  compile comme une page web).
- Commande de build Cloudflare (a saisir dans le dashboard, voir etape 1) :
  `python3 build.py all` genere le site + `data/*.json`, PUIS
  `npx wrangler pages functions build --outdir=dist/_worker.js/` compile
  `functions/api/*.js` en un unique script Worker (`dist/_worker.js/index.js`,
  pointe par `main` dans `wrangler.toml`) -- pont officiel documente par
  Cloudflare pour deployer des Pages Functions comme Worker.

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

**Verification deja faite** (en local, avec le vrai `wrangler` CLI --
version 4.127.1, identique a celle utilisee par le build Cloudflare reel) :
`python3 build.py all` puis `npx wrangler pages functions build
--outdir=dist/_worker.js/` executes l'un apres l'autre -- compilation
reussie ("Compiled Worker successfully"), `dist/_worker.js/index.js` genere
(~1.1 Mo). Verification faite sur la taille et le contenu du bundle que
`verification_contacts.json` (950 Ko) est bien inline dedans -- l'import
statique fonctionne reellement, ce n'est plus une hypothese. Seuls
avertissements attendus et sans consequence : `wrangler` signale que
`node:crypto`/`node:buffer` necessitent `nodejs_compat` a l'execution --
deja declare dans `wrangler.toml`.

## Etapes cote compte Cloudflare (a faire par Greg)

Le projet "legatis" existe deja (cree via Workers & Pages -> Create -> Pages
-> Connect to Git -> `skamer666/Vectis`), mais c'est un Worker, pas un projet
Pages classique -- voir la mise a jour en tete de ce document. Les etapes
ci-dessous corrigent sa configuration en consequence.

### 1. Build command / Deploy command (Settings -> Builds)

- **Build command** :
  ```
  python3 -m pip install -r requirements.txt --break-system-packages 2>/dev/null || python3 -m pip install -r requirements.txt; python3 build.py all && npx wrangler pages functions build --outdir=dist/_worker.js/
  ```
  (la seconde commande compile `functions/api/*.js` en un script Worker,
  voir plus haut -- sans elle, aucune fonction api/* n'est deployee).
- **Deploy command** : `npx wrangler deploy` (la valeur par defaut -- si
  elle a ete changee en `wrangler pages deploy` a un essai precedent, la
  remettre a `wrangler deploy` : "legatis" est un Worker, pas un projet
  Pages, `wrangler pages deploy` echoue avec "The Pages project legatis
  does not exist").

### 2. Permissions du jeton de build

Settings -> Builds -> API token (ou la variable `CLOUDFLARE_API_TOKEN` sous
Build variables and secrets selon la configuration) : le jeton utilise doit
avoir la permission **Account -> Workers Scripts -> Edit** (c'est un Worker
qui est deploye, pas un projet Pages -- **Cloudflare Pages: Edit** n'est pas
necessaire pour ce chemin, meme si l'avoir en plus ne gene pas).

### 3. Variables d'environnement / secrets

Settings -> Variables and Secrets, pour l'environnement Production (et
Preview si vous voulez tester les endpoints API sur les previews) :

| Nom | Requis | Valeur |
|---|---|---|
| `SUPABASE_SERVICE_ROLE_KEY` | Oui | la meme que sur Vercel |
| `ADMIN_EMAILS` | Oui (pour /interne/*) | la meme que sur Vercel |
| `RESEND_API_KEY` | Optionnel | la meme que sur Vercel |
| `RESEND_FROM_EMAIL` | Optionnel | la meme que sur Vercel |

Toutes marquees "secret" (chiffrees), pas juste "variable", memes valeurs
que dans Vercel -> Settings -> Environment Variables.

### 4. Compatibility flags

`wrangler.toml` declare deja `nodejs_compat` + `compatibility_date`. Par
securite, verifiez aussi Settings -> Runtime (ou Compatibility flags selon
l'emplacement exact dans l'UI Worker) : si `nodejs_compat` n'y apparait pas
automatiquement apres le premier deploiement reussi, l'ajouter manuellement
(sinon `process.env`/`Buffer`/`node:crypto` ne fonctionnent pas et toutes
les fonctions api/* echouent en 500).

### 5. Premier deploiement (preview, PAS le domaine final)

Une fois la configuration ci-dessus corrigee, declenchez un nouveau
deploiement (pousser un commit, ou "Create deployment" -- pas "Retry" sur un
ancien deploiement en echec, qui peut rejouer une config perimee). Cloudflare
deploie sur une URL du type `legatis.<compte>.workers.dev` ou une preview
URL. **Ne touchez pas encore au DNS de legatis.ch.**

Verifications a faire sur cette URL preview, dans l'ordre :

1. La page d'accueil se charge (`/fr/`), une fiche avocat se charge.
2. `/api/verification-request` -- LE POINT CRITIQUE : remplir le formulaire
   sur `/fr/verifier-mon-identite/` avec un vrai email publie (ou utiliser le
   compte de test GE + `/api/reset-test-account` pour rejouer le parcours).
   Si ca repond `{"error":"contacts_unavailable"}` ou une 500, voir "Plan de
   repli" ci-dessous.
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

### 6. DNS -- uniquement une fois tout verifie ci-dessus

Le Worker -> Settings -> Domains & Routes -> Add -> Custom domain ->
`legatis.ch` et `www.legatis.ch`. Si le domaine est deja sur Cloudflare
(nameservers), l'ajout cree/ajuste les enregistrements DNS automatiquement.

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
