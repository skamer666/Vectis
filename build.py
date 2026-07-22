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

from jinja2 import Environment, FileSystemLoader

sys.path.insert(0, os.path.dirname(__file__))
import i18n
import presentation_text as pt
import static_pages as sp_content
import guides_content

BASE_DOMAIN = "https://legatis.ch"
SITE_ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(SITE_ROOT, "templates")
DIST_DIR = os.path.join(SITE_ROOT, "dist")
DATA_DIR = os.path.join(SITE_ROOT, "data")
if not os.path.isdir(DATA_DIR):
    DATA_DIR = os.path.abspath(os.path.join(SITE_ROOT, "..", "..", "..", "..", "Vectis", "data"))
if not os.path.isdir(DATA_DIR):
    DATA_DIR = "/sessions/sweet-beautiful-heisenberg/mnt/Vectis/data"

LANGS = i18n.LANGUAGES

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "x"


def norm(text):
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", text).strip().lower()


def seg(name, lang):
    return i18n.SEGMENTS[name][lang]


def canton_path(canton_code, lang):
    c = i18n.CANTONS[canton_code][lang]
    return f"/{lang}/{seg('avocats', lang)}/{c['slug']}/"


def domaine_path(domaine_id, lang):
    d = i18n.DOMAINES[domaine_id][lang]
    return f"/{lang}/{seg('domaines', lang)}/{d['slug']}/"


def cross_path(canton_code, domaine_id, lang):
    c = i18n.CANTONS[canton_code][lang]
    d = i18n.DOMAINES[domaine_id][lang]
    return f"/{lang}/{seg('avocats', lang)}/{c['slug']}/{d['slug']}/"


def avocat_path(canton_code, lawyer_slug, lang):
    c = i18n.CANTONS[canton_code][lang]
    return f"/{lang}/{seg('avocats', lang)}/{c['slug']}/{seg('avocat', lang)}/{lawyer_slug}/"


def etude_path(canton_code, firm_slug, lang):
    c = i18n.CANTONS[canton_code][lang]
    return f"/{lang}/{seg('avocats', lang)}/{c['slug']}/{seg('etude', lang)}/{firm_slug}/"


def ville_path(canton_code, city_slug, lang):
    c = i18n.CANTONS[canton_code][lang]
    return f"/{lang}/{seg('avocats', lang)}/{c['slug']}/{seg('ville', lang)}/{city_slug}/"


def ville_domaine_path(canton_code, city_slug, domaine_id, lang):
    d = i18n.DOMAINES[domaine_id][lang]
    return ville_path(canton_code, city_slug, lang) + d["slug"] + "/"


def guides_index_path(lang):
    return f"/{lang}/{seg('guides', lang)}/"


def guide_path(gid, lang):
    return f"/{lang}/{seg('guides', lang)}/{guides_content.GUIDES[gid][lang]['slug']}/"


def home_path(lang):
    return f"/{lang}/"


def cantons_index_path(lang):
    return f"/{lang}/{seg('avocats', lang)}/"


def domaines_index_path(lang):
    return f"/{lang}/{seg('domaines', lang)}/"


def static_path(lang, depth):
    return "../" * depth + "static/"


