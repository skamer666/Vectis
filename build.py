#!/usr/bin/env python3
"""
Generateur statique du site Legatis (pilote canton de Geneve, 4 langues).
Lit les CSV deja collectes dans data/, genere du HTML statique via Jinja2.
"""
import csv
import datetime
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from urllib.parse import quote as _url_quote

from jinja2 import Environment, FileSystemLoader

sys.path.insert(0, os.path.dirname(__file__))
import i18n

# Mots courts reutilises pour allonger les title tags (SEO) sans fabriquer
# de donnee : ce sont de simples traductions de mots deja utilises ailleurs
# sur le site (avocats/Anwaelte/avvocati/lawyers, Suisse/Schweiz/Svizzera/
# Switzerland), jamais une statistique inventee.
LAWYER_WORD = {"fr": "avocats", "de": "Anwälte", "it": "avvocati", "en": "lawyers"}
COUNTRY_NAME = {"fr": "Suisse", "de": "Schweiz", "it": "Svizzera", "en": "Switzerland"}
COUNTRY_PREP = {"fr": "en", "de": "in der", "it": "in", "en": "in"}
import presentation_text as pt
import static_pages as sp_content
import guides_content
import blog_content
import calc_widget
import legal_tools_widgets
import aj_study_content as aj
import vitrine_content
import review_content
import verification_content
import website_offer_content
import account_content
import supabase_config
from urls import (
    BASE_DOMAIN, LANGS, seg, canton_path, domaine_path, cross_path, avocat_path,
    etude_path, ville_path, ville_domaine_path, guides_index_path, guide_path,
    home_path, cantons_index_path, domaines_index_path, static_path, hreflang_for,
    blog_index_path, blog_article_path, etude_aj_path, vitrine_path,
    avis_request_path, verification_request_path, verification_confirmee_path,
    connexion_path, mon_profil_path,
)

SITE_ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(SITE_ROOT, "templates")
DIST_DIR = os.path.join(SITE_ROOT, "dist")
DATA_DIR = os.path.join(SITE_ROOT, "data")
if not os.path.isdir(DATA_DIR):
    DATA_DIR = os.path.abspath(os.path.join(SITE_ROOT, "..", "..", "..", "..", "Vectis", "data"))
if not os.path.isdir(DATA_DIR):
    DATA_DIR = "/sessions/sweet-beautiful-heisenberg/mnt/Vectis/data"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)


def load_review_aggregates():
    """Recupere les avis approuves depuis Supabase pour enrichir le schema
    Attorney (AggregateRating -> etoiles dans les resultats de recherche).
    Best effort : si Supabase n'est pas configure/joignable ou si la table
    n'existe pas encore, retourne un dict vide sans jamais faire echouer le
    build (SEO en plus, jamais un point de defaillance)."""
    if not supabase_config.SUPABASE_URL:
        return {}
    import urllib.request
    import urllib.error
    url = (f"{supabase_config.SUPABASE_URL}/rest/v1/reviews"
           "?status=eq.approved&select=canton_code,avocat_slug,rating")
    req = urllib.request.Request(url, headers={
        "apikey": supabase_config.SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {supabase_config.SUPABASE_ANON_KEY}",
    })
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            rows = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Avis Supabase non recuperes pour AggregateRating (ignore) : {e}", file=sys.stderr)
        return {}
    agg = {}
    for r in rows if isinstance(rows, list) else []:
        key = (r.get("canton_code"), r.get("avocat_slug"))
        if key[0] and key[1] and isinstance(r.get("rating"), (int, float)):
            agg.setdefault(key, []).append(r["rating"])
    return {k: {"avg": round(sum(v) / len(v), 1), "count": len(v)} for k, v in agg.items() if v}


REVIEW_AGGREGATES = load_review_aggregates()
if REVIEW_AGGREGATES:
    print(f"{len(REVIEW_AGGREGATES)} fiche(s) avec avis approuves (AggregateRating).", file=sys.stderr)


def attorney_rating_schema(canton_code, slug):
    agg = REVIEW_AGGREGATES.get((canton_code, slug))
    if not agg:
        return None
    return {
        "@type": "AggregateRating", "ratingValue": agg["avg"],
        "reviewCount": agg["count"], "bestRating": 5, "worstRating": 1,
    }


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "x"


def norm(text):
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", text).strip().lower()


def write_page(path, html):
    out = os.path.join(DIST_DIR, path.lstrip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    URLS_GENERATED.append(path)


URLS_GENERATED = []


BADGE_ALT = {"fr": "Référencé sur Legatis", "de": "Erfasst auf Legatis", "it": "Censito su Legatis", "en": "Listed on Legatis"}

# Traduction des noms de langues tels que fournis en allemand par le registre
# de Schaffhouse (seul canton avec ce champ pour l'instant) -- juste des noms
# de langues, pas de jargon juridique, donc traduction sure et non ambigue.
LANG_NAME_TRANSLATIONS = {
    "Deutsch": {"fr": "allemand", "de": "Deutsch", "it": "tedesco", "en": "German"},
    "Englisch": {"fr": "anglais", "de": "Englisch", "it": "inglese", "en": "English"},
    "Französisch": {"fr": "français", "de": "Französisch", "it": "francese", "en": "French"},
    "Italienisch": {"fr": "italien", "de": "Italienisch", "it": "italiano", "en": "Italian"},
    "Spanisch": {"fr": "espagnol", "de": "Spanisch", "it": "spagnolo", "en": "Spanish"},
    "Portugiesisch": {"fr": "portugais", "de": "Portugiesisch", "it": "portoghese", "en": "Portuguese"},
    "Serbokroatisch": {"fr": "serbo-croate", "de": "Serbokroatisch", "it": "serbo-croato", "en": "Serbo-Croatian"},
    "Rätoromanisch": {"fr": "romanche", "de": "Rätoromanisch", "it": "romancio", "en": "Romansh"},
    "Türkisch": {"fr": "turc", "de": "Türkisch", "it": "turco", "en": "Turkish"},
    "Schwedisch": {"fr": "suédois", "de": "Schwedisch", "it": "svedese", "en": "Swedish"},
}


def translate_lang_name(name, lang):
    entry = LANG_NAME_TRANSLATIONS.get(name)
    return entry[lang] if entry else name


def base_ctx(lang, path, title, description, extra_hreflang=None):
    depth = path.strip("/").count("/") + 1
    hreflang = extra_hreflang or {}
    page_url = BASE_DOMAIN + path
    badge_svg_url = f"{BASE_DOMAIN}/static/badges/badge-{lang}.svg"
    badge_alt = BADGE_ALT[lang]
    badge_embed_code = (
        f'<a href="{page_url}" target="_blank" rel="noopener">'
        f'<img src="{badge_svg_url}" alt="{badge_alt}" width="220" height="56"></a>'
    )
    return {
        "lang": lang,
        "title": title,
        "meta_description": pt.smart_truncate(description, 158),
        "canonical_url": BASE_DOMAIN + path,
        "hreflang": hreflang,
        "nav_hreflang": {lg: (u[len(BASE_DOMAIN):] if u.startswith(BASE_DOMAIN) else u) for lg, u in hreflang.items()},
        "asset_prefix": static_path(lang, depth).replace("static/", ""),
        "home_url": home_path(lang),
        "cantons_index_url": cantons_index_path(lang),
        "domaines_index_url": domaines_index_path(lang),
        "guides_index_url": guides_index_path(lang),
        "blog_index_url": blog_index_path(lang),
        "claim_page_url": f"/{lang}/{seg('revendiquer', lang)}/",
        "avis_request_url": avis_request_path(lang),
        "verification_request_url": verification_request_path(lang),
        "connexion_url": connexion_path(lang),
        "mon_profil_url": mon_profil_path(lang),
        "supabase_url": supabase_config.SUPABASE_URL,
        "supabase_anon_key": supabase_config.SUPABASE_ANON_KEY,
        "rw": review_content.WIDGET[lang],
        "badge_svg_url": badge_svg_url,
        "badge_alt": badge_alt,
        "badge_embed_code": badge_embed_code,
        "og_image": f"{BASE_DOMAIN}/static/img/og-default-{lang}.png",
        "methodology_url": f"/{lang}/{seg('methodologie', lang)}/",
        "about_url": f"/{lang}/{seg('a-propos', lang)}/",
        "contact_url": f"/{lang}/{seg('contact', lang)}/",
        "legal_url": f"/{lang}/{seg('mentions-legales', lang)}/",
        "privacy_url": f"/{lang}/{seg('confidentialite', lang)}/",
        "correction_url": f"/{lang}/{seg('correction', lang)}/",
        "ui": i18n.UI[lang],
        "schema": None,
        "breadcrumb": None,
    }


# ---------------------------------------------------------------- data load

def load_ge_individuals():
    path = os.path.join(DATA_DIR, "avocats_geneve_enrichi.csv")
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen_slugs = {}
    for r in rows:
        base = slugify(r["nom_complet"])
        n = seen_slugs.get(base, 0)
        seen_slugs[base] = n + 1
        r["_slug"] = base if n == 0 else f"{base}-{n+1}"
    return rows


def load_ge_firms():
    path = os.path.join(DATA_DIR, "etudes_geneve.csv")
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen_slugs = {}
    for r in rows:
        base = slugify(r["etude"])
        n = seen_slugs.get(base, 0)
        seen_slugs[base] = n + 1
        r["_slug"] = base if n == 0 else f"{base}-{n+1}"
        r["_members"] = [
            m.strip() for m in r.get("avocats", "").split("|") if m.strip()
        ]
    return rows


def other_canton_counts():
    counts = {}
    mapping = {
        "AG": "avocats_argovie.csv", "AI": "avocats_appenzell_rhodes_interieures.csv",
        "BS": "avocats_bale_ville.csv", "FR": "avocats_fribourg.csv",
        "GL": "avocats_glaris.csv", "GR": "avocats_grisons.csv", "JU": "avocats_jura.csv",
        "LU": "avocats_lucerne.csv", "NE": "avocats_neuchatel.csv", "NW": "avocats_nidwald.csv",
        "OW": "avocats_obwald.csv", "SG": "avocats_saint_gall.csv", "SO": "avocats_soleure.csv",
        "SZ": "avocats_schwyz.csv", "TG": "avocats_thurgovie.csv", "UR": "avocats_uri.csv",
        "VD": "avocats_vaud.csv", "ZG": "avocats_zoug.csv", "ZH": "avocats_zurich.csv",
    }
    for code, fname in mapping.items():
        p = os.path.join(DATA_DIR, fname)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                counts[code] = sum(1 for _ in csv.DictReader(f))
    counts["GE"] = None  # filled by caller
    return counts


print("Chargement des donnees Geneve...", file=sys.stderr)
def clean_ville(v, npa=""):
    # Retire les suffixes de secteur postal (Geneve 3, Geneve 12 Champel...)
    # qui ne parlent a personne hors du tri postal interne.
    # Corrige aussi les quelques lignes ou l enrichissement a ecrit un texte
    # d activite (ex: nom de societe avec virgule) a la place de la ville :
    # une vraie localite suisse ne contient jamais de virgule.
    if not v:
        return v
    v = re.sub(r"\s+\d+(\s+\S+)*$", "", v).strip()
    known_bad = {"legal, conseil & tax", "gt sa"}
    if (("," in v and npa.strip().startswith("12")) or v.lower() in known_bad):
        return "Genève"
    return v


def load_web_enrichment():
    path = os.path.join(DATA_DIR, "cabinet_web_enrichment.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("_meta", None)
    return data


def load_other_canton_enrichment():
    """Cache de decouverte alimente par la phase 2 du pilote d'enrichissement
    (cabinets des cantons generiques, sans etude/site_web dans leur CSV source
    -- voir data/ENRICHISSEMENT_PROGRESS.md). Contrairement a WEB_ENRICHMENT
    (indexe par domaine, associe via le champ site_web des avocats), ce cache
    doit etre rattache par nom de cabinet car ces CSV n'ont aucun site_web."""
    path = os.path.join(DATA_DIR, "domaines_autres_cantons.json")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    entries = []
    for domain, entry in data.items():
        if not isinstance(entry, dict) or entry.get("_failed"):
            continue
        if not entry.get("canton") or not entry.get("firm_name"):
            continue
        entries.append(entry)
    return entries


_LEGAL_SUFFIX_RE = re.compile(
    r"\b(ag|sa|gmbh|sarl|s a r l|ltd|llp|klg|kollektivgesellschaft|inc|llc|se)\b"
)


def firm_core_name(name):
    """Nom de cabinet reduit a son coeur identifiant (sans forme juridique ni
    ponctuation) pour rapprocher deux graphies du meme nom (ex. 'Schellenberg
    Wittmer AG' vs 'Schellenberg Wittmer Ltd'). Sert uniquement a apparier des
    donnees deja reelles entre elles -- ne genere ni n'invente aucun nom."""
    n = norm(name)
    n = _LEGAL_SUFFIX_RE.sub(" ", n)
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n


def site_domain(url):
    from urllib.parse import urlparse
    u = (url or "").strip()
    if not u:
        return None
    if not u.startswith("http"):
        u = "https://" + u
    try:
        d = urlparse(u).netloc.lower()
        if d.startswith("www."):
            d = d[4:]
        return d or None
    except ValueError:
        return None


WEB_ENRICHMENT = load_web_enrichment()
OTHER_CANTON_ENRICHMENT = load_other_canton_enrichment()


def web_practice_areas(web, lang):
    """Domaines de competence scrapes sur le site du cabinet, dans la langue
    demandee. practice_areas_de/it sont des traductions (voir
    practice_areas_translation_note dans le JSON) de practice_areas_fr (ou
    _en a defaut) -- le scraper lui-meme n'a jamais extrait de version DE/IT.
    Sans ceci, seules les pages FR/EN avaient ce signal, ce qui noindexait a
    tort des fiches en DE/IT (cf. audit SEO du 2026-08-23)."""
    if not web:
        return []
    return web.get(f"practice_areas_{lang}") or []

GE_INDIVIDUALS = load_ge_individuals()
for _r in GE_INDIVIDUALS:
    _r["ville"] = clean_ville(_r.get("ville", ""), _r.get("npa", ""))

GE_FIRMS = load_ge_firms()
for _r in GE_FIRMS:
    _r["ville"] = clean_ville(_r.get("ville", ""), _r.get("npa", ""))

# Exclure les pseudo-"etudes" [Independant] <adresse> : artefact du scraping
# d'origine qui regroupe les avocats sans etude par adresse partagee plutot
# que de les laisser comme individus. Ce ne sont pas de vraies etudes.
GE_FIRMS = [f for f in GE_FIRMS if not f["etude"].strip().startswith("[Ind\u00e9pendant]")]
FIRM_BY_NORM = {norm(r["etude"]): r for r in GE_FIRMS}

MEMBERS_BY_FIRM_NORM = {}
for _r in GE_INDIVIDUALS:
    _e = _r.get("etude", "").strip()
    if _e:
        MEMBERS_BY_FIRM_NORM.setdefault(norm(_e), []).append(_r)

SOLO_LAWYERS = [r for r in GE_INDIVIDUALS if not r.get("etude", "").strip()]

# Vaud (et potentiellement d'autres cantons a l'avenir) n'a aucun champ "etude"
# en texte libre dans son registre source -- contrairement a Geneve, on ne peut
# pas regrouper les avocats par cabinet directement depuis les donnees brutes.
# On derive ce regroupement depuis le domaine du site_web (donnee deja fiable,
# affirmee par l'avocat lui-meme au registre), en reutilisant si possible le nom
# officiel du cabinet tel que declare au barreau de Geneve pour la meme entite.
_domain_name_votes = {}
for _r in GE_INDIVIDUALS:
    _d = site_domain(_r.get("site_web"))
    _e = (_r.get("etude") or "").strip()
    if _d and _e:
        _domain_name_votes.setdefault(_d, Counter())[_e] += 1
GE_DOMAIN_NAMES = {d: votes.most_common(1)[0][0] for d, votes in _domain_name_votes.items()}


def pretty_name_from_domain(domain):
    """Nom lisible derive du nom de domaine, utilise uniquement quand aucun nom
    officiel n'est connu (ni via le registre de Geneve, ni via l'enrichissement
    web). Pur formatage -- aucune information inventee, juste une mise en forme
    lisible du domaine deja fourni par l'avocat lui-meme."""
    base = domain.split(".")[0]
    words = re.split(r"[-_]+", base)
    return " ".join(w.capitalize() for w in words if w)


# Fournisseurs email generalistes/grand public : jamais un nom de cabinet meme
# quand plusieurs avocats les partagent (cas reel constate a Fribourg avec
# bluewin.ch et gmail.com). Les regrouper comme "cabinet" serait une
# fabrication -- ce ne sont que des avocats independants qui partagent un
# hebergeur mail, pas une structure commune.
GENERIC_EMAIL_DOMAINS = {
    "bluewin.ch", "gmail.com", "hotmail.com", "hotmail.ch", "outlook.com",
    "outlook.ch", "yahoo.com", "yahoo.fr", "yahoo.de", "gmx.ch", "gmx.net",
    "gmx.de", "sunrise.ch", "icloud.com", "me.com", "mac.com", "live.com",
    "msn.com", "aol.com", "protonmail.com", "swissonline.ch", "tele2.ch",
    "vtxnet.ch", "freesurf.ch", "bluemail.ch", "bluewin.com", "citycable.ch",
    "hispeed.ch", "web.de", "t-online.de", "libero.it", "alice.it",
}


def email_domain(email):
    e = (email or "").strip().lower()
    if "@" not in e:
        return None
    d = e.rsplit("@", 1)[-1].strip()
    return d or None


def derive_domain_firms(individuals, existing_slugs=None, domain_fn=None, excluded_domains=None):
    """Regroupe par nom de domaine les avocats sans nom d'etude en texte libre.
    Cas d'origine : Vaud, domaine tire du site_web. Generalise pour Fribourg,
    domaine tire de l'email (pas de site_web dans ce registre, mais l'email
    professionnel contient presque toujours le domaine du cabinet -- meme
    principe, source differente). Seuil : au moins 2 avocats partageant le
    meme domaine, OU un seul si ce domaine est deja confirme comme cabinet reel
    via le registre de Geneve ou le cache d'enrichissement web (source externe
    qui etablit deja la realite du cabinet). Les domaines de fournisseurs mail
    grand public (excluded_domains) ne sont jamais traites comme un cabinet,
    quel que soit le nombre d'avocats qui les partagent. Rien n'est jamais
    fabrique : le nom vient du registre officiel quand connu, sinon d'un
    simple formatage du domaine deja declare par l'avocat."""
    domain_fn = domain_fn or (lambda r: site_domain(r.get("site_web")))
    excluded = excluded_domains or set()
    seen_slugs = dict(existing_slugs or {})
    by_domain = {}
    for r in individuals:
        if (r.get("etude") or "").strip():
            continue
        d = domain_fn(r)
        if not d or d in excluded:
            continue
        by_domain.setdefault(d, []).append(r)

    firms = []
    for d, members in sorted(by_domain.items(), key=lambda kv: -len(kv[1])):
        confirmed_external = d in GE_DOMAIN_NAMES or d in WEB_ENRICHMENT
        if len(members) < 2 and not confirmed_external:
            continue
        name = GE_DOMAIN_NAMES.get(d) or pretty_name_from_domain(d)
        for m in members:
            m["etude"] = name
        base = slugify(name)
        n = seen_slugs.get(base, 0)
        seen_slugs[base] = n + 1
        firms.append({"etude": name, "members": members, "ville": members[0]["ville"],
                       "_slug": base if n == 0 else f"{base}-{n+1}"})
    return firms


CANTON_COUNTS = other_canton_counts()
CANTON_COUNTS["GE"] = len(GE_INDIVIDUALS)


def ge_registry(lang):
    """Registre principal : etudes + avocats sans etude, trie alphabetiquement.
    C'est la seule liste browsable exposee aux utilisateurs (pas la liste brute
    des 2895 avocats individuels, qui reste generee pour le SEO mais accessible
    uniquement via les fiches etude / avocats sans etude / maillage interne)."""
    rows = []
    for f in GE_FIRMS:
        n = len(MEMBERS_BY_FIRM_NORM.get(norm(f["etude"]), [])) or int(f.get("nb_avocats") or 0)
        rows.append({
            "type": "etude", "nom": f["etude"], "url": etude_path("GE", f["_slug"], lang),
            "ville": f.get("ville", ""), "n_membres": n,
        })
    for r in SOLO_LAWYERS:
        rows.append({
            "type": "avocat", "nom": r["nom_complet"].title(), "url": avocat_path("GE", r["_slug"], lang),
            "ville": r.get("ville", ""), "role": r.get("fonction", ""),
        })
    rows.sort(key=lambda x: x["nom"])
    return rows
print(f"{len(GE_INDIVIDUALS)} avocats, {len(GE_FIRMS)} etudes charges.", file=sys.stderr)


OG_LOCALES = {"fr": "fr_CH", "de": "de_CH", "it": "it_CH", "en": "en_US"}


def render(template_name, ctx):
    ctx.setdefault("noindex", False)
    ctx.setdefault("og_locale", OG_LOCALES.get(ctx.get("lang"), "fr_CH"))
    extra = list(ctx.get("extra_schema") or [])
    bc = ctx.get("breadcrumb")
    if bc:
        items = [
            {"@type": "ListItem", "position": i + 1, "name": label,
             "item": url if url.startswith("http") else BASE_DOMAIN + url}
            for i, (label, url) in enumerate(bc)
        ]
        extra.append(json.dumps({
            "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items,
        }, ensure_ascii=False))
    reg = ctx.get("registry")
    if reg:
        list_items = [
            {"@type": "ListItem", "position": i + 1, "name": r.get("nom", ""),
             "url": r["url"] if r["url"].startswith("http") else BASE_DOMAIN + r["url"]}
            for i, r in enumerate(reg[:60]) if r.get("url") and r.get("nom")
        ]
        if list_items:
            extra.append(json.dumps({
                "@context": "https://schema.org", "@type": "ItemList",
                "itemListElement": list_items, "numberOfItems": len(reg),
            }, ensure_ascii=False))
    ctx["extra_schema"] = extra
    return env.get_template(template_name).render(**ctx)


# ---------------------------------------------------------------- pages

def gen_home():
    for lang in LANGS:
        path = home_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['site_name']} | {i18n.UI[lang]['tagline']}",
                        i18n.UI[lang]["tagline"] + ". " + pt.canton_intro(lang, i18n.CANTONS["GE"][lang]["name"], CANTON_COUNTS["GE"]),
                        hreflang_for(home_path))
        ctx["intro_text"] = i18n.UI[lang]["tagline"] + "."
        ctx["search_url"] = f"/{lang}/{seg('recherche', lang)}/"
        ctx["schema"] = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization", "name": "Legatis", "url": BASE_DOMAIN,
                    "description": i18n.UI[lang]["tagline"],
                },
                {
                    "@type": "WebSite", "name": "Legatis", "url": BASE_DOMAIN,
                    "inLanguage": lang,
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": f"{BASE_DOMAIN}{ctx['search_url']}?q={{search_term_string}}",
                        "query-input": "required name=search_term_string",
                    },
                },
            ],
        }, ensure_ascii=False)
        ctx["stats"] = {
            "total_avocats": sum(v for v in CANTON_COUNTS.values() if v),
            "total_cantons": len(i18n.CANTONS),
            "total_etudes": len(GE_FIRMS) + sum(len(d["firms"]) for d in CANTON_DATA.values()),
            "total_domaines": len(i18n.DOMAINES),
        }
        ctx["cantons"] = [
            {"code": c, "name": i18n.CANTONS[c][lang]["name"], "url": canton_path(c, lang), "count": CANTON_COUNTS.get(c, 0)}
            for c in i18n.CANTONS
        ]
        ctx["domaines"] = [
            {"id": d, "name": i18n.DOMAINES[d][lang]["name"], "url": domaine_path(d, lang)} for d in i18n.DOMAINES
        ]
        ctx["cross_url_matrix"] = {
            c: {d: cross_path(c, d, lang) for d in i18n.DOMAINES} for c in i18n.CANTONS
        }
        # Domaines reellement pourvus d'avocats par canton, pour filtrer le
        # selecteur "domaine" du wizard une fois le canton choisi. Seul GE
        # dispose aujourd'hui d'un champ "domaines" (specialites FSA) par
        # avocat dans la source de donnees -> seul GE peut etre filtre sur
        # des donnees reelles. Pour les autres cantons (pas encore de donnee
        # de specialite par avocat), on garde tous les domaines disponibles
        # plutot que de vider le selecteur, ce qui casserait le wizard.
        ctx["cross_available_domains"] = {
            c: (sorted(GE_BY_DOMAINE.keys()) if c == "GE" else list(i18n.DOMAINES.keys()))
            for c in i18n.CANTONS
        }
        ctx["etude_aj_url"] = etude_aj_path(lang)
        write_page(path, render("home.html", ctx))


