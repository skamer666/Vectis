#!/usr/bin/env python3
"""
Contenu de la page dediee a l'etude comparative sur l'assistance judiciaire
(taux de majoration cantonaux). Charge les donnees factuelles (data.json,
jamais modifiees ici) et les chaines traduites (i18n.json) preparees pour le
document Word/PDF, et expose page_context(lang) : un dict pret a etre passe
au template Jinja etude_aj.html, avec les templates a substitution deja
resolus (meme logique que fmt() dans build_etude_i18n.js, cote docx).

Aucun fait n'est modifie ici : ce module ne fait que mettre en forme des
donnees deja verifiees (voir data/aj_study/data.json).
"""
import json
import os
import re

_DIR = os.path.join(os.path.dirname(__file__), "data", "aj_study")

with open(os.path.join(_DIR, "data.json"), encoding="utf-8") as f:
    DATA = json.load(f)

with open(os.path.join(_DIR, "i18n.json"), encoding="utf-8") as f:
    I18N = json.load(f)

STRINGS = I18N["strings"]
NOTES = I18N["notes"]
CANTON_NAMES = I18N["cantonNames"]

WORD_NUM = {
    2: {"fr": "Deux", "de": "Zwei", "it": "Due", "en": "Two"},
    4: {"fr": "Quatre", "de": "Vier", "it": "Quattro", "en": "Four"},
}

# Chaines additionnelles specifiques a la page web (pas dans le PDF) : nav,
# libelles d'interactivite. Cle plate {champ: {lang: texte}}.
PAGE_STRINGS = {
    "nav_essentials": {"fr": "L'essentiel", "de": "Das Wichtigste", "it": "L'essenziale", "en": "Essentials"},
    "nav_chart": {"fr": "Vue d'ensemble", "de": "Übersicht", "it": "Panoramica", "en": "Overview"},
    "nav_confirmed": {"fr": "Cantons confirmés", "de": "Bestätigte Kantone", "it": "Cantoni confermati", "en": "Confirmed cantons"},
    "nav_single": {"fr": "Source unique", "de": "Einzelquelle", "it": "Fonte unica", "en": "Single source"},
    "nav_disc": {"fr": "Discrétionnaire", "de": "Ermessenspraxis", "it": "Discrezionale", "en": "Discretionary"},
    "nav_excl": {"fr": "Sans donnée", "de": "Ohne Daten", "it": "Senza dati", "en": "No data"},
    "nav_case": {"fr": "Simulation", "de": "Fallbeispiel", "it": "Simulazione", "en": "Case study"},
    "nav_method": {"fr": "Méthodologie", "de": "Methodik", "it": "Metodologia", "en": "Methodology"},
    "nav_annex": {"fr": "Sources", "de": "Quellen", "it": "Fonti", "en": "Sources"},
    "expand_hint": {"fr": "Voir les décisions citées", "de": "Zitierte Entscheide anzeigen", "it": "Vedi le decisioni citate", "en": "View cited decisions"},
    "decisions_word": {"fr": "décisions", "de": "Entscheide", "it": "decisioni", "en": "decisions"},
    "decision_word": {"fr": "décision", "de": "Entscheid", "it": "decisione", "en": "decision"},
    "pdf_note": {"fr": "Version PDF complète, avec mise en page imprimable, disponible en téléchargement.", "de": "Vollständige PDF-Version mit druckfähigem Layout zum Download verfügbar.", "it": "Versione PDF completa, con impaginazione stampabile, disponibile per il download.", "en": "A full printable PDF version is available for download."},
    "download_pdf": {"fr": "Télécharger le PDF", "de": "PDF herunterladen", "it": "Scarica il PDF", "en": "Download the PDF"},
    "profile_col_head": {"fr": "Profil (minimum vital de base)", "de": "Profil (Existenzminimum)", "it": "Profilo (minimo vitale di base)", "en": "Profile (basic minimum)"},
    "meta_description": {
        "fr": "Étude Legatis : le taux de majoration du minimum vital pour l'assistance judiciaire varie de 0% à 30% selon le canton suisse. 18 cantons confirmés, 135+ décisions de justice vérifiées.",
        "de": "Legatis-Studie: Der Zuschlag auf das Existenzminimum für die unentgeltliche Rechtspflege variiert je nach Schweizer Kanton zwischen 0% und 30%. 18 bestätigte Kantone, über 135 überprüfte Gerichtsentscheide.",
        "it": "Studio Legatis: il tasso di maggiorazione del minimo vitale per il gratuito patrocinio varia dallo 0% al 30% a seconda del Cantone svizzero. 18 Cantoni confermati, oltre 135 decisioni giudiziarie verificate.",
        "en": "Legatis study: the legal-aid surcharge applied to the basic subsistence minimum ranges from 0% to 30% depending on the Swiss canton. 18 confirmed cantons, 135+ verified court decisions.",
    },
}

RATE_GROUPS = [
    {"rate": 0, "codes": ["TI"]},
    {"rate": 15, "codes": ["BL", "BS"]},
    {"rate": 20, "codes": ["LU", "GR", "SO", "ZG", "NW", "UR"]},
    {"rate": 25, "codes": ["GE", "JU", "AG", "FR", "VS"]},
    {"rate": 30, "codes": ["SZ", "BE", "SG", "AI"]},
]