def write_page(path, html):
    out = os.path.join(DIST_DIR, path.lstrip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    URLS_GENERATED.append(path)


URLS_GENERATED = []


def base_ctx(lang, path, title, description, extra_hreflang=None):
    depth = path.strip("/").count("/") + 1
    hreflang = extra_hreflang or {}
    return {
        "lang": lang,
        "title": title,
        "meta_description": description,
        "canonical_url": BASE_DOMAIN + path,
        "hreflang": hreflang,
        "nav_hreflang": {lg: (u[len(BASE_DOMAIN):] if u.startswith(BASE_DOMAIN) else u) for lg, u in hreflang.items()},
        "asset_prefix": static_path(lang, depth).replace("static/", ""),
        "home_url": home_path(lang),
        "cantons_index_url": cantons_index_path(lang),
        "domaines_index_url": domaines_index_path(lang),
        "guides_index_url": guides_index_path(lang),
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


def hreflang_for(path_fn, *args):
    return {lg: BASE_DOMAIN + path_fn(*args, lg) if args else BASE_DOMAIN + path_fn(lg) for lg in LANGS}


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


def derive_domain_firms(individuals, existing_slugs=None):
    """Regroupe par nom de domaine (site_web) les avocats sans nom d'etude en
    texte libre (cas de Vaud). Seuil : au moins 2 avocats partageant le meme
    domaine, OU un seul si ce domaine est deja confirme comme cabinet reel via
    le registre de Geneve ou le cache d'enrichissement web (source externe qui
    etablit deja la realite du cabinet). Rien n'est jamais fabrique : le nom
    vient du registre officiel quand connu, sinon d'un simple formatage du
    domaine deja declare par l'avocat."""
    seen_slugs = dict(existing_slugs or {})
    by_domain = {}
    for r in individuals:
        if (r.get("etude") or "").strip():
            continue
        d = site_domain(r.get("site_web"))
        if not d:
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
    ctx["extra_schema"] = extra
    return env.get_template(template_name).render(**ctx)


# ---------------------------------------------------------------- pages

def gen_home():
    for lang in LANGS:
        path = home_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['site_name']} — {i18n.UI[lang]['tagline']}",
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
            {"name": i18n.CANTONS[c][lang]["name"], "url": canton_path(c, lang), "count": CANTON_COUNTS.get(c, 0)}
            for c in i18n.CANTONS
        ]
        ctx["domaines"] = [
            {"name": i18n.DOMAINES[d][lang]["name"], "url": domaine_path(d, lang)} for d in i18n.DOMAINES
        ]
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


def gen_ge_avocats(start=0, count=None):
    canton_name_fr = i18n.CANTONS["GE"]["fr"]["name"]
    subset = GE_INDIVIDUALS[start:start + count] if count else GE_INDIVIDUALS[start:]
    for row in subset:
        nom = row["nom_complet"].title()
        firm_row = FIRM_BY_NORM.get(norm(row.get("etude", "")))
        domaine_ids = domaines_for_lawyer(row)
        same_city = [r for r in BY_CITY.get(row["ville"], []) if r["_slug"] != row["_slug"]][:6]
        for lang in LANGS:
            canton_name = i18n.CANTONS["GE"][lang]["name"]
            path = avocat_path("GE", row["_slug"], lang)
            title = f"{nom} — {i18n.UI[lang]['firm'] if not row.get('etude') else row.get('etude')} | {i18n.UI[lang]['canton']} {canton_name}"
            desc = pt.lawyer_presentation(lang, nom, canton_name, etude=row.get("etude") or None,
                                           ville=row.get("ville") or None,
                                           domaines=[i18n.DOMAINES[d][lang]["name"] for d in domaine_ids])[:158]
            ctx = base_ctx(lang, path, f"{nom} — {i18n.UI[lang]['site_name']}", desc,
                            {lg: avocat_path("GE", row["_slug"], lg) for lg in LANGS})
            ctx["nom"] = nom
            ctx["canton_name"] = canton_name
            ctx["role_or_titre"] = row.get("fonction") or ""
            ctx["etude"] = row.get("etude") or ""
            ctx["etude_url"] = etude_path("GE", firm_row["_slug"], lang) if firm_row else None
            ctx["adresse"] = row.get("adresse") or ""
            ctx["npa"] = row.get("npa") or ""
            ctx["ville"] = row.get("ville") or ""
            ctx["telephone"] = row.get("telephone") or ""
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
            _raw_langues = [l.strip() for l in (row.get("langues") or "").split(";") if l.strip()]
            ctx["langues"] = pt.translate_langues(_raw_langues, lang)
            ctx["seniority_text"] = pt.seniority_text(lang, row.get("brevet_date"))
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path("GE", lang)), (nom, path)]
            _schema = {
                "@context": "https://schema.org", "@type": "Attorney", "name": nom,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": row.get("telephone", ""), "email": row.get("email", ""),
                "areaServed": canton_name,
            }
            if _raw_langues:
                _lang_map = {"français": "fr", "allemand": "de", "italien": "it", "anglais": "en",
                             "espagnol": "es", "portugais": "pt", "arabe": "ar", "russe": "ru",
                             "romanche": "rm"}
                _codes = [_lang_map.get(l.lower()) for l in _raw_langues]
                _schema["knowsLanguage"] = [c for c in _codes if c] or _raw_langues
            ctx["schema"] = json.dumps(_schema, ensure_ascii=False)
            write_page(path, render("avocat.html", ctx))