def gen_indexes():
    for lang in LANGS:
        path = cantons_index_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['all_cantons']} | Legatis", i18n.UI[lang]["tagline"] + ".",
                        hreflang_for(cantons_index_path))
        ctx["cantons"] = [
            {"name": i18n.CANTONS[c][lang]["name"], "url": canton_path(c, lang), "count": CANTON_COUNTS.get(c, 0)}
            for c in i18n.CANTONS
        ]
        ctx["cantons_a_venir"] = [
            {"name": i18n.CANTONS_A_VENIR[c][lang]["name"], "url": f"/{lang}/{seg('avocats', lang)}/{i18n.CANTONS_A_VENIR[c][lang]['slug']}/"}
            for c in i18n.CANTONS_A_VENIR
        ]
        write_page(path, render("cantons_index.html", ctx))

        path = domaines_index_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['all_practice_areas']} | Legatis", i18n.UI[lang]["tagline"] + ".",
                        hreflang_for(domaines_index_path))
        ctx["domaines"] = [
            {"name": i18n.DOMAINES[d][lang]["name"], "url": domaine_path(d, lang)} for d in i18n.DOMAINES
        ]
        write_page(path, render("domaines_index.html", ctx))


def gen_coming_soon():
    for code in i18n.CANTONS_A_VENIR:
        for lang in LANGS:
            name = i18n.CANTONS_A_VENIR[code][lang]["name"]
            slug = i18n.CANTONS_A_VENIR[code][lang]["slug"]
            path = f"/{lang}/{seg('avocats', lang)}/{slug}/"
            ctx = base_ctx(lang, path, f"{i18n.UI[lang]['find_a_lawyer_near']} {name} | Legatis",
                            i18n.UI[lang]["coming_soon_text"],
                            {lg: f"/{lg}/{seg('avocats', lg)}/{i18n.CANTONS_A_VENIR[code][lg]['slug']}/" for lg in LANGS})
            ctx["canton_name"] = name
            ctx["noindex"] = True
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (i18n.UI[lang]["all_cantons"], cantons_index_path(lang)),
                                  (name, path)]
            write_page(path, render("coming_soon.html", ctx))


def domaines_for_lawyer(row):
    raw = (row.get("domaines") or "").strip()
    if not raw:
        return []
    parts = [p.strip() for p in re.split(r"[;,|]", raw) if p.strip()]
    out = []
    for p in parts:
        did = i18n.FSA_TO_DOMAINE.get(p)
        if did:
            out.append(did)
    return list(dict.fromkeys(out))


BY_CITY = {}
for _r in GE_INDIVIDUALS:
    BY_CITY.setdefault(_r["ville"], []).append(_r)

GE_BY_DOMAINE = {}
for _r in GE_INDIVIDUALS:
    for _did in domaines_for_lawyer(_r):
        GE_BY_DOMAINE.setdefault(_did, []).append(_r)

# Fiche de test dediee au compte avocat de demonstration (voir demande de
# Greg le 20/08/2026) -- ajoutee ICI, apres SOLO_LAWYERS/BY_CITY/GE_BY_DOMAINE/
# CANTON_COUNTS/MEMBERS_BY_FIRM_NORM (tous deja calcules ci-dessus a partir de
# GE_INDIVIDUALS), afin qu'elle n'apparaisse JAMAIS dans l'annuaire visible
# (ge_registry), les suggestions "pres de chez vous" (BY_CITY) ni les
# compteurs affiches publiquement. Elle reste en revanche presente dans
# GE_INDIVIDUALS pour les etapes qui en ont reellement besoin et qui relisent
# GE_INDIVIDUALS a l'execution (pas a l'import) : sa propre fiche (gen_ge_avocats,
# forcee noindex plus bas), data/verification_contacts.json et
# search-index-{lang}.json (gen_verification_contacts/gen_search) -- c'est ce
# qui permet de la retrouver via "Trouvez votre fiche" sur /verifier-mon-identite/
# pour tester le parcours de creation de compte sans jamais toucher a une
# vraie fiche de professionnel. Email/telephone = ceux de Greg (memes valeurs
# que gregoiregiuliano@hotmail.com utilise ailleurs comme contact reel) : les
# 3 paliers de verification (email, telephone, document) sont donc tous
# testables -- le lien de confirmation email et l'appel du palier telephone
# arrivent chez lui. A retirer (une seule ligne) le jour ou ce compte de test
# n'est plus necessaire.
GE_INDIVIDUALS.append({
    "nom_complet": "Compte Test Legatis", "fonction": "Avocat", "etude": "",
    "adresse": "Rue de Test 1", "npa": "1200", "ville": "Genève", "telephone": "+32 493 33 28 62",
    "canton": "GE", "email": "gregoiregiuliano@hotmail.com", "site_web": "", "domaines": "", "langues": "Français",
    "brevet_date": "2020", "brevet_pays": "Suisse", "source_email": "test-fixture",
    "_slug": "compte-test-legatis",
})
TEST_LAWYER_SLUG = "compte-test-legatis"


def clean_city_for_title(ville):
    """Garde-fou pour le <title> des fiches avocat (fix CTR : afficher la ville
    plutot que le canton dans le titre, mot-cle local le plus utile en resultat
    de recherche). Quelques lignes source ont, au lieu d'un nom de ville simple,
    une adresse postale complete/etrangere dans le champ ville (code postal,
    pays, parentheses -- ex: "Montreal (Quebec) H4Z 1B7 CANADA"). Un tel titre
    a l'air casse/spam en resultat Google -- on retombe alors sur le nom du
    canton (comportement d'avant ce fix), jamais sur une valeur brute suspecte."""
    v = (ville or "").strip()
    if not v or len(v) > 28 or "(" in v or ")" in v or any(ch.isdigit() for ch in v):
        return None
    return v


