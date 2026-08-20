-- Schema Supabase pour le systeme d'avis Legatis.
--
-- A executer une seule fois dans Supabase -> SQL Editor, sur un projet
-- fraichement cree par Greg (creation du projet lui-meme, jamais par Claude --
-- voir regles sur la creation de comptes). Une fois ce script execute et les
-- cles recuperees (Project URL, anon/public key, service_role key), donner
-- les trois valeurs a Claude pour brancher api/review-submit.js (secrete,
-- variable d'environnement Vercel SUPABASE_SERVICE_ROLE_KEY) et le widget
-- d'affichage cote client (publique, constantes SUPABASE_URL / SUPABASE_ANON_KEY
-- dans supabase_config.py).
--
-- Moderation : pas de page d'administration dediee dans ce depot. Greg
-- modere directement dans Supabase -> Table Editor -> reviews : changer la
-- colonne `status` de 'pending' a 'approved' (ou 'rejected'). L'avis apparait
-- sur le site en quelques secondes (widget cote client, pas besoin de rebuild).

create extension if not exists pgcrypto;

create table if not exists reviews (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  status text not null default 'pending' check (status in ('pending', 'approved', 'rejected')),
  canton_code text not null,
  avocat_slug text not null,
  avocat_nom text not null,
  rating smallint not null check (rating between 1 and 5),
  title text,
  body text not null check (char_length(body) <= 3000),
  reviewer_name text,
  reviewer_email text not null,
  lang text not null default 'fr',
  moderated_at timestamptz,
  lawyer_response text,
  lawyer_response_at timestamptz
);

create index if not exists reviews_avocat_idx on reviews (canton_code, avocat_slug, status);

alter table reviews enable row level security;

-- Lecture publique : uniquement les avis approuves (clef anon, utilisee cote
-- client sur les fiches avocat). Jamais reviewer_email n'est cense etre
-- affiche par le front (le widget ne le demande jamais), mais par prudence
-- on pourrait aussi restreindre les colonnes lisibles via une vue dediee si
-- besoin plus tard.
drop policy if exists "public read approved reviews" on reviews;
create policy "public read approved reviews"
  on reviews for select
  using (status = 'approved');

-- Aucune policy d'insertion / mise a jour / suppression publique : tous les
-- ecrits passent par api/review-submit.js avec la service_role key (qui
-- contourne RLS), jamais directement depuis le navigateur avec la clef anon.


-- ============================================================================
-- Schema pour la capture d'email (lead magnet discret sur les fiches
-- avocat/etude). A executer dans le meme projet Supabase que `reviews`,
-- toujours via Supabase -> SQL Editor. Cote client (api/lead-capture.js)
-- utilise la meme SUPABASE_SERVICE_ROLE_KEY que review-submit.js.
--
-- Aucun envoi d'email automatique n'est effectue par ce script ni par
-- l'API : les leads s'accumulent dans cette table, a consulter/exporter
-- depuis Supabase -> Table Editor -> leads, ou a brancher plus tard sur
-- un outil d'emailing/automatisation (Zapier, Make, webhook Supabase...).
-- ============================================================================

create table if not exists leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  status text not null default 'pending' check (status in ('pending', 'sent', 'ignored')),
  email text not null,
  page_url text not null,
  page_title text,
  lang text not null default 'fr'
);

create index if not exists leads_created_idx on leads (created_at desc);

alter table leads enable row level security;

-- Aucune policy de lecture/ecriture publique : tous les acces passent par
-- api/lead-capture.js (insertion, service_role key) ou par Greg directement
-- dans le Table Editor Supabase (lecture, cle du compte proprietaire).


