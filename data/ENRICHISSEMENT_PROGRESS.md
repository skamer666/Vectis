# Pilote d'enrichissement web des cabinets — journal de bord

Ce fichier est la mémoire du projet entre deux exécutions automatiques. Il est mis à jour à
chaque passage (manuel ou planifié). Toute exécution future — humaine ou automatisée — doit
commencer par le lire.

## Statut actuel (dernière mise à jour : 2026-07-22 18:35 UTC)

- **486** domaines uniques identifiés à partir des colonnes `site_web` des CSV Genève et Vaud
  (les 18 autres cantons n'ont pas cette colonne — voir "Phase de découverte" plus bas).
- **109** cabinets avec au moins un fait exploitable (année de fondation, taille d'équipe
  annoncée, et/ou liste de domaines de compétence formulée par le cabinet lui-même).
- **41** domaines testés sans succès (page vide/JS, contenu trop mince, chiffres non
  spécifiques à la Suisse, page trop volumineuse pour l'outil de fetch, ou site suspect).
- **336** domaines de la liste connue pas encore testés.
- Taux de réussite observé jusqu'ici : **~72.7%** (109 / 150 domaines réellement testés).
- Note technique : dans cet environnement, l'outil de fetch exige qu'une URL soit d'abord
  « vue » (recherche web) avant de pouvoir être récupérée directement ; chaque domaine est
  donc traité par une recherche web ciblée suivie d'un fetch de la page d'accueil (ou d'une
  sous-page pertinente), jamais sur la base du seul résumé de recherche.

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


### 2026-07-21 16:08 UTC — exécution automatisée (lot 2)

Lot de 20 domaines traités (les plus gros cabinets restants, GE/VD, par nombre d'avocats
décroissant). **18 succès / 2 échecs.**

Faits notables extraits : Bratschi SA fondée en 2008 (fusion de trois études, ~120
avocats et juristes annoncés) ; Etude Lion d'Or fondée en 1995 à Lausanne (22 personnes) ;
BM Avocats fondée en 1990 à Genève ; Etude Athena fondée en 2021 ; BOURG 8 Étude d'avocats
depuis 1987 ; TerrAvocats ouverte en 2019 (Lutry puis Genève) ; Baker McKenzie Suisse
indique plus de 130 avocats (chiffre explicitement suisse, statistiques mondiales du
réseau écartées conformément à la règle 4). Pour les autres succès (Ducrest & Heggli,
Relief Avocats, Alphalex, Tschumy Avocats, De-Beaumont 3, Beker Guiramand & Associés,
Locca Pion & Ryser, LBS/LBR Legal, Pyxis Law, Reiser Avocats, Gillioz Dorsaz & Associés),
seule une liste de domaines de compétence formulée par le cabinet a pu être retenue
(aucune année de fondation ni effectif chiffré explicitement annoncés sur leurs pages).

Échecs : geneva-lawyers.ch (SLRG Avocats — page consultée mais aucun fait chiffré ou
daté, domaines de droit décrits de façon trop générale) ; eversheds-sutherland.com
(pages Genève/Zurich renvoient un contenu quasi vide, probablement rendu en JavaScript).

Totaux cumulés après ce lot : 90 domaines testés au total (58 réussis / 32 échoués) sur
les 486 domaines connus. Il reste environ 396 domaines connus non testés, soit encore
~20 lots de 20 avant d'atteindre la phase de découverte (18 autres cantons).

Vérification post-build : régénération complète du site (`dist/`) sans erreur, échantillon
aléatoire de 40 pages avec `bad=0` artefact Jinja détecté. Entrée Bratschi SA vérifiée
manuellement sur sa fiche étude Genève (`/fr/avocats/geneve/etude/bratschi-sa/`) : les
faits (fondation 2008, ~120 avocats et juristes, domaines de compétence, date de
consultation) s'affichent correctement.


### 2026-07-21 18:15 UTC — exécution automatisée (lot 3)

Lot de 20 domaines traités (GE/VD restants, par nombre d'avocats décroissant). **16 succès /
4 échecs.**

Faits notables extraits : Bottge & Associés SA au barreau de Genève depuis 1998 ; GTHC
(Grobet Thorens Hohl-Chirazi) fondée en 2020 ; 100 Legal SA — histoire débutant en 2009 à
Genève (ex-100 Rhône Avocats, statistiques mondiales UAE/France/UK écartées, seul point
d'ancrage suisse retenu) ; Saint-Léger Avocats (lawyersgeneva.ch) fondée en 2014 ; MCLB
Avocats fondée en 2023 à Lausanne (4 associés explicitement annoncés) ; Noël & Associé.e.s
fondée en 1999 à Lausanne ; Rivara Wenger Cordonier & Amos fondée par Jacopo Rivara en 1986
(5 associés) ; Köstenbaum & Associés SA active depuis 1976 à Genève ; SF5 Avocats et Allia
(Lausanne) annoncent chacune 5 associés/avocats sans année de fondation précise. Pour
Renold et Associé.e.s (renold-gabus.ch, désormais renlaw.ch), BRS Berger Recordon & de
Saugy, id est avocats, Ventura & Associés, Skandamis Avocats et MWR Avocats, seule une
liste de domaines de compétence formulée par le cabinet a été retenue (années vagues du
type « depuis un quart de siècle » ou « plus de 35/40 ans » écartées conformément à la
règle 2 ; statistiques non locales écartées conformément à la règle 4).

Échecs : stralta.ch et interlegal.ch (contenu vide au fetch, rendu JavaScript probable,
plusieurs pages testées) ; avevey.ch (même symptôme sur trois pages différentes) ;
10decembre.ch (page d'accueil consultée mais aucune année de fondation, effectif chiffré,
ni liste de domaines de droit formulée explicitement par le cabinet lui-même).

Totaux cumulés après ce lot : 110 domaines testés au total (74 réussis / 36 échoués) sur
les 486 domaines connus. Il reste environ 376 domaines connus non testés, soit encore
~19 lots de 20 avant d'atteindre la phase de découverte (18 autres cantons).

Vérification post-build : régénération complète du site (`dist/`, 64628 fichiers
`index.html`) sans erreur, échantillon aléatoire de 40 pages avec `bad=0` artefact Jinja
détecté. Entrée Bottge & Associés SA vérifiée manuellement sur sa fiche étude Genève
(`/fr/avocats/geneve/etude/bottge-associes-sa/`) : la mention « Étude fondée en 1998 »
et la date de consultation (2026-07-21) s'affichent correctement.


### 2026-07-22 — exécution automatisée (lot 4)

Lot de 20 domaines traités (GE/VD restants, par nombre d'avocats décroissant). **16 succès /
4 échecs.**

Faits notables extraits : GVA law (gvalaw.com) fondée en 1938, plus de 80 ans d'existence,
liste complète de domaines de compétence (droit commercial, immobilier, bail, travail,
poursuites et faillites, assurances sociales, bancaire et financier, propriété
intellectuelle, pénal, arbitrage international) ; HOUSE attorneys (askhouse.ch) créée en
2018 ; Atlas Legal (atlaslegal.ch) fondée le 27 août 2024 (annonce explicite de création,
liste très étendue de domaines de compétence) ; M & Avocats (mavocats.ch) fondée en 2016
par Nicolas Mattenberger et Jessica Jaccoud ; Etude Richemont (etude-richemont.ch) —
effectif explicitement annoncé de 3 avocats expérimentés (et leurs 3 collaborateurs), liste
étendue de domaines de droit. Pour MBLD Associés, HABEAS Avocats, CG Partners (domaine CSV
cgpartners.ch, contenu réel constaté sur cg-partners.ch), JNC Avocats, Green Avocats, Peter
& Kim (statistiques mondiales du réseau écartées, seule la liste des expertises en
arbitrage retenue), lecocqassociate (effectif de 40+ professionnels écarté car réparti sur
4 bureaux internationaux, non spécifique à la Suisse, conformément à la règle 4),
SwissLegal (réseau national de cabinets, page de domaines de compétence commune retenue),
Integra Avocats, Mazou Avocats et Pétremand & Rappo, seule une liste de domaines de
compétence formulée par le cabinet lui-même a pu être retenue (aucune année de fondation ni
effectif chiffré explicitement annoncés, ou chiffres explicitement écartés car non
spécifiques à la Suisse).

Échecs : kaiser-bohler.com (contenu vide au fetch sur plusieurs URLs testées, page
d'accueil et sous-page "Information") ; msvavocates.ch (page d'accueil vide puis timeout
sur la page équipe, rendu JavaScript probable) ; hcml.ch et lexel.ch (timeout du fetch,
pages trop volumineuses ou lentes).

Totaux cumulés après ce lot : 130 domaines testés au total (90 réussis / 40 échoués) sur
les 486 domaines connus. Il reste environ 356 domaines connus non testés, soit encore
~18 lots de 20 avant d'atteindre la phase de découverte (18 autres cantons).

Vérification post-build : régénération complète du site (`dist/`, 65228 fichiers
`index.html`) sans erreur, échantillon aléatoire de 40 pages avec `bad=0` artefact Jinja
détecté. Entrée GVA law vérifiée manuellement sur sa fiche étude Genève
(`/fr/avocats/geneve/etude/gva-law/`) : la mention « fondée en 1938 (88 ans d'existence) »
s'affiche correctement.


### 2026-07-22 18:35 UTC — exécution automatisée (lot 5)

Lot de 20 domaines traités (GE/VD restants, par nombre d'avocats décroissant). **19 succès /
1 échec** — meilleur taux de réussite du pilote jusqu'ici.

Faits notables extraits : KT Legal SA (Kronbichler & Tourette) — Pascal Tourette « ouvre
l'Etude Kronbichler & Tourette en 2005 » (fait trouvé sur la bio d'un associé, pas sur une
page "à propos" générique) ; ABC Avocats (Nyon) — bloc de statistiques explicite sur la page
d'accueil : « 2023 Founded », « 5 Professionals », « 12 Fields of expertise » ; Sphera Étude
d'avocates — page d'actualités indique explicitement « Depuis le 1er juillet 2022 » (quatre
associées) ; Salomé Preile Associées — « Mes Salomé Daïna et Me Preile ont décidé de créer
leur propre étude en 2023 » (deux associées, deux collaborateurs) ; Libra Law — bandeau
d'accueil « Founded in 2007, Libra Law is a Swiss law firm specialising in Sports and Business
law » ; Leximmo avocat·e·s — « Founded in 2009 », composée de six avocats explicitement
annoncés ; Avocats Palud — bandeau d'accueil « Au plus près de vos intérêts depuis 1976 »
(année précise retenue, à la différence des formulations vagues type "depuis plus de X ans").
Pour Penalex (quatre avocats explicitement chiffrés, sans année de fondation précise —
seulement "20 ans de pratique" jugé trop vague pour l'outil Compass, non retenu), Dayer
Ahlström Fauconnet (page "à propos" trouvée être un gabarit WordPress non complété avec faux
noms et Lorem Ipsum, mais les pages "avocats" et "domaines d'activité" contenaient de vrais
faits exploitables), Faerus, KBLex, DWZ de Weck Zoells & Associés, Meyer Legal (droit de
l'aviation), WLM Avocats, Omnia Avocats, Etude Asteria, Peter & Moreau et André Associés
Avocats, seule une liste de domaines de compétence formulée par le cabinet lui-même a pu être
retenue (aucune année de fondation ni effectif chiffré explicitement annoncés, ou statistiques
de réseau international écartées conformément à la règle 4 — non applicable ici mais
vérifié systématiquement).

Échec : mvh-avocats.ch (contenu vide au fetch sur toutes les pages testées — accueil,
attorneys, contact-acces — rendu JavaScript probable, site non exploitable avec l'outil
actuel).

Totaux cumulés après ce lot : 150 domaines testés au total (109 réussis / 41 échoués) sur
les 486 domaines connus. Il reste environ 336 domaines connus non testés, soit encore
~17 lots de 20 avant d'atteindre la phase de découverte (18 autres cantons).

Vérification post-build : **incident technique de disque signalé pour information.** Le
bac à sable de cette exécution ne disposait que de ~848 Mo d'espace libre au démarrage du
build (disque système à 9,6 Go, en grande partie occupé par des fichiers résiduels d'autres
sessions non liées à ce projet, non supprimables faute de permissions). La régénération
complète a réussi pour Genève, Vaud et les cantons AG à ZG (dans l'ordre du build), mais a
échoué par manque d'espace disque pendant la génération des pages avocat individuelles de
Zurich (dernier canton de la boucle, le plus volumineux avec 4213 avocats). Ceci n'est pas
lié aux données modifiées dans ce lot : `dist/` n'est pas versionné dans Git (`.gitignore`),
le site réel est reconstruit par Vercel au déploiement avec des ressources qu'on suppose
suffisantes ; ce build local ne sert qu'à la vérification anti-régression avant push.
Vérification effectuée sur la portion réellement construite : échantillon aléatoire de 40
pages avec `bad=0` artefact Jinja détecté, plus vérification ciblée des 17 nouvelles fiches
étude (GE et VD) qui affichent toutes correctement leurs faits (ex. KT Legal SA « Étude
fondée en 2005 », ABC Avocats « Étude fondée en 2023 », Sphera « Étude fondée en 2022 »,
avec la date de consultation 2026-07-22). Donnée et code jugés sains ; seule la construction
locale complète (18 cantons) n'a pu être vérifiée intégralement faute d'espace disque dans
ce bac à sable. La prochaine exécution pourra retenter un build complet si l'espace disque
du bac à sable redevient suffisant.