def primary_phone(raw):
    """Le champ telephone du registre GE (avocats et etudes) concatene parfois
    deux numeros sans separateur (tel + fax) -- ex. "022 818 50 52 022 310 93 88".
    Ne garde que le premier numero pour les liens tel: et les donnees structurees.
    Ne touche pas aux formats a un seul numero (avec ou sans +41/parentheses)."""
    raw = (raw or "").strip()
    if not raw:
        return ""
    tokens = raw.split()
    if len(tokens) >= 8 and len(tokens) % 4 == 0 and all(t.isdigit() for t in tokens):
        return " ".join(tokens[:len(tokens) // 2])
    return raw


def gen_ge_avocats(start=0, count=None, rows=None):
    canton_name_fr = i18n.CANTONS["GE"]["fr"]["name"]
    subset = rows if rows is not None else (GE_INDIVIDUALS[start:start + count] if count else GE_INDIVIDUALS[start:])
    for row in subset:
        nom = row["nom_complet"].title()
        firm_row = FIRM_BY_NORM.get(norm(row.get("etude", "")))
        domaine_ids = domaines_for_lawyer(row)
        same_city = [r for r in BY_CITY.get(row["ville"], []) if r["_slug"] != row["_slug"]][:6]
        for lang in LANGS:
            canton_name = i18n.CANTONS["GE"][lang]["name"]
            path = avocat_path("GE", row["_slug"], lang)
            # Signaux reels calcules ici (avant desc/title/presentation) pour
            # differencier les fiches sans domaines de competence renseignes
            # (title = ville plutot que canton -> mot-cle local le plus utile
            # dans le titre ; langues/anciennete injectees dans la description
            # quand domaines est vide -- voir presentation_text.lawyer_presentation).
            _raw_langues = [l.strip() for l in (row.get("langues") or "").split(";") if l.strip()]
            _langues_for_lang = pt.translate_langues(_raw_langues, lang)
            desc = pt.lawyer_presentation(lang, nom, canton_name, etude=row.get("etude") or None,
                                           ville=row.get("ville") or None,
                                           domaines=[i18n.DOMAINES[d][lang]["name"] for d in domaine_ids],
                                           fonction=row.get("fonction") or None,
                                           langues=_langues_for_lang,
                                           seniority_year=row.get("brevet_date"))
            _title_place = clean_city_for_title(row.get("ville")) or canton_name
            title = f"{nom} | {i18n.UI[lang]['find_a_lawyer_near']} {_title_place} | Legatis"
            ctx = base_ctx(lang, path, title, desc,
                            {lg: BASE_DOMAIN + avocat_path("GE", row["_slug"], lg) for lg in LANGS})
            ctx["noindex"] = (row["_slug"] == TEST_LAWYER_SLUG)
            ctx["nom"] = nom
            ctx["canton_name"] = canton_name
            ctx["review_canton_code"] = "GE"
            ctx["review_avocat_slug"] = row["_slug"]
            ctx["role_or_titre"] = row.get("fonction") or ""
            ctx["etude"] = row.get("etude") or ""
            ctx["etude_url"] = etude_path("GE", firm_row["_slug"], lang) if firm_row else None
            ctx["adresse"] = row.get("adresse") or ""
            ctx["npa"] = row.get("npa") or ""
            ctx["ville"] = row.get("ville") or ""
            ctx["telephone"] = primary_phone(row.get("telephone"))
            ctx["email"] = row.get("email") or ""
            ctx["site_web"] = row.get("site_web") or ""
            ctx["site_web_href"] = row.get("site_web") or "#"
            ctx["presentation"] = pt.lawyer_presentation(lang, nom, canton_name, etude=row.get("etude") or None,
                                                           ville=row.get("ville") or None,
                                                           domaines=[i18n.DOMAINES[d][lang]["name"] for d in domaine_ids],
                                                           fonction=row.get("fonction") or None)
            ctx["domaines"] = [{"name": i18n.DOMAINES[d][lang]["name"], "url": domaine_path(d, lang)} for d in domaine_ids]
            ctx["nearby_title"] = f"{i18n.UI[lang]['find_a_lawyer_near']} {row.get('ville','')}" if lang != "de" else f"Weitere Anwältinnen und Anwälte in {row.get('ville','')}"
            ctx["nearby"] = [
                {"nom": r["nom_complet"].title(), "url": avocat_path("GE", r["_slug"], lang),
                 "etude": r.get("etude", ""), "ville": r.get("ville", "")}
                for r in same_city
            ]
            ctx["langues"] = _langues_for_lang
            ctx["seniority_text"] = pt.seniority_text(lang, row.get("brevet_date"))
            _city_link = city_link_for("GE", row.get("ville"), lang)
            ctx["ville_url"] = _city_link[1] if _city_link else None
            _bc = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (canton_name, canton_path("GE", lang))]
            if _city_link:
                _bc.append(_city_link)
            _bc.append((nom, path))
            ctx["breadcrumb"] = _bc
            _schema = {
                "@context": "https://schema.org", "@type": "Attorney", "name": nom,
                "url": BASE_DOMAIN + path,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": primary_phone(row.get("telephone")), "email": row.get("email", ""),
                "areaServed": canton_name,
            }
            if row.get("site_web"):
                _schema["sameAs"] = [row["site_web"]]
            _rating = attorney_rating_schema("GE", row["_slug"])
            if _rating:
                _schema["aggregateRating"] = _rating
            if _raw_langues:
                _lang_map = {"français": "fr", "allemand": "de", "italien": "it", "anglais": "en",
                             "espagnol": "es", "portugais": "pt", "arabe": "ar", "russe": "ru",
                             "romanche": "rm"}
                _codes = [_lang_map.get(l.lower()) for l in _raw_langues]
                _schema["knowsLanguage"] = [c for c in _codes if c] or _raw_langues
            ctx["schema"] = json.dumps(_schema, ensure_ascii=False)
            write_page(path, render("avocat.html", ctx))


def gen_ge_etudes(start=0, count=None, rows=None):
    subset = rows if rows is not None else (GE_FIRMS[start:start + count] if count else GE_FIRMS[start:])
    for row in subset:
        nom_etude = row["etude"]
        matched = MEMBERS_BY_FIRM_NORM.get(norm(nom_etude), [])
        n = len(matched) if matched else int(row.get("nb_avocats") or 0)
        _team_langues = []
        for m in matched:
            for l in (m.get("langues") or "").split(";"):
                l = l.strip()
                if l and l not in _team_langues:
                    _team_langues.append(l)
        _team_domaine_ids = []
        for m in matched:
            for did in domaines_for_lawyer(m):
                if did not in _team_domaine_ids:
                    _team_domaine_ids.append(did)
        _years = []
        for m in matched:
            try:
                _years.append(int(str(m.get("brevet_date") or "")[:4]))
            except ValueError:
                pass
        _oldest_year = min(_years) if _years else None
        _site_url = next((m.get("site_web") for m in matched if m.get("site_web")), "")
        _web = WEB_ENRICHMENT.get(site_domain(_site_url)) if _site_url else None
        # Noindex decide une seule fois pour les 4 langues (jamais indexee dans
        # une langue et pas dans une autre) : voir commentaire complet plus bas.
        _any_lang_lacks_signal = False
        for _lg in LANGS:
            _dn = [i18n.DOMAINES[d][_lg]["name"] for d in _team_domaine_ids] or web_practice_areas(_web, _lg)
            if not pt.firm_insight(_lg, pt.translate_langues(_team_langues, _lg), _dn, _oldest_year,
                                    founding_year=(_web or {}).get("founding_year"),
                                    team_size_n=(_web or {}).get("team_size_n")):
                _any_lang_lacks_signal = True
                break
        for lang in LANGS:
            canton_name = i18n.CANTONS["GE"][lang]["name"]
            path = etude_path("GE", row["_slug"], lang)
            desc = pt.firm_presentation(lang, nom_etude, canton_name, ville=row.get("ville"), n_membres=n)
            _ville = row.get("ville") or ""
            _loc = f"{_ville}, {canton_name}" if _ville and _ville.lower() != canton_name.lower() else canton_name
            _title = f"{nom_etude} | {i18n.UI[lang]['firm']} {i18n.UI[lang]['in']} {_loc} | Legatis"
            ctx = base_ctx(lang, path, _title, desc,
                            {lg: BASE_DOMAIN + etude_path("GE", row["_slug"], lg) for lg in LANGS})
            ctx["nom_etude"] = nom_etude
            ctx["canton_name"] = canton_name
            ctx["adresse"] = row.get("adresse", "")
            ctx["npa"] = row.get("npa", "")
            ctx["ville"] = row.get("ville", "")
            ctx["telephone"] = primary_phone(row.get("telephone"))
            ctx["site_web"] = _site_url or ""
            ctx["site_web_href"] = _site_url or "#"
            ctx["presentation"] = pt.firm_presentation(lang, nom_etude, canton_name, ville=row.get("ville"), n_membres=n)
            ctx["members_title"] = (
                {"fr": "Avocats de l'étude", "de": "Anwältinnen und Anwälte der Kanzlei",
                 "it": "Avvocati dello studio", "en": "Lawyers at this firm"}[lang])
            if matched:
                ctx["membres"] = [
                    {"nom": m["nom_complet"].title(), "role": m.get("fonction", ""),
                     "url": avocat_path("GE", m["_slug"], lang)}
                    for m in sorted(matched, key=lambda m: m["nom_complet"])
                ]
            else:
                fallback_members = []
                for mtxt in row["_members"][:200]:
                    mm = re.match(r"^(.*?)\s*\((.*?)\)\s*$", mtxt)
                    if mm:
                        fallback_members.append({"nom": mm.group(1).title(), "fonction": mm.group(2)})
                    else:
                        fallback_members.append({"nom": mtxt.title(), "fonction": ""})
                ctx["membres"] = [{"nom": m["nom"], "role": m["fonction"],
                                    "url": None} for m in fallback_members]
            _domaine_names = [i18n.DOMAINES[d][lang]["name"] for d in _team_domaine_ids]
            if not _domaine_names:
                _domaine_names = web_practice_areas(_web, lang)
            ctx["insight_text"] = pt.firm_insight(
                lang, pt.translate_langues(_team_langues, lang), _domaine_names, _oldest_year,
                founding_year=(_web or {}).get("founding_year"),
                team_size_n=(_web or {}).get("team_size_n"),
            )
            # Noindex automatique : la fiche n'a aucun signal reel au-dela du nom/adresse/
            # liste de membres (ni annee de fondation, ni taille d'equipe, ni langues, ni
            # domaines de competence). Se retire tout seul au prochain build des qu'une
            # donnee reelle arrive (registre ou enrichissement web) -- rien a faire a la main.
            # Decide une seule fois pour les 4 langues (_any_lang_lacks_signal calcule
            # plus haut) : jamais indexee dans une langue et noindex dans une autre pour
            # la meme fiche (cf. retour utilisateur du 2026-08-23).
            ctx["noindex"] = _any_lang_lacks_signal
            ctx["web_source_note"] = None
            if _web:
                ctx["web_source_note"] = {
                    "fr": f"Certaines informations ci-dessus proviennent du site officiel du cabinet, consulté le {_web['fetched_date']}.",
                    "de": f"Einige der obigen Angaben stammen von der offiziellen Website der Kanzlei, abgerufen am {_web['fetched_date']}.",
                    "it": f"Alcune informazioni sopra riportate provengono dal sito ufficiale dello studio, consultato il {_web['fetched_date']}.",
                    "en": f"Some information above comes from the firm's official website, accessed on {_web['fetched_date']}.",
                }[lang]
            _city_link = city_link_for("GE", row.get("ville"), lang)
            ctx["ville_url"] = _city_link[1] if _city_link else None
            _bc = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (canton_name, canton_path("GE", lang))]
            if _city_link:
                _bc.append(_city_link)
            _bc.append((nom_etude, path))
            ctx["breadcrumb"] = _bc
            _schema = {
                "@context": "https://schema.org", "@type": "LegalService", "name": nom_etude,
                "url": BASE_DOMAIN + path,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": primary_phone(row.get("telephone")),
            }
            if _site_url:
                _schema["sameAs"] = [_site_url]
            if _team_langues:
                _lang_map = {"français": "fr", "allemand": "de", "italien": "it", "anglais": "en",
                             "espagnol": "es", "portugais": "pt", "arabe": "ar", "russe": "ru",
                             "romanche": "rm"}
                _codes = [_lang_map.get(l.lower()) for l in _team_langues]
                _schema["knowsLanguage"] = [c for c in _codes if c] or _team_langues
            ctx["schema"] = json.dumps(_schema, ensure_ascii=False)
            write_page(path, render("etude.html", ctx))


def top_city(individuals):
    from collections import Counter
    c = Counter(r["ville"] for r in individuals if r.get("ville"))
    if not c:
        return None, 0
    city, n = c.most_common(1)[0]
    return city, n


def canton_insight(lang, top_city_name, top_city_n, total, n_solo):
    if not top_city_name or not total:
        return ""
    pct_indep = round(100 * n_solo / total)
    if pct_indep == 0:
        indep_fr = "Tous les avocats référencés sont rattachés à une étude dans le registre."
        indep_de = "Alle erfassten Anwältinnen und Anwälte sind im Register einer Kanzlei zugeordnet."
        indep_it = "Tutti gli avvocati registrati sono associati a uno studio nel registro."
        indep_en = "All listed lawyers are affiliated with a firm in the register."
    elif pct_indep == 100:
        indep_fr = "Aucun n'est rattaché à une étude déclarée dans le registre."
        indep_de = "Keiner ist im Register einer Kanzlei zugeordnet."
        indep_it = "Nessuno è associato a uno studio dichiarato nel registro."
        indep_en = "None are affiliated with a firm declared in the register."
    else:
        indep_fr = f"Environ {pct_indep}% des avocats référencés exercent sans étude déclarée dans le registre."
        indep_de = f"Rund {pct_indep}% der erfassten Anwältinnen und Anwälte üben ohne im Register angegebene Kanzlei aus."
        indep_it = f"Circa il {pct_indep}% degli avvocati registrati esercita senza uno studio dichiarato nel registro."
        indep_en = f"About {pct_indep}% of listed lawyers practise without a firm declared in the register."
    if lang == "fr":
        return (f"{top_city_name} concentre le plus grand nombre d'avocats référencés du canton "
                f"({top_city_n} sur {total}). {indep_fr}")
    if lang == "de":
        return (f"{top_city_name} verzeichnet die meisten im Kanton erfassten Anwältinnen und Anwälte "
                f"({top_city_n} von {total}). {indep_de}")
    if lang == "it":
        return (f"{top_city_name} concentra il maggior numero di avvocati registrati del cantone "
                f"({top_city_n} su {total}). {indep_it}")
    return (f"{top_city_name} has the highest concentration of registered lawyers in the canton "
            f"({top_city_n} out of {total}). {indep_en}")


def gen_canton_hub_ge():
    for lang in LANGS:
        canton_name = i18n.CANTONS["GE"][lang]["name"]
        path = canton_path("GE", lang)
        desc = pt.canton_intro(lang, canton_name, CANTON_COUNTS["GE"])
        _title = (f"{canton_name} : {i18n.UI[lang]['find_a_lawyer']} | "
                  f"{CANTON_COUNTS['GE']} {LAWYER_WORD[lang]} | Legatis")
        ctx = base_ctx(lang, path, _title, desc,
                        {lg: BASE_DOMAIN + canton_path("GE", lg) for lg in LANGS})
        ctx["canton_name"] = canton_name
        ctx["intro_text"] = pt.canton_intro(lang, canton_name, CANTON_COUNTS["GE"])
        _tc_name, _tc_n = top_city(GE_INDIVIDUALS)
        ctx["insight_text"] = canton_insight(lang, _tc_name, _tc_n, len(GE_INDIVIDUALS), len(SOLO_LAWYERS))
        ctx["domaines"] = [{"name": i18n.DOMAINES[d][lang]["name"], "url": cross_path("GE", d, lang),
                             "has_data": bool(GE_BY_DOMAINE.get(d))}
                            for d in i18n.DOMAINES]
        registry = ge_registry(lang)
        ctx["stats_label"] = {
            "fr": f"{len(GE_FIRMS)} études · {len(SOLO_LAWYERS)} avocats indépendants référencés",
            "de": f"{len(GE_FIRMS)} Kanzleien · {len(SOLO_LAWYERS)} unabhängige Anwältinnen und Anwälte erfasst",
            "it": f"{len(GE_FIRMS)} studi legali · {len(SOLO_LAWYERS)} avvocati indipendenti registrati",
            "en": f"{len(GE_FIRMS)} firms · {len(SOLO_LAWYERS)} independent lawyers listed",
        }[lang]
        ctx["registry"] = registry
        ctx["has_more"] = False
        ctx["more_text"] = ""
        ctx["villes"] = canton_villes_links("GE", lang)
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                              (i18n.UI[lang]["all_cantons"], cantons_index_path(lang)), (canton_name, path)]
        write_page(path, render("canton_hub.html", ctx))


def gen_domain_hubs():
    for did in i18n.DOMAINES:
        for lang in LANGS:
            dname = i18n.DOMAINES[did][lang]["name"]
            path = domaine_path(did, lang)
            desc = pt.domaine_intro(lang, dname)
            _title = (f"{dname} | {i18n.UI[lang]['find_a_lawyer']} {COUNTRY_PREP[lang]} "
                      f"{COUNTRY_NAME[lang]} | Legatis")
            ctx = base_ctx(lang, path, _title, desc,
                            {lg: BASE_DOMAIN + domaine_path(did, lg) for lg in LANGS})
            ctx["domaine_name"] = dname
            ctx["intro_text"] = pt.domaine_intro(lang, dname)
            ctx["cantons"] = [
                {"name": i18n.CANTONS[c][lang]["name"], "url": cross_path(c, did, lang)} for c in i18n.CANTONS
            ]
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (i18n.UI[lang]["all_practice_areas"], domaines_index_path(lang)), (dname, path)]
            write_page(path, render("domain_hub.html", ctx))


