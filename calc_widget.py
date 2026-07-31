"""Simulateur d'eligibilite a l'assistance juridique -- canton de Geneve uniquement.

Principe de non-fabrication applique strictement : chaque chiffre utilise ici
est cite et date, aucune approximation inventee.

Sources :
- Normes d'insaisissabilite pour l'annee 2026 (NI-2026), rsGE E 3 60.04,
  adoptees le 20.11.2025 par la Chambre de surveillance des Offices des
  poursuites et des faillites de Geneve, en vigueur depuis le 01.01.2026 :
  montants de base mensuels et supplements par enfant.
- Majoration de 20% du montant de base : pratique du greffe de l'assistance
  juridique genevois, documentee avec un exemple chiffre complet dans la
  fiche cantonale "Assistance juridique" de guidesocial.ch (Geneve),
  actualisee le 14.05.2019.
- Brochure officielle "Assistance juridique en matiere civile et
  administrative", Pouvoir judiciaire de la Republique et canton de Geneve,
  edition fevrier 2025 (justice.ge.ch) : methode generale (minimum vital +
  charges reconnues compares au revenu net) et bases legales (CPC art. 117
  et ss., LaCC art. 21, RAJ -- rsGE E 2 05.04).

Volontairement absent de ce simulateur : un seuil chiffre pour la fortune.
Aucune source officielle ne fixe de montant fixe -- le greffe l'evalue au cas
par cas -- donc aucun chiffre n'est invente ici ; le widget le rappelle
explicitement, de meme que les chances de succes de la cause (art. 117 al. 1
let. b CPC), deuxieme condition legale non calculable automatiquement.
"""

import json

_JS_TEMPLATE = """
(function() {
  var STR = __STRINGS_JSON__;
  var BASE = { seul: 1200, mono: 1350, couple: 1700 };
  var ENFANT_MOINS10 = 400;
  var ENFANT_PLUS10 = 600;
  var MAJORATION = 1.20;

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
    var v = parseFloat(document.getElementById(id).value);
    return isNaN(v) || v < 0 ? 0 : v;
  }

  function calc() {
    var situation = document.getElementById('calc-aj-situation').value;
    var e10m = num('calc-aj-enf10moins');
    var e10p = num('calc-aj-enf10plus');
    var loyer = num('calc-aj-loyer');
    var lamal = num('calc-aj-lamal');
    var autres = num('calc-aj-autres');
    var impots = num('calc-aj-impots');
    var revenu = num('calc-aj-revenu');

    var base = (BASE[situation] || BASE.seul) + e10m * ENFANT_MOINS10 + e10p * ENFANT_PLUS10;
    var minVitalMajore = base * MAJORATION;
    var seuil = minVitalMajore + loyer + lamal + autres + impots;
    var ecart = revenu - seuil;

    var result = document.getElementById('calc-aj-result');
    result.hidden = false;
    var lines = '';
    lines += '<p>' + STR.label_min_vital.replace('{n}', fmt(minVitalMajore)) + '</p>';
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
})();
"""