def gen_ge_etudes(start=0, count=None):
    subset = GE_FIRMS[start:start + count] if count else GE_FIRMS[start:]
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
        for lang in LANGS:
            canton_name = i18n.CANTONS["GE"][lang]["name"]
            path = etude_path("GE", row["_slug"], lang)
            desc = pt.firm_presentation(lang, nom_etude, canton_name, ville=row.get("ville"), n_membres=n)[:158]
            ctx = base_ctx(lang, path, f"{nom_etude} — {i18n.UI[lang]['firm']} {canton_name} | Legatis", desc,
                            {lg: etude_path("GE", row["_slug"], lg) for lg in LANGS})
            ctx["nom_etude"] = nom_etude
            ctx["canton_name"] = canton_name
            ctx["adresse"] = row.get("adresse", "")
            ctx["npa"] = row.get("npa", "")
            ctx["ville"] = row.get("ville", "")
            ctx["presentation"] = pt.firm_presentation(lang, nom_etude, canton_name, ville=row.get("ville"), n_membres=n)
            ctx["members_title"] = (
                {"fr": "Avocats de l'étude", "de": "Anwältinnen und Anwälte der Kanzlei",
                 "it": "Avvocati dello studio", "en": "Lawyers at this firm"}[lang])
            if matched:
                ctx["membres"] = [
                    {"nom": m["nom_complet"].title(), "role": m.get("fonction", ""), "fonction": m.get("fonction", ""),
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
                ctx["membres"] = [{"nom": m["nom"], "role": m["fonction"], "fonction": m["fonction"],
                                    "url": None} for m in fallback_members]
            _domaine_names = [i18n.DOMAINES[d][lang]["name"] for d in _team_domaine_ids]
            if not _domaine_names and _web:
                if lang == "fr" and _web.get("practice_areas_fr"):
                    _domaine_names = _web["practice_areas_fr"]
                elif lang == "en" and _web.get("practice_areas_en"):
                    _domaine_names = _web["practice_areas_en"]
            ctx["insight_text"] = pt.firm_insight(
                lang, pt.translate_langues(_team_langues, lang), _domaine_names, _oldest_year,
                founding_year=(_web or {}).get("founding_year"),
                team_size_n=(_web or {}).get("team_size_n"),
            )
            # Noindex automatique : la fiche n'a aucun signal reel au-dela du nom/adresse/
            # liste de membres (ni annee de fondation, ni taille d'equipe, ni langues, ni
            # domaines de competence). Se retire tout seul au prochain build des qu'une
            # donnee reelle arrive (registre ou enrichissement web) -- rien a faire a la main.
            ctx["noindex"] = not ctx["insight_text"]
            ctx["web_source_note"] = None
            if _web:
                ctx["web_source_note"] = {
                    "fr": f"Certaines informations ci-dessus proviennent du site officiel du cabinet, consulté le {_web['fetched_date']}.",
                    "de": f"Einige der obigen Angaben stammen von der offiziellen Website der Kanzlei, abgerufen am {_web['fetched_date']}.",
                    "it": f"Alcune informazioni sopra riportate provengono dal sito ufficiale dello studio, consultato il {_web['fetched_date']}.",
                    "en": f"Some information above comes from the firm's official website, accessed on {_web['fetched_date']}.",
                }[lang]
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path("GE", lang)), (nom_etude, path)]
            _schema = {
                "@context": "https://schema.org", "@type": "LegalService", "name": nom_etude,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": row.get("telephone", ""),
            }
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
        desc = pt.canton_intro(lang, canton_name, CANTON_COUNTS["GE"])[:158]
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['find_a_lawyer_near']} {canton_name} | Legatis", desc,
                        {lg: canton_path("GE", lg) for lg in LANGS})
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
            desc = pt.domaine_intro(lang, dname)[:158]
            ctx = base_ctx(lang, path, f"{dname} — {i18n.UI[lang]['find_a_lawyer']} | Legatis", desc,
                            {lg: domaine_path(did, lg) for lg in LANGS})
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
            desc = pt.cross_intro(lang, dname, canton_name)[:158]
            ctx = base_ctx(lang, path, f"{dname} {i18n.UI[lang]['in']} {canton_name} | Legatis", desc,
                            {lg: cross_path("GE", did, lg) for lg in LANGS})
            ctx["domaine_name"] = dname
            ctx["canton_name"] = canton_name
            ctx["h1"] = pt.cross_h1(lang, dname, canton_name)
            ctx["intro_text"] = pt.cross_intro(lang, dname, canton_name)
            ctx["avocats"] = [
                {"nom": r["nom_complet"].title(), "url": avocat_path("GE", r["_slug"], lang),
                 "etude": r.get("etude", ""), "ville": r.get("ville", ""), "role": r.get("fonction", "")}
                for r in matches
            ]
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
        desc = pt.canton_intro(lang, canton_name, n_total)[:158]
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['find_a_lawyer_near']} {canton_name} | Legatis", desc,
                        {lg: canton_path(code, lg) for lg in LANGS})
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
            desc = pt.cross_intro(lang, dname, canton_name)[:158]
            ctx = base_ctx(lang, path, f"{dname} {i18n.UI[lang]['in']} {canton_name} | Legatis", desc,
                            {lg: cross_path(code, did, lg) for lg in LANGS})
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