def gen_cross_ge():
    fallback_by_lang = {lang: ge_registry(lang)[:40] for lang in LANGS}
    for did in i18n.DOMAINES:
        matches = GE_BY_DOMAINE.get(did, [])
        for lang in LANGS:
            canton_name = i18n.CANTONS["GE"][lang]["name"]
            dname = i18n.DOMAINES[did][lang]["name"]
            path = cross_path("GE", did, lang)
            desc = pt.cross_intro(lang, dname, canton_name)
            _title = (f"{dname} {i18n.UI[lang]['in']} {canton_name} | "
                      f"{i18n.UI[lang]['find_a_lawyer']} | Legatis")
            ctx = base_ctx(lang, path, _title, desc,
                            {lg: BASE_DOMAIN + cross_path("GE", did, lg) for lg in LANGS})
            ctx["domaine_name"] = dname
            ctx["canton_name"] = canton_name
            ctx["h1"] = pt.cross_h1(lang, dname, canton_name)
            ctx["intro_text"] = pt.cross_intro(lang, dname, canton_name)
            ctx["avocats"] = [
                {"nom": r["nom_complet"].title(), "url": avocat_path("GE", r["_slug"], lang),
                 "etude": r.get("etude", ""), "ville": r.get("ville", ""), "role": r.get("fonction", "")}
                for r in matches
            ]
            ctx["registry"] = ctx["avocats"]
            ctx["list_title"] = i18n.UI[lang]["all_practice_areas"]
            ctx["no_specialty_text"] = pt.cross_fallback_text(lang, dname, canton_name)
            ctx["fallback_avocats"] = fallback_by_lang[lang]
            ctx["noindex"] = not matches
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path("GE", lang)), (dname, path)]
            write_page(path, render("cross.html", ctx))


# ---------------------------------------------------------------- autres cantons (generique)

TITLE_ONLY_RE = re.compile(
    r"^(dr\.?|lic\.?\s*iur\.?|mlaw|ll\.?m\.?|prof\.?|mag\.?\s*iur\.?|me|fürsprecher(in)?|"
    r"rechtsanwalt|rechtsanwältin|avocate?)\.?$",
    re.IGNORECASE,
)


def split_firm_address(text):
    """Heuristique pour separer nom d'etude/prenom et adresse dans un champ combine
    (ex: Lucerne 'etude_adresse', Soleure 'reste_nom_prenom_adresse')."""
    m = re.search(
        r"^(.*?)\s*([A-ZÄÖÜ][\wäöüÄÖÜß.\'’\-]*\.?\s*\d+[a-zA-Z]?.*)$",
        text,
    )
    if m:
        first, rest = m.group(1).strip(" ,-"), m.group(2).strip()
        if TITLE_ONLY_RE.match(first):
            return "", (first + " " + rest).strip() if first else rest
        return first, rest
    return "", text.strip()


CANTON_FILES = {
    "AG": "avocats_argovie.csv", "AI": "avocats_appenzell_rhodes_interieures.csv",
    "BS": "avocats_bale_ville.csv", "FR": "avocats_fribourg.csv",
    "GL": "avocats_glaris.csv", "GR": "avocats_grisons.csv", "JU": "avocats_jura.csv",
    "LU": "avocats_lucerne.csv", "NE": "avocats_neuchatel.csv", "NW": "avocats_nidwald.csv",
    "OW": "avocats_obwald.csv", "SG": "avocats_saint_gall.csv", "SO": "avocats_soleure.csv",
    "SZ": "avocats_schwyz.csv", "TG": "avocats_thurgovie.csv", "UR": "avocats_uri.csv",
    "VD": "avocats_vaud.csv", "ZG": "avocats_zoug.csv", "ZH": "avocats_zurich.csv",
    # Ajoutes le 29/07/2026 : registres officiels decouverts accessibles (voir
    # data/ENRICHISSEMENT_PROGRESS.md). TI : import initial partiel (70/904 --
    # pagination du registre cantonal, le reste suit via la tache planifiee).
    # BL, AR, SH : import complet en un seul passage (pages statiques uniques).
    "TI": "avocats_tessin.csv", "BL": "avocats_bale_campagne.csv",
    "AR": "avocats_appenzell_rhodes_exterieures.csv", "SH": "avocats_schaffhouse.csv",
}


LANG_MARKER_RE = re.compile(r"\s*\((DE|FR|IT|EN)\)\s*$", re.IGNORECASE)
NPA_CITY_RE = re.compile(r"^(\d{4})\s+(.+)$")
TEST_JUNK_RE = re.compile(r"\btest\b", re.IGNORECASE)


def normalize_row(code, r):
    nom_complet = (r.get("nom_complet") or "").strip()
    if not nom_complet:
        prenom = (r.get("prenom") or "").strip()
        nom = (r.get("nom") or "").strip()
        nom_complet = f"{prenom} {nom}".strip()
    if TEST_JUNK_RE.search(nom_complet):
        return {
            "nom_complet": "", "fonction": "", "etude": "", "adresse": "", "npa": "",
            "ville": "", "telephone": "", "email": "", "site_web": "", "canton": code,
        }
    etude = (r.get("etude") or "").strip()
    adresse = (r.get("adresse") or "").strip()
    if code == "LU" and not etude and not adresse:
        etude, adresse = split_firm_address(r.get("etude_adresse", "") or "")
    if code == "SO" and not adresse:
        extra, adresse2 = split_firm_address(r.get("reste_nom_prenom_adresse", "") or "")
        if not adresse:
            adresse = adresse2
        if extra and nom_complet and " " not in nom_complet:
            nom_complet = f"{extra} {nom_complet}".strip()
    fonction = (r.get("profession") or r.get("titre") or r.get("titre_academique") or "").strip()
    fonction = LANG_MARKER_RE.sub("", fonction).strip()
    npa = (r.get("npa") or "").strip()
    ville = (r.get("ville") or "").strip()
    if npa in ("", "[]") or not npa.isdigit():
        m = NPA_CITY_RE.match(ville)
        if m:
            npa, ville = m.group(1), m.group(2)
        elif npa == "[]":
            npa = ""
    if ville == "[]":
        ville = ""
    telephone = (r.get("telephone") or "").strip()
    if telephone == "[]":
        telephone = ""
    email = (r.get("email") or "").strip()
    if email == "[]":
        email = ""
    site_web = (r.get("site_web") or "").strip()
    if site_web == "[]":
        site_web = ""
    annee_admission = ""
    date_insc = (r.get("date_inscription") or "").strip()
    if date_insc:
        parts = date_insc.split(".")
        if len(parts) == 3 and len(parts[-1]) == 4 and parts[-1].isdigit():
            annee_admission = parts[-1]
    # Domaines de competence / langues parlees : uniquement presents pour
    # Schaffhouse pour l'instant (texte brut, virgule-separe, tel que fourni
    # par le registre officiel de l'ordre cantonal -- jamais reformule).
    domaines_raw = (r.get("domaines") or "").strip()
    langues_raw = (r.get("langues") or "").strip()
    return {
        "nom_complet": nom_complet,
        "fonction": fonction,
        "etude": etude,
        "adresse": adresse,
        "npa": npa,
        "ville": ville,
        "telephone": telephone,
        "email": email,
        "site_web": site_web,
        "annee_admission": annee_admission,
        "domaines_raw": domaines_raw,
        "langues_raw": langues_raw,
        "canton": code,
    }


def load_canton(code):
    fname = CANTON_FILES.get(code)
    if not fname:
        return []
    path = os.path.join(DATA_DIR, fname)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))
    rows = [normalize_row(code, r) for r in raw_rows]
    rows = [r for r in rows if r["nom_complet"]]
    for r in rows:
        r["ville"] = clean_ville(r.get("ville", ""), r.get("npa", ""))
    seen_slugs = {}
    for r in rows:
        base = slugify(r["nom_complet"])
        n = seen_slugs.get(base, 0)
        seen_slugs[base] = n + 1
        r["_slug"] = base if n == 0 else f"{base}-{n+1}"
    return rows


def build_canton_firms(individuals):
    """Regroupe les avocats par etude (texte libre) au sein d'un canton.
    Ces cantons n'ont pas de fichier etudes deja construit comme Geneve :
    les etudes sont derivees directement du champ etude des avocats."""
    groups = {}
    for r in individuals:
        e = r["etude"].strip()
        if not e:
            continue
        key = norm(e)
        groups.setdefault(key, {"etude": e, "members": [], "ville": r["ville"]})
        groups[key]["members"].append(r)
    firms = list(groups.values())
    seen_slugs = {}
    for f in firms:
        base = slugify(f["etude"])
        n = seen_slugs.get(base, 0)
        seen_slugs[base] = n + 1
        f["_slug"] = base if n == 0 else f"{base}-{n+1}"
    return firms


OTHER_CANTON_CODES = list(CANTON_FILES.keys())
CANTON_DATA = {}
for _code in OTHER_CANTON_CODES:
    _individuals = load_canton(_code)
    _firms = build_canton_firms(_individuals)
    if _code == "VD":
        # Vaud n'a pas de champ "etude" source -- on derive le regroupement
        # depuis le domaine du site_web (voir derive_domain_firms plus haut).
        _existing_slugs = {f["_slug"]: 1 for f in _firms}
        _firms = _firms + derive_domain_firms(_individuals, existing_slugs=_existing_slugs)
    if _code == "FR":
        # Fribourg n'a ni champ "etude" ni "site_web", mais un champ email
        # rempli a 100% dont le domaine est presque toujours celui du cabinet
        # (ex. v.emery@emery-avocats.ch) -- meme mecanisme que Vaud, source
        # differente. Fournisseurs mail grand public exclus (voir
        # GENERIC_EMAIL_DOMAINS) pour ne jamais fabriquer un faux "cabinet".
        _existing_slugs = {f["_slug"]: 1 for f in _firms}
        _firms = _firms + derive_domain_firms(
            _individuals, existing_slugs=_existing_slugs,
            domain_fn=lambda r: email_domain(r.get("email")),
            excluded_domains=GENERIC_EMAIL_DOMAINS,
        )
    _solo = [r for r in _individuals if not r["etude"].strip()]
    CANTON_DATA[_code] = {
        "individuals": _individuals, "firms": _firms, "solo": _solo,
        "firm_by_norm": {norm(f["etude"]): f for f in _firms},
        "by_city": {},
    }
    for _r in _individuals:
        CANTON_DATA[_code]["by_city"].setdefault(_r["ville"], []).append(_r)
    CANTON_COUNTS[_code] = len(_individuals)
    print(f"{_code}: {len(_individuals)} avocats, {len(_firms)} etudes derivees, {len(_solo)} indep.", file=sys.stderr)


def attach_name_based_enrichment(canton_data, entries):
    """Rattache les entrees du cache de decouverte (autres cantons) aux etudes
    deja regroupees, par nom de cabinet -- ces CSV n'ont pas de site_web pour
    faire le lien par domaine comme WEB_ENRICHMENT. Garde-fou : si plusieurs
    etudes du meme canton partagent le meme nom "coeur" (collision), on
    n'attache rien -- mieux vaut aucun enrichissement qu'un rattachement
    ambigu a la mauvaise etude. Ecrit "_name_web" sur l'etude concernee.
    Retourne (nb_rattaches, nb_ignores_ambigus)."""
    attached = 0
    skipped_ambiguous = 0
    for code, data in canton_data.items():
        by_core = {}
        for f in data["firms"]:
            core = firm_core_name(f["etude"])
            if not core:
                continue
            by_core.setdefault(core, []).append(f)
        for entry in entries:
            if entry.get("canton") != code:
                continue
            core = firm_core_name(entry["firm_name"])
            candidates = by_core.get(core)
            if not candidates:
                continue
            if len(candidates) > 1:
                skipped_ambiguous += 1
                continue
            candidates[0]["_name_web"] = entry
            attached += 1
    return attached, skipped_ambiguous


_name_matches_attached, _name_matches_skipped_ambiguous = attach_name_based_enrichment(
    CANTON_DATA, OTHER_CANTON_ENRICHMENT
)
print(
    f"Cache decouverte autres cantons : {_name_matches_attached} etudes rattachees "
    f"par nom, {_name_matches_skipped_ambiguous} ignorees (collision de nom).",
    file=sys.stderr,
)


def canton_registry(code, lang):
    data = CANTON_DATA[code]
    rows = []
    for f in data["firms"]:
        rows.append({
            "type": "etude", "nom": f["etude"], "url": etude_path(code, f["_slug"], lang),
            "ville": f["ville"], "n_membres": len(f["members"]),
        })
    for r in data["solo"]:
        rows.append({
            "type": "avocat", "nom": r["nom_complet"].title(), "url": avocat_path(code, r["_slug"], lang),
            "ville": r["ville"], "role": r.get("fonction", ""),
        })
    rows.sort(key=lambda x: x["nom"])
    return rows


def gen_canton_hub(code):
    data = CANTON_DATA[code]
    n_total = len(data["individuals"])
    _tc_name, _tc_n = top_city(data["individuals"])
    for lang in LANGS:
        canton_name = i18n.CANTONS[code][lang]["name"]
        path = canton_path(code, lang)
        desc = pt.canton_intro(lang, canton_name, n_total)
        _title = (f"{canton_name} : {i18n.UI[lang]['find_a_lawyer']} | "
                  f"{n_total} {LAWYER_WORD[lang]} | Legatis")
        ctx = base_ctx(lang, path, _title, desc,
                        {lg: BASE_DOMAIN + canton_path(code, lg) for lg in LANGS})
        ctx["canton_name"] = canton_name
        ctx["intro_text"] = pt.canton_intro(lang, canton_name, n_total)
        ctx["insight_text"] = canton_insight(lang, _tc_name, _tc_n, n_total, len(data["solo"]))
        ctx["domaines"] = [{"name": i18n.DOMAINES[d][lang]["name"], "url": cross_path(code, d, lang), "has_data": False}
                            for d in i18n.DOMAINES]
        ctx["stats_label"] = {
            "fr": f"{len(data['firms'])} études · {len(data['solo'])} avocats indépendants référencés",
            "de": f"{len(data['firms'])} Kanzleien · {len(data['solo'])} unabhängige Anwältinnen und Anwälte erfasst",
            "it": f"{len(data['firms'])} studi legali · {len(data['solo'])} avvocati indipendenti registrati",
            "en": f"{len(data['firms'])} firms · {len(data['solo'])} independent lawyers listed",
        }[lang]
        ctx["registry"] = canton_registry(code, lang)
        ctx["has_more"] = False
        ctx["more_text"] = ""
        ctx["villes"] = canton_villes_links(code, lang)
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                              (i18n.UI[lang]["all_cantons"], cantons_index_path(lang)), (canton_name, path)]
        write_page(path, render("canton_hub.html", ctx))


def gen_canton_cross(code):
    fallback_by_lang = {lang: canton_registry(code, lang)[:40] for lang in LANGS}
    for did in i18n.DOMAINES:
        for lang in LANGS:
            canton_name = i18n.CANTONS[code][lang]["name"]
            dname = i18n.DOMAINES[did][lang]["name"]
            path = cross_path(code, did, lang)
            desc = pt.cross_intro(lang, dname, canton_name)
            _title = (f"{dname} {i18n.UI[lang]['in']} {canton_name} | "
                      f"{i18n.UI[lang]['find_a_lawyer']} | Legatis")
            ctx = base_ctx(lang, path, _title, desc,
                            {lg: BASE_DOMAIN + cross_path(code, did, lg) for lg in LANGS})
            ctx["domaine_name"] = dname
            ctx["canton_name"] = canton_name
            ctx["h1"] = pt.cross_h1(lang, dname, canton_name)
            ctx["intro_text"] = pt.cross_intro(lang, dname, canton_name)
            ctx["avocats"] = []
            ctx["list_title"] = i18n.UI[lang]["all_practice_areas"]
            ctx["no_specialty_text"] = pt.cross_fallback_text(lang, dname, canton_name)
            ctx["fallback_avocats"] = fallback_by_lang[lang]
            ctx["noindex"] = True
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path(code, lang)), (dname, path)]
            write_page(path, render("cross.html", ctx))


