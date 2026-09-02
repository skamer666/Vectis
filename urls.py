#!/usr/bin/env python3
"""
Construction des URLs (routing) du site Legatis : point unique de verite pour
la structure des chemins, separe de la logique de chargement des donnees et
de generation des pages. Module pur -- aucune I/O, aucune dependance aux CSV
ou au systeme de fichiers dist/, uniquement i18n.py et guides_content.py.

Extrait de build.py pour reduire la taille du fichier monolithique et isoler
un concept clair (routing) que l'on peut lire, tester et faire evoluer sans
toucher a la generation de pages elle-meme.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import i18n
import guides_content
import blog_content

# www est le domaine effectivement servi par Vercel (l'apex legatis.ch redirige
# vers www.legatis.ch en production) -- canonical/hreflang/sitemap doivent
# pointer vers l'URL qui repond reellement 200, sans quoi Google recoit des
# signaux de canonicalisation contradictoires (canonical sur une URL qui ne
# sert jamais de contenu directement, cf. audit SEO du 2026-08-22).
BASE_DOMAIN = "https://www.legatis.ch"
LANGS = i18n.LANGUAGES


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


def langue_path(canton_code, langue_id, lang):
    c = i18n.CANTONS[canton_code][lang]
    l = i18n.LANGUES[langue_id][lang]
    return f"/{lang}/{seg('avocats', lang)}/{c['slug']}/{seg('langue', lang)}/{l['slug']}/"


def ville_langue_path(canton_code, city_slug, langue_id, lang):
    l = i18n.LANGUES[langue_id][lang]
    return ville_path(canton_code, city_slug, lang) + f"{seg('langue', lang)}/{l['slug']}/"


def guides_index_path(lang):
    return f"/{lang}/{seg('guides', lang)}/"


def guide_path(gid, lang):
    return f"/{lang}/{seg('guides', lang)}/{guides_content.GUIDES[gid][lang]['slug']}/"


def blog_index_path(lang):
    return f"/{lang}/{seg('blog', lang)}/"


def blog_article_path(bid, lang):
    return f"/{lang}/{seg('blog', lang)}/{blog_content.BLOG_ARTICLES[bid][lang]['slug']}/"


def home_path(lang):
    return f"/{lang}/"


def cantons_index_path(lang):
    return f"/{lang}/{seg('avocats', lang)}/"


def domaines_index_path(lang):
    return f"/{lang}/{seg('domaines', lang)}/"


def etude_aj_path(lang):
    return f"/{lang}/{seg('etude-aj', lang)}/"


def vitrine_path(slug, lang):
    return f"/{lang}/{seg('vitrine', lang)}/{slug}/"


def avis_request_path(lang):
    return f"/{lang}/{seg('avis-demande', lang)}/"


def verification_request_path(lang):
    return f"/{lang}/{seg('verification-demande', lang)}/"


def verification_confirmee_path(lang):
    return f"/{lang}/{seg('verification-confirmee', lang)}/"


def connexion_path(lang):
    return f"/{lang}/{seg('connexion', lang)}/"


def mon_profil_path(lang):
    return f"/{lang}/{seg('mon-profil', lang)}/"


def static_path(lang, depth):
    return "../" * depth + "static/"


def hreflang_for(path_fn, *args):
    return {lg: BASE_DOMAIN + path_fn(*args, lg) if args else BASE_DOMAIN + path_fn(lg) for lg in LANGS}
