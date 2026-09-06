"""
Le principe non-negociable du projet : aucune fiche etude/avocat ne doit
etre indexee si elle n'a aucun signal reel. Le code applique ca via
`ctx["noindex"] = not ctx["insight_text"]`, ou insight_text vient de
presentation_text.firm_insight(). Ce test verifie directement ce contrat,
independamment de toute page HTML generee -- une regression ici est le
scenario le plus grave du projet (indexation de contenu "thin").
"""
import os
import re
import presentation_text as pt


def test_every_firm_insight_call_site_passes_all_signal_kwargs():
    """Regression (decouvert le 06/09/2026) : build.py calcule ctx["insight_text"]
    (l'insight reellement affiche) ET _any_lang_lacks_signal (qui decide noindex)
    via deux appels SEPARES a pt.firm_insight() par type de page -- 4 types x 2
    appels = 8 sites au total. Quand specialist_certification/publications ont ete
    ajoutes a firm_insight(), seuls certains de ces 8 sites ont ete mis a jour :
    une fiche dont le SEUL signal reel etait specialist_certification affichait
    le texte correctement (insight_text non vide) mais restait noindex quand
    meme (le pre-check qui decide noindex ignorait ce kwarg), et certains types
    de page (etudes GE/generiques) ne recevaient jamais ce champ du tout, meme
    a l'affichage. Ce test grep-based garantit qu'un futur kwarg de signal ajoute
    a firm_insight() ne peut plus etre oublie sur un sous-ensemble des 8 sites
    sans faire echouer la suite -- un vrai test d'integration serait plus sur
    mais demanderait de construire un CANTON_DATA complet pour les 4 types de
    page ; ce garde-fou statique est le compromis pragmatique."""
    build_py_path = os.path.join(os.path.dirname(__file__), "..", "build.py")
    with open(build_py_path, encoding="utf-8") as f:
        source = f.read()

    # Isole chaque appel a pt.firm_insight(...) jusqu'a la parenthese fermante
    # correspondante (les appels s'etendent sur plusieurs lignes).
    call_sites = []
    for m in re.finditer(r"pt\.firm_insight\(", source):
        start = m.end()
        depth = 1
        i = start
        while depth > 0:
            if source[i] == "(":
                depth += 1
            elif source[i] == ")":
                depth -= 1
            i += 1
        call_sites.append(source[start:i])

    assert len(call_sites) == 8, (
        f"Attendu 8 sites d'appel a pt.firm_insight() dans build.py (4 types de page x "
        f"pre-check noindex + calcul reel), trouve {len(call_sites)} -- si ce nombre a "
        f"change intentionnellement (nouveau type de page), mets a jour ce test."
    )
    for call in call_sites:
        assert "specialist_certification=" in call, f"Site sans specialist_certification: {call[:80]}"
        assert "publications=" in call, f"Site sans publications: {call[:80]}"


def test_no_signal_produces_empty_insight():
    """Aucune langue, aucun domaine, aucune anciennete, aucun enrichissement
    web : le texte doit etre vide, ce qui declenche noindex."""
    text = pt.firm_insight("fr", [], [], None, founding_year=None, team_size_n=None)
    assert text == ""


def test_no_signal_empty_insight_in_all_languages():
    for lang in ("fr", "de", "it", "en"):
        assert pt.firm_insight(lang, [], [], None) == ""


def test_founding_year_alone_produces_non_empty_insight():
    text = pt.firm_insight("fr", [], [], None, founding_year=1998)
    assert text != ""
    assert "1998" in text


def test_oldest_year_alone_produces_non_empty_insight():
    text = pt.firm_insight("fr", [], [], 2005)
    assert text != ""


def test_languages_alone_produce_non_empty_insight():
    text = pt.firm_insight("fr", ["Français", "Anglais"], [], None)
    assert text != ""


def test_domaines_alone_produce_non_empty_insight():
    text = pt.firm_insight("fr", [], ["Droit du travail"], None)
    assert text != ""


def test_founding_year_preferred_over_oldest_year_when_both_known():
    """founding_year (site officiel, precis) doit l'emporter sur oldest_year
    (proxy registre) quand les deux sont disponibles -- voir docstring de
    firm_insight. On verifie que la date affichee est celle de founding_year."""
    text = pt.firm_insight("fr", [], [], 1980, founding_year=1998)
    assert "1998" in text
    assert "1980" not in text


def test_specialist_certification_alone_produces_non_empty_insight():
    text = pt.firm_insight("fr", [], [], None, specialist_certification="Avocat spécialiste FSA droit du travail")
    assert text != ""
    assert "Avocat spécialiste FSA droit du travail" in text


def test_publications_alone_produce_non_empty_insight():
    text = pt.firm_insight("fr", [], [], None, publications=["Le droit du bail en 2026"])
    assert text != ""
    assert "Le droit du bail en 2026" in text


def test_publications_truncated_to_three():
    text = pt.firm_insight("fr", [], [], None, publications=["A", "B", "C", "D", "E"])
    assert "A" in text and "B" in text and "C" in text
    assert "D" not in text and "E" not in text


def test_specialist_certification_and_publications_absent_by_default():
    """Meme contrat que les autres signaux : rien fourni -> rien affiche."""
    text = pt.firm_insight("fr", [], [], None)
    assert text == ""