PROFILES = [
    {"key": "profile_single", "base": 1200},
    {"key": "profile_mono", "base": 1350},
    {"key": "profile_couple", "base": 1700},
]


def fmt(tpl, **vars):
    return re.sub(r"\{(\w+)\}", lambda m: str(vars.get(m.group(1), "")), tpl or "")


def confirmed_sorted():
    return sorted(DATA["confirmed"], key=lambda c: (c["rate"], c["canton"]))


def canton_name(code, lang):
    return CANTON_NAMES.get(code, {}).get(lang, code)


def note(code, field, lang):
    return NOTES.get(code, {}).get(field, {}).get(lang, "")


def rate_color(rate):
    if rate <= 15:
        return "#1b6b1b"
    if rate >= 30:
        return "#b00000"
    return "#1a3a6b"


def page_context(lang):
    S = STRINGS[lang]
    confirmed_raw = confirmed_sorted()
    n_confirmed = len(confirmed_raw)
    n_single = len(DATA["single_source"])
    n_disc = len(DATA["discretionary"])
    n_excl = len(DATA["excluded"])
    total_decisions = sum(c.get("decision_count") or len(c["decisions"]) for c in confirmed_raw)
    total_decisions += sum(c.get("decision_count") or len(c["decisions"]) for c in DATA["single_source"])
    ns_word = WORD_NUM.get(n_single, {}).get(lang, str(n_single))
    nd_word = WORD_NUM.get(n_disc, {}).get(lang, str(n_disc))

    t = dict(S)
    for k, v in PAGE_STRINGS.items():
        t[k] = v[lang]
    t["cover_caption"] = fmt(S.get("cover_caption_tpl"), n=total_decisions)
    t["digest_2"] = fmt(S.get("digest_2_tpl"), n=n_confirmed)
    t["digest_4"] = fmt(S.get("digest_4_tpl"), ns=n_single, nd=n_disc, ne=n_excl)
    t["digest_5"] = fmt(S.get("digest_5_tpl"), n=total_decisions)
    t["synth_p2"] = fmt(S.get("synth_p2_tpl"), n=total_decisions, nc=n_confirmed, ns=n_single)
    t["synth_p5"] = fmt(S.get("synth_p5_tpl"), ns=n_single, nd=n_disc, ne=n_excl)
    t["method_p3"] = fmt(S.get("method_p3_tpl"), n=total_decisions)
    t["h_chart"] = fmt(S.get("h_chart_tpl"), n=n_confirmed)
    t["h_table"] = fmt(S.get("h_table_tpl"), n=n_confirmed)
    t["h_single"] = fmt(S.get("h_single_tpl"), n=ns_word)
    t["h_disc"] = fmt(S.get("h_disc_tpl"), n=nd_word)
    t["conclusion_p1"] = fmt(S.get("conclusion_p1_tpl"), n=n_confirmed)
    t["cover_caption_note"] = t["cover_caption"]

    confirmed = []
    for c in confirmed_raw:
        confirmed.append({
            "code": c["code"],
            "name": canton_name(c["code"], lang),
            "rate": c["rate"],
            "color": rate_color(c["rate"]),
            "decision_count": c.get("decision_count") or len(c["decisions"]),
            "decisions": c["decisions"],
            "note": note(c["code"], "note", lang),
        })

    single = []
    for c in DATA["single_source"]:
        single.append({
            "code": c["code"],
            "name": canton_name(c["code"], lang),
            "rate": c["rate"],
            "decision_count": c.get("decision_count") or len(c["decisions"]),
            "decisions": c["decisions"],
            "note": note(c["code"], "single_source_note", lang),
        })

    disc = []
    for c in DATA["discretionary"]:
        disc.append({
            "code": c["code"],
            "name": canton_name(c["code"], lang),
            "range": c["range"],
            "source": note(c["code"], "source", lang),
            "note": note(c["code"], "note", lang),
        })

    excl = []
    for c in DATA["excluded"]:
        excl.append({
            "code": c["code"],
            "name": canton_name(c["code"], lang),
            "reason": note(c["code"], "reason", lang),
        })

    profiles = []
    def chf(n):
        return "{:,}".format(n).replace(",", "'")

    for prof in PROFILES:
        row = {
            "label": t.get(prof["key"], prof["key"]),
            "base": prof["base"],
            "base_fmt": chf(prof["base"]),
            "amounts": [],
        }
        for g in RATE_GROUPS:
            amount = round(prof["base"] * g["rate"] / 100)
            row["amounts"].append({"rate": g["rate"], "amount": amount, "amount_fmt": chf(amount)})
        profiles.append(row)

    return {
        "t": t,
        "n_confirmed": n_confirmed,
        "n_single": n_single,
        "n_disc": n_disc,
        "n_excl": n_excl,
        "total_decisions": total_decisions,
        "confirmed": confirmed,
        "single_source": single,
        "discretionary": disc,
        "excluded": excl,
        "rate_groups": RATE_GROUPS,
        "profiles": profiles,
        "chart_max": 30,
    }
