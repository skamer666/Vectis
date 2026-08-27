"""Trois calculateurs juridiques gratuits, deterministes, bases sur des
articles de loi federaux codifies (pas de recherche jurisprudentielle
requise, contrairement au simulateur d'assistance judiciaire de
calc_widget.py). Meme principe de non-fabrication : chaque regle utilisee
ici a ete verifiee directement dans le texte de loi ou via une source
secondaire fiable citant ce texte mot pour mot, jamais depuis la seule
memoire du modele.

Sources verifiees (aout 2026) :
- Art. 104 CO : taux d'interet moratoire legal de 5% l'an sauf convention
  contraire (verifie via juriup.ch, qui cite le texte de l'art. 104 CO).
- Art. 127 CO : prescription generale de 10 ans.
- Art. 60 CO : prescription de l'action pour acte illicite, delai relatif
  de 3 ans des la connaissance du dommage et de la personne qui en est
  l'auteur, delai absolu de 20 ans des le jour de l'acte dommageable
  (delai absolu porte de 10 a 20 ans par la revision entree en vigueur le
  1.1.2020 ; verifie via wg-avocats.ch).
- Art. 128 CO : prescription de 5 ans pour certaines creances periodiques
  (loyers, interets de capitaux, salaires, etc.), non modifiee par la
  revision de 2020.
- Art. 97 CP : prescription de l'action penale, delais absolus (non
  interrompus depuis la revision de 2014) : 30 ans (peine privative de
  liberte a vie), 15 ans (peine de plus de 3 ans), 10 ans (peine de 3 ans
  au plus), 7 ans (autres delits), et 3 ans pour les contraventions
  (art. 109 CP) ; verifie via juriup.ch, qui cite le texte de l'art. 97 CP.
- Art. 142 al. 1 CPC : un delai declenche par une communication court des
  le lendemain de celle-ci.
- Art. 142 al. 3 CPC : si le dernier jour est un samedi, un dimanche ou un
  jour ferie reconnu par le droit federal ou cantonal du siege du
  tribunal, le delai expire le premier jour ouvrable qui suit.
- Art. 145 al. 1 CPC : feries judiciaires, trois periodes : du 7e jour
  avant Paques au 7e jour apres Paques inclus ; du 15 juillet au 15 aout
  inclus ; du 18 decembre au 2 janvier inclus.
- Art. 145 al. 2 CPC : la suspension des delais ne s'applique pas a la
  procedure de conciliation ni a la procedure sommaire.
(Art. 142 et 145 CPC verifies via app.zpo-cpc.ch, plateforme de commentaire
en ligne du CPC citant le texte legal.)

Limites assumees et signalees a l'utilisateur dans chaque outil : le
calculateur de delai de procedure ne verifie que le week-end et le 1er
aout (seul jour ferie officiellement federal, art. 20a LTr) -- les jours
feries cantonaux et communaux, non uniformes a l'echelle du pays, ne sont
pas inclus et doivent etre verifies separement. Le calculateur de
prescription ne tient pas compte des causes de suspension ou
d'interruption (art. 134 a 138 CO, dispositions correspondantes du CP).
Aucun de ces trois outils ne remplace une consultation d'avocat.

Sources verifiees pour les 10 outils ajoutes le 2026-08-27 (demande de
Gregoire Giuliano, deduites des recherches SEO -- chaque source citee a
ete recuperee via WebFetch/WebSearch, jamais depuis la seule memoire du
modele) :
- OAO (ordonnance sur les amendes d'ordre), bareme des amendes vitesse :
  verifie via ff-law.ch (bussentabelle 2026) ET juriup.ch (tableau
  autoroute), les deux sources concordent exactement sur les montants
  autoroute (20/60/120/180/260 CHF) -- confiance elevee (deux sources
  independantes).
- Art. 16a/16b/16c LCR, seuils infraction legere/moyenne/grave : verifie
  via recherche croisee (seuil "infraction grave" = 25 km/h en localite,
  30 km/h hors localite, 35 km/h autoroute ; le seuil de denonciation
  penale -- ou l'amende d'ordre fixe cesse de s'appliquer -- coincide
  avec le bas de la fourchette "infraction moyenne", verifie via
  juriup.ch : 16 km/h en localite, 21 km/h hors localite, 26 km/h
  autoroute).
- Art. 90 al. 3-4 LCR, delit de chauffard : seuils verifies via ff-law.ch
  (+40 km/h en zone 30, +50 km/h en zone 50, +60 km/h hors localite,
  +80 km/h autoroute) -- peine privative de liberte d'au moins un an,
  retrait du permis d'au moins deux ans. Le calculateur applique la
  version zone 50/80/120 (cas standard) et signale que les zones 30 et
  semi-autoroutes ont des seuils differents non couverts.
- Art. 266c/266d CO, delais de conge du bail : delai minimal de 3 mois
  pour un logement, 6 mois pour un local commercial, pour le prochain
  terme legal ou contractuel -- verifie par recherche croisee (mobiliere.ch
  et sources juridiques concordantes). Le prochain terme lui-meme (usages
  locaux cantonaux) n'est PAS invente ni suppose : l'outil ne verifie que
  le respect du delai minimal avant la date choisie par l'utilisateur.
- Art. 262 CO, sous-location : consentement ecrit du bailleur obligatoire,
  motifs de refus limitatifs (art. 262 al. 2 CO), loyer de sous-location
  abusif si disproportionne par rapport au bail principal (majoration de
  20% admise pour un logement meuble selon l'ATF 119 II 353) -- verifie
  via recherche croisee.
- Art. 470/471 CC (Code civil, PAS le CO), reserve hereditaire depuis la
  revision entree en vigueur le 1.1.2023 : la reserve du conjoint/partenaire
  enregistre et des descendants est reduite a la moitie de leur part legale
  (etait les 3/4 avant 2023) ; les parents n'ont plus aucune reserve depuis
  cette revision -- verifie par recherche croisee (AXA, SwissLife, UBS,
  justis.ch, deinadieu.ch, tous concordants).
- Art. 16 OELP (ordonnance sur les emoluments percus en application de la
  LP), frais de commandement de payer : bareme degressif verifie
  directement dans le texte officiel en vigueur (fedlex.admin.ch, version
  au 1.1.2026, RO 2025 630) : 7 CHF jusqu'a 100 CHF de creance, 20 CHF
  jusqu'a 500 CHF, 40 CHF jusqu'a 1'000 CHF, 60 CHF jusqu'a 10'000 CHF,
  90 CHF jusqu'a 100'000 CHF, 190 CHF jusqu'a 1'000'000 CHF, 400 CHF
  au-dela. Une premiere recherche via juriup.ch avait donne un bareme
  different (7/20/40/70/200/400/800), visiblement obsolete depuis la
  revision entree en vigueur le 1.1.2026 -- confirme obsolete par
  cross-verification avec gerichtskostenrechner.ch (qui donne le bareme
  a jour) et le texte officiel lui-meme, source retenue en cas de
  divergence. Art. 68 LP : les frais sont avances par le createncier puis
  mis a la charge finale du debiteur.
- Art. 335b/335c CO, delai de conge du contrat de travail : 7 jours durant
  le temps d'essai (sans devoir tomber sur une fin de mois) ; hors essai,
  1 mois pendant la 1re annee de service, 2 mois de la 2e a la 9e annee,
  3 mois des la 10e annee, toujours pour la fin d'un mois sauf accord
  contraire -- verifie par recherche croisee (SECO, sources juridiques
  concordantes).
- Art. 20 et 22a PA (loi federale sur la procedure administrative), delais
  de recours administratif : memes regles que l'art. 142/145 CPC deja
  code ci-dessus (report au premier jour ouvrable si le delai echoit un
  samedi/dimanche/jour ferie ; memes trois periodes de feries que le CPC --
  7 jours avant/apres Paques, 15 juillet-15 aout, 18 decembre-2 janvier) --
  verifie via swissrights.ch qui cite le texte de l'art. 22a PA. Reutilise
  telle quelle la fonction feriesRanges() deja ecrite pour le CPC.
- Montants de base mensuels du minimum vital LP (Existenzminimum, art. 93
  LP) : 1200 CHF personne seule, 1350 CHF parent seul, 1700 CHF couple,
  +400 CHF par enfant de moins de 10 ans, +600 CHF par enfant de 10 ans ou
  plus -- Lignes directrices de la Conference des preposes aux poursuites
  et faillites de Suisse, verifie par recherche croisee (silgeneve.ch,
  fr.ch). Utilises uniquement dans l'estimateur de pension alimentaire
  (voir sa documentation specifique ci-dessous pour les limites assumees,
  plus importantes que pour les autres outils).

ATTENTION particuliere -- estimateur de pension alimentaire : contrairement
aux autres outils ci-dessus, il n'existe PAS de formule legale fixe pour
calculer une pension alimentaire en Suisse. Le Tribunal federal impose
depuis l'ATF 147 III 265 (2021) une methode en deux etapes (determination
du minimum vital de chacun, puis repartition de l'excedent), mais laisse
une large marge d'appreciation au juge sur les besoins concrets, le revenu
hypothetique et la repartition de l'excedent. Ce simulateur applique cette
methode de maniere simplifiee et illustrative, avec les montants de base
LP ci-dessus et une repartition "grandes tetes/petites tetes" presentee
comme une convention parmi d'autres, jamais comme une regle legale. Il ne
demande jamais de deviner un loyer, une prime d'assurance-maladie ou des
charges : ces montants sont toujours saisis par l'utilisateur lui-meme.
"""

import json

