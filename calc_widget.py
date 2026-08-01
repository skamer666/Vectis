"""Simulateur d'eligibilite a l'assistance juridique -- Suisse.

Principe de non-fabrication applique strictement : chaque chiffre utilise ici
est cite et date, lu integralement dans sa source primaire (jamais accepte
sur la seule foi d'une synthese IA de recherche web, qui s'est averee peu
fiable a plusieurs reprises sur ce sujet precis -- des sources concurrentes
se sont contredites sur le pourcentage lucernois, puis sur celui d'Argovie,
avant verification directe du texte).

Deux niveaux de confiance coexistent dans ce simulateur :

1. CANTONS A TAUX CONFIRME (Geneve, Lucerne, Grisons, Soleure) : chacun
   dispose d'une decision de justice ou d'un texte officiel qui applique un
   pourcentage de majoration FIXE a un cas concret, presente comme la regle
   (pas comme une approximation). Le detail des sources est donne plus bas,
   canton par canton.

2. ESTIMATION NATIONALE (tous les autres cantons) : a la demande expresse de
   l'utilisateur du site (qui a explicitement accepte qu'une estimation soit
   utilisee a defaut de taux cantonal precis, du moment qu'elle reste
   clairement distinguee des taux confirmes), les cantons sans taux propre
   verifie affichent une estimation batie sur la jurisprudence du Tribunal
   federal : l'arret 8C_470/2016 du 16 decembre 2016 (consid. 5.5) juge que
   "gemass bundesgerichtlicher Rechtsprechung betragt dieser [Zuschlag] 25 %
   des Grundbetrages", en citant l'arret 8C_377/2016 du 8 aout 2016 (consid.
   4.2) et SVR 2010 IV Nr. 10 S. 31 (consid. 8.3) -- une ligne de
   jurisprudence federale constante sur plusieurs annees. Ce même ordre de
   grandeur ("de l'ordre de 25 %") est aussi cite par le Tribunal cantonal
   vaudois en reference a l'ATF 124 I 1. Il s'agit d'un repere frequemment
   cite par les tribunaux, PAS d'un taux officiel garanti pour un canton
   donne -- le simulateur le presente explicitement comme une estimation,
   distincte des quatre cantons a taux confirme.

Recherche menee (jurisprudence cantonale gratuite via entscheidsuche.ch et
bger.ch, en plus des sources reglementaires) sur une quinzaine de cantons :
- Zurich : un arret de l'Obergericht (VO150084-O, 24.06.2015) montre un calcul
  au cas par cas (72,3% d'un montant de reference etranger pour un requerant
  vivant a l'etranger), sans taux general applicable.
- Vaud : un arret de la Chambre des recours civile (HC/2021/124, 03.02.2021)
  cite "de l'ordre de 25%" (ATF 124 I 1) mais applique en pratique 30% dans
  le cas juge -- le texte lui-meme presente ce chiffre comme approximatif et
  laisse a l'appreciation du juge.
- Argovie : un arret de l'Obergericht (ZSU.2022.37, 04.04.2022) mentionne un
  "Zuschlag" de 15 a 30%, mais il s'agit d'un supplement sur l'indemnite de
  l'avocat d'office (tarif des avocats), pas de la majoration du minimum
  vital du requerant -- deux notions distinctes portant le meme nom.
- Berne : la circulaire officielle de l'Obergericht (Kreisschreiben Nr. B1,
  01.04.2010) definit le montant de base mais ne contient AUCUNE majoration
  pour l'assistance judiciaire (uniquement le minimum vital du droit des
  poursuites/saisie) ; aucune decision bernoise donnant un pourcentage AJ
  precis n'a ete trouvee malgre plusieurs recherches cibless.
- Bale-Ville : une decision trouvee (Appellationsgericht, BEZ.2023.62,
  30.11.2023) porte sur le changement d'avocat d'office, sans aucun calcul
  chiffre -- aucune source chiffree trouvee pour ce canton.
- Valais : une decision (Kantonsgericht, F1 24 92/F2 24 1, 11.04.2024) cite
  "20%" en attribuant ce chiffre a l'arret federal 8C_470/2016 -- mais la
  lecture directe de cet arret montre qu'il retient en realite 25%, pas 20%.
  Cette contradiction interne (probable erreur de citation du tribunal
  valaisan lui-meme) rend la source non fiable ; le canton reste donc dans
  l'estimation nationale plutot que dans les taux confirmes.
- Tessin : le canton publie une table officielle du minimum vital (identique
  a celle de Geneve/Lucerne/Grisons/Soleure, impots exclus) mais aucune
  decision trouvee n'applique explicitement une majoration fixe dans le
  contexte specifique du gratuito patrocinio.
- Saint-Gall : un document officiel probablement pertinent existe mais son
  URL, trop longue, provoque une erreur technique du navigateur utilise ici ;
  reste non lu.

Ces cantons, plutot que de recevoir un chiffre invente ou extrapole a partir
d'indices contradictoires, recoivent donc l'estimation nationale generique
(25%, sources ci-dessus), clairement signalee comme telle.

Sources des quatre cantons a taux confirme :

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
  edition fevrier 2025 (justice.ge.ch).

LUCERNE
- "Weisung zur Berechnung des betreibungsrechtlichen Notbedarfs
  (Existenzminimum) bei Lohn- und Verdienstpfaendungen", Commission de
  surveillance des poursuites et faillites de l'Obergericht lucernois, du
  13.08.2009 (LGVE 2009 I Nr. 42), en vigueur depuis le 01.10.2009, version
  consultee sur steuerbuch.lu.ch (derniere mise a jour indiquee : 01.01.2024).
- Majoration de 20% du montant de base : Cornelia Jozic et Kurt Boesch, "Die
  unentgeltliche Rechtspflege im Zivilprozess -- Praxis des Obergerichts des
  Kantons Luzern", 4e edition, mai 2012, citant LGVE 2003 I Nr. 39.
- Difference avec les autres cantons confirmes : les impots ne sont PAS pris
  en compte dans ce calcul lucernois (section III de la Weisung).

GRISONS
- Ordonnance ("Verfuegung") du Kantonsgericht de Grisons du 26 janvier 2023
  (ZK2 22 56), rendue en matiere d'assistance judiciaire, qui applique un
  montant de base identique a Geneve (CHF 1'200.- pour une personne seule,
  citant KGer GR KSK 09 39 du 18.08.2009), majore d'un supplement de 20% du
  montant de base (CHF 240.- dans le cas traite), en citant une
  jurisprudence anterieure du meme tribunal (KGer GR ZK1 14 112 du
  05.01.2015, consid. 5a/aa ; PKG 2003 Nr. 13, consid. 3-5). Les impots sont
  ajoutes s'il est demontre qu'ils ont ete effectivement payes.

SOLEURE
- Arret de l'Obergericht de Soleure (Zivilkammer, ZKBES-2016-177, 22.12.2016)
  qui affirme explicitement : "Bei der Bemessung des zivilprozessualen
  Notbedarfs ist der Grundbetrag jedoch um die im Kanton Solothurn üblichen
  20% zu erweitern" (le montant de base doit etre majore des 20% usuels
  dans le canton de Soleure), applique concretement (CHF 1'200.- + CHF
  240.- = CHF 1'440.-). Les impots sont ajoutes (meme arret, tableau du
  calcul complet).

Volontairement absent de ce simulateur, quel que soit le canton : un seuil
chiffre pour la fortune (aucune source officielle ne fixe de montant fixe --
evaluee au cas par cas) et les chances de succes de la cause (art. 117 al. 1
let. b CPC), deuxieme condition legale non calculable automatiquement.
"""