def gen_canton_etudes(code, start=0, count=None, rows=None):
    data = CANTON_DATA[code]
    subset = rows if rows is not None else (data["firms"][start:start + count] if count else data["firms"][start:])
    for f in subset:
        nom_etude = f["etude"]
        members = sorted(f["members"], key=lambda m: m["nom_complet"])
        n = len(members)
        ville = f["ville"]
        adresse = members[0].get("adresse", "") if members else ""
        npa = members[0].get("npa", "") if members else ""
        telephone = members[0].get("telephone", "") if members else ""
        _years = []
        for m in members:
            try:
                _years.append(int(str(m.get("annee_admission") or "")[:4]))
            except ValueError:
                pass
        _oldest_year = min(_years) if _years else None
        _site_url = next((m.get("site_web") for m in members if m.get("site_web")), "")
        _web = WEB_ENRICHMENT.get(site_domain(_site_url)) if _site_url else None
        if not _web:
            _web = f.get("_name_web")
        _sh_langues_raw, _seen_shl = [], set()
        _sh_domaines_raw, _seen_shd = [], set()
        for m in members:
            for x in (m.get("langues_raw") or "").split(","):
                x = x.strip()
                if x and x not in _seen_shl:
                    _seen_shl.add(x)
                    _sh_langues_raw.append(x)
            for x in (m.get("domaines_raw") or "").split(","):
                x = x.strip()
                if x and x not in _seen_shd:
                    _seen_shd.add(x)
                    _sh_domaines_raw.append(x)
        # Noindex decide une seule fois pour les 4 langues : voir commentaire
        # complet plus bas (meme principe que gen_ge_etudes).
        _any_lang_lacks_signal = False
        for _lg in LANGS:
            _dn = web_practice_areas(_web, _lg) or (_sh_domaines_raw if _lg == "de" else [])
            _ln = [translate_lang_name(x, _lg) for x in _sh_langues_raw]
            if not pt.firm_insight(_lg, _ln, _dn, _oldest_year,
                                    founding_year=(_web or {}).get("founding_year"),
                                    team_size_n=(_web or {}).get("team_size_n")):
                _any_lang_lacks_signal = True
                break
        for lang in LANGS:
            canton_name = i18n.CANTONS[code][lang]["name"]
            path = etude_path(code, f["_slug"], lang)
            desc = pt.firm_presentation(lang, nom_etude, canton_name, ville=ville, n_membres=n)
            _loc = f"{ville}, {canton_name}" if ville and ville.lower() != canton_name.lower() else canton_name
            _title = f"{nom_etude} | {i18n.UI[lang]['firm']} {i18n.UI[lang]['in']} {_loc} | Legatis"
            ctx = base_ctx(lang, path, _title, desc,
                            {lg: BASE_DOMAIN + etude_path(code, f["_slug"], lg) for lg in LANGS})
            ctx["nom_etude"] = nom_etude
            ctx["canton_name"] = canton_name
            ctx["adresse"] = adresse
            ctx["npa"] = npa
            ctx["ville"] = ville
            ctx["telephone"] = telephone
            ctx["site_web"] = _site_url or ""
            ctx["site_web_href"] = _site_url or "#"
            ctx["presentation"] = pt.firm_presentation(lang, nom_etude, canton_name, ville=ville, n_membres=n)
            ctx["members_title"] = (
                {"fr": "Avocats de l'étude", "de": "Anwältinnen und Anwälte der Kanzlei",
                 "it": "Avvocati dello studio", "en": "Lawyers at this firm"}[lang])
            ctx["membres"] = [
                {"nom": m["nom_complet"].title(), "role": m.get("fonction", ""),
                 "url": avocat_path(code, m["_slug"], lang)}
                for m in members
            ]
            # Langues/domaines tels que fournis par le registre de Schaffhouse
            # (seul canton avec ces champs pour l'instant), agreges sur tous les
            # membres de l'etude (_sh_langues_raw/_sh_domaines_raw, calcules plus
            # haut). Domaines = jargon juridique non traduit (page DE uniquement,
            # risque de contresens) ; langues = noms simples, traduits.
            _domaine_names = web_practice_areas(_web, lang) or (_sh_domaines_raw if lang == "de" else [])
            _langues_names = [translate_lang_name(x, lang) for x in _sh_langues_raw]
            ctx["insight_text"] = pt.firm_insight(
                lang, _langues_names, _domaine_names, _oldest_year,
                founding_year=(_web or {}).get("founding_year"),
                team_size_n=(_web or {}).get("team_size_n"),
            )
            # Noindex automatique : voir commentaire equivalent dans gen_ge_etudes.
            # Decide une seule fois pour les 4 langues (_any_lang_lacks_signal).
            ctx["noindex"] = _any_lang_lacks_signal
            ctx["web_source_note"] = None
            if _web:
                ctx["web_source_note"] = {
                    "fr": f"Certaines informations ci-dessus proviennent du site officiel du cabinet, consulté le {_web['fetched_date']}.",
                    "de": f"Einige der obigen Angaben stammen von der offiziellen Website der Kanzlei, abgerufen am {_web['fetched_date']}.",
                    "it": f"Alcune informazioni sopra riportate provengono dal sito ufficiale dello studio, consultato il {_web['fetched_date']}.",
                    "en": f"Some information above comes from the firm's official website, accessed on {_web['fetched_date']}.",
                }[lang]
            _city_link = city_link_for(code, ville, lang)
            ctx["ville_url"] = _city_link[1] if _city_link else None
            _bc = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (canton_name, canton_path(code, lang))]
            if _city_link:
                _bc.append(_city_link)
            _bc.append((nom_etude, path))
            ctx["breadcrumb"] = _bc
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "LegalService", "name": nom_etude,
                "url": BASE_DOMAIN + path,
                "address": {"@type": "PostalAddress", "streetAddress": adresse,
                             "postalCode": npa, "addressLocality": ville, "addressCountry": "CH"},
                "telephone": telephone,
                **({"sameAs": [_site_url]} if _site_url else {}),
            }, ensure_ascii=False)
            write_page(path, render("etude.html", ctx))


def gen_canton_avocats(code, start=0, count=None, rows=None):
    data = CANTON_DATA[code]
    individuals = data["individuals"]
    by_city = data["by_city"]
    firm_by_norm = data["firm_by_norm"]
    subset = rows if rows is not None else (individuals[start:start + count] if count else individuals[start:])
    for row in subset:
        nom = row["nom_complet"].title()
        etude_name = row.get("etude", "").strip()
        firm_row = firm_by_norm.get(norm(etude_name)) if etude_name else None
        same_city = [r for r in by_city.get(row["ville"], []) if r["_slug"] != row["_slug"]][:6]
        # Signal web reel pour cette fiche individuelle : d'abord le site_web propre a
        # l'avocat, sinon celui d'un autre membre de la meme etude (meme cabinet =
        # meme site officiel). Jamais invente -- vient toujours d'une donnee deja
        # presente en base ou du cache d'enrichissement deja verifie manuellement.
        _site_url = row.get("site_web") or (
            next((m.get("site_web") for m in firm_row["members"] if m.get("site_web")), "")
            if firm_row else ""
        )
        _web = WEB_ENRICHMENT.get(site_domain(_site_url)) if _site_url else None
        if not _web and firm_row:
            _web = firm_row.get("_name_web")
        # Noindex decide une seule fois pour les 4 langues (jamais indexee dans
        # une langue et pas dans une autre pour la meme fiche) : voir commentaire
        # complet plus bas.
        _langues_raw_pass = [x.strip() for x in (row.get("langues_raw") or "").split(",") if x.strip()]
        _any_lang_lacks_signal = False
        for _lg in LANGS:
            _ln = [translate_lang_name(x, _lg) for x in _langues_raw_pass]
            _dn = web_practice_areas(_web, _lg)
            if not _dn and _lg == "de" and row.get("domaines_raw"):
                _dn = [x.strip() for x in row["domaines_raw"].split(",") if x.strip()]
            _seniority = pt.seniority_text(_lg, row.get("annee_admission"))
            _insight = pt.firm_insight(_lg, _ln, _dn, None,
                                        founding_year=(_web or {}).get("founding_year"),
                                        team_size_n=(_web or {}).get("team_size_n")) if (_web or _dn or _ln) else ""
            if not (_seniority or _ln or _insight):
                _any_lang_lacks_signal = True
                break
        for lang in LANGS:
            canton_name = i18n.CANTONS[code][lang]["name"]
            path = avocat_path(code, row["_slug"], lang)
            # Signaux reels calcules ici (avant desc/title) pour differencier les
            # fiches sans domaines (quasi toutes hors GE, cf. ctx["domaines"] = []
            # plus bas) : title = ville plutot que canton, langues/anciennete
            # injectees dans la description quand disponibles -- voir
            # presentation_text.lawyer_presentation.
            _langues_raw = [x.strip() for x in (row.get("langues_raw") or "").split(",") if x.strip()]
            _langues_for_lang = [translate_lang_name(x, lang) for x in _langues_raw]
            desc = pt.lawyer_presentation(lang, nom, canton_name, etude=etude_name or None,
                                           ville=row.get("ville") or None,
                                           fonction=row.get("fonction") or None,
                                           langues=_langues_for_lang,
                                           seniority_year=row.get("annee_admission"))
            _title_place = clean_city_for_title(row.get("ville")) or canton_name
            _title = f"{nom} | {i18n.UI[lang]['find_a_lawyer_near']} {_title_place} | Legatis"
            ctx = base_ctx(lang, path, _title, desc,
                            {lg: BASE_DOMAIN + avocat_path(code, row["_slug"], lg) for lg in LANGS})
            ctx["nom"] = nom
            ctx["canton_name"] = canton_name
            ctx["review_canton_code"] = code
            ctx["review_avocat_slug"] = row["_slug"]
            ctx["role_or_titre"] = row.get("fonction") or ""
            ctx["etude"] = etude_name
            ctx["etude_url"] = etude_path(code, firm_row["_slug"], lang) if firm_row else None
            ctx["adresse"] = row.get("adresse") or ""
            ctx["npa"] = row.get("npa") or ""
            ctx["ville"] = row.get("ville") or ""
            ctx["telephone"] = row.get("telephone") or ""
            ctx["email"] = row.get("email") or ""
            ctx["site_web"] = row.get("site_web") or ""
            ctx["site_web_href"] = row.get("site_web") or "#"
            ctx["presentation"] = pt.lawyer_presentation(lang, nom, canton_name, etude=etude_name or None,
                                                           ville=row.get("ville") or None,
                                                           fonction=row.get("fonction") or None)
            ctx["domaines"] = []
            ctx["nearby_title"] = f"{i18n.UI[lang]['find_a_lawyer_near']} {row.get('ville','')}" if lang != "de" else f"Weitere Anwältinnen und Anwälte in {row.get('ville','')}"
            ctx["nearby"] = [
                {"nom": r["nom_complet"].title(), "url": avocat_path(code, r["_slug"], lang),
                 "etude": r.get("etude", ""), "ville": r.get("ville", "")}
                for r in same_city
            ]
            # Langues parlees : pour l'instant seul Schaffhouse fournit ce champ
            # (langues_raw, allemand source) -- traduction sure (noms de langues,
            # pas de jargon) vers la langue de la page courante. Deja calcule
            # plus haut (_langues_for_lang) pour la description meta, reutilise ici.
            ctx["langues"] = _langues_for_lang
            ctx["seniority_text"] = pt.seniority_text(lang, row.get("annee_admission"))
            _domaine_names = web_practice_areas(_web, lang)
            if not _domaine_names and lang == "de" and row.get("domaines_raw"):
                # Domaines de competence tels que formules par le registre de
                # Schaffhouse -- jargon juridique specifique, on ne traduit pas
                # (risque de contresens) : affiche uniquement sur la page DE.
                _domaine_names = [x.strip() for x in row["domaines_raw"].split(",") if x.strip()]
            ctx["insight_text"] = pt.firm_insight(
                lang, ctx["langues"], _domaine_names, None,
                founding_year=(_web or {}).get("founding_year"),
                team_size_n=(_web or {}).get("team_size_n"),
            ) if (_web or _domaine_names or ctx["langues"]) else ""
            ctx["web_source_note"] = None
            if _web:
                ctx["web_source_note"] = {
                    "fr": f"Certaines informations ci-dessus proviennent du site officiel du cabinet, consulté le {_web['fetched_date']}.",
                    "de": f"Einige der obigen Angaben stammen von der offiziellen Website der Kanzlei, abgerufen am {_web['fetched_date']}.",
                    "it": f"Alcune informazioni sopra riportate provengono dal sito ufficiale dello studio, consultato il {_web['fetched_date']}.",
                    "en": f"Some information above comes from the firm's official website, accessed on {_web['fetched_date']}.",
                }[lang]
            # Noindex automatique : aucun signal reel (ni anciennete, ni langue, ni domaine,
            # ni enrichissement web) au-dela du nom/adresse -- se retire tout seul des qu'une
            # donnee reelle arrive (meme mecanisme que les fiches etude). Decide une seule
            # fois pour les 4 langues (_any_lang_lacks_signal, calcule plus haut).
            ctx["noindex"] = _any_lang_lacks_signal
            _city_link = city_link_for(code, row.get("ville"), lang)
            ctx["ville_url"] = _city_link[1] if _city_link else None
            _bc = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (canton_name, canton_path(code, lang))]
            if _city_link:
                _bc.append(_city_link)
            _bc.append((nom, path))
            ctx["breadcrumb"] = _bc
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "Attorney", "name": nom,
                "url": BASE_DOMAIN + path,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": row.get("telephone", ""), "email": row.get("email", ""),
                "areaServed": canton_name,
                **({"sameAs": [row["site_web"]]} if row.get("site_web") else {}),
                **({"aggregateRating": attorney_rating_schema(code, row["_slug"])}
                   if attorney_rating_schema(code, row["_slug"]) else {}),
            }, ensure_ascii=False)
            write_page(path, render("avocat.html", ctx))


# ---------------------------------------------------------------- pages villes

# Suffixe postal de canton ("Carouge GE", "Kuesnacht ZH") : meme localite que la
# forme sans suffixe -- on regroupe sous un seul nom d'affichage.
CANTON_CODE_SUFFIX_RE = re.compile(
    r"\s+(AG|AI|AR|BE|BL|BS|FR|GE|GL|GR|JU|LU|NE|NW|OW|SG|SH|SO|SZ|TG|TI|UR|VD|VS|ZG|ZH)$")

# Villes eponymes de leur canton (Geneve, Zuerich, Zug, Luzern...) : la page
# canton couvre deja exactement cette requete -- generer une page ville serait
# du contenu duplique. On les exclut.
_EPONYMOUS_NORMS = set()
for _c in list(i18n.CANTONS.values()) + list(i18n.CANTONS_A_VENIR.values()):
    for _lg in i18n.LANGUAGES:
        _EPONYMOUS_NORMS.add(norm(_c[_lg]["name"]))
_EPONYMOUS_NORMS.update({"basel", "bale", "basilea", "geneve 3", "st. gallen", "saint gall"})

CITY_MIN_LAWYERS = 3
EPONYMOUS_CITY_COUNTS = {}


def city_display(ville):
    return CANTON_CODE_SUFFIX_RE.sub("", ville or "").strip()


def build_city_data():
    """Regroupe les avocats par ville (nom postal nettoye) pour chaque canton.
    Seules les villes non eponymes du canton et comptant au moins
    CITY_MIN_LAWYERS avocats donnent lieu a une page (anti-thin-content :
    on ne genere pas de coquilles vides, plutot que de les generer en noindex).
    Alimente aussi EPONYMOUS_CITY_COUNTS : le nombre d'avocats dont la ville
    correspond au nom du canton lui-meme (ex. "Geneve" dans le canton GE),
    utilise pour proposer un lien vers la page canton dans la liste des
    villes plutot que de simplement l'omettre (voir canton_villes_links)."""
    out = {}
    pools = {"GE": GE_INDIVIDUALS}
    for code, data in CANTON_DATA.items():
        pools[code] = data["individuals"]
    for code, individuals in pools.items():
        groups = {}
        eponymous_count = 0
        for r in individuals:
            disp = city_display(r.get("ville", ""))
            if not disp:
                continue
            key = norm(disp)
            if key in _EPONYMOUS_NORMS:
                eponymous_count += 1
                continue
            g = groups.setdefault(key, {"name": disp, "members": []})
            g["members"].append(r)
        EPONYMOUS_CITY_COUNTS[code] = eponymous_count
        cities = [g for g in groups.values() if len(g["members"]) >= CITY_MIN_LAWYERS]
        cities.sort(key=lambda g: -len(g["members"]))
        seen_slugs = {}
        for g in cities:
            base = slugify(g["name"])
            n = seen_slugs.get(base, 0)
            seen_slugs[base] = n + 1
            g["slug"] = base if n == 0 else f"{base}-{n+1}"
            g["count"] = len(g["members"])
        if cities:
            out[code] = cities
    return out


CITY_DATA = build_city_data()
print(f"Pages villes : {sum(len(v) for v in CITY_DATA.values())} villes retenues "
      f"(seuil {CITY_MIN_LAWYERS} avocats) dans {len(CITY_DATA)} cantons.", file=sys.stderr)


CITY_SLUG_BY_NORM = {
    code: {norm(c["name"]): c for c in cities}
    for code, cities in CITY_DATA.items()
}


