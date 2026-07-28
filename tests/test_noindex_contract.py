"""
Le principe non-negociable du projet : aucune fiche etude/avocat ne doit
etre indexee si elle n'a aucun signal reel. Le code applique ca via
`ctx["noindex"] = not ctx["insight_text"]`, ou insight_text vient de
presentation_text.firm_insight(). Ce test verifie directement ce contrat,
independamment de toute page HTML generee -- une regression ici est le
scenario le plus grave du projet (indexation de contenu "thin").
"""
import presentation_text as pt


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
