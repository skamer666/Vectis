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
    raise ValueError(kind)


PRESCRIPTION_HTML = {lang: _widget(lang, "prescription") for lang in ("fr", "de", "it", "en")}
DELAI_HTML = {lang: _widget(lang, "delai") for lang in ("fr", "de", "it", "en")}
INTERETS_HTML = {lang: _widget(lang, "interets") for lang in ("fr", "de", "it", "en")}
