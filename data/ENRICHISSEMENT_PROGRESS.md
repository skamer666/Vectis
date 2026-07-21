# Pilote d'enrichissement web des cabinets — journal de bord

Ce fichier est la mémoire du projet entre deux exécutions automatiques. Il est mis à jour à
chaque passage (manuel ou planifié). Toute exécution future — humaine ou automatisée — doit
commencer par le lire.

## Statut actuel (dernière mise à jour : 2026-07-21)

- **486** domaines uniques identifiés à partir des colonnes `site_web` des CSV Genève et Vaud
  (les 18 autres cantons n'ont pas cette colonne — voir "Phase de découverte" plus bas).
- **40** cabinets avec au moins un fait exploitable (année de fondation, taille d'équipe
  annoncée, et/ou liste de domaines de compétence formulée par le cabinet lui-même).
- **30** domaines testés sans succès (page vide/JS, contenu trop mince, chiffres non
  spécifiques à la Suisse, page trop volumineuse pour l'outil de fetch, ou site suspect).
- **416** domaines de la liste connue pas encore testés.
- Taux de réussite observé jusqu'ici : **~57%** (40 / 70 domaines réellement testés).

Toutes les données sont dans `data/cabinet_web_enrichment.json` :
- chaque clé de premier niveau (hors `_meta` et `_failed`) est un nom de domaine avec des faits
  exploitables : `founding_year`, `team_size_n`, `practice_areas_fr`, `practice_areas_en`,
  `source_url`, `fetched_date`.
- `_failed` liste les domaines testés sans résultat exploitable, avec la raison — **ne jamais
  retester un domaine présent ici** (sauf ceux marqués "à revérifier plus tard", comme
  jmrlegal.ch qui semble compromis).
- `_meta` contient les compteurs globaux.

Ces données sont branchées dans `build.py` (fonctions `gen_ge_etudes` et `gen_canton_etudes`)
et s'affichent automatiquement sur les fiches étude (GE) quand le domaine du cabinet correspond
à une entrée du cache.

## Règles non négociables (méthodologie)

Ces règles ont été fixées dès le début du projet et **ne doivent jamais être assouplies**,
y compris par une exécution automatisée qui chercherait à aller plus vite :

1. **Aucune fabrication.** On extrait uniquement des faits explicitement écrits sur le site du
   cabinet (une année à 4 chiffres après "fondée en"/"depuis"/"gegründet", un nombre suivi de
   "avocats"/"juristes"/"collaborateurs", une liste de domaines de droit formulée par le
   cabinet). On ne résume jamais librement, on ne déduit jamais un chiffre à partir du nombre
   de membres listés sur une page équipe (ambigu : liste peut être partielle).
2. **Rien plutôt qu'une approximation.** Si l'année de fondation est vague ("depuis plus de 35
   ans", "plus de 100 ans"), on ne la convertit PAS en année précise — on la laisse de côté
   (`founding_year: null`).
3. **Toujours attribuer et dater.** Chaque entrée a `source_url` et `fetched_date` — ce sont eux
   qui alimentent la phrase "Certaines informations ci-dessus proviennent du site officiel du
   cabinet, consulté le [date]" affichée sur les fiches.
4. **Se méfier des chiffres non locaux.** Pour les gros cabinets internationaux (Walder Wyss,
   MLL, CMS, Charles Russell Speechlys...), les statistiques globales du réseau (ex. "10 000+
   collaborateurs dans le monde") ne sont PAS retenues — elles induiraient en erreur sur la
   taille de l'entité suisse. On ne prend que des chiffres explicitement suisses/locaux.
5. **Sites suspects → écarter, pas ignorer.** Si un site montre des signes de piratage (liens
   de spam, contenu injecté hors sujet), on le marque dans `_failed` avec la raison plutôt que
   de l'utiliser ou de le retester silencieusement plus tard.
6. **Respect du `robots.txt` implicite** : l'outil de fetch ne contourne aucun blocage. Un
   domaine qui bloque simplement le fetch (page vide) est noté en échec, jamais forcé.

## Comment une exécution automatisée doit procéder (rappel du protocole)

1. `git clone` frais du dépôt (le bac à sable ne persiste pas entre exécutions).
2. Lire `data/cabinet_web_enrichment.json` pour connaître l'état (`_meta`, clés réussies,
   `_failed`).
3. Recalculer la liste des 486 domaines depuis `data/avocats_geneve_enrichi.csv` et
   `data/avocats_vaud.csv` (colonne `site_web`), dédupliquer par nom de domaine, trier par
   nombre d'avocats décroissant.
4. Retirer les domaines déjà réussis et déjà en échec → c'est la file d'attente.
5. **Si la file d'attente est vide (liste des 486 épuisée) : passer en phase de découverte**
   (voir section suivante) au lieu de s'arrêter.
6. Prendre les 20 domaines suivants (les plus gros cabinets en premier).
7. Pour chacun : fetch, extraction stricte selon les règles ci-dessus, mise à jour du cache
   (succès → clé de premier niveau ; échec → `_failed` avec raison).
8. Régénérer le site (3 étapes habituelles : base+GE+static, boucle 19 cantons, search+sitemaps).
9. Vérification rapide : échantillon de 40 pages, doit donner `bad=0` artefacts Jinja.
10. Ajouter une entrée datée en bas de la section "Journal des exécutions" de ce fichier
    (nombre traité, nombre réussi/échoué, faits notables, total cumulé, restant estimé).
11. `git add -A && git commit` avec un message descriptif, puis push vers
    `https://github.com/skamer666/Vectis.git` en utilisant le token fourni pour
    l'authentification (URL distante temporaire, puis remise à l'URL propre après le push —
    ne jamais laisser le token dans l'URL du remote de façon permanente).

## Phase de découverte (après épuisement des 486 domaines connus)

Seuls Genève et Vaud ont une colonne `site_web` dans leurs CSV sources. Les 18 autres cantons
(AG, AI, BS, FR, GL, GR, JU, LU, NE, NW, OW, SG, SO, SZ, TG, UR, ZG, ZH) ont des cabinets mais
aucune URL connue. Une fois les 486 domaines connus épuisés, l'exécution automatisée doit :

1. Identifier, parmi les cabinets de ces 18 cantons (champ `etude` dans les CSV cantonaux),
   les plus gros regroupements par nombre d'avocats (même logique de priorisation que pour
   GE/VD : les gros cabinets en premier, rendement décroissant).
2. Rechercher leur site officiel via une recherche web ciblée (nom du cabinet + canton +
   "avocats"), en ne retenant que des résultats manifestement officiels (nom de domaine
   correspondant au nom du cabinet, pas un annuaire tiers).
3. Ajouter le domaine trouvé (ou l'absence confirmée de site) à un nouveau fichier
   `data/domaines_autres_cantons.json` avec la même structure que le cache principal, pour ne
   pas mélanger les domaines "connus via CSV" et "découverts par recherche" (traçabilité).
4. Une fois un domaine découvert, il suit exactement le même protocole d'extraction que
   ci-dessus.
5. **Si un cabinet n'a manifestement pas de site web** (recherche infructueuse, domaine
   expiré, ou mention explicite de son absence), l'écrire explicitement dans
   `data/domaines_autres_cantons.json` sous une clé `_sans_site` avec le nom du cabinet et la
   date de vérification — pour qu'on sache que la recherche a été faite et qu'il est inutile
   de la refaire.

## Journal des exécutions

### 2026-07-21 — session initiale (manuelle)

Pilote lancé et étendu manuellement sur plusieurs vagues au cours de la même conversation :
23 → 43 → 63 → 73 domaines testés progressivement, 13 → 24 → 33 → 40 cabinets avec faits
exploitables. Bug de traduction des langues parlées (affichées en français brut sur les pages
DE/IT/EN) découvert et corrigé au passage. Fichier `_failed` créé rétroactivement pour
consolider les échecs constatés au fil des vagues. Mise en place de ce journal et de
l'automatisation toutes les 30 minutes à partir de ce point.

*(les prochaines exécutions ajoutent leur entrée ci-dessous, la plus récente en bas)*
