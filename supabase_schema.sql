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
