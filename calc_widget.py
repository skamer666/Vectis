"""Simulateur d'eligibilite a l'assistance juridique -- Geneve et Lucerne.

Principe de non-fabrication applique strictement : chaque chiffre utilise ici
est cite et date. Seuls deux cantons sont couverts, parce que ce sont les deux
seuls pour lesquels une source officielle publique donne un pourcentage de
majoration FIXE et verifiable a la lecture directe du texte (pas une synthese
IA de recherche web, qui s'est averee peu fiable sur ce point precis -- deux
sources concurrentes se sont contredites sur le pourcentage lucernois avant
verification). Pour les 21 autres cantons actifs du site, la recherche menee
(Zurich, Vaud, Argovie, Tessin, Saint-Gall, Grisons) montre que la majoration
est soit fixee au cas par cas par le juge (ex. Zurich, le Tribunal federal
n'imposant aucun taux contraignant), soit non publiee sur le web public (elle
existe dans la jurisprudence cantonale mais n'est accessible que via des
bases de donnees juridiques payantes). Plutot que d'inventer ou d'extrapoler
un chiffre, ces cantons restent hors du simulateur.

Sources par canton :

GENEVE
- Normes d'insaisissabilite pour l'annee 2026 (NI-2026), rsGE E 3 60.04,
  adoptees le 20.11.2025 par la Chambre de surveillance des Offices des
  poursuites et des faillites de Geneve, en vigueur depuis le 01.01.2026 :
  montants de base mensuels et supplements par enfant.
- Majoration de 20% du montant de base (base + enfants) : pratique du greffe
  de l'assistance juridique genevois, documentee avec un exemple chiffre
  complet (verifie au franc pres par calcul) dans la fiche cantonale
  "Assistance juridique" de guidesocial.ch (Geneve), actualisee le 14.05.2019.
- Brochure officielle "Assistance juridique en matiere civile et
  administrative", Pouvoir judiciaire de la Republique et canton de Geneve,
  edition fevrier 2025 (justice.ge.ch) : methode generale (minimum vital +
  charges reconnues compares au revenu net) et bases legales (CPC art. 117
  et ss., LaCC art. 21, RAJ -- rsGE E 2 05.04). Les impots effectivement payes
  sont explicitement ajoutes au seuil selon cette methode.

LUCERNE
- "Weisung zur Berechnung des betreibungsrechtlichen Notbedarfs
  (Existenzminimum) bei Lohn- und Verdienstpfaendungen", Commission de
  surveillance des poursuites et faillites de l'Obergericht lucernois, du
  13.08.2009 (LGVE 2009 I Nr. 42), en vigueur depuis le 01.10.2009, version
  consultee sur steuerbuch.lu.ch (derniere mise a jour indiquee : 01.01.2024).
  Memes montants de base que Geneve (1200/1350/1700 CHF, enfants 400/600 CHF)
  -- les deux cantons reprennent les lignes directrices nationales de la
  Conference des preposes aux poursuites et faillites de Suisse.
- Majoration de 20% du montant de base (base + enfants) pour le calcul du
  "notbedarf" specifique a l'assistance judiciaire : Cornelia Jozic et Kurt
  Boesch, "Die unentgeltliche Rechtspflege im Zivilprozess -- Praxis des
  Obergerichts des Kantons Luzern", 4e edition, mai 2012, publication
  officielle de l'Obergericht lucernois, citant LGVE 2003 I Nr. 39.
- Difference importante avec Geneve : selon la Weisung du 13.08.2009
  elle-meme (section III), les impots ne sont PAS pris en compte dans ce
  calcul lucernois (contrairement a Geneve qui les ajoute explicitement).
  Aucune source consultee ne confirme qu'ils seraient reintegres pour le
  calcul specifique a l'assistance judiciaire -- par prudence, ce simulateur
  ne les ajoute donc pas pour Lucerne (pas de fabrication d'une regle non
  confirmee).

Volontairement absent de ce simulateur, pour les deux cantons : un seuil
chiffre pour la fortune (aucune source officielle ne fixe de montant fixe --
evaluee au cas par cas) et les chances de succes de la cause (art. 117 al. 1
let. b CPC), deuxieme condition legale non calculable automatiquement. Le
widget le rappelle explicitement.
"""

import json

