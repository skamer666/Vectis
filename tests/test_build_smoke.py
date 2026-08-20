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


def test_to_embed_url_recognises_youtube_and_vimeo_only():
    assert build.to_embed_url("https://www.youtube.com/watch?v=abc12345678") == "https://www.youtube-nocookie.com/embed/abc12345678"
    assert build.to_embed_url("https://youtu.be/abc12345678") == "https://www.youtube-nocookie.com/embed/abc12345678"
    assert build.to_embed_url("https://vimeo.com/123456789") == "https://player.vimeo.com/video/123456789"
    assert build.to_embed_url("https://example.com/video.mp4") is None
    assert build.to_embed_url("") is None


def test_avis_request_page_renders_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_avis_request()
    html = (tmp_path / "fr" / "avis-avocat" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "Laisser un avis" in html


def test_verification_request_page_renders_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_request()
    html = (tmp_path / "fr" / "verifier-mon-identite" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "Vérifier mon identité" in html
    assert "/verification-index.json" in html
    assert "/api/verification-request" in html


def test_verification_request_page_collects_account_credentials_and_all_methods(tmp_path, monkeypatch):
    """Le mot de passe est desormais choisi des la demande initiale (pas
    apres coup), et les 3 methodes de verification restent toujours
    proposees -- meme celles non correspondant au palier "ideal" -- pour
    que le demandeur puisse contourner un email/telephone errone."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_request()
    html = (tmp_path / "fr" / "verifier-mon-identite" / "index.html").read_text(encoding="utf-8")
    assert 'id="vf-account-email"' in html
    assert 'id="vf-password"' in html
    assert 'id="vf-password-confirm"' in html
    assert 'value="email"' in html and 'value="phone"' in html and 'value="document"' in html


def test_verification_request_page_has_optional_marketing_consent_checkbox(tmp_path, monkeypatch):
    """Case a cocher FACULTATIVE (pas de attribut 'checked', et distincte du
    consentement d'identite obligatoire) pour recevoir d'autres emails
    Legatis que ceux lies a la creation/activation du compte."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_request()
    html = (tmp_path / "fr" / "verifier-mon-identite" / "index.html").read_text(encoding="utf-8")
    assert 'id="vf-consent-marketing-cb"' in html
    assert '<input type="checkbox" id="vf-consent-marketing-cb">' in html
    assert "recevoir d" in html and "autres emails de Legatis" in html
    assert "marketing_consent" in html


def test_verification_request_page_offers_free_website_after_signup(tmp_path, monkeypatch):
    """Juste apres la creation du compte (avant validation de l'identite),
    la page propose l'offre "site web gratuit" avec un contrat complet a
    faire defiler jusqu'au bout avant de pouvoir l'accepter -- voir
    website_offer_content.py."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_request()
    html = (tmp_path / "fr" / "verifier-mon-identite" / "index.html").read_text(encoding="utf-8")
    assert 'id="vf-offer"' in html
    assert 'id="vf-offer-accept"' in html
    assert 'id="vf-offer-decline"' in html
    assert 'id="vf-contract"' in html
    assert 'id="vf-contract-scrollbox"' in html
    assert 'id="vf-contract-checkbox"' in html
    # La case et le bouton d'acceptation doivent demarrer desactives : ils
    # ne s'activent qu'apres defilement complet du contrat (JS).
    assert '<input type="checkbox" id="vf-contract-checkbox" disabled>' in html
    assert 'id="vf-contract-accept" disabled' in html
    assert "Et si Legatis vous offrait votre site internet" in html
    assert "/api/website-offer-decision" in html


def test_verification_request_page_contract_has_23_full_articles(tmp_path, monkeypatch):
    """Contrat "ULTRA LONG" demande explicitement par Gregoire Giuliano :
    23 articles numerotes sans trou (bug de numerotation corrige lors de la
    redaction), couvrant tous les points requis (gratuite, controle total
    de Legatis, modifications payantes, nom de domaine a la charge de
    l'avocat, backlinks, transmission de leads a des tiers)."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_request()
    html = (tmp_path / "fr" / "verifier-mon-identite" / "index.html").read_text(encoding="utf-8")
    for n in range(1, 24):
        assert f"Article {n} —" in html
    assert "Article 24" not in html
    assert "gratuit" in html.lower()
    assert "backlink" in html.lower()
    assert "leads" in html.lower()


def test_verification_confirmee_page_renders_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_confirmee()
    html = (tmp_path / "fr" / "identite-confirmee" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "Identité confirmée" in html


def test_verification_review_page_is_noindex(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_review()
    html = (tmp_path / "interne" / "verification-avocats" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert 'name="robots" content="noindex' in html
    assert "/api/verification-list" in html
    assert "/api/verification-decide" in html


def test_analytics_dashboard_page_is_noindex(tmp_path, monkeypatch):
    """Page interne de consultation des statistiques d'analytics maison --
    meme principe de protection par jeton que verification_review.html,
    aucune donnee en dur cote build."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_analytics_dashboard()
    html = (tmp_path / "interne" / "analytics" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert 'name="robots" content="noindex' in html
    assert "/api/analytics-summary" in html
    assert 'id="ad-token"' in html


def test_internal_pages_cross_link_via_admin_nav(tmp_path, monkeypatch):
    """Les 3 pages internes (verifications, analytics, vitrines) doivent se
    renvoyer les unes aux autres, pour pouvoir consulter les stats depuis la
    page de moderation habituelle sans avoir a retenir une URL a part."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_review()
    build.gen_analytics_dashboard()
    build.gen_vitrine_review()
    pages = {
        "verification": tmp_path / "interne" / "verification-avocats" / "index.html",
        "analytics": tmp_path / "interne" / "analytics" / "index.html",
        "vitrines": tmp_path / "interne" / "vitrines-en-attente" / "index.html",
    }
    for name, path in pages.items():
        html = path.read_text(encoding="utf-8")
        assert "/interne/verification-avocats/" in html
        assert "/interne/analytics/" in html
        assert "/interne/vitrines-en-attente/" in html
        assert 'admin-nav-link is-active' in html


def test_base_html_loads_privacy_friendly_analytics_script(tmp_path, monkeypatch):
    """static/js/analytics.js doit etre charge sur toutes les pages (via
    base.html) -- verifie ici sur une page simple pour ne pas dependre d'un
    generateur particulier."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_review()
    html = (tmp_path / "interne" / "verification-avocats" / "index.html").read_text(encoding="utf-8")
    assert "static/js/analytics.js" in html


def test_privacy_page_discloses_analytics_and_lawyer_accounts(tmp_path, monkeypatch):
    """La page confidentialite doit rester exacte : elle affirmait par le
    passe qu'aucun compte n'etait jamais requis, ce qui n'est plus vrai
    depuis le systeme de compte avocat ; elle doit aussi divulguer le
    nouveau systeme d'analytics maison (sans cookie, sans IP)."""
    fr = build.sp_content.get_page("confidentialite", "fr")
    all_text = " ".join(p for s in fr["sections"] for p in s["paragraphs"])
    assert "aucune adresse IP" in all_text or "IP" in all_text
    assert "cookie" in all_text
    assert "avocats souhaitant revendiquer" in all_text


def test_connexion_page_renders_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_connexion()
    html = (tmp_path / "fr" / "connexion" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "Connexion avocat" in html
    assert "/auth/v1/token?grant_type=password" in html


def test_mon_profil_page_renders_without_jinja_artifacts(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_mon_profil()
    html = (tmp_path / "fr" / "mon-profil" / "index.html").read_text(encoding="utf-8")
    assert "{{" not in html and "{%" not in html and "Undefined" not in html
    assert "Mon profil" in html
    assert "/rest/v1/lawyer_profile_submissions" in html
    assert 'name="robots" content="noindex' in html


def test_header_has_lawyer_account_cta(tmp_path, monkeypatch):
    """Le bouton signup/connexion avocat doit etre present dans le header
    de toute page (verifie ici via une page deja generee dans ce module)."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_confirmee()
    html = (tmp_path / "fr" / "identite-confirmee" / "index.html").read_text(encoding="utf-8")
    assert "masthead-cta" in html
    assert "/fr/connexion/" in html


def test_verification_confirmee_offers_login_link(tmp_path, monkeypatch):
    """Le compte est deja actif des la confirmation (pre-cree a la demande,
    active par api/verification-confirm.js) : plus besoin d'un lien de
    creation de compte separe, juste d'un lien de connexion."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_confirmee()
    html = (tmp_path / "fr" / "identite-confirmee" / "index.html").read_text(encoding="utf-8")
    assert "/fr/connexion/" in html
    assert "compte est désormais actif" in html


def test_verification_review_lists_profile_moderation_endpoints(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_review()
    html = (tmp_path / "interne" / "verification-avocats" / "index.html").read_text(encoding="utf-8")
    assert "/api/profile-list" in html
    assert "/api/profile-decide" in html


def test_verification_contacts_json_never_shipped_to_dist(tmp_path, monkeypatch):
    """Le fichier server-side (email/telephone reels) ne doit jamais finir
    dans dist/ -- seul le fichier public a booleens (verification-index.json)
    est autorise a y vivre."""
    monkeypatch.setattr(build, "DIST_DIR", str(tmp_path))
    build.gen_verification_contacts()
    assert not (tmp_path / "verification_contacts.json").exists()
    assert (tmp_path / "verification-index.json").exists()


def test_verification_contacts_keys_match_registry_slugs():
    """Chaque cle du lookup email/telephone doit correspondre a une fiche
    reellement generee (meme canton, meme slug) -- sinon la cascade de
    verification pointerait vers une fiche inexistante."""
    build.gen_verification_contacts()
    with open(os.path.join(build.DATA_DIR, "verification_contacts.json"), encoding="utf-8") as f:
        contacts = json.load(f)
    assert contacts
    known_keys = {f"GE/{r['_slug']}" for r in build.GE_INDIVIDUALS}
    for code, data in build.CANTON_DATA.items():
        known_keys |= {f"{code}/{r['_slug']}" for r in data["individuals"]}
    assert set(contacts.keys()) <= known_keys


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
