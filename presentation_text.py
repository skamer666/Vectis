#!/usr/bin/env python3
"""
Compositeur de texte de presentation par avocat/etude, dans les 4 langues.
Approche structurelle (pas d'appel a un modele par fiche) : on assemble des
phrases factuelles a partir des donnees reelles (nom, etude, ville, canton,
domaines de compétence si connus). Les formulations sont construites pour
eviter les problemes d'accord de genre (verbes invariants, tournures
neutres) plutot que de deviner le genre a partir du prenom.
"""


def lawyer_presentation(lang, nom, canton_name, etude=None, ville=None, domaines=None, fonction=None):
    domaines = domaines or []
    if lang == "fr":
        s = f"Me {nom} figure au registre des avocats du canton de {canton_name}"
        if etude:
            s += f", au sein de l'étude {etude}"
        if ville:
            s += f", à {ville}"
        s += "."
        if fonction:
            s += f" Statut au registre : {fonction}."
        if domaines:
            s += f" Domaines de compétence indiqués : {', '.join(domaines)}."
        return s
    if lang == "de":
        s = f"{nom} ist im Anwaltsregister des Kantons {canton_name} eingetragen"
        if etude:
            s += f", tätig bei {etude}"
        if ville:
            s += f", in {ville}"
        s += "."
        if domaines:
            s += f" Angegebene Fachgebiete: {', '.join(domaines)}."
        return s
    if lang == "it":
        s = f"{nom} figura nel registro degli avvocati del Cantone {canton_name}"
        if etude:
            s += f", presso lo studio {etude}"
        if ville:
            s += f", a {ville}"
        s += "."
        if domaines:
            s += f" Ambiti di competenza indicati: {', '.join(domaines)}."
        return s
    # en
    s = f"{nom} is listed in the register of lawyers of the canton of {canton_name}"
    if etude:
        s += f", practising at {etude}"
    if ville:
        s += f", in {ville}"
    s += "."
    if domaines:
        s += f" Listed practice areas: {', '.join(domaines)}."
    return s


def firm_presentation(lang, nom_etude, canton_name, ville=None, n_membres=0):
    if lang == "fr":
        s = f"{nom_etude} est une étude d'avocats enregistrée dans le canton de {canton_name}"
        if ville:
            s += f", à {ville}"
        s += "."
        if n_membres:
            s += f" {n_membres} avocat(e)s de l'étude figurent au registre Legatis."
        return s
    if lang == "de":
        s = f"{nom_etude} ist eine im Kanton {canton_name} registrierte Anwaltskanzlei"
        if ville:
            s += f", in {ville}"
        s += "."
        if n_membres:
            s += f" {n_membres} Anwältinnen und Anwälte der Kanzlei sind bei Legatis erfasst."
        return s
    if lang == "it":
        s = f"{nom_etude} è uno studio legale registrato nel Cantone {canton_name}"
        if ville:
            s += f", a {ville}"
        s += "."
        if n_membres:
            s += f" {n_membres} avvocati dello studio figurano nel registro Legatis."
        return s
    s = f"{nom_etude} is a law firm registered in the canton of {canton_name}"
    if ville:
        s += f", in {ville}"
    s += "."
    if n_membres:
        s += f" {n_membres} lawyers from this firm are listed on Legatis."
    return s


def canton_intro(lang, canton_name, n_avocats):
    if lang == "fr":
        return (f"Legatis recense {n_avocats} avocat(e)s inscrit(e)s au registre officiel du canton de "
                f"{canton_name}. Recherchez par domaine de droit ou parcourez le registre complet.")
    if lang == "de":
        return (f"Legatis verzeichnet {n_avocats} im offiziellen Register des Kantons {canton_name} "
                f"eingetragene Anwältinnen und Anwälte. Suchen Sie nach Rechtsgebiet oder durchsuchen "
                f"Sie das vollständige Register.")
    if lang == "it":
        return (f"Legatis censisce {n_avocats} avvocati iscritti al registro ufficiale del Cantone "
                f"{canton_name}. Cercate per ambito del diritto o consultate il registro completo.")
    return (f"Legatis lists {n_avocats} lawyers registered in the official register of the canton of "
            f"{canton_name}. Search by practice area or browse the full register.")


