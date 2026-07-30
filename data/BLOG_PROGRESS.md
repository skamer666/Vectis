# Blog juridique | journal de bord et liste des 50 sujets

Ce fichier est la mémoire du chantier "blog" entre deux sessions/lots de rédaction.
À lire avant de reprendre la rédaction : contient la liste des 50 sujets validés
par Greg le 30/07/2026, leur état (rédigé / à rédiger / traduit), et les décisions
qui encadrent ce chantier.

## Décisions actées le 30/07/2026 (ne pas redemander)

- Section intégrée au site (`/blog/`), pas des documents livrés à part.
- 4 langues (FR/DE/IT/EN), mais rédaction en français d'abord, par lots de 10,
  traduction dans un second temps (voir tâche "Traduire les 50 articles").
- Liste des 50 sujets validée telle quelle par Greg avant rédaction complète,
  ne pas la modifier sans repasser par lui.
- Même principe de non-fabrication que les guides existants : sources légales
  citées explicitement (CO, CC, CP, CPC, CPP, LCR, LP, LEI, LDIP, LAT, etc.),
  aucun chiffre inventé, contenu informatif général (pas un conseil juridique
  individualisé).
- 2 articles par domaine de droit, sur les 25 domaines déjà référencés par le
  site (`i18n.DOMAINES`), ce qui assure un maillage naturel avec les hubs domaines.
- Format cible : 800-1200 mots par article, FAQ courte en fin d'article avec
  schema markup FAQPage (même mécanisme que les guides).

## Liste des 50 sujets (id technique = clé dans blog_content.BLOG_ARTICLES)

Statut : ✅ rédigé FR+DE+IT+EN · 🟡 rédigé FR seulement · ⬜ pas encore rédigé

