"""
Blog juridique (blog_content.BLOG_ARTICLES) : verifie que la structure de
donnees editoriale reste coherente au fil de la redaction par lots (toutes
les langues ne sont pas forcement encore ecrites pour chaque article), et
que gen_blog() genere bien des pages propres (pas d'artefact Jinja) pour
au moins la langue francaise de chaque article.
"""
import re

import i18n
import build
import blog_content


def test_every_article_has_a_valid_domaine_id():
    for bid, article in blog_content.BLOG_ARTICLES.items():
        assert "domaine_id" in article, f"{bid} sans domaine_id"
        assert article["domaine_id"] in i18n.DOMAINES, f"{bid}: domaine_id inconnu {article['domaine_id']!r}"


def test_every_article_has_at_least_french():
    for bid, article in blog_content.BLOG_ARTICLES.items():
        assert "fr" in article, f"{bid} n'a pas de version francaise"


def test_article_language_entries_have_required_fields():
    required = {"slug", "title", "meta", "sections", "faq"}
    for bid, article in blog_content.BLOG_ARTICLES.items():
        for lang, entry in article.items():
            if lang == "domaine_id":
                continue
            missing = required - entry.keys()
            assert not missing, f"{bid}/{lang}: champs manquants {missing}"
            assert entry["sections"], f"{bid}/{lang}: aucune section"
            assert entry["faq"], f"{bid}/{lang}: aucune FAQ"


def test_slugs_are_unique_per_language():
    seen = {}
    for bid, article in blog_content.BLOG_ARTICLES.items():
        for lang, entry in article.items():
            if lang == "domaine_id":
                continue
            key = (lang, entry["slug"])
            assert key not in seen, f"slug dupliaue : {key} ({bid} et {seen.get(key)})"
            seen[key] = bid


def test_no_em_dash_in_blog_content():
    for bid, article in blog_content.BLOG_ARTICLES.items():
        for lang, entry in article.items():
            if lang == "domaine_id":
                continue
            for s in entry["sections"]:
                for p in s["paragraphs"]:
                    assert "—" not in p, f"{bid}/{lang}: em dash trouve dans une section"
            for item in entry["faq"]:
                assert "—" not in item["q"] and "—" not in item["a"], f"{bid}/{lang}: em dash trouve dans la FAQ"


def test_gen_blog_writes_clean_pages(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.URLS_GENERATED.clear()
    build.gen_blog()
    written = list(tmp_path.rglob("index.html"))
    blog_pages = [p for p in written if "/blog/" in str(p).replace("\\", "/") or str(p.parent.name) != ""]
    assert written, "gen_blog() n'a rien ecrit"
    for p in written:
        html = p.read_text(encoding="utf-8")
        assert "{{" not in html and "{%" not in html and "Undefined" not in html, f"artefact Jinja dans {p}"