STRINGS = {
    "fr": {
        # --- Prescription ---
        "presc_heading": "Calculateur de délai de prescription",
        "presc_disclaimer": "Ce calculateur applique les délais légaux de base (art. 60, 127, 128 CO et 97 CP). Il ne tient pas compte des causes de suspension ou d'interruption de la prescription (art. 134 à 138 CO et dispositions correspondantes du CP), ni des cas particuliers. Le résultat est indicatif, pas un avis juridique.",
        "presc_type_label": "Type de créance ou d'infraction",
        "presc_opt_contrat": "Créance contractuelle générale (art. 127 CO, 10 ans)",
        "presc_opt_illicite": "Dommage résultant d'un acte illicite (art. 60 CO)",
        "presc_opt_periodique": "Créance périodique : loyers, intérêts, salaires (art. 128 CO, 5 ans)",
        "presc_opt_penal": "Infraction pénale (art. 97 CP)",
        "presc_date_exigible": "Date d'exigibilité de la créance",
        "presc_date_acte": "Date de l'acte dommageable",
        "presc_date_connaissance": "Date de connaissance du dommage et de son auteur",
        "presc_date_infraction": "Date de l'infraction",
        "presc_peine_label": "Peine maximale encourue",
        "presc_peine_vie": "Peine privative de liberté à vie (30 ans)",
        "presc_peine_plus3": "Peine privative de liberté de plus de 3 ans (15 ans)",
        "presc_peine_max3": "Peine privative de liberté de 3 ans au plus (10 ans)",
        "presc_peine_autre": "Autre délit (7 ans)",
        "presc_peine_contravention": "Contravention (art. 109 CP, 3 ans)",
        "presc_btn": "Calculer la prescription",
        "presc_result_prefix": "Date de prescription estimée : ",
        "presc_result_illicite_note": " (le plus proche des deux délais, relatif ou absolu, l'emporte)",
        "presc_source_contrat": "Base légale : art. 127 CO, délai de prescription général de 10 ans.",
        "presc_source_illicite": "Base légale : art. 60 al. 1 CO, délai relatif de 3 ans dès la connaissance du dommage et de l'auteur, délai absolu de 20 ans dès l'acte dommageable (délai porté de 10 à 20 ans par la révision entrée en vigueur le 1.1.2020).",
        "presc_source_periodique": "Base légale : art. 128 CO, délai de 5 ans pour les loyers, intérêts de capitaux et autres prestations périodiques, ainsi que pour les salaires et certaines autres créances énumérées par cette disposition.",
        "presc_source_penal": "Base légale : art. 97 CP. Depuis la révision entrée en vigueur en 2014, ces délais sont absolus et ne sont plus interrompus par des actes de procédure.",
        # --- Délai de procédure ---
        "delai_heading": "Calculateur de délai de recours ou de procédure",
        "delai_disclaimer": "Ce calculateur applique l'art. 142 CPC (point de départ, report en cas de week-end ou de jour férié fédéral) et l'art. 145 CPC (féries judiciaires). Il ne vérifie que le week-end et le 1er août, seul jour férié reconnu au niveau fédéral (art. 20a LTr) : les jours fériés cantonaux et communaux, propres au siège du tribunal, doivent être vérifiés séparément. Résultat indicatif, à confirmer avant tout acte de procédure important.",
        "delai_date_comm_label": "Date de la communication ou de l'événement déclencheur",
        "delai_jours_label": "Durée du délai (en jours)",
        "delai_procedure_label": "Type de procédure",
        "delai_opt_ordinaire": "Procédure ordinaire (les féries judiciaires s'appliquent)",
        "delai_opt_sommaire": "Procédure de conciliation ou sommaire (pas de féries, art. 145 al. 2 CPC)",
        "delai_btn": "Calculer l'échéance",
        "delai_result_prefix": "Le délai expire le : ",
        "delai_source": "Base légale : art. 142 al. 1 et 3 CPC (point de départ le lendemain de la communication, report au premier jour ouvrable suivant si le dernier jour tombe un week-end ou le 1er août) et art. 145 CPC (trois périodes de féries : du 7e jour avant Pâques au 7e jour après Pâques inclus, du 15 juillet au 15 août inclus, du 18 décembre au 2 janvier inclus).",
        # --- Intérêts moratoires ---
        "int_heading": "Calculateur d'intérêts moratoires",
        "int_disclaimer": "Calcul indicatif au taux légal de 5% l'an (art. 104 CO), sauf taux conventionnel différent que vous pouvez saisir. Le calcul est fait au prorata du nombre de jours exact, base 365 jours. Ne remplace pas un décompte établi par un tribunal ou une partie.",
        "int_capital_label": "Montant de la créance (CHF)",
        "int_date_debut_label": "Point de départ des intérêts (mise en demeure ou échéance)",
        "int_date_fin_label": "Date de fin du calcul (souvent la date du jour ou du paiement)",
        "int_taux_label": "Taux annuel (%)",
        "int_btn": "Calculer les intérêts",
        "int_result_interet": "Intérêts moratoires : ",
        "int_result_total": "Capital + intérêts : ",
        "int_result_jours": " sur ",
        "int_result_jours_suffix": " jours",
        "int_source": "Base légale : art. 104 al. 1 CO, taux légal de 5% l'an sauf convention contraire. Le point de départ est en principe le lendemain de l'échéance fixée, ou le lendemain de la sommation (mise en demeure) si aucune échéance n'a été fixée (art. 102 CO).",
        "date_placeholder_hint": "jj.mm.aaaa",
        "currency": "CHF",
        # --- Amende exces de vitesse (gratuit) ---
        "amende_heading": "Calculateur gratuit d'amende pour excès de vitesse",
        "amende_disclaimer": "Ce calculateur applique le barème fédéral des amendes d'ordre (OAO) et les seuils de retrait de permis des art. 16a à 16c LCR. Indiquez le dépassement déjà net (tolérance de mesure déjà déduite), tel qu'il figure sur l'amende reçue. Au-delà du barème fixe, l'amende n'est plus déterminée par un tarif : elle est fixée par le Ministère public ou un tribunal. Résultat indicatif, pas un avis juridique.",
        "amende_zone_label": "Zone de circulation",
        "amende_zone_localite": "À l'intérieur d'une localité (limite 50 km/h)",
        "amende_zone_hors": "Hors localité (limite 80 km/h)",
        "amende_zone_autoroute": "Autoroute ou semi-autoroute (limite 100-120 km/h)",
        "amende_exces_label": "Dépassement net (km/h, tolérance déjà déduite)",
        "amende_exces_help": "Ce chiffre figure sur l'amende reçue, ou peut être demandé à l'autorité qui a mesuré la vitesse.",
        "amende_btn": "Calculer l'amende",
        "amende_result_oao_prefix": "Amende d'ordre : ",
        "amende_result_oao_note": "Pas de retrait de permis attendu pour une première infraction à ce niveau (art. 16a LCR).",
        "amende_result_moyen_title": "Infraction moyenne (art. 16b LCR)",
        "amende_result_moyen_text": "Ce dépassement dépasse le barème fixe des amendes d'ordre : il fait l'objet d'une dénonciation pénale, et l'amende elle-même est fixée par le Ministère public, pas par un tarif. Le permis de conduire est en principe retiré pour une durée d'au moins un mois pour un premier cas sans antécédent.",
        "amende_result_grave_title": "Infraction grave (art. 16c LCR)",
        "amende_result_grave_text": "Ce dépassement atteint le seuil de l'infraction grave. Le permis de conduire est retiré pour une durée d'au moins trois mois, quels que soient les antécédents. L'amende elle-même n'est pas fixée par un barème : elle relève du Ministère public ou d'un tribunal pénal.",
        "amende_result_chauffard_title": "Délit de chauffard (art. 90 al. 3-4 LCR)",
        "amende_result_chauffard_text": "Ce dépassement atteint le seuil du délit de chauffard (cas standard : zones 50/80/120 km/h — les zones 30 et semi-autoroutes ont des seuils différents, non couverts par ce calculateur). La peine encourue est une peine privative de liberté d'au moins un an, et le permis de conduire est retiré pour une durée d'au moins deux ans.",
        "amende_source": "Sources : barème des amendes d'ordre (OAO) ; art. 16a à 16c LCR pour les mesures administratives ; art. 90 al. 3-4 LCR pour le délit de chauffard.",
        # --- Generateur lettre resiliation de bail (gratuit) ---
        "rb_heading": "Générateur gratuit de lettre de résiliation de bail",
        "rb_disclaimer": "Ce générateur rédige une lettre de résiliation conforme aux usages, et vérifie uniquement le respect du délai légal minimal (3 mois pour un logement, 6 mois pour un local commercial, art. 266c/266d CO). Il ne vérifie pas si la date choisie correspond à un terme de résiliation valable selon votre contrat ou les usages locaux : cette date doit être un terme prévu par le bail (généralement fin de trimestre, ou échéance annuelle indiquée dans le contrat). En cas de doute, faites confirmer la date par un avocat avant l'envoi.",
        "rb_type_label": "Type de bail",
        "rb_type_habitation": "Logement (délai légal minimal : 3 mois)",
        "rb_type_commercial": "Local commercial (délai légal minimal : 6 mois)",
        "rb_nom_exp_label": "Votre nom",
        "rb_adresse_exp_label": "Votre adresse",
        "rb_nom_dest_label": "Nom du bailleur ou de la régie",
        "rb_adresse_dest_label": "Adresse du bailleur ou de la régie",
        "rb_objet_label": "Adresse du logement ou local loué",
        "rb_date_envoi_label": "Date d'envoi de la lettre",
        "rb_date_fin_label": "Date de fin de bail souhaitée",
        "rb_btn": "Générer la lettre",
        "rb_warning_delai": "Attention : entre la date d'envoi et la date de fin choisie, il ne s'écoule pas les {mois} mois requis par la loi pour ce type de bail. Cette résiliation risque d'être considérée comme donnée pour le terme suivant, pas celui indiqué.",
        "rb_result_heading": "Votre lettre (à relire, compléter et signer avant envoi)",
        "rb_copy_btn": "Copier le texte",
        "rb_copy_done": "Copié !",
        "rb_letter_object": "Résiliation du bail portant sur {objet}",
        "rb_letter_greeting": "Madame, Monsieur,",
        "rb_letter_body1": "Par la présente, je vous notifie la résiliation du contrat de bail me liant à vous pour l'objet susmentionné, pour le {date_fin}.",
        "rb_letter_body2": "Je vous prie de bien vouloir me confirmer par écrit la bonne réception de ce congé ainsi que la date de résiliation retenue.",
        "rb_letter_body3": "Je reste à votre disposition pour convenir d'une date pour l'état des lieux de sortie.",
        "rb_letter_closing": "Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
        "rb_letter_recommande": "(à envoyer de préférence par courrier recommandé, pour prouver la date d'envoi)",
        "rb_source": "Base légale : art. 266c CO (logements, délai de 3 mois) et art. 266d CO (locaux commerciaux, délai de 6 mois), pour le prochain terme légal ou contractuel.",
        # --- Free child-support (pension alimentaire) estimator ---
        "pa_heading": "Estimateur gratuit de pension alimentaire pour enfant",
        "pa_disclaimer": "Important : il n'existe pas de formule légale fixe pour calculer une pension alimentaire en Suisse. Le Tribunal fédéral impose une méthode en deux étapes (ATF 147 III 265) qui laisse une large marge d'appréciation au juge sur les besoins concrets et le revenu hypothétique. Ce simulateur applique une version simplifiée et illustrative de cette méthode, avec les montants de base du minimum vital LP et une répartition \"grandes têtes / petites têtes\" présentée comme une convention parmi d'autres, jamais comme une règle légale. Saisissez vos propres montants réels : rien n'est deviné.",
        "pa_children_heading": "Enfants concernés",
        "pa_children_under10_label": "Nombre d'enfants de moins de 10 ans",
        "pa_children_10plus_label": "Nombre d'enfants de 10 ans ou plus",
        "pa_creancier_heading": "Parent qui a la garde principale",
        "pa_creancier_revenu_label": "Revenu net mensuel (CHF)",
        "pa_creancier_loyer_label": "Loyer ou charge de logement mensuelle (CHF)",
        "pa_creancier_assurance_label": "Prime d'assurance-maladie de base mensuelle (CHF)",
        "pa_creancier_charges_label": "Autres charges mensuelles justifiées (CHF, facultatif)",
        "pa_debiteur_heading": "Parent qui verserait la pension",
        "pa_debiteur_situation_label": "Situation du parent débiteur",
        "pa_debiteur_situation_seul": "Vit seul(e)",
        "pa_debiteur_situation_couple": "Vit en couple / ménage commun",
        "pa_debiteur_revenu_label": "Revenu net mensuel (CHF)",
        "pa_debiteur_loyer_label": "Loyer ou charge de logement mensuelle (CHF)",
        "pa_debiteur_assurance_label": "Prime d'assurance-maladie de base mensuelle (CHF)",
        "pa_debiteur_charges_label": "Autres charges mensuelles justifiées (CHF, facultatif)",
        "pa_btn": "Estimer la pension",
        "pa_result_heading": "Estimation indicative",
        "pa_result_pension_prefix": "Pension mensuelle indicative : ",
        "pa_result_detail_enfants": "Minimum vital des enfants (base LP) : ",
        "pa_result_detail_excedent_positif": "Excédent familial disponible réparti selon la méthode \"grandes têtes / petites têtes\" : ",
        "pa_result_detail_excedent_nul": "Aucun excédent familial disponible : seul le minimum vital des enfants est pris en compte, dans la limite du disponible du parent débiteur.",
        "pa_result_insufficient": "Le parent débiteur ne dispose pas, sur la base des montants saisis, d'un revenu suffisant au-delà de son propre minimum vital pour verser une pension. Dans ce cas, le juge peut envisager de lui imputer un revenu hypothétique s'il estime qu'il pourrait raisonnablement gagner davantage. Consultez un avocat en droit de la famille.",
        "pa_result_capped": "Le montant indicatif calculé pour les enfants ({montant} CHF) dépasse ce que le parent débiteur peut verser sans descendre sous son propre minimum vital. Le montant retenu ci-dessus est donc plafonné à son disponible réel.",
        "pa_source": "Méthode : ATF 147 III 265 (minimum vital selon les lignes directrices LP, puis répartition de l'excédent). Montants de base du minimum vital : Conférence des préposés aux poursuites et faillites de Suisse. Résultat purement indicatif, ne remplace pas une consultation d'avocat en droit de la famille.",
        # --- Free debt-collection (poursuite) fee calculator ---
        "fp_heading": "Calculateur gratuit des frais de poursuite (commandement de payer)",
        "fp_disclaimer": "Ce calculateur applique le barème officiel de l'émolument pour la rédaction, l'établissement et la notification d'un commandement de payer (art. 16 al. 1 OELP), en vigueur depuis le 1er janvier 2026. Il ne couvre pas les frais supplémentaires éventuels (tentative de notification, double exemplaire, opposition, continuation de la poursuite, saisie).",
        "fp_montant_label": "Montant de la créance réclamée (CHF)",
        "fp_btn": "Calculer les frais",
        "fp_result_prefix": "Émolument du commandement de payer : ",
        "fp_result_avance": "Cet émolument est avancé par le créancier lors du dépôt de la réquisition de poursuite, puis mis à la charge finale du débiteur poursuivi si la poursuite aboutit (art. 68 LP).",
        "fp_source": "Source : art. 16 al. 1 OELP (ordonnance sur les émoluments perçus en application de la LP), texte en vigueur depuis le 1er janvier 2026 (RO 2025 630) ; art. 68 LP pour l'avance et la répartition finale des frais.",
        # --- Free sublease consent-request letter generator ---
        "sl_heading": "Générateur gratuit de demande de sous-location",
        "sl_disclaimer": "La sous-location d'un logement requiert le consentement écrit préalable du bailleur (art. 262 CO). Ce générateur prépare une lettre de demande de consentement et signale un loyer de sous-location potentiellement abusif, mais ne remplace pas une consultation d'avocat en droit du bail.",
        "sl_bailleur_nom_label": "Nom du bailleur ou de la régie",
        "sl_bailleur_adresse_label": "Adresse du bailleur ou de la régie",
        "sl_locataire_nom_label": "Votre nom (locataire principal)",
        "sl_locataire_adresse_label": "Votre adresse",
        "sl_objet_label": "Adresse du logement loué",
        "sl_souslocataire_nom_label": "Nom du sous-locataire envisagé",
        "sl_date_debut_label": "Date de début de la sous-location",
        "sl_date_fin_label": "Date de fin de la sous-location (laisser vide si indéterminée)",
        "sl_loyer_principal_label": "Loyer principal mensuel actuel (CHF)",
        "sl_loyer_sous_label": "Loyer de sous-location mensuel envisagé (CHF)",
        "sl_btn": "Générer la demande",
        "sl_warning_abusif": "Attention : le loyer de sous-location envisagé dépasse de plus de 20% le loyer principal. Selon la jurisprudence (ATF 119 II 353), une majoration de cet ordre n'est en principe admise que pour un logement meublé ou accompagné de prestations supplémentaires ; à défaut, ce loyer risque d'être considéré comme abusif et contestable par le bailleur ou le sous-locataire.",
        "sl_result_heading": "Votre lettre (à relire, compléter et signer)",
        "sl_copy_btn": "Copier le texte",
        "sl_copy_done": "Copié !",
        "sl_letter_object": "Demande de consentement à la sous-location de {objet}",
        "sl_letter_greeting": "Madame, Monsieur,",
        "sl_letter_body1": "Je vous informe de mon souhait de sous-louer le logement susmentionné à {souslocataire}, à compter du {date_debut}{date_fin_suffix}, moyennant un loyer de sous-location de {loyer_sous} CHF par mois (loyer principal actuel : {loyer_principal} CHF par mois).",
        "sl_letter_date_fin_suffix": " jusqu'au {date_fin}",
        "sl_letter_body2": "Conformément à l'art. 262 CO, je vous serais reconnaissant de bien vouloir me communiquer par écrit votre consentement à cette sous-location, ou les motifs de votre refus le cas échéant.",
        "sl_letter_body3": "Je reste à votre disposition pour tout complément d'information.",
        "sl_letter_closing": "Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
        "sl_source": "Base légale : art. 262 CO (consentement écrit du bailleur, motifs de refus limitatifs à l'al. 2) ; ATF 119 II 353 sur le seuil de majoration admise pour un logement meublé.",
        # --- Free forced-heirship (réserve héréditaire) calculator ---
        "rh_heading": "Calculateur gratuit de la réserve héréditaire",
        "rh_disclaimer": "Ce calculateur applique les fractions légales de réserve héréditaire depuis la révision du droit des successions entrée en vigueur le 1er janvier 2023 (art. 470 et 471 CC). Il couvre les configurations familiales les plus courantes, sans tenir compte des cas particuliers (héritiers d'un degré plus éloigné, pacte successoral, régime matrimonial à liquider en premier). Résultat indicatif, ne remplace pas une consultation d'avocat en droit des successions.",
        "rh_situation_label": "Situation familiale",
        "rh_situation_conjoint_descendants": "Conjoint (ou partenaire enregistré) survivant et descendants",
        "rh_situation_conjoint_parents": "Conjoint (ou partenaire enregistré) survivant et parents (sans descendants)",
        "rh_situation_conjoint_seul": "Conjoint (ou partenaire enregistré) survivant seul (sans descendants ni parents survivants)",
        "rh_situation_descendants_seuls": "Descendants seuls (sans conjoint survivant)",
        "rh_situation_parents_seuls": "Parents seuls (sans conjoint survivant ni descendants)",
        "rh_nb_enfants_label": "Nombre d'enfants (ou de souches de descendants)",
        "rh_btn": "Calculer la réserve",
        "rh_result_heading": "Répartition indicative",
        "rh_result_reserve_conjoint": "Réserve du conjoint / partenaire enregistré : ",
        "rh_result_reserve_descendants": "Réserve totale des descendants : ",
        "rh_result_reserve_descendants_chacun": "Réserve par enfant : ",
        "rh_result_reserve_parents": "Réserve des parents : 0 (supprimée depuis le 1.1.2023)",
        "rh_result_quotite_disponible": "Quotité disponible (librement attribuable par testament) : ",
        "rh_source": "Base légale : art. 470 et 471 CC (réserve héréditaire depuis la révision entrée en vigueur le 1.1.2023) ; art. 462 CC (parts légales entre héritiers). Réserve du conjoint/partenaire et des descendants réduite à la moitié de leur part légale ; réserve des parents entièrement supprimée.",
        # --- Free lease notice-period (délai de congé) checker ---
        "dc_heading": "Calculateur gratuit du délai de congé de bail",
        "dc_disclaimer": "Ce calculateur vérifie uniquement le respect du délai légal minimal de préavis (art. 266c/266d CO) à partir de votre date d'envoi du congé. Il ne vérifie pas si la date obtenue correspond à un terme valable selon votre contrat ou les usages locaux (souvent la fin d'un trimestre) : vérifiez ce point séparément.",
        "dc_type_label": "Type de bail",
        "dc_type_habitation": "Logement (délai légal minimal : 3 mois)",
        "dc_type_commercial": "Local commercial (délai légal minimal : 6 mois)",
        "dc_date_envoi_label": "Date d'envoi (ou d'envoi prévu) du congé",
        "dc_btn": "Calculer la date la plus proche possible",
        "dc_result_prefix": "Date la plus proche possible pour la fin du bail : ",
        "dc_result_note": "Cette date correspond au strict délai légal minimal après votre envoi. Elle doit encore correspondre à un terme valable pour votre bail (contractuel ou d'usage local) : à défaut, le congé est reporté au terme suivant.",
        "dc_source": "Base légale : art. 266c CO (logements, délai minimal de 3 mois) et art. 266d CO (locaux commerciaux, délai minimal de 6 mois), pour le prochain terme légal ou contractuel.",
        # --- Free formal-notice (mise en demeure) letter generator ---
        "md_heading": "Générateur gratuit de mise en demeure",
        "md_disclaimer": "Ce générateur prépare une mise en demeure formelle (interpellation au sens de l'art. 102 CO) pour réclamer le paiement d'une somme due, avec un délai de grâce et un rappel de l'intérêt moratoire légal (art. 104 CO). Il ne remplace pas une consultation d'avocat, notamment si le débiteur conteste la créance.",
        "md_creancier_nom_label": "Votre nom (créancier)",
        "md_creancier_adresse_label": "Votre adresse",
        "md_debiteur_nom_label": "Nom du débiteur",
        "md_debiteur_adresse_label": "Adresse du débiteur",
        "md_objet_label": "Objet de la créance (ex : facture n° 123 du 1er mars 2026)",
        "md_montant_label": "Montant dû (CHF)",
        "md_delai_grace_label": "Délai de grâce accordé (jours, à compter de l'envoi)",
        "md_btn": "Générer la mise en demeure",
        "md_result_heading": "Votre lettre (à relire, compléter et signer)",
        "md_copy_btn": "Copier le texte",
        "md_copy_done": "Copié !",
        "md_letter_object": "Mise en demeure — {objet}",
        "md_letter_greeting": "Madame, Monsieur,",
        "md_letter_body1": "Malgré nos précédentes démarches, je constate que le montant de {montant} CHF relatif à {objet} demeure impayé à ce jour.",
        "md_letter_body2": "Par la présente, je vous mets formellement en demeure de régler ce montant dans un délai de {delai} jours à compter de la date d'envoi de ce courrier, soit au plus tard le {date_limite}.",
        "md_letter_body3": "À défaut de paiement dans ce délai, un intérêt moratoire de 5% l'an sera réclamé dès la présente mise en demeure, conformément à l'art. 104 CO, et une procédure de poursuite pourra être engagée sans autre avis.",
        "md_letter_closing": "Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
        "md_source": "Base légale : art. 102 CO (mise en demeure par interpellation du créancier) ; art. 104 CO (intérêt moratoire légal de 5% l'an dès la demeure, sauf convention contraire).",
        # --- Free employment notice-period calculator ---
        "dl_heading": "Calculateur gratuit du délai de préavis de licenciement",
        "dl_disclaimer": "Ce calculateur applique les délais légaux minimaux de préavis de l'art. 335b CO (temps d'essai) et de l'art. 335c CO (après le temps d'essai). Un contrat individuel, un contrat-type de travail ou une convention collective peut prévoir des délais plus longs, jamais plus courts (sauf accord contraire admis par la loi). Résultat indicatif, ne remplace pas une consultation d'avocat en droit du travail.",
        "dl_essai_label": "Êtes-vous encore en temps d'essai ?",
        "dl_essai_oui": "Oui, encore en temps d'essai",
        "dl_essai_non": "Non, le temps d'essai est terminé",
        "dl_date_engagement_label": "Date de début des rapports de travail",
        "dl_date_notification_label": "Date de notification du congé",
        "dl_btn": "Calculer le délai de préavis",
        "dl_result_essai_prefix": "Délai de préavis durant le temps d'essai : 7 jours. Date de fin des rapports de travail : ",
        "dl_result_essai_note": "Durant le temps d'essai, le congé peut prendre effet n'importe quel jour, pas nécessairement en fin de mois (art. 335b al. 1 CO).",
        "dl_result_normal_prefix": "Délai de préavis applicable : ",
        "dl_result_normal_mois_1": "1 mois (1re année de service)",
        "dl_result_normal_mois_2": "2 mois (de la 2e à la 9e année de service)",
        "dl_result_normal_mois_3": "3 mois (dès la 10e année de service)",
        "dl_result_date_fin_prefix": "Date de fin des rapports de travail (fin du mois suivant l'échéance du délai) : ",
        "dl_result_normal_note": "Sauf accord contraire, le congé doit être donné pour la fin d'un mois (art. 335c al. 1 CO).",
        "dl_source": "Base légale : art. 335b CO (préavis de 7 jours durant le temps d'essai) et art. 335c CO (préavis de 1, 2 ou 3 mois selon l'ancienneté, pour la fin d'un mois, après le temps d'essai).",
        # --- Free administrative-appeal deadline calculator ---
        "dr_heading": "Calculateur gratuit de délai de recours administratif",
        "dr_disclaimer": "Ce calculateur applique l'art. 20 PA (point de départ, report en cas de week-end ou de jour férié fédéral) et l'art. 22a PA (féries). Il ne s'applique pas aux procédures d'effet suspensif, de mesures provisionnelles ou de marchés publics, pour lesquelles les féries ne s'appliquent pas (art. 22a al. 2 PA). Il ne vérifie que le week-end et le 1er août, seul jour férié reconnu au niveau fédéral : les jours fériés cantonaux doivent être vérifiés séparément si l'autorité concernée est cantonale. Résultat indicatif, à confirmer avant tout acte important.",
        "dr_date_notif_label": "Date de notification de la décision",
        "dr_jours_label": "Durée du délai de recours (en jours, indiquée dans la décision ou par la loi applicable)",
        "dr_btn": "Calculer l'échéance",
        "dr_result_prefix": "Le délai de recours expire le : ",
        "dr_source": "Base légale : art. 20 al. 1 et 3 PA (point de départ le lendemain de la notification, report au premier jour ouvrable suivant si le dernier jour tombe un week-end ou le 1er août) et art. 22a PA (trois périodes de féries, identiques à l'art. 145 CPC : du 7e jour avant Pâques au 7e jour après Pâques inclus, du 15 juillet au 15 août inclus, du 18 décembre au 2 janvier inclus ; sauf effet suspensif, mesures provisionnelles et marchés publics, art. 22a al. 2 PA).",
    },
    "de": {
        "presc_heading": "Verjährungsrechner",
        "presc_disclaimer": "Dieser Rechner wendet die gesetzlichen Grundfristen an (Art. 60, 127, 128 OR und Art. 97 StGB). Hemmungs- und Unterbrechungsgründe (Art. 134 bis 138 OR und entsprechende Bestimmungen des StGB) sowie Sonderfälle werden nicht berücksichtigt. Das Ergebnis ist eine Orientierungshilfe, keine Rechtsauskunft.",
        "presc_type_label": "Art der Forderung oder Straftat",
        "presc_opt_contrat": "Allgemeine vertragliche Forderung (Art. 127 OR, 10 Jahre)",
        "presc_opt_illicite": "Schaden aus unerlaubter Handlung (Art. 60 OR)",
        "presc_opt_periodique": "Periodische Forderung: Miete, Zinsen, Löhne (Art. 128 OR, 5 Jahre)",
        "presc_opt_penal": "Straftat (Art. 97 StGB)",
        "presc_date_exigible": "Fälligkeitsdatum der Forderung",
        "presc_date_acte": "Datum der schädigenden Handlung",
        "presc_date_connaissance": "Datum der Kenntnis von Schaden und Schädiger",
        "presc_date_infraction": "Datum der Straftat",
        "presc_peine_label": "Höchststrafe",
        "presc_peine_vie": "Lebenslängliche Freiheitsstrafe (30 Jahre)",
        "presc_peine_plus3": "Freiheitsstrafe von mehr als 3 Jahren (15 Jahre)",
        "presc_peine_max3": "Freiheitsstrafe von höchstens 3 Jahren (10 Jahre)",
        "presc_peine_autre": "Andere Vergehen (7 Jahre)",
        "presc_peine_contravention": "Übertretung (Art. 109 StGB, 3 Jahre)",
        "presc_btn": "Verjährung berechnen",
        "presc_result_prefix": "Geschätztes Verjährungsdatum: ",
        "presc_result_illicite_note": " (die frühere der beiden Fristen, relativ oder absolut, ist massgebend)",
        "presc_source_contrat": "Rechtsgrundlage: Art. 127 OR, allgemeine Verjährungsfrist von 10 Jahren.",
        "presc_source_illicite": "Rechtsgrundlage: Art. 60 Abs. 1 OR, relative Frist von 3 Jahren ab Kenntnis von Schaden und Schädiger, absolute Frist von 20 Jahren ab der schädigenden Handlung (Frist mit der Revision per 1.1.2020 von 10 auf 20 Jahre angehoben).",
        "presc_source_periodique": "Rechtsgrundlage: Art. 128 OR, Frist von 5 Jahren für Miet- und Kapitalzinse sowie andere periodische Leistungen, für Löhne und weitere in dieser Bestimmung aufgezählte Forderungen.",
        "presc_source_penal": "Rechtsgrundlage: Art. 97 StGB. Seit der 2014 in Kraft getretenen Revision sind diese Fristen absolut und werden durch Verfahrenshandlungen nicht mehr unterbrochen.",
        "delai_heading": "Rechtsmittel- und Verfahrensfristenrechner",
        "delai_disclaimer": "Dieser Rechner wendet Art. 142 ZPO (Fristbeginn, Verschiebung bei Wochenende oder eidgenössischem Feiertag) und Art. 145 ZPO (Gerichtsferien) an. Geprüft werden nur das Wochenende und der 1. August, der einzige eidgenössisch anerkannte Feiertag (Art. 20a ArG): kantonale und kommunale Feiertage am Gerichtssitz müssen separat geprüft werden. Ergebnis als Orientierungshilfe, vor wichtigen Verfahrenshandlungen zu bestätigen.",
        "delai_date_comm_label": "Datum der Mitteilung oder des auslösenden Ereignisses",
        "delai_jours_label": "Fristdauer (in Tagen)",
        "delai_procedure_label": "Verfahrensart",
        "delai_opt_ordinaire": "Ordentliches Verfahren (Gerichtsferien gelten)",
        "delai_opt_sommaire": "Schlichtungs- oder summarisches Verfahren (keine Gerichtsferien, Art. 145 Abs. 2 ZPO)",
        "delai_btn": "Fristende berechnen",
        "delai_result_prefix": "Die Frist endet am: ",
        "delai_source": "Rechtsgrundlage: Art. 142 Abs. 1 und 3 ZPO (Fristbeginn am Tag nach der Mitteilung, Verschiebung auf den nächsten Werktag, wenn der letzte Tag auf ein Wochenende oder den 1. August fällt) und Art. 145 ZPO (drei Gerichtsferien-Perioden: vom 7. Tag vor Ostern bis und mit dem 7. Tag nach Ostern, vom 15. Juli bis und mit 15. August, vom 18. Dezember bis und mit 2. Januar).",
        "int_heading": "Verzugszinsrechner",
        "int_disclaimer": "Orientierungsberechnung zum gesetzlichen Zinssatz von 5% pro Jahr (Art. 104 OR), sofern kein abweichender vereinbarter Zinssatz eingegeben wird. Die Berechnung erfolgt taggenau auf Basis von 365 Tagen. Ersetzt keine gerichtliche oder von einer Partei erstellte Abrechnung.",
        "int_capital_label": "Forderungsbetrag (CHF)",
        "int_date_debut_label": "Beginn des Zinslaufs (Mahnung oder Fälligkeit)",
        "int_date_fin_label": "Enddatum der Berechnung (oft das heutige Datum oder das Zahlungsdatum)",
        "int_taux_label": "Jahreszinssatz (%)",
        "int_btn": "Zinsen berechnen",
        "int_result_interet": "Verzugszinsen: ",
        "int_result_total": "Kapital plus Zinsen: ",
        "int_result_jours": " über ",
        "int_result_jours_suffix": " Tage",
        "int_source": "Rechtsgrundlage: Art. 104 Abs. 1 OR, gesetzlicher Zinssatz von 5% pro Jahr, sofern nichts anderes vereinbart ist. Der Zinslauf beginnt grundsätzlich am Tag nach der vereinbarten Fälligkeit oder am Tag nach der Mahnung, wenn keine Fälligkeit vereinbart wurde (Art. 102 OR).",
        "date_placeholder_hint": "tt.mm.jjjj",
        "currency": "CHF",
        # --- Bussenrechner Geschwindigkeit (kostenlos) ---
        "amende_heading": "Kostenloser Bussenrechner für Geschwindigkeitsüberschreitungen",
        "amende_disclaimer": "Dieser Rechner wendet den eidgenössischen Ordnungsbussenkatalog (OBV) sowie die Ausweisentzugs-Schwellen der Art. 16a bis 16c SVG an. Geben Sie die bereits um die Messtoleranz bereinigte Überschreitung an, wie sie auf der Busse ausgewiesen wird. Ausserhalb des festen Bussenkatalogs wird die Busse nicht mehr tarifmässig festgelegt, sondern von der Staatsanwaltschaft oder einem Gericht bestimmt. Ergebnis als Orientierungshilfe, keine Rechtsauskunft.",
        "amende_zone_label": "Verkehrszone",
        "amende_zone_localite": "Innerorts (Limite 50 km/h)",
        "amende_zone_hors": "Ausserorts (Limite 80 km/h)",
        "amende_zone_autoroute": "Autobahn oder Autostrasse (Limite 100-120 km/h)",
        "amende_exces_label": "Nettoüberschreitung (km/h, Messtoleranz bereits abgezogen)",
        "amende_exces_help": "Diese Zahl steht auf der erhaltenen Busse oder kann bei der messenden Behörde erfragt werden.",
        "amende_btn": "Busse berechnen",
        "amende_result_oao_prefix": "Ordnungsbusse: ",
        "amende_result_oao_note": "Bei einer ersten Widerhandlung auf diesem Niveau ist kein Ausweisentzug zu erwarten (Art. 16a SVG).",
        "amende_result_moyen_title": "Mittelschwere Widerhandlung (Art. 16b SVG)",
        "amende_result_moyen_text": "Diese Überschreitung liegt über dem festen Ordnungsbussenkatalog: Es erfolgt eine Strafanzeige, und die Busse selbst wird von der Staatsanwaltschaft festgelegt, nicht nach Tarif. Der Führerausweis wird bei einer ersten Widerhandlung ohne Vorstrafen in der Regel für mindestens einen Monat entzogen.",
        "amende_result_grave_title": "Schwere Widerhandlung (Art. 16c SVG)",
        "amende_result_grave_text": "Diese Überschreitung erreicht die Schwelle der schweren Widerhandlung. Der Führerausweis wird unabhängig von Vorstrafen für mindestens drei Monate entzogen. Die Busse selbst folgt keinem festen Tarif: Sie liegt bei der Staatsanwaltschaft oder einem Strafgericht.",
        "amende_result_chauffard_title": "Raserdelikt (Art. 90 Abs. 3-4 SVG)",
        "amende_result_chauffard_text": "Diese Überschreitung erreicht die Schwelle des Raserdelikts (Standardfall: Zonen 50/80/120 km/h — 30er-Zonen und Autostrassen haben abweichende Schwellen, die dieser Rechner nicht abdeckt). Es droht eine Freiheitsstrafe von mindestens einem Jahr, und der Führerausweis wird für mindestens zwei Jahre entzogen.",
        "amende_source": "Quellen: eidgenössischer Ordnungsbussenkatalog (OBV); Art. 16a bis 16c SVG für Administrativmassnahmen; Art. 90 Abs. 3-4 SVG für das Raserdelikt.",
        # --- Kostenloser Mietkündigungsschreiben-Generator ---
        "rb_heading": "Kostenloser Generator für Mietkündigungsschreiben",
        "rb_disclaimer": "Dieser Generator verfasst ein übliches Kündigungsschreiben und prüft nur die Einhaltung der gesetzlichen Mindestkündigungsfrist (3 Monate für Wohnraum, 6 Monate für Geschäftsräume, Art. 266c/266d OR). Er prüft nicht, ob das gewählte Datum einem gültigen Kündigungstermin gemäss Ihrem Vertrag oder den örtlichen Gepflogenheiten entspricht (in der Regel Quartalsende oder im Vertrag genannter Jahrestermin). Lassen Sie das Datum im Zweifel vor dem Versand von einer Anwältin oder einem Anwalt bestätigen.",
        "rb_type_label": "Art des Mietverhältnisses",
        "rb_type_habitation": "Wohnung (gesetzliche Mindestfrist: 3 Monate)",
        "rb_type_commercial": "Geschäftsräume (gesetzliche Mindestfrist: 6 Monate)",
        "rb_nom_exp_label": "Ihr Name",
        "rb_adresse_exp_label": "Ihre Adresse",
        "rb_nom_dest_label": "Name der Vermieterschaft oder Verwaltung",
        "rb_adresse_dest_label": "Adresse der Vermieterschaft oder Verwaltung",
        "rb_objet_label": "Adresse der gemieteten Wohnung oder Räumlichkeit",
        "rb_date_envoi_label": "Versanddatum des Schreibens",
        "rb_date_fin_label": "Gewünschtes Kündigungsdatum",
        "rb_btn": "Schreiben erstellen",
        "rb_warning_delai": "Achtung: Zwischen dem Versanddatum und dem gewählten Enddatum liegen nicht die für diese Mietart gesetzlich erforderlichen {mois} Monate. Diese Kündigung könnte als für den nächstfolgenden Termin gegeben gelten, nicht für den angegebenen.",
        "rb_result_heading": "Ihr Schreiben (vor dem Versand prüfen, ergänzen und unterschreiben)",
        "rb_copy_btn": "Text kopieren",
        "rb_copy_done": "Kopiert!",
        "rb_letter_object": "Kündigung des Mietverhältnisses betreffend {objet}",
        "rb_letter_greeting": "Sehr geehrte Damen und Herren,",
        "rb_letter_body1": "Hiermit kündige ich das mit Ihnen bestehende Mietverhältnis für das oben genannte Objekt per {date_fin}.",
        "rb_letter_body2": "Ich bitte Sie, mir den Erhalt dieser Kündigung sowie das massgebende Kündigungsdatum schriftlich zu bestätigen.",
        "rb_letter_body3": "Für die Vereinbarung eines Termins zur Wohnungsübergabe stehe ich Ihnen gerne zur Verfügung.",
        "rb_letter_closing": "Freundliche Grüsse",
        "rb_letter_recommande": "(vorzugsweise per Einschreiben versenden, um das Versanddatum nachzuweisen)",
        "rb_source": "Rechtsgrundlage: Art. 266c OR (Wohnräume, 3-monatige Frist) und Art. 266d OR (Geschäftsräume, 6-monatige Frist), jeweils auf den nächsten gesetzlichen oder vertraglichen Termin.",
        # --- Free child-support (pension alimentaire) estimator ---
        "pa_heading": "Kostenloser Kinderunterhalt-Rechner",
        "pa_disclaimer": "Wichtig: Es gibt in der Schweiz keine feste gesetzliche Formel zur Berechnung des Kinderunterhalts. Das Bundesgericht schreibt ein zweistufiges Verfahren vor (BGE 147 III 265), das dem Gericht einen weiten Ermessensspielraum bezüglich der konkreten Bedürfnisse und des hypothetischen Einkommens lässt. Dieser Rechner wendet eine vereinfachte, illustrative Version dieser Methode an, mit den Grundbeträgen des betreibungsrechtlichen Existenzminimums und einer Überschussverteilung nach der Methode \"grosse Köpfe / kleine Köpfe\", die als eine mögliche Konvention unter anderen dargestellt wird, nie als gesetzliche Regel. Geben Sie Ihre eigenen tatsächlichen Beträge ein: Es wird nichts geschätzt.",
        "pa_children_heading": "Betroffene Kinder",
        "pa_children_under10_label": "Anzahl Kinder unter 10 Jahren",
        "pa_children_10plus_label": "Anzahl Kinder ab 10 Jahren",
        "pa_creancier_heading": "Obhutsberechtigter Elternteil",
        "pa_creancier_revenu_label": "Monatliches Nettoeinkommen (CHF)",
        "pa_creancier_loyer_label": "Monatliche Wohnkosten (CHF)",
        "pa_creancier_assurance_label": "Monatliche Grundversicherungsprämie (CHF)",
        "pa_creancier_charges_label": "Weitere ausgewiesene monatliche Auslagen (CHF, fakultativ)",
        "pa_debiteur_heading": "Unterhaltspflichtiger Elternteil",
        "pa_debiteur_situation_label": "Situation des unterhaltspflichtigen Elternteils",
        "pa_debiteur_situation_seul": "Lebt allein",
        "pa_debiteur_situation_couple": "Lebt in Partnerschaft / gemeinsamem Haushalt",
        "pa_debiteur_revenu_label": "Monatliches Nettoeinkommen (CHF)",
        "pa_debiteur_loyer_label": "Monatliche Wohnkosten (CHF)",
        "pa_debiteur_assurance_label": "Monatliche Grundversicherungsprämie (CHF)",
        "pa_debiteur_charges_label": "Weitere ausgewiesene monatliche Auslagen (CHF, fakultativ)",
        "pa_btn": "Unterhalt schätzen",
        "pa_result_heading": "Orientierende Schätzung",
        "pa_result_pension_prefix": "Orientierender monatlicher Unterhaltsbeitrag: ",
        "pa_result_detail_enfants": "Existenzminimum der Kinder (Grundlage LP): ",
        "pa_result_detail_excedent_positif": "Verfügbarer familiärer Überschuss, verteilt nach der Methode \"grosse Köpfe / kleine Köpfe\": ",
        "pa_result_detail_excedent_nul": "Kein verfügbarer familiärer Überschuss: Es wird nur das Existenzminimum der Kinder berücksichtigt, begrenzt auf das Verfügbare des unterhaltspflichtigen Elternteils.",
        "pa_result_insufficient": "Der unterhaltspflichtige Elternteil verfügt gemäss den eingegebenen Beträgen über kein Einkommen oberhalb seines eigenen Existenzminimums, um einen Unterhaltsbeitrag zu leisten. In diesem Fall kann das Gericht erwägen, ihm ein hypothetisches Einkommen anzurechnen, wenn es davon ausgeht, dass er vernünftigerweise mehr verdienen könnte. Konsultieren Sie eine auf Familienrecht spezialisierte Anwältin oder einen Anwalt.",
        "pa_result_capped": "Der berechnete orientierende Betrag für die Kinder ({montant} CHF) übersteigt, was der unterhaltspflichtige Elternteil leisten kann, ohne unter sein eigenes Existenzminimum zu fallen. Der oben genannte Betrag ist daher auf sein tatsächliches Verfügbares begrenzt.",
        "pa_source": "Methode: BGE 147 III 265 (Existenzminimum nach den LP-Richtlinien, danach Verteilung des Überschusses). Grundbeträge des Existenzminimums: Konferenz der Betreibungs- und Konkursbeamten der Schweiz. Rein orientierendes Ergebnis, ersetzt keine Beratung durch eine auf Familienrecht spezialisierte Anwältin bzw. einen Anwalt.",
        # --- Free debt-collection (poursuite) fee calculator ---
        "fp_heading": "Kostenloser Betreibungskosten-Rechner (Zahlungsbefehl)",
        "fp_disclaimer": "Dieser Rechner wendet den amtlichen Gebührentarif für die Ausfertigung, Erstellung und Zustellung eines Zahlungsbefehls an (Art. 16 Abs. 1 GebV SchKG), gültig seit dem 1. Januar 2026. Er deckt keine allfälligen Zusatzkosten ab (Zustellversuch, Doppel, Rechtsvorschlag, Fortsetzung der Betreibung, Pfändung).",
        "fp_montant_label": "Betrag der geltend gemachten Forderung (CHF)",
        "fp_btn": "Kosten berechnen",
        "fp_result_prefix": "Gebühr für den Zahlungsbefehl: ",
        "fp_result_avance": "Diese Gebühr wird bei der Einreichung des Betreibungsbegehrens vom Gläubiger vorgeschossen und dem betriebenen Schuldner endgültig auferlegt, wenn die Betreibung erfolgreich ist (Art. 68 SchKG).",
        "fp_source": "Quelle: Art. 16 Abs. 1 GebV SchKG (Gebührenverordnung zum Bundesgesetz über Schuldbetreibung und Konkurs), Fassung gültig seit 1. Januar 2026 (AS 2025 630); Art. 68 SchKG zum Vorschuss und zur endgültigen Kostenverteilung.",
        # --- Free sublease consent-request letter generator ---
        "sl_heading": "Kostenloser Generator für Untermietgesuche",
        "sl_disclaimer": "Die Untervermietung einer Wohnung erfordert die vorgängige schriftliche Zustimmung der Vermieterschaft (Art. 262 OR). Dieser Generator erstellt ein Zustimmungsgesuch und weist auf einen möglicherweise missbräuchlichen Untermietzins hin, ersetzt aber keine Beratung durch eine auf Mietrecht spezialisierte Anwältin bzw. einen Anwalt.",
        "sl_bailleur_nom_label": "Name der Vermieterschaft oder Verwaltung",
        "sl_bailleur_adresse_label": "Adresse der Vermieterschaft oder Verwaltung",
        "sl_locataire_nom_label": "Ihr Name (Hauptmieter/in)",
        "sl_locataire_adresse_label": "Ihre Adresse",
        "sl_objet_label": "Adresse der gemieteten Wohnung",
        "sl_souslocataire_nom_label": "Name der vorgesehenen Untermieterin bzw. des Untermieters",
        "sl_date_debut_label": "Beginn der Untermiete",
        "sl_date_fin_label": "Ende der Untermiete (leer lassen, falls unbefristet)",
        "sl_loyer_principal_label": "Aktueller monatlicher Hauptmietzins (CHF)",
        "sl_loyer_sous_label": "Vorgesehener monatlicher Untermietzins (CHF)",
        "sl_btn": "Gesuch erstellen",
        "sl_warning_abusif": "Achtung: Der vorgesehene Untermietzins übersteigt den Hauptmietzins um mehr als 20%. Gemäss Rechtsprechung (BGE 119 II 353) ist ein Aufschlag dieser Grössenordnung grundsätzlich nur bei einer möblierten Wohnung oder bei Zusatzleistungen zulässig; andernfalls riskiert dieser Mietzins, als missbräuchlich zu gelten und von der Vermieterschaft oder der Untermieterin bzw. dem Untermieter angefochten zu werden.",
        "sl_result_heading": "Ihr Schreiben (zum Prüfen, Ergänzen und Unterschreiben)",
        "sl_copy_btn": "Text kopieren",
        "sl_copy_done": "Kopiert!",
        "sl_letter_object": "Gesuch um Zustimmung zur Untervermietung von {objet}",
        "sl_letter_greeting": "Sehr geehrte Damen und Herren,",
        "sl_letter_body1": "Ich teile Ihnen mit, dass ich die oben genannte Wohnung an {souslocataire} untervermieten möchte, ab dem {date_debut}{date_fin_suffix}, zu einem Untermietzins von CHF {loyer_sous} pro Monat (aktueller Hauptmietzins: CHF {loyer_principal} pro Monat).",
        "sl_letter_date_fin_suffix": " bis zum {date_fin}",
        "sl_letter_body2": "Gemäss Art. 262 OR bitte ich Sie, mir Ihre Zustimmung zu dieser Untervermietung schriftlich mitzuteilen, oder gegebenenfalls die Gründe für eine Ablehnung.",
        "sl_letter_body3": "Für weitere Auskünfte stehe ich Ihnen gerne zur Verfügung.",
        "sl_letter_closing": "Freundliche Grüsse",
        "sl_source": "Rechtsgrundlage: Art. 262 OR (schriftliche Zustimmung der Vermieterschaft, abschliessende Ablehnungsgründe in Abs. 2); BGE 119 II 353 zur zulässigen Aufschlagsschwelle bei möblierten Wohnungen.",
        # --- Free forced-heirship (réserve héréditaire) calculator ---
        "rh_heading": "Kostenloser Pflichtteils-Rechner",
        "rh_disclaimer": "Dieser Rechner wendet die gesetzlichen Pflichtteilsquoten seit der am 1. Januar 2023 in Kraft getretenen Revision des Erbrechts an (Art. 470 und 471 ZGB). Er deckt die häufigsten Familienkonstellationen ab, ohne besondere Fälle zu berücksichtigen (Erben entfernteren Grades, Erbvertrag, zuerst zu liquidierendes Güterrecht). Orientierendes Ergebnis, ersetzt keine Beratung durch eine auf Erbrecht spezialisierte Anwältin bzw. einen Anwalt.",
        "rh_situation_label": "Familiensituation",
        "rh_situation_conjoint_descendants": "Überlebende(r) Ehegatte/eingetragene(r) Partner(in) und Nachkommen",
        "rh_situation_conjoint_parents": "Überlebende(r) Ehegatte/eingetragene(r) Partner(in) und Eltern (ohne Nachkommen)",
        "rh_situation_conjoint_seul": "Nur überlebende(r) Ehegatte/eingetragene(r) Partner(in) (ohne Nachkommen und ohne lebende Eltern)",
        "rh_situation_descendants_seuls": "Nur Nachkommen (ohne überlebende(n) Ehegatten/Partner(in))",
        "rh_situation_parents_seuls": "Nur Eltern (ohne überlebende(n) Ehegatten/Partner(in) und ohne Nachkommen)",
        "rh_nb_enfants_label": "Anzahl Kinder (bzw. Nachkommensstämme)",
        "rh_btn": "Pflichtteil berechnen",
        "rh_result_heading": "Orientierende Aufteilung",
        "rh_result_reserve_conjoint": "Pflichtteil des Ehegatten/der eingetragenen Partnerin bzw. des Partners: ",
        "rh_result_reserve_descendants": "Gesamter Pflichtteil der Nachkommen: ",
        "rh_result_reserve_descendants_chacun": "Pflichtteil pro Kind: ",
        "rh_result_reserve_parents": "Pflichtteil der Eltern: 0 (seit 1.1.2023 aufgehoben)",
        "rh_result_quotite_disponible": "Frei verfügbarer Teil (durch Testament frei zuweisbar): ",
        "rh_source": "Rechtsgrundlage: Art. 470 und 471 ZGB (Pflichtteil seit der am 1.1.2023 in Kraft getretenen Revision); Art. 462 ZGB (gesetzliche Erbquoten). Pflichtteil des Ehegatten/der Partnerin bzw. des Partners sowie der Nachkommen auf die Hälfte ihres gesetzlichen Erbanspruchs reduziert; Pflichtteil der Eltern vollständig aufgehoben.",
        # --- Free lease notice-period (délai de congé) checker ---
        "dc_heading": "Kostenloser Rechner für die Mietkündigungsfrist",
        "dc_disclaimer": "Dieser Rechner prüft nur die Einhaltung der gesetzlichen Mindestkündigungsfrist (Art. 266c/266d OR) ab Ihrem Kündigungsdatum. Er prüft nicht, ob das errechnete Datum einem gemäss Ihrem Vertrag oder den örtlichen Gepflogenheiten gültigen Termin entspricht (meist das Quartalsende): Prüfen Sie dies separat.",
        "dc_type_label": "Art des Mietverhältnisses",
        "dc_type_habitation": "Wohnung (gesetzliche Mindestfrist: 3 Monate)",
        "dc_type_commercial": "Geschäftsräume (gesetzliche Mindestfrist: 6 Monate)",
        "dc_date_envoi_label": "Datum der (geplanten) Kündigung",
        "dc_btn": "Frühestmögliches Datum berechnen",
        "dc_result_prefix": "Frühestmögliches Datum für das Ende des Mietverhältnisses: ",
        "dc_result_note": "Dieses Datum entspricht der strikten gesetzlichen Mindestfrist nach Ihrer Kündigung. Es muss noch einem für Ihren Mietvertrag gültigen Termin entsprechen (vertraglich oder ortsüblich): andernfalls wird die Kündigung auf den nächstfolgenden Termin verschoben.",
        "dc_source": "Rechtsgrundlage: Art. 266c OR (Wohnräume, Mindestfrist 3 Monate) und Art. 266d OR (Geschäftsräume, Mindestfrist 6 Monate), jeweils auf den nächsten gesetzlichen oder vertraglichen Termin.",
        # --- Free formal-notice (mise en demeure) letter generator ---
        "md_heading": "Kostenloser Generator für Mahnungen (Inverzugsetzung)",
        "md_disclaimer": "Dieser Generator erstellt eine formelle Mahnung (Inverzugsetzung im Sinne von Art. 102 OR) zur Einforderung eines geschuldeten Betrags, mit einer Nachfrist und einem Hinweis auf den gesetzlichen Verzugszins (Art. 104 OR). Er ersetzt keine Beratung durch eine Anwältin bzw. einen Anwalt, insbesondere wenn der Schuldner die Forderung bestreitet.",
        "md_creancier_nom_label": "Ihr Name (Gläubiger/in)",
        "md_creancier_adresse_label": "Ihre Adresse",
        "md_debiteur_nom_label": "Name des Schuldners",
        "md_debiteur_adresse_label": "Adresse des Schuldners",
        "md_objet_label": "Gegenstand der Forderung (z. B. Rechnung Nr. 123 vom 1. März 2026)",
        "md_montant_label": "Geschuldeter Betrag (CHF)",
        "md_delai_grace_label": "Gewährte Nachfrist (Tage, ab Versand)",
        "md_btn": "Mahnung erstellen",
        "md_result_heading": "Ihr Schreiben (zum Prüfen, Ergänzen und Unterschreiben)",
        "md_copy_btn": "Text kopieren",
        "md_copy_done": "Kopiert!",
        "md_letter_object": "Mahnung — {objet}",
        "md_letter_greeting": "Sehr geehrte Damen und Herren,",
        "md_letter_body1": "Trotz unserer vorherigen Schritte stelle ich fest, dass der Betrag von CHF {montant} betreffend {objet} bis heute unbezahlt geblieben ist.",
        "md_letter_body2": "Hiermit setze ich Sie förmlich in Verzug und fordere Sie auf, diesen Betrag innert {delai} Tagen ab Versanddatum dieses Schreibens zu begleichen, spätestens bis zum {date_limite}.",
        "md_letter_body3": "Bei Nichtzahlung innert dieser Frist wird ab dieser Mahnung ein Verzugszins von 5% pro Jahr geltend gemacht, gemäss Art. 104 OR, und es kann ohne weitere Ankündigung eine Betreibung eingeleitet werden.",
        "md_letter_closing": "Freundliche Grüsse",
        "md_source": "Rechtsgrundlage: Art. 102 OR (Inverzugsetzung durch Mahnung des Gläubigers); Art. 104 OR (gesetzlicher Verzugszins von 5% pro Jahr ab Verzug, soweit keine abweichende Vereinbarung besteht).",
        # --- Free employment notice-period calculator ---
        "dl_heading": "Kostenloser Rechner für die Kündigungsfrist",
        "dl_disclaimer": "Dieser Rechner wendet die gesetzlichen Mindestkündigungsfristen von Art. 335b OR (Probezeit) und Art. 335c OR (nach der Probezeit) an. Ein Einzelarbeitsvertrag, ein Normalarbeitsvertrag oder ein Gesamtarbeitsvertrag kann längere Fristen vorsehen, nie kürzere (ausser bei einer vom Gesetz zugelassenen abweichenden Vereinbarung). Orientierendes Ergebnis, ersetzt keine Beratung durch eine auf Arbeitsrecht spezialisierte Anwältin bzw. einen Anwalt.",
        "dl_essai_label": "Befinden Sie sich noch in der Probezeit?",
        "dl_essai_oui": "Ja, noch in der Probezeit",
        "dl_essai_non": "Nein, die Probezeit ist beendet",
        "dl_date_engagement_label": "Beginn des Arbeitsverhältnisses",
        "dl_date_notification_label": "Datum der Kündigung",
        "dl_btn": "Kündigungsfrist berechnen",
        "dl_result_essai_prefix": "Kündigungsfrist während der Probezeit: 7 Tage. Ende des Arbeitsverhältnisses: ",
        "dl_result_essai_note": "Während der Probezeit kann die Kündigung auf jeden beliebigen Tag wirksam werden, nicht zwingend auf ein Monatsende (Art. 335b Abs. 1 OR).",
        "dl_result_normal_prefix": "Anwendbare Kündigungsfrist: ",
        "dl_result_normal_mois_1": "1 Monat (1. Dienstjahr)",
        "dl_result_normal_mois_2": "2 Monate (vom 2. bis zum 9. Dienstjahr)",
        "dl_result_normal_mois_3": "3 Monate (ab dem 10. Dienstjahr)",
        "dl_result_date_fin_prefix": "Ende des Arbeitsverhältnisses (Ende des Monats nach Ablauf der Frist): ",
        "dl_result_normal_note": "Sofern nichts anderes vereinbart ist, muss die Kündigung auf ein Monatsende erfolgen (Art. 335c Abs. 1 OR).",
        "dl_source": "Rechtsgrundlage: Art. 335b OR (7-tägige Kündigungsfrist während der Probezeit) und Art. 335c OR (Kündigungsfrist von 1, 2 oder 3 Monaten je nach Dienstjahren, auf ein Monatsende, nach der Probezeit).",
        # --- Free administrative-appeal deadline calculator ---
        "dr_heading": "Kostenloser Rechner für die Verwaltungsbeschwerdefrist",
        "dr_disclaimer": "Dieser Rechner wendet Art. 20 VwVG (Fristbeginn, Verschiebung bei Wochenende oder eidgenössischem Feiertag) und Art. 22a VwVG (Gerichtsferien) an. Er gilt nicht für Verfahren betreffend aufschiebende Wirkung, vorsorgliche Massnahmen oder öffentliches Beschaffungswesen, für die die Gerichtsferien nicht gelten (Art. 22a Abs. 2 VwVG). Geprüft werden nur das Wochenende und der 1. August, der einzige eidgenössisch anerkannte Feiertag: kantonale Feiertage sind separat zu prüfen, falls die betroffene Behörde kantonal ist. Orientierendes Ergebnis, vor wichtigen Handlungen zu bestätigen.",
        "dr_date_notif_label": "Datum der Eröffnung der Verfügung",
        "dr_jours_label": "Dauer der Beschwerdefrist (in Tagen, gemäss Verfügung oder anwendbarem Gesetz)",
        "dr_btn": "Fristende berechnen",
        "dr_result_prefix": "Die Beschwerdefrist endet am: ",
        "dr_source": "Rechtsgrundlage: Art. 20 Abs. 1 und 3 VwVG (Fristbeginn am Tag nach der Eröffnung, Verschiebung auf den nächsten Werktag, wenn der letzte Tag auf ein Wochenende oder den 1. August fällt) und Art. 22a VwVG (drei Gerichtsferien-Perioden, identisch mit Art. 145 ZPO: vom 7. Tag vor Ostern bis und mit dem 7. Tag nach Ostern, vom 15. Juli bis und mit 15. August, vom 18. Dezember bis und mit 2. Januar; ausser bei aufschiebender Wirkung, vorsorglichen Massnahmen und öffentlichem Beschaffungswesen, Art. 22a Abs. 2 VwVG).",
    },
    "it": {
        "presc_heading": "Calcolatore del termine di prescrizione",
        "presc_disclaimer": "Questo calcolatore applica i termini legali di base (art. 60, 127, 128 CO e art. 97 CP). Non tiene conto delle cause di sospensione o interruzione della prescrizione (art. 134 a 138 CO e disposizioni corrispondenti del CP), né di casi particolari. Il risultato è indicativo, non una consulenza legale.",
        "presc_type_label": "Tipo di credito o reato",
        "presc_opt_contrat": "Credito contrattuale generale (art. 127 CO, 10 anni)",
        "presc_opt_illicite": "Danno derivante da atto illecito (art. 60 CO)",
        "presc_opt_periodique": "Credito periodico: pigioni, interessi, salari (art. 128 CO, 5 anni)",
        "presc_opt_penal": "Reato penale (art. 97 CP)",
        "presc_date_exigible": "Data di esigibilità del credito",
        "presc_date_acte": "Data dell'atto dannoso",
        "presc_date_connaissance": "Data di conoscenza del danno e del suo autore",
        "presc_date_infraction": "Data del reato",
        "presc_peine_label": "Pena massima comminata",
        "presc_peine_vie": "Pena detentiva a vita (30 anni)",
        "presc_peine_plus3": "Pena detentiva superiore a 3 anni (15 anni)",
        "presc_peine_max3": "Pena detentiva fino a 3 anni (10 anni)",
        "presc_peine_autre": "Altro delitto (7 anni)",
        "presc_peine_contravention": "Contravvenzione (art. 109 CP, 3 anni)",
        "presc_btn": "Calcola la prescrizione",
        "presc_result_prefix": "Data di prescrizione stimata: ",
        "presc_result_illicite_note": " (prevale il termine più vicino, relativo o assoluto)",
        "presc_source_contrat": "Base legale: art. 127 CO, termine di prescrizione generale di 10 anni.",
        "presc_source_illicite": "Base legale: art. 60 cpv. 1 CO, termine relativo di 3 anni dalla conoscenza del danno e dell'autore, termine assoluto di 20 anni dall'atto dannoso (termine portato da 10 a 20 anni dalla revisione in vigore dal 1.1.2020).",
        "presc_source_periodique": "Base legale: art. 128 CO, termine di 5 anni per pigioni, interessi di capitali e altre prestazioni periodiche, nonché per i salari e altri crediti elencati da questa disposizione.",
        "presc_source_penal": "Base legale: art. 97 CP. Dalla revisione in vigore dal 2014, questi termini sono assoluti e non sono più interrotti da atti procedurali.",
        "delai_heading": "Calcolatore del termine di ricorso o procedurale",
        "delai_disclaimer": "Questo calcolatore applica l'art. 142 CPC (decorrenza, proroga in caso di fine settimana o giorno festivo federale) e l'art. 145 CPC (sospensione feriale). Vengono verificati solo il fine settimana e il 1° agosto, unico giorno festivo riconosciuto a livello federale (art. 20a LL): i giorni festivi cantonali e comunali della sede del tribunale devono essere verificati separatamente. Risultato indicativo, da confermare prima di qualsiasi atto procedurale importante.",
        "delai_date_comm_label": "Data della comunicazione o dell'evento scatenante",
        "delai_jours_label": "Durata del termine (in giorni)",
        "delai_procedure_label": "Tipo di procedura",
        "delai_opt_ordinaire": "Procedura ordinaria (si applica la sospensione feriale)",
        "delai_opt_sommaire": "Procedura di conciliazione o sommaria (nessuna sospensione, art. 145 cpv. 2 CPC)",
        "delai_btn": "Calcola la scadenza",
        "delai_result_prefix": "Il termine scade il: ",
        "delai_source": "Base legale: art. 142 cpv. 1 e 3 CPC (decorrenza dal giorno successivo alla comunicazione, proroga al primo giorno feriale successivo se l'ultimo giorno cade di sabato, domenica o il 1° agosto) e art. 145 CPC (tre periodi di sospensione feriale: dal 7° giorno prima di Pasqua al 7° giorno dopo Pasqua incluso, dal 15 luglio al 15 agosto incluso, dal 18 dicembre al 2 gennaio incluso).",
        "int_heading": "Calcolatore degli interessi moratori",
        "int_disclaimer": "Calcolo indicativo al tasso legale del 5% annuo (art. 104 CO), salvo tasso convenzionale diverso inserito. Il calcolo è effettuato in base al numero esatto di giorni, su base 365 giorni. Non sostituisce un conteggio stabilito da un tribunale o da una parte.",
        "int_capital_label": "Importo del credito (CHF)",
        "int_date_debut_label": "Decorrenza degli interessi (diffida o scadenza)",
        "int_date_fin_label": "Data finale del calcolo (spesso la data odierna o del pagamento)",
        "int_taux_label": "Tasso annuo (%)",
        "int_btn": "Calcola gli interessi",
        "int_result_interet": "Interessi moratori: ",
        "int_result_total": "Capitale più interessi: ",
        "int_result_jours": " su ",
        "int_result_jours_suffix": " giorni",
        "int_source": "Base legale: art. 104 cpv. 1 CO, tasso legale del 5% annuo salvo diverso accordo. La decorrenza inizia in linea di principio il giorno successivo alla scadenza pattuita, oppure il giorno successivo alla diffida se non è stata pattuita alcuna scadenza (art. 102 CO).",
        "date_placeholder_hint": "gg.mm.aaaa",
        "currency": "CHF",
        # --- Calcolatore multa eccesso di velocità (gratuito) ---
        "amende_heading": "Calcolatore gratuito di multa per eccesso di velocità",
        "amende_disclaimer": "Questo calcolatore applica il catalogo federale delle multe disciplinari (OAO) e le soglie di ritiro della licenza degli art. 16a-16c LCStr. Indicate il superamento già al netto della tolleranza di misurazione, come riportato sulla multa ricevuta. Oltre il tariffario fisso, la multa non è più determinata da una tariffa: viene fissata dal Ministero pubblico o da un tribunale. Risultato indicativo, non una consulenza legale.",
        "amende_zone_label": "Zona di circolazione",
        "amende_zone_localite": "All'interno di una località (limite 50 km/h)",
        "amende_zone_hors": "Fuori località (limite 80 km/h)",
        "amende_zone_autoroute": "Autostrada o semiautostrada (limite 100-120 km/h)",
        "amende_exces_label": "Superamento netto (km/h, tolleranza già dedotta)",
        "amende_exces_help": "Questo valore figura sulla multa ricevuta o può essere richiesto all'autorità che ha effettuato la misurazione.",
        "amende_btn": "Calcolare la multa",
        "amende_result_oao_prefix": "Multa disciplinare: ",
        "amende_result_oao_note": "Per una prima infrazione a questo livello non è previsto il ritiro della licenza (art. 16a LCStr).",
        "amende_result_moyen_title": "Infrazione media (art. 16b LCStr)",
        "amende_result_moyen_text": "Questo superamento supera il tariffario fisso delle multe disciplinari: comporta una denuncia penale, e la multa stessa è fissata dal Ministero pubblico, non da una tariffa. La licenza di condurre viene di norma ritirata per almeno un mese in caso di prima infrazione senza precedenti.",
        "amende_result_grave_title": "Infrazione grave (art. 16c LCStr)",
        "amende_result_grave_text": "Questo superamento raggiunge la soglia dell'infrazione grave. La licenza di condurre viene ritirata per almeno tre mesi, indipendentemente dai precedenti. La multa stessa non segue un tariffario fisso: spetta al Ministero pubblico o a un tribunale penale.",
        "amende_result_chauffard_title": "Reato da 'pirata della strada' (art. 90 cpv. 3-4 LCStr)",
        "amende_result_chauffard_text": "Questo superamento raggiunge la soglia del reato da 'pirata della strada' (caso standard: zone 50/80/120 km/h — le zone 30 e le semiautostrade hanno soglie diverse, non coperte da questo calcolatore). La pena prevista è una pena detentiva di almeno un anno, e la licenza viene ritirata per almeno due anni.",
        "amende_source": "Fonti: catalogo federale delle multe disciplinari (OAO); art. 16a-16c LCStr per le misure amministrative; art. 90 cpv. 3-4 LCStr per il reato da pirata della strada.",
        # --- Generatore gratuito di lettera di disdetta del contratto d'affitto ---
        "rb_heading": "Generatore gratuito di lettera di disdetta del contratto d'affitto",
        "rb_disclaimer": "Questo generatore redige una lettera di disdetta conforme agli usi e verifica solo il rispetto del termine legale minimo (3 mesi per un'abitazione, 6 mesi per un locale commerciale, art. 266c/266d CO). Non verifica se la data scelta corrisponde a un termine di disdetta valido secondo il vostro contratto o gli usi locali (di norma fine trimestre, o scadenza annuale indicata nel contratto). In caso di dubbio, fate confermare la data da un avvocato prima dell'invio.",
        "rb_type_label": "Tipo di contratto di locazione",
        "rb_type_habitation": "Abitazione (termine legale minimo: 3 mesi)",
        "rb_type_commercial": "Locale commerciale (termine legale minimo: 6 mesi)",
        "rb_nom_exp_label": "Il vostro nome",
        "rb_adresse_exp_label": "Il vostro indirizzo",
        "rb_nom_dest_label": "Nome del locatore o dell'amministrazione",
        "rb_adresse_dest_label": "Indirizzo del locatore o dell'amministrazione",
        "rb_objet_label": "Indirizzo dell'abitazione o del locale affittato",
        "rb_date_envoi_label": "Data di invio della lettera",
        "rb_date_fin_label": "Data di fine locazione desiderata",
        "rb_btn": "Generare la lettera",
        "rb_warning_delai": "Attenzione: tra la data di invio e la data di fine scelta non trascorrono i {mois} mesi richiesti dalla legge per questo tipo di locazione. Questa disdetta rischia di essere considerata valida per il termine successivo, non per quello indicato.",
        "rb_result_heading": "La vostra lettera (da rileggere, completare e firmare prima dell'invio)",
        "rb_copy_btn": "Copiare il testo",
        "rb_copy_done": "Copiato!",
        "rb_letter_object": "Disdetta del contratto di locazione relativo a {objet}",
        "rb_letter_greeting": "Egregio Signore, Gentile Signora,",
        "rb_letter_body1": "Con la presente vi comunico la disdetta del contratto di locazione che mi lega a voi per l'oggetto sopra indicato, con effetto dal {date_fin}.",
        "rb_letter_body2": "Vi prego di confermarmi per iscritto la ricezione della presente disdetta nonché la data di fine locazione ritenuta valida.",
        "rb_letter_body3": "Resto a disposizione per concordare una data per il sopralluogo di riconsegna.",
        "rb_letter_closing": "Distinti saluti",
        "rb_letter_recommande": "(da inviare preferibilmente per raccomandata, per provare la data di invio)",
        "rb_source": "Base legale: art. 266c CO (abitazioni, termine di 3 mesi) e art. 266d CO (locali commerciali, termine di 6 mesi), per il prossimo termine legale o contrattuale.",
        # --- Free child-support (pension alimentaire) estimator ---
        "pa_heading": "Calcolatore gratuito degli alimenti per i figli",
        "pa_disclaimer": "Importante: in Svizzera non esiste una formula legale fissa per calcolare gli alimenti per i figli. Il Tribunale federale impone un metodo in due fasi (DTF 147 III 265) che lascia un ampio margine di apprezzamento al giudice riguardo ai bisogni concreti e al reddito ipotetico. Questo simulatore applica una versione semplificata e illustrativa di tale metodo, con gli importi base del minimo vitale LEF e una ripartizione secondo il metodo delle \"teste grandi / teste piccole\", presentata come una convenzione tra altre, mai come una regola legale. Inserite i vostri importi reali: nulla viene ipotizzato.",
        "pa_children_heading": "Figli interessati",
        "pa_children_under10_label": "Numero di figli sotto i 10 anni",
        "pa_children_10plus_label": "Numero di figli dai 10 anni in su",
        "pa_creancier_heading": "Genitore affidatario principale",
        "pa_creancier_revenu_label": "Reddito netto mensile (CHF)",
        "pa_creancier_loyer_label": "Spese di alloggio mensili (CHF)",
        "pa_creancier_assurance_label": "Premio mensile dell'assicurazione malattia di base (CHF)",
        "pa_creancier_charges_label": "Altre spese mensili giustificate (CHF, facoltativo)",
        "pa_debiteur_heading": "Genitore che verserebbe gli alimenti",
        "pa_debiteur_situation_label": "Situazione del genitore debitore",
        "pa_debiteur_situation_seul": "Vive solo/a",
        "pa_debiteur_situation_couple": "Vive in coppia / economia domestica comune",
        "pa_debiteur_revenu_label": "Reddito netto mensile (CHF)",
        "pa_debiteur_loyer_label": "Spese di alloggio mensili (CHF)",
        "pa_debiteur_assurance_label": "Premio mensile dell'assicurazione malattia di base (CHF)",
        "pa_debiteur_charges_label": "Altre spese mensili giustificate (CHF, facoltativo)",
        "pa_btn": "Stimare gli alimenti",
        "pa_result_heading": "Stima indicativa",
        "pa_result_pension_prefix": "Alimenti mensili indicativi: ",
        "pa_result_detail_enfants": "Minimo vitale dei figli (base LEF): ",
        "pa_result_detail_excedent_positif": "Eccedenza familiare disponibile ripartita secondo il metodo \"teste grandi / teste piccole\": ",
        "pa_result_detail_excedent_nul": "Nessuna eccedenza familiare disponibile: si tiene conto solo del minimo vitale dei figli, entro il limite del disponibile del genitore debitore.",
        "pa_result_insufficient": "In base agli importi inseriti, il genitore debitore non dispone di un reddito superiore al proprio minimo vitale per versare gli alimenti. In tal caso, il giudice può valutare di imputargli un reddito ipotetico se ritiene che potrebbe ragionevolmente guadagnare di più. Consultate un avvocato specializzato in diritto di famiglia.",
        "pa_result_capped": "L'importo indicativo calcolato per i figli ({montant} CHF) supera quanto il genitore debitore può versare senza scendere sotto il proprio minimo vitale. L'importo indicato sopra è quindi limitato al suo disponibile effettivo.",
        "pa_source": "Metodo: DTF 147 III 265 (minimo vitale secondo le linee guida LEF, poi ripartizione dell'eccedenza). Importi base del minimo vitale: Conferenza dei preposti agli uffici d'esecuzione e fallimenti della Svizzera. Risultato puramente indicativo, non sostituisce una consulenza presso un avvocato specializzato in diritto di famiglia.",
        # --- Free debt-collection (poursuite) fee calculator ---
        "fp_heading": "Calcolatore gratuito delle spese di esecuzione (precetto esecutivo)",
        "fp_disclaimer": "Questo calcolatore applica il tariffario ufficiale della tassa per la redazione, l'allestimento e la notificazione di un precetto esecutivo (art. 16 cpv. 1 OTLEF), in vigore dal 1° gennaio 2026. Non copre eventuali spese supplementari (tentativo di notificazione, doppio esemplare, opposizione, continuazione dell'esecuzione, pignoramento).",
        "fp_montant_label": "Importo del credito fatto valere (CHF)",
        "fp_btn": "Calcolare le spese",
        "fp_result_prefix": "Tassa per il precetto esecutivo: ",
        "fp_result_avance": "Questa tassa è anticipata dal creditore al momento del deposito della domanda d'esecuzione, poi posta definitivamente a carico del debitore escusso se l'esecuzione va a buon fine (art. 68 LEF).",
        "fp_source": "Fonte: art. 16 cpv. 1 OTLEF (ordinanza sulle tasse riscosse in applicazione della LEF), testo in vigore dal 1° gennaio 2026 (RU 2025 630); art. 68 LEF per l'anticipo e la ripartizione finale delle spese.",
        # --- Free sublease consent-request letter generator ---
        "sl_heading": "Generatore gratuito di richiesta di sublocazione",
        "sl_disclaimer": "La sublocazione di un'abitazione richiede il consenso scritto preventivo del locatore (art. 262 CO). Questo generatore prepara una lettera di richiesta di consenso e segnala una pigione di sublocazione potenzialmente abusiva, ma non sostituisce una consulenza presso un avvocato specializzato in diritto della locazione.",
        "sl_bailleur_nom_label": "Nome del locatore o dell'amministrazione",
        "sl_bailleur_adresse_label": "Indirizzo del locatore o dell'amministrazione",
        "sl_locataire_nom_label": "Il vostro nome (conduttore principale)",
        "sl_locataire_adresse_label": "Il vostro indirizzo",
        "sl_objet_label": "Indirizzo dell'abitazione locata",
        "sl_souslocataire_nom_label": "Nome del subconduttore previsto",
        "sl_date_debut_label": "Data d'inizio della sublocazione",
        "sl_date_fin_label": "Data di fine della sublocazione (lasciare vuoto se indeterminata)",
        "sl_loyer_principal_label": "Pigione principale mensile attuale (CHF)",
        "sl_loyer_sous_label": "Pigione di sublocazione mensile prevista (CHF)",
        "sl_btn": "Generare la richiesta",
        "sl_warning_abusif": "Attenzione: la pigione di sublocazione prevista supera di oltre il 20% la pigione principale. Secondo la giurisprudenza (DTF 119 II 353), una maggiorazione di questo ordine è di norma ammessa solo per un'abitazione ammobiliata o con prestazioni supplementari; altrimenti questa pigione rischia di essere considerata abusiva e contestabile dal locatore o dal subconduttore.",
        "sl_result_heading": "La vostra lettera (da rileggere, completare e firmare)",
        "sl_copy_btn": "Copiare il testo",
        "sl_copy_done": "Copiato!",
        "sl_letter_object": "Richiesta di consenso alla sublocazione di {objet}",
        "sl_letter_greeting": "Gentile Signora, Egregio Signore,",
        "sl_letter_body1": "Vi informo del mio desiderio di sublocare l'abitazione summenzionata a {souslocataire}, a partire dal {date_debut}{date_fin_suffix}, con una pigione di sublocazione di CHF {loyer_sous} al mese (pigione principale attuale: CHF {loyer_principal} al mese).",
        "sl_letter_date_fin_suffix": " fino al {date_fin}",
        "sl_letter_body2": "Conformemente all'art. 262 CO, vi sarei grato di comunicarmi per iscritto il vostro consenso a questa sublocazione, o gli eventuali motivi di rifiuto.",
        "sl_letter_body3": "Resto a vostra disposizione per ogni ulteriore informazione.",
        "sl_letter_closing": "Con i migliori saluti.",
        "sl_source": "Base legale: art. 262 CO (consenso scritto del locatore, motivi di rifiuto tassativi al cpv. 2); DTF 119 II 353 sulla soglia di maggiorazione ammessa per un'abitazione ammobiliata.",
        # --- Free forced-heirship (réserve héréditaire) calculator ---
        "rh_heading": "Calcolatore gratuito della legittima ereditaria",
        "rh_disclaimer": "Questo calcolatore applica le quote legali della legittima dopo la revisione del diritto successorio entrata in vigore il 1° gennaio 2023 (art. 470 e 471 CC). Copre le configurazioni familiari più comuni, senza considerare i casi particolari (eredi di grado più lontano, patto successorio, regime dei beni da liquidare prima). Risultato indicativo, non sostituisce una consulenza presso un avvocato specializzato in diritto successorio.",
        "rh_situation_label": "Situazione familiare",
        "rh_situation_conjoint_descendants": "Coniuge (o partner registrato) superstite e discendenti",
        "rh_situation_conjoint_parents": "Coniuge (o partner registrato) superstite e genitori (senza discendenti)",
        "rh_situation_conjoint_seul": "Solo coniuge (o partner registrato) superstite (senza discendenti né genitori in vita)",
        "rh_situation_descendants_seuls": "Solo discendenti (senza coniuge superstite)",
        "rh_situation_parents_seuls": "Solo genitori (senza coniuge superstite né discendenti)",
        "rh_nb_enfants_label": "Numero di figli (o stirpi di discendenti)",
        "rh_btn": "Calcolare la legittima",
        "rh_result_heading": "Ripartizione indicativa",
        "rh_result_reserve_conjoint": "Legittima del coniuge / partner registrato: ",
        "rh_result_reserve_descendants": "Legittima totale dei discendenti: ",
        "rh_result_reserve_descendants_chacun": "Legittima per ciascun figlio: ",
        "rh_result_reserve_parents": "Legittima dei genitori: 0 (soppressa dal 1.1.2023)",
        "rh_result_quotite_disponible": "Quota disponibile (liberamente attribuibile per testamento): ",
        "rh_source": "Base legale: art. 470 e 471 CC (legittima dopo la revisione entrata in vigore il 1.1.2023); art. 462 CC (quote legali tra eredi). Legittima del coniuge/partner e dei discendenti ridotta alla metà della loro quota legale; legittima dei genitori interamente soppressa.",
        # --- Free lease notice-period (délai de congé) checker ---
        "dc_heading": "Calcolatore gratuito del termine di disdetta dell'affitto",
        "dc_disclaimer": "Questo calcolatore verifica solo il rispetto del termine legale minimo di preavviso (art. 266c/266d CO) a partire dalla vostra data di invio della disdetta. Non verifica se la data ottenuta corrisponda a una scadenza valida secondo il vostro contratto o gli usi locali (spesso la fine di un trimestre): verificatelo separatamente.",
        "dc_type_label": "Tipo di locazione",
        "dc_type_habitation": "Abitazione (termine legale minimo: 3 mesi)",
        "dc_type_commercial": "Locale commerciale (termine legale minimo: 6 mesi)",
        "dc_date_envoi_label": "Data di invio (o di invio previsto) della disdetta",
        "dc_btn": "Calcolare la data più vicina possibile",
        "dc_result_prefix": "Data più vicina possibile per la fine della locazione: ",
        "dc_result_note": "Questa data corrisponde al rigoroso termine legale minimo dopo il vostro invio. Deve ancora corrispondere a una scadenza valida per il vostro contratto (contrattuale o d'uso locale): altrimenti la disdetta è rinviata alla scadenza successiva.",
        "dc_source": "Base legale: art. 266c CO (abitazioni, termine minimo di 3 mesi) e art. 266d CO (locali commerciali, termine minimo di 6 mesi), per il prossimo termine legale o contrattuale.",
        # --- Free formal-notice (mise en demeure) letter generator ---
        "md_heading": "Generatore gratuito di diffida di pagamento",
        "md_disclaimer": "Questo generatore prepara una diffida formale (costituzione in mora ai sensi dell'art. 102 CO) per richiedere il pagamento di una somma dovuta, con un termine di grazia e un promemoria dell'interesse di mora legale (art. 104 CO). Non sostituisce una consulenza presso un avvocato, in particolare se il debitore contesta il credito.",
        "md_creancier_nom_label": "Il vostro nome (creditore)",
        "md_creancier_adresse_label": "Il vostro indirizzo",
        "md_debiteur_nom_label": "Nome del debitore",
        "md_debiteur_adresse_label": "Indirizzo del debitore",
        "md_objet_label": "Oggetto del credito (es.: fattura n. 123 del 1° marzo 2026)",
        "md_montant_label": "Importo dovuto (CHF)",
        "md_delai_grace_label": "Termine di grazia concesso (giorni, a partire dall'invio)",
        "md_btn": "Generare la diffida",
        "md_result_heading": "La vostra lettera (da rileggere, completare e firmare)",
        "md_copy_btn": "Copiare il testo",
        "md_copy_done": "Copiato!",
        "md_letter_object": "Diffida di pagamento — {objet}",
        "md_letter_greeting": "Gentile Signora, Egregio Signore,",
        "md_letter_body1": "Nonostante i nostri precedenti solleciti, constato che l'importo di CHF {montant} relativo a {objet} risulta a tutt'oggi non pagato.",
        "md_letter_body2": "Con la presente vi metto formalmente in mora, invitandovi a saldare tale importo entro {delai} giorni dalla data di invio di questa lettera, ossia al più tardi entro il {date_limite}.",
        "md_letter_body3": "In mancanza di pagamento entro tale termine, sarà richiesto un interesse di mora del 5% annuo a partire dalla presente diffida, conformemente all'art. 104 CO, e potrà essere avviata una procedura esecutiva senza ulteriore avviso.",
        "md_letter_closing": "Con i migliori saluti.",
        "md_source": "Base legale: art. 102 CO (costituzione in mora mediante diffida del creditore); art. 104 CO (interesse di mora legale del 5% annuo dalla mora, salvo diverso accordo).",
        # --- Free employment notice-period calculator ---
        "dl_heading": "Calcolatore gratuito del termine di disdetta del contratto di lavoro",
        "dl_disclaimer": "Questo calcolatore applica i termini legali minimi di disdetta dell'art. 335b CO (tempo di prova) e dell'art. 335c CO (dopo il tempo di prova). Un contratto individuale, un contratto normale di lavoro o un contratto collettivo può prevedere termini più lunghi, mai più brevi (salvo un accordo diverso ammesso dalla legge). Risultato indicativo, non sostituisce una consulenza presso un avvocato specializzato in diritto del lavoro.",
        "dl_essai_label": "Siete ancora in tempo di prova?",
        "dl_essai_oui": "Sì, ancora in tempo di prova",
        "dl_essai_non": "No, il tempo di prova è terminato",
        "dl_date_engagement_label": "Data di inizio del rapporto di lavoro",
        "dl_date_notification_label": "Data di notifica della disdetta",
        "dl_btn": "Calcolare il termine di disdetta",
        "dl_result_essai_prefix": "Termine di disdetta durante il tempo di prova: 7 giorni. Data di fine del rapporto di lavoro: ",
        "dl_result_essai_note": "Durante il tempo di prova, la disdetta può avere effetto in qualsiasi giorno, non necessariamente a fine mese (art. 335b cpv. 1 CO).",
        "dl_result_normal_prefix": "Termine di disdetta applicabile: ",
        "dl_result_normal_mois_1": "1 mese (1° anno di servizio)",
        "dl_result_normal_mois_2": "2 mesi (dal 2° al 9° anno di servizio)",
        "dl_result_normal_mois_3": "3 mesi (dal 10° anno di servizio)",
        "dl_result_date_fin_prefix": "Data di fine del rapporto di lavoro (fine del mese successivo alla scadenza del termine): ",
        "dl_result_normal_note": "Salvo diverso accordo, la disdetta deve essere data per la fine di un mese (art. 335c cpv. 1 CO).",
        "dl_source": "Base legale: art. 335b CO (termine di disdetta di 7 giorni durante il tempo di prova) e art. 335c CO (termine di disdetta di 1, 2 o 3 mesi secondo l'anzianità, per la fine di un mese, dopo il tempo di prova).",
        # --- Free administrative-appeal deadline calculator ---
        "dr_heading": "Calcolatore gratuito del termine di ricorso amministrativo",
        "dr_disclaimer": "Questo calcolatore applica l'art. 20 PA (decorrenza, proroga in caso di fine settimana o giorno festivo federale) e l'art. 22a PA (sospensione feriale). Non si applica alle procedure di effetto sospensivo, misure cautelari o appalti pubblici, per le quali la sospensione feriale non si applica (art. 22a cpv. 2 PA). Vengono verificati solo il fine settimana e il 1° agosto, unico giorno festivo riconosciuto a livello federale: i giorni festivi cantonali devono essere verificati separatamente se l'autorità interessata è cantonale. Risultato indicativo, da confermare prima di qualsiasi atto importante.",
        "dr_date_notif_label": "Data di notifica della decisione",
        "dr_jours_label": "Durata del termine di ricorso (in giorni, indicata nella decisione o dalla legge applicabile)",
        "dr_btn": "Calcolare la scadenza",
        "dr_result_prefix": "Il termine di ricorso scade il: ",
        "dr_source": "Base legale: art. 20 cpv. 1 e 3 PA (decorrenza dal giorno successivo alla notifica, proroga al primo giorno feriale successivo se l'ultimo giorno cade di fine settimana o il 1° agosto) e art. 22a PA (tre periodi di sospensione feriale, identici all'art. 145 CPC: dal 7° giorno prima di Pasqua al 7° giorno dopo Pasqua incluso, dal 15 luglio al 15 agosto incluso, dal 18 dicembre al 2 gennaio incluso; salvo effetto sospensivo, misure cautelari e appalti pubblici, art. 22a cpv. 2 PA).",
    },
    "en": {
        "presc_heading": "Statute of limitations calculator",
        "presc_disclaimer": "This calculator applies the basic statutory periods (art. 60, 127, 128 CO and art. 97 CC). It does not account for causes of suspension or interruption of limitation (art. 134 to 138 CO and corresponding provisions of the Criminal Code), nor for special cases. The result is indicative, not legal advice.",
        "presc_type_label": "Type of claim or offence",
        "presc_opt_contrat": "General contractual claim (art. 127 CO, 10 years)",
        "presc_opt_illicite": "Damage from an unlawful act (art. 60 CO)",
        "presc_opt_periodique": "Periodic claim: rent, interest, wages (art. 128 CO, 5 years)",
        "presc_opt_penal": "Criminal offence (art. 97 Criminal Code)",
        "presc_date_exigible": "Date the claim became due",
        "presc_date_acte": "Date of the harmful act",
        "presc_date_connaissance": "Date the loss and the liable person became known",
        "presc_date_infraction": "Date of the offence",
        "presc_peine_label": "Maximum penalty incurred",
        "presc_peine_vie": "Life imprisonment (30 years)",
        "presc_peine_plus3": "Custodial sentence of more than 3 years (15 years)",
        "presc_peine_max3": "Custodial sentence of up to 3 years (10 years)",
        "presc_peine_autre": "Other offence (7 years)",
        "presc_peine_contravention": "Minor offence / contravention (art. 109 Criminal Code, 3 years)",
        "presc_btn": "Calculate the limitation date",
        "presc_result_prefix": "Estimated limitation date: ",
        "presc_result_illicite_note": " (whichever of the relative or absolute deadline comes first applies)",
        "presc_source_contrat": "Legal basis: art. 127 CO, general limitation period of 10 years.",
        "presc_source_illicite": "Legal basis: art. 60 para. 1 CO, relative period of 3 years from knowledge of the loss and the liable person, absolute period of 20 years from the harmful act (extended from 10 to 20 years by the revision in force since 1 January 2020).",
        "presc_source_periodique": "Legal basis: art. 128 CO, 5-year period for rent, capital interest and other periodic performances, as well as for wages and other claims listed in this provision.",
        "presc_source_penal": "Legal basis: art. 97 Criminal Code. Since the revision in force since 2014, these periods are absolute and are no longer interrupted by procedural acts.",
        "delai_heading": "Appeal or procedural deadline calculator",
        "delai_disclaimer": "This calculator applies art. 142 CPC (starting point, extension for weekends or a federal public holiday) and art. 145 CPC (court recess periods). It only checks weekends and 1 August, the only public holiday recognised at federal level (art. 20a Employment Act): cantonal and municipal public holidays at the seat of the court must be checked separately. Indicative result, to be confirmed before any significant procedural step.",
        "delai_date_comm_label": "Date of the notice or triggering event",
        "delai_jours_label": "Length of the deadline (in days)",
        "delai_procedure_label": "Type of proceedings",
        "delai_opt_ordinaire": "Ordinary proceedings (court recess periods apply)",
        "delai_opt_sommaire": "Conciliation or summary proceedings (no recess periods, art. 145 para. 2 CPC)",
        "delai_btn": "Calculate the deadline",
        "delai_result_prefix": "The deadline expires on: ",
        "delai_source": "Legal basis: art. 142 para. 1 and 3 CPC (starts the day after notice, extended to the next business day if the last day falls on a weekend or 1 August) and art. 145 CPC (three recess periods: from the 7th day before Easter to the 7th day after Easter inclusive, from 15 July to 15 August inclusive, from 18 December to 2 January inclusive).",
        "int_heading": "Late payment interest calculator",
        "int_disclaimer": "Indicative calculation at the statutory rate of 5% per year (art. 104 CO), unless a different agreed rate is entered. The calculation is prorated to the exact number of days, on a 365-day basis. Does not replace a statement produced by a court or a party.",
        "int_capital_label": "Amount of the claim (CHF)",
        "int_date_debut_label": "Start of interest accrual (formal notice or due date)",
        "int_date_fin_label": "End date of the calculation (often today's date or the payment date)",
        "int_taux_label": "Annual rate (%)",
        "int_btn": "Calculate the interest",
        "int_result_interet": "Late payment interest: ",
        "int_result_total": "Principal plus interest: ",
        "int_result_jours": " over ",
        "int_result_jours_suffix": " days",
        "int_source": "Legal basis: art. 104 para. 1 CO, statutory rate of 5% per year unless otherwise agreed. Interest generally starts accruing the day after the agreed due date, or the day after formal notice (mise en demeure) if no due date was agreed (art. 102 CO).",
        "date_placeholder_hint": "dd.mm.yyyy",
        "currency": "CHF",
        # --- Free speeding fine calculator ---
        "amende_heading": "Free speeding fine calculator",
        "amende_disclaimer": "This calculator applies the federal fixed-penalty fine schedule (OAO) and the licence withdrawal thresholds of art. 16a to 16c LCR (Road Traffic Act). Enter the overage already net of measurement tolerance, as shown on the fine you received. Beyond the fixed schedule, the fine is no longer set by a tariff: it is determined by the public prosecutor or a court. Indicative result, not legal advice.",
        "amende_zone_label": "Traffic zone",
        "amende_zone_localite": "Inside a built-up area (50 km/h limit)",
        "amende_zone_hors": "Outside a built-up area (80 km/h limit)",
        "amende_zone_autoroute": "Motorway or semi-motorway (100-120 km/h limit)",
        "amende_exces_label": "Net overage (km/h, tolerance already deducted)",
        "amende_exces_help": "This figure appears on the fine you received, or can be requested from the authority that measured the speed.",
        "amende_btn": "Calculate the fine",
        "amende_result_oao_prefix": "Fixed-penalty fine: ",
        "amende_result_oao_note": "No licence withdrawal is expected for a first offence at this level (art. 16a LCR).",
        "amende_result_moyen_title": "Moderate offence (art. 16b LCR)",
        "amende_result_moyen_text": "This overage exceeds the fixed fine schedule: it is referred for criminal prosecution, and the fine itself is set by the public prosecutor, not by a tariff. The driving licence is typically withdrawn for at least one month for a first offence with no prior record.",
        "amende_result_grave_title": "Serious offence (art. 16c LCR)",
        "amende_result_grave_text": "This overage reaches the serious-offence threshold. The driving licence is withdrawn for at least three months regardless of prior record. The fine itself does not follow a fixed schedule: it is for the public prosecutor or a criminal court to decide.",
        "amende_result_chauffard_title": "Reckless-driving offence (art. 90 para. 3-4 LCR)",
        "amende_result_chauffard_text": "This overage reaches the reckless-driving threshold (standard case: 50/80/120 km/h zones — 30 km/h zones and semi-motorways have different thresholds not covered by this calculator). The penalty is a custodial sentence of at least one year, and the driving licence is withdrawn for at least two years.",
        "amende_source": "Sources: federal fixed-penalty fine schedule (OAO); art. 16a to 16c LCR for administrative measures; art. 90 para. 3-4 LCR for the reckless-driving offence.",
        # --- Free lease termination letter generator ---
        "rb_heading": "Free lease termination letter generator",
        "rb_disclaimer": "This generator drafts a standard termination letter and only checks compliance with the minimum legal notice period (3 months for housing, 6 months for commercial premises, art. 266c/266d CO). It does not check whether the chosen date matches a valid termination date under your lease or local usage (usually the end of a quarter, or the annual date stated in the lease). If in doubt, have the date confirmed by a lawyer before sending.",
        "rb_type_label": "Type of lease",
        "rb_type_habitation": "Housing (minimum legal notice: 3 months)",
        "rb_type_commercial": "Commercial premises (minimum legal notice: 6 months)",
        "rb_nom_exp_label": "Your name",
        "rb_adresse_exp_label": "Your address",
        "rb_nom_dest_label": "Landlord's or agency's name",
        "rb_adresse_dest_label": "Landlord's or agency's address",
        "rb_objet_label": "Address of the rented housing or premises",
        "rb_date_envoi_label": "Date the letter is sent",
        "rb_date_fin_label": "Desired end-of-lease date",
        "rb_btn": "Generate the letter",
        "rb_warning_delai": "Warning: between the sending date and the chosen end date, there are not the {mois} months required by law for this type of lease. This notice risks being treated as valid for the following term, not the one you indicated.",
        "rb_result_heading": "Your letter (review, complete and sign before sending)",
        "rb_copy_btn": "Copy the text",
        "rb_copy_done": "Copied!",
        "rb_letter_object": "Termination of the lease for {objet}",
        "rb_letter_greeting": "Dear Sir or Madam,",
        "rb_letter_body1": "I hereby give notice of termination of the lease agreement binding me to you for the above-mentioned premises, effective {date_fin}.",
        "rb_letter_body2": "Please confirm in writing receipt of this notice and the termination date thereby retained.",
        "rb_letter_body3": "I remain available to arrange a date for the move-out inspection.",
        "rb_letter_closing": "Yours faithfully,",
        "rb_letter_recommande": "(preferably send by registered mail, to prove the sending date)",
        "rb_source": "Legal basis: art. 266c CO (housing, 3-month notice) and art. 266d CO (commercial premises, 6-month notice), for the next legal or contractual term.",
        # --- Free child-support (pension alimentaire) estimator ---
        "pa_heading": "Free child support (pension alimentaire) estimator",
        "pa_disclaimer": "Important: there is no fixed legal formula for calculating child support in Switzerland. The Federal Supreme Court requires a two-stage method (ATF 147 III 265) that leaves the court wide discretion over concrete needs and hypothetical income. This simulator applies a simplified, illustrative version of that method, using the debt-enforcement (LP) minimum-subsistence base amounts and a \"big heads / small heads\" surplus distribution presented as one convention among others, never as a legal rule. Enter your own real figures: nothing is guessed.",
        "pa_children_heading": "Children concerned",
        "pa_children_under10_label": "Number of children under 10",
        "pa_children_10plus_label": "Number of children 10 or older",
        "pa_creancier_heading": "Parent with primary custody",
        "pa_creancier_revenu_label": "Net monthly income (CHF)",
        "pa_creancier_loyer_label": "Monthly housing cost (CHF)",
        "pa_creancier_assurance_label": "Monthly basic health-insurance premium (CHF)",
        "pa_creancier_charges_label": "Other justified monthly expenses (CHF, optional)",
        "pa_debiteur_heading": "Parent who would pay support",
        "pa_debiteur_situation_label": "Situation of the paying parent",
        "pa_debiteur_situation_seul": "Lives alone",
        "pa_debiteur_situation_couple": "Lives with a partner / shared household",
        "pa_debiteur_revenu_label": "Net monthly income (CHF)",
        "pa_debiteur_loyer_label": "Monthly housing cost (CHF)",
        "pa_debiteur_assurance_label": "Monthly basic health-insurance premium (CHF)",
        "pa_debiteur_charges_label": "Other justified monthly expenses (CHF, optional)",
        "pa_btn": "Estimate support",
        "pa_result_heading": "Indicative estimate",
        "pa_result_pension_prefix": "Indicative monthly child support: ",
        "pa_result_detail_enfants": "Children's minimum subsistence (LP base): ",
        "pa_result_detail_excedent_positif": "Available family surplus distributed via the \"big heads / small heads\" method: ",
        "pa_result_detail_excedent_nul": "No available family surplus: only the children's minimum subsistence is taken into account, capped by what the paying parent has available.",
        "pa_result_insufficient": "Based on the figures entered, the paying parent has no income above their own minimum subsistence to pay child support. In that case, the court may consider imputing a hypothetical income if it judges the parent could reasonably earn more. Consult a lawyer specialising in family law.",
        "pa_result_capped": "The indicative amount calculated for the children ({montant} CHF) exceeds what the paying parent can pay without falling below their own minimum subsistence. The amount shown above is therefore capped at their actual available income.",
        "pa_source": "Method: ATF 147 III 265 (minimum subsistence per LP guidelines, then surplus distribution). Minimum-subsistence base amounts: Conference of Swiss Debt Enforcement and Bankruptcy Officers. Purely indicative result, does not replace a consultation with a lawyer specialising in family law.",
        # --- Free debt-collection (poursuite) fee calculator ---
        "fp_heading": "Free debt-collection fee calculator (payment order)",
        "fp_disclaimer": "This calculator applies the official fee schedule for drafting, preparing and serving a payment order (\"commandement de payer\", art. 16 para. 1 OELP), in force since 1 January 2026. It does not cover any additional costs (service attempt, extra copy, opposition, continuation of the collection proceeding, seizure).",
        "fp_montant_label": "Amount of the claim (CHF)",
        "fp_btn": "Calculate the fee",
        "fp_result_prefix": "Fee for the payment order: ",
        "fp_result_avance": "This fee is advanced by the creditor when filing the collection request, and is ultimately charged to the debtor if the collection proceeding succeeds (art. 68 LP).",
        "fp_source": "Source: art. 16 para. 1 OELP (ordinance on fees under the federal debt-enforcement and bankruptcy act), text in force since 1 January 2026 (RO 2025 630); art. 68 LP for the advance and final allocation of costs.",
        # --- Free sublease consent-request letter generator ---
        "sl_heading": "Free sublease consent-request letter generator",
        "sl_disclaimer": "Subletting a home requires the landlord's prior written consent (art. 262 CO). This generator prepares a consent-request letter and flags a potentially abusive sublease rent, but does not replace a consultation with a lawyer specialising in tenancy law.",
        "sl_bailleur_nom_label": "Landlord's or agency's name",
        "sl_bailleur_adresse_label": "Landlord's or agency's address",
        "sl_locataire_nom_label": "Your name (main tenant)",
        "sl_locataire_adresse_label": "Your address",
        "sl_objet_label": "Address of the rented home",
        "sl_souslocataire_nom_label": "Name of the intended subtenant",
        "sl_date_debut_label": "Sublease start date",
        "sl_date_fin_label": "Sublease end date (leave blank if open-ended)",
        "sl_loyer_principal_label": "Current monthly main rent (CHF)",
        "sl_loyer_sous_label": "Intended monthly sublease rent (CHF)",
        "sl_btn": "Generate the request",
        "sl_warning_abusif": "Warning: the intended sublease rent exceeds the main rent by more than 20%. Under case law (ATF 119 II 353), a mark-up of this size is generally only accepted for furnished accommodation or one that comes with extra services; otherwise this rent risks being considered abusive and challengeable by the landlord or the subtenant.",
        "sl_result_heading": "Your letter (review, complete and sign before sending)",
        "sl_copy_btn": "Copy the text",
        "sl_copy_done": "Copied!",
        "sl_letter_object": "Request for consent to sublet {objet}",
        "sl_letter_greeting": "Dear Sir or Madam,",
        "sl_letter_body1": "I am writing to inform you of my wish to sublet the above-mentioned home to {souslocataire}, starting {date_debut}{date_fin_suffix}, for a sublease rent of CHF {loyer_sous} per month (current main rent: CHF {loyer_principal} per month).",
        "sl_letter_date_fin_suffix": " until {date_fin}",
        "sl_letter_body2": "In accordance with art. 262 CO, I would be grateful if you could confirm your consent to this sublease in writing, or state your reasons for refusal if applicable.",
        "sl_letter_body3": "I remain available for any further information.",
        "sl_letter_closing": "Yours faithfully,",
        "sl_source": "Legal basis: art. 262 CO (landlord's written consent, exhaustive refusal grounds in para. 2); ATF 119 II 353 on the accepted mark-up threshold for furnished accommodation.",
        # --- Free forced-heirship (réserve héréditaire) calculator ---
        "rh_heading": "Free forced-heirship (réserve héréditaire) calculator",
        "rh_disclaimer": "This calculator applies the statutory forced-heirship fractions since the succession-law revision that came into force on 1 January 2023 (art. 470 and 471 CC). It covers the most common family configurations, without accounting for special cases (more distant heirs, inheritance contracts, a matrimonial-property regime to be settled first). Indicative result, does not replace a consultation with a lawyer specialising in inheritance law.",
        "rh_situation_label": "Family situation",
        "rh_situation_conjoint_descendants": "Surviving spouse (or registered partner) and descendants",
        "rh_situation_conjoint_parents": "Surviving spouse (or registered partner) and parents (no descendants)",
        "rh_situation_conjoint_seul": "Surviving spouse (or registered partner) alone (no descendants or surviving parents)",
        "rh_situation_descendants_seuls": "Descendants alone (no surviving spouse)",
        "rh_situation_parents_seuls": "Parents alone (no surviving spouse or descendants)",
        "rh_nb_enfants_label": "Number of children (or lines of descendants)",
        "rh_btn": "Calculate the forced share",
        "rh_result_heading": "Indicative breakdown",
        "rh_result_reserve_conjoint": "Forced share of the spouse / registered partner: ",
        "rh_result_reserve_descendants": "Total forced share of the descendants: ",
        "rh_result_reserve_descendants_chacun": "Forced share per child: ",
        "rh_result_reserve_parents": "Forced share of the parents: 0 (abolished since 1.1.2023)",
        "rh_result_quotite_disponible": "Freely disposable portion (assignable by will): ",
        "rh_source": "Legal basis: art. 470 and 471 CC (forced heirship since the revision in force from 1.1.2023); art. 462 CC (statutory shares among heirs). The forced share of the spouse/partner and of descendants is reduced to half of their statutory share; the forced share of parents is entirely abolished.",
        # --- Free lease notice-period (délai de congé) checker ---
        "dc_heading": "Free lease notice-period calculator",
        "dc_disclaimer": "This calculator only checks compliance with the minimum legal notice period (art. 266c/266d CO) from your notice-sending date. It does not check whether the resulting date matches a valid term under your lease or local usage (often the end of a quarter): check this separately.",
        "dc_type_label": "Type of lease",
        "dc_type_habitation": "Housing (minimum legal notice: 3 months)",
        "dc_type_commercial": "Commercial premises (minimum legal notice: 6 months)",
        "dc_date_envoi_label": "Date the notice is (or will be) sent",
        "dc_btn": "Calculate the earliest possible date",
        "dc_result_prefix": "Earliest possible end date for the lease: ",
        "dc_result_note": "This date reflects the strict minimum legal notice period after you send notice. It still needs to match a valid term for your lease (contractual or local usage): otherwise the notice is postponed to the next term.",
        "dc_source": "Legal basis: art. 266c CO (housing, 3-month minimum notice) and art. 266d CO (commercial premises, 6-month minimum notice), for the next legal or contractual term.",
        # --- Free formal-notice (mise en demeure) letter generator ---
        "md_heading": "Free formal-notice (mise en demeure) letter generator",
        "md_disclaimer": "This generator prepares a formal notice to pay (an interpellation under art. 102 CO) demanding payment of an amount owed, with a grace period and a reminder of the statutory default interest (art. 104 CO). It does not replace a consultation with a lawyer, particularly if the debtor disputes the claim.",
        "md_creancier_nom_label": "Your name (creditor)",
        "md_creancier_adresse_label": "Your address",
        "md_debiteur_nom_label": "Debtor's name",
        "md_debiteur_adresse_label": "Debtor's address",
        "md_objet_label": "Subject of the claim (e.g. invoice no. 123 of 1 March 2026)",
        "md_montant_label": "Amount owed (CHF)",
        "md_delai_grace_label": "Grace period granted (days, from sending)",
        "md_btn": "Generate the formal notice",
        "md_result_heading": "Your letter (review, complete and sign before sending)",
        "md_copy_btn": "Copy the text",
        "md_copy_done": "Copied!",
        "md_letter_object": "Formal notice to pay — {objet}",
        "md_letter_greeting": "Dear Sir or Madam,",
        "md_letter_body1": "Despite our previous reminders, I note that the amount of CHF {montant} relating to {objet} remains unpaid to date.",
        "md_letter_body2": "I hereby formally give you notice to pay this amount within {delai} days from the date this letter is sent, i.e. by {date_limite} at the latest.",
        "md_letter_body3": "Should payment not be made within this period, default interest of 5% per year will be claimed from this notice onward, in accordance with art. 104 CO, and debt-collection proceedings may be initiated without further notice.",
        "md_letter_closing": "Yours faithfully,",
        "md_source": "Legal basis: art. 102 CO (default triggered by the creditor's formal notice); art. 104 CO (statutory default interest of 5% per year from default, unless otherwise agreed).",
        # --- Free employment notice-period calculator ---
        "dl_heading": "Free employment notice-period calculator",
        "dl_disclaimer": "This calculator applies the minimum legal notice periods of art. 335b CO (trial period) and art. 335c CO (after the trial period). An individual contract, a standard employment contract, or a collective bargaining agreement may set longer periods, never shorter ones (except for a deviation the law allows). Indicative result, does not replace a consultation with a lawyer specialising in employment law.",
        "dl_essai_label": "Are you still within the trial period?",
        "dl_essai_oui": "Yes, still within the trial period",
        "dl_essai_non": "No, the trial period is over",
        "dl_date_engagement_label": "Start date of the employment relationship",
        "dl_date_notification_label": "Date the notice is given",
        "dl_btn": "Calculate the notice period",
        "dl_result_essai_prefix": "Notice period during the trial period: 7 days. End date of the employment relationship: ",
        "dl_result_essai_note": "During the trial period, notice can take effect on any day, not necessarily at the end of a month (art. 335b para. 1 CO).",
        "dl_result_normal_prefix": "Applicable notice period: ",
        "dl_result_normal_mois_1": "1 month (1st year of service)",
        "dl_result_normal_mois_2": "2 months (2nd to 9th year of service)",
        "dl_result_normal_mois_3": "3 months (from the 10th year of service)",
        "dl_result_date_fin_prefix": "End date of the employment relationship (end of the month following the notice period): ",
        "dl_result_normal_note": "Unless otherwise agreed, notice must be given for the end of a month (art. 335c para. 1 CO).",
        "dl_source": "Legal basis: art. 335b CO (7-day notice period during the trial period) and art. 335c CO (1, 2 or 3 months' notice depending on seniority, for the end of a month, after the trial period).",
        # --- Free administrative-appeal deadline calculator ---
        "dr_heading": "Free administrative-appeal deadline calculator",
        "dr_disclaimer": "This calculator applies art. 20 PA (starting point, postponement for a weekend or federal holiday) and art. 22a PA (court recess periods). It does not apply to proceedings on suspensive effect, provisional measures, or public procurement, for which the recess periods do not apply (art. 22a para. 2 PA). It only checks weekends and 1 August, the only holiday recognised at federal level: cantonal holidays must be checked separately if the authority concerned is cantonal. Indicative result, to be confirmed before any important step.",
        "dr_date_notif_label": "Date the decision was notified",
        "dr_jours_label": "Length of the appeal deadline (in days, as stated in the decision or the applicable law)",
        "dr_btn": "Calculate the deadline",
        "dr_result_prefix": "The appeal deadline expires on: ",
        "dr_source": "Legal basis: art. 20 para. 1 and 3 PA (starting point the day after notification, postponement to the next business day if the last day falls on a weekend or 1 August) and art. 22a PA (three court recess periods, identical to art. 145 CPC: from the 7th day before Easter to the 7th day after Easter inclusive, 15 July to 15 August inclusive, 18 December to 2 January inclusive; except for suspensive effect, provisional measures and public procurement, art. 22a para. 2 PA).",
    },
}