import json

CANTONS = {
    "GE": {"majoration_pct": 20, "includes_impots": True, "confirmed": True},
    "LU": {"majoration_pct": 20, "includes_impots": False, "confirmed": True},
    "GR": {"majoration_pct": 20, "includes_impots": True, "confirmed": True},
    "SO": {"majoration_pct": 20, "includes_impots": True, "confirmed": True},
    "EST": {"majoration_pct": 25, "includes_impots": True, "confirmed": False},
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
    var box = document.getElementById('calc-aj-ge');
    if (box) {
      if (cfg.confirmed) { box.classList.remove('is-estimate'); }
      else { box.classList.add('is-estimate'); }
    }
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
    if (!cfg.confirmed) {
      lines += '<p class="calc-footnote"><strong>' + STR.estimate_flag + '</strong></p>';
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
        "canton_gr": "Grisons",
        "canton_so": "Soleure",
        "canton_est": "Autre canton (estimation nationale)",
        "heading_GE": "Simulateur d'éligibilité à l'assistance juridique (canton de Genève)",
        "heading_LU": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Lucerne)",
        "heading_GR": "Simulateur d'éligibilité à l'assistance judiciaire (canton des Grisons)",
        "heading_SO": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Soleure)",
        "heading_EST": "Estimation d'éligibilité à l'assistance judiciaire (tous les autres cantons)",
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
        "disclaimer_GR": "Ce calcul ne s'applique qu'aux procédures dans le canton des Grisons. "
                       "Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le "
                       "résultat est une estimation indicative, pas une décision : le tribunal "
                       "examine aussi votre fortune et les chances de succès de votre cause, deux "
                       "conditions non calculées ici.",
        "disclaimer_SO": "Ce calcul ne s'applique qu'aux procédures dans le canton de Soleure. "
                       "Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le "
                       "résultat est une estimation indicative, pas une décision : le tribunal "
                       "examine aussi votre fortune et les chances de succès de votre cause, deux "
                       "conditions non calculées ici.",
        "disclaimer_EST": "Votre canton ne dispose pas (à notre connaissance) d'un pourcentage de "
                       "majoration officiellement publié et vérifiable pour l'assistance "
                       "judiciaire. Ce calcul utilise donc une ESTIMATION générique de 25%, "
                       "reprise de la jurisprudence du Tribunal fédéral (arrêts 8C_470/2016 et "
                       "8C_377/2016) et couramment citée par les tribunaux cantonaux, ce n'est "
                       "PAS le taux officiel de votre canton, seulement un ordre de grandeur. "
                       "Pour un chiffre fiable, contactez le tribunal ou le service d'assistance "
                       "judiciaire de votre canton.",
        "unsupported_canton_note": "Seuls Genève, Lucerne, les Grisons et Soleure disposent d'un "
                       "pourcentage de majoration officiellement publié et vérifiable pour votre "
                       "canton précis. Pour tous les autres cantons, le simulateur affiche une "
                       "estimation nationale distincte (voir ci-dessus) : elle donne un ordre de "
                       "grandeur, pas une garantie.",
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
        "estimate_flag": "Rappel : ce résultat repose sur une estimation nationale (25%), pas sur "
                        "un taux propre à votre canton. Vérifiez auprès du tribunal compétent.",
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
        "source_GR": "Basé sur une ordonnance du Tribunal cantonal des Grisons du 26 janvier 2023 "
                   "(ZK2 22 56), rendue en matière d'assistance judiciaire, qui applique un "
                   "montant de base identique à Genève (CHF 1'200.- pour une personne seule, "
                   "citant KGer GR KSK 09 39 du 18.08.2009), majoré de 20 % selon une "
                   "jurisprudence constante (KGer GR ZK1 14 112 du 05.01.2015 ; PKG 2003 Nr. 13). "
                   "Les impôts ne sont ajoutés que s'ils sont effectivement payés. Cette "
                   "estimation ne remplace pas l'examen du dossier par le tribunal et ne tient "
                   "compte ni de votre fortune, ni des chances de succès de votre cause.",
        "source_SO": "Basé sur un arrêt de l'Obergericht de Soleure (Zivilkammer, ZKBES-2016-177, "
                   "22 décembre 2016), qui affirme explicitement que le montant de base doit être "
                   "majoré des « 20 % usuels dans le canton de Soleure » et l'applique "
                   "concrètement (CHF 1'200.- + CHF 240.- = CHF 1'440.-). Les impôts sont ajoutés "
                   "au calcul selon ce même arrêt. Cette estimation ne remplace pas l'examen du "
                   "dossier par le tribunal et ne tient compte ni de votre fortune, ni des "
                   "chances de succès de votre cause.",
        "source_EST": "Estimation basée sur la jurisprudence du Tribunal fédéral (arrêt "
                   "8C_470/2016 du 16 décembre 2016, consid. 5.5, citant l'arrêt 8C_377/2016 du "
                   "8 août 2016 et SVR 2010 IV n° 10 p. 31 consid. 8.3), qui retient un supplément "
                   "de 25 % du montant de base comme ordre de grandeur généralement appliqué, "
                   "un chiffre également cité par le Tribunal cantonal vaudois en référence à "
                   "l'ATF 124 I 1. Ce n'est PAS un taux garanti pour votre canton : chaque canton "
                   "et chaque juge peut retenir un pourcentage différent (10 % à 30 % selon les "
                   "cas recensés). Cette estimation ne remplace pas l'examen du dossier par le "
                   "tribunal et ne tient compte ni de votre fortune, ni des chances de succès de "
                   "votre cause.",
    },
    "de": {
        "canton_label": "Kanton des Verfahrens",
        "canton_ge": "Genf",
        "canton_lu": "Luzern",
        "canton_gr": "Graubünden",
        "canton_so": "Solothurn",
        "canton_est": "Anderer Kanton (nationale Schätzung)",
        "heading_GE": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Genf)",
        "heading_LU": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Luzern)",
        "heading_GR": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Graubünden)",
        "heading_SO": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Solothurn)",
        "heading_EST": "Schätzung: Anspruch auf unentgeltliche Rechtspflege (alle anderen Kantone)",
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
        "disclaimer_GR": "Diese Berechnung gilt nur für Verfahren im Kanton Graubünden. Wählen "
                       "Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. "
                       "Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das "
                       "Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer "
                       "Sache.",
        "disclaimer_SO": "Diese Berechnung gilt nur für Verfahren im Kanton Solothurn. Wählen Sie "
                       "oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das "
                       "Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das "
                       "Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer "
                       "Sache.",
        "disclaimer_EST": "Für Ihren Kanton ist uns kein offiziell publizierter, nachprüfbarer "
                       "Zuschlagssatz für die unentgeltliche Rechtspflege bekannt. Diese "
                       "Berechnung verwendet daher eine generische SCHÄTZUNG von 25 %, "
                       "entnommen aus der Rechtsprechung des Bundesgerichts (Urteile 8C_470/2016 "
                       "und 8C_377/2016) und häufig von kantonalen Gerichten zitiert, dies ist "
                       "NICHT der offizielle Satz Ihres Kantons, sondern nur eine Grössenordnung. "
                       "Für eine verlässliche Zahl wenden Sie sich an das Gericht oder die "
                       "Rechtspflegestelle Ihres Kantons.",
        "unsupported_canton_note": "Nur Genf, Luzern, Graubünden und Solothurn verfügen über "
                       "einen offiziell publizierten und nachprüfbaren Zuschlagssatz für Ihren "
                       "genauen Kanton. Für alle anderen Kantone zeigt der Simulator eine "
                       "gesonderte nationale Schätzung an (siehe oben): Sie gibt eine "
                       "Grössenordnung an, keine Garantie.",
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
        "estimate_flag": "Hinweis: Dieses Ergebnis beruht auf einer nationalen Schätzung (25 %), "
                        "nicht auf einem für Ihren Kanton spezifischen Satz. Bitte beim "
                        "zuständigen Gericht nachprüfen.",
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
        "source_GR": "Grundlage: Verfügung des Kantonsgerichts Graubünden vom 26. Januar 2023 "
                  "(ZK2 22 56) betreffend unentgeltliche Rechtspflege, die einen Grundbetrag "
                  "anwendet, der mit Genf identisch ist (CHF 1'200.- für eine alleinstehende "
                  "Person, unter Verweis auf KGer GR KSK 09 39 vom 18.08.2009), erhöht um 20 % "
                  "gemäss ständiger Rechtsprechung (KGer GR ZK1 14 112 vom 05.01.2015; PKG 2003 "
                  "Nr. 13). Steuern werden nur berücksichtigt, wenn sie tatsächlich bezahlt "
                  "werden. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und "
                  "berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
        "source_SO": "Grundlage: Urteil des Obergerichts Solothurn (Zivilkammer, ZKBES-2016-177, "
                  "22. Dezember 2016), das ausdrücklich festhält, der Grundbetrag sei um die "
                  "«im Kanton Solothurn üblichen 20 %» zu erweitern, und dies konkret anwendet "
                  "(CHF 1'200.- + CHF 240.- = CHF 1'440.-). Steuern werden gemäss demselben "
                  "Urteil in die Berechnung einbezogen. Diese Schätzung ersetzt nicht die Prüfung "
                  "durch das Gericht und berücksichtigt weder Ihr Vermögen noch die "
                  "Erfolgsaussichten Ihrer Sache.",
        "source_EST": "Schätzung auf Grundlage der bundesgerichtlichen Rechtsprechung (Urteil "
                  "8C_470/2016 vom 16. Dezember 2016, E. 5.5, unter Hinweis auf Urteil 8C_377/2016 "
                  "vom 8. August 2016 und SVR 2010 IV Nr. 10 S. 31 E. 8.3), wonach ein Zuschlag "
                  "von 25 % des Grundbetrages als allgemein angewandte Grössenordnung gilt, ein "
                  "Wert, der auch vom Waadtländer Kantonsgericht unter Hinweis auf BGE 124 I 1 "
                  "zitiert wird. Dies ist KEIN garantierter Satz für Ihren Kanton: Jeder Kanton "
                  "und jedes Gericht kann einen anderen Prozentsatz anwenden (10 % bis 30 % je "
                  "nach untersuchten Fällen). Diese Schätzung ersetzt nicht die Prüfung durch das "
                  "Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer "
                  "Sache.",
    },
    "it": {
        "canton_label": "Cantone della procedura",
        "canton_ge": "Ginevra",
        "canton_lu": "Lucerna",
        "canton_gr": "Grigioni",
        "canton_so": "Soletta",
        "canton_est": "Altro cantone (stima nazionale)",
        "heading_GE": "Simulatore: diritto al gratuito patrocinio (Cantone di Ginevra)",
        "heading_LU": "Simulatore: diritto al gratuito patrocinio (Cantone di Lucerna)",
        "heading_GR": "Simulatore: diritto al gratuito patrocinio (Cantone dei Grigioni)",
        "heading_SO": "Simulatore: diritto al gratuito patrocinio (Cantone di Soletta)",
        "heading_EST": "Stima: diritto al gratuito patrocinio (tutti gli altri cantoni)",
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
        "disclaimer_GR": "Questo calcolo vale solo per le procedure nel Cantone dei Grigioni. "
                       "Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il "
                       "risultato è una stima indicativa, non una decisione: il tribunale esamina "
                       "anche il vostro patrimonio e le probabilità di successo della causa.",
        "disclaimer_SO": "Questo calcolo vale solo per le procedure nel Cantone di Soletta. "
                       "Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il "
                       "risultato è una stima indicativa, non una decisione: il tribunale esamina "
                       "anche il vostro patrimonio e le probabilità di successo della causa.",
        "disclaimer_EST": "Per il vostro cantone non ci risulta una percentuale di maggiorazione "
                       "pubblicata ufficialmente e verificabile per il gratuito patrocinio. "
                       "Questo calcolo utilizza quindi una STIMA generica del 25%, ripresa dalla "
                       "giurisprudenza del Tribunale federale (sentenze 8C_470/2016 e "
                       "8C_377/2016) e spesso citata dai tribunali cantonali, NON è "
                       "l'aliquota ufficiale del vostro cantone, ma solo un ordine di grandezza. "
                       "Per una cifra affidabile, contattate il tribunale o il servizio di "
                       "assistenza giudiziaria del vostro cantone.",
        "unsupported_canton_note": "Solo Ginevra, Lucerna, i Grigioni e Soletta dispongono di una "
                       "percentuale di maggiorazione pubblicata ufficialmente e verificabile per "
                       "il vostro cantone esatto. Per tutti gli altri cantoni, il simulatore "
                       "mostra una stima nazionale distinta (vedi sopra): fornisce un ordine di "
                       "grandezza, non una garanzia.",
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
        "estimate_flag": "Promemoria: questo risultato si basa su una stima nazionale (25%), non "
                        "su un'aliquota specifica del vostro cantone. Verificate presso il "
                        "tribunale competente.",
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
        "source_GR": "Basato su un'ordinanza del Tribunale cantonale dei Grigioni del 26 gennaio "
                  "2023 (ZK2 22 56), in materia di assistenza giudiziaria gratuita, che applica un "
                  "importo di base identico a Ginevra (CHF 1'200.- per una persona sola, citando "
                  "KGer GR KSK 09 39 del 18.08.2009), maggiorato del 20% secondo giurisprudenza "
                  "costante (KGer GR ZK1 14 112 del 05.01.2015; PKG 2003 Nr. 13). Le imposte sono "
                  "conteggiate solo se effettivamente pagate. Questa stima non sostituisce "
                  "l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di "
                  "successo della causa.",
        "source_SO": "Basato su una sentenza dell'Obergericht di Soletta (Zivilkammer, "
                  "ZKBES-2016-177, 22 dicembre 2016), che afferma esplicitamente che l'importo di "
                  "base va maggiorato del «20% usuale nel Cantone di Soletta» e lo applica "
                  "concretamente (CHF 1'200.- + CHF 240.- = CHF 1'440.-). Le imposte sono incluse "
                  "nel calcolo secondo la stessa sentenza. Questa stima non sostituisce l'esame "
                  "del tribunale e non tiene conto del patrimonio né delle probabilità di "
                  "successo della causa.",
        "source_EST": "Stima basata sulla giurisprudenza del Tribunale federale (sentenza "
                  "8C_470/2016 del 16 dicembre 2016, consid. 5.5, che cita la sentenza 8C_377/2016 "
                  "dell'8 agosto 2016 e SVR 2010 IV n. 10 p. 31 consid. 8.3), secondo cui un "
                  "supplemento del 25% dell'importo di base è l'ordine di grandezza generalmente "
                  "applicato, una cifra citata anche dal Tribunale cantonale vodese in "
                  "riferimento alla DTF 124 I 1. NON è un'aliquota garantita per il vostro "
                  "cantone: ogni cantone e ogni giudice può applicare una percentuale diversa "
                  "(dal 10% al 30% nei casi esaminati). Questa stima non sostituisce l'esame del "
                  "tribunale e non tiene conto del patrimonio né delle probabilità di successo "
                  "della causa.",
    },
    "en": {
        "canton_label": "Canton where the case is handled",
        "canton_ge": "Geneva",
        "canton_lu": "Lucerne",
        "canton_gr": "Graubünden",
        "canton_so": "Solothurn",
        "canton_est": "Other canton (national estimate)",
        "heading_GE": "Legal aid eligibility estimator (Canton of Geneva)",
        "heading_LU": "Legal aid eligibility estimator (Canton of Lucerne)",
        "heading_GR": "Legal aid eligibility estimator (Canton of Graubünden)",
        "heading_SO": "Legal aid eligibility estimator (Canton of Solothurn)",
        "heading_EST": "Legal aid eligibility estimate (all other cantons)",
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
        "disclaimer_GR": "This calculation only applies to proceedings in the Canton of "
                       "Graubünden. Switch canton above if your case is elsewhere. The result is "
                       "an indicative estimate, not a decision: the court also assesses your "
                       "assets and the prospects of success of your case.",
        "disclaimer_SO": "This calculation only applies to proceedings in the Canton of "
                       "Solothurn. Switch canton above if your case is elsewhere. The result is "
                       "an indicative estimate, not a decision: the court also assesses your "
                       "assets and the prospects of success of your case.",
        "disclaimer_EST": "We are not aware of an officially published, verifiable surcharge "
                       "percentage for legal aid in your canton. This calculation therefore uses "
                       "a generic ESTIMATE of 25%, drawn from Federal Tribunal case law (rulings "
                       "8C_470/2016 and 8C_377/2016) and commonly cited by cantonal courts, this "
                       "is NOT your canton's official rate, only a ballpark figure. For a "
                       "reliable figure, contact the court or legal aid office of your canton.",
        "unsupported_canton_note": "Only Geneva, Lucerne, Graubünden and Solothurn have an "
                       "officially published, verifiable surcharge percentage for your exact "
                       "canton. For all other cantons, the simulator shows a separate national "
                       "estimate (see above): it gives a ballpark figure, not a guarantee.",
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
        "estimate_flag": "Reminder: this result relies on a national estimate (25%), not a rate "
                        "specific to your canton. Check with the competent court.",
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
        "source_GR": "Based on: a ruling of the Graubünden Cantonal Court of 26 January 2023 "
                  "(ZK2 22 56) on legal aid, applying a base amount identical to Geneva's (CHF "
                  "1,200 for a single person, citing KGer GR KSK 09 39 of 18.08.2009), increased "
                  "by 20% per settled case law (KGer GR ZK1 14 112 of 05.01.2015; PKG 2003 No. "
                  "13). Taxes are only counted if actually paid. This estimate does not replace "
                  "the court's review and does not account for your assets or the prospects of "
                  "success of your case.",
        "source_SO": "Based on: a ruling of the Solothurn Cantonal High Court (Zivilkammer, "
                  "ZKBES-2016-177, 22 December 2016), which explicitly states that the base "
                  "amount must be increased by \"the 20% customary in the Canton of Solothurn\" "
                  "and applies this concretely (CHF 1,200 + CHF 240 = CHF 1,440). Taxes are "
                  "included in the calculation per the same ruling. This estimate does not "
                  "replace the court's review and does not account for your assets or the "
                  "prospects of success of your case.",
        "source_EST": "Estimate based on Federal Tribunal case law (ruling 8C_470/2016 of 16 "
                  "December 2016, consid. 5.5, citing ruling 8C_377/2016 of 8 August 2016 and "
                  "SVR 2010 IV No. 10 p. 31 consid. 8.3), which treats a 25% surcharge on the "
                  "base amount as the generally applied ballpark figure, a figure also cited by "
                  "the Vaud Cantonal Court with reference to Federal Supreme Court ruling ATF 124 "
                  "I 1. This is NOT a guaranteed rate for your canton: each canton and each judge "
                  "may apply a different percentage (10% to 30% across cases reviewed). This "
                  "estimate does not replace the court's review and does not account for your "
                  "assets or the prospects of success of your case.",
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
        <option value="GR">{s['canton_gr']}</option>
        <option value="SO">{s['canton_so']}</option>
        <option value="EST">{s['canton_est']}</option>
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