CANTONS = {
    "GE": {"majoration_pct": 20, "includes_impots": True},
    "LU": {"majoration_pct": 20, "includes_impots": False},
}

_JS_TEMPLATE = """
(function() {
  var STR = __STRINGS_JSON__;
  var CANTONS = __CANTONS_JSON__;
  var BASE = { seul: 1200, mono: 1350, couple: 1700 };
  var ENFANT_MOINS10 = 400;
  var ENFANT_PLUS10 = 600;

  function fmt(n) {
    n = Math.round(n);
    var s = Math.abs(n).toString();
    var out = '';
    for (var i = 0; i < s.length; i++) {
      if (i > 0 && (s.length - i) % 3 === 0) out += '\\u2019';
      out += s[i];
    }
    return (n < 0 ? '-' : '') + out;
  }

  function num(id) {
    var el = document.getElementById(id);
    if (!el) return 0;
    var v = parseFloat(el.value);
    return isNaN(v) || v < 0 ? 0 : v;
  }

  function currentCanton() {
    return document.getElementById('calc-aj-canton').value;
  }

  function updateCantonUI() {
    var code = currentCanton();
    var cfg = CANTONS[code];
    var impotsRow = document.getElementById('calc-aj-impots-row');
    if (impotsRow) impotsRow.hidden = !cfg.includes_impots;
    var headingEl = document.getElementById('calc-aj-heading');
    var discEl = document.getElementById('calc-aj-disclaimer');
    var sourceEl = document.getElementById('calc-aj-source-text');
    if (headingEl) headingEl.textContent = STR['heading_' + code];
    if (discEl) discEl.textContent = STR['disclaimer_' + code];
    if (sourceEl) sourceEl.textContent = STR['source_' + code];
    var result = document.getElementById('calc-aj-result');
    if (result) result.hidden = true;
  }

  function calc() {
    var code = currentCanton();
    var cfg = CANTONS[code];
    var situation = document.getElementById('calc-aj-situation').value;
    var e10m = num('calc-aj-enf10moins');
    var e10p = num('calc-aj-enf10plus');
    var loyer = num('calc-aj-loyer');
    var lamal = num('calc-aj-lamal');
    var autres = num('calc-aj-autres');
    var impots = cfg.includes_impots ? num('calc-aj-impots') : 0;
    var revenu = num('calc-aj-revenu');

    var base = (BASE[situation] || BASE.seul) + e10m * ENFANT_MOINS10 + e10p * ENFANT_PLUS10;
    var minVitalMajore = base * (1 + cfg.majoration_pct / 100);
    var seuil = minVitalMajore + loyer + lamal + autres + impots;
    var ecart = revenu - seuil;

    var result = document.getElementById('calc-aj-result');
    result.hidden = false;
    var lines = '';
    lines += '<p>' + STR.label_min_vital.replace('{pct}', cfg.majoration_pct).replace('{n}', fmt(minVitalMajore)) + '</p>';
    lines += '<p>' + STR.label_seuil.replace('{n}', fmt(seuil)) + '</p>';
    lines += '<p>' + STR.label_revenu.replace('{n}', fmt(revenu)) + '</p>';
    if (ecart <= 0) {
      result.className = 'calc-result is-eligible';
      lines = '<strong>' + STR.result_eligible_title + '</strong>' +
        '<p>' + STR.label_solde_neg.replace('{n}', fmt(Math.abs(ecart))) + '</p>' + lines;
    } else {
      result.className = 'calc-result is-not-eligible';
      lines = '<strong>' + STR.result_not_eligible_title + '</strong>' +
        '<p>' + STR.label_solde_pos.replace('{n}', fmt(ecart)) + '</p>' + lines;
    }
    lines += '<p class="calc-footnote">' + STR.footer_note + '</p>';
    result.innerHTML = lines;
  }

  var btn = document.getElementById('calc-aj-btn');
  if (btn) { btn.addEventListener('click', calc); }
  var cantonSelect = document.getElementById('calc-aj-canton');
  if (cantonSelect) { cantonSelect.addEventListener('change', updateCantonUI); }
  updateCantonUI();
})();
"""