-- ============================================================================
-- Schema pour la verification d'identite des avocats (revendication de
-- fiche) ET la creation de leur compte de connexion. A executer dans le
-- meme projet Supabase que reviews/leads.
--
-- Le mot de passe du compte est choisi des la demande initiale (pas apres
-- coup) : api/verification-request.js pre-cree tout de suite le compte
-- Supabase Auth correspondant a account_email, mais BLOQUE
-- (email_confirm=false) -- Supabase securise et stocke le mot de passe des
-- cette etape, ce depot ne le voit ni ne le stocke jamais lui-meme. Le
-- compte ne devient utilisable (connexion possible) qu'a la confirmation de
-- l'identite, qui bascule email_confirm=true et cree la ligne
-- lawyer_accounts (voir plus bas) :
--   - palier email  -> lien de confirmation a usage unique envoye a
--     l'adresse deja publiee pour la fiche ; auto-approuve des le clic
--     (api/verification-confirm.js). Le compte est cree avec CET email --
--     account_email doit correspondre exactement, verifie cote serveur.
--   - palier telephone -> Greg rappelle manuellement le numero deja publie
--     sur la fiche (jamais un numero saisi par le demandeur), puis valide
--     depuis /interne/verification-avocats/ (api/verification-decide.js).
--   - palier document -> carte de legitimation d'avocat (ou brevet) +
--     selfie, stockes dans le bucket prive verification-documents,
--     examines manuellement par Greg puis SUPPRIMES IMMEDIATEMENT apres la
--     decision (approbation ou refus), quel que soit son sens.
-- Les 3 paliers restent TOUJOURS proposes au demandeur (meme si un email ou
-- un telephone est deja connu pour sa fiche) au cas ou celui-ci serait
-- errone -- seul le palier choisi doit rester cote serveur un canal de
-- confiance reel (email : doit matcher l'adresse deja publiee ; telephone :
-- doit exister deja ; document : toujours disponible).
-- En cas de refus (palier telephone/document), le compte pre-cree est
-- SUPPRIME (api/verification-decide.js) pour liberer l'adresse email.
--
-- Securite : RLS activee, AUCUNE policy pour anon/authenticated (ni lecture,
-- ni ecriture). Seule la service_role key (jamais exposee cote client, lue
-- uniquement depuis les variables d'environnement Vercel) peut toucher
-- cette table -- elle contourne RLS par conception. Idem pour le bucket de
-- stockage : prive, sans policy publique, seule la service_role key peut y
-- lire/ecrire/supprimer.
-- ============================================================================

create table if not exists verification_requests (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  status text not null default 'pending' check (status in ('pending', 'approved', 'rejected')),
  method text not null check (method in ('email', 'phone', 'document')),
  canton text not null,
  avocat_slug text not null,
  avocat_nom text not null,
  avocat_url text not null,
  lang text not null default 'fr',
  -- Email + mot de passe choisis des la demande initiale (le mot de passe
  -- lui-meme n'est jamais stocke ici, uniquement dans auth.users via
  -- adminCreateUser -- voir _verification-lib.js).
  account_email text not null,
  pending_user_id uuid references auth.users(id) on delete set null,
  -- Consentement FACULTATIF (case decochee par defaut cote formulaire) pour
  -- recevoir d'autres emails Legatis que ceux lies a la creation/activation
  -- du compte. Recopie sur lawyer_accounts au moment de l'activation -- voir
  -- api/verification-confirm.js / api/verification-decide.js.
  marketing_consent boolean not null default false,
  contact_note text,
  document_path text,
  selfie_path text,
  token_hash text,
  token_expires_at timestamptz,
  email_sent boolean not null default false,
  decided_at timestamptz,
  decided_by text,
  -- Offre "site web gratuit" presentee juste apres la creation du compte
  -- (avant validation de l'identite) -- voir website_offer_content.py et
  -- api/website-offer-decision.js. null tant que l'avocat n'a pas encore
  -- repondu a l'offre (ce qui reste possible : rien ne bloque la demande de
  -- verification elle-meme si l'offre est ignoree cote client). true/false
  -- une fois qu'il a explicitement accepte ou refuse.
  free_website_interest boolean,
  -- Horodatage + version du contrat au moment de l'acceptation electronique
  -- (case cochee + defilement complet obligatoire côté client, revérifié
  -- cote serveur par la version attendue -- voir api/website-offer-decision.js).
  -- Reste null si l'offre a ete refusee ou jamais presentee.
  free_website_contract_accepted_at timestamptz,
  free_website_contract_version text
);

create index if not exists verification_requests_status_idx on verification_requests (status, created_at desc);

alter table verification_requests enable row level security;

-- Aucune policy de lecture/ecriture publique, volontairement : ni les
-- demandes en attente, ni les liens de stockage, ni le token de
-- confirmation ne doivent jamais transiter par la cle anon publique. Tous
-- les acces (insertion depuis le formulaire, lecture/decision depuis la
-- page interne, confirmation du lien email) passent par les fonctions
-- serverless api/verification-*.js avec la service_role key.

-- Bucket de stockage prive pour la carte de legitimation/brevet + le
-- selfie (palier 3 uniquement). Cree ici par SQL pour que la mise en place
-- soit reproductible depuis ce seul script -- Greg peut aussi le creer a la
-- main depuis Supabase -> Storage en cochant bien "Private bucket" si cette
-- requete echoue selon la version du projet.
insert into storage.buckets (id, name, public)
values ('verification-documents', 'verification-documents', false)
on conflict (id) do nothing;

-- Aucune policy de storage publique n'est ajoutee ici : par defaut, un
-- bucket prive sans policy storage.objects n'est accessible ni en lecture
-- ni en ecriture via la clef anon/authenticated, seulement via la
-- service_role key cote serveur (upload dans verification-request.js,
-- generation d'URL signee temporaire dans verification-list.js, suppression
-- immediate dans verification-decide.js).


-- ============================================================================
-- Schema pour les comptes avocat (connexion + profil complementaire).
-- A executer dans le meme projet Supabase que les schemas ci-dessus.
--
-- Principe : Supabase Auth (auth.users, email + mot de passe) gere
-- l'authentification elle-meme -- aucun mot de passe ne transite ni n'est
-- stocke par ce depot. Le compte auth.users est pre-cree des la demande de
-- verification (verification_requests.pending_user_id) mais reste bloque
-- (email_confirm=false) tant que l'identite n'est pas confirmee. Le lien
-- auth.users <-> fiche du registre (table lawyer_accounts) n'est cree
-- qu'A CE MOMENT LA, par api/verification-confirm.js (palier email) ou
-- api/verification-decide.js (palier telephone/document) avec la
-- service_role key, jamais un choix laisse au client -- sinon n'importe qui
-- pourrait s'inscrire en se pretendant n'importe quel avocat du registre.
--
-- Une fois connecte, l'avocat peut soumettre du contenu complementaire
-- (photo, presentation, coordonnees affichees, liens) sur /mon-profil/,
-- avec le meme modele "append-only + moderation" que les avis : chaque
-- soumission est une nouvelle ligne en attente, jamais modifiee en place ;
-- la derniere approuvee reste affichee publiquement (widget cote client,
-- meme principe que _reviews_widget.html) pendant qu'une nouvelle
-- soumission est en cours de revision, pour ne jamais faire disparaitre le
-- profil public le temps que Greg la traite depuis
-- /interne/verification-avocats/.
-- ============================================================================

create table if not exists lawyer_accounts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null unique references auth.users(id) on delete cascade,
  canton text not null,
  avocat_slug text not null,
  avocat_nom text not null,
  avocat_url text not null,
  -- Copie de verification_requests.marketing_consent au moment de
  -- l'activation du compte : c'est cette valeur-ci qui fait foi une fois le
  -- compte actif (utilisation future pour d'eventuelles campagnes email).
  marketing_consent boolean not null default false,
  created_at timestamptz not null default now()
);

create unique index if not exists lawyer_accounts_fiche_idx on lawyer_accounts (canton, avocat_slug);

alter table lawyer_accounts enable row level security;

drop policy if exists "self read lawyer account" on lawyer_accounts;
create policy "self read lawyer account"
  on lawyer_accounts for select
  using (user_id = auth.uid());

-- Aucune policy d'insertion/mise a jour/suppression, meme pour le
-- proprietaire : ce lien identite <-> fiche est etabli une fois, au moment
-- de la confirmation d'identite (service_role, verification-confirm.js /
-- verification-decide.js), et n'a jamais vocation a changer depuis le
-- navigateur.


create table if not exists lawyer_profile_submissions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  canton text not null,
  avocat_slug text not null,
  status text not null default 'pending' check (status in ('pending', 'approved', 'rejected')),
  bio text check (bio is null or char_length(bio) <= 3000),
  photo_path text,
  display_email text check (display_email is null or display_email ~* '^[^\s@]+@[^\s@]+\.[^\s@]+$'),
  display_telephone text check (display_telephone is null or char_length(display_telephone) <= 40),
  links jsonb,
  submitted_at timestamptz not null default now(),
  decided_at timestamptz,
  decided_by text
);