def city_link_for(code, ville_raw, lang):
    """Retourne (nom_affiche, url) vers la page ville si une page existe pour
    cette ville dans ce canton (seuil CITY_MIN_LAWYERS respecte, ville non
    eponyme du canton -- voir build_city_data), sinon None. Utilise pour
    inserer un niveau "ville" dans le breadcrumb des fiches avocat/etude et
    lier leur champ ville vers le hub ville correspondant (maillage interne :
    jusque-la aucune fiche avocat/etude ne renvoyait vers sa page ville)."""
    disp = city_display(ville_raw or "")
    if not disp:
        return None
    c = CITY_SLUG_BY_NORM.get(code, {}).get(norm(disp))
    if not c:
        return None
    return c["name"], ville_path(code, c["slug"], lang)


def ville_intro(lang, ville, canton_name, n_avocats, n_etudes):
    if lang == "fr":
        base = (f"{n_avocats} avocats sont référencés à {ville}, dans le canton de {canton_name}, "
                f"sur la base du registre cantonal officiel.")
        if n_etudes:
            base += f" Ils exercent au sein de {n_etudes} études ou cabinets recensés dans cette localité."
        return base
    if lang == "de":
        base = (f"{n_avocats} Anwältinnen und Anwälte sind in {ville} (Kanton {canton_name}) erfasst, "
                f"auf Grundlage des offiziellen kantonalen Anwaltsregisters.")
        if n_etudes:
            base += f" Sie sind in {n_etudes} an diesem Ort erfassten Kanzleien tätig."
        return base
    if lang == "it":
        base = (f"{n_avocats} avvocati sono registrati a {ville}, nel cantone {canton_name}, "
                f"sulla base dell'albo cantonale ufficiale.")
        if n_etudes:
            base += f" Esercitano in {n_etudes} studi legali censiti in questa località."
        return base
    base = (f"{n_avocats} lawyers are listed in {ville}, canton of {canton_name}, "
            f"based on the official cantonal bar registry.")
    if n_etudes:
        base += f" They practise in {n_etudes} firms recorded in this locality."
    return base


def ville_faq(lang, ville, canton_name, n_avocats, n_etudes):
    """FAQ courte pour les pages ville : uniquement des chiffres deja reels
    (n_avocats, n_etudes) et le meme principe de verification que le reste du
    site (registre cantonal officiel, aucune donnee inventee). Sert a la fois
    de contenu unique par ville (les pages ville n'ont sinon qu'un seul
    paragraphe d'intro) et de schema.org FAQPage."""
    if lang == "fr":
        a1 = f"{n_avocats} avocats sont référencés à {ville} sur la base du registre cantonal officiel de {canton_name}."
        if n_etudes:
            a1 += f" Ils exercent au sein de {n_etudes} études ou cabinets recensés dans cette localité."
        return [
            {"q": f"Combien d'avocats sont référencés à {ville} ?", "a": a1},
            {"q": "Ces avocats sont-ils vérifiés ?",
             "a": f"Oui. Chaque avocat référencé par Legatis à {ville} est inscrit au registre cantonal officiel des avocats du canton de {canton_name}, seule source utilisée pour construire cette liste."},
        ]
    if lang == "de":
        a1 = f"{n_avocats} Anwältinnen und Anwälte sind in {ville} auf Grundlage des offiziellen kantonalen Anwaltsregisters von {canton_name} erfasst."
        if n_etudes:
            a1 += f" Sie sind in {n_etudes} an diesem Ort erfassten Kanzleien tätig."
        return [
            {"q": f"Wie viele Anwältinnen und Anwälte sind in {ville} erfasst?", "a": a1},
            {"q": "Sind diese Anwältinnen und Anwälte überprüft?",
             "a": f"Ja. Jede von Legatis in {ville} aufgeführte Anwältin bzw. jeder Anwalt ist im offiziellen kantonalen Anwaltsregister des Kantons {canton_name} eingetragen, der einzigen für diese Liste verwendeten Quelle."},
        ]
    if lang == "it":
        a1 = f"{n_avocats} avvocati sono registrati a {ville} sulla base dell'albo cantonale ufficiale del cantone {canton_name}."
        if n_etudes:
            a1 += f" Esercitano in {n_etudes} studi legali censiti in questa località."
        return [
            {"q": f"Quanti avvocati sono registrati a {ville}?", "a": a1},
            {"q": "Questi avvocati sono verificati?",
             "a": f"Sì. Ogni avvocato indicato da Legatis a {ville} è iscritto all'albo cantonale ufficiale degli avvocati del cantone {canton_name}, unica fonte utilizzata per costruire questo elenco."},
        ]
    a1 = f"{n_avocats} lawyers are listed in {ville}, based on the official cantonal bar registry of {canton_name}."
    if n_etudes:
        a1 += f" They practise in {n_etudes} firms recorded in this locality."
    return [
        {"q": f"How many lawyers are listed in {ville}?", "a": a1},
        {"q": "Are these lawyers verified?",
         "a": f"Yes. Every lawyer Legatis lists in {ville} is registered with the official cantonal bar registry of {canton_name}, the only source used to build this list."},
    ]


def _city_registry(code, city, lang):
    """Registre d'une ville : etudes presentes (avec lien vers leur fiche) puis
    avocats sans etude referencable, tries alphabetiquement."""
    if code == "GE":
        firm_map = FIRM_BY_NORM
    else:
        firm_map = CANTON_DATA[code]["firm_by_norm"]
    firms_seen = {}
    solos = []
    for m in city["members"]:
        e = (m.get("etude") or "").strip()
        f = firm_map.get(norm(e)) if e else None
        if f is not None:
            k = norm(e)
            firms_seen.setdefault(k, {"row": f, "n": 0})
            firms_seen[k]["n"] += 1
        else:
            solos.append(m)
    rows = []
    for entry in firms_seen.values():
        f = entry["row"]
        rows.append({
            "type": "etude", "nom": f["etude"], "url": etude_path(code, f["_slug"], lang),
            "ville": city["name"], "n_membres": entry["n"],
        })
    for m in solos:
        rows.append({
            "type": "avocat", "nom": m["nom_complet"].title(), "url": avocat_path(code, m["_slug"], lang),
            "ville": city["name"], "role": m.get("fonction", ""),
        })
    rows.sort(key=lambda x: x["nom"])
    return rows, len(firms_seen)


def _ge_city_domain_matches(city):
    """Pour une ville GE : avocats de la ville par domaine (donnees registre)."""
    by_dom = {}
    for m in city["members"]:
        for did in domaines_for_lawyer(m):
            by_dom.setdefault(did, []).append(m)
    return {did: ms for did, ms in by_dom.items() if len(ms) >= 2}


def gen_villes():
    for code, cities in CITY_DATA.items():
        for city in cities:
            dom_matches = _ge_city_domain_matches(city) if code == "GE" else {}
            for lang in LANGS:
                canton_name = i18n.CANTONS[code][lang]["name"]
                path = ville_path(code, city["slug"], lang)
                registry, n_firms = _city_registry(code, city, lang)
                intro = ville_intro(lang, city["name"], canton_name, city["count"], n_firms)
                title = (f"{i18n.UI[lang]['find_a_lawyer_near']} {city['name']} | "
                         f"{city['count']} {LAWYER_WORD[lang]} | Legatis")
                ctx = base_ctx(lang, path, title, intro,
                                {lg: BASE_DOMAIN + ville_path(code, city["slug"], lg) for lg in LANGS})
                ctx["ville_name"] = city["name"]
                ctx["canton_name"] = canton_name
                ctx["intro_text"] = intro
                ctx["registry"] = registry
                ctx["stats_label"] = {
                    "fr": f"{city['count']} avocats référencés à {city['name']}",
                    "de": f"{city['count']} erfasste Anwältinnen und Anwälte in {city['name']}",
                    "it": f"{city['count']} avvocati registrati a {city['name']}",
                    "en": f"{city['count']} lawyers listed in {city['name']}",
                }[lang]
                ctx["domaines"] = [
                    {"name": i18n.DOMAINES[did][lang]["name"],
                     "url": ville_domaine_path(code, city["slug"], did, lang)}
                    for did in dom_matches
                ]
                ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                      (canton_name, canton_path(code, lang)),
                                      (city["name"], path)]
                # FAQ courte + schema FAQPage : seul contenu unique par ville au-dela
                # du paragraphe d'intro (voir ville_faq -- chiffres reels uniquement).
                ctx["faq"] = ville_faq(lang, city["name"], canton_name, city["count"], n_firms)
                ctx["schema"] = json.dumps({
                    "@context": "https://schema.org", "@type": "FAQPage",
                    "mainEntity": [
                        {"@type": "Question", "name": item["q"],
                         "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
                        for item in ctx["faq"]
                    ],
                }, ensure_ascii=False)
                # Maillage interne vers des pages deja existantes et pertinentes
                # (guides + etude AJ) : les pages ville n'avaient jusque-la aucun
                # lien sortant vers le contenu editorial du site.
                ctx["related"] = [
                    {"name": guides_content.GUIDES["choisir-avocat"][lang]["title"],
                     "url": guide_path("choisir-avocat", lang)},
                    {"name": guides_content.GUIDES["cout-avocat"][lang]["title"],
                     "url": guide_path("cout-avocat", lang)},
                    {"name": i18n.UI[lang]["press_study_title"], "url": etude_aj_path(lang)},
                ]
                write_page(path, render("ville_hub.html", ctx))


def gen_ville_domaines():
    """Pages ville x domaine, uniquement la ou des avocats du registre declarent
    effectivement le domaine (Geneve : seul canton avec domaines par avocat).
    Seuil de 2 avocats minimum -- jamais de page vide."""
    for code, cities in CITY_DATA.items():
        if code != "GE":
            continue
        for city in cities:
            dom_matches = _ge_city_domain_matches(city)
            for did, matches in dom_matches.items():
                for lang in LANGS:
                    canton_name = i18n.CANTONS[code][lang]["name"]
                    dname = i18n.DOMAINES[did][lang]["name"]
                    path = ville_domaine_path(code, city["slug"], did, lang)
                    desc = pt.ville_cross_intro(lang, dname, canton_name, city["name"])
                    ctx = base_ctx(lang, path, f"{dname} {i18n.UI[lang]['in']} {city['name']} | Legatis", desc,
                                    {lg: BASE_DOMAIN + ville_domaine_path(code, city["slug"], did, lg) for lg in LANGS})
                    ctx["domaine_name"] = dname
                    ctx["canton_name"] = canton_name
                    ctx["h1"] = pt.cross_h1(lang, dname, city["name"])
                    ctx["intro_text"] = pt.ville_cross_intro(lang, dname, canton_name, city["name"])
                    ctx["avocats"] = [
                        {"nom": r["nom_complet"].title(), "url": avocat_path(code, r["_slug"], lang),
                         "etude": r.get("etude", ""), "ville": r.get("ville", ""), "role": r.get("fonction", "")}
                        for r in matches
                    ]
                    ctx["registry"] = ctx["avocats"]
                    ctx["list_title"] = i18n.UI[lang]["all_practice_areas"]
                    ctx["no_specialty_text"] = ""
                    ctx["fallback_avocats"] = []
                    ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                          (canton_name, canton_path(code, lang)),
                                          (city["name"], ville_path(code, city["slug"], lang)),
                                          (dname, path)]
                    write_page(path, render("cross.html", ctx))


def canton_villes_links(code, lang):
    """Liens vers les pages villes d'un canton (maillage interne du hub canton).
    Ajoute en tete un lien vers la page canton elle-meme au nom de la ville
    eponyme (ex. "Geneve" pour le canton GE) : cette ville n'a pas de page
    dediee (contenu dupliquerait la page canton, voir _EPONYMOUS_NORMS),
    mais l'omettre completement de la liste des villes est deroutant --
    on preferait pouvoir "choisir Geneve-ville" alors que ce choix existe
    deja, c'est simplement la page canton elle-meme."""
    links = []
    eponymous_count = EPONYMOUS_CITY_COUNTS.get(code, 0)
    if eponymous_count:
        links.append({
            "name": i18n.CANTONS[code][lang]["name"],
            "url": canton_path(code, lang),
            "count": eponymous_count,
        })
    links.extend(
        {"name": c["name"], "url": ville_path(code, c["slug"], lang), "count": c["count"]}
        for c in CITY_DATA.get(code, [])
    )
    return links


# ---------------------------------------------------------------- guides

GUIDES_INDEX_INTRO = {
    "fr": "Des guides pratiques pour comprendre comment travailler avec un avocat en Suisse : choix, coûts, assistance judiciaire, spécialisations.",
    "de": "Praktische Ratgeber zur Zusammenarbeit mit Anwältinnen und Anwälten in der Schweiz: Auswahl, Kosten, unentgeltliche Rechtspflege, Spezialisierungen.",
    "it": "Guide pratiche per capire come lavorare con un avvocato in Svizzera: scelta, costi, gratuito patrocinio, specializzazioni.",
    "en": "Practical guides to working with a lawyer in Switzerland: choosing one, costs, legal aid, specialisations.",
}


GUIDE_CALCULATORS = {
    "assistance-judiciaire": calc_widget.CALCULATOR_HTML,
    "calcul-prescription": legal_tools_widgets.PRESCRIPTION_HTML,
    "calcul-delai-procedure": legal_tools_widgets.DELAI_HTML,
    "calcul-interets-moratoires": legal_tools_widgets.INTERETS_HTML,
}


def gen_guides():
    gids = list(guides_content.GUIDES.keys())
    for lang in LANGS:
        path = guides_index_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['guides_title']} | Legatis",
                        GUIDES_INDEX_INTRO[lang], hreflang_for(guides_index_path))
        ctx["intro_text"] = GUIDES_INDEX_INTRO[lang]
        ctx["guides"] = [
            {"title": guides_content.GUIDES[g][lang]["title"],
             "meta": guides_content.GUIDES[g][lang]["meta"],
             "url": guide_path(g, lang)}
            for g in gids
        ]
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                              (i18n.UI[lang]["guides_title"], path)]
        write_page(path, render("guides_index.html", ctx))

    for gid in gids:
        for lang in LANGS:
            g = guides_content.GUIDES[gid][lang]
            path = guide_path(gid, lang)
            ctx = base_ctx(lang, path, f"{g['title']} | Legatis", g["meta"],
                            {lg: BASE_DOMAIN + guide_path(gid, lg) for lg in LANGS})
            ctx["page_title"] = g["title"]
            ctx["sections"] = g["sections"]
            ctx["faq"] = g["faq"]
            ctx["calculator_html"] = GUIDE_CALCULATORS[gid][lang] if gid in GUIDE_CALCULATORS else None
            ctx["related"] = (
                [{"name": guides_content.GUIDES[o][lang]["title"], "url": guide_path(o, lang)}
                 for o in gids if o != gid]
                + [{"name": i18n.UI[lang]["all_cantons"], "url": cantons_index_path(lang)},
                   {"name": i18n.UI[lang]["all_practice_areas"], "url": domaines_index_path(lang)}]
            )
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (i18n.UI[lang]["guides_title"], guides_index_path(lang)),
                                  (g["title"], path)]
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": item["q"],
                     "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
                    for item in g["faq"]
                ],
            }, ensure_ascii=False)
            write_page(path, render("guide.html", ctx))


# ---------------------------------------------------------------- blog

BLOG_INDEX_INTRO = {
    "fr": "Des articles précis, domaine de droit par domaine de droit, pour comprendre vos droits en Suisse. Sources légales citées, aucun chiffre inventé.",
    "de": "Präzise Artikel, Rechtsgebiet für Rechtsgebiet, um Ihre Rechte in der Schweiz zu verstehen. Rechtsquellen werden zitiert, keine erfundenen Zahlen.",
    "it": "Articoli precisi, ambito del diritto per ambito del diritto, per capire i vostri diritti in Svizzera. Fonti legali citate, nessuna cifra inventata.",
    "en": "Precise articles, one practice area at a time, to help you understand your rights in Switzerland. Legal sources cited, no invented figures.",
}


def gen_etude_aj():
    """Page dediee interactive de l'etude comparative AJ (taux de majoration
    du minimum vital selon le canton). Contenu factuel dans
    data/aj_study/data.json (jamais modifie ici), traductions dans
    data/aj_study/i18n.json, mis en forme par aj_study_content.page_context()."""
    for lang in LANGS:
        path = etude_aj_path(lang)
        pc = aj.page_context(lang)
        title = pc["t"]["title"]
        meta_desc = pc["t"]["meta_description"]
        ctx = base_ctx(lang, path, f"{title} | Legatis", meta_desc, hreflang_for(etude_aj_path))
        ctx.update(pc)
        ctx["pdf_url"] = f"/static/downloads/etude-aj-cantons-{lang}.pdf"
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (title, path)]
        ctx["schema"] = json.dumps({
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": meta_desc,
            "inLanguage": lang,
            "url": BASE_DOMAIN + path,
            "publisher": {"@type": "Organization", "name": "Legatis", "url": BASE_DOMAIN},
        }, ensure_ascii=False)
        write_page(path, render("etude_aj.html", ctx))