_JS_COMMON = r"""
function padZ(n){return String(n).padStart(2,'0');}
function parseD(s){ if(!s) return null; var p=s.split('-'); if(p.length!==3) return null; return new Date(Date.UTC(+p[0],+p[1]-1,+p[2])); }
function fmtD(d){ return padZ(d.getUTCDate())+'.'+padZ(d.getUTCMonth()+1)+'.'+d.getUTCFullYear(); }
function addDays(d,n){ var r=new Date(d.getTime()); r.setUTCDate(r.getUTCDate()+n); return r; }
function addYears(d,n){ var r=new Date(d.getTime()); r.setUTCFullYear(r.getUTCFullYear()+n); return r; }
function easterSunday(year){
  var a=year%19,b=Math.floor(year/100),c=year%100,d=Math.floor(b/4),e=b%4,
      f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),
      h=(19*a+b-d-g+15)%30,i=Math.floor(c/4),k=c%4,
      l=(32+2*e+2*i-h-k)%7,m=Math.floor((a+11*h+22*l)/451),
      month=Math.floor((h+l-7*m+114)/31),day=((h+l-7*m+114)%31)+1;
  return new Date(Date.UTC(year,month-1,day));
}
function feriesRanges(year){
  var easter=easterSunday(year);
  return [
    [addDays(easter,-7), addDays(easter,7)],
    [new Date(Date.UTC(year,6,15)), new Date(Date.UTC(year,7,15))],
    [new Date(Date.UTC(year,11,18)), new Date(Date.UTC(year+1,0,2))],
    [new Date(Date.UTC(year-1,11,18)), new Date(Date.UTC(year,0,2))]
  ];
}
function inRanges(d, ranges){ for(var i=0;i<ranges.length;i++){ if(d>=ranges[i][0] && d<=ranges[i][1]) return true; } return false; }
function isWeekend(d){ var wd=d.getUTCDay(); return wd===0||wd===6; }
function isAug1(d){ return d.getUTCMonth()===7 && d.getUTCDate()===1; }
"""