def gen_canton_etudes(code, start=0, count=None):
    data = CANTON_DATA[code]
    subset = data["firms"][start:start + count] if count else data["firms"][start:]
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
        for lang in LANGS:
            canton_name = i18n.CANTONS[code][lang]["name"]
            path = etude_path(code, f["_slug"], lang)
            desc = pt.firm_presentation(lang, nom_etude, canton_name, ville=ville, n_membres=n)[:158]
            ctx = base_ctx(lang, path, f"{nom_etude} — {i18n.UI[lang]['firm']} {canton_name} | Legatis", desc,
                            {lg: etude_path(code, f["_slug"], lg) for lg in LANGS})
            ctx["nom_etude"] = nom_etude
            ctx["canton_name"] = canton_name
            ctx["adresse"] = adresse
            ctx["npa"] = npa
            ctx["ville"] = ville
            ctx["presentation"] = pt.firm_presentation(lang, nom_etude, canton_name, ville=ville, n_membres=n)
            ctx["members_title"] = (
                {"fr": "Avocats de l'étude", "de": "Anwältinnen und Anwälte der Kanzlei",
                 "it": "Avvocati dello studio", "en": "Lawyers at this firm"}[lang])
            ctx["membres"] = [
                {"nom": m["nom_complet"].title(), "role": m.get("fonction", ""), "fonction": m.get("fonction", ""),
                 "url": avocat_path(code, m["_slug"], lang)}
                for m in members
            ]
            _domaine_names = []
            if _web:
                if lang == "fr" and _web.get("practice_areas_fr"):
                    _domaine_names = _web["practice_areas_fr"]
                elif lang == "en" and _web.get("practice_areas_en"):
                    _domaine_names = _web["practice_areas_en"]
            ctx["insight_text"] = pt.firm_insight(
                lang, [], _domaine_names, _oldest_year,
                founding_year=(_web or {}).get("founding_year"),
                team_size_n=(_web or {}).get("team_size_n"),
            )
            # Noindex automatique : voir commentaire equivalent dans gen_ge_etudes.
            ctx["noindex"] = not ctx["insight_text"]
            ctx["web_source_note"] = None
            if _web:
                ctx["web_source_note"] = {
                    "fr": f"Certaines informations ci-dessus proviennent du site officiel du cabinet, consulté le {_web['fetched_date']}.",
                    "de": f"Einige der obigen Angaben stammen von der offiziellen Website der Kanzlei, abgerufen am {_web['fetched_date']}.",
                    "it": f"Alcune informazioni sopra riportate provengono dal sito ufficiale dello studio, consultato il {_web['fetched_date']}.",
                    "en": f"Some information above comes from the firm's official website, accessed on {_web['fetched_date']}.",
                }[lang]
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path(code, lang)), (nom_etude, path)]
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "LegalService", "name": nom_etude,
                "address": {"@type": "PostalAddress", "streetAddress": adresse,
                             "postalCode": npa, "addressLocality": ville, "addressCountry": "CH"},
                "telephone": telephone,
            }, ensure_ascii=False)
            write_page(path, render("etude.html", ctx))