VITRINE_SPECIALITES_ORDER = list(i18n.DOMAINES.keys())


def gen_verification_contacts():
    """Genere deux artefacts a partir des memes donnees de registre officiel
    deja chargees en memoire (GE_INDIVIDUALS + CANTON_DATA) pour le systeme
    de verification d'identite (revendication de fiche) :

    - data/verification_contacts.json : JAMAIS copie dans dist/, jamais
      public. Email + telephone reels par cle "{canton}/{slug}", lu
      uniquement cote serveur par api/verification-request.js pour decider
      QUEL palier de la cascade de verification s'applique (email connu >
      telephone connu > document+selfie) et pour connaitre la vraie
      destination du lien/appel. Le client ne peut jamais influencer ce choix
      -- il n'a acces qu'a des booleens (voir plus bas), jamais aux valeurs.

    - dist/verification-index.json : public, mais ne contient QUE des
      booleens has_email/has_phone par fiche, jamais les valeurs elles-memes
      (meme si email/telephone sont deja affiches individuellement sur
      chaque fiche avocat -- on evite volontairement d'agreger ces valeurs
      dans un seul fichier propice au scraping en masse). Utilise cote
      client sur /verifier-mon-identite/ pour afficher immediatement le bon
      texte d'etape sans attendre l'aller-retour serveur ; le serveur
      revalide de toute facon tout a la soumission."""
    contacts = {}
    public_index = []

    def _add(code, slug, email, telephone):
        key = f"{code}/{slug}"
        email = (email or "").strip()
        telephone = (telephone or "").strip()
        contacts[key] = {"email": email or None, "telephone": telephone or None}
        public_index.append({"c": code, "s": slug, "e": bool(email), "p": bool(telephone)})

    for r in GE_INDIVIDUALS:
        _add("GE", r["_slug"], r.get("email"), r.get("telephone"))
    for code, data in CANTON_DATA.items():
        for r in data["individuals"]:
            _add(code, r["_slug"], r.get("email"), r.get("telephone"))

    with open(os.path.join(DATA_DIR, "verification_contacts.json"), "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False)

    with open(os.path.join(DIST_DIR, "verification-index.json"), "w", encoding="utf-8") as f:
        json.dump(public_index, f, ensure_ascii=False)


def gen_verification_request():
    """Page publique du formulaire de verification d'identite. La cascade
    (email/telephone/document) est decidee cote serveur dans
    api/verification-request.js -- cette page ne fait qu'afficher, pour
    chaque cas, le texte prepare dans verification_content.FORM."""
    for lang in LANGS:
        path = verification_request_path(lang)
        f = verification_content.FORM[lang]
        ctx = base_ctx(lang, path, f"{f['title']} | Legatis", f["intro"], hreflang_for(verification_request_path))
        ctx["f"] = f
        ctx["search_index_url"] = f"/search-index-{lang}.json"
        ctx["verification_index_url"] = "/verification-index.json"
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (f["title"], path)]
        # Offre "site web gratuit" + contrat, presentee juste apres la
        # creation du compte (avant validation de l'identite) -- voir
        # website_offer_content.py et api/website-offer-decision.js.
        ctx["offer"] = website_offer_content.OFFER[lang]
        ctx["contract"] = website_offer_content.CONTRACT[lang]
        ctx["contract_version"] = website_offer_content.CONTRACT_VERSION
        write_page(path, render("verification_demande.html", ctx))


def gen_verification_confirmee():
    """Page statique de destination du lien de confirmation envoye par email
    (palier 1 de la cascade). Le resultat reel (ok/expire/invalide) est
    determine par api/verification-confirm.js AVANT la redirection ici (voir
    le parametre ?status= dans l'URL) ; cette page ne fait qu'afficher le
    texte correspondant en JS, sans jamais elle-meme decider quoi que ce
    soit cote serveur."""
    for lang in LANGS:
        path = verification_confirmee_path(lang)
        c = verification_content.CONFIRM[lang]
        ctx = base_ctx(lang, path, f"{c['title']} | Legatis", c["ok_text"], hreflang_for(verification_confirmee_path))
        ctx["c"] = c
        ctx["verification_request_url"] = verification_request_path(lang)
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (c["title"], path)]
        write_page(path, render("verification_confirmee.html", ctx))


def gen_verification_review():
    """Page interne (noindex) de revision des demandes de verification
    d'identite en attente (paliers telephone/document). Contrairement a
    gen_vitrine_review() (qui lit des fichiers JSON commit dans le depot),
    cette page ne contient aucune donnee en dur : elle affiche un simple
    formulaire d'acces (jeton admin) et recupere la liste + agit via
    api/verification-list.js / api/verification-decide.js, cote client,
    apres authentification par jeton. Aucune donnee sensible ne transite
    par le build Python ni n'est jamais committee dans le depot (public)."""
    lang = "fr"
    path = "/interne/verification-avocats/"
    ctx = base_ctx(lang, path, "Verifications en attente | Legatis (interne)", "Page interne de revision.", {})
    ctx["noindex"] = True
    ctx["admin_nav_active"] = "verification"
    write_page(path, render("verification_review.html", ctx))


def gen_analytics_dashboard():
    """Page interne (noindex) de consultation des statistiques d'analytics
    "maison" -- voir supabase_schema.sql (table analytics_events),
    api/track.js (collecte), api/analytics-summary.js (agregation, protegee
    par jeton admin) et static/js/analytics.js (collecte cote client sur
    toutes les pages). Meme principe que gen_verification_review() : aucune
    donnee en dur, tout est recupere cote client apres authentification par
    jeton."""
    lang = "fr"
    path = "/interne/analytics/"
    ctx = base_ctx(lang, path, "Analytics | Legatis (interne)", "Page interne de statistiques.", {})
    ctx["noindex"] = True
    ctx["admin_nav_active"] = "analytics"
    write_page(path, render("analytics_dashboard.html", ctx))


def gen_connexion():
    """Page de connexion avocat (email + mot de passe classique, via
    Supabase Auth). Requetes REST directes vers /auth/v1/token, sans SDK
    supabase-js, comme le reste du site."""
    for lang in LANGS:
        path = connexion_path(lang)
        l = account_content.LOGIN[lang]
        ctx = base_ctx(lang, path, f"{l['title']} | Legatis", l["intro"], hreflang_for(connexion_path))
        ctx["l"] = l
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (l["title"], path)]
        write_page(path, render("connexion.html", ctx))


def gen_mon_profil():
    """Tableau de bord de l'avocat connecte : donnees du registre en lecture
    seule + formulaire de soumission du contenu complementaire (bio, photo,
    coordonnees affichees, liens), moderees ensuite via
    api/profile-list.js / api/profile-decide.js. Page personnelle,
    non indexee."""
    for lang in LANGS:
        path = mon_profil_path(lang)
        p = account_content.PROFILE[lang]
        ctx = base_ctx(lang, path, f"{p['title']} | Legatis", p["intro"], hreflang_for(mon_profil_path))
        ctx["p"] = p
        ctx["noindex"] = True
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (p["title"], path)]
        write_page(path, render("mon_profil.html", ctx))


def gen_avis_request():
    """Page publique du formulaire de depot d'avis."""
    for lang in LANGS:
        path = avis_request_path(lang)
        f = review_content.FORM[lang]
        ctx = base_ctx(lang, path, f"{f['title']} | Legatis", f["intro"], hreflang_for(avis_request_path))
        ctx["f"] = f
        ctx["search_index_url"] = f"/search-index-{lang}.json"
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (f["title"], path)]
        write_page(path, render("avis_demande.html", ctx))


ACCENT_RAMPS = {
    "bordeaux": {"700": "oklch(30% 0.09 22)", "600": "oklch(38% 0.11 22)", "500": "oklch(45% 0.13 22)", "100": "oklch(92% 0.03 22)", "50": "oklch(96% 0.018 22)"},
    "encre": {"700": "oklch(30% 0.09 258)", "600": "oklch(38% 0.11 258)", "500": "oklch(45% 0.13 258)", "100": "oklch(92% 0.03 258)", "50": "oklch(96% 0.018 258)"},
    "sapin": {"700": "oklch(30% 0.09 150)", "600": "oklch(38% 0.11 150)", "500": "oklch(45% 0.13 150)", "100": "oklch(92% 0.03 150)", "50": "oklch(96% 0.018 150)"},
    "ardoise": {"700": "oklch(30% 0.09 210)", "600": "oklch(38% 0.11 210)", "500": "oklch(45% 0.13 210)", "100": "oklch(92% 0.03 210)", "50": "oklch(96% 0.018 210)"},
}


def accent_style(accent_color):
    ramp = ACCENT_RAMPS.get(accent_color, ACCENT_RAMPS["bordeaux"])
    return "".join(f"--accent-{k}:{v};" for k, v in ramp.items())


_YOUTUBE_RE = re.compile(r"(?:youtube\.com/watch\?v=|youtube\.com/shorts/|youtu\.be/)([\w-]{6,})")
_VIMEO_RE = re.compile(r"vimeo\.com/(\d+)")


def to_embed_url(video_url):
    """Convertit un lien YouTube/Vimeo grand public en URL embarquable.
    Retourne None pour tout ce qui n'est pas reconnu (jamais d'iframe
    pointant vers un domaine arbitraire non verifie)."""
    if not video_url:
        return None
    m = _YOUTUBE_RE.search(video_url)
    if m:
        return f"https://www.youtube-nocookie.com/embed/{m.group(1)}"
    m = _VIMEO_RE.search(video_url)
    if m:
        return f"https://player.vimeo.com/video/{m.group(1)}"
    return None


def maps_search_url(adresse):
    if not adresse:
        return None
    return f"https://www.google.com/maps/search/?api=1&query={_url_quote(adresse)}"


def whatsapp_href(whatsapp):
    if not whatsapp:
        return None
    digits = re.sub(r"[^0-9]", "", whatsapp)
    if not digits:
        return None
    return f"https://wa.me/{digits}"


def _load_vitrine_submissions(subdir):
    out = []
    d = os.path.join(DATA_DIR, "vitrines", subdir)
    if not os.path.isdir(d):
        return out
    for fname in sorted(os.listdir(d)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(d, fname), encoding="utf-8") as fh:
            try:
                out.append(json.load(fh))
            except json.JSONDecodeError:
                continue
    return out


def _vitrine_page_ctx(sub, lang):
    locked = sub.get("locked", {})
    free = sub.get("free", {})
    canton_code = locked.get("canton") or (sub.get("registry_match") or {}).get("code")
    canton_name = i18n.CANTONS.get(canton_code, {}).get(lang, {}).get("name", locked.get("canton_name", ""))
    specialites = [
        {"id": did, "name": i18n.DOMAINES[did][lang]["name"], "url": domaine_path(did, lang)}
        for did in (free.get("specialites") or []) if did in i18n.DOMAINES
    ]
    photo_filename = free.get("photo_filename")
    return {
        "nom_complet": locked.get("nom_complet", ""),
        "canton_name": canton_name,
        "ville": locked.get("ville", ""),
        "langues": locked.get("langues", []),
        "photo_url": f"/static/vitrines/photos/{photo_filename}" if photo_filename else None,
        "role_titre": free.get("role_titre"),
        "accroche": free.get("accroche"),
        "bio": free.get("bio"),
        "citation": free.get("citation"),
        "specialites": specialites,
        "distinctions": free.get("distinctions") or [],
        "site_web": free.get("site_web"),
        "site_web_href": free.get("site_web"),
        "linkedin": free.get("linkedin"),
        "instagram": free.get("instagram"),
        "telephone": sub.get("contact_phone"),
        "email": sub.get("contact_email"),
        "registry_url": avocat_path(canton_code, (sub.get("registry_match") or {}).get("slug", ""), lang) if canton_code else None,
        "accent_color": free.get("accent_color") or "bordeaux",
        "accent_style": accent_style(free.get("accent_color") or "bordeaux"),
        "photo_frame": free.get("photo_frame") or "cercle",
        "style_titres": free.get("style_titres") or "classique",
        "adresse": free.get("adresse"),
        "maps_url": maps_search_url(free.get("adresse")),
        "horaires": free.get("horaires"),
        "whatsapp": free.get("whatsapp"),
        "whatsapp_href": whatsapp_href(free.get("whatsapp")),
        "rdv_url": free.get("rdv_url"),
        "video_url": free.get("video_url"),
        "video_embed_url": to_embed_url(free.get("video_url")),
        "galerie": [u for u in (free.get("galerie") or []) if isinstance(u, str) and u.startswith(("http://", "https://"))][:4],
    }


def gen_vitrines():
    """Genere les pages vitrine publiques pour chaque demande approuvee
    (data/vitrines/approved/*.json), dans les 4 langues. Voir
    data/vitrines/README.md pour le cycle de vie complet."""
    for sub in _load_vitrine_submissions("approved"):
        slug = sub.get("slug")
        if not slug:
            continue
        template = sub.get("template") if sub.get("template") in vitrine_content.TEMPLATE_ORDER else "prestige"
        for lang in LANGS:
            path = vitrine_path(slug, lang)
            pctx = _vitrine_page_ctx(sub, lang)
            title = f"{pctx['nom_complet']} | Legatis"
            desc = pctx.get("accroche") or pctx.get("bio") or ""
            ctx = base_ctx(lang, path, title, desc, {lg: vitrine_path(slug, lg) for lg in LANGS})
            ctx.update(pctx)
            ctx["noindex"] = False
            write_page(path, render(f"vitrine_{template}.html", ctx))


def gen_vitrine_review():
    """Page interne (noindex) listant les demandes en attente, pour
    validation visuelle par Greg avant deplacement pending -> approved."""
    pending = _load_vitrine_submissions("pending")
    lang = "fr"
    path = "/interne/vitrines-en-attente/"
    ctx = base_ctx(lang, path, "Vitrines en attente | Legatis (interne)", "Page interne de revision.", {})
    ctx["noindex"] = True
    ctx["admin_nav_active"] = "vitrines"
    ctx["pending"] = []
    for sub in pending:
        pctx = _vitrine_page_ctx(sub, lang)
        ctx["pending"].append({
            "slug": sub.get("slug"),
            "submitted_at": sub.get("submitted_at"),
            "template": sub.get("template"),
            "contact_email": sub.get("contact_email"),
            "registry_verified": (sub.get("registry_match") or {}).get("verified", False),
            **pctx,
        })
    write_page(path, render("vitrine_review.html", ctx))


def gen_blog():
    """Blog juridique : contenu edite dans blog_content.BLOG_ARTICLES. Toutes
    les langues ne sont pas forcement encore ecrites pour chaque article
    (rediaction par lots) -- on ne genere que les langues presentes, sans
    jamais planter sur une langue manquante."""
    bids = list(blog_content.BLOG_ARTICLES.keys())

    # index par langue : ne liste que les articles deja rediges dans cette langue
    for lang in LANGS:
        path = blog_index_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['blog_title']} | Legatis",
                        i18n.UI[lang]["blog_intro"], hreflang_for(blog_index_path))
        ctx["intro_text"] = i18n.UI[lang]["blog_intro"]
        ctx["articles"] = [
            {"title": blog_content.BLOG_ARTICLES[b][lang]["title"],
             "meta": blog_content.BLOG_ARTICLES[b][lang]["meta"],
             "url": blog_article_path(b, lang),
             "domaine_name": i18n.DOMAINES[blog_content.BLOG_ARTICLES[b]["domaine_id"]][lang]["name"]}
            for b in bids if lang in blog_content.BLOG_ARTICLES[b]
        ]
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                              (i18n.UI[lang]["blog_title"], path)]
        write_page(path, render("blog_index.html", ctx))

    # pages article : uniquement pour les langues deja rediges de cet article
    for bid in bids:
        article = blog_content.BLOG_ARTICLES[bid]
        did = article["domaine_id"]
        available_langs = [lg for lg in LANGS if lg in article]
        article_hreflang = {lg: BASE_DOMAIN + blog_article_path(bid, lg) for lg in available_langs}
        for lang in available_langs:
            a = article[lang]
            path = blog_article_path(bid, lang)
            dname = i18n.DOMAINES[did][lang]["name"]
            ctx = base_ctx(lang, path, f"{a['title']} | Legatis", a["meta"], article_hreflang)
            ctx["page_title"] = a["title"]
            ctx["domaine_name"] = dname
            ctx["sections"] = a["sections"]
            ctx["faq"] = a["faq"]
            same_domain_others = [
                o for o in bids
                if o != bid and lang in blog_content.BLOG_ARTICLES[o]
                and blog_content.BLOG_ARTICLES[o]["domaine_id"] == did
            ][:3]
            ctx["related"] = (
                [{"name": blog_content.BLOG_ARTICLES[o][lang]["title"], "url": blog_article_path(o, lang)}
                 for o in same_domain_others]
                + [{"name": dname, "url": domaine_path(did, lang)},
                   {"name": i18n.UI[lang]["guides_title"], "url": guides_index_path(lang)}]
            )
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (i18n.UI[lang]["blog_title"], blog_index_path(lang)),
                                  (a["title"], path)]
            page_url = BASE_DOMAIN + path
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "BlogPosting",
                "headline": a["title"], "description": a["meta"],
                "url": page_url, "mainEntityOfPage": page_url,
                "inLanguage": lang, "datePublished": article["published"],
                "dateModified": article["published"],
                "publisher": {"@type": "Organization", "name": "Legatis", "url": BASE_DOMAIN},
                "about": dname,
            }, ensure_ascii=False)
            ctx["extra_schema"] = [json.dumps({
                "@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": item["q"],
                     "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
                    for item in a["faq"]
                ],
            }, ensure_ascii=False)]
            write_page(path, render("blog_article.html", ctx))