create index if not exists lawyer_profile_submissions_fiche_idx on lawyer_profile_submissions (canton, avocat_slug, status);
create index if not exists lawyer_profile_submissions_user_idx on lawyer_profile_submissions (user_id, submitted_at desc);

alter table lawyer_profile_submissions enable row level security;

-- Lecture publique : uniquement la derniere soumission approuvee (widget
-- client sur les fiches avocat, meme principe que les avis).
drop policy if exists "public read approved profile submissions" on lawyer_profile_submissions;
create policy "public read approved profile submissions"
  on lawyer_profile_submissions for select
  using (status = 'approved');

-- L'avocat connecte voit TOUTES ses propres soumissions (y compris en
-- attente/refusees), pour afficher un statut clair sur /mon-profil/.
drop policy if exists "self read own profile submissions" on lawyer_profile_submissions;
create policy "self read own profile submissions"
  on lawyer_profile_submissions for select
  using (user_id = auth.uid());

-- L'avocat connecte peut soumettre une nouvelle version, mais UNIQUEMENT
-- pour la fiche a laquelle son compte est lie (jointure contre
-- lawyer_accounts) -- jamais une fiche arbitraire choisie cote client.
drop policy if exists "self insert own profile submission" on lawyer_profile_submissions;
create policy "self insert own profile submission"
  on lawyer_profile_submissions for insert
  with check (
    user_id = auth.uid()
    and exists (
      select 1 from lawyer_accounts la
      where la.user_id = auth.uid()
        and la.canton = lawyer_profile_submissions.canton
        and la.avocat_slug = lawyer_profile_submissions.avocat_slug
    )
  );

