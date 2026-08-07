"""
Tests d'integration legers sur le module build : verifient que le
chargement complet des donnees reussit (tous les CSV parsent), et que les
mecanismes ajoutes pour le rebuild cible / IndexNow / les guides restent
coherents entre eux. N'ecrit dans dist/ que ce qui est strictement
necessaire, jamais un rebuild complet (trop lent pour une suite de tests
executee a chaque push).
"""
import json
import os

import build


def test_core_datasets_load_and_are_non_empty():
    assert len(build.GE_INDIVIDUALS) > 0
    assert len(build.GE_FIRMS) > 0
    assert len(build.CANTON_DATA) == len(build.OTHER_CANTON_CODES)
    assert len(build.CITY_DATA) > 0


def test_every_generated_lawyer_has_a_slug():
    assert all(r.get("_slug") for r in build.GE_INDIVIDUALS)


def test_eponymous_cities_are_excluded_from_city_pages():
    """Pas de page ville 'Genève' dans le canton GE ni 'Zürich' dans ZH --
    la page canton couvre deja exactement cette requete (anti-duplication)."""
    ge_city_names = {c["name"] for c in build.CITY_DATA.get("GE", [])}
    assert "Genève" not in ge_city_names
    zh_city_names = {c["name"] for c in build.CITY_DATA.get("ZH", [])}
    assert "Zürich" not in zh_city_names


def test_city_pages_respect_minimum_lawyer_threshold():
    for cities in build.CITY_DATA.values():
        for c in cities:
            assert c["count"] >= build.CITY_MIN_LAWYERS


def test_urls_for_domain_and_gen_affected_agree_on_page_count(tmp_path, monkeypatch):
    """Regression cle : le rebuild cible (gen_affected_for_domain, qui ECRIT
    les pages) et l'aide a la soumission IndexNow (urls_for_domain, qui
    LISTE les URLs) doivent toujours porter sur exactement le meme
    perimetre. Un ecart signifie qu'un lot enrichi ne sera pas notifie a
    IndexNow, ou inversement qu'on notifie des URLs jamais regenerees."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    domains = [k for k in build.WEB_ENRICHMENT if not k.startswith("_")][:5]
    assert domains, "aucun domaine connu dans cabinet_web_enrichment.json pour ce test"
    for domain in domains:
        n_urls = len(build.urls_for_domain(domain))
        n_written = build.gen_affected_for_domain(domain)
        assert n_urls == n_written, f"{domain}: {n_urls} URLs listees vs {n_written} pages ecrites"


def test_gen_affected_for_domain_is_noop_for_unknown_domain(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    assert build.gen_affected_for_domain("ce-domaine-n-existe-pas-xyz123.ch") == 0


def test_indexnow_key_file_content_matches_key_used_for_submission():
    """Le fichier de verification doit contenir exactement la cle utilisee
    par indexnow_submit.py -- sinon les moteurs rejettent toute soumission."""
    import indexnow_submit
    assert build.INDEXNOW_KEY == indexnow_submit.INDEXNOW_KEY


def test_gen_indexnow_key_writes_expected_file(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_indexnow_key()
    key_file = tmp_path / f"{build.INDEXNOW_KEY}.txt"
    assert key_file.exists()
    assert key_file.read_text(encoding="utf-8").strip() == build.INDEXNOW_KEY


def test_vitrine_previews_render_for_all_templates_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_vitrine_previews()
    import vitrine_content
    for template in vitrine_content.TEMPLATE_ORDER:
        html = (tmp_path / "fr" / "vitrine-preview" / template / "index.html").read_text(encoding="utf-8")
        assert "{{" not in html and "{%" not in html and "Undefined" not in html
        assert 'data-field="nom_complet"' in html
        assert "Camille Fontaine" in html


def test_vitrine_request_form_embeds_accent_ramps_and_preview_urls(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_vitrine_previews()
    build.gen_vitrine_request()
    html = (tmp_path / "fr" / "vitrine-avocat" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "ACCENT_RAMPS" in html
    assert "/fr/vitrine-preview/prestige/" in html
    assert 'id="vf-role-titre"' in html
    assert 'id="vf-instagram"' in html


def test_avis_request_page_renders_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_avis_request()
    html = (tmp_path / "fr" / "avis-avocat" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "Laisser un avis" in html


def test_reviews_widget_hidden_when_supabase_not_configured(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    monkeypatch.setattr(build.supabase_config, "SUPABASE_URL", "")
    build.gen_ge_avocats(0, 1)
    files = list((tmp_path / "fr" / "avocats" / "geneve" / "avocat").glob("*/index.html"))
    assert files
    html = files[0].read_text(encoding="utf-8")
    assert "reviews-widget" not in html


def test_reviews_widget_shown_when_supabase_configured(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    monkeypatch.setattr(build.supabase_config, "SUPABASE_URL", "https://fake.supabase.co")
    monkeypatch.setattr(build.supabase_config, "SUPABASE_ANON_KEY", "fake-key")
    build.gen_ge_avocats(0, 1)
    files = list((tmp_path / "fr" / "avocats" / "geneve" / "avocat").glob("*/index.html"))
    assert files
    html = files[0].read_text(encoding="utf-8")
    assert "reviews-widget" in html
    assert 'data-canton="GE"' in html


def test_guides_have_matching_faq_schema_structure():
    """Chaque guide doit avoir au moins une question, et chaque FAQ doit
    avoir une question et une reponse non vides, dans les 4 langues."""
    import guides_content
    for gid, per_lang in guides_content.GUIDES.items():
        for lang in ("fr", "de", "it", "en"):
            g = per_lang[lang]
            assert g["faq"], f"{gid}/{lang}: aucune FAQ"
            for item in g["faq"]:
                assert item["q"].strip()
                assert item["a"].strip()


def test_guide_faq_schema_json_is_valid():
    import guides_content
    g = guides_content.GUIDES["cout-avocat"]["fr"]
    schema = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"],
             "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in g["faq"]
        ],
    }
    parsed = json.loads(json.dumps(schema, ensure_ascii=False))
    assert len(parsed["mainEntity"]) == len(g["faq"])