# ---------------------------------------------------------------- llms.txt

def gen_llms_txt():
    """Fichier llms.txt a la racine : oriente les assistants IA (AEO) vers les
    points d'entree structures du site. Uniquement des faits reels du build."""
    n_avocats = sum(v for v in CANTON_COUNTS.values() if v)
    n_etudes = len(GE_FIRMS) + sum(len(d["firms"]) for d in CANTON_DATA.values())
    n_cantons = len(i18n.CANTONS)
    lines = [
        "# Legatis",
        "",
        "> Legatis (legatis.ch) is a multilingual directory (FR/DE/IT/EN) of lawyers in Switzerland, "
        f"built from the official cantonal bar registries. It currently lists {n_avocats} lawyers and "
        f"{n_etudes} law firms across {n_cantons} cantons. Facts shown on profile pages come from official "
        "registers or from the firms' own websites (always dated and attributed); nothing is invented or estimated.",
        "",
        "## Main entry points",
        "",
        "- [Accueil (FR)](https://legatis.ch/fr/): French home page",
        "- [Startseite (DE)](https://legatis.ch/de/): German home page",
        "- [Home (IT)](https://legatis.ch/it/): Italian home page",
        "- [Home (EN)](https://legatis.ch/en/): English home page",
        "- [Cantons (FR)](https://legatis.ch/fr/avocats/): lawyers by canton",
        "- [Practice areas (EN)](https://legatis.ch/en/practice-areas/): lawyers by field of law",
        "- [Guides pratiques (FR)](https://legatis.ch/fr/guides/): practical guides (choosing a lawyer, "
        "costs, legal aid, specialist titles, first consultation)",
        "- [Methodology (EN)](https://legatis.ch/en/methodology/): data sources and methodology",
        "",
        "## Data principles",
        "",
        "- Sources: official cantonal bar registries (registre cantonal des avocats / kantonales Anwaltsregister).",
        "- Enrichment: facts published by law firms on their own official websites, always dated and attributed.",
        "- No fabrication: profiles without verified signals carry no invented content.",
        "- Corrections: https://legatis.ch/fr/signaler-une-correction/",
        "",
        "## Sitemap",
        "",
        "- https://legatis.ch/sitemap.xml",
        "",
    ]
    with open(os.path.join(DIST_DIR, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("llms.txt genere.", file=sys.stderr)


def copy_static():
    import shutil
    src = os.path.join(SITE_ROOT, "static")
    dst = os.path.join(DIST_DIR, "static")
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        for root, dirs, files in os.walk(src):
            rel = os.path.relpath(root, src)
            target_dir = os.path.join(dst, rel) if rel != "." else dst
            os.makedirs(target_dir, exist_ok=True)
            for fname in files:
                shutil.copyfile(os.path.join(root, fname), os.path.join(target_dir, fname))


STATIC_PAGE_IDS = ["methodologie", "a-propos", "contact", "mentions-legales", "confidentialite", "correction", "revendiquer"]


def gen_static_pages():
    for page_id in STATIC_PAGE_IDS:
        for lang in LANGS:
            content = sp_content.get_page(page_id, lang)
            path = f"/{lang}/{seg(page_id, lang)}/"
            desc = content["sections"][0]["paragraphs"][0]
            ctx = base_ctx(lang, path, f"{content['title']} | Legatis", desc,
                            {lg: f"/{lg}/{seg(page_id, lg)}/" for lg in LANGS})
            ctx["page_title"] = content["title"]
            ctx["sections"] = content["sections"]
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (content["title"], path)]
            write_page(path, render("page.html", ctx))


def gen_sitemaps():
    today = datetime.date.today().isoformat()
    by_lang = {lg: [] for lg in LANGS}
    hreflang_re = re.compile(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">')
    for lg in LANGS:
        lang_dir = os.path.join(DIST_DIR, lg)
        for dirpath, _dirnames, filenames in os.walk(lang_dir):
            if "index.html" in filenames:
                fpath = os.path.join(dirpath, "index.html")
                with open(fpath, encoding="utf-8") as f:
                    # Le <head> peut largement depasser une taille fixe (jusqu'a
                    # ~14 Ko sur les pages avec schema ItemList, cf. audit SEO du
                    # 2026-08-22 -- une lecture tronquee a 3500 octets a deja
                    # rate la balise noindex de ~35000 pages et gonfle le
                    # sitemap en consequence). On lit le fichier entier : le cout
                    # est negligeable au regard du reste du build.
                    head = f.read()
                if 'name="robots" content="noindex' in head:
                    continue
                rel = os.path.relpath(dirpath, DIST_DIR).replace(os.sep, "/")
                alternates = hreflang_re.findall(head)
                by_lang[lg].append(("/" + rel + "/", alternates))
    sitemap_files = []
    for lg in LANGS:
        urls = by_lang[lg]
        fname = f"sitemap-{lg}.xml"
        xml = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
        for p, alternates in urls:
            xml.append(f'  <url><loc>{BASE_DOMAIN}{p}</loc><lastmod>{today}</lastmod>')
            for hl, href in alternates:
                xml.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{href}"/>')
            xml.append('  </url>')
        xml.append("</urlset>")
        with open(os.path.join(DIST_DIR, fname), "w", encoding="utf-8") as f:
            f.write("\n".join(xml))
        sitemap_files.append(fname)
    idx = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for fname in sitemap_files:
        idx.append(f"  <sitemap><loc>{BASE_DOMAIN}/{fname}</loc><lastmod>{today}</lastmod></sitemap>")
    idx.append("</sitemapindex>")
    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(idx))
    print(f"sitemap.xml + {len(sitemap_files)} sous-sitemaps ({sum(len(v) for v in by_lang.values())} URLs, hreflang inclus)", file=sys.stderr)


# ---------------------------------------------------------------- IndexNow
# Cle stable (Bing/Yandex/Seznam/Naver partagent le meme protocole via
# api.indexnow.org) : ne jamais changer cette valeur, le fichier de
# verification a la racine et la cle utilisee dans chaque soumission doivent
# rester identiques indefiniment.
INDEXNOW_KEY = "7f3a9c14e8b5426a9d2f6c1e0a7b8d3f"


def gen_indexnow_key():
    with open(os.path.join(DIST_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)


def urls_for_domain(domain):
    """URLs (etude + avocats membres, 4 langues) dont le contenu depend d'un
    domaine de site web donne -- utilise pour cibler les soumissions IndexNow
    apres un lot d'enrichissement, sans avoir a resoumettre tout le site."""
    urls = []

    def _collect(code, firm, members):
        for lang in LANGS:
            urls.append(BASE_DOMAIN + etude_path(code, firm["_slug"], lang))
        for m in members:
            for lang in LANGS:
                urls.append(BASE_DOMAIN + avocat_path(code, m["_slug"], lang))

    for f in GE_FIRMS:
        members = MEMBERS_BY_FIRM_NORM.get(norm(f["etude"]), [])
        if any(site_domain(m.get("site_web")) == domain for m in members):
            _collect("GE", f, members)
    for r in GE_INDIVIDUALS:
        if not r.get("etude", "").strip() and site_domain(r.get("site_web")) == domain:
            for lang in LANGS:
                urls.append(BASE_DOMAIN + avocat_path("GE", r["_slug"], lang))
    for code, data in CANTON_DATA.items():
        for f in data["firms"]:
            if any(site_domain(m.get("site_web")) == domain for m in f["members"]):
                _collect(code, f, f["members"])
        for r in data["solo"]:
            if site_domain(r.get("site_web")) == domain:
                for lang in LANGS:
                    urls.append(BASE_DOMAIN + avocat_path(code, r["_slug"], lang))
    return sorted(set(urls))


def _dedup(rows):
    return list({id(r): r for r in rows}.values())


def gen_affected_for_domain(domain):
    """Regenere uniquement les pages etude + avocats dont le contenu depend
    de ce domaine de site web (fiche etude elle-meme, et fiches des avocats
    membres puisqu'elles heritent de l'insight/enrichissement du cabinet).

    Utilise par la tache planifiee apres un lot d'enrichissement cible, pour
    eviter un rebuild complet des ~66'000 pages du site a chaque execution
    (30 min) -- c'etait la cause directe du risque de saturation disque du
    bac a sable. Le deploiement de production (Vercel, sur chaque push)
    continue de faire un rebuild complet via `python3 build.py all` : cette
    fonction ne sert que pour la verification/ecriture locale ciblee avant
    de pousser, pas pour remplacer le build de reference."""
    written_before = len(URLS_GENERATED)

    ge_firms_touched = [
        f for f in GE_FIRMS
        if any(site_domain(m.get("site_web")) == domain
               for m in MEMBERS_BY_FIRM_NORM.get(norm(f["etude"]), []))
    ]
    if ge_firms_touched:
        gen_ge_etudes(rows=ge_firms_touched)
    ge_avocats_touched = [r for r in GE_INDIVIDUALS if site_domain(r.get("site_web")) == domain]
    for f in ge_firms_touched:
        ge_avocats_touched += MEMBERS_BY_FIRM_NORM.get(norm(f["etude"]), [])
    ge_avocats_touched = _dedup(ge_avocats_touched)
    if ge_avocats_touched:
        gen_ge_avocats(rows=ge_avocats_touched)

    for code, data in CANTON_DATA.items():
        firms_touched = [
            f for f in data["firms"]
            if any(site_domain(m.get("site_web")) == domain for m in f["members"])
        ]
        if firms_touched:
            gen_canton_etudes(code, rows=firms_touched)
        avocats_touched = [r for r in data["individuals"] if site_domain(r.get("site_web")) == domain]
        for f in firms_touched:
            avocats_touched += f["members"]
        avocats_touched = _dedup(avocats_touched)
        if avocats_touched:
            gen_canton_avocats(code, rows=avocats_touched)

    return len(URLS_GENERATED) - written_before


def gen_robots():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /search-index-*.json\n"
        "Disallow: /interne/\n"
        "\n"
        f"Sitemap: {BASE_DOMAIN}/sitemap.xml\n"
    )
    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(content)


def gen_search():
    for lang in LANGS:
        index = []
        for r in GE_INDIVIDUALS:
            index.append({
                "nom": r["nom_complet"].title(),
                "etude": r.get("etude", ""),
                "ville": r.get("ville", ""),
                "url": avocat_path("GE", r["_slug"], lang),
                "type": "avocat", "code": "GE", "slug": r["_slug"],
            })
        for r in GE_FIRMS:
            index.append({
                "nom": r["etude"],
                "etude": "",
                "ville": r.get("ville", ""),
                "url": etude_path("GE", r["_slug"], lang),
            })
        for code, data in CANTON_DATA.items():
            for r in data["individuals"]:
                index.append({
                    "nom": r["nom_complet"].title(),
                    "etude": r.get("etude", ""),
                    "ville": r.get("ville", ""),
                    "url": avocat_path(code, r["_slug"], lang),
                    "type": "avocat", "code": code, "slug": r["_slug"],
                })
            for f in data["firms"]:
                index.append({
                    "nom": f["etude"],
                    "etude": "",
                    "ville": f.get("ville", ""),
                    "url": etude_path(code, f["_slug"], lang),
                })
        json_path = os.path.join(DIST_DIR, f"search-index-{lang}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False)

        path = f"/{lang}/{seg('recherche', lang)}/"
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['search_title']} | Legatis", i18n.UI[lang]["tagline"] + ".",
                        hreflang_for(lambda lg: f"/{lg}/{seg('recherche', lg)}/"))
        ctx["search_index_url"] = f"/search-index-{lang}.json"
        ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (i18n.UI[lang]["search_title"], path)]
        write_page(path, render("search.html", ctx))


if __name__ == "__main__":
    copy_static()
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    if stage == "base":
        gen_home()
        gen_indexes()
        gen_coming_soon()
        gen_canton_hub_ge()
        gen_domain_hubs()
        gen_cross_ge()
        gen_static_pages()
        gen_villes()
        gen_ville_domaines()
        gen_guides()
        gen_blog()
        gen_etude_aj()
        gen_vitrines()
        gen_vitrine_review()
        gen_avis_request()
        gen_verification_contacts()
        gen_verification_request()
        gen_verification_confirmee()
        gen_verification_review()
        gen_analytics_dashboard()
        gen_connexion()
        gen_mon_profil()
        gen_llms_txt()
        gen_indexnow_key()
        gen_search()
    elif stage == "urls-for-domains":
        domains = sys.argv[2].split(",")
        seen = []
        for d in domains:
            for u in urls_for_domain(d.strip()):
                if u not in seen:
                    seen.append(u)
        print("\n".join(seen))
    elif stage == "affected":
        # Rebuild cible : ecrit uniquement les pages etude/avocat touchees par
        # les domaines donnes (+ index/sitemap NON regeneres -- production=Vercel).
        domains = sys.argv[2].split(",")
        total = 0
        for d in domains:
            total += gen_affected_for_domain(d.strip())
        print(f"{total} pages ecrites pour {len(domains)} domaine(s)", file=sys.stderr)
    elif stage == "etudes":
        start = int(sys.argv[2]); count = int(sys.argv[3])
        gen_ge_etudes(start, count)
    elif stage == "avocats":
        start = int(sys.argv[2]); count = int(sys.argv[3])
        gen_ge_avocats(start, count)
    elif stage == "canton-base":
        code = sys.argv[2]
        gen_canton_hub(code)
        gen_canton_cross(code)
    elif stage == "canton-etudes":
        code = sys.argv[2]; start = int(sys.argv[3]); count = int(sys.argv[4])
        gen_canton_etudes(code, start, count)
    elif stage == "canton-avocats":
        code = sys.argv[2]; start = int(sys.argv[3]); count = int(sys.argv[4])
        gen_canton_avocats(code, start, count)
    elif stage == "canton-full":
        code = sys.argv[2]
        gen_canton_hub(code)
        gen_canton_cross(code)
        gen_canton_etudes(code)
        gen_canton_avocats(code)
    elif stage == "other-cantons":
        for code in OTHER_CANTON_CODES:
            gen_canton_hub(code)
            gen_canton_cross(code)
            gen_canton_etudes(code)
            gen_canton_avocats(code)
    else:
        gen_home(); gen_indexes(); gen_coming_soon(); gen_canton_hub_ge()
        gen_domain_hubs(); gen_cross_ge(); gen_ge_etudes(); gen_ge_avocats()
        for code in OTHER_CANTON_CODES:
            gen_canton_hub(code)
            gen_canton_cross(code)
            gen_canton_etudes(code)
            gen_canton_avocats(code)
        gen_static_pages()
        gen_villes()
        gen_ville_domaines()
        gen_guides()
        gen_blog()
        gen_etude_aj()
        gen_vitrines()
        gen_vitrine_review()
        gen_avis_request()
        gen_verification_contacts()
        gen_verification_request()
        gen_verification_confirmee()
        gen_verification_review()
        gen_analytics_dashboard()
        gen_connexion()
        gen_mon_profil()
        gen_llms_txt()
        gen_indexnow_key()
        gen_search()
        gen_sitemaps()
        gen_robots()
    print(f"{len(URLS_GENERATED)} pages generees dans {DIST_DIR}", file=sys.stderr)