_JS_PRESCRIPTION = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
var sel = document.getElementById('calc-presc-type');
var rows = {
  contrat: document.getElementById('calc-presc-row-contrat'),
  illicite: document.getElementById('calc-presc-row-illicite'),
  periodique: document.getElementById('calc-presc-row-periodique'),
  penal: document.getElementById('calc-presc-row-penal')
};
function syncRows(){
  var v = sel.value;
  Object.keys(rows).forEach(function(k){ rows[k].hidden = (k !== v); });
}
sel.addEventListener('change', syncRows);
syncRows();
document.getElementById('calc-presc-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-presc-result');
  var srcEl = document.getElementById('calc-presc-source-text');
  var v = sel.value;
  var result = null, sourceKey = null, note = '';
  if (v === 'contrat') {
    var dExig = parseD(document.getElementById('calc-presc-date-exigible').value);
    if (dExig) { result = addYears(dExig, 10); sourceKey = 'presc_source_contrat'; }
  } else if (v === 'periodique') {
    var dExig2 = parseD(document.getElementById('calc-presc-date-exigible-2').value);
    if (dExig2) { result = addYears(dExig2, 5); sourceKey = 'presc_source_periodique'; }
  } else if (v === 'illicite') {
    var dActe = parseD(document.getElementById('calc-presc-date-acte').value);
    var dConn = parseD(document.getElementById('calc-presc-date-connaissance').value);
    if (dActe && dConn) {
      var relatif = addYears(dConn, 3);
      var absolu = addYears(dActe, 20);
      result = relatif < absolu ? relatif : absolu;
      sourceKey = 'presc_source_illicite';
      note = s.presc_result_illicite_note;
    }
  } else if (v === 'penal') {
    var dInf = parseD(document.getElementById('calc-presc-date-infraction').value);
    var peine = document.getElementById('calc-presc-peine').value;
    var years = {vie:30, plus3:15, max3:10, autre:7, contravention:3}[peine];
    if (dInf && years) { result = addYears(dInf, years); sourceKey = 'presc_source_penal'; }
  }
  if (result) {
    out.hidden = false;
    out.textContent = s.presc_result_prefix + fmtD(result) + note;
    srcEl.textContent = s[sourceKey];
  }
});
})();
"""

_JS_DELAI = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
document.getElementById('calc-delai-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-delai-result');
  var dComm = parseD(document.getElementById('calc-delai-date-comm').value);
  var n = parseInt(document.getElementById('calc-delai-jours').value, 10);
  var procType = document.getElementById('calc-delai-procedure').value;
  var applyFeries = (procType === 'ordinaire');
  if (!dComm || !n || n < 1) return;
  var ranges = feriesRanges(dComm.getUTCFullYear())
    .concat(feriesRanges(dComm.getUTCFullYear()+1))
    .concat(feriesRanges(dComm.getUTCFullYear()+2));
  var cursor = addDays(dComm, 1);
  var count = 0;
  var guard = 0;
  while (count < n && guard < 5000) {
    if (!applyFeries || !inRanges(cursor, ranges)) { count++; }
    if (count === n) break;
    cursor = addDays(cursor, 1);
    guard++;
  }
  while (isWeekend(cursor) || isAug1(cursor)) { cursor = addDays(cursor, 1); }
  out.hidden = false;
  out.textContent = s.delai_result_prefix + fmtD(cursor);
});
})();
"""

