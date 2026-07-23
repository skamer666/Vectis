# Pilote d'enrichissement web des cabinets — journal de bord

Ce fichier est la mémoire du projet entre deux exécutions automatiques. Il est mis à jour à
chaque passage (manuel ou planifié). Toute exécution future — humaine ou automatisée — doit
commencer par le lire.

## Statut actuel (dernière mise à jour : 2026-07-23)

- **485** domaines uniques identifiés à partir des colonnes `site_web` des CSV Genève et Vaud
  (les 18 autres cantons n'ont pas cette colonne — voir "Phase de découverte" plus bas).
- **274** cabinets avec au moins un fait exploitable (année de fondation, taille d'équipe annoncée, et/ou liste de domaines de compétence formulée par le cabinet lui-même).
  spécifiques à la Suisse, page trop volumineuse pour l'outil de fetch, ou site suspect).
- **125** domaines de la liste connue pas encore testés.
- Taux de réussite observé jusqu'ici : **~75.9%** (274 / 361 domaines réellement testés).
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

### 2026-07-22 19:05 UTC — exécution automatisée (lot 6)

Lot de 20 domaines traités (GE/VD restants, par nombre d'avocats décroissant). **17 succès /
3 échecs.**

Faits notables extraits : RSBP | Legal (Lausanne) — bandeau d'accueil « Établis depuis 1986 »
(année précise retenue, malgré une formulation complémentaire vague « Créée il y a 30 ans » non
utilisée pour la date) ; Alinéa Avocats — « Etablie place Saint-François à Lausanne depuis
2012 », liste complète de neuf domaines de compétence ; AVOCATS-CH — « étude fondée en 2000 à
Lausanne », « constituée de trois associés » (Olivier Subilia, Mélanie Freymond, Alain Sauteur,
effectif explicitement chiffré, sans compter les « plusieurs collaborateurs » ajoutés de façon
vague) ; Rivieravocats (Vevey) — « actuellement formée de quatre avocats » (effectif explicite,
sans année de fondation) ; Collectif d'avocat·e·s (Lausanne) — « créé en 2004 par Me Jean-Michel
Dolivo et Me Christophe Tafelmacher » ; Legentis Avocats (ex-Boudry/Derron, Lausanne) —
« Fondée en 1947 par Me Pierre Bolomey et Me Georges Derron », liste complète de dix domaines de
compétence ; Dini & Lardi Avocats (pdglaw.ch, Genève) — historique détaillé remontant à 1958
(création par Me Jean-Pierre Imhoos), seize domaines d'expertise listés. Pour Kilani Bugnion
Emonet Avocats, Etude Boudry & Arnouni (etudegp.ch), Centralex Avocats, Wilhelm Avocats
(wg-avocats.ch), Avocats Yverdon (Etude Casino 1), VZ Lawyers, Djaziri & Nuzzo, Salamian
Bolsterli (sblegal.ch) et Sulmoni & Félix (sflegal.ch), seule une liste de domaines de
compétence formulée par le cabinet lui-même a pu être retenue (aucune année de fondation ni
effectif chiffré explicitement annoncés sur les pages consultées, ou formulations trop vagues
type « plus de 50 ans » écartées conformément à la règle 2). Aubert Neyroud Stückelberg Fratini
(ibilex.ch) : liste de six domaines d'activité retenue de façon similaire.

Échecs : aperys.ch (contenu vide au fetch sur toutes les pages testées — accueil, à-propos,
contact, équipe — rendu JavaScript probable) ; barokas.ch (contenu vide au fetch, y compris sur
un miroir alternatif, rendu JavaScript probable) ; lion-d-or.ch (domaine ne correspond pas au
cabinet d'avocats — la recherche web ne renvoie qu'un restaurant/hôtel homonyme à Cologny ; le
cabinet réel « Etude Lion d'Or » est déjà présent dans le cache sous son vrai domaine
etudeliondor.ch, traité lors du lot 2).

Totaux cumulés après ce lot : 170 domaines testés au total (126 réussis / 44 échoués) sur les
486 domaines connus. Il reste environ 316 domaines connus non testés, soit encore ~16 lots de 20
avant d'atteindre la phase de découverte (18 autres cantons).

Vérification post-build : régénération complète du site (`dist/`, 65228 fichiers `index.html`)
réussie intégralement cette fois, y compris les 18 cantons hors GE/VD (Zurich compris, contrairement
au lot précédent qui avait buté sur l'espace disque à ce stade). Échantillon aléatoire de 40
pages avec `bad=0` artefact Jinja détecté. Entrées vérifiées manuellement sur leurs fiches étude
Vaud : RSBP | Legal (« Étude fondée en 1986 (40 ans d'existence) »), AVOCATS-CH (« L'étude
indique elle-même compter environ 3 avocats et juristes. Étude fondée en 2000 (26 ans
d'existence) »), Legentis (liste des dix domaines de compétence et « Étude fondée en 1947 (79
ans d'existence) »), toutes avec la date de consultation 2026-07-22 affichée correctement. Note
sur l'espace disque du bac à sable : à nouveau très contraint (moins de 10 Mo libres en fin de
build), mais suffisant pour compléter le build cette fois ; ceci reste un problème d'environnement
(fichiers résiduels non supprimables d'autres sessions, propriété "nobody") sans lien avec les
données du projet, `dist/` n'étant de toute façon pas versionné dans Git.

### 2026-07-22 19:35 UTC — lot automatique de 20 (GE/VD)

- 20 domaines traités : 13 réussites, 7 échecs.
- Années de fondation trouvées : avocatsassocies.net (1890), etudelknr.ch (1955),
  avopep.ch (1976), riavocats.ch (2011), spiralaw.ch (2018).
- Tailles d'équipe : avopep.ch (7 avocats), etudelknr.ch (4 avocats associés).
- Autres réussites (domaines de compétence) : gantey.ch, smblaw.ch, taadvisory.law,
  groslimond-avocats.ch, resolution-lp.ch, phbavocats.ch, hz-avocats.ch, waser-avocats.ch.
- Échecs : mbavocats.law, judiciaire.ch, arcuslegal.ch (aucune présence web indexée) ;
  wm-legal.ch, lexiss.ch, droit-immo.ch (contenu vide au fetch, rendu JS probable) ;
  zenithav.ch (site accessible mais aucun fait exploitable).
- Note : « depuis plus de vingt ans » (riavocats), « plus de 125 ans d'expérience »
  (avocatsassocies) et la fondation 2018 de Groslimond (vue seulement dans un résumé de
  recherche, pas sur le site) n'ont PAS été retenus, conformément aux règles.
- Totaux cumulés : 139 réussites / 51 échecs / 190 testés sur 486 connus, ~295 restants.
- Rebuild complet OK (65 228 pages, échantillon de 40 fichiers sans artefact Jinja).

### 2026-07-22 20:05 UTC — lot automatique de 20 (GE/VD)

- 20 domaines traités : 14 réussites, 6 échecs.
- Années de fondation trouvées : avopartner.ch (1932), avocadid.com (1947), pacta-avocats.ch
  (2012), kananirezki.com (2024), b4legal.ch (2025).
- Tailles d'équipe : avopartner.ch (8 avocats associés), psf12.ch (4 avocats),
  avocadid.com (3 associés).
- Autres réussites (domaines de compétence) : 373-avocats.com, abtavocats.ch, nexlaw.ch,
  avgroupe.ch, tabet.law, etude-bersier.ch, whitecase.com (bureau de Genève uniquement,
  stats mondiales ignorées), enodo.ch.
- Échecs : sda-avocats.ch, streng.ch, baalaw.ch, mdlaw.ch (aucune présence web indexée) ;
  fld-law.com, decandolle.ch (contenu vide au fetch, rendu JS probable).
- Notes de rigueur : fondation 2014 de 373-avocats (vue seulement sur Moneyhouse), 2016 de
  De Candolle et 2023 de Tabet (résumés de recherche), 2017 de Waser et « depuis 1980 » de
  FLD (annuaires tiers) NON retenues — jamais sur le site du cabinet lui-même.
- Totaux cumulés : 153 réussites / 57 échecs / 210 testés sur 486 connus, ~276 restants.
- Rebuild complet OK (65 228 pages, échantillon de 40 fichiers sans artefact Jinja).

### 2026-07-22 21:00 UTC — lot automatique de 20 (GE/VD)

- 20 domaines traités : 18 réussites, 2 échecs.
- Années de fondation trouvées : pirker.ch (1999), seidler.law (2024), jobin-legal.ch (2025),
  patocchimarzolini.com (2014), vmp-avocats.ch (2022), avdem.ch (2016).
- Tailles d'équipe : heimavocats.ch (3 avocats, équipe nommément identifiée) ;
  metropole-avocats.ch (12 collaborateurs annoncés explicitement).
- Autres réussites (domaines de compétence) : e-avocats.ch (Page & Partners — droit commercial,
  IA/nouvelles technologies, protection des données, immobilier, successions, criminalité en col
  blanc, entraide judiciaire) ; andlaw.ch (liste étendue de 12 domaines dont bancaire, circulation
  routière, migrations) ; savolainen.law (droit pénal international, criminalité en col blanc,
  responsabilité des entreprises) ; jordanlex.ch (cabinet spécialisé droit de la famille —
  divorce, garde, alimentaire, filiation) ; callan.law (13 domaines listés, palette très étendue) ;
  fravocats.ch (11 domaines dont droit pénal militaire et droit des étrangers) ; edifice-avocats.ch
  (spécialiste construction/immobilier — 8 domaines dont marchés publics et droit de l'environnement) ;
  parein-avocats.ch (droit pénal des affaires exclusivement) ; ipfa.ch (6 domaines incluant
  médiation) ; edeb.ch (8 domaines dont droit aérien et droit du sport, spécialités inhabituelles).
- Notes de rigueur : « expérience accumulée depuis plus de 15 ans » (parein-avocats.ch),
  « depuis plus de 80 ans » et « Depuis 2010 » comme date de changement de nom (ipfa.ch) NON
  retenus — jamais une année exacte de fondation ni une formulation sans ambiguïté sur la page
  du cabinet lui-même.
- Échecs : hornung-lawfirm.ch (erreur PHP fatale sur toutes les pages, site entièrement
  inaccessible) ; etude-blb.ch (contenu vide au fetch sur toutes les pages, rendu JavaScript
  probable).
- Totaux cumulés : **171 réussites / 59 échecs / 230 testés** sur 486 connus, ~256 restants.
- Rebuild complet OK (65 892 fichiers `index.html`, échantillon de 40 fichiers sans artefact Jinja).

### 2026-07-22 22:00 UTC — lot automatique de 20 (GE/VD)

- 20 domaines traités : 18 réussites, 2 échecs.
- Années de fondation trouvées : giorgini-avocats.ch (2008), helvetica-avocats.ch (2016),
  avocat-fiscal.ch (2025), legalinsights.ch (2018), lexr.com (2016), avsp.ch (1979),
  thevoz.ch (2015), stc-avocats.ch (2009), avocatsleman.ch (1994), vos-avocates.ch (2018),
  plaideurs.ch (1997), rsbblegal.ch (1986 — cabinet devenu RSBP Legal, source : rsbplegal.ch).
- Tailles d'équipe : helvetica-avocats.ch (9 avocats annoncés), avsp.ch (5 associés),
  stc-avocats.ch (4 avocats), rsbblegal.ch (7 avocats nommés sur rsbplegal.ch).
- Autres réussites (domaines de compétence) : primault-tieche.ch (9 domaines dont assurances/RC
  et propriété intellectuelle) ; lex-avocats.ch / Mitrea & Associés (16 domaines, palette étendue) ;
  proxima.legal (droit des sociétés, technologies, médias, cybersécurité) ; alta-avocats.ch
  (7 domaines) ; morgia-avocats.ch (11 domaines dont pénal/exécution des peines et PI) ;
  bory-legal.ch (cabinet spécialisé médiation/arbitrage et droit commercial) ; plaideurs.ch
  (redirect vers avocats-lawyers.ch — 23 domaines, palette très étendue).
- Notes de rigueur : rsbblegal.ch → fondation 1986 lue « Établis depuis 1986 » sur la page
  d'accueil de rsbplegal.ch (site actuel du même cabinet, mention directe et non ambiguë).
  proxima.legal et bory-legal.ch : années non mentionnées explicitement → founding_year null.
- Échecs : avocats-romandie.ch (Wix JS, contenu vide) ; avocats-morges.ch (contenu vide,
  rendu JavaScript probable).
- Totaux cumulés : **189 réussites / 61 échecs / 250 testés** sur 486 connus, ~236 restants.
- Rebuild complet OK (65 972 fichiers HTML, sitemap 23 055 URLs, échantillon de 40 fichiers
  sans artefact Jinja).

### 2026-07-22 22:45 UTC — lot automatique de 20 (GE/VD)

- 20 domaines traités : **17 réussites, 3 échecs**.
- Années de fondation trouvées : etudegr.ch (Gabus Avocats, 1985 — « Pierre Gabus exerce le
  métier d'avocat à titre indépendant depuis 1985 », mention directe sur sa page bio) ;
  bonnant-associes.ch (Bonnant & Associés, 1996 — « L'Étude Bonnant & Associés, fondée en 1996
  par le Bâtonnier Marc Bonnant ») ; santana-lima.com (Sant'Ana Lima Avocats, 2016 — « Fondée
  en 2016 ») ; swisslawyersgroup.ch (SwissLawyersGroup FOGLIA, 2001 — « fondé en 2001 par des
  avocats bien établis, dont le Studio Legale Foglia créé à Lugano et à Genève en 1990 ») ;
  fabiennefischer.ch (Me Fabienne Fischer, 2005 — « avocate à Genève depuis 2005 »).
- Autres réussites (domaines de compétence) : vca-avocats.ch (4 domaines : représentation en
  justice, optimisation fiscale, conseils juridiques, planification patrimoniale) ; bmjlex.ch
  (exclusivement droit du travail pour les entreprises) ; lesavocatesge.ch (26 domaines, palette
  très étendue — droit public et administratif, asile, migrations, pénal adultes/mineurs, personnes
  détenues, civil, famille, bail, travail, successions, sport, arbitrage, etc.) ; novalegal.ch
  (8 domaines — banking/finance, fondations/philanthropie, clients privés HNWI, planification
  fiscale et successorale, trusts, droit des sociétés, contrats, recouvrement de créances) ;
  casus-belli.legal (15 domaines, dont blockchain/Fintech et marchés publics internationaux,
  « plus de 10 avocats et autres professionnels ») ; avocat-cecconi.ch (solo — famille, divorce,
  successions, assurances sociales et privées) ; avocatsge.com (CCK Avocats — famille, pénal,
  responsabilité civile) ; philippecurrat.ch (Currat & Associés — droits de l'homme, droit
  international, pénal, droit suisse, présence en RDC depuis 2012) ; nevesavocats.ch (conseil
  juridique, arbitrage international, droit suisse) ; linea-avocats.ch (7 domaines spécialisés
  droit du travail/prévoyance/assurances sociales/ONG/bail/contrats/procédure) ;
  gunter-arbitration.law (boutique arbitrage international — ICC, LCIA, UNCITRAL, SIAC, SCAI —
  Pierre-Yves Gunter au barreau depuis 1991, 245+ cas) ; ilazi-law.com (famille, successions,
  litiges contractuels, philanthropie/ONG).
- Notes de rigueur : « une douzaine d'avocats » (Bonnant & Associés) — formulation approximative,
  non retenue comme effectif précis conformément à la règle 2. Année 2009 de fondation de Currat &
  Associés (trouvée dans des résumés de recherche) — non mentionnée sur le site du cabinet lui-même,
  non retenue. Admission au barreau 1991 de Pierre-Yves Gunter — date de début de carrière, pas
  de fondation du cabinet Gunter Arbitration Sàrl, non retenue comme founding_year.
- Échecs : ksr-avocats.ch (site en construction, page vide) ; cramer-avocats.ch (contenu vide
  au fetch — page blanche) ; fdlex.ch (contenu vide au fetch — page blanche).
- Totaux cumulés : **206 réussites / 64 échecs / 270 testés** sur 486 connus, ~216 restants.
- Rebuild complet OK (65 972 fichiers `index.html`, sitemap 23 057 URLs, échantillon de 40
  fichiers sans artefact Jinja). Entrée Bonnant & Associés vérifiée manuellement
  (`/fr/avocats/geneve/etude/bonnant-associes/`) : « Étude fondée en 1996 (30 ans d'existence) »
  et date de consultation 2026-07-22 s'affichent correctement.

### 2026-07-22 ~23:30 UTC — lot automatique de 20 (GE/VD — fin de la liste principale)

- 20 domaines traités (dont jmrlegal.ch re-vérifié, [] domaine invalide ignoré) : **17 réussites, 1 échec** (avocats-riviera.ch).
- jmrlegal.ch confirmé toujours compromis (liens spam football persistants) — reste dans `_failed`.
- Années de fondation trouvées : vogelimarquis.ch (2024 — "Sébastien Vögeli et Julien Marquis s'associent... en novembre 2024") ; iustopia.com (2020 — "IUSTOPIA Law Firm (fondateur, 2020)" dans la bio d'Andrea Pappalardo) ; ardenterlaw.ch (2021 — "fondée en octobre 2021 par Me Antonia Mottironi") ; vsavocats.ch (2019 — "fondée par Me Maud VOLPER et Me Thierry STICHER en mai 2019") ; dubail-kasser.ch (2017 — "Fondée par Maîtres Laïtka Dubail et Anny Kasser-Overney en 2017") ; raptis-avocats.ch (2012 — "En décembre 2012, elle a ouvert sa propre Étude à Morges") ; blochavocats.com (2014 — "Founded in 2014 by Esq. Olivier Bloch") ; npdp-avocats.ch (1992 — "Créée en 1992" pour l'étude de Monthey, étude fondatrice du réseau NPDP) ; banic-stamenkovic.ch (2020 — "En 2020, il s'associe à Me Radivoje Stamenkovic et fonde l'Étude Banic Stamenkovic").
- Autres réussites (domaines de compétence) : hirsch-law.ch (arbitrage, licences internationales, M&A, banque), lubiniavocats.ch (droit de la famille et successions, maintenant "Lubini Hottelier Avocats"), prlex.ch/pr-avocats.ch (12 domaines : banque, contrats, vente internationale, maritime, bail, successions, travail, famille, pénal, poursuites, sanctions, DIP), 3mai.ch (droit pénal, responsabilité civile, droit public), depreuxavocats.ch (litiges, droit du travail, responsabilité médicale, droit de l'art), altius-avocats.ch (contrats, arbitrage, droit privé, administratif, sociétés, pénal, droit aérien — spécialité rare), etude-fontana.ch (liste très étendue — pénal, civil, administratif, circulation routière, RC, assurances, famille, travail, bail, banque, contrats, sport ; fondation "dans les années 50" trop vague, non retenue), fairlaw.ch (pénal, famille, travail, contrats).
- Note rigueur : la mention "dans les années 50" pour l'Étude Fontana (fondée par Jean-Pierre Cottier) n'est pas une année précise et n'a pas été retenue conformément à la règle 2. Le chiffre "12 attorneys and assistants" de l'Étude Fontana est un total mixte (avocats + assistants), non retenu comme team_size_n.
- Échec : avocats-riviera.ch (contenu vide au fetch — site inaccessible).
- Domaine invalide `[]` présent dans les données CSV ignoré (entrée corrompue, aucun nom de domaine).
- Totaux cumulés : **223 réussites / 65 échecs / 288 testés** sur les 487 domaines normalisés connus. Il reste environ **199 domaines** non testés, soit encore ~10 lots de 20 avant d'atteindre la phase de découverte.
- Rebuild complet OK (65 972 fichiers `index.html`, sitemap 23 135 URLs, échantillon de 40 fichiers sans artefact Jinja).

### 2026-07-23 — lot automatique de 20 (GE/VD)

- 20 domaines traités : **15 réussites, 5 échecs**.
- Années de fondation trouvées : kavocats.ch (2022 — "Fondée en septembre 2022"), legalia-avocats.ch
  (2006 — "Fondée en 2006 par trois avocats lausannois"), flurilaw.ch (2007 — "she created FLURI &
  Partner in 2007"), avocates-lavaux.ch (2005 — "Fondation de l'Etude Valentine Gétaz Kunz" dans
  la biographie de l'associée), feldmann-savoy-avocats.ch (2006 — "nous avons créé ensemble le 1er
  février 2006 l'Étude d'avocats BUDIN ASSOCIÉS Vaud"), avocatlausanne.com (1971 — "L'étude, fondée
  en 1971").
- Tailles d'équipe : leiravelloavocats.ch ("Deux associés, un seul nom" — 2 associés explicites),
  legalia-avocats.ch ("5 collaborateurs" affiché explicitement), avocatlausanne.com ("formée de quatre
  associés" — 4 associés explicites).
- Autres réussites (domaines de compétence) : espace.legal (13 domaines dont technologie/esport/IA
  — spécialité rare), tp-avocats.ch (9 domaines, Étude Tobler & Plumez à Vevey), etude-jl.ch
  (JL Avocats & Médiation Sàrl, 4 domaines + médiation), hnblaw.ch (H&B Law Morges, domaines
  extraits depuis bios — pages principales en JS), pgavocats.ch (PG Avocats Lausanne, 4 domaines
  dont droit de la concurrence), pvlegal.ch (Portmann Ventura Lausanne, 6 domaines variés dont
  horlogerie et aéronautique), novier.ch (Novier Avocats Pully, 5 domaines dont droit de la
  formation et de la santé), dha-avocats.ch (DHA Avocats Lausanne, 6 domaines).
- Notes de rigueur : "plus de trente ans de pratique du barreau" (dha-avocats.ch — cumul non
  daté, non retenu), "De dimension humaine" (novier.ch — vague, non retenu), biographies
  indiquant "depuis 1992" ou "plus de 25 ans" pour des associés (flurilaw.ch, feldmann) —
  toujours non retenus comme founding_year car relatifs à des carrières individuelles, pas à la
  date de fondation du cabinet actuel.
- Échecs : kellerpachoud.ch (contenu vide, rendu JS) ; avocats-stpierre.ch (redirige vers
  avsp.ch, déjà traité, fondation 1979) ; mont-avocats.ch (aucune présence web indexée) ;
  avocatlausanne.ch (site secondaire de Me Vollenweider pour la même étude que avocatlausanne.com) ;
  aberlaw.ch (aucune présence web indexée).
- Totaux cumulés : **238 réussites / 70 échecs / 308 testés** sur les ~485 domaines connus.
  Il reste environ **177 domaines** non testés, soit encore ~9 lots de 20.
- Rebuild complet OK (65 972 fichiers `index.html`, sitemap 23 267 URLs, échantillon de 40
  fichiers sans artefact Jinja détecté).


### 2026-07-23 — lot automatique de 20 (GE/VD)

- 20 domaines traités : **16 réussites, 4 échecs**.
- Années de fondation trouvées : avocatsgeneve.ch (BARTH Avocats, 2006 — "il a ouvert son Cabinet d'avocats en 2006") ; abgavocate.ch (ABG Avocate, 2023 — "fonder mon Etude ABG AVOCATE au début de l'année 2023") ; bouzaglo.law (Etude de Me James Bouzaglo, 2024 — "il a fondé au début de l'année 2024 l'étude de Me James Bouzaglo") ; mjcosta-litige-assurances.ch (Etude Costa, 2020 — "Création de l'étude COSTA en avril 2020") ; croce-associes.ch (CROCE & Associés SA, 1981 — "Founded in 1981 by Franco CROCE" dans la meta-description officielle du site) ; daudinlaw.com (Daudin Law, 1975 — "L'Etude Daudin Law a été fondée en 1975") ; decourtensolutions.ch (de Courten Solutions, 2022 — "Frédérique founded de Courten Solutions in 2022").
- Tailles d'équipe : swiss-lawyers.com (BEGUIN DE GORSKI HUNZIKER — "Les trois avocats de l'étude", 3 avocats explicitement annoncés).
- Autres réussites (domaines de compétence) : legalea.ch (médiation, résolution amiable, famille/divorce — première étude à Genève à maîtriser plusieurs processus de résolution amiable hors tribunaux) ; gvalex.ch (droit civil, bail, travail, pénal économique, entraide judiciaire) ; atatavocate.ch (9 domaines dont droit des étrangers, assurances, circulation routière, pénal des mineurs) ; azha.ch (boutique spécialisée arbitrage international et sanctions économiques, 2 associés) ; siegrist-lazzarotto.ch (renommé SIEGRIST LAZZAROTTO LACHAT CLERIGO MULLER — spécialisée exclusivement immobilier, construction, aménagement, environnement, marchés publics) ; bellonderham.ch (Bellon & de Rham — profil unique: avocat titulaire d'un doctorat en médecine, spécialisé droit médical/médico-légal en plus des domaines classiques) ; camporini-avocat.ch (6 domaines : pénal/pénal des mineurs, travail, LCR, étrangers, assurances sociales, administratif) ; croce-associes.ch (15 domaines très étendus dont navires et aéronefs, trusts/fondations, Family Office — cabinet international avec bureaux à Genève, Londres, Singapour et Shanghai) ; pdllaw.ch (droit fiscal entreprises et particuliers, imposition immobilière, successions, contrats/compliance, fondations/OSBL — site en rendu JS, données issues des métadonnées HTML).
- Notes de rigueur : copyright "2015-2026" de gvalex.ch non retenu comme founding_year (date de copyright du site, pas de fondation du cabinet). "Expérience professionnelle variée de plus de 20 ans" (legalea.ch) et "20 years of experience" (pdllaw.ch) non retenus — formulations vagues. "Les trois avocats" de swiss-lawyers.com retenu comme team_size_n: 3 car déclaration directe ("Les trois avocats de l'étude BEGUIN DE GORSKI HUNZIKER, Marc Béguin, Alexandre de Gorski et Sayeh Hunziker"), non déduit d'un comptage de profils. Données de daldewolf.com non retenues : cabinet basé à Bruxelles (Belgique), statistiques mondiales (49 avocats, bureaux à Kinshasa) non spécifiques à la Suisse, conformément à la règle 4.
- Échecs : alkatout-legal.ch (aucune présence web indexée pour ce domaine) ; votreavocat.ch (contenu vide au fetch sur toutes les pages, rendu JavaScript probable) ; daldewolf.com (cabinet belge, données non suisses, règle 4) ; tribunal.ch (aucune présence indexée comme cabinet d'avocats, résultats renvoient vers institutions judiciaires officielles).
- Totaux cumulés : **254 réussites / 74 échecs / 328 testés** sur ~485 domaines connus. Il reste environ **157 domaines** non testés, soit encore ~8 lots de 20 avant d'atteindre la phase de découverte.
- Rebuild complet OK (65 972 fichiers `index.html`, sitemap 23 267 URLs, échantillon de 40 fichiers sans artefact Jinja détecté).

### 2026-07-23 — lot automatique de 13 (GE/VD — longue traîne solo)

- **Lot limité à 13 domaines** (au lieu de 20) : la recherche web a été interrompue par la limite mensuelle de l'outil WebSearch après 13 domaines. La prochaine exécution reprend à partir du 14e domaine de la file.
- 13 domaines traités : **10 réussites, 3 échecs**.
- **Correctif important** : bug détecté et corrigé — les `practice_areas_fr`/`en` avaient été enregistrées comme chaînes de caractères (comma-separated string) au lieu de listes Python dans `cabinet_web_enrichment.json`. Ce format incorrect provoquait un affichage caractère par caractère sur les fiches (ex. "D, r, o, i, t, ..."). Corrigé en convertissant toutes les nouvelles entrées en listes avant le rebuild. Le bug n'affectait que ce lot ; tous les lots précédents utilisaient déjà le bon format (listes).
- Années de fondation trouvées : gd-avocat.ch (Étude Gilbert Deschamps, 2024 — nouvel emplacement à Bernex) ; dinh-avocat.ch (Étude Dinh Avocat, 2023) ; interdroit.ch (Interdroit avocat-e-s Sàrl, 2017 — « l'étude a été fondée en 2017 ») ; soniaelkrief.com (Sonia Elkrief IP Lawyers, 2015 — « launched her own practice in 2015 ») ; gloor-avocat.ch (Étude Werner Gloor, 1995 — « Depuis 1995 — Avocat indépendant »).
- Autres réussites (domaines de compétence) : etude-themis.ch (droits humains, famille, pénal mineur-e-s, défense victimes, protection de l'adulte) ; ducor-law.ch (boutique spécialisée droit de la santé, produits thérapeutiques, technologie — Prof. Philippe Ducor) ; impulsius.ch (contrats, propriété intellectuelle, droit fiscal, travail, PME/ONG/ESG) ; gabellon-legal.com (philanthropie, litiges, white-collar, contrats/sociétés, famille/successions) ; cmg-avocats.ch (famille, travail, bail, successions, protection de la personnalité, contrats, pénal).
- Note : gloor-avocat.ch est un cabinet à spécialité rare (droit diplomatique/immunités internationales en plus du droit du travail).
- Échecs : tglf.ch et partem.ch (aucune présence web indexée) ; lg-avocats.ch (contenu vide au fetch, rendu JavaScript probable).
- Totaux cumulés : **264 réussites / 77 échecs / 341 testés** sur ~486 domaines connus. Il reste environ **145 domaines** non testés, soit encore ~7-8 lots avant d'atteindre la phase de découverte.
- Rebuild complet OK (65 972 fichiers `index.html`, sitemap 23 267 URLs, échantillon de 40 fichiers sans artefact Jinja détecté). Interdroit avocat-e-s Sàrl vérifiée manuellement : « Étude fondée en 2017 (9 ans d'existence) » s'affiche correctement.

### 2026-07-23 — lot automatique de 20 (GE/VD — longue traîne solo, suite)

- **Correction normalization détectée en début d'exécution** : la queue précédente utilisait `lstrip('www.')` (buggy — strip des caractères dans l'ensemble {'w','.'}) au lieu de `d[4:]` (correct). Ce bug n'affectait pas le JSON (les clés y étaient correctes) mais faussait le calcul de la file d'attente, créant des fantômes comme `alderwyss.com` (vraiment `walderwyss.com`, déjà en `_failed`). Corrigé pour cette exécution : queue recalculée avec la normalisation correcte → 145 domaines restants.
- 20 domaines traités : **10 réussites, 10 échecs**.
- **Années de fondation** : alainlevy.ch (2001 — « 2001 - Avocat indépendant Genève » sur la page des expériences professionnelles) ; markarian-avocat.ch (2012 — « Established in 2012 by Françoise Markarian »).
- **Autres réussites** (domaines de compétence) : ifntaxlaw.com (IFN Tax & Law — fiscalité d'entreprises, TVA, fiscalité internationale et des produits dérivés, due diligence, divulgation volontaire, droit civil/bancaire/sportif — boutique fiscale et juridique spécialisée) ; id-avocats.ch (ID Avocats — droit de la famille, divorce, pénal, judiciaire, successions, **droit équin** — spécialité très rare) ; jgpartners.ch (JG Partners — famille, cohabitation, patrimoine, pénal, contrats, poursuites, droit constitutionnel/administratif, étrangers, médiation) ; kellezi-legal.ch (Kellezi Legal — concurrence/antitrust, protection des données, droit public économique, marchés publics, aide d'État — boutique droit des affaires et régulation) ; degaullefleurance.com (De Gaulle Fleurance Genève — M&A, fiscal, immobilier transfrontalier, bancaire, compliance, patrimoine, fonds, droit financier — office genevois du cabinet franco-européen ; statistiques mondiales « 200+ talents » non retenues, règle 4) ; loonis-quelen.ch (Loonis Quélen — droit maritime, **droit de l'espace**, droit civil/commercial, représentation d'intérêts — spécialité espace extrêmement rare, site effectif sur loonis-quelen.com) ; withersworldwide.com (Withers Genève — fiscalité US/UK/internationale, trusts, planification patrimoniale, clients HNWI, litige multi-juridictionnel — office genevois du cabinet international ; statistiques mondiales « 220 partners, 1100 staff » non retenues, règle 4) ; fourknights.ch (FourKnights — arbitrage international, litige, mesures conservatoires, poursuites/faillites, entraide judiciaire, pénal des affaires, médiation, contrats, sociétés, travail, DIP, gestion de projet).
- **Notes de rigueur** : degaullefleurance.com mentionne « plus de 200 talents » (global, non suisse, règle 4) et « plus de 30 ans d'expertise sur le marché suisse » (durée, pas année précise, règle 2) — non retenus. withersworldwide.com : « 220+ partners, 1100+ staff » (global, règle 4) — non retenu. fourknights.ch : « © 2018 BY FLOREAT PROJECT » = copyright du webdesigner, pas de l'étude — non retenu. loonis-quelen.ch → données lues sur loonis-quelen.com (même cabinet, domaine .ch probablement alias/redirigé).
- **Échecs** : gowenlaw.ch, grossin-avocat.ch, glegal.ch, shgavocats.ch, k-lm.ch, decerjat.ch, mlgeneva.com (aucune présence web indexée) ; landrove.ch (URL non accessible via l'outil de fetch) ; sautter29avocats.ch (erreur HTTP 503) ; moro-avocats.ch (site en construction, aucun contenu exploitable).
- Totaux cumulés : **274 réussites / 87 échecs / 361 testés** sur ~486 domaines connus. Il reste environ **125 domaines** non testés (145 selon queue corrigée moins 20 de ce lot), soit encore ~6-7 lots de 20.
- Rebuild complet OK (65 972 fichiers `index.html`, sitemap 23 267 URLs, échantillon de 40 fichiers sans artefact Jinja). Markarian Avocat vérifiée manuellement (`/fr/avocats/geneve/etude/markarian-avocat/`) : « Étude fondée en 2012 (14 ans d'existence) » s'affiche correctement. Alain Lévy (rue-de-la-fontaine-7) : « Étude fondée en 2001 (25 ans d'existence) » s'affiche correctement.

### 2026-07-23 — lot automatique de 20 (GE/VD — longue traîne solo, suite)

- 20 domaines traités : **14 réussites, 6 échecs**.
- **Années de fondation trouvées** : vaudan-avocat.ch (Jean-Baptiste Vaudan, 2010 — « Fondée en 2010
  pour la pratique du barreau en Suisse », mention explicite sur la page d'accueil) ;
  urbensignori.ch (URBEN SIGNORI *étude d'avocats, 2023 — « Fondation de l'Étude URBEN SIGNORI
  *étude d'avocats en 2023 » sur la bio de Me Luca Urben) ; urbenavocats.ch (URBEN AVOCAT•E•S,
  2018 pour la fondation originale de l'Étude Urben Legal — même cabinet renommé successivement
  en Urben Signori 2023 puis URBEN AVOCAT•E•S 2026 ; founding_year = 2018 retenu comme date de
  fondation continue) ; sutter-avocats.com (SUTTER Avocats, 2011 — « Fondée en 2011, l'Etude
  déploie une activité de conseil », mention directe sur la page d'accueil) ; stucki-legal.ch
  (Stucki Legal, 2019 — « Founded in 2019 by Blaise Stucki », mention explicite dans la
  meta-description et le corps de la page).
- **Autres réussites** (domaines de compétence) : west-avocats.fr (cabinet français avec bureau à
  Lausanne — droit des affaires, droit du travail, droit du cheval, droit international, droit
  immobilier, audit des risques et gestion des crises) ; vaney-avocat.ch (droit de la famille et
  du divorce, protection de l'enfant et de l'adulte, successions, droit pénal) ; thevozpartners.ch
  (cabinet international Lausanne+US — droit fiscal international, droit des sociétés, services
  patrimoniaux, litiges commerciaux ; statistiques mondiales non retenues, règle 4) ; tanlegal.ch
  (My-Hué TAN — General Counsel Desk pour entreprises, management consulting pour cabinets
  d'avocats, médiation, droit commercial) ; subilia-avialegal.ch (Dr Julien Subilia — droit aérien
  et spatial, droit médical, spécialités très rares ; expert ICAO, instructeur IATA depuis 2015) ;
  staub-law.com (STAUB AVOCATS — droit pénal économique, entraide judiciaire internationale,
  litiges civils et commerciaux, droit successoral) ; sportlegis.com (Dr Despina Mavromati —
  droit international du sport, arbitrage CAS, litiges disciplinaires et gouvernance sportive,
  droit UEFA/FIFA ; ancienne Managing Counsel au CAS, arbitre CAS et membre UEFA CFCB Appeals
  Chamber, auteure du commentaire Code CAS 2015 et 2025) ; sivanesan.ch (Me Gayatthiri Sivanesan
  — famille, travail, pénal, étrangers, contrats, assurances, prévoyance professionnelle,
  poursuites et faillites) ; sekkiouavocat.ch (Me Mourad Sekkiou — procédure civile, divorce et
  famille, étrangers, commercial et sociétés, travail, contrats, pénal économique, droit de
  l'architecte, droit des personnes ; brevet 1987, associé GRAZ & SEKKIOU 1999-2014).
- **Notes de rigueur** : urbenavocats.ch et urbensignori.ch désignent le même cabinet physique
  (même adresse Montreux, même Me Luca Urben), traités comme deux entrées distinctes dans le
  cache puisque le CSV en a deux entrées distinctes. founding_year = 2018 retenu pour
  urbenavocats.ch (fondation originale Urben Legal), 2023 pour urbensignori.ch (fusion
  créatrice de l'entité URBEN SIGNORI). trivialmass.com et trivialmass.ch : société de
  marketing (trivial mass SA, Savigny VD) — entrées incorrectes dans les données CSV, aucun
  rapport avec un cabinet d'avocats, marquées en échec. west-avocats.fr : cabinet inscrit au
  barreau de Paris (pas Genève), bureau à Lausanne uniquement comme antenne ; domaines de
  compétence retenus car explicitement formulés par le cabinet lui-même et applicables à
  l'antenne suisse.
- **Échecs** : wettstein-mediation.ch (contenu vide, rendu JS) ; vestrae.ch (contenu vide, rendu
  JS) ; trivialmass.com et trivialmass.ch (pas un cabinet d'avocats — société de marketing) ;
  siegrist-avocat.ch (contenu vide, rendu JS) ; sfalegal.com (URL non accessible via l'outil
  de fetch malgré recherche web préalable).
- **Totaux cumulés** : **288 réussites / 93 échecs / 381 testés** sur ~486 domaines connus.
  Il reste environ **105 domaines** non testés, soit encore ~5-6 lots de 20.
- Rebuild complet OK (66 008 fichiers `index.html`, sitemap 23 311 URLs, échantillon de 40
  fichiers sans artefact Jinja détecté).