def gen_canton_avocats(code, start=0, count=None):
    data = CANTON_DATA[code]
    individuals = data["individuals"]
    by_city = data["by_city"]
    firm_by_norm = data["firm_by_norm"]
    subset = individuals[start:start + count] if count else individuals[start:]
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
        for lang in LANGS:
            canton_name = i18n.CANTONS[code][lang]["name"]
            path = avocat_path(code, row["_slug"], lang)
            desc = pt.lawyer_presentation(lang, nom, canton_name, etude=etude_name or None,
                                           ville=row.get("ville") or None,
                                           fonction=row.get("fonction") or None)[:158]
            ctx = base_ctx(lang, path, f"{nom} — {i18n.UI[lang]['site_name']}", desc,
                            {lg: avocat_path(code, row["_slug"], lg) for lg in LANGS})
            ctx["nom"] = nom
            ctx["canton_name"] = canton_name
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
            ctx["langues"] = []
            ctx["seniority_text"] = pt.seniority_text(lang, row.get("annee_admission"))
            _domaine_names = []
            if _web:
                if lang == "fr" and _web.get("practice_areas_fr"):
                    _domaine_names = _web["practice_areas_fr"]
                elif lang == "en" and _web.get("practice_areas_en"):
                    _domaine_names = _web["practice_areas_en"]
            ctx["insight_text"] = pt.firm_insight(
                lang, [], _domaine_names, None,
                founding_year=(_web or {}).get("founding_year"),
                team_size_n=(_web or {}).get("team_size_n"),
            ) if _web else ""
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
            # donnee reelle arrive (meme mecanisme que les fiches etude).
            ctx["noindex"] = not (ctx["seniority_text"] or ctx["langues"] or ctx["domaines"] or ctx["insight_text"])
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path(code, lang)), (nom, path)]
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "Attorney", "name": nom,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": row.get("telephone", ""), "email": row.get("email", ""),
                "areaServed": canton_name,
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


def city_display(ville):
    return CANTON_CODE_SUFFIX_RE.sub("", ville or "").strip()


def build_city_data():
    """Regroupe les avocats par ville (nom postal nettoye) pour chaque canton.
    Seules les villes non eponymes du canton et comptant au moins
    CITY_MIN_LAWYERS avocats donnent lieu a une page (anti-thin-content :
    on ne genere pas de coquilles vides, plutot que de les generer en noindex)."""
    out = {}
    pools = {"GE": GE_INDIVIDUALS}
    for code, data in CANTON_DATA.items():
        pools[code] = data["individuals"]
    for code, individuals in pools.items():
        groups = {}
        for r in individuals:
            disp = city_display(r.get("ville", ""))
            if not disp:
                continue
            key = norm(disp)
            if key in _EPONYMOUS_NORMS:
                continue
            g = groups.setdefault(key, {"name": disp, "members": []})
            g["members"].append(r)
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
                title = f"{i18n.UI[lang]['find_a_lawyer_near']} {city['name']} | Legatis"
                ctx = base_ctx(lang, path, title, intro[:158],
                                {lg: ville_path(code, city["slug"], lg) for lg in LANGS})
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
                    desc = pt.cross_intro(lang, dname, city["name"])[:158]
                    ctx = base_ctx(lang, path, f"{dname} {i18n.UI[lang]['in']} {city['name']} | Legatis", desc,
                                    {lg: ville_domaine_path(code, city["slug"], did, lg) for lg in LANGS})
                    ctx["domaine_name"] = dname
                    ctx["canton_name"] = canton_name
                    ctx["h1"] = pt.cross_h1(lang, dname, city["name"])
                    ctx["intro_text"] = pt.cross_intro(lang, dname, city["name"])
                    ctx["avocats"] = [
                        {"nom": r["nom_complet"].title(), "url": avocat_path(code, r["_slug"], lang),
                         "etude": r.get("etude", ""), "ville": r.get("ville", ""), "role": r.get("fonction", "")}
                        for r in matches
                    ]
                    ctx["list_title"] = i18n.UI[lang]["all_practice_areas"]
                    ctx["no_specialty_text"] = ""
                    ctx["fallback_avocats"] = []
                    ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                          (canton_name, canton_path(code, lang)),
                                          (city["name"], ville_path(code, city["slug"], lang)),
                                          (dname, path)]
                    write_page(path, render("cross.html", ctx))