_JS_INTERETS = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
document.getElementById('calc-int-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-int-result');
  var capital = parseFloat(document.getElementById('calc-int-capital').value);
  var dDebut = parseD(document.getElementById('calc-int-date-debut').value);
  var dFin = parseD(document.getElementById('calc-int-date-fin').value);
  var taux = parseFloat(document.getElementById('calc-int-taux').value);
  if (!capital || !dDebut || !dFin || isNaN(taux) || dFin <= dDebut) return;
  var jours = Math.round((dFin.getTime() - dDebut.getTime()) / 86400000);
  var interet = capital * (taux/100) * (jours/365);
  var total = capital + interet;
  var fmt2 = function(x){ return x.toLocaleString('fr-CH', {minimumFractionDigits:2, maximumFractionDigits:2}); };
  out.hidden = false;
  out.innerHTML = s.int_result_interet + fmt2(interet) + ' ' + s.currency + s.int_result_jours + jours + s.int_result_jours_suffix +
    '<br>' + s.int_result_total + fmt2(total) + ' ' + s.currency;
});
})();
"""

# Bareme amendes d'ordre (OAO) : [seuil_haut_km/h, montant_CHF], le premier
# seuil >= exces s'applique. Au-dela du dernier seuil, plus de bareme fixe
# (denonciation penale). Sources : voir docstring du module.
_JS_AMENDE = r"""(function(){
var s = __STRINGS_JSON__;
var BAREME = {
  localite:  [[5,40],[10,120],[15,250]],
  hors:      [[5,40],[10,100],[15,160],[20,240]],
  autoroute: [[5,20],[10,60],[15,120],[20,180],[25,260]]
};
var SEUIL_GRAVE = {localite:25, hors:30, autoroute:35};
var SEUIL_CHAUFFARD = {localite:50, hors:60, autoroute:80};
document.getElementById('calc-amende-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-amende-result');
  var zone = document.getElementById('calc-amende-zone').value;
  var exces = parseFloat(document.getElementById('calc-amende-exces').value);
  if (!exces || exces <= 0) return;
  var bareme = BAREME[zone];
  var fixe = null;
  for (var i = 0; i < bareme.length; i++) {
    if (exces <= bareme[i][0]) { fixe = bareme[i][1]; break; }
  }
  out.hidden = false;
  if (fixe !== null) {
    out.className = 'calc-result is-eligible';
    out.innerHTML = '<p><strong>' + s.amende_result_oao_prefix + fixe + ' ' + s.currency + '</strong></p><p>' + s.amende_result_oao_note + '</p>';
    return;
  }
  if (exces >= SEUIL_CHAUFFARD[zone]) {
    out.className = 'calc-result is-severe';
    out.innerHTML = '<p><strong>' + s.amende_result_chauffard_title + '</strong></p><p>' + s.amende_result_chauffard_text + '</p>';
  } else if (exces >= SEUIL_GRAVE[zone]) {
    out.className = 'calc-result is-severe';
    out.innerHTML = '<p><strong>' + s.amende_result_grave_title + '</strong></p><p>' + s.amende_result_grave_text + '</p>';
  } else {
    out.className = 'calc-result is-not-eligible';
    out.innerHTML = '<p><strong>' + s.amende_result_moyen_title + '</strong></p><p>' + s.amende_result_moyen_text + '</p>';
  }
});
})();
"""

_JS_RESILIATION_BAIL = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
var DELAI_MOIS = { habitation: 3, commercial: 6 };
function monthsBetween(d1, d2) {
  var m = (d2.getUTCFullYear() - d1.getUTCFullYear()) * 12 + (d2.getUTCMonth() - d1.getUTCMonth());
  if (d2.getUTCDate() < d1.getUTCDate()) m -= 1;
  return m;
}
document.getElementById('calc-rb-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-rb-result');
  var warn = document.getElementById('calc-rb-warning');
  var type = document.getElementById('calc-rb-type').value;
  var nomExp = document.getElementById('calc-rb-nom-exp').value.trim();
  var adresseExp = document.getElementById('calc-rb-adresse-exp').value.trim();
  var nomDest = document.getElementById('calc-rb-nom-dest').value.trim();
  var adresseDest = document.getElementById('calc-rb-adresse-dest').value.trim();
  var objet = document.getElementById('calc-rb-objet').value.trim();
  var dEnvoi = parseD(document.getElementById('calc-rb-date-envoi').value);
  var dFin = parseD(document.getElementById('calc-rb-date-fin').value);
  if (!nomExp || !nomDest || !objet || !dEnvoi || !dFin || dFin <= dEnvoi) return;

  var moisRequis = DELAI_MOIS[type];
  warn.hidden = true;
  if (monthsBetween(dEnvoi, dFin) < moisRequis) {
    warn.hidden = false;
    warn.textContent = s.rb_warning_delai.replace('{mois}', moisRequis);
  }

  var dateFinStr = fmtD(dFin);
  var lines = [];
  lines.push(nomExp);
  if (adresseExp) lines.push(adresseExp);
  lines.push('');
  lines.push(nomDest);
  if (adresseDest) lines.push(adresseDest);
  lines.push('');
  lines.push(fmtD(dEnvoi));
  lines.push('');
  lines.push(s.rb_letter_object.replace('{objet}', objet));
  lines.push('');
  lines.push(s.rb_letter_greeting);
  lines.push('');
  lines.push(s.rb_letter_body1.replace('{date_fin}', dateFinStr));
  lines.push('');
  lines.push(s.rb_letter_body2);
  lines.push('');
  lines.push(s.rb_letter_body3);
  lines.push('');
  lines.push(s.rb_letter_closing);
  lines.push('');
  lines.push(nomExp);
  lines.push('');
  lines.push(s.rb_letter_recommande);
  var letterText = lines.join('\n');

  out.hidden = false;
  document.getElementById('calc-rb-letter').value = letterText;
});
document.getElementById('calc-rb-copy-btn').addEventListener('click', function(){
  var ta = document.getElementById('calc-rb-letter');
  var btn = document.getElementById('calc-rb-copy-btn');
  var done = function(){ btn.textContent = s.rb_copy_done; setTimeout(function(){ btn.textContent = s.rb_copy_btn; }, 2000); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(ta.value).then(done).catch(function(){ ta.select(); document.execCommand('copy'); done(); });
  } else {
    ta.select();
    document.execCommand('copy');
    done();
  }
});
})();
"""


