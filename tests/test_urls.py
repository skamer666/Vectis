"""
Tests du module urls.py (routing pur, sans dependance aux donnees CSV).
"""
import re

import i18n
import urls


def test_seg_covers_all_languages():
    for name, per_lang in i18n.SEGMENTS.items():
        for lang in i18n.LANGUAGES:
            assert urls.seg(name, lang) == per_lang[lang]


def test_canton_path_distinct_per_language():
    paths = {lang: urls.canton_path("GE", lang) for lang in i18n.LANGUAGES}
    # Chaque langue doit produire un chemin distinct (slugs traduits), et
    # chaque chemin doit commencer et finir par "/".
    assert len(set(paths.values())) == len(i18n.LANGUAGES)
    for lang, p in paths.items():
        assert p.startswith(f"/{lang}/")
        assert p.endswith("/")


def test_etude_and_avocat_paths_nest_under_canton():
    for lang in i18n.LANGUAGES:
        canton = urls.canton_path("GE", lang)
        assert urls.etude_path("GE", "cabinet-x", lang).startswith(canton)
        assert urls.avocat_path("GE", "jean-dupont", lang).startswith(canton)


def test_ville_domaine_path_nests_under_ville_path():
    for lang in i18n.LANGUAGES:
        ville = urls.ville_path("VD", "lausanne", lang)
        domaine_id = next(iter(i18n.DOMAINES))
        vd_path = urls.ville_domaine_path("VD", "lausanne", domaine_id, lang)
        assert vd_path.startswith(ville)
        assert vd_path.endswith("/")


def test_guide_path_resolves_for_every_guide_and_language():
    import guides_content
    for gid in guides_content.GUIDES:
        for lang in i18n.LANGUAGES:
            p = urls.guide_path(gid, lang)
            assert p.startswith(f"/{lang}/")
            assert guides_content.GUIDES[gid][lang]["slug"] in p


def test_hreflang_for_produces_one_url_per_language():
    result = urls.hreflang_for(urls.canton_path, "GE")
    assert set(result.keys()) == set(i18n.LANGUAGES)
    for lang, u in result.items():
        assert u.startswith(urls.BASE_DOMAIN)
        assert u.endswith(urls.canton_path("GE", lang))


def test_no_double_slash_in_any_generated_path():
    """Regression : un chemin d'URL bien construit ne contient jamais '//'
    (hors le prefixe https://)."""
    candidates = [
        urls.canton_path("GE", "fr"),
        urls.etude_path("GE", "x", "fr"),
        urls.avocat_path("GE", "x", "fr"),
        urls.ville_path("VD", "lausanne", "de"),
        urls.ville_domaine_path("VD", "lausanne", next(iter(i18n.DOMAINES)), "it"),
        urls.guides_index_path("en"),
        urls.home_path("fr"),
    ]
    for path in candidates:
        assert "//" not in path, path
