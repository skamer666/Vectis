"""
Mecanisme badge + revendication de fiche (levier de backlinks). Verifie que
le code d'integration genere pour chaque page est correct et absolu (il est
destine a etre colle sur le SITE EXTERNE d'un cabinet, jamais sur legatis.ch
lui-meme -- une URL relative y serait cassee).
"""
import i18n
import build


def test_claim_page_resolves_for_every_language():
    for lang in i18n.LANGUAGES:
        path = build.base_ctx(lang, "/x/", "t", "d")["claim_page_url"]
        assert path.startswith(f"/{lang}/")
        assert path.endswith("/")


def test_badge_embed_code_uses_absolute_urls():
    ctx = build.base_ctx("fr", "/fr/avocats/geneve/etude/exemple/", "t", "d")
    code = ctx["badge_embed_code"]
    assert code.startswith(f'<a href="{build.BASE_DOMAIN}')
    assert build.BASE_DOMAIN + "/fr/avocats/geneve/etude/exemple/" in code
    assert f"{build.BASE_DOMAIN}/static/badges/badge-fr.svg" in code


def test_badge_embed_code_matches_page_language():
    for lang in i18n.LANGUAGES:
        ctx = build.base_ctx(lang, "/x/", "t", "d")
        assert f"badge-{lang}.svg" in ctx["badge_embed_code"]
        assert ctx["badge_alt"] == build.BADGE_ALT[lang]


def test_every_badge_svg_asset_exists():
    import os
    for lang in i18n.LANGUAGES:
        svg_path = os.path.join(build.SITE_ROOT, "static", "badges", f"badge-{lang}.svg")
        assert os.path.exists(svg_path), svg_path