def domaine_intro(lang, domaine_name):
    if lang == "fr":
        return (f"Trouvez un avocat spécialisé en {domaine_name.lower()} dans chaque canton de Suisse. "
                f"Legatis recense les avocats inscrits aux registres cantonaux officiels.")
    if lang == "de":
        return (f"Finden Sie eine Anwältin oder einen Anwalt im Bereich {domaine_name} in jedem "
                f"Schweizer Kanton. Legatis verzeichnet die in den offiziellen kantonalen Registern "
                f"eingetragenen Anwältinnen und Anwälte.")
    if lang == "it":
        return (f"Trova un avvocato specializzato in {domaine_name.lower()} in ogni cantone svizzero. "
                f"Legatis censisce gli avvocati iscritti ai registri cantonali ufficiali.")
    return (f"Find a lawyer specialising in {domaine_name.lower()} in every Swiss canton. Legatis lists "
            f"lawyers registered in the official cantonal registers.")


def cross_intro(lang, domaine_name, canton_name):
    if lang == "fr":
        return (f"Liste des avocats inscrits au registre du canton de {canton_name} ayant indiqué "
                f"{domaine_name.lower()} parmi leurs domaines de compétence.")
    if lang == "de":
        return (f"Liste der im Register des Kantons {canton_name} eingetragenen Anwältinnen und "
                f"Anwälte mit dem angegebenen Fachgebiet {domaine_name}.")
    if lang == "it":
        return (f"Elenco degli avvocati iscritti al registro del Cantone {canton_name} che indicano "
                f"{domaine_name.lower()} tra i propri ambiti di competenza.")
    return (f"List of lawyers registered in the canton of {canton_name} who list "
            f"{domaine_name.lower()} among their practice areas.")


def cross_fallback_text(lang, domaine_name, canton_name):
    if lang == "fr":
        return (f"Aucun avocat de {canton_name} n'a encore de spécialité renseignée pour "
                f"{domaine_name.lower()} dans nos données. Voici l'ensemble des avocats inscrits au "
                f"registre du canton — contactez-les directement pour vérifier leur domaine de "
                f"compétence.")
    if lang == "de":
        return (f"Für {domaine_name} liegen im Kanton {canton_name} noch keine erfassten "
                f"Fachgebietsangaben vor. Hier finden Sie das vollständige kantonale Register — bitte "
                f"fragen Sie direkt nach dem Fachgebiet.")
    if lang == "it":
        return (f"Per {domaine_name.lower()} non risultano ancora ambiti di competenza registrati nel "
                f"Cantone {canton_name}. Ecco l'elenco completo del registro cantonale — vi invitiamo a "
                f"verificare direttamente l'ambito di competenza.")
    return (f"No lawyer in {canton_name} yet has a recorded specialty for {domaine_name.lower()} in our "
            f"data. Here is the full cantonal register — please confirm their practice area directly.")


def cross_h1(lang, domaine_name, canton_name):
    if lang == "fr":
        return f"{domaine_name} à {canton_name} — trouver un avocat"
    if lang == "de":
        return f"{domaine_name} in {canton_name} — Anwalt finden"
    if lang == "it":
        return f"{domaine_name} a {canton_name} — trova un avvocato"
    return f"{domaine_name} in {canton_name} — find a lawyer"


def seniority_text(lang, year):
    """Texte d'anciennete au barreau, calcule depuis une annee d'admission reelle
    (jamais devine). Retourne une chaine vide si l'annee est absente ou invalide."""
    if not year:
        return ""
    try:
        y = int(str(year).strip()[:4])
    except (TypeError, ValueError):
        return ""
    if y < 1900 or y > 2026:
        return ""
    import datetime
    n = datetime.date.today().year - y
    if lang == "fr":
        return f"Inscrit\u00b7e au barreau depuis {y}" + (f" ({n} ans)" if n > 0 else "")
    if lang == "de":
        return f"Im Anwaltsregister eingetragen seit {y}" + (f" ({n} Jahre)" if n > 0 else "")
    if lang == "it":
        return f"Iscritto/a all'albo dal {y}" + (f" ({n} anni)" if n > 0 else "")
    return f"Registered with the bar since {y}" + (f" ({n} years)" if n > 0 else "")


