"""Constantes publiques Supabase (projet + cle anon), embarquees dans les
pages statiques cote client pour le widget d'avis (templates/_reviews_widget.html)
et lues par build.py pour decider si le widget doit s'afficher.

Ce ne sont PAS des secrets : la cle anon Supabase est concue pour etre
publique, protegee par les policies RLS de supabase_schema.sql (lecture
seule, uniquement les avis approuves). La cle service_role (secrete, seule
capable d'inserer/modifier) ne va jamais ici -- elle vit uniquement en
variable d'environnement Vercel (SUPABASE_SERVICE_ROLE_KEY), lue par
api/review-submit.js.

Tant que SUPABASE_URL est vide, gen_avis_request() et le widget d'avis ne
sont pas generes : rien ne casse, aucun lien mort n'apparait sur le site.
Une fois le projet Supabase cree par Greg (creation de compte -- jamais par
Claude) et supabase_schema.sql execute, renseigner les deux valeurs
ci-dessous (visibles dans Supabase -> Project Settings -> API) suffit a
activer la fonctionnalite au prochain build.
"""

SUPABASE_URL = "https://qjiyxhsnrzahdmdvzsqi.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_6ea4cRTyW51Fk3h9ud9ibw_ffYFHdr2"
# force redeploy: SUPABASE_SERVICE_ROLE_KEY env var