STRINGS = {
    "fr": {
        "canton_label": "Canton concerné par la procédure",
        "canton_ge": "Genève",
        "canton_lu": "Lucerne",
        "heading_GE": "Simulateur d'éligibilité à l'assistance juridique (canton de Genève)",
        "heading_LU": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Lucerne)",
        "disclaimer_GE": "Ce calcul ne s'applique qu'aux procédures dans le canton de Genève. "
                       "Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le "
                       "résultat est une estimation indicative, pas une décision : le greffe de "
                       "l'assistance juridique examine aussi votre fortune et les chances de "
                       "succès de votre cause, deux conditions non calculées ici.",
        "disclaimer_LU": "Ce calcul ne s'applique qu'aux procédures dans le canton de Lucerne, et "
                       "ne tient pas compte des impôts (non intégrés dans le calcul lucernois "
                       "d'après la source officielle utilisée). Changez de canton ci-dessus si "
                       "votre procédure se déroule ailleurs. Le résultat est une estimation "
                       "indicative, pas une décision : le tribunal examine aussi votre fortune et "
                       "les chances de succès de votre cause, deux conditions non calculées ici.",
        "unsupported_canton_note": "Seuls Genève et Lucerne disposent d'un pourcentage de "
                       "majoration officiellement publié et vérifiable. Pour les autres cantons, "
                       "consultez le tribunal compétent : chaque canton applique son propre barème.",
        "situation": "Votre situation familiale",
        "opt_seul": "Vous vivez seul·e, sans enfant à charge",
        "opt_mono": "Vous êtes seul·e avec un ou plusieurs enfants à charge (famille monoparentale)",
        "opt_couple": "Vous êtes marié·e, en partenariat enregistré, ou en couple avec des enfants à charge",
        "enf_moins10": "Nombre d'enfants à charge de moins de 10 ans",
        "enf_plus10": "Nombre d'enfants à charge de 10 ans ou plus",
        "loyer": "Loyer mensuel net (hors charges de chauffage), en CHF",
        "lamal": "Prime d'assurance-maladie obligatoire (par mois, en CHF)",
        "autres": "Autres charges reconnues : frais professionnels indispensables, pensions "
                  "alimentaires versées, etc. (par mois, en CHF)",
        "impots": "Impôts mensuels effectivement payés, y compris arriérés (en CHF)",
        "revenu": "Revenu net mensuel total du foyer, toutes ressources confondues (en CHF)",
        "btn": "Estimer mon éligibilité",
        "result_eligible_title": "Votre situation semble ouvrir droit à l'assistance juridique",
        "result_not_eligible_title": "Sur ces chiffres, le seuil ne semble pas atteint",
        "label_min_vital": "Minimum vital majoré de {pct} % : {n} CHF",
        "label_seuil": "Seuil total (minimum vital + charges reconnues) : {n} CHF",
        "label_revenu": "Revenu net mensuel déclaré : {n} CHF",
        "label_solde_neg": "Votre revenu est inférieur au seuil de {n} CHF : c'est en votre faveur.",
        "label_solde_pos": "Votre revenu dépasse le seuil de {n} CHF.",
        "footer_note": "N'oubliez pas : la fortune et les chances de succès de votre cause sont "
                        "aussi examinées par le tribunal, indépendamment de ce calcul.",
        "source_GE": "Basé sur les normes d'insaisissabilité 2026 du canton de Genève (NI-2026, "
                   "rsGE E 3 60.04, en vigueur depuis le 1ᵉʳ janvier 2026), majorées de 20 % selon "
                   "la pratique du greffe de l'assistance juridique (source : fiche cantonale "
                   "Genève, guidesocial.ch, actualisée le 14 mai 2019), et la brochure officielle "
                   "« Assistance juridique en matière civile et administrative » du Pouvoir "
                   "judiciaire genevois (édition février 2025). Cette estimation ne remplace pas "
                   "l'examen du dossier par le greffe et ne tient compte ni de votre fortune, ni "
                   "des chances de succès de votre cause.",
        "source_LU": "Basé sur la Weisung du 13 août 2009 de la Commission de surveillance des "
                   "poursuites et faillites de l'Obergericht lucernois (LGVE 2009 I n° 42, en "
                   "vigueur depuis le 1ᵉʳ octobre 2009, consultée sur steuerbuch.lu.ch), majorée "
                   "de 20 % selon la pratique confirmée dans Jozic/Boesch, « Die unentgeltliche "
                   "Rechtspflege im Zivilprozess », Obergericht du canton de Lucerne, 4ᵉ édition, "
                   "mai 2012 (citant LGVE 2003 I n° 39). Les impôts ne sont pas comptés dans ce "
                   "calcul, conformément à cette même source. Cette estimation ne remplace pas "
                   "l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, "
                   "ni des chances de succès de votre cause.",
    },
    "de": {
        "canton_label": "Kanton des Verfahrens",
        "canton_ge": "Genf",
        "canton_lu": "Luzern",
        "heading_GE": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Genf)",
        "heading_LU": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Luzern)",
        "disclaimer_GE": "Diese Berechnung gilt nur für Verfahren im Kanton Genf. Wählen Sie oben "
                       "einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das "
                       "Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Die "
                       "Geschäftsstelle prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten "
                       "Ihrer Sache. Diese beiden Voraussetzungen werden hier nicht berechnet.",
        "disclaimer_LU": "Diese Berechnung gilt nur für Verfahren im Kanton Luzern und "
                       "berücksichtigt keine Steuern (gemäss der verwendeten offiziellen Quelle "
                       "nicht Teil der luzernischen Berechnung). Wählen Sie oben einen anderen "
                       "Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine "
                       "unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich "
                       "Ihr Vermögen und die Erfolgsaussichten Ihrer Sache.",
        "unsupported_canton_note": "Nur Genf und Luzern verfügen über einen offiziell "
                       "publizierten und nachprüfbaren Zuschlagssatz. Für andere Kantone wenden "
                       "Sie sich an das zuständige Gericht: jeder Kanton wendet einen eigenen "
                       "Ansatz an.",
        "situation": "Ihre familiäre Situation",
        "opt_seul": "Sie leben allein, ohne unterhaltsberechtigte Kinder",
        "opt_mono": "Sie sind alleinerziehend mit einem oder mehreren unterhaltsberechtigten Kindern",
        "opt_couple": "Sie sind verheiratet, in eingetragener Partnerschaft oder leben als Paar mit "
                      "unterhaltsberechtigten Kindern",
        "enf_moins10": "Anzahl unterhaltsberechtigter Kinder unter 10 Jahren",
        "enf_plus10": "Anzahl unterhaltsberechtigter Kinder ab 10 Jahren",
        "loyer": "Monatlicher Nettomietzins (ohne Heizkosten), in CHF",
        "lamal": "Obligatorische Krankenkassenprämie (pro Monat, in CHF)",
        "autres": "Weitere anerkannte Auslagen: notwendige Berufsauslagen, geleistete "
                  "Unterhaltsbeiträge usw. (pro Monat, in CHF)",
        "impots": "Tatsächlich bezahlte monatliche Steuern, inkl. Rückstände (in CHF)",
        "revenu": "Monatliches Nettoeinkommen des Haushalts insgesamt (in CHF)",
        "btn": "Anspruch schätzen",
        "result_eligible_title": "Ihre Situation scheint einen Anspruch auf unentgeltliche "
                                  "Rechtspflege zu begründen",
        "result_not_eligible_title": "Aufgrund dieser Zahlen scheint die Schwelle nicht erreicht",
        "label_min_vital": "Um {pct} % erhöhtes Existenzminimum: {n} CHF",
        "label_seuil": "Gesamtschwelle (Existenzminimum + anerkannte Auslagen): {n} CHF",
        "label_revenu": "Angegebenes monatliches Nettoeinkommen: {n} CHF",
        "label_solde_neg": "Ihr Einkommen liegt {n} CHF unter der Schwelle: das spricht für Sie.",
        "label_solde_pos": "Ihr Einkommen liegt {n} CHF über der Schwelle.",
        "footer_note": "Nicht vergessen: Vermögen und Erfolgsaussichten Ihrer Sache werden vom "
                        "Gericht zusätzlich geprüft, unabhängig von dieser Berechnung.",
        "source_GE": "Grundlage: Normes d'insaisissabilité 2026 des Kantons Genf (NI-2026, rsGE E 3 "
                  "60.04, in Kraft seit 01.01.2026), um 20 % erhöht gemäss Praxis der Genfer "
                  "Geschäftsstelle der Rechtspflege (Quelle: Kantonsblatt Genf, guidesocial.ch, "
                  "aktualisiert am 14.05.2019) sowie der offiziellen Broschüre «Assistance "
                  "juridique en matière civile et administrative» der Genfer Justizbehörde "
                  "(Ausgabe Februar 2025). Diese Schätzung ersetzt nicht die Prüfung durch die "
                  "Geschäftsstelle und berücksichtigt weder Ihr Vermögen noch die "
                  "Erfolgsaussichten Ihrer Sache.",
        "source_LU": "Grundlage: Weisung vom 13. August 2009 der Schuldbetreibungs- und "
                  "Konkurskommission des Obergerichts Luzern (LGVE 2009 I Nr. 42, in Kraft seit "
                  "01.10.2009, eingesehen auf steuerbuch.lu.ch), um 20 % erhöht gemäss der in "
                  "Jozic/Boesch, «Die unentgeltliche Rechtspflege im Zivilprozess», Obergericht "
                  "des Kantons Luzern, 4. Auflage, Mai 2012, bestätigten Praxis (unter Hinweis auf "
                  "LGVE 2003 I Nr. 39). Steuern sind gemäss derselben Quelle nicht in dieser "
                  "Berechnung enthalten. Diese Schätzung ersetzt nicht die Prüfung durch das "
                  "Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer "
                  "Sache.",
    },
    "it": {
        "canton_label": "Cantone della procedura",
        "canton_ge": "Ginevra",
        "canton_lu": "Lucerna",
        "heading_GE": "Simulatore: diritto al gratuito patrocinio (Cantone di Ginevra)",
        "heading_LU": "Simulatore: diritto al gratuito patrocinio (Cantone di Lucerna)",
        "disclaimer_GE": "Questo calcolo vale solo per le procedure nel Cantone di Ginevra. "
                       "Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il "
                       "risultato è una stima indicativa, non una decisione: la cancelleria "
                       "esamina anche il vostro patrimonio e le probabilità di successo della "
                       "causa, due condizioni non calcolate qui.",
        "disclaimer_LU": "Questo calcolo vale solo per le procedure nel Cantone di Lucerna e non "
                       "tiene conto delle imposte (non incluse nel calcolo lucernese secondo la "
                       "fonte ufficiale utilizzata). Cambiate cantone qui sopra se la vostra "
                       "procedura si svolge altrove. Il risultato è una stima indicativa, non una "
                       "decisione: il tribunale esamina anche il vostro patrimonio e le "
                       "probabilità di successo della causa.",
        "unsupported_canton_note": "Solo Ginevra e Lucerna dispongono di una percentuale di "
                       "maggiorazione pubblicata ufficialmente e verificabile. Per gli altri "
                       "cantoni, rivolgetevi al tribunale competente: ogni cantone applica il "
                       "proprio barème.",
        "situation": "La vostra situazione familiare",
        "opt_seul": "Vivete soli, senza figli a carico",
        "opt_mono": "Siete soli con uno o più figli a carico (famiglia monoparentale)",
        "opt_couple": "Siete coniugati, in unione domestica registrata, o in coppia con figli a "
                      "carico",
        "enf_moins10": "Numero di figli a carico di età inferiore a 10 anni",
        "enf_plus10": "Numero di figli a carico di 10 anni o più",
        "loyer": "Pigione mensile netta (senza spese di riscaldamento), in CHF",
        "lamal": "Premio dell'assicurazione malattia obbligatoria (al mese, in CHF)",
        "autres": "Altri oneri riconosciuti: spese professionali indispensabili, contributi di "
                  "mantenimento versati, ecc. (al mese, in CHF)",
        "impots": "Imposte mensili effettivamente pagate, inclusi arretrati (in CHF)",
        "revenu": "Reddito netto mensile totale del nucleo familiare (in CHF)",
        "btn": "Stima la mia idoneità",
        "result_eligible_title": "La vostra situazione sembra dare diritto al gratuito patrocinio",
        "result_not_eligible_title": "In base a queste cifre, la soglia non sembra raggiunta",
        "label_min_vital": "Minimo vitale maggiorato del {pct}%: {n} CHF",
        "label_seuil": "Soglia totale (minimo vitale + oneri riconosciuti): {n} CHF",
        "label_revenu": "Reddito netto mensile dichiarato: {n} CHF",
        "label_solde_neg": "Il vostro reddito è inferiore alla soglia di {n} CHF: ciò gioca a "
                            "vostro favore.",
        "label_solde_pos": "Il vostro reddito supera la soglia di {n} CHF.",
        "footer_note": "Da non dimenticare: patrimonio e probabilità di successo della causa sono "
                        "esaminati a parte dal tribunale, indipendentemente da questo calcolo.",
        "source_GE": "Basato su: normes d'insaisissabilité 2026 del Cantone di Ginevra (NI-2026, "
                  "rsGE E 3 60.04, in vigore dal 01.01.2026), maggiorate del 20% secondo la prassi "
                  "della cancelleria ginevrina dell'assistenza giuridica (fonte: scheda cantonale "
                  "Ginevra, guidesocial.ch, aggiornata il 14.05.2019) e l'opuscolo ufficiale "
                  "«Assistance juridique en matière civile et administrative» del potere "
                  "giudiziario ginevrino (edizione febbraio 2025). Questa stima non sostituisce "
                  "l'esame della cancelleria e non tiene conto del patrimonio né delle "
                  "probabilità di successo della causa.",
        "source_LU": "Basato su: Weisung del 13 agosto 2009 della Commissione di vigilanza sulle "
                  "esecuzioni e i fallimenti dell'Obergericht lucernese (LGVE 2009 I n. 42, in "
                  "vigore dal 01.10.2009, consultata su steuerbuch.lu.ch), maggiorata del 20% "
                  "secondo la prassi confermata in Jozic/Boesch, «Die unentgeltliche Rechtspflege "
                  "im Zivilprozess», Obergericht del Cantone di Lucerna, 4a edizione, maggio 2012 "
                  "(che cita LGVE 2003 I n. 39). Le imposte non sono conteggiate in questo "
                  "calcolo, in base alla stessa fonte. Questa stima non sostituisce l'esame del "
                  "tribunale e non tiene conto del patrimonio né delle probabilità di successo "
                  "della causa.",
    },
    "en": {
        "canton_label": "Canton where the case is handled",
        "canton_ge": "Geneva",
        "canton_lu": "Lucerne",
        "heading_GE": "Legal aid eligibility estimator (Canton of Geneva)",
        "heading_LU": "Legal aid eligibility estimator (Canton of Lucerne)",
        "disclaimer_GE": "This calculation only applies to proceedings in the Canton of Geneva. "
                       "Switch canton above if your case is elsewhere. The result is an "
                       "indicative estimate, not a decision: the legal aid registry also assesses "
                       "your assets and the prospects of success of your case, two conditions not "
                       "calculated here.",
        "disclaimer_LU": "This calculation only applies to proceedings in the Canton of Lucerne "
                       "and does not account for taxes (not part of the Lucerne calculation "
                       "according to the official source used). Switch canton above if your case "
                       "is elsewhere. The result is an indicative estimate, not a decision: the "
                       "court also assesses your assets and the prospects of success of your case.",
        "unsupported_canton_note": "Only Geneva and Lucerne have an officially published, "
                       "verifiable surcharge percentage. For other cantons, contact the competent "
                       "court: each canton applies its own scale.",
        "situation": "Your family situation",
        "opt_seul": "You live alone, with no dependent children",
        "opt_mono": "You are a single parent with one or more dependent children",
        "opt_couple": "You are married, in a registered partnership, or a couple with dependent "
                      "children",
        "enf_moins10": "Number of dependent children under 10",
        "enf_plus10": "Number of dependent children 10 or older",
        "loyer": "Net monthly rent (excluding heating charges), in CHF",
        "lamal": "Mandatory health insurance premium (per month, in CHF)",
        "autres": "Other recognised expenses: necessary work-related costs, maintenance payments "
                  "made, etc. (per month, in CHF)",
        "impots": "Monthly taxes actually paid, including arrears (in CHF)",
        "revenu": "Total net monthly household income (in CHF)",
        "btn": "Estimate my eligibility",
        "result_eligible_title": "Your situation appears to qualify for legal aid",
        "result_not_eligible_title": "Based on these figures, the threshold does not appear to be "
                                      "met",
        "label_min_vital": "Subsistence minimum increased by {pct}%: {n} CHF",
        "label_seuil": "Total threshold (subsistence minimum + recognised expenses): {n} CHF",
        "label_revenu": "Declared net monthly income: {n} CHF",
        "label_solde_neg": "Your income is {n} CHF below the threshold: this is in your favour.",
        "label_solde_pos": "Your income is {n} CHF above the threshold.",
        "footer_note": "Keep in mind: your assets and the prospects of success of your case are "
                        "also assessed separately by the court, independently of this "
                        "calculation.",
        "source_GE": "Based on: the Canton of Geneva's 2026 seizure-exemption norms (NI-2026, "
                  "rsGE E 3 60.04, in force since 01.01.2026), increased by 20% per the practice "
                  "of Geneva's legal aid registry (source: Geneva cantonal factsheet, "
                  "guidesocial.ch, updated 14.05.2019), and the official brochure \"Assistance "
                  "juridique en matière civile et administrative\" published by the Geneva "
                  "judiciary (February 2025 edition). This estimate does not replace the "
                  "registry's review and does not account for your assets or the prospects of "
                  "success of your case.",
        "source_LU": "Based on: the 13 August 2009 directive of the Debt Collection and "
                  "Bankruptcy Supervisory Commission of the Lucerne Cantonal High Court (LGVE "
                  "2009 I No. 42, in force since 01.10.2009, consulted on steuerbuch.lu.ch), "
                  "increased by 20% per the practice confirmed in Jozic/Boesch, \"Die "
                  "unentgeltliche Rechtspflege im Zivilprozess\", Lucerne Cantonal High Court, "
                  "4th edition, May 2012 (citing LGVE 2003 I No. 39). Taxes are not counted in "
                  "this calculation, per the same source. This estimate does not replace the "
                  "court's review and does not account for your assets or the prospects of "
                  "success of your case.",
    },
}