def canton_villes_links(code, lang):
    """Liens vers les pages villes d'un canton (maillage interne du hub canton)."""
    return [
        {"name": c["name"], "url": ville_path(code, c["slug"], lang), "count": c["count"]}
        for c in CITY_DATA.get(code, [])
    ]


# ---------------------------------------------------------------- guides

GUIDES_INDEX_INTRO = {
    "fr": "Des guides pratiques pour comprendre comment travailler avec un avocat en Suisse : choix, coûts, assistance judiciaire, spécialisations.",
    "de": "Praktische Ratgeber zur Zusammenarbeit mit Anwältinnen und Anwälten in der Schweiz: Auswahl, Kosten, unentgeltliche Rechtspflege, Spezialisierungen.",
    "it": "Guide pratiche per capire come lavorare con un avvocato in Svizzera: scelta, costi, gratuito patrocinio, specializzazioni.",
    "en": "Practical guides to working with a lawyer in Switzerland: choosing one, costs, legal aid, specialisations.",
}


def gen_guides():
    gids = list(guides_content.GUIDES.keys())
    for lang in LANGS:
        path = guides_index_path(lang)
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['guides_title']} | Legatis",
                        GUIDES_INDEX_INTRO[lang][:158], hreflang_for(guides_index_path))
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
            ctx = base_ctx(lang, path, f"{g['title']} | Legatis", g["meta"][:158],
                            {lg: guide_path(gid, lg) for lg in LANGS})
            ctx["page_title"] = g["title"]
            ctx["sections"] = g["sections"]
            ctx["faq"] = g["faq"]
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


STATIC_PAGE_IDS = ["methodologie", "a-propos", "contact", "mentions-legales", "confidentialite", "correction"]


def gen_static_pages():
    for page_id in STATIC_PAGE_IDS:
        for lang in LANGS:
            content = sp_content.get_page(page_id, lang)
            path = f"/{lang}/{seg(page_id, lang)}/"
            desc = (content["sections"][0]["paragraphs"][0])[:158]
            ctx = base_ctx(lang, path, f"{content['title']} | Legatis", desc,
                            {lg: f"/{lg}/{seg(page_id, lg)}/" for lg in LANGS})
            ctx["page_title"] = content["title"]
            ctx["sections"] = content["sections"]
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)), (content["title"], path)]
            write_page(path, render("page.html", ctx))


def gen_sitemaps():
    today = datetime.date.today().isoformat()
    by_lang = {lg: [] for lg in LANGS}
    for lg in LANGS:
        lang_dir = os.path.join(DIST_DIR, lg)
        for dirpath, _dirnames, filenames in os.walk(lang_dir):
            if "index.html" in filenames:
                fpath = os.path.join(dirpath, "index.html")
                with open(fpath, encoding="utf-8") as f:
                    head = f.read(2500)
                if 'name="robots" content="noindex' in head:
                    continue
                rel = os.path.relpath(dirpath, DIST_DIR).replace(os.sep, "/")
                by_lang[lg].append("/" + rel + "/")
    sitemap_files = []
    for lg in LANGS:
        urls = by_lang[lg]
        fname = f"sitemap-{lg}.xml"
        xml = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for p in urls:
            xml.append(f"  <url><loc>{BASE_DOMAIN}{p}</loc><lastmod>{today}</lastmod></url>")
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
    print(f"sitemap.xml + {len(sitemap_files)} sous-sitemaps ({sum(len(v) for v in by_lang.values())} URLs)", file=sys.stderr)


def gen_robots():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /search-index-*.json\n"
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
        gen_llms_txt()
        gen_search()
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
        gen_llms_txt()
        gen_search()
        gen_sitemaps()
        gen_robots()
    print(f"{len(URLS_GENERATED)} pages generees dans {DIST_DIR}", file=sys.stderr)
