"""
Tests des fonctions pures de nettoyage/normalisation de donnees dans build.py.
Ces fonctions sont le rempart contre les artefacts de scraping (secteurs
postaux, marqueurs de langue, valeurs "[]", lignes de test) -- une regression
ici abime silencieusement des milliers de fiches.
"""
import build


def test_slugify_strips_accents_and_lowercases():
    assert build.slugify("Étude Général & Associés") == "etude-general-associes"


def test_slugify_never_returns_empty():
    assert build.slugify("") == "x"
    assert build.slugify("!!!") == "x"


def test_norm_is_accent_and_case_insensitive():
    assert build.norm("Genève") == build.norm("GENEVE")
    assert build.norm("  Étude   Dupont ") == "etude dupont"


def test_clean_ville_strips_postal_sector_suffix():
    assert build.clean_ville("Genève 3") == "Genève"
    assert build.clean_ville("Genève 12 Champel") == "Genève"
    assert build.clean_ville("Carouge GE") == "Carouge GE"  # pas un suffixe numerique


def test_clean_ville_recovers_known_bad_ge_values():
    assert build.clean_ville("Legal, Conseil & Tax", npa="1204") == "Genève"


def test_clean_ville_passthrough_for_normal_city():
    assert build.clean_ville("Lausanne", npa="1003") == "Lausanne"


def test_site_domain_strips_www_and_scheme():
    assert build.site_domain("https://www.example.ch/fr") == "example.ch"
    assert build.site_domain("example.ch") == "example.ch"
    assert build.site_domain("http://Example.CH") == "example.ch"


def test_site_domain_handles_empty_and_junk():
    assert build.site_domain("") is None
    assert build.site_domain(None) is None


def test_normalize_row_filters_test_junk():
    row = build.normalize_row("GE", {"nom_complet": "TEST Ligne De Test"})
    assert row["nom_complet"] == ""


def test_normalize_row_recovers_npa_from_ville_field():
    row = build.normalize_row("ZH", {"nom_complet": "Jean Muster", "npa": "", "ville": "8001 Zürich"})
    assert row["npa"] == "8001"
    assert row["ville"] == "Zürich"


def test_normalize_row_treats_bracket_placeholders_as_empty():
    row = build.normalize_row("ZH", {
        "nom_complet": "Jean Muster", "npa": "[]", "ville": "[]",
        "telephone": "[]", "email": "[]", "site_web": "[]",
    })
    assert row["npa"] == ""
    assert row["ville"] == ""
    assert row["telephone"] == ""
    assert row["email"] == ""
    assert row["site_web"] == ""