def firm_insight(lang, langues, domaines, oldest_year, founding_year=None, team_size_n=None):
    """Agrege des faits reels sur l'equipe d'une etude (langues et domaines
    couverts par ses membres, anciennete du membre le plus ancien ou date de
    fondation reelle si connue via le site du cabinet, taille annoncee),
    calcules depuis les donnees deja en base -- jamais devine ni complete par
    defaut. founding_year (source : site officiel du cabinet) est toujours
    prefere a oldest_year (proxy : membre le plus ancien du registre) quand
    disponible, car plus precis et plus honnete."""
    parts = []
    oldest_txt = None
    if founding_year:
        import datetime
        n = datetime.date.today().year - founding_year
        if lang == "fr":
            oldest_txt = f"Étude fondée en {founding_year}" + (f" ({n} ans d'existence)." if n > 0 else ".")
        elif lang == "de":
            oldest_txt = f"Kanzlei gegründet {founding_year}" + (f" ({n} Jahre Bestehen)." if n > 0 else ".")
        elif lang == "it":
            oldest_txt = f"Studio fondato nel {founding_year}" + (f" ({n} anni di attività)." if n > 0 else ".")
        else:
            oldest_txt = f"Firm founded in {founding_year}" + (f" ({n} years of activity)." if n > 0 else ".")
    elif oldest_year:
        import datetime
        n = datetime.date.today().year - oldest_year
        if lang == "fr":
            oldest_txt = (f"Le membre le plus ancien de l'étude est inscrit au barreau depuis "
                          f"{oldest_year}" + (f" ({n} ans)." if n > 0 else "."))
        elif lang == "de":
            oldest_txt = (f"Das dienstälteste Mitglied der Kanzlei ist seit {oldest_year} im "
                          f"Anwaltsregister eingetragen" + (f" ({n} Jahre)." if n > 0 else "."))
        elif lang == "it":
            oldest_txt = (f"Il membro più anziano dello studio è iscritto all'albo dal "
                          f"{oldest_year}" + (f" ({n} anni)." if n > 0 else "."))
        else:
            oldest_txt = (f"The most senior member of the firm has been registered with the bar "
                          f"since {oldest_year}" + (f" ({n} years)." if n > 0 else "."))
    if team_size_n:
        _unit = {"fr": "avocats et juristes", "de": "Anwältinnen, Anwälte und Juristen",
                 "it": "avvocati e giuristi", "en": "lawyers and jurists"}[lang]
        if lang == "fr":
            parts.append(f"L'étude indique elle-même compter environ {team_size_n} {_unit}.")
        elif lang == "de":
            parts.append(f"Die Kanzlei gibt selbst an, rund {team_size_n} {_unit} zu zählen.")
        elif lang == "it":
            parts.append(f"Lo studio dichiara di contare circa {team_size_n} {_unit}.")
        else:
            parts.append(f"The firm itself states it has around {team_size_n} {_unit}.")
    if lang == "fr":
        if langues:
            parts.append("Langues parlées par l'équipe : " + ", ".join(langues) + ".")
        if domaines:
            parts.append("Domaines de compétence indiqués par l'équipe : " + ", ".join(domaines) + ".")
    elif lang == "de":
        if langues:
            parts.append("Vom Team gesprochene Sprachen: " + ", ".join(langues) + ".")
        if domaines:
            parts.append("Vom Team angegebene Fachgebiete: " + ", ".join(domaines) + ".")
    elif lang == "it":
        if langues:
            parts.append("Lingue parlate dal team: " + ", ".join(langues) + ".")
        if domaines:
            parts.append("Ambiti di competenza indicati dal team: " + ", ".join(domaines) + ".")
    else:
        if langues:
            parts.append("Languages spoken by the team: " + ", ".join(langues) + ".")
        if domaines:
            parts.append("Practice areas indicated by the team: " + ", ".join(domaines) + ".")
    if oldest_txt:
        parts.append(oldest_txt)
    return " ".join(parts)
