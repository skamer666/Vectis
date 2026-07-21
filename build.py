#!/usr/bin/env python3
"""
Generateur statique du site Legatis (pilote canton de Geneve, 4 langues).
Lit les CSV deja collectes dans data/, genere du HTML statique via Jinja2.
"""
import csv
import json
import os
import re
import sys
import unicodedata

from jinja2 import Environment, FileSystemLoader

sys.path.insert(0, os.path.dirname(__file__))
import i18n
import presentation_text as pt

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


def render(template_name, ctx):
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
        ctx["stats"] = {
            "total_avocats": sum(v for v in CANTON_COUNTS.values() if v),
            "total_cantons": len(i18n.CANTONS),
            "total_etudes": len(GE_FIRMS),
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
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path("GE", lang)), (nom, path)]
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "Attorney", "name": nom,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": row.get("telephone", ""), "email": row.get("email", ""),
                "areaServed": canton_name,
            }, ensure_ascii=False)
            write_page(path, render("avocat.html", ctx))


def gen_ge_etudes(start=0, count=None):
    subset = GE_FIRMS[start:start + count] if count else GE_FIRMS[start:]
    for row in subset:
        nom_etude = row["etude"]
        matched = MEMBERS_BY_FIRM_NORM.get(norm(nom_etude), [])
        n = len(matched) if matched else int(row.get("nb_avocats") or 0)
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
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path("GE", lang)), (nom_etude, path)]
            ctx["schema"] = json.dumps({
                "@context": "https://schema.org", "@type": "LegalService", "name": nom_etude,
                "address": {"@type": "PostalAddress", "streetAddress": row.get("adresse", ""),
                             "postalCode": row.get("npa", ""), "addressLocality": row.get("ville", ""),
                             "addressCountry": "CH"},
                "telephone": row.get("telephone", ""),
            }, ensure_ascii=False)
            write_page(path, render("etude.html", ctx))


def gen_canton_hub_ge():
    for lang in LANGS:
        canton_name = i18n.CANTONS["GE"][lang]["name"]
        path = canton_path("GE", lang)
        desc = pt.canton_intro(lang, canton_name, CANTON_COUNTS["GE"])[:158]
        ctx = base_ctx(lang, path, f"{i18n.UI[lang]['find_a_lawyer_near']} {canton_name} | Legatis", desc,
                        {lg: canton_path("GE", lg) for lg in LANGS})
        ctx["canton_name"] = canton_name
        ctx["intro_text"] = pt.canton_intro(lang, canton_name, CANTON_COUNTS["GE"])
        ctx["domaines"] = [{"name": i18n.DOMAINES[d][lang]["name"], "url": cross_path("GE", d, lang), "has_data": False}
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
            ctx["avocats"] = []  # GE n'a pas de specialites structurees pour l'instant
            ctx["list_title"] = i18n.UI[lang]["all_practice_areas"]
            ctx["no_specialty_text"] = pt.cross_fallback_text(lang, dname, canton_name)
            ctx["fallback_avocats"] = fallback_by_lang[lang]
            ctx["breadcrumb"] = [(i18n.UI[lang]["breadcrumb_home"], home_path(lang)),
                                  (canton_name, canton_path("GE", lang)), (dname, path)]
            write_page(path, render("cross.html", ctx))


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
        gen_search()
    elif stage == "etudes":
        start = int(sys.argv[2]); count = int(sys.argv[3])
        gen_ge_etudes(start, count)
    elif stage == "avocats":
        start = int(sys.argv[2]); count = int(sys.argv[3])
        gen_ge_avocats(start, count)
    else:
        gen_home(); gen_indexes(); gen_coming_soon(); gen_canton_hub_ge()
        gen_domain_hubs(); gen_cross_ge(); gen_search(); gen_ge_etudes(); gen_ge_avocats()
    print(f"{len(URLS_GENERATED)} pages generees dans {DIST_DIR}", file=sys.stderr)