-- Aucune policy update/delete pour authenticated : les soumissions sont
-- immuables une fois creees (modifier = soumettre une nouvelle version).
-- La moderation (passage a approved/rejected) passe par la service_role
-- key, depuis la page interne /interne/verification-avocats/.


-- Bucket public pour les photos de profil : contenu non sensible, destine
-- a devenir public une fois approuve. Chaque avocat ne peut ecrire que
-- sous son propre prefixe {auth.uid()}/... (policy storage ci-dessous) ;
-- une photo pas encore approuvee n'est reliee depuis aucune page du site
-- tant que Greg ne l'a pas validee, meme si le bucket est techniquement
-- public.
insert into storage.buckets (id, name, public)
values ('lawyer-photos', 'lawyer-photos', true)
on conflict (id) do nothing;

drop policy if exists "lawyer upload own photo" on storage.objects;
create policy "lawyer upload own photo"
  on storage.objects for insert
  with check (bucket_id = 'lawyer-photos' and (storage.foldername(name))[1] = auth.uid()::text);

drop policy if exists "lawyer replace own photo" on storage.objects;
create policy "lawyer replace own photo"
  on storage.objects for update
  using (bucket_id = 'lawyer-photos' and (storage.foldername(name))[1] = auth.uid()::text);

drop policy if exists "public read lawyer photos" on storage.objects;
create policy "public read lawyer photos"
  on storage.objects for select
  using (bucket_id = 'lawyer-photos');


-- ============================================================================
-- Schema pour l'analytics "maison" (respectueuse de la vie privee), voir
-- api/track.js (ecriture), api/analytics-summary.js (lecture agregee,
-- protegee par jeton admin) et static/js/analytics.js (collecte cote
-- client). Objectif : mesurer l'engagement (pages vues, temps sur page,
-- profondeur de defilement, taux de rebond approximatif, visiteurs
-- recurrents) pour guider les futures experiences de gamification, sans
-- dependre d'un outil tiers (Google Analytics et consorts) et sans
-- collecter de donnees personnelles identifiantes.
--
-- Choix de confidentialite deliberes (voir aussi la page /confidentialite/,
-- mise a jour en consequence) :
--   - Aucune adresse IP n'est stockee, meme temporairement.
--   - Aucun cookie : les identifiants ci-dessous vivent en sessionStorage
--     (session_id, remis a zero a chaque nouvelle session de navigation) et
--     en localStorage (visitor_id, persistant mais totalement anonyme --
--     un UUID aleatoire genere cote client, jamais relie a un email, un
--     compte ou une IP). Seuls des compteurs agreges (ex: "% de visiteurs
--     revenus un autre jour") sont calcules a partir de visitor_id ; aucun
--     tableau de bord n'expose de donnees au niveau d'un visitor_id
--     individuel.
--   - referrer_domain ne stocke que le nom de domaine du referrer (ex:
--     "google.com"), jamais l'URL complete (qui peut contenir des
--     parametres de recherche identifiants).
--   - device_type est une categorie grossiere (mobile/tablet/desktop)
--     deduite cote client de la largeur de fenetre, jamais une empreinte
--     detaillee (pas de user-agent brut stocke).
create table if not exists analytics_events (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  event_type text not null,
  path text not null,
  lang text,
  canton text,
  referrer_domain text,
  device_type text check (device_type is null or device_type in ('mobile', 'tablet', 'desktop')),
  session_id text not null,
  visitor_id text not null,
  meta jsonb
);

create index if not exists analytics_events_created_idx on analytics_events (created_at desc);
create index if not exists analytics_events_type_idx on analytics_events (event_type, created_at desc);
create index if not exists analytics_events_path_idx on analytics_events (path, created_at desc);

alter table analytics_events enable row level security;

-- Aucune policy de lecture/ecriture publique : l'ecriture passe par
-- api/track.js (insertion, service_role key) et la lecture agregee par
-- api/analytics-summary.js (jeton admin, meme principe que
-- /interne/verification-avocats/), jamais par le client directement.
