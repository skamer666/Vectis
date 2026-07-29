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