def widget_html(lang):
    s = STRINGS[lang]
    js = (_JS_TEMPLATE
          .replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
          .replace("__CANTONS_JSON__", json.dumps(CANTONS, ensure_ascii=False)))
    return f"""
<div class="calc-box" id="calc-aj-ge">
  <h2 id="calc-aj-heading" style="margin-top:0;">{s['heading_GE']}</h2>
  <p class="calc-disclaimer" id="calc-aj-disclaimer">{s['disclaimer_GE']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['canton_label']}
      <select id="calc-aj-canton">
        <option value="GE">{s['canton_ge']}</option>
        <option value="LU">{s['canton_lu']}</option>
      </select>
    </label>
    <label class="calc-field">{s['situation']}
      <select id="calc-aj-situation">
        <option value="seul">{s['opt_seul']}</option>
        <option value="mono">{s['opt_mono']}</option>
        <option value="couple">{s['opt_couple']}</option>
      </select>
    </label>
    <label class="calc-field">{s['enf_moins10']}
      <input type="number" id="calc-aj-enf10moins" min="0" step="1" value="0" inputmode="numeric">
    </label>
    <label class="calc-field">{s['enf_plus10']}
      <input type="number" id="calc-aj-enf10plus" min="0" step="1" value="0" inputmode="numeric">
    </label>
    <label class="calc-field">{s['loyer']}
      <input type="number" id="calc-aj-loyer" min="0" step="10" value="0" inputmode="numeric">
    </label>
    <label class="calc-field">{s['lamal']}
      <input type="number" id="calc-aj-lamal" min="0" step="10" value="0" inputmode="numeric">
    </label>
    <label class="calc-field">{s['autres']}
      <input type="number" id="calc-aj-autres" min="0" step="10" value="0" inputmode="numeric">
    </label>
    <label class="calc-field" id="calc-aj-impots-row">{s['impots']}
      <input type="number" id="calc-aj-impots" min="0" step="10" value="0" inputmode="numeric">
    </label>
    <label class="calc-field">{s['revenu']}
      <input type="number" id="calc-aj-revenu" min="0" step="10" value="0" inputmode="numeric">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-aj-btn">{s['btn']}</button>
  <div id="calc-aj-result" class="calc-result" hidden></div>
  <p class="calc-source" id="calc-aj-source-text">{s['source_GE']}</p>
  <p class="calc-source">{s['unsupported_canton_note']}</p>
</div>
<script>{js}</script>
"""


CALCULATOR_HTML = {lang: widget_html(lang) for lang in ("fr", "de", "it", "en")}