STRINGS = {
    "fr": {
        "heading": "Simulateur d'éligibilité à l'assistance juridique (canton de Genève)",
        "disclaimer": "Ce simulateur ne s'applique qu'aux procédures dans le canton de Genève. "
                       "Chaque canton suisse applique son propre barème ; pour les autres cantons, "
                       "adressez-vous au tribunal compétent. Le résultat est une estimation "
                       "indicative, pas une décision : le greffe de l'assistance juridique examine "
                       "aussi votre fortune et les chances de succès de votre cause, deux conditions "
                       "non calculées ici.",
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
        "label_min_vital": "Minimum vital majoré de 20 % : {n} CHF",
        "label_seuil": "Seuil total (minimum vital + charges reconnues) : {n} CHF",
        "label_revenu": "Revenu net mensuel déclaré : {n} CHF",
        "label_solde_neg": "Votre revenu est inférieur au seuil de {n} CHF : c'est en votre faveur.",
        "label_solde_pos": "Votre revenu dépasse le seuil de {n} CHF.",
        "footer_note": "N'oubliez pas : la fortune et les chances de succès de votre cause sont "
                        "aussi examinées par le greffe, indépendamment de ce calcul.",
        "source": "Basé sur les normes d'insaisissabilité 2026 du canton de Genève (NI-2026, rsGE "
                   "E 3 60.04, en vigueur depuis le 1ᵉʳ janvier 2026), majorées de 20 % selon la "
                   "pratique du greffe de l'assistance juridique (source : fiche cantonale Genève, "
                   "guidesocial.ch, actualisée le 14 mai 2019), et la brochure officielle "
                   "« Assistance juridique en matière civile et administrative » du Pouvoir "
                   "judiciaire genevois (édition février 2025). Cette estimation ne remplace pas "
                   "l'examen du dossier par le greffe et ne tient compte ni de votre fortune, ni "
                   "des chances de succès de votre cause.",
    },
    "de": {
        "heading": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Genf)",
        "disclaimer": "Dieser Simulator gilt nur für Verfahren im Kanton Genf. Jeder Schweizer "
                       "Kanton wendet eigene Ansätze an; wenden Sie sich für andere Kantone an das "
                       "zuständige Gericht. Das Ergebnis ist eine unverbindliche Schätzung, keine "
                       "Entscheidung: Die Geschäftsstelle der Rechtspflege prüft zusätzlich Ihr "
                       "Vermögen und die Erfolgsaussichten Ihrer Sache. Diese beiden Voraussetzungen "
                       "werden hier nicht berechnet.",
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
        "label_min_vital": "Um 20 % erhöhtes Existenzminimum: {n} CHF",
        "label_seuil": "Gesamtschwelle (Existenzminimum + anerkannte Auslagen): {n} CHF",
        "label_revenu": "Angegebenes monatliches Nettoeinkommen: {n} CHF",
        "label_solde_neg": "Ihr Einkommen liegt {n} CHF unter der Schwelle: das spricht für Sie.",
        "label_solde_pos": "Ihr Einkommen liegt {n} CHF über der Schwelle.",
        "footer_note": "Nicht vergessen: Vermögen und Erfolgsaussichten Ihrer Sache werden von der "
                        "Geschäftsstelle zusätzlich geprüft, unabhängig von dieser Berechnung.",
        "source": "Grundlage: Normes d'insaisissabilité 2026 des Kantons Genf (NI-2026, rsGE E 3 "
                  "60.04, in Kraft seit 01.01.2026), um 20 % erhöht gemäss Praxis der Genfer "
                  "Geschäftsstelle der Rechtspflege (Quelle: Kantonsblatt Genf, guidesocial.ch, "
                  "aktualisiert am 14.05.2019) sowie der offiziellen Broschüre «Assistance "
                  "juridique en matière civile et administrative» der Genfer Justizbehörde "
                  "(Ausgabe Februar 2025). Diese Schätzung ersetzt nicht die Prüfung durch die "
                  "Geschäftsstelle und berücksichtigt weder Ihr Vermögen noch die "
                  "Erfolgsaussichten Ihrer Sache.",
    },
    "it": {
        "heading": "Simulatore: diritto al gratuito patrocinio (Cantone di Ginevra)",
        "disclaimer": "Questo simulatore vale solo per le procedure nel Cantone di Ginevra. Ogni "
                       "cantone svizzero applica il proprio barème; per gli altri cantoni "
                       "rivolgetevi al tribunale competente. Il risultato è una stima indicativa, "
                       "non una decisione: la cancelleria dell'assistenza giuridica esamina anche "
                       "il vostro patrimonio e le probabilità di successo della causa, due "
                       "condizioni non calcolate qui.",
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
        "label_min_vital": "Minimo vitale maggiorato del 20%: {n} CHF",
        "label_seuil": "Soglia totale (minimo vitale + oneri riconosciuti): {n} CHF",
        "label_revenu": "Reddito netto mensile dichiarato: {n} CHF",
        "label_solde_neg": "Il vostro reddito è inferiore alla soglia di {n} CHF: ciò gioca a "
                            "vostro favore.",
        "label_solde_pos": "Il vostro reddito supera la soglia di {n} CHF.",
        "footer_note": "Da non dimenticare: patrimonio e probabilità di successo della causa sono "
                        "esaminati a parte dalla cancelleria, indipendentemente da questo calcolo.",
        "source": "Basato su: normes d'insaisissabilité 2026 del Cantone di Ginevra (NI-2026, rsGE "
                  "E 3 60.04, in vigore dal 01.01.2026), maggiorate del 20% secondo la prassi "
                  "della cancelleria ginevrina dell'assistenza giuridica (fonte: scheda cantonale "
                  "Ginevra, guidesocial.ch, aggiornata il 14.05.2019) e l'opuscolo ufficiale "
                  "«Assistance juridique en matière civile et administrative» del potere "
                  "giudiziario ginevrino (edizione febbraio 2025). Questa stima non sostituisce "
                  "l'esame della cancelleria e non tiene conto del patrimonio né delle "
                  "probabilità di successo della causa.",
    },
    "en": {
        "heading": "Legal aid eligibility estimator (Canton of Geneva)",
        "disclaimer": "This estimator only applies to proceedings in the Canton of Geneva. Each "
                       "Swiss canton applies its own scale; for other cantons, contact the "
                       "competent court. The result is an indicative estimate, not a decision: "
                       "the legal aid registry also assesses your assets and the prospects of "
                       "success of your case, two conditions not calculated here.",
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
        "label_min_vital": "Subsistence minimum increased by 20%: {n} CHF",
        "label_seuil": "Total threshold (subsistence minimum + recognised expenses): {n} CHF",
        "label_revenu": "Declared net monthly income: {n} CHF",
        "label_solde_neg": "Your income is {n} CHF below the threshold: this is in your favour.",
        "label_solde_pos": "Your income is {n} CHF above the threshold.",
        "footer_note": "Keep in mind: your assets and the prospects of success of your case are "
                        "also assessed separately by the registry, independently of this "
                        "calculation.",
        "source": "Based on: the Canton of Geneva's 2026 seizure-exemption norms (NI-2026, rsGE "
                  "E 3 60.04, in force since 01.01.2026), increased by 20% per the practice of "
                  "Geneva's legal aid registry (source: Geneva cantonal factsheet, guidesocial.ch, "
                  "updated 14.05.2019), and the official brochure \"Assistance juridique en "
                  "matière civile et administrative\" published by the Geneva judiciary "
                  "(February 2025 edition). This estimate does not replace the registry's review "
                  "and does not account for your assets or the prospects of success of your case.",
    },
}


def widget_html(lang):
    s = STRINGS[lang]
    js = _JS_TEMPLATE.replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
    return f"""
<div class="calc-box" id="calc-aj-ge">
  <h2 style="margin-top:0;">{s['heading']}</h2>
  <p class="calc-disclaimer">{s['disclaimer']}</p>
  <div class="calc-grid">
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
    <label class="calc-field">{s['impots']}
      <input type="number" id="calc-aj-impots" min="0" step="10" value="0" inputmode="numeric">
    </label>
    <label class="calc-field">{s['revenu']}
      <input type="number" id="calc-aj-revenu" min="0" step="10" value="0" inputmode="numeric">
    </label>
  </div>
  <button type="button" class="cta-btn is-primary" id="calc-aj-btn">{s['btn']}</button>
  <div id="calc-aj-result" class="calc-result" hidden></div>
  <p class="calc-source">{s['source']}</p>
</div>
<script>{js}</script>
"""


CALCULATOR_HTML = {lang: widget_html(lang) for lang in ("fr", "de", "it", "en")}
