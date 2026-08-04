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

MISE A JOUR DU 04/08/2026 : le simulateur passe de 4 a 18 cantons a taux
confirme, en reutilisant les donnees de l'etude comparative Legatis sur
l'assistance judiciaire (data/aj_study/data.json -- meme corpus de decisions
verifiees individuellement, meme principe de non-fabrication). Nouveaux
cantons : Tessin (0%), Bale-Campagne (15%), Bale-Ville (15%), Zoug (20%),
Nidwald (20%), Uri (20%), Jura (25%), Argovie (25%), Fribourg (25%), Valais
(25%), Schwytz (30%), Berne (30%), Saint-Gall (30%), Appenzell
Rhodes-Interieures (30%). Pour ces 14 cantons, l'inclusion des impots dans le
calcul cantonal n'a pas ete documentee par les sources trouvees (a la
difference de Geneve/Lucerne/Grisons/Soleure, ou ce point avait ete verifie
individuellement) : le champ impots est donc masque par defaut pour eux,
signale explicitement dans le disclaimer de chaque canton.

CORRECTION GENEVE : la majoration passe de 20% a 25%, suite a la recherche
approfondie de l'etude comparative qui a mis en evidence un changement de
pratique de la Chambre penale de recours (20% entre 2020 et 2022, 25% depuis,
mieux motive en droit par l'arret du Tribunal federal 1B_383/2017). L'ancien
taux de 20% reste documente dans l'etude complete pour transparence.

Chaque canton nouvellement ajoute cite sa decision ou source officielle
principale directement dans le simulateur ; le detail complet (toutes les
decisions, tous les liens de verification) reste dans l'etude comparative,
accessible depuis la page dediee /{lang}/etude-assistance-judiciaire/ (et
equivalents par langue).
"""

import json

CANTONS = json.loads(r'''
{
  "GE": {
    "majoration_pct": 25,
    "includes_impots": true,
    "confirmed": true
  },
  "LU": {
    "majoration_pct": 20,
    "includes_impots": false,
    "confirmed": true
  },
  "GR": {
    "majoration_pct": 20,
    "includes_impots": true,
    "confirmed": true
  },
  "SO": {
    "majoration_pct": 20,
    "includes_impots": true,
    "confirmed": true
  },
  "EST": {
    "majoration_pct": 25,
    "includes_impots": true,
    "confirmed": false
  },
  "TI": {
    "majoration_pct": 0,
    "includes_impots": false,
    "confirmed": true
  },
  "BL": {
    "majoration_pct": 15,
    "includes_impots": false,
    "confirmed": true
  },
  "BS": {
    "majoration_pct": 15,
    "includes_impots": false,
    "confirmed": true
  },
  "ZG": {
    "majoration_pct": 20,
    "includes_impots": false,
    "confirmed": true
  },
  "NW": {
    "majoration_pct": 20,
    "includes_impots": false,
    "confirmed": true
  },
  "UR": {
    "majoration_pct": 20,
    "includes_impots": false,
    "confirmed": true
  },
  "JU": {
    "majoration_pct": 25,
    "includes_impots": false,
    "confirmed": true
  },
  "AG": {
    "majoration_pct": 25,
    "includes_impots": false,
    "confirmed": true
  },
  "FR": {
    "majoration_pct": 25,
    "includes_impots": false,
    "confirmed": true
  },
  "VS": {
    "majoration_pct": 25,
    "includes_impots": false,
    "confirmed": true
  },
  "SZ": {
    "majoration_pct": 30,
    "includes_impots": false,
    "confirmed": true
  },
  "BE": {
    "majoration_pct": 30,
    "includes_impots": false,
    "confirmed": true
  },
  "SG": {
    "majoration_pct": 30,
    "includes_impots": false,
    "confirmed": true
  },
  "AI": {
    "majoration_pct": 30,
    "includes_impots": false,
    "confirmed": true
  }
}
''')

CANTON_ORDER = ['GE', 'TI', 'BL', 'BS', 'LU', 'GR', 'SO', 'ZG', 'NW', 'UR', 'JU', 'AG', 'FR', 'VS', 'SZ', 'BE', 'SG', 'AI', 'EST']


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

STRINGS = json.loads(r'''
{
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
    "disclaimer_GE": "Ce calcul ne s'applique qu'aux procédures dans le canton de Genève. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le greffe de l'assistance juridique examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici.",
    "disclaimer_LU": "Ce calcul ne s'applique qu'aux procédures dans le canton de Lucerne, et ne tient pas compte des impôts (non intégrés dans le calcul lucernois d'après la source officielle utilisée). Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici.",
    "disclaimer_GR": "Ce calcul ne s'applique qu'aux procédures dans le canton des Grisons. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici.",
    "disclaimer_SO": "Ce calcul ne s'applique qu'aux procédures dans le canton de Soleure. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici.",
    "disclaimer_EST": "Votre canton ne dispose pas (à notre connaissance) d'un pourcentage de majoration officiellement publié et vérifiable pour l'assistance judiciaire. Ce calcul utilise donc une ESTIMATION générique de 25%, reprise de la jurisprudence du Tribunal fédéral (arrêts 8C_470/2016 et 8C_377/2016) et couramment citée par les tribunaux cantonaux, ce n'est PAS le taux officiel de votre canton, seulement un ordre de grandeur. Pour un chiffre fiable, contactez le tribunal ou le service d'assistance judiciaire de votre canton.",
    "unsupported_canton_note": "18 cantons disposent désormais d'un pourcentage de majoration confirmé par au moins deux décisions de justice indépendantes (ou une directive officielle générale) : Genève, Lucerne, les Grisons, Soleure, le Tessin, Bâle-Campagne, Bâle-Ville, Zoug, Nidwald, Uri, le Jura, Argovie, Fribourg, le Valais, Schwytz, Berne, Saint-Gall et Appenzell Rhodes-Intérieures. Pour tous les autres cantons, le simulateur affiche une estimation nationale distincte (voir ci-dessus) : elle donne un ordre de grandeur, pas une garantie. Détail complet des sources et des décisions citées dans l'étude comparative Legatis sur l'assistance judiciaire.",
    "situation": "Votre situation familiale",
    "opt_seul": "Vous vivez seul·e, sans enfant à charge",
    "opt_mono": "Vous êtes seul·e avec un ou plusieurs enfants à charge (famille monoparentale)",
    "opt_couple": "Vous êtes marié·e, en partenariat enregistré, ou en couple avec des enfants à charge",
    "enf_moins10": "Nombre d'enfants à charge de moins de 10 ans",
    "enf_plus10": "Nombre d'enfants à charge de 10 ans ou plus",
    "loyer": "Loyer mensuel net (hors charges de chauffage), en CHF",
    "lamal": "Prime d'assurance-maladie obligatoire (par mois, en CHF)",
    "autres": "Autres charges reconnues : frais professionnels indispensables, pensions alimentaires versées, etc. (par mois, en CHF)",
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
    "estimate_flag": "Rappel : ce résultat repose sur une estimation nationale (25%), pas sur un taux propre à votre canton. Vérifiez auprès du tribunal compétent.",
    "footer_note": "N'oubliez pas : la fortune et les chances de succès de votre cause sont aussi examinées par le tribunal, indépendamment de ce calcul.",
    "source_GE": "Basé sur les normes d'insaisissabilité 2026 du canton de Genève (NI-2026, rsGE E 3 60.04, en vigueur depuis le 1ᵉʳ janvier 2026) pour les montants de base, et sur la pratique actuelle de la Chambre pénale de recours de la Cour de justice genevoise qui majore ce montant de 25% (arrêt ACPR/552/2025 du 05.05.2025 : « Pour établir les dépenses du requérant, il convient de se fonder sur son minimum vital du droit des poursuites, augmenté de 25% (arrêt du Tribunal fédéral 1B_383/2017 du 23 novembre 2017 consid. 2). »). CAS PARTICULIER, documenté comme une pratique évolutive plutôt qu'un taux fixe unique (à l'instar de la Thurgovie) : 5 décisions indépendantes de la Chambre pénale de recours appliquent 20% entre 2020 et 2022, mais 6 décisions plus récentes (2022-2025), dont la plus récente lue intégralement, appliquent 25% en se fondant sur un arrêt du Tribunal fédéral. Aucune directive ou arrêt de principe formalisant ce changement n'a été identifié : les deux lignées se chevauchent en 2022 sans cutover officiel. Comptabilisé ici sous 25% (la pratique la plus récente et la mieux motivée en droit), mais les deux taux sont documentés pour transparence. Cette estimation ne remplace pas l'examen du dossier par le greffe et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "source_LU": "Basé sur la Weisung du 13 août 2009 de la Commission de surveillance des poursuites et faillites de l'Obergericht lucernois (LGVE 2009 I n° 42, en vigueur depuis le 1ᵉʳ octobre 2009, consultée sur steuerbuch.lu.ch), majorée de 20 % selon la pratique confirmée dans Jozic/Boesch, « Die unentgeltliche Rechtspflege im Zivilprozess », Obergericht du canton de Lucerne, 4ᵉ édition, mai 2012 (citant LGVE 2003 I n° 39). Les impôts ne sont pas comptés dans ce calcul, conformément à cette même source. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "source_GR": "Basé sur une ordonnance du Tribunal cantonal des Grisons du 26 janvier 2023 (ZK2 22 56), rendue en matière d'assistance judiciaire, qui applique un montant de base identique à Genève (CHF 1'200.- pour une personne seule, citant KGer GR KSK 09 39 du 18.08.2009), majoré de 20 % selon une jurisprudence constante (KGer GR ZK1 14 112 du 05.01.2015 ; PKG 2003 Nr. 13). Les impôts ne sont ajoutés que s'ils sont effectivement payés. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "source_SO": "Basé sur un arrêt de l'Obergericht de Soleure (Zivilkammer, ZKBES-2016-177, 22 décembre 2016), qui affirme explicitement que le montant de base doit être majoré des « 20 % usuels dans le canton de Soleure » et l'applique concrètement (CHF 1'200.- + CHF 240.- = CHF 1'440.-). Les impôts sont ajoutés au calcul selon ce même arrêt. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "source_EST": "Estimation basée sur la jurisprudence du Tribunal fédéral (arrêt 8C_470/2016 du 16 décembre 2016, consid. 5.5, citant l'arrêt 8C_377/2016 du 8 août 2016 et SVR 2010 IV n° 10 p. 31 consid. 8.3), qui retient un supplément de 25 % du montant de base comme ordre de grandeur généralement appliqué, un chiffre également cité par le Tribunal cantonal vaudois en référence à l'ATF 124 I 1. Ce n'est PAS un taux garanti pour votre canton : chaque canton et chaque juge peut retenir un pourcentage différent (10 % à 30 % selon les cas recensés). Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_ti": "Tessin",
    "heading_TI": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Tessin)",
    "disclaimer_TI": "Ce calcul ne s'applique qu'aux procédures dans le canton de Tessin. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_TI": "Basé sur : Tribunale d'appello TI (Camera dei ricorsi penali), 60.2010.124, 05.07.2010 : « Calcul du fabbisogno minimo strictement limité au montant de base LEF et aux postes de charges réelles documentées, sans aucun supplément en pourcentage. ». Seul canton suisse où la jurisprudence affirme explicitement l'absence de toute majoration du minimum vital pour l'assistance judiciaire, confirmée par la table officielle du minimo di esistenza du pouvoir judiciaire tessinois qui ne prévoit aucun supplément forfaitaire, contrairement aux autres cantons. Détail complet des 3 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_bl": "Bâle-Campagne",
    "heading_BL": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Bâle-Campagne)",
    "disclaimer_BL": "Ce calcul ne s'applique qu'aux procédures dans le canton de Bâle-Campagne. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_BL": "Basé sur : Kantonsgericht Basel-Landschaft (tribunal des assurances sociales), 725 2015 188, 2015 : « Application du même taux de 15% hors chambre civile, devant le tribunal des assurances sociales. ». 14 décisions indépendantes identifiées au total (2012-2021), le corpus le plus riche de l'étude avec Bâle-Ville. Nuance signalée : une lignée distincte 2013-2015 appliquait 25-50% mais uniquement pour le calcul du remboursement de l'AJ après coup (pas l'octroi initial), lignée abandonnée depuis 2021. Détail complet des 14 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_bs": "Bâle-Ville",
    "heading_BS": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Bâle-Ville)",
    "disclaimer_BS": "Ce calcul ne s'applique qu'aux procédures dans le canton de Bâle-Ville. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_BS": "Basé sur : Appellationsgericht Basel-Stadt, KR.2025.2, 02.10.2025 : « Zuschlag von 15 % [CHF 382.80]. ». 11 décisions indépendantes identifiées (2015-2025), formant une chaîne de précédents ininterrompue sur 10 ans (ZB.2016.39 → ZB.2020.6 → BEZ.2018.40 → BEZ.2018.24 → VD.2018.76 → VD.2022.138 → ZB.2022.11 → KR.2025.2), le corpus le plus dense de toute l'étude. Détail complet des 11 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_zg": "Zoug",
    "heading_ZG": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Zoug)",
    "disclaimer_ZG": "Ce calcul ne s'applique qu'aux procédures dans le canton de Zoug. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_ZG": "Basé sur : Obergericht Zug, BZ 2025 19, 01.07.2025 : « Existenzminimum CHF 3'589.70 (Grundbetrag [plus 20 % Zuschlag]: CHF 1'440.00...). ». 7 décisions indépendantes identifiées (2022-2025), toutes formulées comme pratique constante (\"praxisgemäss\"). Aucune contradiction trouvée. Détail complet des 7 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_nw": "Nidwald",
    "heading_NW": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Nidwald)",
    "disclaimer_NW": "Ce calcul ne s'applique qu'aux procédures dans le canton de Nidwald. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_NW": "Basé sur : Kantonsgericht Nidwalden, formulaire officiel \"Unentgeltliche Rechtspflege\", 20.06.2024 : « Total Grundbeträge (inkl. Zuschlag von 20%) : CHF 1'200 (personne seule), CHF 1'350 (famille monoparentale), CHF 1'700 (couple). ». Formulaire officiel du tribunal cantonal, seule source disponible mais de nature générale (applicable à tous les cas, pas un dossier isolé). Recherche exhaustive (~20 décisions candidates ouvertes en texte intégral) sans trouver de décision de justice individuelle appliquant ce taux, corpus judiciaire publié très mince pour ce petit canton, la directive elle-même ne datant que de 2024. Détail complet des 1 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_ur": "Uri",
    "heading_UR": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Uri)",
    "disclaimer_UR": "Ce calcul ne s'applique qu'aux procédures dans le canton de Uri. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_UR": "Basé sur : Obergericht Uri (Präsidium Zivilrechtliche Abteilung), 2026_OG ZP 26 2, 10.04.2026 : « Zivilprozessualer Zuschlag 20 % CHF 310.00. ». Upgradé de « source unique » à « confirmé » : deuxième décision indépendante trouvée (juge différent, dossier différent, trois ans d'écart). Une piste plus ancienne (1996, Obergerichtspräsidium OGP-Z-3/96) reste non vérifiable en texte intégral (seul le regeste est disponible) et n'est donc pas comptée. Détail complet des 2 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_ju": "Jura",
    "heading_JU": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Jura)",
    "disclaimer_JU": "Ce calcul ne s'applique qu'aux procédures dans le canton de Jura. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_JU": "Basé sur : Tribunal cantonal JU (Cour administrative), ADM 2025 157, 20.01.2026 : « minimum vital de droit des poursuites pour une personne seule majoré de 25 %, citant la Circulaire n° 14 du 30 septembre 2015 du Tribunal cantonal relative à l'octroi de l'assistance judiciaire. ». 10 décisions indépendantes identifiées (2013-2026, Cour civile et Cour administrative), adossées à une directive officielle du Tribunal cantonal (Circulaire n° 14 du 30.09.2015). Deux décisions antérieures à cette circulaire (2013-2014) montrent que la pratique des 25% était déjà constante avant sa formalisation écrite. Aucune contradiction trouvée. Détail complet des 10 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_ag": "Argovie",
    "heading_AG": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Argovie)",
    "disclaimer_AG": "Ce calcul ne s'applique qu'aux procédures dans le canton de Argovie. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_AG": "Basé sur : Zivilgericht Argovie, XBE.2022.47, 23.11.2022 : « 25 % des Grundbetrags (AGVE 2002 Nr. 15 S. 65 ff.). ». 10 décisions indépendantes identifiées (2002-2026), couvrant trois instances (Zivilgericht, Strafgericht, Verwaltungsgericht). Une décision (ZOR.2023.6) qualifie explicitement le taux de « stetige Praxis des Obergerichts » (pratique constante du tribunal cantonal). Aucune contradiction trouvée. Détail complet des 10 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_fr": "Fribourg",
    "heading_FR": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Fribourg)",
    "disclaimer_FR": "Ce calcul ne s'applique qu'aux procédures dans le canton de Fribourg. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_FR": "Basé sur : Tribunal cantonal FR, 502 2022 147, 19.08.2022 : « le minimum vital du droit des poursuites, majoré de 25%, à hauteur de CHF 1'687.50. ». 13 décisions indépendantes identifiées (2013-2025). Trajectoire historique documentée : deux décisions de 2015 (102 2014 195 et 502 2015 252) appliquaient encore 20%, présenté comme la « jurisprudence fribourgeoise constante » de l'époque ; toutes les décisions à partir de 2018 confirment 25%, alignées sur les arrêts fédéraux 4A_432/2016 et 5A_328/2016. Basculement de pratique daté et sourcé plutôt qu'une simple photographie statique. Détail complet des 13 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_vs": "Valais",
    "heading_VS": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Valais)",
    "disclaimer_VS": "Ce calcul ne s'applique qu'aux procédures dans le canton de Valais. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_VS": "Basé sur : Tribunal cantonal VS (Cour civile I), C2 25 37, 12.05.2025 : « il peut ainsi couvrir son minimum vital du droit des poursuites majoré de 25 % (1500 fr.). ». 4 décisions indépendantes identifiées (2022-2025), deux chambres différentes du Tribunal cantonal (civile et pénale) concordantes. Détail complet des 4 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_sz": "Schwytz",
    "heading_SZ": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Schwytz)",
    "disclaimer_SZ": "Ce calcul ne s'applique qu'aux procédures dans le canton de Schwytz. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_SZ": "Basé sur : Gericht SZ, BEK 2021 33, 04.06.2021 : « Zuschlag von 30 Prozent auf dem Grundbetrag von Fr. 360.00. ». Adossé à une directive officielle nommée (Richtlinien der Gerichtspräsidentenkonferenz, 03.11.2003). 6 décisions indépendantes identifiées au total (2019-2022) ; corpus jugé proche de l'épuisement après ~200 décisions passées en revue. Deux anomalies contextuelles signalées (une application discrétionnaire à 20% pour un cas particulier, un rejet de 30% dans un contexte de remise de frais pénaux différent du calcul AJ), aucune ne contredisant le taux dans le cadre de l'octroi initial de l'AJ. Détail complet des 6 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_be": "Berne",
    "heading_BE": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Berne)",
    "disclaimer_BE": "Ce calcul ne s'applique qu'aux procédures dans le canton de Berne. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_BE": "Basé sur : Verwaltungsgericht du canton de Berne, 100.2024.304U, 12.12.2025 : « prozessualer Zwangsbedarf [...] Grundbetrag von Fr. 1'200.--, prozessualer Zuschlag von Fr. 360.-- (soit 30%). ». 12 décisions indépendantes identifiées (2013-2025), couvrant à la fois l'Obergericht/Regionalgericht (civil) et le Verwaltungsgericht (administratif), deux instances différentes appliquant le même taux, ce qui renforce la preuve d'une pratique cantonale constante plutôt qu'un cas isolé. Détail complet des 12 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_sg": "Saint-Gall",
    "heading_SG": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Saint-Gall)",
    "disclaimer_SG": "Ce calcul ne s'applique qu'aux procédures dans le canton de Saint-Gall. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_SG": "Basé sur : Kantonsgericht St. Gallen, VZ.2007.31, 21.08.2007 : « Auch in quantitativer Hinsicht ist ein strengerer Massstab anzulegen als bei der Gewährung der unentgeltlichen Prozessführung, wo ein Zuschlag von 30% zum Grundbetrag berücksichtigt wird. ». Directive officielle du tribunal cantonal (2011), confirmée par une décision de justice qui applique concrètement ce taux (2007, antérieure à la directive elle-même). Corpus judiciaire jugé quasi épuisé au-delà de ces deux sources (la plupart des décisions publiées du Kantonsgericht SG sur l'AJ sont des arrêts de principe qui ne rechiffrent pas le calcul, non contesté en pratique). Détail complet des 2 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause.",
    "canton_ai": "Appenzell Rhodes-Interieures",
    "heading_AI": "Simulateur d'éligibilité à l'assistance judiciaire (canton de Appenzell Rhodes-Interieures)",
    "disclaimer_AI": "Ce calcul ne s'applique qu'aux procédures dans le canton de Appenzell Rhodes-Interieures. Changez de canton ci-dessus si votre procédure se déroule ailleurs. Le résultat est une estimation indicative, pas une décision : le tribunal examine aussi votre fortune et les chances de succès de votre cause, deux conditions non calculées ici. L'inclusion des impôts dans le calcul cantonal n'a pas pu être vérifiée pour ce canton précis à partir des sources trouvées : ils ne sont donc pas comptés ici, ce qui peut légèrement sous-estimer le seuil réel.",
    "source_AI": "Basé sur : Canton d'Appenzell Rhodes-Intérieures (site officiel), page \"Unentgeltliche Rechtspflege\", consultée le 03.08.2026 : « Zur Berechnung des prozessualen Zwangsbedarfs wird der Grundbetrag um 30% erhöht. ». Upgradé de « source unique » à « confirmé » : la décision de justice est corroborée mot pour mot par une déclaration générale de pratique publiée sur le site officiel du canton, qui n'est pas liée à un dossier particulier, ce qui satisfait le critère de confirmation par directive/déclaration officielle générale. Recherche exhaustive (~240 décisions appenzelloises relues au total sur deux passes) sans trouver de deuxième décision de justice, le corpus judiciaire de ce très petit canton étant structurellement limité. Détail complet des 2 décision(s)/source(s) examinées et liens de vérification dans l'étude comparative Legatis. Cette estimation ne remplace pas l'examen du dossier par le tribunal et ne tient compte ni de votre fortune, ni des chances de succès de votre cause."
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
    "disclaimer_GE": "Diese Berechnung gilt nur für Verfahren im Kanton Genf. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Die Geschäftsstelle prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Diese beiden Voraussetzungen werden hier nicht berechnet.",
    "disclaimer_LU": "Diese Berechnung gilt nur für Verfahren im Kanton Luzern und berücksichtigt keine Steuern (gemäss der verwendeten offiziellen Quelle nicht Teil der luzernischen Berechnung). Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache.",
    "disclaimer_GR": "Diese Berechnung gilt nur für Verfahren im Kanton Graubünden. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache.",
    "disclaimer_SO": "Diese Berechnung gilt nur für Verfahren im Kanton Solothurn. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache.",
    "disclaimer_EST": "Für Ihren Kanton ist uns kein offiziell publizierter, nachprüfbarer Zuschlagssatz für die unentgeltliche Rechtspflege bekannt. Diese Berechnung verwendet daher eine generische SCHÄTZUNG von 25 %, entnommen aus der Rechtsprechung des Bundesgerichts (Urteile 8C_470/2016 und 8C_377/2016) und häufig von kantonalen Gerichten zitiert, dies ist NICHT der offizielle Satz Ihres Kantons, sondern nur eine Grössenordnung. Für eine verlässliche Zahl wenden Sie sich an das Gericht oder die Rechtspflegestelle Ihres Kantons.",
    "unsupported_canton_note": "18 Kantone verfügen mittlerweile über einen durch mindestens zwei unabhängige Gerichtsentscheide (oder eine allgemeine amtliche Richtlinie) bestätigten Zuschlagssatz: Genf, Luzern, Graubünden, Solothurn, Tessin, Basel-Landschaft, Basel-Stadt, Zug, Nidwalden, Uri, Jura, Aargau, Freiburg, Wallis, Schwyz, Bern, St. Gallen und Appenzell Innerrhoden. Für alle anderen Kantone zeigt der Simulator eine gesonderte nationale Schätzung an (siehe oben): Sie gibt eine Grössenordnung an, keine Garantie. Vollständige Quellenangaben und zitierte Entscheide in der vergleichenden Legatis-Studie zur unentgeltlichen Rechtspflege.",
    "situation": "Ihre familiäre Situation",
    "opt_seul": "Sie leben allein, ohne unterhaltsberechtigte Kinder",
    "opt_mono": "Sie sind alleinerziehend mit einem oder mehreren unterhaltsberechtigten Kindern",
    "opt_couple": "Sie sind verheiratet, in eingetragener Partnerschaft oder leben als Paar mit unterhaltsberechtigten Kindern",
    "enf_moins10": "Anzahl unterhaltsberechtigter Kinder unter 10 Jahren",
    "enf_plus10": "Anzahl unterhaltsberechtigter Kinder ab 10 Jahren",
    "loyer": "Monatlicher Nettomietzins (ohne Heizkosten), in CHF",
    "lamal": "Obligatorische Krankenkassenprämie (pro Monat, in CHF)",
    "autres": "Weitere anerkannte Auslagen: notwendige Berufsauslagen, geleistete Unterhaltsbeiträge usw. (pro Monat, in CHF)",
    "impots": "Tatsächlich bezahlte monatliche Steuern, inkl. Rückstände (in CHF)",
    "revenu": "Monatliches Nettoeinkommen des Haushalts insgesamt (in CHF)",
    "btn": "Anspruch schätzen",
    "result_eligible_title": "Ihre Situation scheint einen Anspruch auf unentgeltliche Rechtspflege zu begründen",
    "result_not_eligible_title": "Aufgrund dieser Zahlen scheint die Schwelle nicht erreicht",
    "label_min_vital": "Um {pct} % erhöhtes Existenzminimum: {n} CHF",
    "label_seuil": "Gesamtschwelle (Existenzminimum + anerkannte Auslagen): {n} CHF",
    "label_revenu": "Angegebenes monatliches Nettoeinkommen: {n} CHF",
    "label_solde_neg": "Ihr Einkommen liegt {n} CHF unter der Schwelle: das spricht für Sie.",
    "label_solde_pos": "Ihr Einkommen liegt {n} CHF über der Schwelle.",
    "estimate_flag": "Hinweis: Dieses Ergebnis beruht auf einer nationalen Schätzung (25 %), nicht auf einem für Ihren Kanton spezifischen Satz. Bitte beim zuständigen Gericht nachprüfen.",
    "footer_note": "Nicht vergessen: Vermögen und Erfolgsaussichten Ihrer Sache werden vom Gericht zusätzlich geprüft, unabhängig von dieser Berechnung.",
    "source_GE": "Grundlage: die Normes d'insaisissabilité 2026 des Kantons Genf (NI-2026, rsGE E 3 60.04, in Kraft seit 01.01.2026) für die Grundbeträge, sowie die aktuelle Praxis der Strafrechtlichen Beschwerdekammer des Genfer Gerichtshofs, die diesen Betrag um 25% erhöht (Entscheid ACPR/552/2025 vom 05.05.2025: «Pour établir les dépenses du requérant, il convient de se fonder sur son minimum vital du droit des poursuites, augmenté de 25% (arrêt du Tribunal fédéral 1B_383/2017 du 23 novembre 2017 consid. 2).»). SONDERFALL, dokumentiert als sich wandelnde Praxis statt als einheitlicher fester Satz (wie im Fall Thurgau): 5 unabhängige Entscheide der Strafrechtlichen Beschwerdekammer wenden zwischen 2020 und 2022 20% an, doch 6 neuere Entscheide (2022-2025), darunter der jüngste vollständig gelesene, wenden gestützt auf einen Bundesgerichtsentscheid 25% an. Es wurde keine Richtlinie oder Grundsatzentscheidung gefunden, die diesen Wechsel formalisiert: Die beiden Linien überschneiden sich 2022 ohne offiziellen Umstellungszeitpunkt. Hier unter 25% verbucht (die jüngere und rechtlich besser begründete Praxis), doch beide Sätze werden aus Transparenzgründen dokumentiert. Diese Schätzung ersetzt nicht die Prüfung durch die Geschäftsstelle und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "source_LU": "Grundlage: Weisung vom 13. August 2009 der Schuldbetreibungs- und Konkurskommission des Obergerichts Luzern (LGVE 2009 I Nr. 42, in Kraft seit 01.10.2009, eingesehen auf steuerbuch.lu.ch), um 20 % erhöht gemäss der in Jozic/Boesch, «Die unentgeltliche Rechtspflege im Zivilprozess», Obergericht des Kantons Luzern, 4. Auflage, Mai 2012, bestätigten Praxis (unter Hinweis auf LGVE 2003 I Nr. 39). Steuern sind gemäss derselben Quelle nicht in dieser Berechnung enthalten. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "source_GR": "Grundlage: Verfügung des Kantonsgerichts Graubünden vom 26. Januar 2023 (ZK2 22 56) betreffend unentgeltliche Rechtspflege, die einen Grundbetrag anwendet, der mit Genf identisch ist (CHF 1'200.- für eine alleinstehende Person, unter Verweis auf KGer GR KSK 09 39 vom 18.08.2009), erhöht um 20 % gemäss ständiger Rechtsprechung (KGer GR ZK1 14 112 vom 05.01.2015; PKG 2003 Nr. 13). Steuern werden nur berücksichtigt, wenn sie tatsächlich bezahlt werden. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "source_SO": "Grundlage: Urteil des Obergerichts Solothurn (Zivilkammer, ZKBES-2016-177, 22. Dezember 2016), das ausdrücklich festhält, der Grundbetrag sei um die «im Kanton Solothurn üblichen 20 %» zu erweitern, und dies konkret anwendet (CHF 1'200.- + CHF 240.- = CHF 1'440.-). Steuern werden gemäss demselben Urteil in die Berechnung einbezogen. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "source_EST": "Schätzung auf Grundlage der bundesgerichtlichen Rechtsprechung (Urteil 8C_470/2016 vom 16. Dezember 2016, E. 5.5, unter Hinweis auf Urteil 8C_377/2016 vom 8. August 2016 und SVR 2010 IV Nr. 10 S. 31 E. 8.3), wonach ein Zuschlag von 25 % des Grundbetrages als allgemein angewandte Grössenordnung gilt, ein Wert, der auch vom Waadtländer Kantonsgericht unter Hinweis auf BGE 124 I 1 zitiert wird. Dies ist KEIN garantierter Satz für Ihren Kanton: Jeder Kanton und jedes Gericht kann einen anderen Prozentsatz anwenden (10 % bis 30 % je nach untersuchten Fällen). Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_ti": "Tessin",
    "heading_TI": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Tessin)",
    "disclaimer_TI": "Diese Berechnung gilt nur für Verfahren im Kanton Tessin. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_TI": "Grundlage: Tribunale d'appello TI (Camera dei ricorsi penali), 60.2010.124, 05.07.2010: «Calcul du fabbisogno minimo strictement limité au montant de base LEF et aux postes de charges réelles documentées, sans aucun supplément en pourcentage.». Einziger Schweizer Kanton, in dem die Rechtsprechung ausdrücklich bestätigt, dass auf das Existenzminimum bei der unentgeltlichen Rechtspflege keinerlei Zuschlag erhoben wird, was durch die offizielle Tabelle des Tessiner Gerichtswesens zum minimo di esistenza bestätigt wird, die im Gegensatz zu den übrigen Kantonen keinen pauschalen Zuschlag vorsieht. Vollständige Übersicht der 3 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_bl": "Basel-Landschaft",
    "heading_BL": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Basel-Landschaft)",
    "disclaimer_BL": "Diese Berechnung gilt nur für Verfahren im Kanton Basel-Landschaft. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_BL": "Grundlage: Kantonsgericht Basel-Landschaft (tribunal des assurances sociales), 725 2015 188, 2015: «Application du même taux de 15% hors chambre civile, devant le tribunal des assurances sociales.». Insgesamt 14 unabhängige Entscheide identifiziert (2012-2021), zusammen mit Basel-Stadt der umfangreichste Bestand dieser Studie. Wichtige Präzisierung: Eine eigenständige Rechtsprechungslinie von 2013-2015 wandte 25-50% an, allerdings nur bei der nachträglichen Rückforderungsberechnung (nicht bei der ursprünglichen Bewilligung); diese Linie wurde seit 2021 aufgegeben. Vollständige Übersicht der 14 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_bs": "Basel-Stadt",
    "heading_BS": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Basel-Stadt)",
    "disclaimer_BS": "Diese Berechnung gilt nur für Verfahren im Kanton Basel-Stadt. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_BS": "Grundlage: Appellationsgericht Basel-Stadt, KR.2025.2, 02.10.2025: «Zuschlag von 15 % [CHF 382.80].». 11 unabhängige Entscheide identifiziert (2015-2025), die eine über 10 Jahre ununterbrochene Präjudizienkette bilden (ZB.2016.39 → ZB.2020.6 → BEZ.2018.40 → BEZ.2018.24 → VD.2018.76 → VD.2022.138 → ZB.2022.11 → KR.2025.2), der dichteste Bestand der gesamten Studie. Vollständige Übersicht der 11 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_zg": "Zug",
    "heading_ZG": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Zug)",
    "disclaimer_ZG": "Diese Berechnung gilt nur für Verfahren im Kanton Zug. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_ZG": "Grundlage: Obergericht Zug, BZ 2025 19, 01.07.2025: «Existenzminimum CHF 3'589.70 (Grundbetrag [plus 20 % Zuschlag]: CHF 1'440.00...).». 7 unabhängige Entscheide identifiziert (2022-2025), alle als ständige Praxis («praxisgemäss») formuliert. Kein Widerspruch gefunden. Vollständige Übersicht der 7 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_nw": "Nidwalden",
    "heading_NW": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Nidwalden)",
    "disclaimer_NW": "Diese Berechnung gilt nur für Verfahren im Kanton Nidwalden. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_NW": "Grundlage: Kantonsgericht Nidwalden, formulaire officiel \"Unentgeltliche Rechtspflege\", 20.06.2024: «Total Grundbeträge (inkl. Zuschlag von 20%) : CHF 1'200 (personne seule), CHF 1'350 (famille monoparentale), CHF 1'700 (couple).». Offizielles Formular des Kantonsgerichts, einzige verfügbare Quelle, jedoch allgemeiner Natur (auf alle Fälle anwendbar, nicht auf einen Einzelfall bezogen). Erschöpfende Recherche (~20 Kandidatenentscheide vollständig gesichtet) ohne Fund eines Einzelentscheids, der diesen Satz anwendet; sehr dünner veröffentlichter Rechtsprechungsbestand für diesen kleinen Kanton, die Weisung selbst stammt erst aus dem Jahr 2024. Vollständige Übersicht der 1 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_ur": "Uri",
    "heading_UR": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Uri)",
    "disclaimer_UR": "Diese Berechnung gilt nur für Verfahren im Kanton Uri. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_UR": "Grundlage: Obergericht Uri (Präsidium Zivilrechtliche Abteilung), 2026_OG ZP 26 2, 10.04.2026: «Zivilprozessualer Zuschlag 20 % CHF 310.00.». Von «Einzelquelle» auf «bestätigt» hochgestuft: zweiter unabhängiger Entscheid gefunden (anderer Richter, anderes Dossier, drei Jahre Abstand). Ein älterer Hinweis (1996, Obergerichtspräsidium OGP-Z-3/96) bleibt im Volltext nicht überprüfbar (nur das Regest ist verfügbar) und wird daher nicht mitgezählt. Vollständige Übersicht der 2 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_ju": "Jura",
    "heading_JU": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Jura)",
    "disclaimer_JU": "Diese Berechnung gilt nur für Verfahren im Kanton Jura. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_JU": "Grundlage: Tribunal cantonal JU (Cour administrative), ADM 2025 157, 20.01.2026: «minimum vital de droit des poursuites pour une personne seule majoré de 25 %, citant la Circulaire n° 14 du 30 septembre 2015 du Tribunal cantonal relative à l'octroi de l'assistance judiciaire.». 10 unabhängige Entscheide identifiziert (2013-2026, Zivilgericht und Verwaltungsgericht), gestützt auf eine offizielle Weisung des Kantonsgerichts (Rundschreiben Nr. 14 vom 30.09.2015). Zwei Entscheide vor diesem Rundschreiben (2013-2014) zeigen, dass die Praxis der 25% bereits vor ihrer schriftlichen Formalisierung konstant war. Kein Widerspruch gefunden. Vollständige Übersicht der 10 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_ag": "Aargau",
    "heading_AG": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Aargau)",
    "disclaimer_AG": "Diese Berechnung gilt nur für Verfahren im Kanton Aargau. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_AG": "Grundlage: Zivilgericht Argovie, XBE.2022.47, 23.11.2022: «25 % des Grundbetrags (AGVE 2002 Nr. 15 S. 65 ff.).». 10 unabhängige Entscheide identifiziert (2002-2026), die drei Instanzen abdecken (Zivilgericht, Strafgericht, Verwaltungsgericht). Ein Entscheid (ZOR.2023.6) bezeichnet den Satz ausdrücklich als «stetige Praxis des Obergerichts». Kein Widerspruch gefunden. Vollständige Übersicht der 10 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_fr": "Freiburg",
    "heading_FR": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Freiburg)",
    "disclaimer_FR": "Diese Berechnung gilt nur für Verfahren im Kanton Freiburg. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_FR": "Grundlage: Tribunal cantonal FR, 502 2022 147, 19.08.2022: «le minimum vital du droit des poursuites, majoré de 25%, à hauteur de CHF 1'687.50.». 13 unabhängige Entscheide identifiziert (2013-2025). Dokumentierter historischer Verlauf: Zwei Entscheide von 2015 (102 2014 195 und 502 2015 252) wandten damals noch 20% an, dargestellt als die zu jener Zeit «ständige freiburgische Rechtsprechung»; alle Entscheide ab 2018 bestätigen 25%, ausgerichtet an den Bundesgerichtsurteilen 4A_432/2016 und 5A_328/2016. Ein datierter und belegter Praxiswechsel statt einer blossen Momentaufnahme. Vollständige Übersicht der 13 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_vs": "Wallis",
    "heading_VS": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Wallis)",
    "disclaimer_VS": "Diese Berechnung gilt nur für Verfahren im Kanton Wallis. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_VS": "Grundlage: Tribunal cantonal VS (Cour civile I), C2 25 37, 12.05.2025: «il peut ainsi couvrir son minimum vital du droit des poursuites majoré de 25 % (1500 fr.).». 4 unabhängige Entscheide identifiziert (2022-2025), zwei verschiedene Kammern des Kantonsgerichts (Zivil- und Strafkammer) übereinstimmend. Vollständige Übersicht der 4 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_sz": "Schwyz",
    "heading_SZ": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Schwyz)",
    "disclaimer_SZ": "Diese Berechnung gilt nur für Verfahren im Kanton Schwyz. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_SZ": "Grundlage: Gericht SZ, BEK 2021 33, 04.06.2021: «Zuschlag von 30 Prozent auf dem Grundbetrag von Fr. 360.00.». Gestützt auf eine namentlich bekannte offizielle Richtlinie (Richtlinien der Gerichtspräsidentenkonferenz vom 03.11.2003). Insgesamt 6 unabhängige Entscheide identifiziert (2019-2022); der Bestand gilt nach Durchsicht von rund 200 Entscheiden als nahezu ausgeschöpft. Zwei kontextuelle Abweichungen vermerkt (eine Ermessensanwendung von 20% in einem Einzelfall, eine Ablehnung von 30% im Kontext eines vom AJ-Berechnungsverfahren abweichenden Erlasses von Strafkosten), keine davon widerspricht dem Satz im Rahmen der ursprünglichen Bewilligung der unentgeltlichen Rechtspflege. Vollständige Übersicht der 6 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_be": "Bern",
    "heading_BE": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Bern)",
    "disclaimer_BE": "Diese Berechnung gilt nur für Verfahren im Kanton Bern. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_BE": "Grundlage: Verwaltungsgericht du canton de Berne, 100.2024.304U, 12.12.2025: «prozessualer Zwangsbedarf [...] Grundbetrag von Fr. 1'200.--, prozessualer Zuschlag von Fr. 360.-- (soit 30%).». 12 unabhängige Entscheide identifiziert (2013-2025), die sowohl das Obergericht/Regionalgericht (Zivilrecht) als auch das Verwaltungsgericht (Verwaltungsrecht) abdecken, zwei unterschiedliche Instanzen, die denselben Satz anwenden, was den Nachweis einer konstanten kantonalen Praxis statt eines Einzelfalls verstärkt. Vollständige Übersicht der 12 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_sg": "St. Gallen",
    "heading_SG": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton St. Gallen)",
    "disclaimer_SG": "Diese Berechnung gilt nur für Verfahren im Kanton St. Gallen. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_SG": "Grundlage: Kantonsgericht St. Gallen, VZ.2007.31, 21.08.2007: «Auch in quantitativer Hinsicht ist ein strengerer Massstab anzulegen als bei der Gewährung der unentgeltlichen Prozessführung, wo ein Zuschlag von 30% zum Grundbetrag berücksichtigt wird.». Offizielle Weisung des Kantonsgerichts (2011), bestätigt durch einen Gerichtsentscheid, der diesen Satz konkret anwendet (2007, älter als die Weisung selbst). Der Bestand an Rechtsprechung gilt über diese beiden Quellen hinaus als nahezu ausgeschöpft (die meisten publizierten Entscheide des Kantonsgerichts SG zur unentgeltlichen Rechtspflege sind Grundsatzentscheide, die die Berechnung nicht neu beziffern, da sie in der Praxis unbestritten ist). Vollständige Übersicht der 2 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache.",
    "canton_ai": "Appenzell Innerrhoden",
    "heading_AI": "Simulator: Anspruch auf unentgeltliche Rechtspflege (Kanton Appenzell Innerrhoden)",
    "disclaimer_AI": "Diese Berechnung gilt nur für Verfahren im Kanton Appenzell Innerrhoden. Wählen Sie oben einen anderen Kanton, falls Ihr Verfahren anderswo stattfindet. Das Ergebnis ist eine unverbindliche Schätzung, keine Entscheidung: Das Gericht prüft zusätzlich Ihr Vermögen und die Erfolgsaussichten Ihrer Sache. Ob Steuern in die kantonale Berechnung einbezogen werden, konnte anhand der gefundenen Quellen für diesen Kanton nicht überprüft werden; sie werden hier daher nicht mitgezählt, was die tatsächliche Schwelle leicht unterschätzen kann.",
    "source_AI": "Grundlage: Canton d'Appenzell Rhodes-Intérieures (site officiel), page \"Unentgeltliche Rechtspflege\", consultée le 03.08.2026: «Zur Berechnung des prozessualen Zwangsbedarfs wird der Grundbetrag um 30% erhöht.». Von «Einzelquelle» auf «bestätigt» hochgestuft: Der Gerichtsentscheid wird wortgleich durch eine allgemeine Praxiserklärung auf der offiziellen Website des Kantons bestätigt, die nicht an einen bestimmten Einzelfall gebunden ist, was das Bestätigungskriterium einer Weisung/allgemeinen offiziellen Erklärung erfüllt. Erschöpfende Recherche (insgesamt rund 240 gesichtete Appenzeller Entscheide in zwei Durchgängen) ohne Fund eines zweiten Gerichtsentscheids; der Rechtsprechungsbestand dieses sehr kleinen Kantons ist strukturell begrenzt. Vollständige Übersicht der 2 untersuchten Entscheide/Quellen mit Verifizierungslinks in der vergleichenden Legatis-Studie. Diese Schätzung ersetzt nicht die Prüfung durch das Gericht und berücksichtigt weder Ihr Vermögen noch die Erfolgsaussichten Ihrer Sache."
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
    "disclaimer_GE": "Questo calcolo vale solo per le procedure nel Cantone di Ginevra. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: la cancelleria esamina anche il vostro patrimonio e le probabilità di successo della causa, due condizioni non calcolate qui.",
    "disclaimer_LU": "Questo calcolo vale solo per le procedure nel Cantone di Lucerna e non tiene conto delle imposte (non incluse nel calcolo lucernese secondo la fonte ufficiale utilizzata). Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa.",
    "disclaimer_GR": "Questo calcolo vale solo per le procedure nel Cantone dei Grigioni. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa.",
    "disclaimer_SO": "Questo calcolo vale solo per le procedure nel Cantone di Soletta. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa.",
    "disclaimer_EST": "Per il vostro cantone non ci risulta una percentuale di maggiorazione pubblicata ufficialmente e verificabile per il gratuito patrocinio. Questo calcolo utilizza quindi una STIMA generica del 25%, ripresa dalla giurisprudenza del Tribunale federale (sentenze 8C_470/2016 e 8C_377/2016) e spesso citata dai tribunali cantonali, NON è l'aliquota ufficiale del vostro cantone, ma solo un ordine di grandezza. Per una cifra affidabile, contattate il tribunale o il servizio di assistenza giudiziaria del vostro cantone.",
    "unsupported_canton_note": "18 Cantoni dispongono ormai di una percentuale di maggiorazione confermata da almeno due decisioni giudiziarie indipendenti (o una direttiva ufficiale generale): Ginevra, Lucerna, i Grigioni, Soletta, il Ticino, Basilea Campagna, Basilea Città, Zugo, Nidvaldo, Uri, il Giura, l'Argovia, Friburgo, il Vallese, Svitto, Berna, San Gallo e Appenzello Interno. Per tutti gli altri Cantoni, il simulatore mostra una stima nazionale distinta (vedi sopra): fornisce un ordine di grandezza, non una garanzia. Dettaglio completo delle fonti e delle decisioni citate nello studio comparativo Legatis sul gratuito patrocinio.",
    "situation": "La vostra situazione familiare",
    "opt_seul": "Vivete soli, senza figli a carico",
    "opt_mono": "Siete soli con uno o più figli a carico (famiglia monoparentale)",
    "opt_couple": "Siete coniugati, in unione domestica registrata, o in coppia con figli a carico",
    "enf_moins10": "Numero di figli a carico di età inferiore a 10 anni",
    "enf_plus10": "Numero di figli a carico di 10 anni o più",
    "loyer": "Pigione mensile netta (senza spese di riscaldamento), in CHF",
    "lamal": "Premio dell'assicurazione malattia obbligatoria (al mese, in CHF)",
    "autres": "Altri oneri riconosciuti: spese professionali indispensabili, contributi di mantenimento versati, ecc. (al mese, in CHF)",
    "impots": "Imposte mensili effettivamente pagate, inclusi arretrati (in CHF)",
    "revenu": "Reddito netto mensile totale del nucleo familiare (in CHF)",
    "btn": "Stima la mia idoneità",
    "result_eligible_title": "La vostra situazione sembra dare diritto al gratuito patrocinio",
    "result_not_eligible_title": "In base a queste cifre, la soglia non sembra raggiunta",
    "label_min_vital": "Minimo vitale maggiorato del {pct}%: {n} CHF",
    "label_seuil": "Soglia totale (minimo vitale + oneri riconosciuti): {n} CHF",
    "label_revenu": "Reddito netto mensile dichiarato: {n} CHF",
    "label_solde_neg": "Il vostro reddito è inferiore alla soglia di {n} CHF: ciò gioca a vostro favore.",
    "label_solde_pos": "Il vostro reddito supera la soglia di {n} CHF.",
    "estimate_flag": "Promemoria: questo risultato si basa su una stima nazionale (25%), non su un'aliquota specifica del vostro cantone. Verificate presso il tribunale competente.",
    "footer_note": "Da non dimenticare: patrimonio e probabilità di successo della causa sono esaminati a parte dal tribunale, indipendentemente da questo calcolo.",
    "source_GE": "Basato su: le normes d'insaisissabilité 2026 del Cantone di Ginevra (NI-2026, rsGE E 3 60.04, in vigore dal 01.01.2026) per gli importi di base, e sulla prassi attuale della Camera penale dei ricorsi della Corte di giustizia ginevrina, che maggiora questo importo del 25% (sentenza ACPR/552/2025 del 05.05.2025: «Pour établir les dépenses du requérant, il convient de se fonder sur son minimum vital du droit des poursuites, augmenté de 25% (arrêt du Tribunal fédéral 1B_383/2017 du 23 novembre 2017 consid. 2).»). CASO PARTICOLARE, documentato come prassi evolutiva piuttosto che come tasso fisso unico (analogamente a Turgovia): 5 decisioni indipendenti della Camera penale dei ricorsi applicano il 20% tra il 2020 e il 2022, ma 6 decisioni più recenti (2022-2025), tra cui l'ultima letta integralmente, applicano il 25% basandosi su una sentenza del Tribunale federale. Non è stata individuata alcuna direttiva o sentenza di principio che formalizzi questo cambiamento: i due filoni si sovrappongono nel 2022 senza un passaggio ufficiale. Qui contabilizzato al 25% (la prassi più recente e meglio motivata in diritto), ma entrambi i tassi sono documentati per trasparenza. Questa stima non sostituisce l'esame della cancelleria e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "source_LU": "Basato su: Weisung del 13 agosto 2009 della Commissione di vigilanza sulle esecuzioni e i fallimenti dell'Obergericht lucernese (LGVE 2009 I n. 42, in vigore dal 01.10.2009, consultata su steuerbuch.lu.ch), maggiorata del 20% secondo la prassi confermata in Jozic/Boesch, «Die unentgeltliche Rechtspflege im Zivilprozess», Obergericht del Cantone di Lucerna, 4a edizione, maggio 2012 (che cita LGVE 2003 I n. 39). Le imposte non sono conteggiate in questo calcolo, in base alla stessa fonte. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "source_GR": "Basato su un'ordinanza del Tribunale cantonale dei Grigioni del 26 gennaio 2023 (ZK2 22 56), in materia di assistenza giudiziaria gratuita, che applica un importo di base identico a Ginevra (CHF 1'200.- per una persona sola, citando KGer GR KSK 09 39 del 18.08.2009), maggiorato del 20% secondo giurisprudenza costante (KGer GR ZK1 14 112 del 05.01.2015; PKG 2003 Nr. 13). Le imposte sono conteggiate solo se effettivamente pagate. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "source_SO": "Basato su una sentenza dell'Obergericht di Soletta (Zivilkammer, ZKBES-2016-177, 22 dicembre 2016), che afferma esplicitamente che l'importo di base va maggiorato del «20% usuale nel Cantone di Soletta» e lo applica concretamente (CHF 1'200.- + CHF 240.- = CHF 1'440.-). Le imposte sono incluse nel calcolo secondo la stessa sentenza. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "source_EST": "Stima basata sulla giurisprudenza del Tribunale federale (sentenza 8C_470/2016 del 16 dicembre 2016, consid. 5.5, che cita la sentenza 8C_377/2016 dell'8 agosto 2016 e SVR 2010 IV n. 10 p. 31 consid. 8.3), secondo cui un supplemento del 25% dell'importo di base è l'ordine di grandezza generalmente applicato, una cifra citata anche dal Tribunale cantonale vodese in riferimento alla DTF 124 I 1. NON è un'aliquota garantita per il vostro cantone: ogni cantone e ogni giudice può applicare una percentuale diversa (dal 10% al 30% nei casi esaminati). Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_ti": "Ticino",
    "heading_TI": "Simulatore: diritto al gratuito patrocinio (Cantone Ticino)",
    "disclaimer_TI": "Questo calcolo vale solo per le procedure nel Cantone Ticino. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_TI": "Basato su: Tribunale d'appello TI (Camera dei ricorsi penali), 60.2010.124, 05.07.2010: «Calcul du fabbisogno minimo strictement limité au montant de base LEF et aux postes de charges réelles documentées, sans aucun supplément en pourcentage.». Unico Cantone svizzero in cui la giurisprudenza afferma esplicitamente l'assenza di qualsiasi maggiorazione del minimo vitale per il gratuito patrocinio, confermata dalla tabella ufficiale del minimo di esistenza del potere giudiziario ticinese, che non prevede alcun supplemento forfettario, a differenza degli altri Cantoni. Elenco completo delle 3 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_bl": "Basilea Campagna",
    "heading_BL": "Simulatore: diritto al gratuito patrocinio (Cantone Basilea Campagna)",
    "disclaimer_BL": "Questo calcolo vale solo per le procedure nel Cantone Basilea Campagna. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_BL": "Basato su: Kantonsgericht Basel-Landschaft (tribunal des assurances sociales), 725 2015 188, 2015: «Application du même taux de 15% hors chambre civile, devant le tribunal des assurances sociales.». In totale 14 decisioni indipendenti individuate (2012-2021), il corpus più ricco dello studio insieme a Basilea Città. Precisazione importante: un filone distinto del periodo 2013-2015 applicava il 25-50%, ma unicamente per il calcolo del rimborso successivo del gratuito patrocinio (non per la concessione iniziale); filone abbandonato dal 2021. Elenco completo delle 14 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_bs": "Basilea Città",
    "heading_BS": "Simulatore: diritto al gratuito patrocinio (Cantone Basilea Città)",
    "disclaimer_BS": "Questo calcolo vale solo per le procedure nel Cantone Basilea Città. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_BS": "Basato su: Appellationsgericht Basel-Stadt, KR.2025.2, 02.10.2025: «Zuschlag von 15 % [CHF 382.80].». 11 decisioni indipendenti individuate (2015-2025), che formano una catena di precedenti ininterrotta su 10 anni (ZB.2016.39 → ZB.2020.6 → BEZ.2018.40 → BEZ.2018.24 → VD.2018.76 → VD.2022.138 → ZB.2022.11 → KR.2025.2), il corpus più denso dell'intero studio. Elenco completo delle 11 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_zg": "Zugo",
    "heading_ZG": "Simulatore: diritto al gratuito patrocinio (Cantone Zugo)",
    "disclaimer_ZG": "Questo calcolo vale solo per le procedure nel Cantone Zugo. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_ZG": "Basato su: Obergericht Zug, BZ 2025 19, 01.07.2025: «Existenzminimum CHF 3'589.70 (Grundbetrag [plus 20 % Zuschlag]: CHF 1'440.00...).». 7 decisioni indipendenti individuate (2022-2025), tutte formulate come prassi costante («praxisgemäss»). Nessuna contraddizione riscontrata. Elenco completo delle 7 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_nw": "Nidvaldo",
    "heading_NW": "Simulatore: diritto al gratuito patrocinio (Cantone Nidvaldo)",
    "disclaimer_NW": "Questo calcolo vale solo per le procedure nel Cantone Nidvaldo. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_NW": "Basato su: Kantonsgericht Nidwalden, formulaire officiel \"Unentgeltliche Rechtspflege\", 20.06.2024: «Total Grundbeträge (inkl. Zuschlag von 20%) : CHF 1'200 (personne seule), CHF 1'350 (famille monoparentale), CHF 1'700 (couple).». Modulo ufficiale del tribunale cantonale, unica fonte disponibile ma di natura generale (applicabile a tutti i casi, non a un fascicolo isolato). Ricerca esaustiva (circa 20 decisioni candidate esaminate in testo integrale) senza trovare una decisione giudiziaria individuale che applichi questo tasso, corpus giurisprudenziale pubblicato molto esiguo per questo piccolo Cantone, la direttiva stessa risale solo al 2024. Elenco completo delle 1 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_ur": "Uri",
    "heading_UR": "Simulatore: diritto al gratuito patrocinio (Cantone Uri)",
    "disclaimer_UR": "Questo calcolo vale solo per le procedure nel Cantone Uri. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_UR": "Basato su: Obergericht Uri (Präsidium Zivilrechtliche Abteilung), 2026_OG ZP 26 2, 10.04.2026: «Zivilprozessualer Zuschlag 20 % CHF 310.00.». Promosso da «fonte unica» a «confermato»: trovata una seconda decisione indipendente (giudice diverso, fascicolo diverso, a tre anni di distanza). Una traccia più antica (1996, Obergerichtspräsidium OGP-Z-3/96) resta non verificabile in testo integrale (è disponibile solo il regesto) e non viene pertanto conteggiata. Elenco completo delle 2 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_ju": "Giura",
    "heading_JU": "Simulatore: diritto al gratuito patrocinio (Cantone Giura)",
    "disclaimer_JU": "Questo calcolo vale solo per le procedure nel Cantone Giura. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_JU": "Basato su: Tribunal cantonal JU (Cour administrative), ADM 2025 157, 20.01.2026: «minimum vital de droit des poursuites pour une personne seule majoré de 25 %, citant la Circulaire n° 14 du 30 septembre 2015 du Tribunal cantonal relative à l'octroi de l'assistance judiciaire.». 10 decisioni indipendenti individuate (2013-2026, Corte civile e Corte amministrativa), sostenute da una direttiva ufficiale del Tribunale cantonale (Circolare n. 14 del 30.09.2015). Due decisioni anteriori a questa circolare (2013-2014) mostrano che la prassi del 25% era già costante prima della sua formalizzazione scritta. Nessuna contraddizione riscontrata. Elenco completo delle 10 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_ag": "Argovia",
    "heading_AG": "Simulatore: diritto al gratuito patrocinio (Cantone Argovia)",
    "disclaimer_AG": "Questo calcolo vale solo per le procedure nel Cantone Argovia. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_AG": "Basato su: Zivilgericht Argovie, XBE.2022.47, 23.11.2022: «25 % des Grundbetrags (AGVE 2002 Nr. 15 S. 65 ff.).». 10 decisioni indipendenti individuate (2002-2026), che coprono tre istanze (Tribunale civile, Tribunale penale, Tribunale amministrativo). Una decisione (ZOR.2023.6) qualifica esplicitamente il tasso come «stetige Praxis des Obergerichts» (prassi costante del tribunale cantonale). Nessuna contraddizione riscontrata. Elenco completo delle 10 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_fr": "Friburgo",
    "heading_FR": "Simulatore: diritto al gratuito patrocinio (Cantone Friburgo)",
    "disclaimer_FR": "Questo calcolo vale solo per le procedure nel Cantone Friburgo. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_FR": "Basato su: Tribunal cantonal FR, 502 2022 147, 19.08.2022: «le minimum vital du droit des poursuites, majoré de 25%, à hauteur de CHF 1'687.50.». 13 decisioni indipendenti individuate (2013-2025). Traiettoria storica documentata: due decisioni del 2015 (102 2014 195 e 502 2015 252) applicavano ancora il 20%, presentato come la «giurisprudenza friburghese costante» dell'epoca; tutte le decisioni a partire dal 2018 confermano il 25%, allineate alle sentenze federali 4A_432/2016 e 5A_328/2016. Cambiamento di prassi datato e documentato, non una semplice fotografia statica. Elenco completo delle 13 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_vs": "Vallese",
    "heading_VS": "Simulatore: diritto al gratuito patrocinio (Cantone Vallese)",
    "disclaimer_VS": "Questo calcolo vale solo per le procedure nel Cantone Vallese. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_VS": "Basato su: Tribunal cantonal VS (Cour civile I), C2 25 37, 12.05.2025: «il peut ainsi couvrir son minimum vital du droit des poursuites majoré de 25 % (1500 fr.).». 4 decisioni indipendenti individuate (2022-2025), due diverse camere del Tribunale cantonale (civile e penale) concordanti. Elenco completo delle 4 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_sz": "Svitto",
    "heading_SZ": "Simulatore: diritto al gratuito patrocinio (Cantone Svitto)",
    "disclaimer_SZ": "Questo calcolo vale solo per le procedure nel Cantone Svitto. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_SZ": "Basato su: Gericht SZ, BEK 2021 33, 04.06.2021: «Zuschlag von 30 Prozent auf dem Grundbetrag von Fr. 360.00.». Sostenuto da una direttiva ufficiale nominata (Richtlinien der Gerichtspräsidentenkonferenz, 03.11.2003). In totale 6 decisioni indipendenti individuate (2019-2022); corpus ritenuto prossimo all'esaurimento dopo la revisione di circa 200 decisioni. Segnalate due anomalie contestuali (un'applicazione discrezionale al 20% per un caso particolare, un rigetto del 30% in un contesto di condono delle spese penali diverso dal calcolo del gratuito patrocinio), nessuna delle quali contraddice il tasso nell'ambito della concessione iniziale del gratuito patrocinio. Elenco completo delle 6 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_be": "Berna",
    "heading_BE": "Simulatore: diritto al gratuito patrocinio (Cantone Berna)",
    "disclaimer_BE": "Questo calcolo vale solo per le procedure nel Cantone Berna. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_BE": "Basato su: Verwaltungsgericht du canton de Berne, 100.2024.304U, 12.12.2025: «prozessualer Zwangsbedarf [...] Grundbetrag von Fr. 1'200.--, prozessualer Zuschlag von Fr. 360.-- (soit 30%).». 12 decisioni indipendenti individuate (2013-2025), che coprono sia l'Obergericht/Regionalgericht (civile) sia il Verwaltungsgericht (amministrativo), due istanze diverse che applicano lo stesso tasso, il che rafforza la prova di una prassi cantonale costante piuttosto che di un caso isolato. Elenco completo delle 12 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_sg": "San Gallo",
    "heading_SG": "Simulatore: diritto al gratuito patrocinio (Cantone San Gallo)",
    "disclaimer_SG": "Questo calcolo vale solo per le procedure nel Cantone San Gallo. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_SG": "Basato su: Kantonsgericht St. Gallen, VZ.2007.31, 21.08.2007: «Auch in quantitativer Hinsicht ist ein strengerer Massstab anzulegen als bei der Gewährung der unentgeltlichen Prozessführung, wo ein Zuschlag von 30% zum Grundbetrag berücksichtigt wird.». Direttiva ufficiale del tribunale cantonale (2011), confermata da una decisione giudiziaria che applica concretamente questo tasso (2007, anteriore alla direttiva stessa). Il corpus giurisprudenziale è ritenuto pressoché esaurito oltre queste due fonti (la maggior parte delle decisioni pubblicate del Kantonsgericht SG sul gratuito patrocinio sono sentenze di principio che non ricalcolano l'importo, non contestato nella prassi). Elenco completo delle 2 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa.",
    "canton_ai": "Appenzello Interno",
    "heading_AI": "Simulatore: diritto al gratuito patrocinio (Cantone Appenzello Interno)",
    "disclaimer_AI": "Questo calcolo vale solo per le procedure nel Cantone Appenzello Interno. Cambiate cantone qui sopra se la vostra procedura si svolge altrove. Il risultato è una stima indicativa, non una decisione: il tribunale esamina anche il vostro patrimonio e le probabilità di successo della causa. Non è stato possibile verificare, sulla base delle fonti reperite, se le imposte siano incluse nel calcolo cantonale per questo Cantone specifico; non vengono quindi conteggiate qui, il che può sottostimare leggermente la soglia reale.",
    "source_AI": "Basato su: Canton d'Appenzell Rhodes-Intérieures (site officiel), page \"Unentgeltliche Rechtspflege\", consultée le 03.08.2026: «Zur Berechnung des prozessualen Zwangsbedarfs wird der Grundbetrag um 30% erhöht.». Promosso da «fonte unica» a «confermato»: la decisione giudiziaria è corroborata parola per parola da una dichiarazione generale di prassi pubblicata sul sito ufficiale del Cantone, non legata a un fascicolo particolare, il che soddisfa il criterio di conferma tramite direttiva/dichiarazione ufficiale generale. Ricerca esaustiva (circa 240 decisioni appenzellesi riesaminate in totale su due passaggi) senza trovare una seconda decisione giudiziaria, il corpus giurisprudenziale di questo piccolissimo Cantone essendo strutturalmente limitato. Elenco completo delle 2 decisioni/fonti esaminate e link di verifica nello studio comparativo Legatis. Questa stima non sostituisce l'esame del tribunale e non tiene conto del patrimonio né delle probabilità di successo della causa."
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
    "disclaimer_GE": "This calculation only applies to proceedings in the Canton of Geneva. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the legal aid registry also assesses your assets and the prospects of success of your case, two conditions not calculated here.",
    "disclaimer_LU": "This calculation only applies to proceedings in the Canton of Lucerne and does not account for taxes (not part of the Lucerne calculation according to the official source used). Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case.",
    "disclaimer_GR": "This calculation only applies to proceedings in the Canton of Graubünden. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case.",
    "disclaimer_SO": "This calculation only applies to proceedings in the Canton of Solothurn. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case.",
    "disclaimer_EST": "We are not aware of an officially published, verifiable surcharge percentage for legal aid in your canton. This calculation therefore uses a generic ESTIMATE of 25%, drawn from Federal Tribunal case law (rulings 8C_470/2016 and 8C_377/2016) and commonly cited by cantonal courts, this is NOT your canton's official rate, only a ballpark figure. For a reliable figure, contact the court or legal aid office of your canton.",
    "unsupported_canton_note": "18 cantons now have a surcharge percentage confirmed by at least two independent court decisions (or a general official directive): Geneva, Lucerne, Graubünden, Solothurn, Ticino, Basel-Country, Basel-City, Zug, Nidwalden, Uri, Jura, Aargau, Fribourg, Valais, Schwyz, Bern, St. Gallen, and Appenzell Innerrhoden. For all other cantons, the simulator shows a separate national estimate (see above): it gives a ballpark figure, not a guarantee. Full source detail and cited decisions are available in the Legatis comparative study on legal aid.",
    "situation": "Your family situation",
    "opt_seul": "You live alone, with no dependent children",
    "opt_mono": "You are a single parent with one or more dependent children",
    "opt_couple": "You are married, in a registered partnership, or a couple with dependent children",
    "enf_moins10": "Number of dependent children under 10",
    "enf_plus10": "Number of dependent children 10 or older",
    "loyer": "Net monthly rent (excluding heating charges), in CHF",
    "lamal": "Mandatory health insurance premium (per month, in CHF)",
    "autres": "Other recognised expenses: necessary work-related costs, maintenance payments made, etc. (per month, in CHF)",
    "impots": "Monthly taxes actually paid, including arrears (in CHF)",
    "revenu": "Total net monthly household income (in CHF)",
    "btn": "Estimate my eligibility",
    "result_eligible_title": "Your situation appears to qualify for legal aid",
    "result_not_eligible_title": "Based on these figures, the threshold does not appear to be met",
    "label_min_vital": "Subsistence minimum increased by {pct}%: {n} CHF",
    "label_seuil": "Total threshold (subsistence minimum + recognised expenses): {n} CHF",
    "label_revenu": "Declared net monthly income: {n} CHF",
    "label_solde_neg": "Your income is {n} CHF below the threshold: this is in your favour.",
    "label_solde_pos": "Your income is {n} CHF above the threshold.",
    "estimate_flag": "Reminder: this result relies on a national estimate (25%), not a rate specific to your canton. Check with the competent court.",
    "footer_note": "Keep in mind: your assets and the prospects of success of your case are also assessed separately by the court, independently of this calculation.",
    "source_GE": "Based on: the Canton of Geneva's 2026 seizure-exemption norms (NI-2026, rsGE E 3 60.04, in force since 01.01.2026) for the base amounts, and the current practice of the Geneva Court of Justice's Criminal Appeals Chamber, which increases this amount by 25% (ruling ACPR/552/2025 of 05.05.2025: \"Pour établir les dépenses du requérant, il convient de se fonder sur son minimum vital du droit des poursuites, augmenté de 25% (arrêt du Tribunal fédéral 1B_383/2017 du 23 novembre 2017 consid. 2).\"). SPECIAL CASE, documented as an evolving practice rather than a single fixed rate (as with Thurgau): 5 independent decisions of the Criminal Appeals Chamber applied 20% between 2020 and 2022, but 6 more recent decisions (2022-2025), including the most recent one read in full, apply 25% based on a Federal Supreme Court ruling. No directive or landmark ruling formalizing this shift was identified: the two lines overlap in 2022 with no official cutover. Counted here under 25% (the more recent and better legally reasoned practice), but both rates are documented for transparency. This estimate does not replace the registry's review and does not account for your assets or the prospects of success of your case.",
    "source_LU": "Based on: the 13 August 2009 directive of the Debt Collection and Bankruptcy Supervisory Commission of the Lucerne Cantonal High Court (LGVE 2009 I No. 42, in force since 01.10.2009, consulted on steuerbuch.lu.ch), increased by 20% per the practice confirmed in Jozic/Boesch, \"Die unentgeltliche Rechtspflege im Zivilprozess\", Lucerne Cantonal High Court, 4th edition, May 2012 (citing LGVE 2003 I No. 39). Taxes are not counted in this calculation, per the same source. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "source_GR": "Based on: a ruling of the Graubünden Cantonal Court of 26 January 2023 (ZK2 22 56) on legal aid, applying a base amount identical to Geneva's (CHF 1,200 for a single person, citing KGer GR KSK 09 39 of 18.08.2009), increased by 20% per settled case law (KGer GR ZK1 14 112 of 05.01.2015; PKG 2003 No. 13). Taxes are only counted if actually paid. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "source_SO": "Based on: a ruling of the Solothurn Cantonal High Court (Zivilkammer, ZKBES-2016-177, 22 December 2016), which explicitly states that the base amount must be increased by \"the 20% customary in the Canton of Solothurn\" and applies this concretely (CHF 1,200 + CHF 240 = CHF 1,440). Taxes are included in the calculation per the same ruling. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "source_EST": "Estimate based on Federal Tribunal case law (ruling 8C_470/2016 of 16 December 2016, consid. 5.5, citing ruling 8C_377/2016 of 8 August 2016 and SVR 2010 IV No. 10 p. 31 consid. 8.3), which treats a 25% surcharge on the base amount as the generally applied ballpark figure, a figure also cited by the Vaud Cantonal Court with reference to Federal Supreme Court ruling ATF 124 I 1. This is NOT a guaranteed rate for your canton: each canton and each judge may apply a different percentage (10% to 30% across cases reviewed). This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_ti": "Ticino",
    "heading_TI": "Legal aid eligibility estimator (canton of Ticino)",
    "disclaimer_TI": "This calculation only applies to proceedings in the canton of Ticino. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_TI": "Based on: Tribunale d'appello TI (Camera dei ricorsi penali), 60.2010.124, 05.07.2010: \"Calcul du fabbisogno minimo strictement limité au montant de base LEF et aux postes de charges réelles documentées, sans aucun supplément en pourcentage.\". The only Swiss canton where case law explicitly confirms that no surcharge whatsoever is applied to the basic minimum for legal aid purposes, confirmed by the official minimo di esistenza table used by the Ticino judiciary, which provides for no flat-rate surcharge, unlike every other canton. See the Legatis comparative study for the full list of 3 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_bl": "Basel-Country",
    "heading_BL": "Legal aid eligibility estimator (canton of Basel-Country)",
    "disclaimer_BL": "This calculation only applies to proceedings in the canton of Basel-Country. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_BL": "Based on: Kantonsgericht Basel-Landschaft (tribunal des assurances sociales), 725 2015 188, 2015: \"Application du même taux de 15% hors chambre civile, devant le tribunal des assurances sociales.\". 14 independent decisions identified in total (2012-2021), the richest body of case law in this study alongside Basel-Stadt. Important nuance: a separate line of decisions from 2013-2015 applied 25-50%, but only for calculating subsequent reimbursement of legal aid (not the initial grant); this line was abandoned from 2021 onward. See the Legatis comparative study for the full list of 14 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_bs": "Basel-City",
    "heading_BS": "Legal aid eligibility estimator (canton of Basel-City)",
    "disclaimer_BS": "This calculation only applies to proceedings in the canton of Basel-City. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_BS": "Based on: Appellationsgericht Basel-Stadt, KR.2025.2, 02.10.2025: \"Zuschlag von 15 % [CHF 382.80].\". 11 independent decisions identified (2015-2025), forming an unbroken chain of precedent over 10 years (ZB.2016.39 → ZB.2020.6 → BEZ.2018.40 → BEZ.2018.24 → VD.2018.76 → VD.2022.138 → ZB.2022.11 → KR.2025.2), the densest body of case law in the entire study. See the Legatis comparative study for the full list of 11 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_zg": "Zug",
    "heading_ZG": "Legal aid eligibility estimator (canton of Zug)",
    "disclaimer_ZG": "This calculation only applies to proceedings in the canton of Zug. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_ZG": "Based on: Obergericht Zug, BZ 2025 19, 01.07.2025: \"Existenzminimum CHF 3'589.70 (Grundbetrag [plus 20 % Zuschlag]: CHF 1'440.00...).\". 7 independent decisions identified (2022-2025), all worded as settled practice (\"praxisgemäss\"). No contradiction found. See the Legatis comparative study for the full list of 7 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_nw": "Nidwalden",
    "heading_NW": "Legal aid eligibility estimator (canton of Nidwalden)",
    "disclaimer_NW": "This calculation only applies to proceedings in the canton of Nidwalden. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_NW": "Based on: Kantonsgericht Nidwalden, formulaire officiel \"Unentgeltliche Rechtspflege\", 20.06.2024: \"Total Grundbeträge (inkl. Zuschlag von 20%) : CHF 1'200 (personne seule), CHF 1'350 (famille monoparentale), CHF 1'700 (couple).\". Official form of the cantonal court, the only available source but of a general nature (applicable to all cases, not a single file). Exhaustive research (~20 candidate decisions opened in full text) found no individual court decision applying this rate; the published body of case law for this small canton is very thin, and the directive itself dates only from 2024. See the Legatis comparative study for the full list of 1 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_ur": "Uri",
    "heading_UR": "Legal aid eligibility estimator (canton of Uri)",
    "disclaimer_UR": "This calculation only applies to proceedings in the canton of Uri. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_UR": "Based on: Obergericht Uri (Präsidium Zivilrechtliche Abteilung), 2026_OG ZP 26 2, 10.04.2026: \"Zivilprozessualer Zuschlag 20 % CHF 310.00.\". Upgraded from \"single source\" to \"confirmed\": a second independent decision was found (different judge, different case file, three years apart). An older lead (1996, Obergerichtspräsidium OGP-Z-3/96) remains unverifiable in full text (only the headnote is available) and is therefore not counted. See the Legatis comparative study for the full list of 2 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_ju": "Jura",
    "heading_JU": "Legal aid eligibility estimator (canton of Jura)",
    "disclaimer_JU": "This calculation only applies to proceedings in the canton of Jura. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_JU": "Based on: Tribunal cantonal JU (Cour administrative), ADM 2025 157, 20.01.2026: \"minimum vital de droit des poursuites pour une personne seule majoré de 25 %, citant la Circulaire n° 14 du 30 septembre 2015 du Tribunal cantonal relative à l'octroi de l'assistance judiciaire.\". 10 independent decisions identified (2013-2026, Civil Court and Administrative Court), backed by an official directive of the Cantonal Court (Circular No. 14 of 30.09.2015). Two decisions predating this circular (2013-2014) show that the 25% practice was already constant before it was formalized in writing. No contradiction found. See the Legatis comparative study for the full list of 10 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_ag": "Aargau",
    "heading_AG": "Legal aid eligibility estimator (canton of Aargau)",
    "disclaimer_AG": "This calculation only applies to proceedings in the canton of Aargau. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_AG": "Based on: Zivilgericht Argovie, XBE.2022.47, 23.11.2022: \"25 % des Grundbetrags (AGVE 2002 Nr. 15 S. 65 ff.).\". 10 independent decisions identified (2002-2026), covering three courts (Civil Court, Criminal Court, Administrative Court). One decision (ZOR.2023.6) explicitly describes the rate as \"stetige Praxis des Obergerichts\" (the cantonal court's consistent practice). No contradiction found. See the Legatis comparative study for the full list of 10 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_fr": "Fribourg",
    "heading_FR": "Legal aid eligibility estimator (canton of Fribourg)",
    "disclaimer_FR": "This calculation only applies to proceedings in the canton of Fribourg. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_FR": "Based on: Tribunal cantonal FR, 502 2022 147, 19.08.2022: \"le minimum vital du droit des poursuites, majoré de 25%, à hauteur de CHF 1'687.50.\". 13 independent decisions identified (2013-2025). Documented historical trajectory: two decisions from 2015 (102 2014 195 and 502 2015 252) still applied 20%, described at the time as \"settled Fribourg case law\"; every decision from 2018 onward confirms 25%, aligned with Federal Supreme Court rulings 4A_432/2016 and 5A_328/2016. A dated and sourced shift in practice rather than a mere static snapshot. See the Legatis comparative study for the full list of 13 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_vs": "Valais",
    "heading_VS": "Legal aid eligibility estimator (canton of Valais)",
    "disclaimer_VS": "This calculation only applies to proceedings in the canton of Valais. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_VS": "Based on: Tribunal cantonal VS (Cour civile I), C2 25 37, 12.05.2025: \"il peut ainsi couvrir son minimum vital du droit des poursuites majoré de 25 % (1500 fr.).\". 4 independent decisions identified (2022-2025), two different chambers of the Cantonal Court (civil and criminal) in agreement. See the Legatis comparative study for the full list of 4 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_sz": "Schwyz",
    "heading_SZ": "Legal aid eligibility estimator (canton of Schwyz)",
    "disclaimer_SZ": "This calculation only applies to proceedings in the canton of Schwyz. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_SZ": "Based on: Gericht SZ, BEK 2021 33, 04.06.2021: \"Zuschlag von 30 Prozent auf dem Grundbetrag von Fr. 360.00.\". Backed by a named official directive (Richtlinien der Gerichtspräsidentenkonferenz, 03.11.2003). 6 independent decisions identified in total (2019-2022); the body of case law is considered close to exhausted after reviewing around 200 decisions. Two contextual anomalies noted (a discretionary application of 20% in one particular case, a rejection of 30% in a context of remission of criminal costs distinct from the legal aid calculation), neither of which contradicts the rate within the context of the initial grant of legal aid. See the Legatis comparative study for the full list of 6 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_be": "Bern",
    "heading_BE": "Legal aid eligibility estimator (canton of Bern)",
    "disclaimer_BE": "This calculation only applies to proceedings in the canton of Bern. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_BE": "Based on: Verwaltungsgericht du canton de Berne, 100.2024.304U, 12.12.2025: \"prozessualer Zwangsbedarf [...] Grundbetrag von Fr. 1'200.--, prozessualer Zuschlag von Fr. 360.-- (soit 30%).\". 12 independent decisions identified (2013-2025), covering both the Obergericht/Regionalgericht (civil) and the Verwaltungsgericht (administrative), two different courts applying the same rate, which strengthens the evidence of a constant cantonal practice rather than an isolated case. See the Legatis comparative study for the full list of 12 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_sg": "St. Gallen",
    "heading_SG": "Legal aid eligibility estimator (canton of St. Gallen)",
    "disclaimer_SG": "This calculation only applies to proceedings in the canton of St. Gallen. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_SG": "Based on: Kantonsgericht St. Gallen, VZ.2007.31, 21.08.2007: \"Auch in quantitativer Hinsicht ist ein strengerer Massstab anzulegen als bei der Gewährung der unentgeltlichen Prozessführung, wo ein Zuschlag von 30% zum Grundbetrag berücksichtigt wird.\". Official directive of the cantonal court (2011), confirmed by a court decision that concretely applies this rate (2007, predating the directive itself). The body of case law is considered nearly exhausted beyond these two sources (most published Kantonsgericht SG decisions on legal aid are landmark rulings that do not recompute the calculation, since it is uncontested in practice). See the Legatis comparative study for the full list of 2 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case.",
    "canton_ai": "Appenzell Innerrhoden",
    "heading_AI": "Legal aid eligibility estimator (canton of Appenzell Innerrhoden)",
    "disclaimer_AI": "This calculation only applies to proceedings in the canton of Appenzell Innerrhoden. Switch canton above if your case is elsewhere. The result is an indicative estimate, not a decision: the court also assesses your assets and the prospects of success of your case. Whether taxes are included in this canton's calculation could not be verified from the sources found, so they are not counted here, which may slightly understate the real threshold.",
    "source_AI": "Based on: Canton d'Appenzell Rhodes-Intérieures (site officiel), page \"Unentgeltliche Rechtspflege\", consultée le 03.08.2026: \"Zur Berechnung des prozessualen Zwangsbedarfs wird der Grundbetrag um 30% erhöht.\". Upgraded from \"single source\" to \"confirmed\": the court decision is corroborated word for word by a general statement of practice published on the canton's official website, which is not tied to a particular case, satisfying the confirmation criterion of an official directive/general statement. Exhaustive research (around 240 Appenzell decisions reviewed in total across two passes) found no second court decision, as the body of case law for this very small canton is structurally limited. See the Legatis comparative study for the full list of 2 decisions/sources reviewed and verification links. This estimate does not replace the court's review and does not account for your assets or the prospects of success of your case."
  }
}
''')

def widget_html(lang):
    s = STRINGS[lang]
    js = (_JS_TEMPLATE
          .replace("__STRINGS_JSON__", json.dumps(s, ensure_ascii=False))
          .replace("__CANTONS_JSON__", json.dumps(CANTONS, ensure_ascii=False)))
    canton_options = "\n".join(
        f'        <option value="{code}">{s["canton_" + code.lower()]}</option>'
        for code in CANTON_ORDER
    )
    return f"""
<div class="calc-box" id="calc-aj-ge">
  <h2 id="calc-aj-heading" style="margin-top:0;">{s['heading_GE']}</h2>
  <p class="calc-disclaimer" id="calc-aj-disclaimer">{s['disclaimer_GE']}</p>
  <div class="calc-grid">
    <label class="calc-field">{s['canton_label']}
      <select id="calc-aj-canton">
{canton_options}
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