# Estimateur de pension alimentaire : methode simplifiee et illustrative en
# deux etapes (minimum vital LP, puis repartition de l'excedent familial
# selon "grandes tetes / petites tetes"). Voir le paragraphe "ATTENTION
# particuliere" dans la docstring du module pour les limites assumees.
_JS_PENSION = r"""(function(){
var s = __STRINGS_JSON__;
var BASE_CREANCIER = 1350;
var BASE_DEBITEUR_SEUL = 1200;
var BASE_DEBITEUR_COUPLE = 1700;
var ENFANT_MOINS10 = 400;
var ENFANT_10PLUS = 600;
function num(id){ var v = parseFloat(document.getElementById(id).value); return isNaN(v) ? 0 : v; }
function fmt2(x){ return x.toLocaleString('fr-CH', {minimumFractionDigits:2, maximumFractionDigits:2}); }
document.getElementById('calc-pa-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-pa-result');
  var n10 = Math.max(0, parseInt(document.getElementById('calc-pa-n10').value, 10) || 0);
  var n10p = Math.max(0, parseInt(document.getElementById('calc-pa-n10p').value, 10) || 0);
  var nbEnfants = n10 + n10p;
  if (nbEnfants < 1) return;

  var revenuC = num('calc-pa-c-revenu');
  var loyerC = num('calc-pa-c-loyer');
  var assC = num('calc-pa-c-assurance');
  var chargesC = num('calc-pa-c-charges');
  var revenuD = num('calc-pa-d-revenu');
  var loyerD = num('calc-pa-d-loyer');
  var assD = num('calc-pa-d-assurance');
  var chargesD = num('calc-pa-d-charges');
  var situationD = document.getElementById('calc-pa-d-situation').value;

  var minEnfants = n10 * ENFANT_MOINS10 + n10p * ENFANT_10PLUS;
  var minCreancier = BASE_CREANCIER + loyerC + assC + chargesC;
  var baseDeb = situationD === 'couple' ? BASE_DEBITEUR_COUPLE : BASE_DEBITEUR_SEUL;
  var minDebiteur = baseDeb + loyerD + assD + chargesD;
  var dispoDebiteur = revenuD - minDebiteur;

  var excedent = (revenuC + revenuD) - (minCreancier + minDebiteur + minEnfants);
  var parts = 4 + nbEnfants;
  var partExcedentEnfants = excedent > 0 ? excedent * nbEnfants / parts : 0;
  var pensionBrute = minEnfants + partExcedentEnfants;

  out.hidden = false;
  if (dispoDebiteur <= 0) {
    out.className = 'calc-result is-not-eligible';
    out.innerHTML = '<p>' + s.pa_result_insufficient + '</p>';
    return;
  }

  var pension = Math.min(pensionBrute, dispoDebiteur);
  var capped = pensionBrute > dispoDebiteur;

  var detailExcedent = excedent > 0
    ? s.pa_result_detail_excedent_positif + fmt2(partExcedentEnfants) + ' ' + s.currency
    : s.pa_result_detail_excedent_nul;

  var html = '<h3 style="margin-top:0;">' + s.pa_result_heading + '</h3>';
  html += '<p><strong>' + s.pa_result_pension_prefix + fmt2(pension) + ' ' + s.currency + '</strong></p>';
  html += '<p>' + s.pa_result_detail_enfants + fmt2(minEnfants) + ' ' + s.currency + '</p>';
  html += '<p>' + detailExcedent + '</p>';
  if (capped) {
    html += '<p>' + s.pa_result_capped.replace('{montant}', fmt2(pensionBrute)) + '</p>';
  }
  out.className = 'calc-result is-eligible';
  out.innerHTML = html;
});
})();
"""


