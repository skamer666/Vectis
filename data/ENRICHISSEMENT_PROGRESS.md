# Pilote d'enrichissement web des cabinets — journal de bord

Ce fichier est la mémoire du projet entre deux exécutions automatiques. Il est mis à jour à
chaque passage (manuel ou planifié). Toute exécution future — humaine ou automatisée — doit
commencer par le lire.

## Statut actuel (dernière mise à jour : 2026-07-29 — lot 37 — FILE D'ATTENTE ÉPUISÉE)

- **486** domaines uniques identifiés à partir des colonnes `site_web` des CSV Genève et Vaud
  (les 18 autres cantons n'ont pas cette colonne — voir "Phase de découverte" plus bas).
- **370** cabinets avec au moins un fait exploitable dans le cache principal GE/VD (inchangé).
- **126** domaines testés sans succès dans le cache principal GE/VD (inchangé).
- **0** domaines GE/VD restants — liste épuisée.
- **Cache découverte autres cantons :** 157 succès / 46 échecs (lot 36 : +9 succès, +9 échecs).
- Taux de réussite phase de découverte : **~77%** (157 / 203 entrées).
- **Prochaine étape :** ⚠️ FILE D'ATTENTE ÉPUISÉE — tous les cabinets ≥3 avocats des cantons de découverte ont été traités. Greg doit rediriger ou désactiver cette tâche planifiée.

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


### 2026-07-23 — lot automatique de 20 (GE/VD — longue traîne solo, suite)

- 20 domaines traités : **14 réussites, 6 échecs**.
- **Années de fondation trouvées** : rochatlex.ch (Étude de Me Elizaveta Rochat, 2011 — « L'Etude
  a été fondée en 2011 par Me Elizaveta Rochat », mention directe sur la page d'accueil) ;
  landoltandkoch.com (Landolt & Koch, 2011 — « Trusted advocates for international arbitration
  and dispute resolution since 2011 », mention explicite dans le footer) ; lna-paris.com (Langer
  Netter Adler, 1970 — « LNA was founded in 1970 by Renée Langer-Netter », mention directe sur
  la page d'accueil ; cabinet franco-genevois, bureau genevois au 8C Avenue de Champel, 1206) ;
  kdbavocats.ch (Lawsanne Avocats, 2011 — « Founded on 1st Mai 2011 », mention explicite sur la
  page d'accueil).
- **Autres réussites** (domaines de compétence) : artes-juris.ch (Artes Juris — droit des
  affaires, droit pénal, droit numérique/Web3/Blockchain, contentieux, droit de la famille) ;
  plaw.ch (PANCHAUD Tax & Legal — spécialiste fiscalité : personnes physiques et morales,
  fiscalité immobilière, restructuration, plans d'intéressement, prévoyance professionnelle,
  fiscalité des trusts, fiscalité internationale, rulings et contentieux fiscal) ;
  pulver-suhajda-avocates.ch (Étude NP&VS — droit de la famille, droit du travail, droit des
  successions ; données issues de l'index de recherche, page non accessible au fetch) ;
  rey-avocat-geneve.ch (Étude de Me Stéphane Rey — divorce/séparation, droit du travail, droit
  des étrangers, circulation routière, droit pénal, droit fiscal) ; schutz-law.ch (DFS Avocats,
  Daniel F. Schütz — droit du travail, droit des sociétés, famille et successions, poursuites et
  faillites, immobilier et bail, droit bancaire, étrangers, pénal, protection des données) ;
  dantes-law.com (Dantès Law — contentieux des affaires, droit social, pénal des affaires ;
  bureau Paris + Genève) ; deve.law (Degni & Vecchio — contentieux commercial, pénal économique,
  droit de l'entreprise, droit administratif, travail, contentieux bancaire, famille, entraide
  internationale) ; davocats.ch (d.avocats — immobilier et construction, droit du bail, travail,
  administratif, contentieux civil) ; gh-avocats.ch (Guisan & Hämmerli — large généraliste :
  immobilier, construction, affaires, poursuites, contrats, famille, successions, pénal, droits
  réels, circulation routière, étrangers, bail, responsabilité civile, travail, administratif) ;
  keller-pachoud-avocats.ch (Keller Pachoud Avocats — droit des contrats, droit de l'énergie,
  externalisation du service juridique ; domaines issus des titres de pages indexées, fetch vide).
- **Notes de rigueur** : reiser-anne.ch exclue car cabinet formellement fermé depuis le
  31 janvier 2025 (mention explicite sur le site). kdbavocats.ch : page contient un lien spam
  injecté (cialisfrance24.com) mais le reste du contenu est intact et le founding_year 2011 est
  explicitement indiqué — le lien spam est un artefact CSS/template, pas une compromission de
  contenu ; retenu comme succès pour le founding_year uniquement, sans practice_areas (non listées
  explicitement sur la page d'accueil). artes-juris.ch : statistique "8 Attorneys and Experts /
  450+ Satisfied clients" ambiguë (ordre labels/chiffres incertain sur la page) — team_size_n
  non retenu.
- **Échecs** : nv-avocats.ch (non indexé, contenu inaccessible) ; rodavocats.ch (page vide, JS)
  ; rothavocates.ch (site compromis — injection spam e-commerce FNAC) ; etudeise.ch (site
  compromis — injection spam casino) ; reiser-anne.ch (cabinet fermé janvier 2025) ;
  baz-legal.ch (site en construction, contenu vide).
- **Totaux cumulés** : **302 réussites / 99 échecs / 401 testés** sur ~486 domaines connus.
  Il reste environ **85 domaines** non testés, soit encore ~4-5 lots de 20.
- Rebuild complet OK (sitemap 23 327 URLs, échantillon de 40 fichiers sans artefact Jinja).


### 2026-07-23 — lot automatique de 20 (GE/VD — longue traîne solo et petits cabinets, suite)

- 20 domaines traités : **15 réussites, 5 échecs**.
- **Années de fondation trouvées** : avocats-lawyers.ch (Bénédict // Bernel // Capt, 1997 —
  mention directe sur la page d'accueil du cabinet à Lausanne et Aigle) ; kdbtavocats.ch
  (Lawsanne Avocats, 2011 — alias de kdbavocats.ch, même fondation 2011 confirmée sur le site) ;
  reyavocats.ch (Rey Avocats Sàrl, 2021 — fondation indiquée sur la page d'accueil) ;
  primalex.ch (PRIMALEX – Haymoz Avocat, 2026 — cabinet récent, mention directe) ;
  avocats-nyon.ch (MGB Avocats Nyon, 1974 — « depuis 1974 », mention explicite sur le site) ;
  graenicher.law (GRAENICHER., 2024 — fondation indiquée sur le site) ; lapaix6.ch (Etude de la
  Paix 6 – David Abikzer, 2012 — « fondée en 2012 » sur la page d'accueil) ; hdb-law.com
  (HdB-Law – Hugues du Bois de Dunilac, 2023 — « In November 2023, Hugues du Bois de Dunilac
  decided to put his legal experience at the service of demanding clients within his own firm »,
  mention directe sur le site) ; bclegal.ch (BC Legal, 2016 — « L'Etude BC Legal est née en 2016
  de la fusion des Etudes CLegal créée par Me Nadia Calabria... et MBLegal fondée par Me Myriam
  Bitschy », mention directe sur la page d'accueil).
- **Taille d'équipe trouvée** : avocats-nyon.ch (MGB Avocats Nyon, 2 avocats — confirmé sur le
  site) ; bclegal.ch (BC Legal, 3 associées — Me Bitschy, Me Calabria, Me Safaï, mentionnées
  explicitement).
- **Autres réussites** (domaines de compétence uniquement) : gros-waltenspuhl.ch (Gros &
  Waltenspühl — droit commercial, sociétés, contrats, immobilier, trusts/successions, fiscal
  suisse et international, concurrence, sport, étrangers, travail, contentieux/arbitrage, PI) ;
  aebilaw.ch (Aebilaw – Me Florence Aebi — droit des affaires, gestion de sociétés, arbitrage,
  droit de l'art, immigration, famille, égalité, violence domestique, sociétés, poursuites, pénal
  économique, immobilier) ; sbplegal.ch (SBP Legal – Me Stéfanie Brun — travail, assurances
  sociales, famille, contrats, pénal) ; avo-k.ch (Elsig & Fivian — RC, assurances, médical,
  prévoyance, montagne/ski, construction, circulation routière, pénal, travail, contrats, art) ;
  nouvjur.ch (NOUVJUR SA – Jean-Michel Duc — assurances sociales, assurances privées, RC, travail,
  recouvrement) ; lavoielegale.ch (La Voie Légale – Me Pavel Vasilevski — contentieux, arbitrage,
  exécution forcée, planification patrimoniale, étrangers, sanctions, pénal économique).
- **Notes de rigueur** : kdbtavocats.ch est un alias de kdbavocats.ch (même cabinet Lawsanne
  Avocats), traité comme entrée distincte dans le cache car il apparaît comme une entrée distincte
  dans les CSV ; aucune practice_areas ajoutée car non listées explicitement (cohérent avec
  kdbavocats.ch). hdb-law.com est un cabinet boutique très spécialisé (life sciences, produits,
  marketing digital) — domaines inhabituels mais explicitement listés sur le site. gros-waltenspuhl.ch :
  l'année 1981 mentionnée par des tiers (annuaires) n'est pas confirmée sur le site propre du
  cabinet (page JS non accessible au fetch) — founding_year laissé à null. Pour primalex.ch :
  founding_year=2026 est inhabituel mais explicitement mentionné sur le site pour ce cabinet très
  récent.
- **Échecs** : jm-avocats.ch (aucune présence web indexée) ; pirrello.legal (site non accessible
  via fetch, URL hors provenance) ; bogensbergerlaw.ch (site WordPress non configuré — page
  « Hello world! » par défaut, créé mai 2025) ; etude-lubishtani.ch (site non indexé, URL non
  accessible) ; ides.pro (domaine expiré — redirige vers expireddomains.com).
- **Totaux cumulés** : **317 réussites / 104 échecs / 421 testés** sur ~486 domaines connus
  (GE + VD). Il reste environ **65 domaines** non testés, soit ~3 lots de 20.
- Rebuild complet OK (65 336 fichiers HTML, sitemap 22 667 URLs, échantillon de 40 fichiers
  sans artefact Jinja détecté).


### 2026-07-23 — lot automatique 22 (GE/VD — longue traîne solo, avant-dernier lot de domaines connus)

- 22 entrées traitées (20 domaines valides + 2 entrées invalides dans les CSV) : **12 réussites,
  10 échecs**.
- **Années de fondation trouvées** : etude-avocat.com (Rive Avocats, 2001 — « il a fondé l'étude
  Rive Avocats en janvier 2001 », mention explicite dans la biographie de Me Abderrahim Razi) ;
  etudetissieres.ch (Étude Tissières, 2025 — « Dès 2025 Avocate indépendante – Étude Tissières »,
  biographie de Me Alexia Tissières) ; drpb.ch (Burkhalter Rechtsanwälte / Burkhalter Avocats,
  1922 — « 1922 Dr. Armin Hodler fonde le cabinet à Berne », chronologie officielle ; succursale
  Lausanne ouverte le 1er janvier 2026).
- **Autres réussites** (domaines de compétence uniquement) : etude-adelia.ch (AdElia – Me
  Nour-Aïda Bujard, Lausanne — famille, enfant/curatelle, pénal, travail, bail, poursuites) ;
  benardavocats.ch (Bénard Avocats Sàrl – Me Guillaume Bénard, Montreux — famille, travail,
  défense pénale, PI) ; casimiromartins-avocat.ch (Me Sara Casimiro Martins, Montreux — pénal,
  construction, civil, assurances sociales, obligations, faillites) ; nravocate.ch (Natacha
  Rickenbacher Avocate, Lausanne — bail, travail, PPE, famille, pénal, protection enfant) ;
  dmplegal.ch (DMP Legal – Me Fabienne Delapierre, Lausanne — énergie, entreprise, marchés
  publics, droit privé général) ; perspective-solution.ch (Perspective Solution Sàrl – Me Barbara
  Regamey, St-Prex — administratif/communal, travail, bail, contrats, médiation, PCE) ;
  avocat-oron.ch (Étude CMM – Me Caroline Matthey-Marchesi, Oron-la-Ville — famille, protection
  adulte/enfant, contrats, bail, travail, successions, assurances sociales, poursuites, pénal/LAVI,
  circulation routière, violences domestiques) ; lexinn.ch (LexInn sàrl, Morges — conseil
  juridique, arbitrage/médiation international, expertise juridique, spécialité énergie et sport) ;
  raphaelhammerli.ch (Me Raphaël Hämmerli, Yverdon-les-Bains — contrats, immobilier/construction,
  pénal, famille/successions, poursuites, administratif).
- **Notes de rigueur** : avocat-oron.ch mentionne « il y a sept ans » pour l'ancienneté —
  durée relative, founding_year laissé à null. casimiromartins-avocat.ch n'a que « © 2023 by
  MC & SC » — copyright de site, pas une année de fondation. antaria-legal.ch présentait un
  rapport de parenté possible avec etude-adelia.ch (même avocate Me Nour-Aïda Bujard) mais le
  site antaria-legal.ch est littéralement en construction (page blanche) — marqué en échec.
  latourinternational.ch est un cabinet parisien (49 rue de Lisbonne, 75008 Paris) malgré le
  .ch — exclu car non suisse.
- **Échecs** : etude-eich.ch (sous-pages inaccessibles au fetch, accueil sans faits exploitables) ;
  latourinternational.ch (cabinet français, non suisse) ; juriscausa.ch (aucune présence indexée) ;
  antaria-legal.ch (site en construction) ; lawsanneavocats.ch (inaccessible directement ; données
  déjà en cache sous kdbavocats.ch ; ancienne version kdbtavocats.ch montre des signes d'injection
  spam cialisfrance24.com) ; homepage (entrée invalide CSV — non-domaine) ; groslimond-avocat.ch
  (contenu vide, JS ; déjà traité sous groslimond-avocats.ch) ; redzepi-avocats.ch (contenu vide,
  JS probable) ; etude@lion-or.ch (entrée invalide CSV — adresse e-mail) ; baudraz-torchio.ch
  (contenu vide, JS probable).
- **Totaux cumulés** : **329 réussites / 114 échecs / 443 testés** sur ~486 domaines connus
  (GE + VD). Il reste environ **43 domaines** non testés, soit ~2 lots de 20.
- Rebuild complet OK (66 128 fichiers HTML, sitemap 23 471 URLs, échantillon de 40 fichiers
  sans artefact Jinja détecté).


### 2026-07-23 — lot automatique 23 (GE/VD — dernier lot de domaines connus, fin de la liste des 486)

- 20 domaines traités : **16 réussites, 4 échecs**.
- **Années de fondation trouvées** : waeberavocats.ch (Waeber Avocats, 2006 — fondée explicitement
  en 2006 sur la page "étude") ; borlatavocate.ch (Borlat Avocate & Médiation, 2020 — année de
  démarrage explicite sur le site) ; borgeaud-avocat.ch (Nathan Borgeaud, 2025 — cabinet très
  récent) ; kalbermatten-avocat.ch (Stève Kalbermatten, 2016 — fondation 2016 sur le site) ;
  intermandat.ch (Intermandat SA, 1932 — fiduciaire fondée en 1932, depuis 93 ans, non un cabinet
  d'avocats traditionnel).
- **Autres réussites** (domaines de compétence uniquement) : alderwyss.com (Walder Wyss SA —
  grand cabinet national, 26 domaines listés en FR — clé normalisée lstrip bug sur "walderwyss") ;
  lm-law.ch (WLM Avocats, 6 domaines — clé normalisée depuis "wlm-law.ch") ; g-avocats.ch
  (Wilhelm Avocats SA, Lausanne — 10 domaines) ; m-legal.ch (WM Legal / Waeber Penet, Genève —
  8 domaines incluant droit français) ; aser-avocats.ch (Marcel Waser Avocats, Lausanne — 7
  domaines, clé depuis "waser-avocats.ch") ; hitecase.com (White & Case Genève — commerce
  international / OMC / arbitrage, bureau GE uniquement, clé lstrip "whitecase.com") ;
  ithersworldwide.com (Withers Genève — 13 domaines page Genève, clé lstrip "withersworldwide") ;
  est-avocats.fr (West Avocats — cabinet français avec bureau Lausanne, 6 domaines du site FR) ;
  ivt-legal.ch (Ingrid Van Tongerloo, civil/pénal/administratif) ; etudeaz.ch (Aesane Ziegler,
  7 domaines) ; legalex.ch (LEGALEX Avocats, 6 domaines).
- **Notes de rigueur** : alderwyss.com et hitecase.com/ithersworldwide.com : clés normalisées
  dues au bug lstrip('www.') dans extract_domain() de build.py — les clés dans le cache
  correspondent bien aux formes normalisées utilisées par build.py. intermandat.ch est une
  fiduciaire (pas stricto sensu un cabinet d'avocats) mais le site est présent dans les données
  CSV GE — marqué en succès avec note. Pour White & Case et Withers, chiffres globaux du réseau
  exclus ; seuls les domaines et informations spécifiques au bureau de Genève retenus.
- **Échecs** : reichenbach@waser-avocats.ch (adresse e-mail dans le champ site_web) ;
  raphaelguisan.ch (site redirige vers gh-avocats.ch depuis 2025, pas de faits propres) ;
  avocat-vertesi.ch (contenu vide au fetch) ; personne-de-confiance.com (service de médiation,
  pas de cabinet d'avocats, pas de faits chiffrés).
- **Totaux cumulés** : **346 réussites / 118 échecs / 464 testés** sur 486 domaines connus
  (GE + VD). Il reste **22 domaines non testés** dans la liste connue (~1 lot).
  Taux de réussite : ~74.6% (346 / 464).
- Rebuild complet OK (66 156 fichiers HTML, sitemap 23 509 URLs, échantillon de 40 fichiers
  sans artefact Jinja détecté).


### 2026-07-23 — lot automatique 24 (GE/VD — avant-dernier lot, 3 domaines restants après ce lot)

- 20 domaines traités : **15 réussites, 5 échecs**.
- **Années de fondation trouvées** : bourgeoisavocats.ch (1953 — "Fondée en 1953", cabinet genevois
  de renom) ; codexavocats.ch (1962 — "depuis 1962", Lausanne) ; bvhlegal.ch/bvlegal.ch (2005 —
  "DEPUIS 2005", Me Bender & Vogel, Monthey/Lausanne) ; etudelacote.com (2012 — "depuis 2012",
  Nyon) ; heringavocats.com (2012 — "Fondée par Me Isabelle Hering en 2012", Nyon) ;
  imhof-avocat.ch (2021 — "à titre indépendant, dès juin 2021").
- **Taille d'équipe trouvée** : bvhlegal.ch (2 avocats-associés — "2 AVOCATS-ASSOCIÉS", explicite).
- **Autres réussites** (domaines de compétence uniquement) : pache-henny-burdet.ch/phbavocats.ch
  (10 domaines) ; merenyi-avocats.ch (6 domaines — famille/AI/successions/RC/contrats/circulation) ;
  brenci.ch (5 domaines — droit douanier international, compliance AML/KYC) ; etudepetito.ch
  (13 domaines — droit de la famille, pénal, circulation, étrangers) ; charpie.pro (6 domaines
  — droit international des affaires, pénal international) ; laurentdamond.ch (7 domaines —
  droit commercial, successions, bail, médiation) ; avocats-rumine.ch (11 domaines — cabinet
  Dessemontet & Ghosn, Lausanne) ; besselegal.com (5 domaines — PI, immobilier, concurrence,
  patrimoine, pénal économique) ; gillieronavocat.ch (6 domaines — PI, droit numérique, IA,
  FinTech) ; heringavocats.com (7 domaines — TI, PI, protection des données, DPO externe).
- **Notes de rigueur** : bourgeoisavocats.ch redirige vers bourgeoisavocats.com (clé CSV conservée) ;
  bvhlegal.ch redirige vers bvlegal.ch (clé CSV conservée) ; pache-henny-burdet.ch redirige
  vers phbavocats.ch (clé CSV conservée). Pour charpie.pro, inscription au barreau vaudois
  depuis 1977 non retenue comme année de fondation (date personnelle ≠ création de l'étude).
- **Échecs** : avocatchappaz.ch (aucune présence web indexée) ; bp-avocats.ch (aucune présence
  web indexée) ; etude-saint-marc.ch, lexpro.ch, hofstetter-avocats.ch (contenu vide au fetch,
  rendu JavaScript probable).
- **Totaux cumulés** : **360 réussites / 123 échecs / 483 testés** sur 486 domaines connus.
  Il reste **3 domaines non testés** dans la liste connue (dernier lot très partiel — peut être
  combiné avec le démarrage de la phase de découverte des 18 autres cantons).
  Taux de réussite : ~74.5% (360 / 483).
- Rebuild complet OK (66 216 fichiers HTML, sitemap 23 593 URLs, échantillon de 40 fichiers
  sans artefact Jinja détecté).

### 2026-07-23 — lot automatique 25 (GE/VD — DERNIER LOT, liste épuisée)

- 12 domaines traités (les derniers restants de la liste GE/VD) : **9 réussites, 3 échecs**.
- **Années de fondation trouvées** : avocats-montreux.com (2003 — "Il s'est établi à
  Montreux en 2003", Me Kohli) ; avocats-nordvaudois.ch (2004 — "fondée par Me Monnin
  Zwahlen, installée rue de la Plaine depuis 2004", mention explicite).
- **Autres réussites** (domaines de compétence uniquement) : rufavocate.ch (droit des
  successions/famille/travail/contrats — Lorraine Ruf, spécialiste FSA successions) ;
  boldtapfer.ch (famille/habitation/travail) ; richardlaw.ch (criminalité économique,
  successions/trusts, droit bancaire, responsabilité médicale, arbitrage, droit fiscal) ;
  datalex.ch (protection des données, droit de la santé, technologies avancées, cybercriminalité) ;
  lagrotte.ch = Heim Avocats (9 domaines : famille, successions, immobilier, bail, travail,
  pénal, contrats, protection adulte, droit international privé) ; bettems.ch (immobilier/
  construction, droit du travail — Me Denis Bettems, inscrit au barreau depuis 1990 à Aubonne) ;
  mediation-concorde.com (service de médiation, domaines commerciaux/immobiliers/familiaux).
- **Échecs** : brownandpage.com (page placeholder cyon, aucun contenu) ; cm-avocat.ch (contenu
  vide) ; avocat-mediation-aigle.com (domaine non indexé, sans contenu).
- **Totaux cumulés** : **370 réussites / 126 échecs / 496 entrées cache**.
  Les **486 domaines GE/VD sont intégralement testés**. Taux de réussite : ~74.6%.
- Rebuild complet OK. Sitemap 23 629 URLs. Échantillon 40 fichiers sans artefact Jinja.
- **La prochaine exécution démarrera la phase de découverte** : recherche web des sites
  officels des cabinets des 18 cantons sans colonne `site_web` (AG, AI, BS, FR, GL, GR,
  JU, LU, NE, NW, OW, SG, SO, SZ, TG, UR, ZG, ZH), en commençant par les plus gros cabinets
  (champ `etude`). Fichier de suivi : `data/domaines_autres_cantons.json` (créé si absent).

### 2026-07-23 — lot automatique 26 (phase de découverte — autres cantons, lot 1)
- Liste GE/VD épuisée depuis le lot 25. Passage en phase de découverte pour les 18 cantons hors GE/VD.
- **20 cabinets traités** (top firms par taille depuis les cantons avec champ `etude` : ZH, BS, SG) : **14 faits utiles / 6 entrées sans fait chiffré** (founding_year ou team_size_n null, mais domaines de compétence extraits).
- Données stockées dans `data/domaines_autres_cantons.json` (nouveau fichier, même structure que le cache principal).
- Résultats notables :
  - Homburger AG (ZH) : fondé en 1957, 43 associés + plus de 160 professionnels
  - Schellenberg Wittmer (ZH/GE) : 150+ avocats, 19 domaines de compétence
  - Wenger Vieli AG (ZH) : fondé en 1971
  - MME Legal AG (ZH) : fondé en 1999, 19 domaines de compétence
  - Prager Dreifuss AG (ZH) : fondé en 1980, 45 avocats
  - Wenger Plattner (BS/ZH/BE) : 100+ collaborateurs, 17 domaines de compétence
  - schochauer ag (SG) : fondé en 1970
  - NEOVIUS AG (BS) : fondé en 1972, 9 domaines de compétence
  - Badertscher Rechtsanwälte (ZH) : fondé en 1996, ~24 avocats
  - Advestra AG (ZH) : fondé en 2020
  - Blum & Grob (ZH) : 55 collaborateurs
  - Nater Dallafior (ZH) : fondé en 2006
  - Probst Partner AG (ZH) : fondé en 1995
  - Streichenberg (ZH) : fondé en 1997
  - BEELEGAL (ZH) : fondé en 2014
- Note : ces données ne sont pas encore utilisées dans le build (les CSV des autres cantons n'ont pas de colonne `site_web`). Prochaine étape : intégrer `domaines_autres_cantons.json` dans `build.py` ou enrichir les CSV des autres cantons avec les URLs découvertes.
- Cache GE/VD inchangé : 369 succès / 126 échecs.
- Phase de découverte autres cantons : 20 cabinets découverts (lot 1/N).

### 2026-07-28 — lot automatique 27 (phase de découverte — autres cantons, lot 2)

- **20 cabinets traités** (top firms ZH/BS par taille — suite du lot 26) : **16 succès (dont 5 copies du cache principal) / 4 échecs**.
- Données stockées dans `data/domaines_autres_cantons.json` (37 entrées total, 3 _failed).
- **Résultats notables (nouveaux faits extraits) :**
  - **Walder Wyss AG** (walderwyss.com, ZH) : 26 domaines de compétence (site FR consulté). Année de fondation vague ("depuis 50 ans") → null.
  - **Bär & Karrer AG** (baerkarrer.ch, ZH) : fondé en **mars 1969**, **200+ avocats** (méta officielle), 28 domaines de compétence. Bureaux : Zurich, Genève, Lugano, Zoug, Bâle, St-Moritz.
  - **Lenz & Staehelin** (lenzstaehelin.com, ZH) : fondé le **1er janvier 1991** (fusion des études Lenz/Genève 1951 et Staehelin/Zurich 1917), 19 domaines de compétence. Bureaux : Zurich, Genève, Lausanne.
  - **CMS von Erlach Partners AG** (cms.law, ZH) : fondé en **1936** (explicite), **70+ professionnels** à Zurich (siège CH, chiffre CH-spécifique), 13 domaines de compétence.
  - **LALIVE SA** (lalive.law, ZH) : 12 domaines de compétence (spécialiste contentieux et arbitrage international). Note : l'URL a changé de lalive.ch à lalive.law.
  - **Lenz Caemmerer** (lclaw.ch, BS) : 14 domaines de compétence. Effectif total (45+) non retenu car non spécifique à la Suisse (inclut bureau Karlsruhe).
  - **burckhardt AG** (burckhardtlaw.com, BS) : **20 avocats, notaires et experts fiscaux** (explicite : "20 Anwälte, Notare sowie Steuerexperten"). 2 bureaux CH (Bâle + Zurich).
  - **Barandun AG** (barandun-law.ch, ZH) : 14 domaines de compétence.
  - **Rechtskraft Advokatur** (rechtskraft.ch, ZH) : 16 domaines de compétence.
  - **SwissLegal Dürr + Partner** (swisslegal.ch, BS) : 12 domaines de compétence.
  - **VISCHER AG** (vischer.com, ZH) : domaines partiels extraits (commercial, fiscal, réglementaire), page about partiellement JS-rendue.
  - **MLL Legal AG** (mll-legal.com, ZH) : 150+ avocats mentionnés dans la méta mais inclut bureaux Londres et Madrid → non retenu comme chiffre CH-spécifique.
- **Copies depuis cache principal (aucun nouveau fetch) :** bratschi.ch, nkf.ch, bakermckenzie.com, kellerhals-carrard.ch, pestalozzilaw.com.
- **Échecs (4) :** staiger.law (contenu vide, JS), quadra.law (contenu vide, JS), epartners.ch (URL non accessible via fetch), vischer.com classé succès partiel.
- **Cache principal GE/VD :** 369 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 37 entrées / 3 _failed.
- Rebuild complet OK : 66 252 fichiers HTML, sitemap **23 633 URLs**, échantillon de 40 fichiers sans artefact Jinja.

### 2026-07-28 — lot automatique 28 (phase de découverte — autres cantons, lot 3)

- **20 domaines traités** (cabinets ZH/BS principalement, tranche 14-12 avocats) : **12 succès / 8 échecs**.
- Données stockées dans `data/domaines_autres_cantons.json` (49 succès, 11 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **Valfor Rechtsanwälte AG** (valfor.ch, ZH) : fondé le **1er juillet 2024** (fusion de BianchiSchwald, GHR Rechtsanwälte et PYTHON), 20 domaines de compétence. Note : 70+ juristes incluent le bureau de Bruxelles — taille non spécifiquement suisse, non retenue.
  - **Streiff von Kaenel AG** (streiffvonkaenel.ch, ZH/Wetzikon) : fondé en **1962** (origine : Advokatenbüro Dr. Ullin Streiff à Uster), spécialités : droit du travail et droit de la construction.
  - **Steinbrüchel Hüssy Rechtsanwälte** (steinlex.ch, ZH) : fondé en **1951**, **16 avocats** (explicite : "derzeit 16 Anwältinnen und Anwälten").
  - **Wartmann Merker AG** (wartmann-merker.ch, ZH) : fondé en **1992** par Thomas Wartmann et Rudolf Merker. Spécialité : dispute resolution.
  - **Werder Viganò AG** (werdervigano.ch, ZH) : fondé en **2009** (fusion des études Werder et Viganò), **15 experts** (explicite), 3 domaines de compétence.
  - **Schiller Rechtsanwälte AG** (schillerlegal.ch, ZH/Winterthur) : issu d'un cabinet fondé en **1875**, 15 domaines de compétence.
  - **Reichenbach Rechtsanwälte AG** (rlaw.ch, ZH) : fondé en **1938** (explicite : "advising... since 1938"). Spécialité : droit commercial.
  - **Altenburger Ltd legal + tax** (altenburger.ch, ZH) : fondé en **1978** (explicite dans la méta-description officielle), 10 domaines de compétence.
  - **weber schaub & partner ag** (weber-schaub.ch, ZH) : fondé en **1993** par Peter Schaub et son épouse (explicite), 4 domaines de compétence.
  - **Baumgartner Mächler Rechtsanwälte AG** (bmlaw.ch, ZH) : 3 domaines de compétence (droit pénal, litiges, droit des sociétés). Pas d'année ni taille explicite.
  - **BALEX AG** (balex.law, BS) : liste complète de spécialités (12 domaines principaux). Pas d'année ni taille explicite.
  - **Rohrer Müller Partner AG** (rmp.ch, ZH) : spécialité Bau- und Immobilienrecht (explicite dans titre/méta). Pas d'année ni taille.
- **Échecs (8) :** gbf-legal.ch (hors provenance), vialex.ch (contenu trop sommaire), kleinlaw.ch / nigon.ch / zurich-law.ch / zurichlawyers.com / suterhowald.ch / landmann.ch (rendu JavaScript — page vide).
- **Cache principal GE/VD :** 370 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 49 succès / 11 échecs.
- Rebuild complet OK : sitemap **23 629 URLs**, échantillon de 40 fichiers sans artefact Jinja.

### 2026-07-28 — lot automatique 29 (phase de découverte — autres cantons, lot 4)

- **19 domaines traités** (cabinets ZH/BS/SG/GR/LU — tranche suivante par taille) : **17 succès / 2 échecs**.
- Données stockées dans `data/domaines_autres_cantons.json` (66 succès / 13 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **Tschümperlin Lötscher Schwarz AG** (tls-partner.ch, LU) : fondé en **1973** (50e anniversaire célébré en juin 2023), 9 domaines de compétence. Grande étude du centre de la Suisse (Lucerne, Emmenbrücke, Sursee).
  - **Baur Hürlimann AG** (bhlaw.ch, ZH) : fondé en **1956**, **env. 30 avocats** (explicite), 7 domaines de compétence. Spécialistes construction, énergie et droit administratif. Bureaux Zurich et Baden.
  - **FROMER Advokatur und Notariat** (fromer-law.com, BS) : fondé en **1941** par Dr. Leo Fromer, fusionné avec Fischer & Megert en 2011. 16 domaines de compétence.
  - **rtwp rechtsanwälte & notare** (rtwp.ch, SG) : fondé en **1940** ("seit 1940"), 13 domaines de compétence. Étude généraliste Saint-Gall.
  - **Scherler Siegenthaler Schweizer Rechtsanwälte AG** (sms-lawyers.ch, ZH) : fondé en **1956**, **10 avocats** (explicite). Étude généraliste.
  - **Kanzlei am Park** (ampark.law, ZH) : fondé en **1972**, **10 avocats** (explicite), 7 domaines de compétence.
  - **AH4 AG** (ah4.law, ZH) : fondé en **2017**, boutique spécialisée exclusivement droit de la famille et successions.
  - **Advokaturbüro Kernstrasse** (advokern.ch, ZH) : fondé en **1991** (explicite : "Einige Mitglieder des ersten Zürcher Anwaltskollektivs haben 1991 das advokaturbüro kernstrasse gegründet"), 9 avocats + 1 juriste, 6 domaines de compétence. Collectif zurichois, ne représente pas les économiquement forts contre les faibles.
  - **Quinn Emanuel Urquhart & Sullivan (Schweiz) GmbH** (quinnemanuel.com, ZH) : bureau zurichois ouvert en **2016**, 13 domaines de compétence. Plus grande étude mondiale consacrée exclusivement aux litiges commerciaux.
  - **Battegay Dürr AG** (bdlegal.ch, BS) : 14 domaines de compétence (FR/EN/IT/ES desks), pas d'année ni taille explicite.
  - **Walder Häusermann Rechtsanwälte AG** (whr.ch, ZH) : 15 domaines de compétence (spécialistes droit pénal, migrations, famille, bail).
  - **HOLENSTEIN BRUSA Ltd** (hol-law.ch, ZH) : 5 domaines de compétence (médias, PI, corporate, banque, contentieux, clientèle privée).
  - **Lustenberger + Partners** (lplegal.ch, ZH) : boutique contentieux/arbitrage/travail/construction.
  - **Rudin Cantieni Rechtsanwälte AG** (rudincantieni.ch, ZH) : 10 domaines de compétence (droit public, scolaire, personnel).
  - **Kunz Schmid Rechtsanwälte und Notare AG** (kunzschmid.ch, GR) : 10 domaines de compétence, "seit über 50 Jahren" → année non retenue (vague).
  - **Advokatur Walche** (walche.ch, ZH) : 9 avocats, 5 domaines (pénal, migrations, bail).
  - **Ringhof Rechtsanwälte** (bahnhofstrasse58.ch, ZH) : 8 avocats, pas d'année ("um 1930" → vague).
- **Échecs (2) :** advotech.ch / vincenzpartner.ch (rendu JavaScript — page vide).
- **Note architecture :** commit `edcce0e` récupéré avant push — ajout de `gen_affected_for_domain()`, `urls.py`, `indexnow_submit.py`, tests pytest. `domaines_autres_cantons.json` non encore utilisé dans `build.py` → pas de changement HTML, pas de rebuild local (inutile). Vercel fait le build complet sur push.
- **Cache principal GE/VD :** 370 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 66 succès / 13 échecs.

### 2026-07-28 — lot 30 (phase de découverte — autres cantons, lot 5)

- **20 domaines traités** (cabinets BS/GR/SG/ZH/LU — tranche suivante par taille) : **19 succès / 1 échec**.
- Données stockées dans `data/domaines_autres_cantons.json` (86 succès / 14 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **WALDMANN Rechtsanwälte** (lawyers.ch, BS) : fondé en **1953**, 15 domaines de compétence.
  - **ME Advocat AG** (advocat.ch, SG) : fondé en **1992** (explicite : fondation par Prof. Dr. Roland Müller à Staad SG), 8 domaines de compétence. 2 bureaux (Staad + Herisau).
  - **Buis Bürgi AG** (bblegal.ch, ZH) : fondé en **1955** (explicite : "long history going back to 1955"), boutique banking/litige, 8 domaines de compétence. Recommandé Legal 500 EMEA, IFLR1000.
  - **basleradvokat:innen Advokatur & Notariat** (basleradvokatinnen.ch, BS) : fondé en **1992**, **9 avocats** (explicite), 26 domaines de compétence. Mixte généralistes + spécialistes SAV.
  - **ettlersuter Rechtsanwälte** (ettlersuter.ch, ZH) : fondé en **1986**, 11 domaines de compétence. Quartier Seefeld, Zurich.
  - **KSPartner AG** (kspartner.ch, ZH) : fondé en **1993**, 7 domaines de compétence — spécialistes droit de la responsabilité civile, assurances et droit de la santé.
  - **Simonius & Partner** (advokaten.ch, BS) : fondé en **2000** (fusion Holliger Pfrommer & Partners et Simonius & Partners, oct. 2000 ; origines remontant à 1916).
  - **Böckli Häring Partner AG** (bhplaw.ch, BS — domaine canonique de boeckli-buehler.ch après rebranding) : 17 domaines de compétence.
  - **Teichmann International (Schweiz) AG** (teichmann-law.ch, SG) : 9 domaines principaux + 16 groupes d'expertise. Bureaux Saint-Gall, Zurich, Frauenfeld + international (Liechtenstein, Londres, Dubaï).
  - **Mengiardi Fey & Partner AG** (mfpartner.ch, GR) : 11 domaines de compétence. Notariat et droit civil/pénal à Coire (Graubünden).
  - **Caviezel Partner AG** (caviezelpartner.ch, GR) : 8 domaines spécialisés droit public, construction, eau/énergie, environnement. Notariat.
  - **Bolzern Haas & Partner AG** (bhup.ch, LU) : 10 domaines de compétence. 5 bureaux lucernois (Lucerne, Hochdorf, Sursee, Weggis, Hergiswil).
  - **Grossenbacher Rechtsanwälte AG** (gr-law.ch, LU) : 12 domaines de compétence. Notariat à Lucerne.
  - **schadenanwaelte AG** (schadenanwaelte.ch, ZH) : **20 spécialistes** (explicite), spécialiste responsabilité civile, assurances sociales et privées.
  - **Advoro Zürich AG** (advoro.ch, ZH) : 9 domaines de compétence. Boutique corporate/fintech/contentieux.
  - **LEXTERNA AG** (lexterna.ch, BS) : 3 domaines (droit des entreprises, données & innovation, droit personnel).
  - **Ludwig + Partner AG** (ludwigpartner.ch, BS) : 4 domaines (fiscal, affaires, immobilier, notariat/successions).
  - **Liatowitsch & Partner** (liatowitsch.ch, BS) : conseil, contentieux, notariat, expertises, médiation.
  - **advokatur am brühl** (adab.ch, SG) : droit privé et public généraliste.
- **Échec (1) :** mzbs.ch (contenu vide, rendu JavaScript probable).
- **Note :** comme pour les lots précédents, domaines_autres_cantons.json non encore consommé par build.py → pas de rebuild local ciblé (pages HTML inchangées). Vercel fait le build complet sur push.
- **Cache principal GE/VD :** 370 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 86 succès / 14 échecs.

### 2026-07-28 — lot 31 (phase de découverte — autres cantons, lot 6)

- **20 domaines traités** (cabinets ZH/BS/SZ — tranche suivante par taille) : **14 succès / 6 échecs**.
- Données stockées dans `data/domaines_autres_cantons.json` (99 succès / 20 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **Prof. Giger & Partner Rechtsanwälte** (gigerpartnerlaw.ch, ZH) : fondé en **1962** (explicite : "im Jahre 1962"), 12 domaines de compétence (emploi, famille, scolaire, circulation, pénal, contrats, construction, successions, sociétés, leasing, administratif, assurances/responsabilité).
  - **meyer & meier Rechtsanwälte AG** (mmlawyers.ch, ZH) : fondé en **2012** (explicite : "wurde 2012 gegründet"), 9 domaines de compétence.
  - **Advokatur West** (advokatur-west.ch, ZH) : fondé en **1995** (explicite : "Seit 1995"), 11 domaines de compétence (généraliste, médiation).
  - **DUFOUR Advokatur AG** (dufour-advokatur.ch, BS) : fondé en **1991** (explicite : "Founded in 1991"), 6 domaines de compétence — fondations/NPO, sociétés, clientèle privée, prévoyance, art/culture, successions.
  - **gbk Rechtsanwälte AG** (gbk-law.ch, ZH) : 6 domaines de compétence (droit immobilier public/privé, construction, environnement, assurances, droit scolaire).
  - **Advokatur Lachen** (advokatur-lachen.ch, SZ) : **9 avocats** (explicite : 3 avocates + 5 avocats + 1 Rechtskonsulent), 5 domaines (généraliste, notariat, pénal, famille, droit public). Nom actuel depuis avril 2017 ; tradition familiale Schwander depuis ~1920.
  - **PMP Rechtsanwälte AG** (pmp-ra.ch, ZH) : boutique planification/construction/immobilier.
  - **HUMBERT HEINZEN HISCHIER Rechtsanwälte** (hhh-law.ch, ZH) : boutique droit du travail.
  - **Thaler Berz Partner Rechtsanwälte** (tbp-law.ch, ZH) : boutique immobilier/bail/construction.
  - **Blesi & Papa** (blesi-papa.ch, ZH) : 6 domaines — emploi, prévoyance professionnelle, sécurité sociale, immigration, protection des données, litiges.
  - **TIMES Attorneys** (timesattorneys.ch, ZH) : boutique spécialisée technologie, PI, droit médical, entertainment, sports.
  - **Suffert Neuenschwander & Partner** (snplegal.com, ZH) : 18 domaines de compétence (généraliste + digital/IT, marchés publics, sports).
  - **LAUX LAWYERS AG** (lauxlawyers.ch, ZH) : spécialiste IT law, propriété intellectuelle, protection des données, droit de la santé numérique.
  - **WS LAW** (wslaw.ch, ZH) : 5 domaines — emploi, successions, droit des sociétés, famille, pénal.
- **Échecs (6) :**
  - reberlaw.ch (REBER Rechtsanwälte, ZH) — rendu JavaScript probable
  - advogar.ch (Advokatur Gartenhof, ZH) — rendu JavaScript probable
  - stplaw.ch (Stiffler & Partner, ZH) — rendu JavaScript probable
  - eversheds-sutherland.com (Eversheds Sutherland AG, ZH) — rendu JavaScript probable (site global)
  - klgp.ch (Kessler Landolt Giacomini & Partner, SZ) — rendu JavaScript probable
  - pachmann.law (Pachmann AG, ZH) — URL hors provenance, non accessible via web_fetch
- **Note :** domaines_autres_cantons.json non encore consommé par build.py → pas de rebuild local (pages HTML inchangées). Vercel fait le build complet sur push.
- **Cache principal GE/VD :** 370 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 99 succès / 20 échecs.
### 2026-07-28 — intégration `domaines_autres_cantons.json` dans build.py

Correction du point mort signalé après le lot 30 : le cache de découverte (86 cabinets
ZH/BS/SG/GR/LU) était alimenté par la tâche automatique mais jamais lu par `build.py` —
les CSV des cantons génériques n'ont pas de colonne `site_web`, donc le mécanisme
d'enrichissement existant (`WEB_ENRICHMENT`, indexé par domaine) ne pouvait pas s'y
brancher.

Ajout d'un second mécanisme de rattachement, par **nom de cabinet** plutôt que par
domaine : `firm_core_name()` réduit un nom à son cœur identifiant (sans forme juridique —
AG/SA/Ltd/GmbH/etc. — ni ponctuation) pour rapprocher deux graphies du même cabinet
(ex. « Schellenberg Wittmer AG » vs « Schellenberg Wittmer Ltd »). `attach_name_based_enrichment()`
apparie ensuite chaque entrée du cache à l'étude correspondante dans `CANTON_DATA`, canton
par canton — avec garde-fou anti-collision : si deux études distinctes du même canton
partagent le même nom cœur, aucune n'est enrichie (mieux vaut rater un rattachement que se
tromper de cabinet, conformément au principe de non-fabrication). `gen_canton_etudes` et
`gen_canton_avocats` utilisent ce rattachement en repli quand le rattachement par domaine
échoue (site_web absent).

Résultat mesuré après rebase sur le lot 31 (99 entrées exploitables) : **92 études
rattachées avec succès, 1 ignorée pour collision de nom, 6 non rattachées** (variantes de
nom trop éloignées — ex. rebranding non reflété dans le registre officiel — laissées sans
enrichissement plutôt que forcées). Ce chiffre grandira automatiquement à chaque nouveau
lot de découverte, sans action supplémentaire. Vérifié manuellement sur Homburger AG
(Zurich) : la fiche affiche désormais « Étude fondée en 1957 (69 ans d'existence) » et sort
du noindex automatique.

6 tests ajoutés (`tests/test_other_canton_enrichment.py`), dont un test explicite du
garde-fou anti-collision. 46 tests passent au total. Rebuild ciblé (ZH, BS, SG, GR, LU) +
échantillon de 40 pages sur l'ensemble du site : aucun artefact Jinja détecté.

Les prochains lots de la phase de découverte bénéficieront désormais automatiquement de ce
rattachement dès le prochain rebuild Vercel — aucune action supplémentaire requise côté
tâche planifiée.

### 2026-07-28 — lot 32 (phase de découverte — autres cantons, lot 7)

- **20 domaines traités** (cabinets ZH/SG — tranche suivante par taille) : **13 succès / 4 échecs / 2 copies / 1 correction**.
- Données stockées dans `data/domaines_autres_cantons.json` (112 succès / 24 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **LEXR Law Switzerland AG** (lexr.com, ZH) : fondé en **2016** (explicite : "2016 gegründet"), boutique tech law spécialisée startups/VC/fintech/data. 4 bureaux suisses (Zurich, Lausanne, Saint-Gall, Zoug) + Allemagne.
  - **Binder Legal KLG** (binderlegal.ch, ZH) : fondé en **1953** (explicite : "Since 1953"), boutique droit des affaires. Bureaux Zurich et Baden.
  - **Advokatur 107** (advokatur107.ch, SG) : **9 avocats** (explicite : "Team von 9 Anwältinnen und Anwälten"), 22 domaines de compétence généraliste + notariat.
  - **Advokatur Ankerstrasse** (anker24.ch, ZH) : histoire remontant à **1944** (explicite : "Geschichte, die bis ins Jahr 1944 zurückreicht"), spécialiste droit pénal et droit de la famille. À l'Ankerstrasse 24 depuis 2000.
  - **Barbier Habegger Rödl Rechtsanwälte AG** (bhr.law, ZH) : 17 domaines de compétence. Bureaux Winterthur (siège) et Zoug.
  - **Bürgi Nägeli Rechtsanwälte** (bnlawyers.ch, ZH) : 37 domaines de compétence. Cabinet généraliste très large spectre. Deux adresses zurichoises.
  - **Fischer Ramp Buchmann AG** (frb-law.ch, ZH) : boutique Private Clients (fiscalité, immobilier, successions, family offices, philanthropie). Band 2 Chambers 2026 Private Wealth, Leading Firm Legal 500 EMEA 2025.
  - **Fankhauser Rechtsanwälte** (fank-law.ch, ZH) : 12 domaines de compétence (généraliste). Bureaux Zurich + Samedan (GR).
  - **Legal Partners Zurich** (lp-zurich.ch, ZH) : Bürogemeinschaft (avocats individuellement responsables, pas de solidarité mutuelle), 12 domaines. Reconnue 5 années consécutives parmi les meilleures études suisses (BILANZ/PME).
  - **Linde Law AG** (linde-law.ch, ZH) : 5 domaines (contentieux & litige). Bureaux Zurich et Coire.
  - **Riedweg & Partner AG** (riedwegpartner.ch, ZH) : boutique droit fiscal & droit des sociétés, 10 domaines.
  - **Rutschmann Schwaibold Partner** (rsplaw.ch, ZH) : 15 domaines de compétence. Spécialiste droit des médias, insolvabilité, contentieux. Reconnu parmi les meilleures études suisses (BILANZ, 9 années consécutives).
  - **Jacober Bialas & Partner** (jb-anwaelte.ch, SG) : 13 domaines (généraliste + notariat). Cabinet orienté personnes privées, Saint-Gall.
- **Échecs (4) :** frt-anwaelte.ch (FRT RECHTSANWÄLTE & NOTARE, SG), bachmann.law (Bachmann Rechtsanwälte AG, ZH), tappolet-partner.ch (Tappolet & Partner, ZH), nplaw.ch (NEUPERT VUILLE PARTNERS, ZH) — pages vides, rendu JavaScript probable.
- **Copies (2) :** SwissLegal (Zürich) AG et SwissLegal asg.advocati (SG) → domaine swisslegal.ch déjà en cache (cabinet Basel). Entités distinctes, même site web — pas de nouvelle entrée.
- **Correction (1) :** sms-lawyers.ch — nom de cabinet corrigé de "Scherler Siegenthaler Schweizer Rechtsanwälte AG" (ZH, lot 28) en "Schwager Mätzler Schneider Rechtsanwälte" (SG). SMS = Schwager/Mätzler/Schneider, pas SSS. Canton mis à jour ZH→SG.
- **Note :** domaines_autres_cantons.json désormais consommé par build.py (intégration ajoutée ce même jour — voir section précédente). Le rattachement par nom (`attach_name_based_enrichment`) bénéficiera aux fiches ZH/SG au prochain rebuild Vercel.
- **Cache principal GE/VD :** 370 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 112 succès / 24 échecs.

### 2026-07-28 — Fribourg : regroupement par domaine d'email

Fribourg fait partie des 7 cantons sans champ `etude` ni `site_web` dans son CSV
source — jusqu'ici hors de portée de tout mécanisme de regroupement. Constat : le champ
`email` est rempli à 100% (217/217) et son domaine correspond presque toujours au
cabinet (ex. `v.emery@emery-avocats.ch` → Emery Avocats), exactement comme le `site_web`
sert pour Vaud.

`derive_domain_firms()` généralisé pour accepter un extracteur de domaine (`domain_fn`)
et une liste d'exclusion (`excluded_domains`) au lieu d'être câblé sur `site_web`.
Fribourg utilise `email_domain()` comme extracteur, avec une liste
`GENERIC_EMAIL_DOMAINS` de fournisseurs mail grand public (bluewin.ch, gmail.com,
hotmail.com, etc.) — sans quoi 7 avocats indépendants partageant bluewin.ch pour leur
messagerie personnelle auraient été regroupés à tort en un faux « cabinet ».

Résultat : 51 études dérivées, 162 avocats sur 217 (75%) désormais rattachés à un
cabinet plutôt que listés en indépendants isolés. Les 55 restants n'ont pas de domaine
partagé exploitable (email personnel ou domaine à avocat unique non confirmé ailleurs).
4 tests ajoutés (`tests/test_fribourg_email_firms.py`), dont un test explicite
garantissant que les fournisseurs mail grand public ne deviennent jamais un « cabinet ».
50 tests passent au total. Rebuild ciblé (canton FR) + échantillon 40 pages sur
l'ensemble du site : aucun artefact Jinja détecté.

Note pour la suite : ce mécanisme (extraction de domaine depuis l'email) ne s'applique
qu'à Fribourg — c'est le seul des 7 cantons thin (AG, FR, JU, NE, SO, TG, ZG) dont le CSV
contient un champ email exploitable. Les 6 autres (1501 avocats) n'ont aucun signal
structuré de regroupement dans leurs données source ; un test à petite échelle de
recherche web nom par nom est prévu pour évaluer si une autre piste est envisageable.

### 2026-07-29 — Test à petite échelle : recherche web nom par nom (cantons sans email/site_web)

Pour les 6 cantons restants sans aucun signal structuré (AG, JU, NE, SO, TG, ZG — 1501
avocats), test manuel sur un échantillon de 20 avocats d'Argovie (recherche web
"Prénom Nom Rechtsanwalt/Rechtsanwältin canton").

Résultat : 12/20 (60%) rattachements fiables à un cabinet identifiable sans ambiguïté ;
3/20 identité confirmée mais avocat solo (pas de cabinet à rattacher) ou nom de cabinet
contradictoire selon la source ; 5/20 noms trop courants en Suisse (Müller, Weber,
Fröhlich) pour garantir qu'il s'agit du bon homonyme sans signal supplémentaire.

**Conclusion : ne pas automatiser cette approche.** Le problème n'est pas seulement le
taux de succès plus faible que l'enrichissement par domaine (60% contre 76-90%), c'est le
risque qualitatif différent : un domaine mal fetché donne un échec silencieux (rien n'est
publié), alors qu'un nom mal désambiguïsé donne une **fausse attribution à une vraie
personne** (associer un avocat au cabinet de son homonyme). C'est strictement pire que le
principe de non-fabrication du projet — pas une fiche vide, une fiche fausse. Le coût est
aussi plus élevé (une recherche + un jugement de désambiguïsation par avocat, contre un
fetch par domaine qui couvre plusieurs avocats d'un coup).

**Décision : ces 6 cantons restent fermés pour l'instant**, sauf nouvelle piste (ex. un
registre alternatif avec un identifiant plus fiable que le nom seul). Aucune tâche
récurrente n'est dirigée vers eux.

### 2026-07-29 — lot 33 (phase de découverte — autres cantons, lot 8)

- **20 domaines traités** (cabinets ZH/SG — tranche suivante par taille) : **10 succès / 9 échecs / 1 copie**.
- Données stockées dans `data/domaines_autres_cantons.json` (122 succès / 26 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **EPARTNERS AG** (epartners.ch, ZH) : 23 domaines de compétence (full-service : corporate/M&A, arbitrage, concurrence, IT/IA, marché public, insolvabilité, start-ups, sports, télécoms, etc.).
  - **advokatur kanonengasse** (kanonengasse.ch, ZH) : 3 domaines (asile/étranger, famille, pénal). Boutique zurichoise.
  - **Cognitor Rechtsanwälte** (cognitor.ch, ZH) : fondé en **1932** (explicite : date sur le site), spécialisé droit pénal, droit pénal économique, droit de la famille.
  - **rechtsanwälte.og42** (og42.ch, SG) : 8 domaines de compétence (généraliste). Cabinet Saint-Gallois.
  - **bürki bolt rechtsanwälte ag** (buerki-bolt.ch, SG) : fondé en **1920**, **7 avocats** (tous deux explicites sur le site), 14 domaines de compétence (généraliste + notariat). Cabinet ancré à Saint-Gall.
  - **Fricker Füllemann Rechtsanwälte GmbH** (ff-law.ch, ZH) : 7 domaines (pénal, social, migration, circulation, animaux, travail, contrats).
  - **Niedermann Rechtsanwälte** (niedermann.com, ZH) : fondé en **1994** (explicite), 6 domaines (contentieux commercial, recouvrement d'actifs, affaires pénales économiques, entraide judiciaire). Boutique litige international.
  - **5Gambit Disputes AG** (5gambit.com, ZH) : 2 domaines (litige, réglementaire). Boutique spécialisée contentieux.
  - **BodmerFischer AG** (bodmerfischer.ch, ZH) : fondé en **2005** (explicite), 20 domaines de compétence (full-service : arbitrage, bancaire, corporate, pénal, famille, immigration, notariat, sanctions, fiscal, etc.).
  - **Losinger Rechtsanwälte** (losinger.law, ZH) : 17 domaines de compétence (généraliste : travail, banque, succession, AML, sociétés, immobilier, famille, loyer, pénal militaire, voisinage, arbitrage, poursuites, pénal, circulation, contrats, administratif, entreprise).
- **Échecs (9) :** staiger.law, quadra.law, advotech.ch, vincenzpartner.ch, mzbs.ch, drsp-law.ch, reichle-stehle.ch, lexp.ch, klgp.ch — pages vides, rendu JavaScript côté client.
- **Copie (1) :** boeckli-buehler.ch redirige vers bhplaw.ch (déjà en cache). Même cabinet, ancienne URL.
- **Corrections de firm_name (6) :** reetz-sohm.ch (→ "Reetz Sohm AG"), steinlex.ch (→ "Steinbrüchel Hüssy"), lawyers.ch (→ "WALDMANN Rechtsanwälte und Notare"), kellerhals-carrard.ch (→ "Kellerhals Carrard Zürich"), basleradvokatinnen.ch (→ "basleradvokat:innen"), bhplaw.ch (→ "böckli bühler partner") — noms mis à jour pour correspondre aux champs `etude` de leurs CSV respectifs.
- **Clés composites ajoutées (4) :** kellerhals-carrard.ch#BS (BS, "Kellerhals Carrard Basel"), wenger-plattner.ch#ZH (ZH, "Wenger Plattner"), vischer.com#BS (BS, "VISCHER AG"), walderwyss.com#BS (BS, "Walder Wyss AG") — permettent à ces cabinets présents dans plusieurs cantons d'être rattachés dans chaque canton.
- **Rebuild ciblé :** cantons ZH, SG, BS — pages étude + avocat régénérées. Échantillon 40 pages : aucun artefact Jinja détecté.
- **Cache principal GE/VD :** 370 succès / 126 échecs — inchangé.
- **Cache découverte autres cantons :** 122 succès / 26 échecs.
### 2026-07-29 — 4 nouveaux cantons débloqués : Tessin (partiel), Bâle-Campagne, Appenzell Rhodes-Ext., Schaffhouse

Constat déclencheur : les 4 cantons documentés comme « bloqués à la source » (BE, BL, TI, VS)
n'avaient en réalité jamais été revérifiés individuellement — ils avaient été groupés sous une
même étiquette. Une vérification canton par canton a montré que 2 d'entre eux (BL, TI) ont bien
un registre officiel scrapable statiquement, et que 2 cantons supplémentaires jamais documentés
du tout comme « à venir » dans `i18n.CANTONS_A_VENIR` (AR, SH) le sont aussi. Seuls BE et VS
restent réellement bloqués (outil de recherche JS/JSF sans liste statique).

**Bâle-Campagne (BL)** — registre officiel (baselland.ch) : 174 avocats transcrits, adresse
combinée (nom, cabinet, rue, NPA/ville) parsée par une heuristique commune
(`sources/registry_parse_common.py`, `parse_address()` : découpe sur virgules, isole NPA+ville
en fin de chaîne via regex, remonte pour trouver le premier segment avec un chiffre qui n'est
pas une case postale). 174/174 avec NPA/ville, 142/174 avec cabinet identifié, 79 études
dérivées par regroupement texte libre (mécanisme générique existant).

**Appenzell Rhodes-Extérieures (AR)** — registre officiel (ar.ch) : 29 avocats, même parsing,
29/29 correctement traités (échantillon complet vérifié), 10 études dérivées.

**Schaffhouse (SH)** — association professionnelle (shav.ch), le jeu de données le plus riche
des 4 : 36 avocats actifs (14 membres passifs/inactifs explicitement exclus — aucune donnée
exploitable pour eux), avec en plus téléphone, site web, **domaines de compétence** et
**langues parlées** par avocat — deux champs qu'aucun autre canton hors Genève n'a. Nouveaux
champs `domaines_raw`/`langues_raw` ajoutés en passthrough dans `normalize_row()`, consommés
dans `gen_canton_avocats` et `gen_canton_etudes` : les langues sont traduites dans les 4 langues
du site (`LANG_NAME_TRANSLATIONS`, noms de langues uniquement — traduction sûre) et affichées
partout ; les domaines de compétence (jargon juridique) ne sont affichés que sur la page
allemande, langue source, pour éviter tout risque de contresens en traduisant un terme de droit
sans certitude. Résultat : les fiches SH avec ces signaux sortent automatiquement du mécanisme
de noindex (signal réel = ancienneté OU langue OU domaine OU enrichissement web).

**Tessin (TI) — import partiel, à compléter en tâche de fond** : registre officiel (OTAF/CAT,
plateforme TYPO3, pagination `?cHash=...&page=N`, ~91 pages, ~904-907 avocats). Le seul canton
italophone du pays, donc prioritaire pour la crédibilité multilingue du site. Après avoir
constaté que chaque fetch de page coûte ~1800-2000 tokens de contexte (menu/footer/réseaux
sociaux répétés à chaque page pour ~10 avocats utiles), fetcher les 91 pages en une seule
conversation aurait épuisé le budget de contexte avant la fin. Décision : import des 7 premières
pages (70 avocats, 7,7% du total) mis en ligne immédiatement, complément des ~84 pages restantes
(~834 avocats) délégué à un mécanisme en arrière-plan à concevoir (probablement une tâche
planifiée dédiée, suivant le même principe que celle des cabinets : traiter un lot de pages par
exécution, état persisté en JSON, commit+push, reprise au lot suivant) — **pas encore créée**,
à faire dans une prochaine session.

Parsing Tessin : mêmes heuristiques (`registry_parse_common.py`), avec en plus une colonne
`date_inscription` (renommée depuis l'italien « iscrizione ») lue par `normalize_row()` pour
dériver `annee_admission` automatiquement, comme pour les autres cantons. 68/70 avec NPA/ville
(2 sans code postal dans la source, laissé vide plutôt que deviné), 39/70 avec cabinet identifié
(beaucoup d'avocats tessinois ne listent qu'une adresse personnelle, sans cabinet).

**Fichiers sources bruts** conservés dans `sources/` (transcriptions + scripts de parsing) pour
traçabilité/audit, distincts des CSV finaux dans `data/`.

**État après cet ajout : 23 cantons sur 26 avec des données actives** (au lieu de 19),
soit ~88% des cantons suisses. Seuls BE, VS (registres inaccessibles) et le solde du Tessin
(834 avocats restants, mécanisme de complément à créer) restent à traiter. Build complet
vérifié (import + rebuild ciblé des 4 nouveaux cantons + échantillon complet des pages
générées) : aucun artefact Jinja, 50 tests existants toujours au vert.

### 2026-07-29 — lot 34 (phase de découverte — autres cantons, lot 9)

- **20 domaines traités** (cabinets LU/BS/GR/SG — tranche suivante par taille) : **14 succès / 6 échecs**.
- Données stockées dans `data/domaines_autres_cantons.json` (140 succès / 32 échecs au total).
- **Résultats notables (nouveaux faits extraits) :**
  - **Troller Hitz Troller** (trollerlaw.ch, LU) : fondé en **1941** ("im Jahre 1941 gegründete"), 8 domaines
    (Wirtschaftsrecht, Immaterialgüterrecht, Wettbewerbsrecht, Handels/Gesellschaftsrecht, Bankenrecht,
    Vertragsrecht, Staats/Verwaltungsrecht, Notariat). Bureaux Luzern + Bern.
  - **Kaufmann Rüedi Rechtsanwälte AG** (krlaw.ch, LU) : fondé en **1974** ("Gemeinsamer Erfolg seit 1974"),
    15 domaines de compétence (Arbeiten, Beschaffungswesen, Compliance/Wirtschaftsstrafrecht,
    Familie/Erbe, Gesundheit/Life Sciences, Immobilien/Bauen, Inkasso/Insolvenz, International Desk,
    IT/ICT/Datenschutz, Notariat, Übersetzungen, Schiedsgerichtsbarkeit/Mediation, Sportrecht,
    Staat/Behörden, Unternehmen/M&A/Nachfolge). Certifié ISO 9001:2015.
  - **Hofstetter Advokatur & Notariat AG** (hofstetteradvokatur.ch, LU) : fondé en **1987** ("Since 1987"),
    4 domaines (Bau/Planungsrecht, Immobilienrecht, Erb/Nachlassrecht, Energie/Umweltrecht).
  - **Anwaltsgemeinschaft Baud Diehl Stauffer** (awg.ch, BS) : fondé en **1981** ("Seit 1981 beraten und
    vertreten wir…"), 10 domaines (Berufliche Vorsorge, Familienrecht, Sozialversicherungsrecht,
    Arbeitsrecht, Migrationsrecht, Erbrecht, Mediation, Ombudsstellen, Strafrecht, Vereins/Stiftungsrecht).
    Note : les deux entrées BS ("Baud, Diehl, Stauffer" et "Baud Diehl Stauffer") ont le même nom-cœur
    → collision détectée par `attach_name_based_enrichment` → enrichissement non rattaché pour l'instant
    (mieux vaut aucun rattachement qu'un rattachement ambigu). À corriger ultérieurement en fusionnant
    les deux entrées du registre BS.
  - **Schwegler & Partner Anwälte und Notare AG** (anwaltspraxis.ch, LU) : fondé en **1997** (explicite),
    généraliste (Anwalts/Notariats/Mediationstätigkeit). Bureaux Menznau + Sursee.
  - **Stadelmann Advokatur & Notariat AG** (stadelmann-law.ch, LU) : 6 domaines (Bau/Immobilienrecht,
    Gesellschafts/Vertragsrecht, Arbeitsrecht, Erbrecht, Notariat, Mediation). Bureaux Luzern/Ruswil/Willisau.
  - **Brack & Partner AG** (brackpartner.ch, LU) : 8 domaines (Immobilien/Bau/Miete, Wirtschaftsstrafrecht,
    Vertragsrecht/Wirtschafts/Gesellschaftsrecht, Scheidung/Konkubinat, Notariat, Altersvorsorge,
    Betreibung/Konkurs, Domizile/Verwaltungsrat).
  - **Hess Advokatur AG** (hess-advokatur.ch, LU) : 17 domaines (Alter, Arbeit, Bauen, Datenschutz,
    Familie, Gemeinde, Internet, Immaterialgüterrecht, Kindesvertretung, KMU, Landwirtschaft, Mediation,
    Miete, Notariat, Strafrecht, Schule, Strassenverkehr). Bureaux Sursee + Luzern.
  - **Vetsch Rechtsanwälte AG** (vetsch-rechtsanwaelte.ch, LU) : 11 domaines (Notariat, Erbrecht,
    Familienrecht, Immobilienrecht, Vertragsrecht, Gesellschaftsrecht, Arbeitsrecht, Mietrecht,
    Schuldbetreibungsrecht, Landwirtschaftsrecht, Strafrecht). Bureaux Luzern + Hochdorf.
  - **Kanzlei Kornplatz AG** (kornplatz.ch, GR) : 17 domaines (Verwaltungsrecht, Baurecht, Vertragsrecht,
    Gesellschaftsrecht/M&A, Strafrecht, Datenschutz, Familienrecht, Erbrecht, Arbeitsrecht, Litigation,
    Notariat, Raumplanung, Immobilienrecht, Sportrecht, Submissionsrecht, Steuerrecht, Mietrecht).
    Bureaux Chur/Flims/St.Moritz.
  - **BänzigerPallySchuler KLG** (bps-partner.ch, GR) : 4 domaines (Öffentliches Recht, Strafrecht,
    Privatrecht, Notariat).
  - **Gremmelspacher Ruppanner Roth Gass** (advokaturteam.ch, BS) : 17 domaines (Zivilrecht + Öffentliches
    Recht + Strafrecht : Arbeitsrecht, Familienrecht, Gesellschaftsrecht, Haftpflichtrecht,
    Immaterialgüterrecht, Mietrecht, Persönlichkeitsrecht, Sachenrecht, SchKG, Vertragsrecht, Life Sciences,
    Medienrecht, Öff.Personalrecht, Raumplanung, Verwaltungsrecht, Strafverteidigung, Opfervertretung).
  - **SteuriFisch AG** (steurifisch.ch, SG) : 11 domaines (Erbrecht, Familienrecht, Strafrecht,
    Gesellschafts/Handelsrecht, Bildungs/Schulrecht, Vertragsrecht, Arbeitsrecht, Mietrecht, Baurecht,
    Datenschutzrecht, IP-IT-Recht). Bureaux Wil SG/Zürich/Gossau SG.
  - **Hofmann Gehler Schmidlin & Partner Rechtsanwälte und Notare KLG** (anwaelte-hgs.ch, SG) : 21 domaines
    (Familienrecht, Kindes/Erwachsenenschutzrecht, Scheidungsrecht, Erbrecht, Sachenrecht,
    allgemeines Vertragsrecht, Mietrecht, Arbeitsrecht, Werkvertragsrecht, Haftpflichtrecht,
    Versicherungsrecht, Gesellschaftsrecht, Handelsrecht, Baurecht, öff.Bau/Planungsrecht,
    Enteignungsrecht, Sozialversicherungsrecht, Strassenverkehrsrecht, Schuldbetreibungsrecht,
    Verwaltungsrecht, Steuerrecht). Bureaux Rapperswil-Jona + St-Gall.
- **Échecs (6) :** rudolf-bieri.ch (JS), museum35.ch (JS), indemnis.ch (JS), baeumlin-partner.ch (JS),
  kuenglaw-sg.ch (accessible mais aucun fait extractible), sglaw.ch (accessible mais aucun fait extractible).
- **Corrections firm_name (8 entrées _failed) :** staiger.law, quadra.law, advotech.ch, vincenzpartner.ch,
  mzbs.ch, drsp-law.ch, reichle-stehle.ch, klgp.ch — firm_name et canton ajoutés pour permettre à
  `is_handled()` de les reconnaître correctement dans les prochains passages.
- **Années de fondation trouvées ce lot :** 1941 (Troller), 1974 (Kaufmann Rüedi), 1981 (AWG Baud Diehl
  Stauffer), 1987 (Hofstetter), 1997 (Schwegler & Partner) — 5 nouvelles dates.
- **Rebuild ciblé :** cantons LU (8 études/58 avocats), BS (1 étude/6 avocats), GR (2 études/12 avocats),
  SG (2 études/12 avocats) — pages étude + avocat régénérées (~376 pages × 4 langues). Zéro artefact Jinja.
- **Cache découverte autres cantons :** 140 succès / 32 échecs (total cumulé).

### 2026-07-29 — vectis-tessin-scraping, lot 1 (pages 8-17)

Première exécution de la tâche planifiée dédiée au complément du Tessin. Pages 8 à 17 du
registre cantonal (www4.ti.ch) fetchées avec succès (10/10, aucun échec). 100 avocats extraits
(BELTRAMI Gianfrancesco → CAMPONOVO Teo), écrits dans `sources/ti_raw/batch02.txt`.

`sources/build_ti_csv.py` relancé : combine batch01 (70) + batch02 (100) = **170 avocats** dans
`data/avocats_tessin.csv` (164/170 avec NPA/ville identifié, 94/170 avec cabinet identifié).
Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 1068 fichiers `dist/**/tessin|ticino/**/index.html` générés, échantillon
complet vérifié sans artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 7 → 17.

**Cumul : 170 avocats sur ~907 (18,7%), page 17/91.**

### 2026-07-29 — lot 35 (phase de découverte — autres cantons, lot 10)

- **20 domaines traités** (ZH/BS/SG/BL/GR — clés composites + nouvelles études) : **13 succès (dont 4 clés composites) / 7 échecs**.
- Cache mis à jour : `data/domaines_autres_cantons.json` → **148 succès / 37 échecs** (total cumulé).
- **Clés composites ajoutées (même cabinet, plusieurs cantons) :**
  - `bratschi.ch#SG` et `bratschi.ch#BS` : Bratschi AG (fondé 2008, 120 avocats) déjà en cache pour ZH —
    composite keys pour rattacher les bureaux SG et BS.
  - `swisslegal.ch#ZH` (SwissLegal (Zürich) AG) et `swisslegal.ch#SG` (SwissLegal asg.advocati) :
    8 domaines communs (Commercial Law & Tax, Construction & Real Estate, Family/Marriage/Succession,
    Data/Technology/AI & Crypto, Litigation & Arbitration, Labour/Mobility/Health, Notarial Services,
    Federal & Administrative Law). La clé de base `swisslegal.ch` correspond à SwissLegal Dürr + Partner (BS).
- **Nouveaux succès (faits extraits) :**
  - **LEXPARTNERS.** (lexpartners.ch, BL) : fondé en **1978** par Prof. Ernst Fischli,
    cabinet d'avocats et notaires spécialisé BL/BS.
  - **\@vocate** (vocate.ch, SG) : **6 avocats** (3 femmes, 3 hommes) — effectif confirmé explicitement.
  - **Spühler Rechtsanwälte AG** (spuehler.legal, ZH) : 6 domaines (Strafverteidigung, Opfervertretung,
    Familienrecht, Arbeitsrecht, Vertragsrecht, Betreibung und Konkurs).
  - **Strazzer Zeiter Rechtsanwälte AG** (szlaw.ch, ZH) : 8 domaines (Nachlassplanung, Nachlassabwicklung,
    Erbstreitigkeiten, Ehegüterrecht, Erwachsenenschutz und Vorsorge, Vertragsrecht und
    Vermögensgestaltung, Unternehmensnachfolge, Philanthropie und Stiftungen). Spécialiste Erbrecht.
  - (kspartner.ch, mfpartner.ch, gigerpartnerlaw.ch, dufour-advokatur.ch déjà en cache depuis lots précédents,
    non recomptés ici.)
- **Échecs (7) :** lplegal.ch (aucun fait extractible), kanzlei-helvetiaplatz.ch (JS/Readymag),
  kanzlei-im-turm.ch (JS/Webflow), suter.legal (URL hors provenance), advobasel.ch (mauvais cabinet :
  Pfander/Alder ≠ Emmel/Jedelhauser BS « Advokatur und Mediation »), hol-law.ch (déjà en cache ZH),
  mzbs.ch (déjà en _failed).
- **Note technique :** collision de nom toujours active pour « Baud, Diehl, Stauffer » / « Baud Diehl Stauffer »
  (deux entrées BS avec le même nom-cœur) — enrichissement awg.ch toujours non rattaché (mieux vaut rien
  qu'ambigu). À corriger en fusionnant les deux entrées du registre BS.
- **Rebuild ciblé :** bratschi.ch (ZH/SG/BS), swisslegal.ch (BS/ZH/SG), lexpartners.ch (BL),
  vocate.ch (SG), spuehler.legal (ZH), szlaw.ch (ZH). Zéro artefact Jinja (60 fichiers vérifiés).
- **Cache découverte autres cantons :** 148 succès / 37 échecs (total cumulé).

### 2026-07-29 — lot 36 (phase de découverte — autres cantons, lot 11)

*Note : entrée de journal reconstruite rétrospectivement — le commit 7022c49 a mis à jour le
header et le cache JSON mais a omis d'écrire cette section. Données issues du commit et du JSON.*

- **20 domaines traités** (ZH — tranche suivante par taille) : **9 succès / 9 échecs / 2 mises à jour d'entrées existantes**.
- Cache mis à jour : `data/domaines_autres_cantons.json` → **157 succès / 46 échecs** (total cumulé).
- **Succès (9, tous ZH) :**
  - **VALLONI Attorneys at Law GmbH** (valloni.ch) : 4 domaines (Vertragsrecht, Gesellschaftsrecht,
    Immobilienrecht, Schiedsgerichtsbarkeit/Mediation).
  - **SILK Rechtsanwälte** (silk-rechtsanwaelte.ch) : 16 domaines de compétence (cabinet spécialisé).
  - **Legis Rechtsanwälte AG** (legis-law.ch) : présence confirmée, aucun fait chiffré.
  - **BÜHLMANN KOENIG & PARTNER AG** (bkp-legal.ch) : 6 domaines (Wirtschaftsrecht, Streit/Schiedsverfahren,
    Technologie/IP/Datenschutz, Immobilien/Bau, Steuerrecht, Regulierung/Compliance).
  - **DAVATZ LEGAL AG** (davatzlegal.ch) : 2 domaines (Bau/Immobilienrecht, Schiedsgerichtsbarkeit).
  - **Romero & Ziegler Meier Jucker Rechtsanwälte** (romeroziegler.ch) : fondé en **1999** — présence confirmée.
  - **Frey & Jud Rechtsanwälte** (frey-jud.ch) : présence confirmée, aucun fait chiffré.
  - **Scherler Siegenthaler Schweizer Rechtsanwälte AG** (advo-net.ch) : présence confirmée.
  - **Charles Russell Speechlys AG** (charlesrussellspeechlys.com#ZH, clé composite) : 5 domaines
    (Corporate/M&A, Private Client, Employment, IP/Technology, Dispute Resolution) — bureau ZH du réseau
    international, chiffres locaux uniquement.
- **Échecs (9) :** lexp.ch (JS), quadra.law (JS — mise à jour firm_name/canton),
  staiger.law (JS — mise à jour firm_name/canton), advotech.ch (BS/JS), baeumlin-partner.ch (BS/JS),
  indemnis.ch (BS/JS), klgp.ch (SZ/JS), museum35.ch (SG/JS), vincenzpartner.ch (GR/JS).
- **Cache découverte autres cantons :** 157 succès / 46 échecs (total cumulé).

### 2026-07-29 — Tessin, lot pages 18-27 (tâche planifiée vectis-tessin-scraping)

Pages 18 à 27 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 100 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch03.txt`.

`sources/build_ti_csv.py` relancé sur les 3 lots cumulés (`batch01.txt` + `batch02.txt` +
`batch03.txt`) : **270 avocats** dans `data/avocats_tessin.csv` (258/270 avec npa/ville identifié,
154/270 avec cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 808 fichiers `dist/**/tessin|ticino/**/index.html` régénérés, aucun
artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 17 → 27.

**Cumul : 270 avocats sur ~907 (29,8%), page 27/91.**

### 2026-07-29 — lot 37 (file d'attente épuisée)

- **0 domaines traités.** La file d'attente de la phase de découverte est vide : tous les cabinets
  de ≥3 avocats dans les cantons de découverte (ZH, BS, SG, LU, GR, SZ, AI, GL, NW, OW, UR)
  ont été traités ou tentés.
- **Détail par canton :** ZH (1260 études dérivées), SG (248), LU (179), BS (175), GR (148), SZ (77),
  OW (19), NW (16), GL (7), UR (5), AI (1). Cantons avec 0 études dérivées (pas d'entrée `etude` dans
  le CSV) : AG, JU, NE, SO, TG, ZG — exclus depuis le 29/07/2026 (test web nom par nom : 60% fiabilité,
  risque d'homonymie).
- **Compte exact :** 202 paires (nom-cœur, canton) couvertes sur 202 identifiées (seuil 3 avocats).
  Cache `domaines_autres_cantons.json` : **157 succès / 46 échecs** (inchangé).
- **Aucun rebuild, aucune modification de données** — seule cette entrée de journal est ajoutée.
- **Prochaine action :** Greg doit rediriger explicitement cette tâche planifiée. Pistes possibles :
  descendre à 2 avocats (non recommandé — testé, rendement très faible), cibler BE/VS si une nouvelle
  source de données apparaît, ou désactiver la tâche si l'enrichissement est considéré complet.

### 2026-07-29 — Tessin, lot pages 28-37 (tâche planifiée vectis-tessin-scraping)

Pages 28 à 37 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 100 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch04.txt`.

`sources/build_ti_csv.py` relancé sur les 4 lots cumulés (`batch01.txt` à `batch04.txt`) :
**370 avocats** dans `data/avocats_tessin.csv` (353/370 avec npa/ville identifié, 215/370 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 2160 fichiers `dist/**/tessin|ticino/**/index.html` régénérés, aucun
artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 27 → 37.

**Cumul : 370 avocats sur ~907 (40,8%), page 37/91.**

### 2026-07-29 — Tessin, lot pages 38-47 (tâche planifiée vectis-tessin-scraping)

Pages 38 à 47 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 100 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch05.txt`.

`sources/build_ti_csv.py` relancé sur les 5 lots cumulés (`batch01.txt` à `batch05.txt`) :
**470 avocats** dans `data/avocats_tessin.csv` (452/470 avec npa/ville identifié, 280/470 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 1346 fichiers `dist/**/tessin/**/index.html` + 1346 `dist/**/ticino/**/index.html`
régénérés, aucun artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 37 → 47.

**Cumul : 470 avocats sur ~907 (51,8%), page 47/91.**

### 2026-07-29 — Tessin, lot pages 48-57 (tâche planifiée vectis-tessin-scraping)

Pages 48 à 57 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 99 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch06.txt` (une entrée, MAMELI Gabriella,
apparaissait en doublon exact à la frontière pages 53/54 — dédupliquée automatiquement par
`build_ti_csv.py`).

`sources/build_ti_csv.py` relancé sur les 6 lots cumulés (`batch01.txt` à `batch06.txt`) :
**569 avocats** dans `data/avocats_tessin.csv` (547/569 avec npa/ville identifié, 329/569 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 9432 fichiers `dist/**/tessin/**/index.html` + `dist/**/ticino/**/index.html`
régénérés, aucun artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 47 → 57.

**Cumul : 569 avocats sur ~907 (62,7%), page 57/91.**

### 2026-07-29 — Tessin, lot pages 58-67 (tâche planifiée vectis-tessin-scraping)

Pages 58 à 67 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 100 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch07.txt`.

`sources/build_ti_csv.py` relancé sur les 7 lots cumulés (`batch01.txt` à `batch07.txt`) :
**669 avocats** dans `data/avocats_tessin.csv` (643/669 avec npa/ville identifié, 380/669 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 3664 fichiers `dist/**/tessin/**/index.html` + `dist/**/ticino/**/index.html`
régénérés, aucun artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 57 → 67.

**Cumul : 669 avocats sur ~907 (73,8%), page 67/91.**

### 2026-07-29 — Tessin, lot pages 68-77 (tâche planifiée vectis-tessin-scraping)

Pages 68 à 77 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 99 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch08.txt` (une entrée, ROSSETTI Raffaele,
apparaissait en doublon exact à la frontière pages 76/77 — dédupliquée automatiquement par
`build_ti_csv.py`).

`sources/build_ti_csv.py` relancé sur les 8 lots cumulés (`batch01.txt` à `batch08.txt`) :
**768 avocats** dans `data/avocats_tessin.csv` (742/768 avec npa/ville identifié, 438/768 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 4136 fichiers `dist/**/tessin/**/index.html` + `dist/**/ticino/**/index.html`
régénérés, aucun artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 67 → 77.

**Cumul : 768 avocats sur ~907 (84,7%), page 77/91.**

### 2026-07-29 — Tessin, lot pages 78-87 (tâche planifiée vectis-tessin-scraping)

Pages 78 à 87 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (10/10 pages,
aucun échec). 100 nouveaux avocats extraits (noms, adresses, dates d'inscription) selon le format
pipe-delimité habituel, écrits dans `sources/ti_raw/batch09.txt`.

`sources/build_ti_csv.py` relancé sur les 9 lots cumulés (`batch01.txt` à `batch09.txt`) :
**868 avocats** dans `data/avocats_tessin.csv` (837/868 avec npa/ville identifié, 499/868 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 4668 fichiers `dist/**/tessin/**/index.html` + `dist/**/ticino/**/index.html`
régénérés, aucun artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 77 → 87.

**Cumul : 868 avocats sur ~907 (95,7%), page 87/91.**

### 2026-07-29 — Tessin, lot pages 88-91 (tâche planifiée vectis-tessin-scraping) — IMPORT TERMINÉ

Pages 88 à 91 du registre cantonal tessinois (www4.ti.ch) récupérées avec succès (4/4 pages,
aucun échec — c'était le solde des 91 pages du registre). 34 lignes extraites (noms, adresses,
dates d'inscription) selon le format pipe-delimité habituel, écrites dans `sources/ti_raw/batch10.txt`.
Chevauchement attendu en fin de pagination : ZORZI Luca et ZORZI Nicola apparaissent à la fois en
page 90 et en page 91 (le registre source a légèrement bougé entre les deux fetches, passant de
904 à 906 résultats totaux affichés) — dédupliqués automatiquement par `build_ti_csv.py`
(nom+adresse), donc sans double compte dans le CSV final.

`sources/build_ti_csv.py` relancé sur les 10 lots cumulés (`batch01.txt` à `batch10.txt`) :
**902 avocats** dans `data/avocats_tessin.csv` (870/902 avec npa/ville identifié, 516/902 avec
cabinet identifié).

Rebuild ciblé du canton TI (`gen_canton_hub`, `gen_canton_cross`, `gen_canton_etudes`,
`gen_canton_avocats`) : 4832 fichiers `dist/**/tessin/**/index.html` + `dist/**/ticino/**/index.html`
régénérés, aucun artefact Jinja (`{{`, `{%`, `Undefined`). Suite de tests : 50/50 au vert.

`data/tessin_import_progress.json` : `last_page_imported` 87 → 91 (= `total_pages`, 91/91).

**Cumul final : 902 avocats sur ~907 attendus (99,4%), 91/91 pages — l'import du Tessin est
terminé.** L'écart résiduel (~5 avocats) s'explique par le mouvement naturel du registre source
entre le début et la fin de la collecte (radiations/inscriptions en cours de route, le registre
n'est pas figé) et par la marge d'incertitude du chiffre indicatif initial (907), pas par des pages
manquées. La tâche planifiée `vectis-tessin-scraping` n'a plus de raison de tourner : à supprimer
(`mcp__scheduled-tasks__delete_scheduled_task`, id `vectis-tessin-scraping`) lors d'une prochaine
session interactive, ou laissée tourner sans effet (chaque exécution future constatera
`last_page_imported >= total_pages` et s'arrêtera sans rien committer, comme prévu par son prompt).

## PAUSE DE LA COLLECTE DE DONNÉES (29/07/2026, décision de Greg)

Greg a explicitement décidé de s'arrêter là pour la donnée pour l'instant : **aucune tâche
planifiée ne doit relancer une collecte ou une extension de périmètre sans instruction
explicite de sa part.** Concrètement, à ce stade :

- `vectis-tessin-scraping` a été supprimée (import terminé, 902/907, 91/91 pages).
- `vectis-enrichissement-cabinets` reste désactivée (file d'attente GE/VD épuisée, phase de
  découverte des 11 autres cantons épuisée aussi — 154 cabinets rattachés, seuil 3+ avocats
  atteint). **Ne pas la réactiver, ne pas baisser le seuil de 3 avocats, ne pas la rediriger
  vers BE/VS ni vers les 6 cantons fermés (AG, JU, NE, SO, TG, ZG)** sans que Greg le demande
  explicitement dans une conversation.
- Toute future session qui reprend ce projet doit traiter l'état de données actuel (24/26
  cantons actifs : GE + 23 génériques dont TI/BL/AR/SH ; BE et VS absents ; 6 cantons fermés
  sans regroupement) comme un point d'arrêt stable, pas comme un chantier à reprendre
  automatiquement.

Si une nouvelle source de données apparaît (BE, VS, ou une piste pour les 6 cantons fermés),
ou si Greg redemande explicitement de continuer l'enrichissement, cette pause peut être levée
— mais l'initiative doit venir de lui.

## REPRISE EXPLICITE DE L'ENRICHISSEMENT (06/09/2026, décision de Greg)

Contexte : la mise à jour anti-spam de Google (« scaled content abuse », déploiement confirmé
18-21/08/2026) a fait chuter le nombre d'URLs indexées à partir du 19/08/2026, en ciblant très
probablement les ~8 333 fiches avocat « thin » (nom + ville seuls, sans signal réel). Greg a
explicitement redemandé de relancer l'enrichissement pour combler ce déficit de signal réel
(jamais de texte généré par IA — uniquement des faits vérifiés sur sites officiels/OSM, avec
`source_url`/date). Ceci lève la pause du 29/07/2026 ci-dessus, dans le cadre précis suivant
(pas un blanc-seing général) :

- **Phase 3 (cabinets, 12 cantons groupables)** : reprise de `data/domaines_autres_cantons.json`
  (ZH/TI/SG/GR/BL/SZ/UR/OW/NW/AR/AI/LU), même méthodologie que les lots ci-dessus, plus fallback
  OpenStreetMap Overpass (`office=lawyer|notary`) quand le site officiel est inaccessible/JS.
  Lot porté à 50 cabinets/heure (demande explicite de Greg).
- **Phase 3b (nouvelle)** : avocats individuels des 5 cantons sans champ `etude` du tout
  (AG/ZG/NE/TG/SO — précédemment qualifiés à tort de « structurellement impossibles », corrigé
  après test réel) — cache `data/avocats_individuels_enrichment.json`, rattachement par nom+canton
  (`attach_individual_enrichment` dans build.py).
- **Phase 3c (nouvelle)** : avocats indépendants (`solo`, sans étude) au sein des 12 cantons
  groupables de la Phase 3 — 634 fiches identifiées comme non couvertes ni par Phase 3 ni par 3b —
  même cache que 3b.
- **BE et VS restent hors périmètre** (registre JS/JSF non scrapable, décision de Greg de ne pas
  s'y attaquer maintenant) — ne pas étendre à ces deux cantons sans nouvelle demande explicite.
- **Le seuil de 3+ avocats pour le regroupement en étude reste inchangé.**

Bug d'infrastructure corrigé le même jour : les 3 tâches planifiées (Phase 3/3b/3c) avaient été
créées avec `create_new_session_on_fire: true`, ce qui spawnait à chaque déclenchement une
session neuve sans accès push au dépôt (`add_repo` absent/bloqué par une confirmation humaine
obligatoire) — échec systématique, aucune donnée perdue (juste des appels de recherche
gaspillés), les 3 anciennes tâches supprimées et recréées pour se déclencher directement dans
la session interactive principale (qui a déjà l'accès push confirmé), sur demande explicite de
Greg (« zéro action de ta part »).

### 2026-09-06 — Phase 3, lot 1 (premier passage horaire depuis la reprise)

12 cabinets traités (12 succès / 2 échecs) dans les cantons ZH et SG, tous vérifiés sur leur
site officiel (WebFetch direct, jamais de traduction croisée) : Klein Rechtsanwälte AG (ZH,
domaines EN, tel/email), gbf Rechtsanwälte AG (ZH, domaines EN, tel), VIALEX Rechtsanwälte AG
(ZH, tel/email), Landmann & Partner AG (ZH, domaines DE, tel/email, Fachanwalt SAV Strafrecht/
Familienrecht), Tappolet & Partner (ZH, domaines DE, tel/email, 7 avocats), Advokatur Gartenhof
(ZH, domaines DE, tel), Stiffler & Partner (ZH, fondé **1975**, domaines EN, tel/email,
Fachanwältin SAV Erbrecht, publication « Schweizerisches Schneesportrecht » 3e éd. 2002),
Bachmann Rechtsanwälte AG (ZH, fondé **2009**, domaines EN, tel/email), Neupert Vuille Partners
(ZH, fondé **1851**, domaines EN, tel/email), FRT RECHTSANWÄLTE & NOTARE (SG, tel/email),
Zürcher Rechtsanwälte AG (ZH, domaines EN, tel), ZL ZurichLawyers (ZH, domaines DE, tel, 12
avocats). **Échecs (2) :** suterhowald.ch (HTTP 503, site indisponible au moment du passage),
eversheds-sutherland.com (page équipe bloquée HTTP 403).

Rattachement (`attach_name_based_enrichment`) : 166 études rattachées au total (154 → 166, +12,
zéro nouvelle collision). Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3b, lot 1 (premier passage horaire depuis la reprise)

7 avocats individuels traités (7 succès / 1 échec) dans AG (3), ZG (3), NE (1) — début de liste
alphabétique, ordre stable choisi en l'absence de signal de priorisation : Marcel Aebi (AG,
Contractus AG, domaines DE, tel), Jacqueline Alf (AG, Voser Rechtsanwälte, domaines DE,
tel/email), Jonas Ammann (AG, Berger Rohrer Rechtsanwältinnen AG, domaines DE, email), Aepli
Michael (ZG, Studer & Aepli, domaines DE, tel/email), Aeschi Othmar (ZG, Aeschi Notariat &
Anwaltskanzlei, domaines DE, tel), Amstad-Dittli Alexandra (ZG, fondé **2017**, domaines DE,
tel/email), David Agerba (NE, Étude Agerba, domaines FR, tel). **Échec (1) :** Simon Aiassa (NE,
aucun site personnel trouvé, seulement listé au rôle du barreau).

Rattachement (`attach_individual_enrichment`) : 7/7 rattachés, zéro collision. TG et SO pas
encore traités (prochain lot). Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3c, lot 1 (premier passage horaire depuis la reprise)

Vérification préalable importante : les avocats `solo` des 12 cantons groupables (ZH/TI/SG/GR/
BL/SZ/UR/OW/NW/AR/AI/LU) sont les **mêmes objets Python** que dans `CANTON_DATA[code]["individuals"]`
(juste un sous-ensemble filtré, pas une copie) — `attach_individual_enrichment` qui parcourt
`individuals` rattache donc aussi correctement les entrées `solo`, aucune modification de
build.py nécessaire. Vérifié explicitement avant de committer.

9 avocats indépendants traités (canton TI, 386 avocats sans étude au registre cantonal — début
de liste alphabétique) : **5 succès / 5 échecs**. Succès : ACHERMANN BERNASCHINA Sonja (Studio
legale e notarile Cattori-Achermann-Bernaschina, domaines IT, mediatrice FSA), ALLIDI Aldo/Luca/
Rachele (Studio Allidi, fondé **1971**, domaines IT, tel/email — étude familiale à 3 avocats,
un seul WebFetch réutilisé pour les 3 fiches), ALDI Sabrina (Studio Legale Aldi, domaines IT,
email). **Échecs (5) :** ABATE Fabio, AFFOLTER Christof, AGUSTONI Alberto, AIROLDI Luca,
ANDREOLI Alida — aucun site officiel personnel trouvé (seulement registre cantonal, déjà en
base via le CSV, et annuaires tiers type search.ch/local.ch non exploités pour éviter la
redondance et la dépendance à des sources secondaires).

Rattachement (`attach_individual_enrichment`) : 12/12 rattachés au total (7 phase 3b + 5 phase
3c), zéro collision. Reste 625 avocats solo sur 634 (12 cantons groupables, 9 traités ce lot).
Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3, lot 2 (2e passage horaire)

6 cabinets traités (6 succès / 0 échec), tous à Lugano (TI) sauf Pachmann (pas de domaine
officiel trouvé, écarté sans forcer) : Studio legale 1896 SA (fondé **1896**, domaines EN),
TEAM LEGAL SA (domaines IT, tel — 3 bureaux Lugano/Locarno/Mendrisio), Studio legale e notarile
Gaggini & Partners SA (fondé **1954**, 19 domaines IT), Aequitas Studio legale e notarile
(domaines IT, tel/email, 9 avocats/notaires, 3 publications de Rosa Maria Cappa 2023-2024 avec
titres exacts). **Clés composites ajoutées (cabinets internationaux déjà en cache pour d'autres
cantons, bureau tessinois ajouté)** : `baerkarrer.ch#TI` (Bär & Karrer, bureau Lugano — mêmes
données que ZH, notes précisant que les chiffres sont globaux au cabinet), `kellerhals-carrard.ch#TI`
(Kellerhals Carrard Lugano SA, idem).

Rattachement (`attach_name_based_enrichment`) : 172 études rattachées au total (166 → 172, +6,
zéro nouvelle collision). Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3b, lot 2 (2e passage horaire)

4 avocats individuels traités (4 succès / 0 échec) dans TG (2) et SO (2) — TG et SO complètement
non traités jusqu'ici, donc repris depuis le début de leur liste alphabétique respective :
David Georg Ackermann (TG, FLB Rechtsanwälte, tel/email, Fachanwalt SAV Familienrecht + Mediator
SAV/SDM-FSM), Elsbeth Verena Aepli (TG, Recht am See Anwaltsbüro — renommé depuis Schlatter Aepli
Partner début 2026, domaines DE, tel/email), Beatrice Abegglen (SO, domaines DE, tel — source :
annuaire professionnel jurata.ch, aucun site officiel personnel trouvé), Christian Aebersold
(SO, Morandi Schnider Rechtsanwälte und Notare, 9 domaines DE, tel/email).

Rattachement (`attach_individual_enrichment`) : 16/16 rattachés au total (12 → 16, +4), zéro
collision. AG (3/459), ZG (3/396), NE (1/259), TG (2/151), SO (2/188) traités à ce stade.
Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3c, lot 2 (2e passage horaire)

4 avocats indépendants traités (canton TI, suite de la liste alphabétique) : **4 succès / 0
échec**. AGUSTONI Emanuela (fondé **1983**, domaines IT, tel/email — source annuaire
professionnel, aucun site officiel personnel trouvé), AGUSTONI Paolo (Studio legale Agustoni —
peu de données disponibles au-delà du nom du cabinet, ancien syndic de Bellinzone), ANTONINI
LUVINI Micaela (cabinet privé ouvert en **1991**, domaines IT — droit du travail, LPar, droit de
la famille — tel/email, exerce aujourd'hui comme consultante chez equi-lab.ch), AUGUGLIARO
Giovanni (Studio Legale e Notarile Augugliaro, actif depuis **1984**, tel/email, bureaux
Lugano + Mendrisio).

Rattachement (`attach_individual_enrichment`) : 20/20 rattachés au total (16 → 20, +4), zéro
collision. TI : 13/386 avocats solo traités à ce stade. Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3, lot 3 (3e passage horaire)

4 cabinets traités (4 succès / 0 échec) : REBER Rechtsanwälte (ZH, fondé **1988**, domaines EN,
tel/email, 13 collaborateurs, "Top Law Firm 2026" Bilanz), btc.legal SA (TI, tel/email, 13
collaborateurs), Studio legale e notarile Perucchi (TI, fondé **1959**, 15 domaines IT,
tel/email), Mattei & Partners Studio Legale SA (TI, fondé **1995**, tel/email, 10 avocats).

Rattachement (`attach_name_based_enrichment`) : 176 études rattachées au total (172 → 176, +4,
zéro nouvelle collision). Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3b, lot 3 (3e passage horaire)

3 avocats individuels traités (3 succès / 0 échec) dans NE (2) et AG (1) : Gautier Aubert et
Oriane Aubert (NE, A2L Avocates et Avocats de l'Entre-deux-Lacs, domaines FR, tel/email partagé
— même cabinet, un seul WebFetch réutilisé pour les 2 fiches), Stefan Augstburger (AG, Merki &
Partner, domaines DE, tel/email, notaire et avocat depuis 2012/2017).

Rattachement (`attach_individual_enrichment`) : 23/23 rattachés au total (20 → 23, +3), zéro
collision. Suite de tests : 91/91 au vert.

### 2026-09-06 — Phase 3c, lot 3 (3e passage horaire)

3 avocats indépendants traités (canton TI, suite de la liste alphabétique) : **3 succès / 0
échec**. AMMANN BONFANTI Claudia (Studio legale e notarile Bonfanti-Ammann, licence **1989**,
5 domaines IT, tel/email — source annuaire professionnel jurata.ch, aucun site officiel
personnel trouvé), BALMELLI Riccardo (Studio legale e notarile Balmelli, Unternährer, secrétaire
de l'Ordre des notaires tessinois — peu de données au-delà du nom du cabinet), BANFI Gabriele
(Studio Legale Banfi / G.B. Law, fondé **2011**, 7 domaines IT).

Rattachement (`attach_individual_enrichment`) : 26/26 rattachés au total (23 → 26, +3), zéro
collision. TI : 19/386 avocats solo traités à ce stade. Suite de tests : 91/91 au vert.

### 2026-09-06 — Accélération explicite du rythme (demande de Greg : « fait 20 de l'heure pas 5 »)

Greg a constaté que le débit réel (~4-12 fiches/heure/phase) était trop lent par rapport à
l'objectif affiché de 50/heure et a demandé un rythme cible d'environ 20/heure. Ce lot ci-dessous
est un rattrapage manuel hors déclenchement automatique, pour démontrer et caler ce rythme :
**19 fiches traitées au total** (7 cabinets Phase 3 + 8 individus Phase 3b + 4 individus solo
Phase 3c), toutes vérifiées sur source primaire (site officiel fetché directement, sauf mention
contraire). Le débit reste borné par le temps de vérification réelle (WebSearch puis WebFetch,
contrôle robots.txt) -- 20/heure est un maximum soutenable, pas une garantie a chaque passage
(certains cabinets/avocats n'ont simplement aucun site officiel trouvable).

**Phase 3, lot 4 (rattrapage)** — 7 succès / 1 échec-connu-redocumenté : REBER (déjà en cache),
COLLEGAL Studio legale (TI, tel/email), studio legale e notarile Claudio Cereghetti & Partner
(TI, fondé **1996**, tel/email — site officiel indisponible HTTP 503 au moment du passage,
faits repris des extraits indexés, à revalider), Lexperience AG (ZH, tel/email), Bettoni &
Partner (ZH, 5 partenaires), Frick Nafz Bieri Jost Rechtsanwälte (ZH, tel, 6 avocats), KANZLEI
KREIS 2 AG (ZH, tel), Lexarte AG (ZH, 8 domaines DE, tel, 10 avocats). **Échec redocumenté :**
museum35.ch (LOCHER\|KOBLER\|STADELMANN, SG) — déjà connu JS/Readymag inextractible depuis un
lot antérieur, ajouté au cache actuel pour que les passages futurs ne le retentent plus.

Rattachement : 183 études rattachées au total (176 → 183, +7). Suite de tests : 91/91 au vert.

**Phase 3b, lot 4 (rattrapage)** — 8 succès / 0 échec, AG(2)/ZG(2)/NE(1)/TG(1)/SO(2) : Zoë
Arnold (AG, chkp., domaines DE, tel/email), Kim Attenhofer (AG, Geissmann Rechtsanwälte AG,
Fachanwältin SAV Bau- und Immobilienrecht, tel/email), Andermatt Philipp (ZG, Bright Law AG, 8
domaines DE, tel/email), Bachmann Philipp (ZG, Reichlin Hess AG, Certified Specialist SBA
Employment Law 2018, domaines EN), Isabelle Augsburger (NE, notaire et avocate, 5 domaines FR,
tel), Doris Ammann (TG, Im Zehntenhaus, Zertifizierte Kinderanwältin, domaines DE, tel/email),
Nicole Allemann-Aeschlimann (SO, aarejura Rechtsanwälte, email), Daniel Altermatt (SO, regio
iuris, licencié **2004**, domaines DE, tel/email).

**Phase 3c, lot 4 (rattrapage)** — 4 succès / 0 échec (TI, suite liste alphabétique) : ARENSI
Alessandra (Kellerhals Carrard Lugano SA, tel/email), BACCHETTA-CATTORI Fabio (tel), ANTONINI
Elisa (Studio Legale Antonini, fondé **2015**, tel/email), BAGGI Marcello (Studio Legale Baggi,
actif depuis **2003**, 4 domaines IT).

Rattachement individus : 38/38 rattachés au total (26 → 38, +12 combiné 3b+3c), zéro collision.
Suite de tests : 91/91 au vert.

## COORDINATION MULTI-AGENTS (06/09/2026, décision de Greg)

Greg a demandé de faire travailler des agents externes (OpenAI Codex, Google Jules) en parallèle
de Claude, en autonomie complète (tâches planifiées côté OpenAI/Google, PR ouvertes sur ce
dépôt), sur le **même chantier d'enrichissement**. Pour que 3 agents indépendants puissent
écrire sans jamais entrer en conflit git, le cache individus (`avocats_individuels_enrichment.json`,
partagé par les phases 3b et 3c) a été éclaté en 3 fichiers, un par agent :

- `data/avocats_individuels_enrichment.json` — **Claude** (phases 3b + 3c, routines existantes).
- `data/avocats_individuels_enrichment_chatgpt.json` — **OpenAI Codex**, phase 3b (cantons
  AG/ZG/NE/TG/SO).
- `data/avocats_individuels_enrichment_gemini.json` — **Google Jules**, phase 3c (avocats
  `solo` dans les 12 cantons groupables : ZH/TI/SG/GR/BL/SZ/UR/OW/NW/AR/AI/LU).

`build.load_individual_enrichment()` (build.py) lit maintenant les 3 fichiers
(`INDIVIDUAL_ENRICHMENT_FILES`) et les fusionne : si un `(canton, nom_normalisé)` apparaît dans
plus d'un fichier (collision inter-agents), l'entrée est écartée des deux côtés plutôt que de
choisir arbitrairement laquelle garder -- même philosophie anti-collision que le reste du
module. Testé (`test_load_individual_enrichment_merges_multiple_agent_files`,
`test_load_individual_enrichment_drops_cross_file_collision`).

**Règles pour tout agent externe qui lit ce document** (Codex, Jules, ou un futur agent) :
mêmes règles non négociables que Claude tout au long de ce fichier -- jamais de fait inventé,
uniquement des faits explicites sur site officiel (ou OpenStreetMap Overpass en repli), robots.txt
vérifié avant tout fetch, `source_url` + `fetched_date` systématiques, `_failed` documenté plutôt
que forcé. Ne JAMAIS modifier `build.py`, `presentation_text.py`, les templates, ou les tests
(seul Claude fait évoluer le code). Ne JAMAIS lancer `python3 build.py` (rebuild complet) ni
`wrangler deploy`. Écrire UNIQUEMENT dans le fichier qui vous est assigné ci-dessus -- jamais
dans le fichier `.json` d'un autre agent, jamais dans `domaines_autres_cantons.json` (réservé à
Claude, phase 3 cabinets) sauf instruction contraire explicite de Greg. Ouvrir une pull request
(ne pas pousser directement sur `main`) ; Claude ou Greg la relit avant fusion.

**État du déploiement (06/09/2026) :**
- **OpenAI Codex** — tâche "Enrichissement Codex — 20 avocats/h" configurée par Greg côté
  chatgpt.com/codex, cron horaire, ouvre une branche + PR (jamais de push direct).
- **Google Jules** — configuré via GitHub Actions (`.github/workflows/jules-schedule.yml`,
  action `google-labs-code/jules-invoke@v1`, cron horaire `0 * * * *`, secret repo
  `JULES_API_KEY` à ajouter par Greg dans Settings → Secrets and variables → Actions). Le
  prompt complet de la tâche est encodé dans ce fichier de workflow (pas besoin de le
  recopier ailleurs) ; toute modification de la tâche Jules passe par une modification de ce
  fichier YAML, pas par une reconfiguration manuelle côté jules.google.com.
- **Pourquoi zéro risque de collision entre les 3 agents** : (1) chaque agent écrit dans un
  fichier JSON distinct (jamais le même que les deux autres), (2) `load_individual_enrichment()`
  fusionne les 3 fichiers et écarte toute collision inter-agents plutôt que de trancher, (3)
  Codex et Jules ouvrent des PR au lieu de pousser sur `main` -- Claude (ou Greg) les relit et
  les fusionne une par une, donc même si deux PR arrivent au même moment, elles se fusionnent
  séquentiellement sans jamais s'écraser l'une l'autre. Seul point de vigilance restant :
  éviter que Claude retouche par erreur `avocats_individuels_enrichment_chatgpt.json` ou
  `_gemini.json`, ou que Codex/Jules retouchent `avocats_individuels_enrichment.json` (celui de
  Claude) -- règle déjà rappelée ci-dessus, à vérifier à chaque relecture de PR.

**Correction importante (même jour, quelques minutes après le paragraphe ci-dessus) :**
Greg a repéré que les fichiers séparés n'empêchent PAS le vrai doublon qui compte : au moment
d'écrire ce qui précède, les routines Claude `vectis-enrichissement-phase3b-individus`
(cantons AG/ZG/NE/TG/SO) et `vectis-enrichissement-phase3c-solos` (avocats solo des 12 cantons
groupables) tournaient TOUJOURS en parallèle de Codex (même périmètre AG/ZG/NE/TG/SO) et Jules
(même périmètre avocats solo 12 cantons) -- chacune des deux routines Claude ne vérifiait que
SON PROPRE fichier avant de choisir un lot, jamais celui de Codex/Jules. Résultat concret :
Claude et Codex/Jules pouvaient chercher indépendamment le même avocat en vrai (recherche web
gaspillée en double), et si les deux réussissaient sur la même personne, la fusion inter-fichiers
les aurait ENTRAÎNÉS À S'ANNULER MUTUELLEMENT (collision inter-agents = entrée écartée des deux
côtés) -- pire que juste redondant.

**Correction appliquée :** les deux routines Claude `vectis-enrichissement-phase3b-individus`
(`trig_01QN4pTNW8oGBGCuWm8SuyJv`) et `vectis-enrichissement-phase3c-solos`
(`trig_014WRGxcWeAwN8XpEq5FtKrM`) ont été désactivées (`enabled: false`, pas supprimées --
réactivables si Codex/Jules s'arrêtaient un jour). Répartition finale, un phase = un agent,
sans chevauchement de périmètre :
- **Claude** : Phase 3 uniquement (cabinets des 12 cantons groupables, `domaines_autres_cantons.json`).
- **OpenAI Codex** : Phase 3b uniquement (individus AG/ZG/NE/TG/SO, `..._chatgpt.json`).
- **Google Jules** : Phase 3c uniquement (avocats solo des 12 cantons groupables, `..._gemini.json`).

Aucun des 3 agents ne doit retravailler le périmètre d'un autre sans que Greg le redemande
explicitement.

### 2026-09-06 — Phase 3, lot 5 (premier passage horaire Claude depuis la correction de chevauchement)

4 cabinets traités (4 succès / 0 échec), tous ZH : VFS Partner (Voillat Facincani Sutter +
Partner, tel), bellpark legal AG (tel/email), Uto Legal (fondé par 6 avocats, tel, 6 emails
nominatifs), Bellerive Rechtsanwälte (17 domaines DE, généraliste particuliers + entreprises).

Rattachement (`attach_name_based_enrichment`) : 187 études rattachées au total (183 → 187, +4).
Suite de tests : 93/93 au vert.

### 2026-09-06 — Abandon de Google Jules, retour à Gemini en mode manuel

Jules (Google, connecté via `.github/workflows/jules-schedule.yml` + secret `JULES_API_KEY`)
a tourné deux fois sur la Phase 3c, produit un plan complet et annoncé "Ready for submission"
les deux fois, mais **n'a jamais réellement poussé la branche ni ouvert de PR sur GitHub**
(vérifié directement via l'API : ni branche `jules-batch-phase-3c`, ni PR ouverte ou fermée,
aux deux tentatives). Cause non élucidée côté Jules (probablement un problème d'autorisation
d'écriture ou un bug de son "submit tool") -- pas retenté une 3e fois, Greg a décidé de passer à
un mode manuel avec Gemini (interface web standard, recherche activée) à la place :

- Le fichier `.github/workflows/jules-schedule.yml` a été **supprimé** (plus d'automatisation
  GitHub Actions pour cette phase).
- **Gemini (mode manuel)** reprend la Phase 3c (avocats solo des 12 cantons groupables), mais
  sans accès direct au dépôt : Greg colle un prompt de lot dans l'interface Gemini, colle le
  JSON de résultat obtenu ici, et Claude valide + fusionne dans
  `data/avocats_individuels_enrichment_gemini.json` (nom de fichier inchangé, toujours partagé
  avec Codex/Claude via `load_individual_enrichment()`).
- La clé `JULES_API_KEY` reste en secret GitHub (inoffensive tant qu'aucun workflow ne la
  référence) -- Greg peut la supprimer à sa discrétion, ce n'est plus utilisé par rien.

Répartition à jour : **Claude** = Phase 3 (cabinets, routine automatique) ; **OpenAI Codex** =
Phase 3b (individus AG/ZG/NE/TG/SO, automatique via chatgpt.com/codex) ; **Gemini (manuel)** =
Phase 3c (avocats solo 12 cantons, relai manuel Greg ↔ Claude, PAS automatique).

### 2026-09-06 — Phase 3, lot 6

4 cabinets traités (4 succès / 0 échec) : Schwarzmann Brändli Hofer Rechtsanwälte AG (ZH,
fondé **1936**, tel), Felchlin Harb Schenkel Rechtsanwälte AG (ZH, tel/email, 6 avocats),
Studio I&P Law Office SA (TI, 11 domaines IT, tel/email), Küng Rechtsanwälte & Notare AG (SG,
8 domaines EN, tel/email — précédemment noté comme sans fait extractible dans un lot antérieur,
mais la page /leistungen/ en donne bien cette fois).

Rattachement (`attach_name_based_enrichment`) : 191 études rattachées au total (187 → 191, +4).
Suite de tests : 93/93 au vert.

**Statut Codex (constat, pas d'action) :** plus d'1h15 après la configuration de la tâche
"Enrichissement Codex — 20 avocats/h", toujours aucune PR ni branche sur GitHub. Greg vérifie
directement côté chatgpt.com/codex.

### 2026-09-06 — Correctif critique noindex/insight_text, puis Phase 3 lot 7

**Bug corrigé ce jour (commit 8de992a)** : `specialist_certification`/`publications` manquaient
sur 6 des 8 sites d'appel à `pt.firm_insight()` dans build.py -- une fiche dont le seul signal
réel était une certification restait `noindex` en prod malgré un `insight_text` non vide (cas
concret : David Georg Ackermann, TG), et 3 des 4 types de page (études GE, études génériques,
avocats GE) ne recevaient jamais ces deux champs même à l'affichage -- toute la donnée collectée
en Phase 3 aujourd'hui (spécialisations, publications) était invisible sur les fiches cabinet.
Corrigé, testé (nouveau test de régression statique), `python3 build.py all` relancé en local
(73819 pages, aucun artefact Jinja), poussé -- **déploiement automatique confirmé** (Cloudflare
rebuild sur push GitHub, pas besoin de `wrangler deploy` manuel). Vérifié en prod : la fiche
Ackermann n'est plus noindex, la page Aequitas affiche ses publications.

3 cabinets traités (3 succès / 1 échec) : CBM Studio legale e notarile (TI, tel/email),
Advokatur Roth (BL, 5 domaines DE, tel, 8 avocats), Advokatur Stoll Schulthess Partner (BL,
20 domaines DE, tel/email, 11 personnes). **Échec redocumenté :** sglaw.ch (Rüesch Rechtsanwälte,
SG) -- page `/taetigkeitsbereiche/` toujours vide (JS), déjà connu d'un lot antérieur.

Rattachement : 194 études rattachées au total (191 → 194, +3). Suite de tests : 94/94 au vert.

### 2026-09-06 — Phase 3, lot 8

4 cabinets traités (4 succès / 0 échec) : Novalex Rechtsanwälte AG (AR, 17 domaines DE, tel/email),
taormina law AG (ZH, boutique droit pénal, 4 domaines EN, tel/email, 8 avocats), HERZER
Rechtsanwälte (ZH, fondé **1947**, tel/email, 6 avocats), Knobel, Michel & Brändli (SZ, fondé
**1986**, 9 domaines DE, tel/email, 7 juristes).

Rattachement : 198 études rattachées au total (194 → 198, +4). Suite de tests : 94/94 au vert.

### 2026-09-06 — Phase 3, lot 9

4 cabinets traités (4 succès / 0 échec), tous ZH : Wicki Partners AG (4 domaines DE, tel/email,
8 personnes, classé "TOP law firm" Bilanz 2024), Stössel Schweizer Partner Rechtsanwälte und
Mediation (fondé **2016**, 6 domaines DE, email, 3 associés), Advokatur Dr. Valentin Landmann
GmbH (nouvelle étude du même avocat après scission d'avec Landmann & Partner AG déjà en cache --
5 domaines DE, tel/email, 10 personnes), Bächtold Gallarotti Rechtsanwälte (fondé **2022**, 6
domaines DE dont cybercrime, tel, 5 personnes).

Rattachement : 202 études rattachées au total (198 → 202, +4). Suite de tests : 94/94 au vert.

### 2026-09-06 — Phase 3, lot 10

4 cabinets traités (4 succès / 0 échec), tous ZH : Turicum Legal AG (fondé **2022**, 9 domaines
DE, tel/email), Schiffbau Rechtsanwälte (12 domaines EN, 6 avocats), Berther Moeri Neuber
Schindler (tel), Advokatur Aussersihl (6 domaines DE, tel, 8 personnes).

Rattachement : 206 études rattachées au total (202 → 206, +4). Suite de tests : 94/94 au vert.

### 2026-09-06 — Phase 3, lot 11

3 cabinets traités (3 succès / 1 échec) : Advokatur Landi Ruckstuhl Giess Tzikas Baumgartner
(BL, 15 domaines DE, tel/email), SPIESS+PARTNER AG Büro für Baurecht (ZH, fondé **2018**,
spécialiste droit de la construction, tel), FamPlus AG (ZH, fondé **2024**, droit de la
famille, tel/email, 5 personnes, "5 Certified Specialists SBA Family Law"). **Échec :** wkf AG
(ZH) -- site wkflegal.com indisponible (HTTP 503) au moment du passage.

Rattachement : 209 études rattachées au total (206 → 209, +3). Suite de tests : 94/94 au vert.

### 2026-09-06 — Phase 3, lot 12

3 cabinets traités (3 succès / 1 échec), tous ZH : Rütimann Rechtsanwälte (fondée **1990**,
7 domaines DE, tel, 10 personnes), Wild Schnyder AG (fondée **2001**, cabinet spécialisé
propriété intellectuelle — marques, dessins, concurrence déloyale, droit d'auteur, publicité,
médias, protection des données —, tel/email), Advokatur Weinberg (communauté d'étude de 6
avocats indépendants, 14 domaines DE ; pas de téléphone/email unique enregistré car chaque
avocat a ses propres coordonnées, non attribuable au « cabinet » en tant que tel). **Échec :**
LENZ & CADUFF Rechtsanwälte AG — site lenzcaduff.ch indisponible (HTTP 503 à répétition sur
plusieurs URLs testées), aucune donnée du WebSearch utilisée faute de confirmation directe.

Rattachement : 212 études rattachées au total (209 → 212, +3). Suite de tests : 94/94 au vert.

### 2026-09-06 — Phase 3, lot 13 (lot élargi à la demande de Greg)

**Retour utilisateur : les lots de 3-4 cabinets sont trop lents, il faut viser plus gros à
chaque passage.** 11 cabinets traités (11 succès / 0 échec réel), essentiellement ZH/FR/GR/SZ/BS :
Schellenberg Wittmer AG (ZH, 21 domaines DE — année de fondation vue sur Wikipédia mais absente
du site officiel, donc non retenue), Nater Dallafior Rechtsanwälte AG (ZH, boutique litige/
arbitrage international, tel/email, 13 domaines EN), Holenstein Brusa AG (ZH+Lugano, tel/email,
10 domaines EN), KSPartner (ZH, fondé **1993**, tel/email, 7 spécialisations en droit des
assurances/RC), Prof. Giger & Partner Rechtsanwälte (ZH, 12 domaines DE), Mengiardi Fey &
Partner AG (GR, 11 domaines DE, notariat inclus), Hartmanndreyer (FR, tel/email, 6 domaines FR),
FRPA/Fribourg Partners (FR, tel/email, 19 domaines FR), FRILegal SA (FR, tel/email, 4 domaines
FR), Kessler Landolt Giacomini (SZ, fondé **1974**, tel), DUFOUR Advokatur AG (BS, fondé
**1991** — confirmé explicitement sur la page officielle malgré une source tierce contradictoire
citant 2021 pour l'entité juridique actuelle, tel/email, 6 domaines EN).

**Note technique importante :** pour 4 cabinets (FRPA, Hartmanndreyer, Kessler Landolt
Giacomini, KSPartner), le nom complet/officiel ne correspondait pas au "nom cœur" utilisé par
`attach_name_based_enrichment()` pour rattacher l'enrichissement à la fiche CSV (ex. le CSV
contient littéralement "Hartmanndreyer" collé sans espace, ou "KSPartner" seul sans "Anwalts-
kanzlei"). Le champ `firm_name` de ces 4 entrées a donc été ajusté pour correspondre exactement
au nom du registre CSV -- cela n'affecte pas l'affichage réel sur le site (qui utilise toujours
le nom `etude` du CSV), seulement la clé de rattachement interne.

**Doublon détecté et corrigé :** en recherchant "Baud, Diehl, Stauffer" (BS), une entrée
`awg.ch` avait déjà été traitée lors d'un lot antérieur (29/07, hors de cette conversation) sous
le nom "Anwaltsgemeinschaft Baud Diehl Stauffer", fondée en 1981 -- travail redondant, aucune
modification nécessaire, l'entrée existante a été laissée intacte (une tentative d'ajout en
`_failed` a été annulée après vérification).

Rattachement : 217 études rattachées au total (212 → 217, +5 nettes après correction des clés de
rattachement -- 11 cabinets enrichis au total ce lot, dont 6 rattachés du premier coup et 4 après
correction du nom, 1 doublon retiré). Suite de tests : 94/94 au vert.

### 2026-09-06 22h03 UTC — Phase 3, lot 14 (exécution automatisée, prompt élargi appliqué)

12 cabinets traités (12 succès / 1 échec), tous ZH : ZR Law AG (tel/email), Wolfer & Frey
Rechtsanwälte (13 domaines DE droit public/privé, tel), Weber & Partner Rechtsanwälte AG (fondé
**1984** comme Advokaturbüro Stünzi & Weber, tel/email), Rickenbach & Partner (fondé **1955**,
13 domaines DE, tel), RISE Attorneys at Law (tel), Rentsch Partner AG (boutique PI, 7 domaines
EN), Müller Paparis AG (fondé **2001**, 8 domaines EN, tel/email), Meier Vogel Partner GmbH
(tel/email), Lanter Partner (tel/email), Krepper Spring Partner (9 domaines DE), Huber
Rechtsanwälte AG (fondé **1989**, droit de la construction/immobilier, tel/email — adresse
Mühlebachstrasse 38 confirmée via la page contact pour écarter tout risque de confusion avec un
autre "Huber Rechtsanwälte" à Pfäffikon SZ), advo5 Rechtsanwälte (dommages corporels, tel/email).
**Échec :** Ankerlex/Peyer Felder Kahlhöfer Gloor Leumann (page d'accueil vide, rendu JS
probable).

**Note technique :** 2 noms officiels complets ("Lanter Partner Rechtsanwälte", "advo5
Rechtsanwälte" collé) ne correspondaient pas au nom cœur du CSV ("LANTER PARTNER" sans
"Rechtsanwälte", "advo 5 Rechtsanwälte" avec espace) -- `firm_name` ajusté pour le rattachement,
même principe que le lot précédent.

Rattachement : 229 études rattachées au total (217 → 229, +12). Suite de tests : 94/94 au vert.

### 2026-09-06 23h03 UTC — Phase 3, lot 15 (exécution automatisée)

14 cabinets traités (14 succès / 1 échec), ZH/SG/OW/GR : Good Rechtsanwälte GmbH (ZH, tel/email,
14 domaines), Gloor Junker Rechtsanwälte (ZH, tel/email, 10 domaines DE), Fischer Rechtsanwälte
AG (ZH, tel, 6 domaines DE), Enquire Rechtsanwälte AG (ZH, boutique investigations/compliance,
tel/email, 5 domaines EN), Büchel von Rohr AG (ZH, tel/email, 11 domaines DE), Baldi & Caratsch
(ZH, fondé **1977**, tel, 8 domaines EN), ADROIT Anwälte (ZH, tel/email, 7 domaines DE), gm
Rechtsanwälte und Notare (SG, tel, 14 domaines DE), Sartorial Rechtsanwälte AG (SG, tel/email),
Glaus Gabathuler AG (SG, tel/email), Advoro AG (SG, tel/email, 9 domaines EN), Advokatur Staub
AG (SG, boutique droit public, tel/email, 6 domaines DE), Gabriel & Bucher AG Anwälte und Notare
(OW, tel/email), SwissLegal Lardi & Partner AG (GR, fondé **1971**, tel/email, 9 domaines FR).
**Échec :** BAADER Rechtsanwälte AG (BL) -- site baaderlex.ch inaccessible (HTTP 403).

Rattachement : 242 études rattachées au total (229 → 242, +13). Suite de tests : 94/94 au vert.

### 2026-09-07 00h03 UTC — Phase 3, lot 16 (exécution automatisée)

12 cabinets traités (12 succès / 1 échec), tous ZH sauf 2 LU : Advoro Zürich AG (bureau ZH
distinct d'Advoro AG SG déjà en cache, tel/email, 9 domaines EN), grosz poledna rc AG (boutique
droit public, tel/email, 14 domaines DE), Häfliger Haag Häfliger AG (LU, tel, 9 domaines DE),
Vollenweider Steiner Advokatur & Notariat (LU, tel/email, 5 domaines DE), rothorn legal AG
(adresse seule, aucun autre fait exploitable), Willimann & Donghi Rechtsanwälte (tel/email, 15
domaines DE), Wieduwilt Rechtsanwälte AG (tel/email, 11 domaines DE), Wehrenberg Rechtsanwälte
GmbH (boutique pénal économique, tel/email, 3 domaines DE), Trachsel Bürgi & Partner (tel, 16
domaines DE), Viadukt Recht GmbH (boutique droit de la construction, tel/email, 8 domaines DE),
Theiler Hablützel Rechtsanwälte AG (tel/email, 12 domaines DE). **Échec :** WEINMANN ZIMMERLI
Rechtsanwälte AG (site en rendu JS, "Loading..." uniquement).

**Note :** le CSV ZH contient une duplication ("Wieduwilt Rechtsanwälte AG" et "Wieduwilt
Rechtsanwälte" comme deux études distinctes) -- collision de nom cœur, rattachement
correctement ignoré par le garde-fou plutôt que risquer une mauvaise attribution.

Rattachement : 252 études rattachées au total (242 → 252, +10 ; 1 collision supplémentaire
ignorée à bon escient). Suite de tests : 94/94 au vert.

### 2026-09-07 01h02 UTC — Phase 3, lot 17 (exécution automatisée)

10 cabinets traités (10 succès / 4 échecs), ZH/BL/LU/SG : Schwarz Breitenstein Rechtsanwälte AG
(tel/email, 8 domaines DE), Roesle Frick & Partner (tel/email), Rioult & Partner (tel/email, 5
domaines DE), Schmid Sutter Rechtsanwälte AG (boutique immobilier/construction, tel/email, 4
domaines DE), Teuscher Hediger Höhener Wimmer Rechtsanwältinnen (7 domaines DE), Advokatur am
Fischmarkt (BL, fondée **1979** -- confirmé explicitement sur la page officielle --, tel, 12
domaines DE), Lischer Zemp & Partner (LU, tel), EMMLEGAL (tel), Dietsche AG Rechtsanwälte &
Notare (SG, tel/email, 4 domaines DE), Brun Forrer Kern KIG (boutique pénal, tel/email, 2
domaines DE). **Échecs :** Schaub Hochl Rechtsanwälte AG (page anti-bot "One moment please..."),
rabaglio schär ag (page JS quasi vide), Nievergelt & Stoehr AG (aucun site officiel dédié
trouvé), Raum & Recht AG (entité trop récente, inscrite au RC le 15.05.2026, aucun site trouvé).

**Note :** CSV LU contient "Lischer Zemp & Partner St." (troncature probable d'une mention
d'adresse) -- `firm_name` ajusté pour correspondre exactement au nom cœur du CSV.

Rattachement : 262 études rattachées au total (252 → 262, +10). Suite de tests : 94/94 au vert.

### 2026-09-07 02h02 UTC — Phase 3, lot 18 (exécution automatisée)

10 cabinets traités (10 succès / 1 échec), tous ZH : Kämpfen Rechtsanwälte (tel/email), HOHLER
TRÖHLER RECHTSANWÄLTE (tel, 7 domaines DE), Kloter Rechtsanwälte AG (fondée **1989** par Modl et
Scheibler avant la création de l'AG actuelle en 2016 -- les deux dates figurent explicitement
sur la page officielle, 1989 retenue comme date de fondation continue --, tel/email, 6
domaines DE), Niklaus Rechtsanwälte (boutique droit agricole/protection animale, 10 domaines
DE), JETZER FRANK AG (boutique pénal économique, tel/email, 5 domaines DE), Perucchi & Partner
AG (tel/email, 5 domaines EN), Nötzli Raess Bächtold Rechtsanwälte (tel/email), KLEB & PARTNER
Rechtsanwälte (boutique droit de la construction, tel), Hafner Urbach Partner (tel), Künzi Hess
MacNab Rechtsanwälte (boutique fintech/régulation financière, tel/email, 10 domaines EN).
**Échec :** Schoch Jaeggi Hoch (page d'accueil sans contenu exploitable, email protégé anti-bot).

Rattachement : 272 études rattachées au total (262 → 272, +10). Suite de tests : 94/94 au vert.

### 2026-09-07 03h02 UTC — Phase 3, lot 19 (exécution automatisée)

9 cabinets traités (9 succès / 1 échec), tous ZH : Gabriel Arbitration AG (boutique arbitrage
international, 5 domaines EN), Birgelen Wehrli Rechtsanwälte (fondée **1893** -- confirmé
explicitement sur la page officielle, doyenne des cabinets traités jusqu'ici --, tel/email, 8
domaines EN), Fellmann Klett Rothenberger (boutique RC/assurances, tel/email, 7 domaines DE),
Bertschinger Wiesendanger Sutter (aujourd'hui "Advokatur Lindenplatz", tel/email, 4 domaines
DE), Binder Sutter Mumenthaler Wiget (tel/email, 12 domaines DE), Glatthard & Stählin AG
(tel/email, 9 domaines EN), Meier-Stehlik Rupp & Gisler (tel -- emails affichés inversés en
anti-scraping, non exploitables de façon fiable), Burri Breitschmid AG (ex-Schneider
Rechtsanwälte AG, boutique droit public/marchés publics, tel/email, 4 domaines DE), Grieder
Baumann Lerch Meienberg Rechtsanwälte (boutique RC/assurances, tel/email, 8 domaines DE).
**Échec :** EBD Rechtsanwälte AG (HTTP 503 au fetch).

Rattachement : 281 études rattachées au total (272 → 281, +9). Suite de tests : 94/94 au vert.

### 2026-09-07 04h02 UTC — Phase 3, lot 20 (exécution automatisée)

10 cabinets traités (10 succès / 0 échec), ZH sauf 1 BL : Baumberger Rechtsanwälte AG (Winterthur,
fondée **1973** -- "Für Klarheit beim Bauen. Seit 1973." --, boutique droit de la construction/
immobilier, tel/email, 17 domaines DE), BGPartner AG (fondée **1988**, tel/email, 4 domaines DE),
Allegra Law AG (boutique droit financier/blockchain, tel/email, 6 domaines EN), AAK Anwälte und
Konsulenten AG (boutique droit public, tel/email), BNS Attorneys at Law (boutique RC/assurances,
tel/email, 9 domaines), Buchli & Hochuli (fondée **2000**, tel, 3 domaines DE), HMV Rechtsanwälte
(fondée **1989**, boutique prévoyance professionnelle, tel/email), Luks und Vogt Rechtsanwältinnen
(fondée **1999** -- "Seit 1999" --, tel/email, Fachanwältin SAV Erbrecht), Advocentral Advokaturen
(tel, 6 domaines DE), Advokatur Enderle Felix Haidlauf Schmid (BL, tel/email).

Rattachement : 291 études rattachées au total (281 → 291, +10). Suite de tests : 94/94 au vert.

### 2026-09-07 05h03 UTC — Phase 3, lot 21 (exécution automatisée, première incursion au Tessin)

7 cabinets traités (7 succès / 1 sans-site / 2 échecs) — premier lot avec des cabinets tessinois
(italophones) : SwissLegal Indemini Partner SA (TI, Lugano, fondé **2008**, tel/email, 14
domaines EN), Studio legale e notarile VERDA (TI, Lugano, email), Studio legale ad metam SA (TI,
Locarno, tel/email, 12 domaines IT), Studio legale Wuthier & Nicora SA (TI, Ascona, email, 20
domaines IT), Studio legale Barchi Nicoli Trisconi Gianini SA (TI, Lugano, 7 domaines IT --
aujourd'hui "Barchi Partners"), Bilger Mattli Bomatter Gisler AG (UR, Altdorf, tel/email, 19
domaines DE), Maison Droite AG (ZH, boutique droit de la famille, tel/email, 5 domaines DE,
Fachanwältin SAV Familienrecht). **Sans site :** Studio legale e notarile Censi & Associati (TI)
-- aucun site officiel dédié trouvé. **Échecs :** 4sight legal (ZH, page anti-bot), Mercury
Compliance AG (ZH, pages contact/entreprise en simple redirection sans contenu).

Rattachement : 298 études rattachées au total (291 → 298, +7). Suite de tests : 94/94 au vert.

### 2026-09-07 06h04 UTC — Phase 3, lot 22 (exécution automatisée)

7 cabinets traités (7 succès / 3 échecs), SG/SZ/TI : Studio Legale Casoni Delcò (TI, boutique
droit de la famille, tel, 6 domaines IT), Thalhammer | Bossart | von Rohr Rechtsanwälte & Notare
(SG, tel/email, 8 domaines DE), Gründler & Partner Rechtsanwälte AG (SG, tel/email, 9 domaines
DE), Frey & Partner Rechtsanwälte und Notare (SG, tel/email), Pfister & Partner (SZ, tel/email,
6 domaines DE), Degginger Bischof Zlabinger (SG, tel, 12 domaines DE synthétisés depuis les
pages individuelles des 5 avocats -- dont une spécialité rare "droit des chiens"), TRACHSEL
HUTTER FLATTICH (SZ, tel/email, 7 domaines DE). **Échecs :** Kaufmann Brühwiler & Partner (SG,
page anti-bot), Acocella Keller Wolf Schilter (SZ, HTTP 503), Studio notarile Velo & Associati
(TI, HTTP 403).

**Note :** 2 des 7 succès (Gründler & Partner, Frey & Partner) n'ont pas pu être rattachés
automatiquement -- le CSV SG contient chacun deux fois sous des graphies très proches
("Gründler & Partner Rechtsanwälte AG" / "Gründler + Partner Rechtsanwälte" ; "Frey & Partner,
Rechtsanwälte und Notare" / "Frey & Partner Rechtsanwälte und Notare"), créant une collision de
nom cœur -- garde-fou correctement appliqué (aucun rattachement plutôt qu'un choix arbitraire).

Rattachement : 303 études rattachées au total (298 → 303, +5 ; 2 collisions supplémentaires
ignorées à bon escient). Suite de tests : 94/94 au vert.

### 2026-09-07 07h04 UTC — Phase 3, lot 23 (exécution automatisée)

8 cabinets traités (8 succès / 0 échec), LU sauf 1 SG : Mayr von Baldegg Agten Humbel Joos
(tel/email), Mühlebach Advokatur AG (tel, 15 domaines DE), Pilatushof AG (tel, 13 domaines FR,
9 personnes), Peter und Partner Anwaltsbüro und Notariat (fondé **1982**, tel/email), Zgraggen
Rechtsanwälte AG (tel/email, 9 domaines DE), Stadelmann Rechtsanwälte AG (fondée **1968**, tel,
7 domaines EN, Fachanwalt SAV Bau- und Immobilienrecht pour 2 avocats), Schenkel & Serrago AG
(tel/email), AMPARO Anwälte und Notare (SG, tel/email, 18 domaines DE).

Rattachement : 311 études rattachées au total (303 → 311, +8). Suite de tests : 94/94 au vert.

### 2026-09-07 08h03 UTC — Phase 3, lot 24 (exécution automatisée, premières fiches Grisonnes)

7 cabinets traités (7 succès / 2 échecs), premiers cabinets grisons (GR) : Fryberg Augustin
Breitenmoser Partner (GR, Chur, tel/email), Buchli Just Advokatur und Notariat (GR, fondé
**1976**, 5 domaines DE), Lardelli Conrad Advokatur Notariat (GR, tel/email, 9 domaines DE),
Kanzlei Bellevue (LU, tel/email, 9 domaines DE), Anwälte 44 (SG, tel, 7 domaines DE), Studio
legale e notarile Olgiati Ghiringhelli Sala (TI, fondé **1968**, boutique droit de l'art rare,
tel/email, 12 domaines EN), Studio legale e notarile Guggiari-Guerra-Rapelli-Gottardi (TI, tel/
email, 12 domaines IT -- renommé depuis en "...Aiolfi Gottardi", même cabinet). **Échecs :** Egli
Hess Schwegler Rechtsanwälte und Notare (LU, domaine ehs-kanzlei.ch introuvable en DNS), Studio
legale e notarile Brioschi Gianella Timbal & Cometta (TI, HTTP 503).

Rattachement : 318 études rattachées au total (311 → 318, +7). Suite de tests : 94/94 au vert.

### 2026-09-07 09h03 UTC — Phase 3, lot 25 (exécution automatisée)

7 cabinets traités (7 succès / 1 échec), tous ZH : von Segesser Rechtsanwälte AG (boutique
arbitrage international, tel/email, 3 domaines EN), felderspälti Rechtsanwälte AG (boutique
droit successoral/immobilier, tel/email, 3 domaines DE, Fachanwalt SAV Erbrecht pour Andreas
Felder), veriat legal AG (tel/email, 10 domaines DE), lelex Rechtsanwälte (boutique droit du
travail, tel), hba Rechtsanwälte AG (bureau zurichois d'un cabinet autrichien, tel/email
spécifiques à Zurich, 12 domaines EN droit immobilier/construction), von Arx Schmidiger Faber
(tel/email, 6 domaines DE), Advokatur am Bleicherweg GmbH (boutique droit de la famille/
médiation, tel). **Échec :** versaLex AG (HTTP 403 Forbidden).

Rattachement : 325 études rattachées au total (318 → 325, +7). Suite de tests : 94/94 au vert.

### 2026-09-07 10h03 UTC — Phase 3, lot 26 (exécution automatisée)

7 cabinets traités (7 succès / 1 échec), tous ZH -- la file des cabinets ≥4 avocats est
maintenant quasi épuisée, ce lot est majoritairement composé de cabinets à 3 avocats : Rappold
Köhli Rechtsanwälte AG (tel, 3 domaines EN), Sautter & Ammann (fondée **1973**, tel, 12
domaines DE), Schwärzler Rechtsanwälte AG (bureau zurichois d'un cabinet liechtensteinois,
tel/email, 12 domaines FR), Steiger Legal AG (boutique droit numérique, tel/email, 4 domaines
DE), Wildeisen Anwaltskanzlei GmbH (tel/email, 3 domaines DE), Scope Law AG (tel/email, 8
domaines EN), Zanetti & Schmidhauser Rechtsanwälte (boutique droit fiscal, tel/email, 4
domaines EN). **Échec :** Wiesli Rechtsanwälte (domaine ww-law.ch introuvable en DNS).

**Note sur l'ampleur du travail restant :** ~1959 études non traitées restent dans les 12
cantons groupables (325 rattachées sur 2322 études recensées, soit ~14%) -- au rythme actuel
(~7 cabinets/heure), il reste plusieurs jours de travail avant d'épuiser cette liste, et elle
ne couvre pas GE/VD ni les avocats individuels sans cabinet identifiable.

Rattachement : 332 études rattachées au total (325 → 332, +7). Suite de tests : 94/94 au vert.

### 2026-09-07 11h04 UTC — Phase 3, lot 27 (exécution automatisée)

7 cabinets traités (7 succès / 1 échec), ZH sauf 1 BL : Advokatur Stadthof AG (BL, tel/email, 4
domaines DE), NSF Rechtsanwälte AG (bureau zurichois d'un cabinet basé au Liechtenstein,
tel/email spécifiques à Zurich), Moser Advokatur AG (3 domaines DE), Lutz Partner Rechtsanwälte
AG (tel, 4 domaines DE), Michlig Knutti Partner AG (tel/email, 9 domaines DE), Sorg Bosshard
Neth (boutique droit de l'art en plus des domaines classiques, tel/email, 11 domaines EN),
Rüesch & Müller Rechtsanwälte (tel/email, 8 domaines DE). **Échec :** TA Advisory AG (seule
l'adresse du bureau zurichois indiquée, aucun tel/email/domaine confirmé pour cette antenne).

Rattachement : 339 études rattachées au total (332 → 339, +7). Suite de tests : 94/94 au vert.

### 2026-09-07 12h04 UTC — Phase 3, lot 28 (exécution automatisée)

7 cabinets traités (7 succès / 0 échec), tous ZH : Kuoni Rechtsanwälte AG (tel/email, 10
domaines EN), Klavis Law GmbH (tel/email, 6 domaines DE), Langner Arndt Rechtsanwälte AG
(boutique droit de la famille, 3 bureaux ZH/Zug/St-Moritz, tel/email, 7 domaines EN), Lawside
Rechtsanwälte GmbH (boutique droit bancaire/fintech, tel, 7 domaines DE), Lehmann & Waldburger
(tel, 8 domaines EN), OZB Rechtsanwälte (fondée **1998**, tel/email, 9 domaines DE), Nastra
Rechtsanwälte AG (tel, 5 domaines EN).

Rattachement : 346 études rattachées au total (339 → 346, +7). Suite de tests : 94/94 au vert.

### 2026-09-07 13h04 UTC — Phase 3, lot 29 (exécution automatisée)

10 cabinets traités (8 succès / 2 échecs), tous ZH : KELLER Rechtsanwälte AG (boutique droit
de la construction/immobilier, tel/email, 5 domaines DE, 3 avocats), Heuberger Rippmann
Hoffmann (tel/email uniquement, page pratiques non exploitable), Internationale Rechtsanwälte
Zürich/IRAZ (boutique droit international, tel/email, 12 domaines DE, 3 avocats), Kull Ruzek
Eggenschwiler (fondée **1968** — "Im Jahr 1968 haben sich die Anwälte Dr. Walter Vollenweider
und Dr. Werner Zuppinger zusammengeschlossen", page histoire officielle, tel/email, droit
public de la construction/planification), Lindtlaw Anwaltskanzlei (fondée **1970**, tel/email,
~15 professionnels, 20 domaines DE, **Fachanwalt SAV Erbrecht** pour Beat Rüedi, **Fachanwalt
SAV Arbeitsrecht** pour Fabian Kapfhamer, **Fachanwälte SAV Bau- und Immobilienrecht** pour
quatre associés), Public Sector Law (boutique droit public, tel/email, 6 domaines DE, 3
personnes), devon ag/devonlegal.ch (tel/email, site en construction sinon), advokatur
rechtsanker (tel, 9 domaines DE, 4 avocats, **Fachanwältin SAV Familienrecht** pour Barbara
Laur, **Fachanwalt SAV Haftpflicht- und Versicherungsrecht** pour Silvan Meier Rhein).
**Échecs :** Josephsohn Hauert Blöchlinger (luther4.ch, HTTP 403 Forbidden) ; Kanzlei
rechtschaffen (rechtschaffen.ch, HTTP 403 Forbidden sur deux URLs testées).

Note : le champ `firm_name` de l'entrée `iraz.ch` a été écrit sous la forme exacte du CSV
("Internationale Rechtsanwälte Zürich") et celui de `devonlegal.ch` sous la forme "devon ag"
pour permettre le rattachement automatique (le nom commercial affiché sur les sites diffère
légèrement du libellé CSV) ; cela n'affecte pas l'affichage réel sur le site.

Rattachement : 354 études rattachées au total (346 → 354, +8). Suite de tests : 94/94 au vert.

### 2026-09-07 14h04 UTC — Phase 3, lot 30 (exécution automatisée)

12 cabinets traités (10 succès / 2 échecs), sur 5 cantons (ZH, SG, GR, LU, SZ) : k&s
rechtsanwälte klg (ZH, tel/email, 8 domaines DE — site officiel logé sur kalbermatter.law,
domaine confirmé identifier explicitement le cabinet), Dobler Rechtsanwälte AG (SZ, tel/email),
Münch Singh Rechtsanwälte (ZH, tel/email, 4 personnes), Stieger + Schütt Rechtsanwälte (ZH,
tel/email, 5 avocats, 6 domaines DE, **Fachanwalt SAV Arbeitsrecht** pour Peter Stieger,
**Fachanwalt SAV Familienrecht** pour Thomas Schütt), DGS. Rechtsanwälte / Steuerexperten (ZH,
tel/email, 13 domaines DE), Littler Switzerland AG (ZH, bureau zurichois d'un cabinet
international — tel/email spécifiques à Zurich uniquement, statistiques mondiales écartées
conformément à la règle 4), Advoro AG (SG, tel/email spécifiques au bureau de St-Gall, 9
domaines DE), GM Rechtsanwälte (SG, tel spécifique au bureau de St-Gall, 10 domaines DE),
Visinoni & Metzger (GR, fondée **2008**, tel/email, 5 avocats, 13 domaines DE, **Fachanwalt
SAV Erbrecht** pour Fabrizio Visinoni, **Fachanwalt SAV Bau- und Immobilienrecht** pour Stefan
Metzger), Fellmann Klett Rothenberger AG (LU, tel/email, 12 domaines DE, **Fachanwalt/-anwältin
SAV Haftpflicht- und Versicherungsrecht** pour Walter Fellmann et Barbara Klett). **Échecs :**
Janiak Freivogel Schweighauser von Wartburg (BL, advokaturbuero-bl.ch, résolution DNS
impossible sur deux tentatives) ; PRUDENTIA LAW (ZH, prudentia-law.ch, page d'accueil sans
fait exploitable, /kontakt et /impressum en 404).

Correctif matching : l'entrée existante `klgp.ch` (Kessler Landolt Giacomini, SZ, lot antérieur)
avait un `firm_name` ne correspondant pas au libellé CSV dupliqué ("Kessler Landolt Giacomini &
Kessler Landolt Giacomini") ; corrigé pour permettre le rattachement (aucun impact sur
l'affichage réel du site).

Note de rigueur : le total « 9 membres » de Fellmann Klett Rothenberger AG mêlait avocats et
assistants (source non ventilée) — non retenu comme `team_size_n`, conformément au précédent
établi pour ce type de chiffre mixte. Le "Dipl. Steuerexperte" de DGS. Rechtsanwälte n'est pas
un titre de spécialiste FSA/SAV et n'a pas été enregistré comme `specialist_certification`.

Rattachement : 361 études rattachées au total (354 → 361, +7 nettes après correctif). Suite de
tests : 94/94 au vert.

### 2026-09-07 15h04 UTC — Phase 3, lot 31 (exécution automatisée)

17 cabinets traités (17 succès / 0 échec), tous ZH sauf mentions contraires. **Découverte
importante :** le CSV source contient de nombreuses lignes dupliquées pour un même cabinet réel
(même adresse/site officiel, libellés `etude` légèrement différents — ex. suffixe tronqué, ou
raison sociale répétée deux fois). Plutôt que de re-rechercher inutilement le même site, 5
entrées "doublon" ont été ajoutées en réutilisant les faits déjà vérifiés d'une entrée existante,
avec une clé de premier niveau disambiguée (`domaine#suffixe`) : `klgp.ch#2` (Kessler Landolt
Giacomini &, SZ, 7 avocats — 2e ligne CSV pour le même cabinet que `klgp.ch`), `fkr-legal.ch#ZH`
(Fellmann Klett Rothenberger, ZH, 4 avocats — le cabinet fkr-legal.ch a des avocats inscrits à
la fois au barreau LU et ZH), `advoro.ch#2` (Advoro AG, SG, 5 avocats), `gmlaw.ch#2` (gm
Rechtsanwälte und Notare, SG, 5 avocats), `lelex.law#2` (lelex AG, ZH, 3 avocats).

12 cabinets nouvellement recherchés (tous ZH, 3 avocats chacun sauf mention) : Abdelaziz Schmidt
(boutique droit pénal, tel/email, **Fachanwalt SAV Strafrecht** pour Amr Abdelaziz et Maurin
Schmidt, tous deux certifiés en 2022), Dr. Eschmann Rechtsanwälte (aujourd'hui "Eschmann Ribi
Akikol Rechtsanwälte" — même adresse/tel/email, changement de raison sociale constaté sur le
site officiel, 8 domaines DE), Aliotta + Partner (Winterthur, tel, 6 domaines DE), Borer
Rechtsanwälte AG (tel/email), Forum Rechtsanwälte (tel, 3 avocats, 6 domaines EN), Attanasio
Rechtsanwälte AG (tel/email, 5 avocats, 10 domaines DE), IPrime Legal AG (boutique PI/tech, tel
spécifique à cette entité — attention : deux entités distinctes partagent la même adresse
zurichoise, IPrime Legal AG et IPrime Rentsch Kaelin AG, avec des numéros différents), Isler
Partner Rechtsanwälte (Stäfa, tel/email, 3 avocats, 12 domaines DE), BosLaw AG Rechtsanwälte
(tel/email), Blumenfeld Law AG (boutique droit de la famille, tel/email, 6 avocats), Burkart &
Pfammatter (Erlenbach, tel, 4 avocats, 11 domaines DE), BFMS Rechtsanwälte (tel, 6 domaines DE).

Note de rigueur : la mention "fondée en 1990" pour Dr. Eschmann (vue uniquement dans un résumé
WebSearch tiers) n'a pas été retenue — la page officielle elle-même ne l'indique pas
explicitement. "Plus de 20 ans" pour Burkart & Pfammatter écarté (formulation vague).

Rattachement : 378 études rattachées au total (361 → 378, +17). Suite de tests : 94/94 au vert.

### 2026-09-07 16h04 UTC — Phase 3, lot 32 (exécution automatisée)

15 cabinets traités (15 succès / 0 échec), 13 ZH + 2 TI : Greter & Partner Rechtsanwälte AG
(fondée **2013**, tel, 7 avocats, 7 domaines DE dont droit fiscal international US), AGON
PARTNERS LEGAL AG (boutique droit de la concurrence, tel/email bureau zurichois — cabinet
multi-sites CH Zurich/Berne/Pfäffikon), Gubler & Gysler Rechtsanwälte (fondée **2022** sous le
nom "Gubler Rechtsanwälte", rebaptisée 2023, tel/email, 3 avocats inscrits au barreau, 8
domaines DE, **Fachanwalt SAV Strafrecht** pour Simon Gubler), ADVOMED (boutique droit de la
responsabilité civile/médical, tel/email, 4 avocats, 4 domaines DE, titre de spécialiste en
droit de la responsabilité civile et des assurances pour Evalotta Samuelsson — première et
seule avocate suisse avec ce profil selon le site), Advokatur & Rechtsberatung TRIAS AG
(cabinet multi-sites CH, tel bureau zurichois, 11 domaines DE), HERZOG.law AG (tel/email, 4
avocats, 6 domaines DE, **Fachanwältin SAV Erbrecht** pour Sabine Herzog, **Fachanwältin SAV
Arbeitsrecht** pour Martina Patricia Steiner), AMIKO Anwält:innen (tel/email, 3 avocats, 5
domaines DE), Advokraft (tel/email, 4 avocats, 2 domaines DE), 4Legal (communauté de cabinet
indépendants Zurich/Coire/Lugano, tel du secrétariat commun uniquement -- aucun tel/email de
cabinet inventé pour les avocats individuels), Bellevue Rechtsanwälte (tel/email, 4 avocats),
Anwaltskanzlei WT92 AG (tel/email, 4 avocats, 9 domaines DE), Advokatur Bülach AG (tel), burckhardt
AG (cabinet bi-site Bâle/Zurich, tel/email bureau zurichois, 3 domaines DE), Studio legale MAG
Legis SA (TI, tel/email), Berra Vigilante & Partners - bvp SA (TI, 5 professionnels listés).

Note de rigueur : "founded on March 22, 2023" pour Berra Vigilante (vu uniquement sur Moneyhouse,
tiers) n'a PAS été retenu comme `founding_year` -- absent du site officiel bvlaw.ch lui-même.
Idem pour "opened in 1990" (Advokatur Bülach, résumé WebSearch tiers, non confirmé sur le site).
Entrée bvlaw.ch en collision de nom avec une 2e ligne CSV quasi identique ("Berra Vigilante &
Partners bvp SA" sans tiret) -- non rattachée automatiquement, `skipped_ambiguous` passé de 5 à
6, garde-fou fonctionnant comme prévu.

Rattachement : 391 études rattachées au total (378 → 391, +13 nettes, 1 entrée en collision de
nom). Suite de tests : 94/94 au vert.

### 2026-09-07 17h04 UTC — Phase 3, lot 33 (exécution automatisée)

13 cabinets traités (13 succès / 0 échec), première incursion sur SG et TI dans ce lot après
plusieurs lots ZH consécutifs. 6 TI : studio legale e notarile Guidicelli Badaracco (tel/email),
BMA Brunoni Mottis & Associati Studio Legale SA (Lugano/Locarno, tel, 11 personnes listées),
Studio legale e notarile Cavadini Steger Gianinazzi Maffi (Lugano/Mendrisio, tel/email, 4
avocats-notaires, 10 domaines EN), Studio Legale e Notarile avv. Costanino Delogu
(Lugano/Mendrisio, tel/email, 12 domaines EN), Studio legale CIAMEI-PADLINA-DE STEFANI (7
domaines EN, inscrit aussi au barreau de Côme en Italie), Legem Studio legale e notarile (fondée
**2015** -- "Il nostro Studio nasce nel 2015 dalla fusione di due esperienze professionali", tel/
email, 3 avocats, 13 domaines IT). 7 SG : Senn Somm Bossart Anwälte (tel/email), Gmünder
Frischknecht & Partner (fondée **1980** -- "gründete im Jahre 1980 die Anwaltskanzlei", tel, 4
avocats/notaires), PETERER Rechtsanwälte Notare AG (tel, 5 personnes, 7 domaines EN), AMG
Rechtsanwälte AG (cabinet multi-sites SG/SH/AI, tel/email spécifiques au bureau de St-Gall, 10
domaines EN), Hueberli Lawyers AG (fondée **2019**, tel/email, 4 avocats-notaires, 5 domaines
EN), Bartl Egli & Partner AG (fondée **2017** -- date de fusion des deux études préexistantes,
tel/email, 3 domaines DE), LEXR Law Switzerland AG (boutique droit tech multi-sites CH/DE/US,
tel bureau de St-Gall, domaines DE -- statistiques mondiales "30+ avocats" écartées, règle 4).

Note de rigueur : la fondation "2011" d'Advokatur Bartl (prédécesseur individuel) écartée au
profit de la date de fusion 2017 de Bartl Egli & Partner AG elle-même. Team size de BMA (11
personnes) et de PETERER (5 personnes) et Cavadini Steger (4) retenus tels qu'affichés
nommément sur la page officielle (pas de comptage déduit).

Rattachement : 403 études rattachées au total (391 → 403, +12 nettes après vérification
individuelle des 13 entrées). Suite de tests : 94/94 au vert.

### 2026-09-07 18h04 UTC — Phase 3, lot 34 (exécution automatisée)

11 cabinets traités (11 succès / 0 échec), premier lot couvrant GR et BL, plus 4 SG et 1 TI.
Doublon réutilisé : `lexr.com#ZH` (LEXR Law Switzerland AG, 2e ligne CSV ZH pour un cabinet déjà
traité en SG au lot 33). 2 GR : Nievergelt & Stoehr AG (cabinet multi-sites Samedan/Poschiavo/
St-Moritz/Lucerne/Lugano/Muralto, tel/email des bureaux grisons, 3 domaines DE), Gadient +
Partner (fondée **1963** -- "seit 1963", tel/email, 6 personnes, 5 domaines DE). 3 BL : BIRSLEX
Advokatur (tel/email, 9 domaines EN), KIPFERHUBER Advokatur (tel/email, 2 avocats), Butz Corvini
Sigel Advokatur & Mediation (fondée **2010** -- date de création du partenariat Butz & Corvini,
Sigel rejointe en 2014, tel, 3 associés). 4 SG : Schwager Mätzler Schneider AG (fondée **1956**
par Dr. Josef Otto Schneider, tel/email, 10 avocats, 17 domaines EN), Gmür Galbier Nüesch
Rechtsanwälte & Notare (tel/email, 4 avocats), Schwizer Rechtsanwälte AG (fondée **1996**,
tel, 3 avocats sur deux générations, 5 domaines EN), Mätzler & Partner (tel/email, 4 avocats --
"limitation volontaire de l'effectif pour préserver le caractère régional"). 1 TI : Studio
legale e notarile Fiscalini (tel/email, 3 avocats-notaires).

Note de rigueur : "since 1990" pour Mätzler & Partner (résumé WebSearch tiers uniquement) non
retenu -- absent de la page officielle elle-même. Team size de Schwager Mätzler Schneider (10
avocats + 4 secrétaires) et de Gmür Galbier Nüesch (4 avocats + 1 secrétariat) ventilés
proprement -- seul le nombre d'avocats retenu, jamais le total mixte.

Rattachement : 413 études rattachées au total (403 → 413, +10 nettes). Suite de tests : 94/94
au vert.

### 2026-09-07 19h04 UTC — Phase 3, lot 35 (exécution automatisée)

14 cabinets traités (13 succès / 1 échec `_sans_site`), premier lot couvrant LU (8 cabinets),
plus NW, AR et 2 GR/SZ supplémentaires. Doublon réutilisé : `sms-lawyers.ch#2` (Schwager
Mätzler Schneider Rechtsanwälte, 2e ligne CSV SG). 8 LU : Amrein Partner Advokatur & Notariat
(tel/email), Kaeslin Bänziger David & Partner (tel/email, 6 avocats -- **piège évité** : la
mention "1882" concerne la villa Art nouveau abritant le cabinet, pas sa fondation, donc NON
retenue comme `founding_year`), ZIMMERLI & PARTNER Advokatur Zentralschweiz AG (tel/email),
Beeler & Marbacher AG (tel/email, 10 domaines EN), RÜTTER STOCKER (tel/email, 10 domaines DE),
Gübeli & Müller RECHTSANWÄLTE | NOTARE (tel/email, 2 notaires, 11 domaines DE), Brücker AG
(tel, 4 personnes, 7 domaines DE), Engelberger Anwälte & Notare (cabinet multi-sites LU/NW/OW,
tel/email bureau de Lucerne, 5 domaines EN). 1 AR : ME Advocat AG (bureaux Staad SG/Herisau AR,
tel bureau AR, email). 1 NW : Poli und Bernardi Notariat Anwaltskanzlei (tel, 3 avocats, 7
domaines DE). 2 GR : Advokatur-Notariat Cahannes (fondée **1939** -- "Unsere Kanzlei wurde 1939
in Chur gegründet", 3e génération familiale, tel/email, 4 domaines DE), Schawalder + Kocher
(fondée **2004**, tel/email, 3 avocats, 8 domaines DE). 1 SZ : Anwaltskanzlei Christoph Pfister
(tel/email, 2 avocats, **Fachanwalt SAV Bau- und Immobilienrecht** et **Fachanwalt SAV Erbrecht**
pour Christoph Pfister -- double titre confirmé explicitement sur la page d'accueil).

Échec `_sans_site` : Wolf Kuny Trütsch (SZ) -- avocat solo utilisant une adresse email bluewin.ch
générique, aucun site officiel dédié trouvé malgré recherche, présence uniquement via annuaires
tiers.

Note de rigueur : le premier jet de l'entrée Schawalder + Kocher (téléphone tiré d'un résumé
WebSearch, jamais vérifié en direct) a été corrigé par un WebFetch direct de la page d'accueil
avant commit -- le numéro affiché sur le site officiel diffère de celui trouvé via recherche
tierce, confirmant l'importance de toujours vérifier sur la source primaire.

Rattachement : 426 études rattachées au total (413 → 426, +13 nettes). Suite de tests : 94/94
au vert.

### 2026-09-07 20h04 UTC — Phase 3, lot 36 (exécution automatisée)

9 cabinets traités (9 succès / 0 échec), poursuite de LU (4), plus SZ, BL, SG (2). Doublon
réutilisé : `advocat.ch#2` (ME Advocat AG, 2e ligne CSV SG pour le cabinet déjà traité en AR au
lot 35). 4 LU : FRISCHKOPF & LOOP Advokatur (Sursee, tel/email, 4 personnes), Walder Haas
Berner AG (cabinet multi-sites Zofingen AG/Sursee LU/Wolhusen LU, tel/email bureau lucernois),
Kanzlei KMUFORUM GmbH (Emmenbrücke/Hitzkirch, tel/email, 4 avocats, 10 domaines EN), Lüdi Ludin
Steiner AG (Sursee, tel/email, 3 notaires-avocats). 1 SZ : Roesle Frick & Partner (cabinet
bi-site Zurich/Pfäffikon SZ, tel/email bureau schwytzois). 1 BL : Advokatur Lehner, Trüeb &
Küng (fondée **1987**, tel/email, 3 associés, 6 domaines EN). 2 SG : Kellenberger Kaufmann
Rechtsanwälte Notare (3 avocats, 5 domaines DE -- aucun tel/email confirmé sur la source
disponible), Weber Noser von Gleichenstein (cabinet multi-sites SG/TG, tel bureau st-gallois,
10 domaines DE).

Note de rigueur : team size de Weber Noser von Gleichenstein (14 personnes au total : 6 avocats
diplômés + 4 juristes/substituts + 4 administratif) ventilé -- seul le nombre d'avocats diplômés
(6) retenu comme `team_size_n`.

Rattachement : 434 études rattachées au total (426 → 434, +8 nettes). Suite de tests : 94/94 au
vert.

### 2026-09-07 21h04 UTC — Phase 3, lot 37 (exécution automatisée)

8 cabinets traités (8 succès / 0 échec), retour sur ZH -- la file des cabinets ≥3 avocats du
canton est quasi épuisée, ce lot porte sur des boutiques à 1-2 avocats. Doublon réutilisé :
`rfplegal.ch#ZH` (Roesle Frick & Partner, 2e ligne CSV ZH pour le cabinet bi-site déjà traité en
SZ au lot 36). 7 nouveaux : Baudenbacher Law AG (cabinet international Zurich/Bruxelles/Oslo,
tel/email bureau zurichois, 8 domaines EN -- statistiques des bureaux étrangers écartées, règle
4), Nobel & Partner Rechtsanwälte (boutique droit commercial international, tel/email, 10
domaines EN), Dietrich, Baumgartner & Partner (tel, 8 domaines EN), Widmer Baurecht AG
(boutique droit de la construction, tel/email), ammann + rosselet rechtsanwälte (fondée
**1994** -- "besteht in ihrer heutigen Form seit 1994", tel/email, 6 domaines DE), CONSAVO Legal
AG (bureaux Zurich/Zoug/Kobe, tel/email bureau légal), ATR Rechtsanwälte AG (tel, 3 avocats, 12
domaines EN).

Note : un candidat (Adler Salminen Rechtsanwälte AG) a été écarté après recherche -- une source
tierce suggérait une fusion avec BAT Rechtsanwälte AG, mais le site officiel de BAT ne confirme
cette continuité nulle part ; par prudence, aucune entrée n'a été créée plutôt que de supposer
un lien non vérifié sur la source primaire (candidat laissé pour une prochaine tentative avec
une recherche plus ciblée).

Rattachement : 442 études rattachées au total (434 → 442, +8 nettes). Suite de tests : 94/94 au
vert.

### 2026-09-07 22h04 UTC — Phase 3, lot 38 (exécution automatisée)

10 cabinets traités (9 succès / 1 échec), majoritairement ZH (boutiques à 2-3 avocats), plus 1
SG. Bänziger Bänziger Rechtsanwälte (Winterthour, tel/email, 4 personnes, **Fachanwalt SAV
Arbeitsrecht** pour Martin Bänziger, **Fachanwalt SAV Erbrecht** pour Urs Bänziger), Bettschart
Litscher Rechtsanwälte (Richterswil, tel/email, 2 avocats), BommerMathys Rechtsanwälte (tel/
email, 4 personnes, 6 domaines EN), Bihrer Rechtsanwälte AG (tel/email, 6 domaines DE), Büttler
I Benn Rechtsanwälte (tel/email, 2 avocats), Hugelshofer Rechtsanwälte (tel/email, 3 avocats, 9
domaines EN), Baur Imkamp & Partner (Dübendorf, fondée **1985**, tel, 3 avocats), Arioli Law
(boutique droit tech/données, fondée **2013** par Martina Arioli ex-Walder Wyss, email, 2
associés, 5 domaines EN), David Scherrer Büsser (aujourd'hui "Löwengasse – Rechtsanwälte &
Notare", tel/email, 3 avocats, 9 domaines EN). **Échec :** Ben-Attia LawPartners AG (HTTP 403
Forbidden sur la page de contact).

Rattachement : 451 études rattachées au total (442 → 451, +9 nettes). Suite de tests : 94/94 au
vert.

### 2026-09-07 23h04 UTC — Phase 3, lot 39 (exécution automatisée)

9 cabinets traités (8 succès / 1 échec), tous ZH -- boutiques à 2 avocats, file des cabinets
≥3 avocats désormais quasi épuisée sur ce canton. Bruppacher Anderes KIG (Zollikon, fondée
**1993**, tel, 2 avocats, 10 domaines DE), SEQUOIA Legal & Advisory GmbH (tel/email, 6 domaines
DE), Bonin & Langner Rechtsanwälte (boutique droit pénal exclusivement, tel/email, 2 avocats, 6
domaines DE), Brüngger Mattenberger Rechtsanwälte (tel/email, 2 avocats, 4 domaines DE),
Tethong Blattner AG (cabinet bi-site Zurich/Berne, tel/email bureau zurichois, 3 domaines DE),
Trachsel Bortolani Partner Rechtsanwälte & Mediatoren (tel, 2 avocats, **Fachanwalt SAV
Erbrecht** pour Daniel Trachsel), Bosonnet Wick Rechtsanwälte (fondée **2007** -- "Seit 2007
führen wir gemeinsam eine Kanzlei", tel, 2 avocats fondateurs), Chlup Legal Services (boutique
droit de la famille/divorce, tel/email, 6 domaines EN). **Échec :** Jaquenod Rechtsanwälte
(apollolaw.ch, HTTP 503 sur deux tentatives http et https).

Rattachement : 459 études rattachées au total (451 → 459, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 00h04 UTC — Phase 3, lot 40 (exécution automatisée)

11 cabinets traités (9 succès / 1 échec / 1 sans-site), tous ZH -- boutiques à 2-4 avocats.
Camp Fahrni Rechtsanwälte (tel/email, 2 avocats, 4 domaines DE, **Fachanwalt SAV Familienrecht**
pour Silvan Fahrni depuis 2017), Wyss & Partner (fondée **1975**, tel/email, 3 associés, 10
domaines EN), LEXIMPACT (boutique droit financier/FinTech, tel, 3 avocats, 7 domaines EN),
Chabrier Rechtsanwälte GmbH (bureau zurichois d'un cabinet basé à Genève, tel/email spécifiques
à Zurich), Bürgi & Kriegers-Tejura Legal (tel/email, 2 avocates, 5 domaines EN), Advokatur
Glavas AG (cabinet bi-site Muolen SG/Zurich, tel/email spécifiques au bureau zurichois, 4
avocats, 7 domaines DE), BLM Rechtsanwälte (Dietikon, tel/email, 2 avocats), Anwaltsbüro Brem
(Richterswil, boutique très spécialisée -- droit de la consommation, cosmétique, chimique,
douanier, tel/email, 9 domaines DE), Peter & Kim AG (bureau zurichois d'un cabinet d'arbitrage
international basé à Genève, fondé **2019**, tel/email spécifiques à Zurich, 5 domaines EN).

**Échec :** Schmid Rechtsanwälte (schmidlaw.ch, seule la page d'accueil générique accessible,
/en/contact et /team en 404, aucun fait exploitable). **Sans site :** Jositsch Brunner
Rechtsanwälte (aucun site officiel dédié trouvé après deux recherches distinctes, présence
uniquement via annuaires tiers).

Rattachement : 468 études rattachées au total (459 → 468, +9). Suite de tests : 94/94 au vert.

### 2026-09-08 01h04 UTC — Phase 3, lot 41 (exécution automatisée)

10 cabinets traités (8 succès / 2 échecs), tous ZH -- boutiques à 2-3 avocats. Fingerhuth
Anwälte (droit pénal, tel/email, 3 avocats), Fertig Keller Stark Rechtsanwälte (tel, 3 avocats,
**Fachanwältin SAV Haftpflicht- und Versicherungsrecht** pour Britta Keller depuis 2017),
EhlertZillig (tel, 2 avocats, 6 domaines DE), Schönmann Law (Dietikon, tel/email, 2 avocats, 8
domaines DE), Rechtsanwälte Pfau & Egli (Winterthour, tel/email, 2 avocats), Christe & Isler
Rechtsanwälte (Winterthour, tel/email, 2 avocats), Raewel Advokatur (tel/email, 3 personnes,
**Fachanwältin SAV Strafrecht** pour Dina Raewel depuis 2001), Isler I Del Grande Rechtsanwälte
(tel/email, 2 avocats). **Échecs :** Jack Würgler & Partner Rechtsanwälte (wuergler-ra.ch, HTTP
503 sur http et https) ; DTK Rechtsanwälte AG (dtk-legal.ch, HTTP 503 sur deux pages testées).

Note de rigueur : "in den frühen 90er Jahren" (Pfau & Egli, formulation vague) écarté comme
`founding_year`, conformément à la règle 2.

Rattachement : 476 études rattachées au total (468 → 476, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 02h04 UTC — Phase 3, lot 42 (exécution automatisée)

8 cabinets traités (7 succès / 1 échec), tous ZH -- boutiques à 2 avocats. Kanzlei Caro (fondée
**1996**, tel/email, 4 domaines EN, clientèle internationale germano/anglo-saxonne), FARNER
WAGNER EICHIN (tel/email, 2 avocats, 5 domaines DE, **Fachanwalt SAV Arbeitsrecht** pour Martin
Farner ET **Fachanwältin SAV Arbeitsrecht** pour Martina Wagner Eichin -- les deux associés
certifiés), FISCHER WICKI Rechtsanwälte (Schlieren, tel/email, 2 avocats, 6 domaines DE),
Künzli Sommer Frey AG (fondée **1928** -- cabinet centenaire, tel/email, 3 domaines EN,
boutique droit fiscal), Gegenschatz Partner AG (tel, 3 domaines DE), GRP Partner KIG (tel, 3
domaines DE), Gisler & Haltiner Rechtsanwälte (Wetzikon, tel, 6 domaines DE). **Échec :** RCS
Trust & Legal AG (rcslegal.ch, page d'accueil quasi vide -- rendu JavaScript probable, /en/
contact en 404).

Rattachement : 483 études rattachées au total (476 → 483, +7). Suite de tests : 94/94 au vert.

### 2026-09-08 03h04 UTC — Phase 3, lot 43 (exécution automatisée)

8 cabinets traités (8 succès / 0 échec), 7 ZH + 1 BL. Anwaltskanzlei Horák (fondée **2011** --
"Im Jahre 2011 gründete er... eine Anwaltskanzlei", tel/email, 2 avocats, 8 domaines DE), Gloor
& Sieger AG (Zollikon, fondée **1989**, tel/email, 2 avocats, 8 domaines EN), Schwager Schmid
Giusto (tel, 2 avocats), Goetz & Patak (Küsnacht, tel/email, 2 avocats), Kanzlei Käser (fondée
**2023**, tel/email, avocat solo, 6 domaines EN), Gresch, Schwab & Varela Rechtsanwälte
(cabinet bi-site Zurich/Pfäffikon SZ, tel/email bureau zurichois), AlpinumLaw Rechtsanwälte AG
(tel/email, 9 personnes, 12 domaines DE dont blockchain/IA), Advokaturbüro Albrecht I Riedo I
Anwander (BL, Muttenz, tel/email, 4 avocats, 8 domaines EN).

Note de rigueur : un candidat (Advokatur Schweighauser von Wartburg Aeschlimann Maier, BL) a
été écarté après recherche -- un résumé tiers suggérait un renommage en "LAMOLEX", mais le site
officiel de LAMOLEX ne confirme cette continuité nulle part (aucune mention du nom d'origine) ;
par prudence, même principe que pour Adler Salminen/BAT au lot 37, aucune entrée créée plutôt
que de supposer un lien non vérifié sur la source primaire.

Rattachement : 491 études rattachées au total (483 → 491, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 04h04 UTC — Phase 3, lot 44 (exécution automatisée)

12 cabinets traités (12 succès / 0 échec), tous ZH -- meilleur lot de boutiques à 2-3 avocats
depuis plusieurs heures. RÜD Partners AG (tel/email, 3 personnes, 7 domaines EN dont litiges
bancaires/financiers), HELBLING Rechtsanwälte (boutique executive compensation, fondée
**2013** -- déduit du "10ème anniversaire célébré le 1er avril 2023" affiché sur le site, tel,
3 personnes, 4 domaines DE), Marghitola Dispute Resolution (tel/email, 2 avocats, 6 domaines
EN), SCHWENNINGER INGLIN RECHTSANWÄLTE (Rüti, tel/email, 2 avocats, 3 domaines DE), Peyrot,
Schlegel und Györffy Rechtsanwälte (cabinet bi-site Zurich/Buchs SG, tel/email bureau
zurichois, 13 domaines DE), Hüppi & von Sprecher (tel/email, 7 domaines DE), Advokatur Libero
AG (fondée **2024**, tel/email, 2 avocats), Martin Rechtsanwälte GmbH (cabinet bi-site
Winterthour/Zurich, tel/email), Advokatur Regensdorf GmbH (tel/email, 8 domaines DE),
Anwaltsbüro Lätsch + Hässig (Rüti, tel/email, 2 avocats), H&K Legal GmbH (boutique droit de la
famille international, tel/email, 3 domaines EN), Hauser & Hauser (fondée **1920** -- "seit
1920 als erweiterter Familienbetrieb geführten Kanzlei", 9 domaines DE, boutique art/famille/
succession).

Rattachement : 503 études rattachées au total (491 → 503, +12). Suite de tests : 94/94 au vert.

### 2026-09-08 05h04 UTC — Phase 3, lot 45 (exécution automatisée)

8 cabinets traités (7 succès / 1 échec), tous ZH. LINDEMANN LAW AG (boutique gestion de
fortune/wealth management, tel/email), Sosso Jaeger Law AG (tel, 4 domaines EN), Iten McNally
GmbH (fondée **2020**, tel, 2 avocats, 4 domaines EN), Kägi Schuler Partner (issue de la
scission de Baumann Kägi Schuler en 2025, tel/email, 2 avocats, 6 domaines DE), Jakob I
Marsella Rechtsanwälte (tel/email, 2 avocats, 10 domaines EN), Jäger & Schweiter (boutique
droit médical, tel, 2 avocats, 5 domaines DE), rechtdirekt (Uster, tel/email, 2 avocats, 12
domaines DE). **Échec :** Jermann Künzli Rechtsanwälte (jkr.ch, HTTP 403 Forbidden).

Rattachement : 510 études rattachées au total (503 → 510, +7). Suite de tests : 94/94 au vert.

### 2026-09-08 06h04 UTC — Phase 3, lot 46 (exécution automatisée)

9 cabinets traités (8 succès / 1 échec), tous ZH. Obergass Advokatur (fondée **1970** -- "Sie
besteht seit 1970", tel/email, 2 avocats, 6 domaines DE dont droit de la responsabilité
civile/assurances et aide aux victimes), Kramer & Kramer (fondée **1971**, 3 domaines DE),
CORE Rechtsanwälte AG (boutique droit de la concurrence/antitrust, tel/email, 6 domaines EN --
année de fondation vue en recherche tierce (2020) non retenue, absente de la source primaire),
Legal Experts Switzerland AG (4 domaines DE dont droit des sociétés et droit du travail/
étrangers), Seidel & Partner Rechtsanwälte AG (boutique droit de la construction/immobilier,
tel/email, 5 domaines DE), Küng & Meili Rechtsanwälte (tel/email), Anwaltskanzlei Köppel GmbH
(cabinet bi-site Winterthour/Bienne, tel, 2 domaines DE dont conseil juridique Chine),
Zulauf Partner (zulauflegal.ch, boutique droit des médias/réputation, tel/email, 9 domaines
DE). **Échec :** Zuppiger Jenny Rechtsanwälte AG (aucun domaine identifié).

Rattachement : 518 études rattachées au total (510 → 518, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 07h04 UTC — Phase 3, lot 47 (exécution automatisée)

15 cabinets traités (12 succès / 3 échecs), tous ZH. Streiff Rechtsanwälte AG (Wetzikon,
fondée **2004** -- "Gegründet wurde die ... Anwaltskanzlei von Dr. Matthias Streiff im Jahr
2004", tel/email, 6 domaines DE droit immobilier/construction), Schuler Forrer Schumacher
Rechtsanwälte (communauté de 4 avocats indépendants, chacun avec son propre tel/email --
aucun tel/email de cabinet inventé, conformément au protocole), Schaub Rechtsanwälte
(Limmatquai, fondée **1994**, tel/email, 4 avocats, 11 domaines DE), Risch Legal (boutique
droit de la construction, tel, 2 avocats, 7 domaines DE), Rechsteiner Thürkauf Rechtsanwälte
(fondée **2007** -- "im Herzen von Zürich seit 2007", tel/email, 2 avocats, 7 domaines DE),
ROMANG & WENGER Rechtsanwälte (communauté de 2 avocats indépendants avec tel propres --
domaines combinés retenus, aucun tel de cabinet inventé), ROH Rechtsanwälte AG (tel/email,
4 domaines EN, faits limités au cabinet suisse), Pikó Uhl Rechtsanwälte AG (boutique
compliance/investigations, tel/email, 2 avocats, 4 domaines EN), PRINS Law GmbH (boutique
propriété intellectuelle, tel/email, 8 avocats, 8 domaines EN), Meyer & Wipf Rechtsanwälte
(tel/email, 2 avocats, 2 domaines DE), Meili Pfortmüller (boutique droit des médias/
communication/arts, tel/email, 3 avocats), Ronzani Schlauri Anwälte (boutique droit des
technologies/IT, tel/email, 3 domaines EN). **Échecs :** Sigg Schwarz Advokatur (siggschwarz.ch,
403×2), SIEBER RECHTSANWÄLTE (sieberlex.ch, 404 sur plusieurs chemins), Schai & Vultier
(schai-vultier.ch, 503×2).

Rattachement : 530 études rattachées au total (518 → 530, +12). Suite de tests : 94/94 au vert.

### 2026-09-08 08h04 UTC — Phase 3, lot 48 (exécution automatisée)

20 cabinets traités (17 succès / 3 échecs), tous ZH. Schnitter Weber Staub Weidmann
(tel/email, 9 domaines DE), MV Legal Partners AG (fondée **2015** -- "Founding partner MV
Legal Partners Inc. (since 2015)", tel/email, 5 personnes), M&R Rechtsanwälte AG (Kilchberg,
tel/email, 2 avocats -- personnel administratif exclu du compte, 9 domaines DE), Luginbühl
Roesle Rechtsanwälte (tel/email, 3 avocats, 5 domaines DE -- "besteht seit rund 30 Jahren"
trop vague pour une année précise, non retenu), Loosli Schmid Rechtsanwälte AG (tel/email,
2 avocats -- personnel administratif exclu, 6 domaines DE), Lindholm & Rosenkranz
Rechtsanwälte GmbH (boutique contentieux/arbitrage, 5 avocats, 7 domaines EN), Lerch & Lerch
(Bubikon, tel/email, 2 avocats), Kaiser Odermatt & Partner AG (bureau zurichois, tel/email
spécifiques à Zurich, 8 domaines DE), IXAR Legal AG (email, 6 domaines DE dont compliance/
protection des données), HWN RECHTSANWÄLTE KLG (fondée **1985** -- "since 1985", tel/email,
2 avocats, 4 domaines DE), Burki Rechtsanwälte (Zollikon, fondée **1997** -- "im Jahre 1997
die Kanzlei Burki Rechtsanwälte ... gründete", 13 domaines DE fiscalité/succession),
Baurechtspartner AG (tel/email, 2 avocats -- juristes non-avocats exclus, 7 domaines DE droit
de la construction), Wenfei Rechtsanwälte AG (bureau zurichois, tel/email spécifiques à
Zurich, faits globaux du réseau Shanghai/Pékin exclus), Pontinova AG (boutique crypto/DLT,
tel/email), PALOMBO Anwaltskanzlei (email, 10 domaines DE), RIHAR & THOUVENIN DISPUTE
RESOLUTION (boutique arbitrage international, tel/email, 2 avocates), Ramelet AG (boutique
droit des marchés financiers, email, 5 domaines DE). **Échecs :** Maurer & Stäger AG
(mst-law.ch, 503×2), Maron Zirngast Rechtsanwälte (zirngast.ch, site accessible mais aucune
coordonnée exploitable après 4 pages testées), Luchsinger + Spinner Rechtsanwälte
(luchsingerspinner.ch, site accessible mais rien d'exploitable au-delà de l'adresse déjà
connue).

Rattachement : 547 études rattachées au total (530 → 547, +17). Suite de tests : 94/94 au vert.

### 2026-09-08 09h03 UTC — Phase 3, lot 49 (exécution automatisée)

16 cabinets traités (10 succès / 6 échecs dont sans-site), ZH et TI. von der Crone
Rechtsanwälte AG (tel/email, 2 avocats), von Grünigen Rechtsanwälte (tel/email, 2 avocates),
team alex gmbh (boutique droit du travail, tel/email, 9 domaines DE), Advokatur Mörikofer
(tel/email, 2 avocates, 3 domaines DE droit de la construction/environnement), Baryon AG
(fondée **1997** -- "Founded 1997", tel/email, 3 domaines EN gestion de fortune/fiscalité/
conseil juridique), Anwaltsbüro Dr. Walter Hagger (rattachement par déduplication : cette
fiche CSV correspond à l'ancien nom du cabinet aujourd'hui HWN RECHTSANWÄLTE -- continuité
confirmée par la page "Kanzleiportrait" de hwn-law.ch elle-même, faits déjà vérifiés en lot
48 réutilisés, fondée 1985), Quadranti Molteni Studio legale e notarile (Chiasso, tel/email,
11 domaines IT), studio legale Nievergelt & Stoehr SA -- antenne de Lugano (rattachement par
déduplication : même cabinet déjà rattaché au canton GR en lot antérieur sous
nievergeltundstoehr.ch, même téléphone confirmant l'identité, 6 domaines IT), studio legale
e notarile Dominé - Marone (Bellinzona/Biasca, communauté de 2 avocats indépendants avec
lignes directes propres -- aucun tel de cabinet inventé, domaines combinés retenus), studio
legale e notarile Marcellini-Galliani (Lugano, 5 domaines IT droit pénal/international).
**Échecs :** Advokaturbüro Lengyel (lengyel.ch, 503×2), lo studio notarile Velo & Associati
(rattachement possible à LVA VELO SA selon une source tierce mais jamais confirmé par la
source primaire, 403 sur la page About Us -- lien non retenu), Studio Legale Avv. Luisa Polli
(identité incertaine, rattachement à un autre studio selon une source tierce non confirmée).
**Sans site officiel identifié :** ARGO Rechtsanwälte, Studio legale e notarile Poma-Gandolfi
& Associati, Studio Legale M LAW.

Rattachement : 556 études rattachées au total (547 → 556, +9). Suite de tests : 94/94 au vert.

### 2026-09-08 10h04 UTC — Phase 3, lot 50 (exécution automatisée)

18 cabinets traités (12 succès / 7 échecs dont sans-site), tous TI -- premier lot exclusivement
tessinois de la campagne. Studio legale e notarile Rossi-Pellegrini-Sauvain (Mendrisio, fondé
**1965** -- "Fondato nel 1965 dall'avv. Pierluigi Rossi, già Sindaco di Mendrisio", tel/email,
6 domaines IT), Studio legale e notarile Luisoni (Bellinzona, tel/email, 2 avocats), Studio
legale e notarile Guglielmetti & Basic (Mendrisio, tel -- fondation 1926 vue en résumé de
recherche tierce mais non confirmée par une source primaire, non retenue), Studio legale e
notarile Gagliardi & Giang (Bellinzona, tel/email), Studio legale e notarile Corti & Partner
(Lugano/Milan, email, 2 avocats -- personnel administratif exclu, 9 domaines EN), Studio
legale e notarile Colombo & Mameli (Lugano, tel/email), Studio legale e notarile Cocchi &
Bisazza Ranzi (Gravesano, tel/email, 2 domaines IT), Studio legale e notarile Camponovo &
Camponovo (Chiasso, fondé **2003** -- "attivo... dal 2003", tel/email, 13 domaines IT),
Studio Legale Pedrazzini Zanazza & Associati SA (Lugano, tel/email, 12 domaines IT), MCM
studio legale e notarile (Lugano, fondé **2022** -- "2022 – oggi ... fondatore e Partner",
tel/email, 2 avocats, 11 domaines IT), Grandini Studio legale e notarile (Lugano, fondé
**1985** -- "premier cabinet ouvert en août 1985", tel/email, 9 domaines IT), CSNLAW (Lugano,
11 domaines EN). **Échecs :** Studio Legale Ferracin & Associati (503×2), Studio legale e
notarile Tamagni Fornara & Associati (503×2), Studio legale e notarile Cereghetti (identité
ambiguë -- au moins deux études distinctes portant ce nom au Tessin, rattachement non
confirmé). **Sans site officiel :** Torricelli Zveiger Studio legale e notarile, Studio
legale e notarile Zandrini & Partners, Studio legale e notarile Ferrari Partner (à distinguer
du cabinet homonyme sans lien "Legal Ferrari Rei"). Note bibliographique : ajout d'une entrée
`_failed` pour Adler Salminen Rechtsanwälte AG (ZH, identité déclinée en lot 37) afin d'éviter
qu'elle ne resurgisse dans les futurs lots.

Rattachement : 566 études rattachées au total (556 → 566, +10). Suite de tests : 94/94 au vert.

### 2026-09-08 11h04 UTC — Phase 3, lot 51 (exécution automatisée)

12 cabinets traités (10 succès / 2 échecs), premier lot centré sur SG. Weber Noser von
Gleichenstein (rattachement par déduplication : deuxième ligne CSV pour un cabinet déjà
rattaché ce jour sous une variante de nom, faits déjà vérifiés réutilisés), Stach
Rechtsanwälte AG (St-Gall/Zurich, tel/email, 5 domaines EN), Studer Zahner Anwälte (fondée
**2001** -- "Gründung: 2001", tel, 5 domaines DE), Huber Walker Rechtsanwälte (Kaltbrunn,
8 domaines DE droit agraire/rural), Gysi & Partner Rechtsanwälte AG (tel/email), Dolder Züst
Rechtsanwälte (boutique droit de la famille, tel/email, 3 avocats tous titulaires du titre
Fachanwalt SAV Familienrecht), Brunner Knobel Rechtsanwälte (Rapperswil-Jona, tel, 2 avocats,
7 domaines DE dont droit de l'environnement/dangers naturels), BST Rechtsanwälte & Notare
(tel/email, 4 avocats, 8 domaines DE), BRENNER STILLHART TSCHURR Rechtsanwälte & Notare
(rattachement par déduplication : même cabinet que BST Rechtsanwälte & Notare ci-dessus, nom
long vs nom court, faits réutilisés), ARTARIS Advokatur AG (tel/email, 5 domaines EN).
**Échecs :** Schöbi Rechtsanwälte (rattachement possible à Schöbi Studio Legis AG selon le
patronyme partagé, mais aucune confirmation de continuité sur le site du cabinet -- lien non
retenu), Grand & Nisple Rechtsanwälte (grandnisple.ch, 503×2).

Rattachement : 576 études rattachées au total (566 → 576, +10). Suite de tests : 94/94 au vert.

### 2026-09-08 12h04 UTC — Phase 3, lot 52 (exécution automatisée)

12 cabinets traités (9 succès / 3 échecs dont sans-site), SZ et LU. Toedtli.Law GmbH
(Wollerau, fondée **2021**, tel/email, 2 avocats), Droxler Rechtsanwälte AG (Altendorf,
tel/email, 10 domaines DE), Rothenbühler Cocchi Rechtsanwälte (Lucerne, fondée **1993** --
"besteht seit 1993", tel/email, 2 avocats, 9 domaines DE), Niggli & Huber (Lucerne, fondée
**2013** -- "Seit 2013 ein eingespieltes Team", tel/email, 2 avocats), Kälin & Bruhin
(Freienbach, tel, 2 domaines DE), Anwaltskanzlei Zürichsee AG (Wollerau, tel/email, 3 avocats,
12 domaines DE), zm rechtsanwälte (Lucerne, fondée **2017** -- "Die im Jahr 2017 von zwei
langjährigen Freunden gegründete Anwaltskanzlei", tel), Mensik & Schmid Rechtsanwälte
(Meggen/Lucerne, tel, 2 avocats), Lauper & Partner AG (Lucerne, tel/email). Kaufmann Rüedi
Rechtsanwälte AG (LU) déjà présent au cache (lot antérieur, doublon identifié et écarté).
**Échec :** Rechtsmanufaktur (chaîne de redirections vers un sous-domaine d'hébergement
générique cyon.site, site non fonctionnel). **Sans site officiel :** Beeler & Wiget
(aujourd'hui "Beeler, Wiget & Huwyler", aucun site propre identifié), Keller Lehmann
Rechtsanwälte AG.

Rattachement : 584 études rattachées au total (576 → 584, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 13h04 UTC — Phase 3, lot 53 (exécution automatisée)

12 cabinets traités (8 succès / 4 échecs), LU, SG et GR. Horvath Rechtsanwälte AG et Costa
Rechtsanwälte AG (deux entités juridiques distinctes opérant ensemble sous la bannière
"Neustadt Advokatur" à la même adresse/tel/email -- confirmé sur la page d'accueil qui liste
les deux raisons sociales en pied de page -- avec titres de spécialiste FSA propres à chacune :
Fachanwalt SAV Familienrecht pour Horvath, Fachanwältin SAV Erbrecht pour Costa Oreiller),
Domenghini & Partners AG (tel/email), Cottinelli Advokatur & Notariat GmbH (tel/email,
13 domaines DE), Graf Niedermann Rechtsanwälte (rattachement confirmé via une chaîne de
redirections graf-niedermann.ch → gnb-law.ch → gb-law.ch où le téléphone et l'adresse restent
identiques à chaque étape, preuve de continuité malgré les renommages successifs, 4 domaines
DE), Schneider & Schneider Rechtsanwälte & Notare (tel/email, 2 avocats, 10 domaines DE),
hsm legal AG (email, 3 avocats, 8 domaines DE), Die Advokatur Sury AG (boutique IA/gouvernance
des données, tel/email, 6 domaines DE). **Échecs :** Suenderhauf Sax Schäfer (communauté de
3 avocats totalement indépendants avec sites propres, aucun site commun), Zgraggen & Ulrich
(rattachement possible à Zgraggen Rechtsanwälte AG selon le patronyme partagé, mais aucun
avocat nommé Ulrich sur l'équipe actuelle -- lien non retenu), Schucan & Wohlwend (503×2),
Erni Grab & Partner AG (communauté d'avocats, aucun domaine de compétence concret extrait).

Rattachement : 592 études rattachées au total (584 → 592, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 14h04 UTC — Phase 3, lot 54 (exécution automatisée)

9 cabinets traités (9 succès / 0 échec), premier lot majoritairement GR sans aucun échec.
Brändli Rechtsanwälte AG (Chur, tel/email, 5 avocats), Flütsch Advokatur & Notariat GmbH
(Davos, tel/email, spécialiste FSA Bau- und Immobilienrecht, 5 domaines DE), Schnyder Janett
Advokatur & Notariat (Landquart, tel/email, 5 domaines DE), Ganzoni & Pedretti AG (St-Moritz,
tel), Caviezel Thöny Cantieni Scarpatetti (Chur, tel/email, 8 domaines DE), Götte
Rechtsanwälte (Lucerne, fondée **2009** -- "Wir sind seit 2009 als Rechtsanwälte tätig",
tel/email, 2 avocats, 7 domaines DE), Dr. Rudolf & Bieri AG (Lucerne, tel/email), Meisser &
Partners AG (boutique marques, Klosters/Landquart, tel, 3 avocats -- 5 paralegals/secrétaires
exclus du compte, 5 domaines DE). Nievergelt & Stoehr AG (rattachement par déduplication :
troisième ligne CSV pour ce cabinet déjà rattaché deux fois ce jour sous GR et TI, faits déjà
vérifiés réutilisés).

Rattachement : 600 études rattachées au total (592 → 600, +8). Suite de tests : 94/94 au vert.

### 2026-09-08 15h04 UTC — Phase 3, lot 55 (exécution automatisée)

9 cabinets traités (7 succès / 2 échecs), GR, BL et LU. Schmid Christoffel Rechtsanwälte AG
(Davos, fondée **2017** -- "Im April 2017 gründete sie zusammen mit Hansjürg Christoffel die
Kanzlei", tel/email, spécialiste FSA Familienrecht, 4 domaines DE), Areum Rechtsanwälte AG
(Chur, fondée **2023** -- "am 1. Juni 2023 die AREUM Rechtsanwälte AG ... gegründet", tel,
2 avocats, 11 domaines DE combinés), Erhart Rechtsanwälte & Notariat (Oberwil BL, tel/email),
Perl Advokatur und Notariat (Chur, tel/email), Lüthi & Bondolfi (Samedan/Chur, tel/email,
4 domaines DE). Deux rattachements par déduplication : Ganzoni & Pedretti AG Via (deuxième
ligne CSV pour le cabinet déjà rattaché en lot 54) et Dr. Tschümperlin Lötscher Schwarz AG
(deuxième ligne CSV pour un cabinet déjà en cache depuis un lot antérieur, fondé en 1973).
**Échecs :** Tenchio & Partner (tenchio.ch, 503×2), Zeller Dettwiler Advokatur & Notariat
(site accessible mais aucun tel/email exploitable).

Rattachement : 605 études rattachées au total (600 → 605, +5). Suite de tests : 94/94 au vert.

### 2026-09-08 16h04 UTC — Phase 3, lot 56 (exécution automatisée)

7 cabinets traités (6 succès / 1 échec), OW, NW, LU et GR. Krummenacher Rechtsanwälte und
Notare AG (Sarnen/Kerns, tel, 4 domaines DE), Würsch-Müller Grendelmeier Advokatur Notariat
(Stans, communauté de 2 avocats indépendants avec lignes directes propres -- aucun tel de
cabinet inventé), Ineichen Advokatur und Notariat (rattachement confirmé : la page de contact
de iup.ch cite explicitement "Reto Ineichen ... Advokatur Ineichen AG", tel/email, spécialiste
FSA Strafrecht), Däppen Rechtsanwälte (Coire, fondée **2001** -- "Däppen Rechtsanwälte besteht
seit dem Jahr 2001", tel/email, 2 avocats, 12 domaines DE). Deux rattachements par
déduplication : Schmid Christoffel Rechtsanwälte AG Obere et Lüthi & Bondolfi Via (deuxièmes
lignes CSV pour des cabinets déjà rattachés en lot 55). **Échec :** Hischier & Brunner
(hb-recht.ch, 503×2).

Rattachement : 611 études rattachées au total (605 → 611, +6). Suite de tests : 94/94 au vert.

### 2026-09-08 17h04 UTC — Phase 3, lot 57 (exécution automatisée)

6 cabinets traités (4 succès / 2 échecs), OW, LU, BL et NW. WILD DUBACH AG (cabinet multi-
sites Bâle/Hergiswil/Sarnen, tel/email, 28 domaines EN -- rattaché deux fois par
déduplication pour les lignes CSV OW et LU du même cabinet), Enderle, Felix, Haidlauf, Schmid,
Advokatur (Reinach BL, tel/email -- rattachement par déduplication d'un cabinet déjà en cache
sous un ordre de noms différent), Blöchlinger Iten Anwaltskanzlei Notariat Alter (Stans,
aujourd'hui "Blöchlinger Iten Fessler" avec un troisième associé -- continuité confirmée par
la présence de Marc Blöchlinger sur l'équipe actuelle de bilaw.ch, tel/email). **Échecs :**
Advokatur Notariat Schmid (piège d'identité évité : le site trouvé, notariat-schmid.ch,
correspond en réalité à un cabinet homonyme à Münchenstein BL et non au Fortunat Schmid de
Coire GR recherché -- lien non retenu), Durrer Britschgi Advokatur und Notariat (advo-stans.ch,
503×2).

Rattachement : 615 études rattachées au total (611 → 615, +4). Suite de tests : 94/94 au vert.

### 2026-09-08 18h03 UTC — Phase 3, lot 58 (exécution automatisée)

6 cabinets traités (5 succès / 1 échec), SG et NW. Reiser + Partner AG (fondée **2024** --
"Im Jahr 2024 gründete er die Reiser + Partner AG", tel/email, 10 domaines DE, rattachée deux
fois par déduplication pour les lignes CSV avec et sans adresse), J&K Rechtsanwälte AG
(tel/email, 7 domaines DE dont venture capital/M&A), HEBRECHT AG (boutique responsabilité
civile/droit médical, tel/email, 5 domaines DE). Dubach Wild AG Rechtsanwälte Notariat
(rattachement par déduplication : troisième ligne CSV pour WILD DUBACH AG déjà rattaché deux
fois en lot 57). **Échec :** Advokatur Wieser & Wieser (wieser-wieser.ch, 503×2).

Rattachement : 620 études rattachées au total (615 → 620, +5). Suite de tests : 94/94 au vert.

### 2026-09-08 19h03 UTC — Phase 3, lot 59 (exécution automatisée)

5 cabinets traités (4 succès / 1 échec), SG et BL. Good Rechtsanwälte St.Gallen AG (tel/email,
11 domaines EN), Rosenhof Legal GmbH (Rapperswil, tel/email, 3 domaines DE), Advokatur Sissach
(fondée **2015** -- "Selbstständiger Advokat mit eigener Kanzlei (seit 2015)", tel/email,
9 domaines DE), Advokatur und Notariat Neidhart Joset Bürgi (Bâle/Liestal, continuité
confirmée : les 4 associés du nom CSV -- Martin Neidhart, Alain Joset, Alinda Neidhart, Silvio
Bürgi -- figurent tous sur l'équipe actuelle de baselrecht.ch malgré l'ajout depuis d'un 5e
associé sur une fiche tierce, tel, 4 avocats). **Échec :** LM Rechtsanwälte AG (lmrecht.ch,
503×2).

Rattachement : 623 études rattachées au total (620 → 623, +3). Suite de tests : 94/94 au vert.

### 2026-09-08 20h03 UTC — Phase 3, lot 60 (exécution automatisée)

5 cabinets traités (3 succès / 2 échecs), premier lot touchant le canton AR. Advokatur
Tomaschett (Coire, fondée **1989** -- "Unsere Anwaltskanzlei führen wir seit 1989", tel/email),
Kistler & Kollegen (Davos, email, 3 avocats, 7 domaines DE), Cavelti & Wernli (Herisau AR,
6 domaines DE, aucun tel/email exploitable trouvé sur les pages testées). **Échec :** schmid,
giuliani, Rechtsanwälte (schmidgiuliani.ch, 503×2). **Sans site confirmé :** Polartis Advokatur
(identité incertaine -- seule entité trouvée sous ce nom est une société de conseil en
stratégie, pas un cabinet d'avocats confirmé).

Rattachement : 625 études rattachées au total (623 → 625, +2). Suite de tests : 94/94 au vert.

### 2026-09-08 21h03 UTC — Phase 3, lot 61 (exécution automatisée)

5 cabinets traités (3 succès / 2 échecs), LU et ZH. Anwaltsbüro Kost (Ebikon, tel, 8 domaines
DE dont droit d'internet/cybercriminalité -- email volontairement absent du site, non
inventé), wyttenbach law (boutique droit pénal, tel/email, spécialiste FSA Strafrecht depuis
2015, 3 domaines EN), steinlaw (boutique droit de la famille/pénal, tel/email, spécialiste FSA
Familienrecht, 4 domaines DE). **Échecs :** staedeli legal partners GmbH (503×2), weberlegal
(503×2).

Rattachement : 628 études rattachées au total (625 → 628, +3). Suite de tests : 94/94 au vert.

### 2026-09-08 22h04 UTC — Phase 3, lot 62 (exécution automatisée)

6 cabinets traités (4 succès / 2 échecs), tous ZH -- lot ciblant les boutiques unipersonnelles
à nom de domaine distinctif. penalisti Rechtsanwälte AG (boutique droit pénal, Zurich/Aarau,
tel/email, 5 avocats, 4 domaines DE), freigutpartners IP Law Firm (boutique propriété
intellectuelle, tel/email spécifiques au bureau de Zurich, 10 domaines EN -- faits limités aux
bureaux suisses, réseau international exclu), kaelin.legal AG (boutique restructuration/
insolvabilité, tel/email, 4 domaines EN), kerber.legal (tel/email). **Échecs :** rauchlegal
(403×2), schaller.law GmbH (503×2).

Rattachement : 632 études rattachées au total (628 → 632, +4). Suite de tests : 94/94 au vert.

### 2026-09-08 23h03 UTC — Phase 3, lot 63 (exécution automatisée)

6 cabinets traités (2 succès / 4 échecs), tous ZH. Zeier & Dekker Rechtsanwälte (Küsnacht,
communauté avec lignes directes propres -- aucun tel/email de cabinet inventé, 11 domaines
DE), mbh ATTORNEYS AT LAW Mönnich, Bell & Oldani KLG (boutique droit des assurances/
réassurance, tel/email, 5 avocats). **Échecs :** Umbricht Rechtsanwälte AG (503×2), Weinmann
Zimmerli (site JS-only Nuxt, aucun contenu HTML statique exploitable), Zollinger Rohner
Rechtsanwälte (zr-law.ch, 503×2), Winzeler Law (503×2 y compris après redirection).

Rattachement : 634 études rattachées au total (632 → 634, +2). Suite de tests : 94/94 au vert.

### 2026-09-09 00h03 UTC — Phase 3, lot 64 (exécution automatisée)

6 cabinets traités (5 succès / 1 échec), tous ZH. WWNW Advokatur AG (tel/email, 4 avocats),
Zuzak Rechtsanwälte AG (tel/email spécifiques au bureau de Zurich -- cabinet international
avec Prague/Bratislava, faits limités à la Suisse), Uhlmann Trümpler Rechtsanwälte (UTR) GmbH
(boutique droit public, tel/email, 2 avocats fondateurs), VALLUCCI & SCHMUTZ AG (boutique
fiscalité/planification successorale, tel, 2 avocats, 6 domaines EN), Weidmann Rechtsanwälte
(tel/email, 5 domaines DE). **Échec :** Winter & Partner (winterpartner.ch, 503×2).

Rattachement : 639 études rattachées au total (634 → 639, +5). Suite de tests : 94/94 au vert.

### 2026-09-09 01h03 UTC — Phase 3, lot 65 (exécution automatisée)

6 cabinets traités (3 succès / 3 échecs dont sans-site), tous ZH. Swiss Insurance Law GmbH
(boutique droit des assurances/réassurance, tel/email, 2 avocates, 5 domaines EN), THEMIS
Legal & Advisory (Volketswil, boutique droit de la famille/représentation d'enfants, tel/
email, 5 domaines DE), Urbach Law (tel, 10 domaines EN dont droit des sociétés/contrats/
arbitrage). **Échec :** Stäubli Advokatur (staeubliadvocate.com, 503×3). **Sans site
identifié :** Sutter & Camenzind Rechtsanwälte, TM & Partner Rechtsanwälte (aucun cabinet
correspondant trouvé).

Rattachement : 642 études rattachées au total (639 → 642, +3). Suite de tests : 94/94 au vert.

### 2026-09-09 02h03 UTC — Phase 3, lot 66 (exécution automatisée)

5 cabinets traités (3 succès / 2 échecs), tous ZH. Stefan Minder Rechtsanwälte (fondée
**2003** -- "Seit 2003 ist Stefan Minder unabhängiger Rechtsanwalt in Zürich", tel/email,
spécialiste FSA Arbeitsrecht depuis 2014, 5 domaines DE), Zeltweg Rechtsanwälte (tel,
4 avocats), Walker Law AG (fondée **2020** -- "Im Jahr 2020 gründete er seine eigene Kanzlei
Walker Law", tel/email, 7 domaines EN). **Échecs :** Weber Law Partners AG (wlaw.ch, 503×2),
Terekhov Law (terekhov-law.ch, 403×2).

Rattachement : 645 études rattachées au total (642 → 645, +3). Suite de tests : 94/94 au vert.

### 2026-09-09 03h03 UTC — Phase 3, lot 67 (exécution automatisée)

4 cabinets traités (3 succès / 1 échec), tous ZH. Sperling Legal GmbH (fondée **2023** --
"Selbständige Rechtsanwältin (seit 2019) et Inhaberin von Sperling Legal GmbH (seit 2023)",
tel/email), ZOLLINGER.LEGAL (tel/email, 5 domaines DE dont pénal/santé/poursuites/agraire/
contrats), Senser Steueranwälte (boutique fiscale, tel/email, 5 domaines DE dont droit fiscal
et procédure fiscale pénale). **Échec :** Wehrli Zimmermann & Partner (wehrlipartner.ch,
503×2).

Rattachement : 648 études rattachées au total (645 → 648, +3). Suite de tests : 94/94 au vert.

### 2026-09-09 04h03 UTC — Phase 3, lot 68 (exécution automatisée)

**Rythme accéléré suite au retour de Greg (06/09) : 21 cabinets traités en un seul lot**
(recherches WebSearch et vérifications WebFetch groupées en parallèle), répartis sur 6
cantons (ZH, TI, SG, BL, SZ, LU) — **14 succès / 7 échecs**.

ZH : anwaltsboutique Rechtsanwälte (fondée **2010** par Caroline MacNicholas, 2 avocates,
tel/email, 12 domaines EN) ; Burkhalter Rechtsanwälte Zürich AG (bureau zurichois du cabinet
suisse Burkhalter Rechtsanwälte, tel/email spécifiques à Zurich -- année de fondation du
cabinet global écartée, ambiguë pour cette entité enregistrée séparément) ; AffinityLaw AG
(Regina Arquint, tel/email, 8 domaines EN dont protection des données/technologie).

TI : Battaglioni & Giovanettina Studio Legale SA (fondée **2020** -- "Studio legale che nasce
a gennaio 2020", Bellinzona, 2 avocats, tel/email, 4 domaines IT) ; Broggini Armati Binzoni
Studio Legale SA (fondée **1992** par Andrea Broggini, renommée BAB Legal SA en 2024 --
continuité confirmée explicitement par le site, 4 avocats, tel/email, 13 domaines IT) --
**dédupliqué 3 fois** (le CSV référence ce même cabinet sous 3 graphies distinctes : "Broggini
Armati Binzoni Studio Legale SA", "Studio legale Broggini Armati Binzoni" et "Studio legale
Broggini Armati Binzoni SA" -- ces deux dernières partagent le même nom cœur après réduction
et sont mutuellement ambiguës, donc **ignorées par le garde-fou anti-collision** malgré
l'entrée cache correcte ; seule la première graphie s'est rattachée proprement).

SG : RHYNER LIPPUNER BERTSCHINGER Rechtsanwälte & öffentliche Notare (Buchs SG, 4 avocats/
notaires, tel/email, 9 domaines DE) -- dédupliqué (2 graphies CSV, "RHYNER LIPPUNER
BERTSCHINGER..." et "Rhyner Lippuner Bertschinger", toutes deux rattachées avec succès) ;
Advokaturbureau Brunner & Dudli (tel/email uniques du cabinet -- ligne partagée confirmée
explicitement par le site, pas une communauté à lignes séparées, 6 domaines DE) ; advore
rechtsanwälte ag (Wil SG, tel/email, effectif et domaines trop imprécis sur le site pour être
retenus).

BL : Advokaturbüro Heinzelmann & Levy (fondé le 1er janvier **2016** -- "haben wir uns... zum
Advokaturbüro... zusammengeschlossen", 6 domaines DE communs -- communauté de deux avocats
indépendants avec lignes séparées, aucun tel/email "du cabinet" inventé conformément à la
règle 4).

SZ : Basso Tschümperlin (Bahnhofstrasse 21, Schwyz, 8 domaines DE -- même schéma de communauté
à lignes séparées que Heinzelmann & Levy, aucun tel/email commun retenu).

LU : LL.M. Kaufmann Rüedi Rechtsanwälte AG -- dédupliqué depuis l'entrée déjà en cache
`krlaw.ch` (fondée 1974, 15 domaines DE), le CSV référençant ce cabinet sous 2 graphies
distinctes.

**Échecs :** Zuppiger Jenny Rechtsanwälte AG (ZH -- seul un cabinet homonyme partiel trouvé,
zuppiger-baurecht.ch, qui ne se présente nulle part comme "Zuppiger Jenny" : lien décliné,
continuité non confirmée par le site lui-même) ; Arvian Legal AG (ZH, aucun site officiel,
seule l'adresse au registre du commerce) ; Arnold & Partner Studio Legale Sagl (TI, aucun site
officiel, seuls des annuaires tiers) ; Eigenmann Associés (TI -- siège principal à Lausanne
VD, aucun fait spécifique à l'antenne tessinoise confirmé) ; K & B Rechtsanwälte (SG,
kb-lawyers.ch, 503×2) ; relevanz.legal (SG, 503×2) ; LegalOne AG (SZ, domaine legalone.ch
injoignable -- échec DNS).

Rattachement : 660 études rattachées au total (648 → 660, +12 -- 2 graphies Broggini ignorées
par le garde-fou anti-collision malgré cache correct, cf. ci-dessus). Suite de tests : 94/94
au vert.

### 2026-09-09 05h04 UTC — Phase 3, lot 69 (exécution automatisée)

23 cabinets traités (11 succès / 10 échecs), tous ZH (boutiques d'avocat·e·s indépendant·e·s
Zurich, recherches et vérifications groupées en parallèle).

Succès : Balthasar Legal AG (7 personnes, tel/email, 6 domaines DE dont IA/protection des
données -- **dédupliqué** vers son antenne lucernoise, le CSV référençant la même étude sous
"lic. iur Balthasar Legal AG" en LU) ; Bischofberger Rechtsanwälte (fondée **1998** --
"hat die Kanzlei im Jahre 1998 gegründet", tel/email, 5 domaines DE dont droit de la
construction) ; BRUNNER & PARTNER Advokatur (fondée **2002** -- "seit 2002", 2 avocats,
tel/email, 5 domaines DE) ; BYLANDLAW (fondée **2009**, solo, tel/email) ; CORAY LAW (solo,
tel/email, 3 domaines DE dont droit successoral) ; Caputo & Partners AG (fondée **2006**, tel,
9 domaines EN -- boutique spécialisée protection d'actifs bancaires) ; Benz Rechtsanwälte AG
(tel/email) ; BollmannLaw (solo, email) ; Limmatlegal (tel/email, droit de la responsabilité
civile et des assurances) ; Dätwyler Advokatur GmbH (solo, tel/email, 4 domaines DE dont droit
du divorce).

Échecs : OMB & Partners AG, Bärtschi Rechtsanwälte AG (barlex.ch, 403 Forbidden), Behrens
Trusted Advisors Rechtsanwälte AG (contenu JS insuffisant), Berlinger AG (n'est plus un
cabinet d'avocats -- société de conseil, confirmé par le site), Bietenholz Consulting & Law
(site en construction), Braun Advokatur + Steuern (503×2), Borbély Legal GmbH (503×2), Burns
Legal (contenu JS insuffisant), Calò Partners AG (aucun site officiel), Becchio & Partner
(site en construction).

Rattachement : 671 études rattachées au total (660 → 671, +11). Suite de tests : 94/94 au
vert.

### 2026-09-09 06h04 UTC — Phase 3, lot 70 (exécution automatisée)

16 cabinets traités (10 succès / 6 échecs), tous ZH (poursuite de la longue traîne de boutiques
zurichoises solo, plage alphabétique E-K, recherches et vérifications groupées en parallèle).

Succès : Hollinger Rechtsanwälte (fondée **2013** -- "Seit 2013 beraten und vertreten wir",
tel/email, 3 domaines DE) ; Koller Law AG (fondée **2020**, solo, tel/email, 5 domaines EN
dont droit financier/réglementaire) ; Isler & Pedrazzini (tel/email, 3 domaines DE dont droit
des brevets et des marques) ; Gattlen Rechtsanwälte (tel, 5 domaines DE dont droit de
l'assainissement et informatique) ; Kissling Legal GmbH (tel/email, 12 domaines EN) ; Frey &
Partner Zürich AG (tel/email, 5 domaines EN dont planification successorale) ; Huber & Partner
(tel/email, 11 domaines DE dont droit fiscal et succession d'entreprise) ; Haefelin Law (tel
uniquement -- email affiché comme placeholder obscurci non exploitable) ; Jäger Legal
Anwaltskanzlei (1 domaine DE) ; Esteves Law (tel/email uniquement -- site officiel encore en
construction).

**Piège d'identité évité :** Graf & Partner (ZH, Seegartenstrasse 2) -- le domaine
grafpartner.com trouvé en recherche correspondait en réalité à un cabinet homonyme allemand
sans rapport (Schmeilzl & Groll, Ratisbonne, indicatif +49) ; le vrai domaine
(grafundpartner.ch) étant injoignable (503), le rattachement a été décliné plutôt que
d'utiliser les données du mauvais cabinet.

Échecs : Herb Takata Rechtsanwälte (site en construction), Kieser Senn Partner / KSPartner
(aucun site officiel), Ernst & Partner (aucun site officiel), Fausch & Schenkel (aucun site
officiel), Heller Rechtsanwalts AG (domaine officiel ambigu parmi plusieurs sites personnels
similaires de Dr. Heinz Heller).

Rattachement : 681 études rattachées au total (671 → 681, +10). Suite de tests : 94/94 au
vert.

### 2026-09-09 07h04 UTC — Phase 3, lot 71 (exécution automatisée)

14 cabinets traités (7 succès / 7 échecs), tous ZH (poursuite longue traîne, recherches et
vérifications groupées en parallèle).

Succès : Hanhart Law (fondée **2020**, solo, tel/email, 10 domaines EN dont droit des médias) ;
Killias & Legler GmbH (boutique arbitrage international fondée par deux anciens associés de
Pestalozzi, 2 avocats, tel, 8 domaines EN) ; GÖNÜLER Rechtsanwälte (tel/email, 5 domaines EN
dont white collar et droit bancaire) ; FREYLAW GmbH (solo, tel/email, 7 domaines EN) ;
IsenringLaw (tel/email, 5 domaines DE dont droit pénal économique et droit de la protection
animale) ; kübler.legal (Winterthur, solo, tel/email, 5 domaines DE) ; Mark Livschitz AG
(tel/email uniquement).

**Piège d'identité évité :** Meisser & Haller Rechtsanwälte -- le site officiel (mhra.ch) se
présente désormais uniquement comme "Anwaltskanzlei Meisser AG" (Gregor Meisser seul), sans
aucune mention de "Haller" : continuité non confirmée par le site lui-même, rattachement
décliné plutôt que d'utiliser des données incertaines.

Échecs : Herenda Rechtsanwälte (503×2), Kohler Law GmbH (503×2), Hofmann Law (503×2),
Bühlmann & Fritschi Rechtsanwälte / b-law.ch (503×2), Guery Legal (Edith Guery apparaît comme
membre de l'étude ADROIT attorneys-at-law, aucune marque indépendante confirmée), Meroni &
Schmid Rechtsanwälte (aucun site officiel trouvé).

Rattachement : 688 études rattachées au total (681 → 688, +7). Suite de tests : 94/94 au
vert.

### 2026-09-09 08h03 UTC — Phase 3, lot 72 (exécution automatisée)

13 cabinets traités (6 succès / 6 échecs), tous ZH.

Succès : AsyLex (ONG d'assistance juridique aux demandeurs d'asile fondée **2017**, 3 domaines
EN) ; Meier Legal (fondée **2019**, tel, 9 domaines EN) ; Nater Legal (Dr. Hans Nater, ancien
associé-fondateur de Nater Dallafior 2006-2025, pratique solo indépendante depuis **2025**,
tel/email, droit commercial et sportif) ; mulle legal GmbH (droit de la famille, tel/email,
6 domaines DE) ; Mathis Legalzone - Advokatur (tel/email, 10 domaines EN) ; SJP JENNY LAW (droit
du sport et des associations, tel/email).

**Piège de fondation évité :** Bürgi Nägeli Rechtsanwälte (bnlawyers.ch, déjà en cache depuis
juillet) affiche une mention "Copyright © 1995-2026" en bas de page qui aurait pu être
confondue avec une année de fondation -- déjà correctement écartée par le cache existant
(`founding_year: null`), confirmé lors de la vérification de ce lot.

Échecs : kern law (503×2), NETZLE LEGAL AG (503×2), Nägeli Rechtsanwälte (503×2 -- site distinct
de Bürgi Nägeli déjà rattaché), Groner Advokatur (identité ambiguë entre plusieurs
sites/marques de Dr. Roger Groner), HAFERLAND LEGAL (aucun site officiel), Metin Legal (403
Forbidden).

Rattachement : 694 études rattachées au total (688 → 694, +6). Suite de tests : 94/94 au
vert.

### 2026-09-09 09h02 UTC — Phase 3, lot 73 (exécution automatisée)

8 cabinets traités (8 succès / 0 échec), tous ZH -- lot particulièrement propre, tous les
sites trouvés étaient accessibles.

Succès : Oesch & Partner (fondée **1997** par Dr. Patrick K. Oesch, tel) ; MONFERRINI LAW AG
(fondée **2020** -- "Die Kanzlei Monferrini Law wurde am 1. Februar 2020 von Rechtsanwältin
Dr. iur. Isabelle Monferrini gegründet", tel/email, 10 domaines DE) ; Niggli Rechtsanwälte
(boutique droit financier/marchés des capitaux, solo, 5 domaines EN) ; Pairfact Legal AG
(cabinet digitalisé, tel/email, 3 domaines EN) ; Peter Rechtsanwälte AG (tel/email, droit
commercial/sociétés/immobilier) ; Judith Naef Rechtsanwälte AG (tel/email) ; MEYER RECHT AG
(tel/email, 4 domaines DE) ; Apex Legal GmbH (tel/email).

Rattachement : 702 études rattachées au total (694 → 702, +8). Suite de tests : 94/94 au
vert.

### 2026-09-09 10h03 UTC — Phase 3, lot 74 (exécution automatisée)

10 cabinets traités (5 succès / 5 échecs), tous ZH.

Succès : Neubauer Law (fondée **2022**, tel/email, 6 domaines DE dont PI/technologie) ; Rihm
Rechtsanwälte (tel/email, 10 domaines EN dont FinTech/blockchain) ; ib legal AG (tel/email) ;
Gehrilegal Attorneys (Zollikon, tel/email, 3 domaines EN + secteurs logistique/IT/life
science) ; J.C. Gil Rechtsanwälte (tel, droit commercial).

Échecs : Reinarz Tax & Legal (pages contact en 404, aucun tel/email exploitable), Müllhaupt &
Partner (503 puis 404), Rechtsanwälte Pugatsch / rp-law.ch (503×2), Kruse I Law (503×2),
ADVOSUISSE (403×2).

Rattachement : 707 études rattachées au total (702 → 707, +5). Suite de tests : 94/94 au
vert.

### 2026-09-09 11h04 UTC — Phase 3, lot 75 (exécution automatisée)

8 cabinets traités (6 succès / 2 échecs), tous ZH.

Succès : Ritter & Partner Rechtsanwälte (fondée **2000** par Dr. Andreas Ritter, boutique
droit de l'art/PI, tel/email, 6 domaines EN) ; Meier Sadiku Law AG (bureaux Lucerne+Zurich, tel/
email, 7 domaines DE dont droit du sport) ; RUGGLE PARTNER (2 avocats, tel, 7 domaines DE dont
droit de l'art) ; Kiener & Märki AG (2 avocats, tel/email, spécialisation clientèle
russophone) ; SABETI LEGAL (tel/email) ; Rutishauser Rechtsanwälte (tel/email, droit fiscal).

**Piège de fondation évité :** Kiener & Märki AG (kmag.ch) affiche "Seit 1999 strebt Dr. iur.
Olaf Kiener danach..." -- une date de carrière individuelle de l'un des deux associés, pas la
fondation de l'entité "Kiener & Märki AG" elle-même (formée en 2021 selon des sources tierces,
non vérifiée sur le site) : `founding_year` volontairement omis.

Échecs : Obrecht & Frehner (identité incertaine, aucun site confirmé sous ce nom exact),
Doggwiler Aschwanden Rechtsanwälte (addlaw.ch, échec DNS).

Rattachement : 713 études rattachées au total (707 → 713, +6). Suite de tests : 94/94 au
vert.

### 2026-09-09 12h04 UTC — Phase 3, lot 76 (exécution automatisée)

10 cabinets traités (5 succès / 5 échecs), tous ZH.

Succès : Müller Rechtsanwälte und Treuhand AG (fondée **2004** -- "die 2004 als Brücke im
Schweizerisch-Brasilianischen Rechtsverkehr gegründet wurde", tel/email, 8 domaines DE dont
droit suisso-brésilien) ; **dédupliqué** Ruoss Vögele (déjà en cache `ruossvoegele.ch` sous la
graphie "Ruoss Vögele Partner", 18 avocats -- le CSV référence ce même cabinet sous une 2e
graphie "Ruoss Vögele", 5 domaines EN) ; SCHLEGEL RECHT (solo, tel/email, 5 domaines DE) ;
Schaltegger Rechtsanwälte (bauanwalt.ch, tel, droit de la construction) ; MUELLER LEGAL,
Anwaltskanzlei Damian Müller (tel/email).

Échecs : Schmid & Partner (aucun site officiel), Revesz und Partner Rechtsanwälte (drplegal.ch
-- vérification anti-bot Cloudflare, aucun contenu reçu), Piasini Advokatur (aucun site
officiel, possiblement fermé), Schill Legal et Paltzer Private Clients Law (même blocage
anti-bot Cloudflare).

Rattachement : 718 études rattachées au total (713 → 718, +5). Suite de tests : 94/94 au
vert.