| # | Domaine | Titre (FR) | Base légale | Statut |
|---|---|---|---|---|
| 1 | Droit du travail | Licenciement en Suisse : délais de préavis et protection contre le congé abusif | CO art. 335-337c | ✅ `licenciement-delais-conge-abusif` |
| 2 | Droit du travail | Heures supplémentaires, salaire et vacances : vos droits selon le CO | CO art. 321c, 329a | 🟡 `heures-supplementaires-salaire-vacances` |
| 3 | Droit de la famille | Autorité parentale et garde des enfants après une séparation | CC art. 296-301a | 🟡 `autorite-parentale-garde-enfants` |
| 4 | Droit de la famille | Pension alimentaire : comment elle est calculée en Suisse | CC art. 285 | 🟡 `pension-alimentaire-calcul` |
| 5 | Droit du divorce | Divorce en Suisse : procédure, délais et divorce par consentement mutuel | CC art. 111-114 | 🟡 `divorce-procedure-delais` |
| 6 | Droit du divorce | Partage du 2e pilier en cas de divorce | CC art. 122-124 | 🟡 `partage-deuxieme-pilier-divorce` |
| 7 | Droit pénal | Casier judiciaire suisse : inscription, consultation et radiation | Loi sur le casier judiciaire (VOSTRA) | 🟡 `casier-judiciaire-suisse` |
| 8 | Droit pénal | Ordonnance pénale : que faire si vous en recevez une | CPP art. 352-356 | 🟡 `ordonnance-penale-opposition` |
| 9 | Droit du bail | Résiliation du bail : délais, formulaire officiel et contestation | CO art. 266-273 | 🟡 `resiliation-bail-delais-contestation` |
| 10 | Droit du bail | Contester une augmentation de loyer | CO art. 269-270e | 🟡 `contester-augmentation-loyer` |
| 11 | Droit de la construction | Défauts de construction : garantie et délais de réclamation | CO art. 367-371 | 🟡 `defauts-construction-garantie-delais` |
| 12 | Droit de la construction | Hypothèque légale des artisans et entrepreneurs | CC art. 837-841 | 🟡 `hypotheque-legale-artisans-entrepreneurs` |
| 13 | Droit des successions | Réserve héréditaire et quotité disponible depuis la révision de 2023 | CC art. 470-475 | 🟡 `reserve-hereditaire-quotite-disponible` |
| 14 | Droit des successions | Rédiger un testament valable en droit suisse | CC art. 498-508 | 🟡 `rediger-testament-valable` |
| 15 | Droit des contrats | Résilier un contrat pour justes motifs | CO (règles générales) | 🟡 `resilier-contrat-justes-motifs` |
| 16 | Droit des contrats | Clause pénale et dommages-intérêts contractuels | CO art. 160-163 | 🟡 `clause-penale-dommages-interets` |
| 17 | Droit des sociétés | Créer une Sàrl en Suisse : capital, statuts, formalités | CO art. 772 ss | 🟡 `creer-sarl-suisse` |
| 18 | Droit des sociétés | Responsabilité des administrateurs de société anonyme | CO art. 754-755 | 🟡 `responsabilite-administrateurs-sa` |
| 19 | Droit de la circulation routière | Retrait de permis : durées selon la gravité de l'infraction | LCR art. 16-16c | 🟡 `retrait-permis-duree-infraction` |
| 20 | Droit de la circulation routière | Accident de la route : qui paie et comment déclarer le sinistre | LCR / LCA | 🟡 `accident-route-qui-paie-declaration` |
| 21 | Droit administratif | Recours contre une décision administrative : délais et procédure | PA / lois cantonales | 🟡 `recours-decision-administrative-delais` |
| 22 | Droit administratif | Marchés publics : droits des soumissionnaires évincés | AIMP / LMP | 🟡 `marches-publics-soumissionnaires-evinces` |
| 23 | Droit des étrangers | Permis de séjour B, C, L : conditions et différences | LEI | 🟡 `permis-sejour-b-c-l-conditions` |
| 24 | Droit des étrangers | Regroupement familial : faire venir sa famille en Suisse | LEI art. 42-52 | 🟡 `regroupement-familial-faire-venir-famille` |
| 25 | Droit des assurances | Assurance perte de gain maladie : droits et délai de carence | LCA | 🟡 `assurance-perte-gain-maladie-carence` |
| 26 | Droit des assurances | Contester une décision de l'assurance invalidité | LPGA art. 52 | 🟡 `contester-decision-assurance-invalidite` |
| 27 | Responsabilité civile | Qui est responsable et comment être indemnisé | CO art. 41 ss | 🟡 `responsabilite-civile-indemnisation` |
| 28 | Responsabilité civile | Responsabilité du détenteur d'animal et du propriétaire immobilier | CO art. 56, 58 | 🟡 `responsabilite-detenteur-animal-proprietaire` |
| 29 | Poursuites et faillite | Commandement de payer : comment faire opposition | LP art. 69-74 | 🟡 `commandement-payer-opposition` |
| 30 | Poursuites et faillite | Faillite personnelle : procédure et conséquences | LP art. 171 ss | 🟡 `faillite-personnelle-procedure-consequences` |
| 31 | Protection de l'enfant et de l'adulte | Curatelle : quand et comment elle est prononcée | CC art. 390-398 | ⬜ |
| 32 | Protection de l'enfant et de l'adulte | Mandat pour cause d'inaptitude : anticiper sa propre incapacité | CC art. 360-369 | ⬜ |
| 33 | Droit fiscal | Contester une décision de taxation : réclamation et délais | LIFD art. 132 | ⬜ |
| 34 | Droit fiscal | Imposition à la source : qui est concerné et comment ça marche | LIFD art. 83-101 | ⬜ |
| 35 | Droit bancaire | Secret bancaire suisse : ce qu'il protège encore aujourd'hui | LB | ⬜ |
| 36 | Droit bancaire | Litige avec sa banque : ombudsman et voies de recours | Ombudsman des banques suisses | ⬜ |
| 37 | Droit médical | Erreur médicale : comment faire valoir ses droits | CO art. 41 / droit cantonal | ⬜ |
| 38 | Droit médical | Consentement éclairé du patient : droits et obligations du médecin | CC / droit cantonal de la santé | ⬜ |
| 39 | Propriété intellectuelle | Protéger une marque en Suisse : dépôt auprès de l'IPI | LPM | ⬜ |
| 40 | Propriété intellectuelle | Droit d'auteur : durée de protection et exceptions | LDA | ⬜ |
| 41 | Droit international privé | Reconnaissance d'un divorce prononcé à l'étranger | LDIP | ⬜ |
| 42 | Droit international privé | Quel droit s'applique à un contrat international | LDIP | ⬜ |
| 43 | Procédure civile | Conciliation obligatoire avant un procès civil | CPC art. 197-212 | ⬜ |
| 44 | Procédure civile | Frais de justice et dépens : qui paie en cas de procès | CPC art. 95-111 | ⬜ |
| 45 | Procédure pénale | Être entendu comme prévenu : vos droits pendant l'audition | CPP art. 157-158 | ⬜ |
| 46 | Procédure pénale | Plainte pénale : délais et différence avec la dénonciation | CP art. 30-33 | ⬜ |
| 47 | Médiation | Médiation familiale : quand et pourquoi y recourir | CPC art. 214-218 | ⬜ |
| 48 | Médiation | Médiation commerciale : alternative au procès pour les entreprises | n/a | ⬜ |
| 49 | Aménagement du territoire | Permis de construire : procédure et opposition des voisins | LAT / droit cantonal | ⬜ |
| 50 | Aménagement du territoire | Zone à bâtir et hors zone à bâtir : ce que ça change pour un terrain | LAT | ⬜ |

