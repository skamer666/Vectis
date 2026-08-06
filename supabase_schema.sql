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