# Bareme des emoluments de commandement de payer (art. 16 al. 1 OELP),
# texte officiel en vigueur depuis le 1.1.2026 (RO 2025 630). Chaque paire
# est [plafond_creance_CHF, emolument_CHF] ; le premier plafond >= montant
# s'applique, au-dela du dernier plafond l'emolument fixe est 400 CHF.
_JS_FRAIS_POURSUITE = r"""(function(){
var s = __STRINGS_JSON__;
var BAREME = [[100,7],[500,20],[1000,40],[10000,60],[100000,90],[1000000,190]];
var EMOLUMENT_MAX = 400;
document.getElementById('calc-fp-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-fp-result');
  var montant = parseFloat(document.getElementById('calc-fp-montant').value);
  if (!montant || montant <= 0) return;
  var emolument = EMOLUMENT_MAX;
  for (var i = 0; i < BAREME.length; i++) {
    if (montant <= BAREME[i][0]) { emolument = BAREME[i][1]; break; }
  }
  out.hidden = false;
  out.className = 'calc-result is-eligible';
  out.innerHTML = '<p><strong>' + s.fp_result_prefix + emolument + ' ' + s.currency + '</strong></p><p>' + s.fp_result_avance + '</p>';
});
})();
"""


_JS_SOUS_LOCATION = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
document.getElementById('calc-sl-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-sl-result');
  var warn = document.getElementById('calc-sl-warning');
  var nomBailleur = document.getElementById('calc-sl-bailleur-nom').value.trim();
  var adresseBailleur = document.getElementById('calc-sl-bailleur-adresse').value.trim();
  var nomLocataire = document.getElementById('calc-sl-locataire-nom').value.trim();
  var adresseLocataire = document.getElementById('calc-sl-locataire-adresse').value.trim();
  var objet = document.getElementById('calc-sl-objet').value.trim();
  var nomSousLoc = document.getElementById('calc-sl-souslocataire-nom').value.trim();
  var dDebut = parseD(document.getElementById('calc-sl-date-debut').value);
  var dFin = parseD(document.getElementById('calc-sl-date-fin').value);
  var loyerPrincipal = parseFloat(document.getElementById('calc-sl-loyer-principal').value);
  var loyerSous = parseFloat(document.getElementById('calc-sl-loyer-sous').value);
  if (!nomBailleur || !nomLocataire || !objet || !nomSousLoc || !dDebut || !loyerPrincipal || !loyerSous) return;

  warn.hidden = true;
  if (loyerSous > loyerPrincipal * 1.2) {
    warn.hidden = false;
    warn.textContent = s.sl_warning_abusif;
  }

  var dateFinSuffix = dFin ? s.sl_letter_date_fin_suffix.replace('{date_fin}', fmtD(dFin)) : '';
  var lines = [];
  lines.push(nomLocataire);
  if (adresseLocataire) lines.push(adresseLocataire);
  lines.push('');
  lines.push(nomBailleur);
  if (adresseBailleur) lines.push(adresseBailleur);
  lines.push('');
  lines.push(fmtD(new Date()));
  lines.push('');
  lines.push(s.sl_letter_object.replace('{objet}', objet));
  lines.push('');
  lines.push(s.sl_letter_greeting);
  lines.push('');
  lines.push(s.sl_letter_body1
    .replace('{souslocataire}', nomSousLoc)
    .replace('{date_debut}', fmtD(dDebut))
    .replace('{date_fin_suffix}', dateFinSuffix)
    .replace('{loyer_sous}', loyerSous)
    .replace('{loyer_principal}', loyerPrincipal));
  lines.push('');
  lines.push(s.sl_letter_body2);
  lines.push('');
  lines.push(s.sl_letter_body3);
  lines.push('');
  lines.push(s.sl_letter_closing);
  lines.push('');
  lines.push(nomLocataire);
  var letterText = lines.join('\n');

  out.hidden = false;
  document.getElementById('calc-sl-letter').value = letterText;
});
document.getElementById('calc-sl-copy-btn').addEventListener('click', function(){
  var ta = document.getElementById('calc-sl-letter');
  var btn = document.getElementById('calc-sl-copy-btn');
  var done = function(){ btn.textContent = s.sl_copy_done; setTimeout(function(){ btn.textContent = s.sl_copy_btn; }, 2000); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(ta.value).then(done).catch(function(){ ta.select(); document.execCommand('copy'); done(); });
  } else {
    ta.select();
    document.execCommand('copy');
    done();
  }
});
})();
"""


# Fractions legales (art. 462 CC) et fractions de reserve (art. 470/471 CC,
# depuis la revision entree en vigueur le 1.1.2023) : reserve conjoint et
# descendants = 1/2 de leur part legale, reserve parents = 0. Verifie par
# recherche croisee (croce-associes.ch et ubs.com, concordants).
_JS_RESERVE_HEREDITAIRE = r"""(function(){
var s = __STRINGS_JSON__;
function fmtPct(x){ return (x*100).toLocaleString('fr-CH', {maximumFractionDigits:2}) + '%'; }
document.getElementById('calc-rh-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-rh-result');
  var situation = document.getElementById('calc-rh-situation').value;
  var n = Math.max(1, parseInt(document.getElementById('calc-rh-nb-enfants').value, 10) || 1);

  var partLegaleConjoint = 0, partLegaleDescendants = 0;
  if (situation === 'conjoint_descendants') { partLegaleConjoint = 0.5; partLegaleDescendants = 0.5; }
  else if (situation === 'conjoint_parents') { partLegaleConjoint = 0.75; }
  else if (situation === 'conjoint_seul') { partLegaleConjoint = 1; }
  else if (situation === 'descendants_seuls') { partLegaleDescendants = 1; }
  // 'parents_seuls' : aucune part legale de conjoint ni de descendants, reserve nulle

  var reserveConjoint = partLegaleConjoint * 0.5;
  var reserveDescendantsTotal = partLegaleDescendants * 0.5;
  var reserveDescendantsChacun = (situation === 'conjoint_descendants' || situation === 'descendants_seuls') ? reserveDescendantsTotal / n : 0;
  var reserveTotal = reserveConjoint + reserveDescendantsTotal;
  var quotiteDisponible = 1 - reserveTotal;

  var html = '<h3 style="margin-top:0;">' + s.rh_result_heading + '</h3>';
  if (reserveConjoint > 0) {
    html += '<p>' + s.rh_result_reserve_conjoint + fmtPct(reserveConjoint) + '</p>';
  }
  if (reserveDescendantsTotal > 0) {
    html += '<p>' + s.rh_result_reserve_descendants + fmtPct(reserveDescendantsTotal) + '</p>';
    html += '<p>' + s.rh_result_reserve_descendants_chacun + fmtPct(reserveDescendantsChacun) + '</p>';
  }
  if (situation === 'conjoint_parents' || situation === 'parents_seuls') {
    html += '<p>' + s.rh_result_reserve_parents + '</p>';
  }
  html += '<p><strong>' + s.rh_result_quotite_disponible + fmtPct(quotiteDisponible) + '</strong></p>';

  out.hidden = false;
  out.className = 'calc-result is-eligible';
  out.innerHTML = html;
});
})();
"""


_JS_DELAI_CONGE = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
var DELAI_MOIS = { habitation: 3, commercial: 6 };
document.getElementById('calc-dc-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-dc-result');
  var type = document.getElementById('calc-dc-type').value;
  var dEnvoi = parseD(document.getElementById('calc-dc-date-envoi').value);
  if (!dEnvoi) return;
  var moisRequis = DELAI_MOIS[type];
  var dateLimite = addDays(dEnvoi, 0);
  dateLimite.setUTCMonth(dateLimite.getUTCMonth() + moisRequis);
  out.hidden = false;
  out.className = 'calc-result is-eligible';
  out.innerHTML = '<p><strong>' + s.dc_result_prefix + fmtD(dateLimite) + '</strong></p><p>' + s.dc_result_note + '</p>';
});
})();
"""


_JS_MISE_EN_DEMEURE = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
document.getElementById('calc-md-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-md-result');
  var nomCreancier = document.getElementById('calc-md-creancier-nom').value.trim();
  var adresseCreancier = document.getElementById('calc-md-creancier-adresse').value.trim();
  var nomDebiteur = document.getElementById('calc-md-debiteur-nom').value.trim();
  var adresseDebiteur = document.getElementById('calc-md-debiteur-adresse').value.trim();
  var objet = document.getElementById('calc-md-objet').value.trim();
  var montant = parseFloat(document.getElementById('calc-md-montant').value);
  var delai = parseInt(document.getElementById('calc-md-delai-grace').value, 10);
  if (!nomCreancier || !nomDebiteur || !objet || !montant || !delai || delai < 1) return;

  var today = new Date();
  today.setUTCHours(0,0,0,0);
  var dateLimite = addDays(today, delai);
  var fmt2 = function(x){ return x.toLocaleString('fr-CH', {minimumFractionDigits:2, maximumFractionDigits:2}); };

  var lines = [];
  lines.push(nomCreancier);
  if (adresseCreancier) lines.push(adresseCreancier);
  lines.push('');
  lines.push(nomDebiteur);
  if (adresseDebiteur) lines.push(adresseDebiteur);
  lines.push('');
  lines.push(fmtD(today));
  lines.push('');
  lines.push(s.md_letter_object.replace('{objet}', objet));
  lines.push('');
  lines.push(s.md_letter_greeting);
  lines.push('');
  lines.push(s.md_letter_body1.replace('{montant}', fmt2(montant)).replace('{objet}', objet));
  lines.push('');
  lines.push(s.md_letter_body2.replace('{delai}', delai).replace('{date_limite}', fmtD(dateLimite)));
  lines.push('');
  lines.push(s.md_letter_body3);
  lines.push('');
  lines.push(s.md_letter_closing);
  lines.push('');
  lines.push(nomCreancier);
  var letterText = lines.join('\n');

  out.hidden = false;
  document.getElementById('calc-md-letter').value = letterText;
});
document.getElementById('calc-md-copy-btn').addEventListener('click', function(){
  var ta = document.getElementById('calc-md-letter');
  var btn = document.getElementById('calc-md-copy-btn');
  var done = function(){ btn.textContent = s.md_copy_done; setTimeout(function(){ btn.textContent = s.md_copy_btn; }, 2000); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(ta.value).then(done).catch(function(){ ta.select(); document.execCommand('copy'); done(); });
  } else {
    ta.select();
    document.execCommand('copy');
    done();
  }
});
})();
"""


_JS_DELAI_LICENCIEMENT = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
function addMonths(d, n) {
  var r = new Date(d.getTime());
  r.setUTCMonth(r.getUTCMonth() + n);
  return r;
}
function endOfMonth(d) {
  return new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, 0));
}
function anneesCompletes(d1, d2) {
  var years = d2.getUTCFullYear() - d1.getUTCFullYear();
  var anniv = new Date(Date.UTC(d1.getUTCFullYear() + years, d1.getUTCMonth(), d1.getUTCDate()));
  if (anniv > d2) years -= 1;
  return years;
}
var selEssai = document.getElementById('calc-dl-essai');
var rowEngagement = document.getElementById('calc-dl-row-engagement');
function syncRows(){
  rowEngagement.hidden = (selEssai.value === 'oui');
}
selEssai.addEventListener('change', syncRows);
syncRows();

document.getElementById('calc-dl-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-dl-result');
  var dNotif = parseD(document.getElementById('calc-dl-date-notification').value);
  if (!dNotif) return;

  out.hidden = false;
  out.className = 'calc-result is-eligible';

  if (selEssai.value === 'oui') {
    var dateFinEssai = addDays(dNotif, 7);
    out.innerHTML = '<p><strong>' + s.dl_result_essai_prefix + fmtD(dateFinEssai) + '</strong></p><p>' + s.dl_result_essai_note + '</p>';
    return;
  }

  var dEngagement = parseD(document.getElementById('calc-dl-date-engagement').value);
  if (!dEngagement) return;
  var anciennete = anneesCompletes(dEngagement, dNotif);
  var moisDelai, libelleDelai;
  if (anciennete < 1) { moisDelai = 1; libelleDelai = s.dl_result_normal_mois_1; }
  else if (anciennete < 9) { moisDelai = 2; libelleDelai = s.dl_result_normal_mois_2; }
  else { moisDelai = 3; libelleDelai = s.dl_result_normal_mois_3; }

  var brut = addMonths(dNotif, moisDelai);
  var dateFin = endOfMonth(brut);

  var html = '<p><strong>' + s.dl_result_normal_prefix + libelleDelai + '</strong></p>';
  html += '<p>' + s.dl_result_date_fin_prefix + fmtD(dateFin) + '</p>';
  html += '<p>' + s.dl_result_normal_note + '</p>';
  out.innerHTML = html;
});
})();
"""