## Journal des sessions

### 2026-07-30 | Lancement : architecture + article pilote

- Architecture blog créée : `blog_content.py`, `gen_blog()` dans `build.py`,
  templates `blog_index.html`/`blog_article.html`, segment URL "blog" et
  chaînes UI (`blog_title`, `blog_intro`, `all_blog_articles`) ajoutés dans
  `i18n.py`.
- `gen_blog()` tolère les articles partiellement traduits (seules les langues
  présentes dans `BLOG_ARTICLES[id]` sont générées), ce qui permet une mise en ligne
  progressive par lots sans bloquer sur la traduction.
- 1 article pilote rédigé et vérifié dans les 4 langues : "Licenciement en
  Suisse" (droit du travail, CO art. 335-337c). Choisi comme pilote pour
  valider le format de bout en bout avant de lancer les 49 restants.
- 6 nouveaux tests (`tests/test_blog.py`) : structure des données, unicité des
  slugs, absence d'em dash, absence d'artefact Jinja dans les pages générées.
  56 tests au total, tous au vert.
- Build vérifié : pages FR/DE/IT/EN générées, hreflang correct, aucun noindex
  (signal réel présent dès le premier article), schema FAQPage présent.
- **Reste à faire** : rédiger les 49 sujets restants en français (par lots de
  10, voir tâche dédiée), puis traduire l'ensemble en DE/IT/EN.

### 2026-07-30 | Lot 1 complet : articles 2 à 10 (FR)

- 9 articles rédigés en français et intégrés à `blog_content.py` : heures
  supplémentaires/salaire/vacances (CO art. 321c, 329a), autorité parentale
  et garde (CC art. 296-301a), pension alimentaire (CC art. 285), procédure
  de divorce (CC art. 111-115), partage du 2e pilier (CC art. 122-124b),
  casier judiciaire (loi VOSTRA), ordonnance pénale (CPP art. 352-356),
  résiliation du bail (CO art. 264-273), contestation d'augmentation de
  loyer (CO art. 269-270b).
- Lot 1 (articles 1 à 10) donc complet en français : 10/50 sujets rédigés,
  tous rattachés à leur hub de domaine, maillage interne entre articles du
  même domaine actif.
- 57 tests passés (aucun em dash, aucun artefact Jinja, structure de données
  valide, slugs uniques). Titres tous sous 60 caractères hors suffixe
  " | Legatis".
- Toutes les langues DE/IT/EN restent à faire (tâche dédiée #28), FR-only
  pour l'instant conformément au plan par lots.
- Prochaine étape : lot 2 (articles 11 à 20, à partir de la liste ci-dessus).

### 2026-07-30 | Lot 2 complet : articles 11 à 20 (FR)

- 10 articles rédigés en français : défauts de construction (CO art. 367-371),
  hypothèque légale des artisans (CC art. 837-841), réserve héréditaire post-
  révision 2023 (CC art. 470-475), rédaction d'un testament (CC art. 498-508),
  résiliation pour justes motifs (principe jurisprudentiel), clause pénale
  (CO art. 160-163), création d'une Sàrl (CO art. 772 ss), responsabilité des
  administrateurs de SA (CO art. 754-755), retrait de permis (LCR art. 16-16c),
  accident de la route (LCR/LCA).
- 20/50 sujets rédigés en français. 57 tests toujours au vert, aucun em dash,
  aucun artefact Jinja, titres tous sous 60 caractères.
- Prochaine étape : lot 3 (articles 21 à 30).

### 2026-07-30 | Lot 3 complet : articles 21 à 30 (FR)

- 10 articles rédigés en français : recours administratif (PA art. 50, 55),
  marchés publics (AIMP/LMP), permis de séjour B/C/L (LEI), regroupement
  familial (LEI art. 42-52), assurance perte de gain maladie (LCA, art. 324a
  CO), contestation de décision AI (LPGA art. 52), responsabilité civile
  générale (CO art. 41, 60), responsabilité du détenteur d'animal et du
  propriétaire d'ouvrage (CO art. 56, 58), commandement de payer (LP art.
  69-74), faillite personnelle (LP art. 171 ss).
- Attention particulière portée à la non-fabrication sur les délais de
  recours en marchés publics et sur les durées de séjour pour le permis C
  (fortement variables selon nationalité/accords bilatéraux) : formulations
  volontairement générales plutôt qu'un chiffre précis non garanti exact
  dans tous les cas.
- 30/50 sujets rédigés en français. 57 tests toujours au vert, aucun em
  dash, aucun artefact Jinja, titres tous sous 60 caractères.
- Prochaine étape : lot 4 (articles 31 à 40).