_JS_DELAI_RECOURS = r"""(function(){
""" + _JS_COMMON + r"""
var s = __STRINGS_JSON__;
document.getElementById('calc-dr-btn').addEventListener('click', function(){
  var out = document.getElementById('calc-dr-result');
  var dNotif = parseD(document.getElementById('calc-dr-date-notif').value);
  var n = parseInt(document.getElementById('calc-dr-jours').value, 10);
  if (!dNotif || !n || n < 1) return;
  var ranges = feriesRanges(dNotif.getUTCFullYear())
    .concat(feriesRanges(dNotif.getUTCFullYear()+1))
    .concat(feriesRanges(dNotif.getUTCFullYear()+2));
  var cursor = addDays(dNotif, 1);
  var count = 0;
  var guard = 0;
  while (count < n && guard < 5000) {
    if (!inRanges(cursor, ranges)) { count++; }
    if (count === n) break;
    cursor = addDays(cursor, 1);
    guard++;
  }
  while (isWeekend(cursor) || isAug1(cursor)) { cursor = addDays(cursor, 1); }
  out.hidden = false;
  out.className = 'calc-result is-eligible';
  out.textContent = s.dr_result_prefix + fmtD(cursor);
});
})();
"""


def _widget(lang, kind):
    s = STRINGS[lang]
    if kind == "prescription":
        js = _JS_PRESCRIPTION.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-presc">
  <h2 style="margin-top:0;">{s['presc_heading']}</h2>
  <p class="calc-disclaimer">{s['presc_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['presc_type_label']}
      <select id="calc-presc-type">
        <option value="contrat">{s['presc_opt_contrat']}</option>
        <option value="illicite">{s['presc_opt_illicite']}</option>
        <option value="periodique">{s['presc_opt_periodique']}</option>
        <option value="penal">{s['presc_opt_penal']}</option>
      </select>
    </label>
    <label class="calc-field" id="calc-presc-row-contrat">{s['presc_date_exigible']}
      <input type="date" id="calc-presc-date-exigible">
    </label>
    <label class="calc-field" id="calc-presc-row-periodique" hidden>{s['presc_date_exigible']}
      <input type="date" id="calc-presc-date-exigible-2">
    </label>
    <div id="calc-presc-row-illicite" hidden>
      <label class="calc-field">{s['presc_date_acte']}
        <input type="date" id="calc-presc-date-acte">
      </label>
      <label class="calc-field">{s['presc_date_connaissance']}
        <input type="date" id="calc-presc-date-connaissance">
      </label>
    </div>
    <div id="calc-presc-row-penal" hidden>
      <label class="calc-field">{s['presc_date_infraction']}
        <input type="date" id="calc-presc-date-infraction">
      </label>
      <label class="calc-field">{s['presc_peine_label']}
        <select id="calc-presc-peine">
          <option value="vie">{s['presc_peine_vie']}</option>
          <option value="plus3">{s['presc_peine_plus3']}</option>
          <option value="max3">{s['presc_peine_max3']}</option>
          <option value="autre">{s['presc_peine_autre']}</option>
          <option value="contravention">{s['presc_peine_contravention']}</option>
        </select>
      </label>
    </div>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-presc-btn">{s['presc_btn']}</button>
  <div id="calc-presc-result" class="calc-result" hidden></div>
  <p class="calc-source" id="calc-presc-source-text"></p>
</div>
<script>{js}</script>
"""
    if kind == "delai":
        js = _JS_DELAI.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-delai">
  <h2 style="margin-top:0;">{s['delai_heading']}</h2>
  <p class="calc-disclaimer">{s['delai_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['delai_date_comm_label']}
      <input type="date" id="calc-delai-date-comm">
    </label>
    <label class="calc-field">{s['delai_jours_label']}
      <input type="number" id="calc-delai-jours" min="1" step="1" value="30" inputmode="numeric">
    </label>
    <label class="calc-field">{s['delai_procedure_label']}
      <select id="calc-delai-procedure">
        <option value="ordinaire">{s['delai_opt_ordinaire']}</option>
        <option value="sommaire">{s['delai_opt_sommaire']}</option>
      </select>
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-delai-btn">{s['delai_btn']}</button>
  <div id="calc-delai-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['delai_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "interets":
        js = _JS_INTERETS.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-int">
  <h2 style="margin-top:0;">{s['int_heading']}</h2>
  <p class="calc-disclaimer">{s['int_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['int_capital_label']}
      <input type="number" id="calc-int-capital" min="0" step="10" inputmode="numeric">
    </label>
    <label class="calc-field">{s['int_date_debut_label']}
      <input type="date" id="calc-int-date-debut">
    </label>
    <label class="calc-field">{s['int_date_fin_label']}
      <input type="date" id="calc-int-date-fin">
    </label>
    <label class="calc-field">{s['int_taux_label']}
      <input type="number" id="calc-int-taux" min="0" step="0.1" value="5" inputmode="decimal">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-int-btn">{s['int_btn']}</button>
  <div id="calc-int-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['int_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "amende":
        js = _JS_AMENDE.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-amende">
  <h2 style="margin-top:0;">{s['amende_heading']}</h2>
  <p class="calc-disclaimer">{s['amende_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['amende_zone_label']}
      <select id="calc-amende-zone">
        <option value="localite">{s['amende_zone_localite']}</option>
        <option value="hors">{s['amende_zone_hors']}</option>
        <option value="autoroute">{s['amende_zone_autoroute']}</option>
      </select>
    </label>
    <label class="calc-field">{s['amende_exces_label']}
      <input type="number" id="calc-amende-exces" min="1" step="1" inputmode="numeric">
      <span class="calc-source">{s['amende_exces_help']}</span>
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-amende-btn">{s['amende_btn']}</button>
  <div id="calc-amende-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['amende_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "resiliation_bail":
        js = _JS_RESILIATION_BAIL.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-rb">
  <h2 style="margin-top:0;">{s['rb_heading']}</h2>
  <p class="calc-disclaimer">{s['rb_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['rb_type_label']}
      <select id="calc-rb-type">
        <option value="habitation">{s['rb_type_habitation']}</option>
        <option value="commercial">{s['rb_type_commercial']}</option>
      </select>
    </label>
    <label class="calc-field">{s['rb_nom_exp_label']}
      <input type="text" id="calc-rb-nom-exp">
    </label>
    <label class="calc-field">{s['rb_adresse_exp_label']}
      <input type="text" id="calc-rb-adresse-exp">
    </label>
    <label class="calc-field">{s['rb_nom_dest_label']}
      <input type="text" id="calc-rb-nom-dest">
    </label>
    <label class="calc-field">{s['rb_adresse_dest_label']}
      <input type="text" id="calc-rb-adresse-dest">
    </label>
    <label class="calc-field">{s['rb_objet_label']}
      <input type="text" id="calc-rb-objet">
    </label>
    <label class="calc-field">{s['rb_date_envoi_label']}
      <input type="date" id="calc-rb-date-envoi">
    </label>
    <label class="calc-field">{s['rb_date_fin_label']}
      <input type="date" id="calc-rb-date-fin">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-rb-btn">{s['rb_btn']}</button>
  <div id="calc-rb-warning" class="vform-error" hidden></div>
  <div id="calc-rb-result" class="calc-result" hidden>
    <h3 style="margin-top:0;">{s['rb_result_heading']}</h3>
    <textarea id="calc-rb-letter" readonly rows="16" style="width:100%; font-family:inherit; padding:10px; border-radius:var(--radius-sm); border:1px solid var(--border-strong);"></textarea>
    <button type="button" class="cta-btn" id="calc-rb-copy-btn" style="margin-top:var(--space-sm);">{s['rb_copy_btn']}</button>
  </div>
  <p class="calc-source">{s['rb_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "pension":
        js = _JS_PENSION.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-pa">
  <h2 style="margin-top:0;">{s['pa_heading']}</h2>
  <p class="calc-disclaimer">{s['pa_disclaimer']}</p>
  <h3>{s['pa_children_heading']}</h3>
  <div class="calc-grid">
    <label class="calc-field">{s['pa_children_under10_label']}
      <input type="number" id="calc-pa-n10" min="0" step="1" inputmode="numeric" value="0">
    </label>
    <label class="calc-field">{s['pa_children_10plus_label']}
      <input type="number" id="calc-pa-n10p" min="0" step="1" inputmode="numeric" value="0">
    </label>
  </div>
  <h3>{s['pa_creancier_heading']}</h3>
  <div class="calc-grid">
    <label class="calc-field">{s['pa_creancier_revenu_label']}
      <input type="number" id="calc-pa-c-revenu" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['pa_creancier_loyer_label']}
      <input type="number" id="calc-pa-c-loyer" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['pa_creancier_assurance_label']}
      <input type="number" id="calc-pa-c-assurance" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['pa_creancier_charges_label']}
      <input type="number" id="calc-pa-c-charges" min="0" step="1" inputmode="numeric" value="0">
    </label>
  </div>
  <h3>{s['pa_debiteur_heading']}</h3>
  <div class="calc-grid">
    <label class="calc-field">{s['pa_debiteur_situation_label']}
      <select id="calc-pa-d-situation">
        <option value="seul">{s['pa_debiteur_situation_seul']}</option>
        <option value="couple">{s['pa_debiteur_situation_couple']}</option>
      </select>
    </label>
    <label class="calc-field">{s['pa_debiteur_revenu_label']}
      <input type="number" id="calc-pa-d-revenu" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['pa_debiteur_loyer_label']}
      <input type="number" id="calc-pa-d-loyer" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['pa_debiteur_assurance_label']}
      <input type="number" id="calc-pa-d-assurance" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['pa_debiteur_charges_label']}
      <input type="number" id="calc-pa-d-charges" min="0" step="1" inputmode="numeric" value="0">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-pa-btn">{s['pa_btn']}</button>
  <div id="calc-pa-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['pa_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "frais_poursuite":
        js = _JS_FRAIS_POURSUITE.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-fp">
  <h2 style="margin-top:0;">{s['fp_heading']}</h2>
  <p class="calc-disclaimer">{s['fp_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['fp_montant_label']}
      <input type="number" id="calc-fp-montant" min="1" step="1" inputmode="numeric">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-fp-btn">{s['fp_btn']}</button>
  <div id="calc-fp-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['fp_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "sous_location":
        js = _JS_SOUS_LOCATION.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-sl">
  <h2 style="margin-top:0;">{s['sl_heading']}</h2>
  <p class="calc-disclaimer">{s['sl_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['sl_bailleur_nom_label']}
      <input type="text" id="calc-sl-bailleur-nom">
    </label>
    <label class="calc-field">{s['sl_bailleur_adresse_label']}
      <input type="text" id="calc-sl-bailleur-adresse">
    </label>
    <label class="calc-field">{s['sl_locataire_nom_label']}
      <input type="text" id="calc-sl-locataire-nom">
    </label>
    <label class="calc-field">{s['sl_locataire_adresse_label']}
      <input type="text" id="calc-sl-locataire-adresse">
    </label>
    <label class="calc-field">{s['sl_objet_label']}
      <input type="text" id="calc-sl-objet">
    </label>
    <label class="calc-field">{s['sl_souslocataire_nom_label']}
      <input type="text" id="calc-sl-souslocataire-nom">
    </label>
    <label class="calc-field">{s['sl_date_debut_label']}
      <input type="date" id="calc-sl-date-debut">
    </label>
    <label class="calc-field">{s['sl_date_fin_label']}
      <input type="date" id="calc-sl-date-fin">
    </label>
    <label class="calc-field">{s['sl_loyer_principal_label']}
      <input type="number" id="calc-sl-loyer-principal" min="0" step="1" inputmode="numeric">
    </label>
    <label class="calc-field">{s['sl_loyer_sous_label']}
      <input type="number" id="calc-sl-loyer-sous" min="0" step="1" inputmode="numeric">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-sl-btn">{s['sl_btn']}</button>
  <div id="calc-sl-warning" class="vform-error" hidden></div>
  <div id="calc-sl-result" class="calc-result" hidden>
    <h3 style="margin-top:0;">{s['sl_result_heading']}</h3>
    <textarea id="calc-sl-letter" readonly rows="16" style="width:100%; font-family:inherit; padding:10px; border-radius:var(--radius-sm); border:1px solid var(--border-strong);"></textarea>
    <button type="button" class="cta-btn" id="calc-sl-copy-btn" style="margin-top:var(--space-sm);">{s['sl_copy_btn']}</button>
  </div>
  <p class="calc-source">{s['sl_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "reserve_hereditaire":
        js = _JS_RESERVE_HEREDITAIRE.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-rh">
  <h2 style="margin-top:0;">{s['rh_heading']}</h2>
  <p class="calc-disclaimer">{s['rh_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['rh_situation_label']}
      <select id="calc-rh-situation">
        <option value="conjoint_descendants">{s['rh_situation_conjoint_descendants']}</option>
        <option value="conjoint_parents">{s['rh_situation_conjoint_parents']}</option>
        <option value="conjoint_seul">{s['rh_situation_conjoint_seul']}</option>
        <option value="descendants_seuls">{s['rh_situation_descendants_seuls']}</option>
        <option value="parents_seuls">{s['rh_situation_parents_seuls']}</option>
      </select>
    </label>
    <label class="calc-field">{s['rh_nb_enfants_label']}
      <input type="number" id="calc-rh-nb-enfants" min="1" step="1" inputmode="numeric" value="1">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-rh-btn">{s['rh_btn']}</button>
  <div id="calc-rh-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['rh_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "delai_conge":
        js = _JS_DELAI_CONGE.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-dc">
  <h2 style="margin-top:0;">{s['dc_heading']}</h2>
  <p class="calc-disclaimer">{s['dc_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['dc_type_label']}
      <select id="calc-dc-type">
        <option value="habitation">{s['dc_type_habitation']}</option>
        <option value="commercial">{s['dc_type_commercial']}</option>
      </select>
    </label>
    <label class="calc-field">{s['dc_date_envoi_label']}
      <input type="date" id="calc-dc-date-envoi">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-dc-btn">{s['dc_btn']}</button>
  <div id="calc-dc-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['dc_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "mise_en_demeure":
        js = _JS_MISE_EN_DEMEURE.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-md">
  <h2 style="margin-top:0;">{s['md_heading']}</h2>
  <p class="calc-disclaimer">{s['md_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['md_creancier_nom_label']}
      <input type="text" id="calc-md-creancier-nom">
    </label>
    <label class="calc-field">{s['md_creancier_adresse_label']}
      <input type="text" id="calc-md-creancier-adresse">
    </label>
    <label class="calc-field">{s['md_debiteur_nom_label']}
      <input type="text" id="calc-md-debiteur-nom">
    </label>
    <label class="calc-field">{s['md_debiteur_adresse_label']}
      <input type="text" id="calc-md-debiteur-adresse">
    </label>
    <label class="calc-field">{s['md_objet_label']}
      <input type="text" id="calc-md-objet">
    </label>
    <label class="calc-field">{s['md_montant_label']}
      <input type="number" id="calc-md-montant" min="0" step="0.05" inputmode="decimal">
    </label>
    <label class="calc-field">{s['md_delai_grace_label']}
      <input type="number" id="calc-md-delai-grace" min="1" step="1" inputmode="numeric" value="10">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-md-btn">{s['md_btn']}</button>
  <div id="calc-md-result" class="calc-result" hidden>
    <h3 style="margin-top:0;">{s['md_result_heading']}</h3>
    <textarea id="calc-md-letter" readonly rows="16" style="width:100%; font-family:inherit; padding:10px; border-radius:var(--radius-sm); border:1px solid var(--border-strong);"></textarea>
    <button type="button" class="cta-btn" id="calc-md-copy-btn" style="margin-top:var(--space-sm);">{s['md_copy_btn']}</button>
  </div>
  <p class="calc-source">{s['md_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "delai_licenciement":
        js = _JS_DELAI_LICENCIEMENT.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-dl">
  <h2 style="margin-top:0;">{s['dl_heading']}</h2>
  <p class="calc-disclaimer">{s['dl_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['dl_essai_label']}
      <select id="calc-dl-essai">
        <option value="non">{s['dl_essai_non']}</option>
        <option value="oui">{s['dl_essai_oui']}</option>
      </select>
    </label>
    <label class="calc-field" id="calc-dl-row-engagement">{s['dl_date_engagement_label']}
      <input type="date" id="calc-dl-date-engagement">
    </label>
    <label class="calc-field">{s['dl_date_notification_label']}
      <input type="date" id="calc-dl-date-notification">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-dl-btn">{s['dl_btn']}</button>
  <div id="calc-dl-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['dl_source']}</p>
</div>
<script>{js}</script>
"""
    if kind == "delai_recours":
        js = _JS_DELAI_RECOURS.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
        return f"""
<div class="calc-box" id="calc-dr">
  <h2 style="margin-top:0;">{s['dr_heading']}</h2>
  <p class="calc-disclaimer">{s['dr_disclaimer']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['dr_date_notif_label']}
      <input type="date" id="calc-dr-date-notif">
    </label>
    <label class="calc-field">{s['dr_jours_label']}
      <input type="number" id="calc-dr-jours" min="1" step="1" inputmode="numeric">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-dr-btn">{s['dr_btn']}</button>
  <div id="calc-dr-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['dr_source']}</p>
</div>
<script>{js}</script>
"""
    raise ValueError(kind)


PRESCRIPTION_HTML = {lang: _widget(lang, "prescription") for lang in ("fr", "de", "it", "en")}
DELAI_HTML = {lang: _widget(lang, "delai") for lang in ("fr", "de", "it", "en")}
INTERETS_HTML = {lang: _widget(lang, "interets") for lang in ("fr", "de", "it", "en")}
AMENDE_HTML = {lang: _widget(lang, "amende") for lang in ("fr", "de", "it", "en")}
RESILIATION_BAIL_HTML = {lang: _widget(lang, "resiliation_bail") for lang in ("fr", "de", "it", "en")}
PENSION_HTML = {lang: _widget(lang, "pension") for lang in ("fr", "de", "it", "en")}
FRAIS_POURSUITE_HTML = {lang: _widget(lang, "frais_poursuite") for lang in ("fr", "de", "it", "en")}
SOUS_LOCATION_HTML = {lang: _widget(lang, "sous_location") for lang in ("fr", "de", "it", "en")}
RESERVE_HEREDITAIRE_HTML = {lang: _widget(lang, "reserve_hereditaire") for lang in ("fr", "de", "it", "en")}
DELAI_CONGE_HTML = {lang: _widget(lang, "delai_conge") for lang in ("fr", "de", "it", "en")}
MISE_EN_DEMEURE_HTML = {lang: _widget(lang, "mise_en_demeure") for lang in ("fr", "de", "it", "en")}
DELAI_LICENCIEMENT_HTML = {lang: _widget(lang, "delai_licenciement") for lang in ("fr", "de", "it", "en")}
DELAI_RECOURS_HTML = {lang: _widget(lang, "delai_recours") for lang in ("fr", "de", "it", "en")}
