#!/usr/bin/env python3
"""
Compositeur de texte de presentation par avocat/etude, dans les 4 langues.
Approche structurelle (pas d'appel a un modele par fiche) : on assemble des
phrases factuelles a partir des donnees reelles (nom, etude, ville, canton,
domaines de compétence si connus). Les formulations sont construites pour
eviter les problemes d'accord de genre (verbes invariants, tournures
neutres) plutot que de deviner le genre a partir du prenom.
"""


def smart_truncate(text, limit=158):
    """Coupe `text` a `limit` caracteres sans jamais couper un mot en deux.
    Sans quoi une meta description generee a partir d'un texte plus long
    finit sur un mot tronque (ex. "...seront pu" au lieu de "...seront
    publiees") -- visible tel quel dans le snippet Google. Ajoute une
    ellipse uniquement quand une troncature a reellement eu lieu."""
    if text is None or len(text) <= limit:
        return text
    cut = text[:limit]
    last_space = cut.rfind(" ")
    if last_space > 0:
        cut = cut[:last_space]
    return cut.rstrip(" ,;:.-") + "…"


def lawyer_presentation(lang, nom, canton_name, etude=None, ville=None, domaines=None, fonction=None,
                         langues=None, seniority_year=None):
    """langues et seniority_year sont deux signaux reels supplementaires (deja
    presents en base, jamais devines) utilises pour differencier les fiches qui
    n'ont pas de domaines de competence renseignes (majorite des fiches hors
    GE) -- sans quoi leur description ne varie que par le nom, ce qui nuit au
    CTR (Google reecrit/masque des snippets trop proches d'une fiche a l'autre)."""
    domaines = domaines or []
    langues = langues or []
    seniority_txt = seniority_text(lang, seniority_year) if seniority_year else ""
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
        elif langues:
            s += f" Langues parlées : {', '.join(langues)}."
        if seniority_txt:
            s += f" {seniority_txt}."
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
        elif langues:
            s += f" Gesprochene Sprachen: {', '.join(langues)}."
        if seniority_txt:
            s += f" {seniority_txt}."
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
        elif langues:
            s += f" Lingue parlate: {', '.join(langues)}."
        if seniority_txt:
            s += f" {seniority_txt}."
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
    elif langues:
        s += f" Languages spoken: {', '.join(langues)}."
    if seniority_txt:
        s += f" {seniority_txt}."
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
                f"{domaine_name.lower()} parmi leurs domaines de compétence, avec étude, ville et "
                f"coordonnées de contact pour chaque fiche.")
    if lang == "de":
        return (f"Liste der im Register des Kantons {canton_name} eingetragenen Anwältinnen und "
                f"Anwälte mit dem angegebenen Fachgebiet {domaine_name}, jeweils mit Kanzlei, Ort "
                f"und Kontaktangaben.")
    if lang == "it":
        return (f"Elenco degli avvocati iscritti al registro del Cantone {canton_name} che indicano "
                f"{domaine_name.lower()} tra i propri ambiti di competenza, con studio, città e "
                f"contatti per ciascuna scheda.")
    return (f"List of lawyers registered in the canton of {canton_name} who list "
            f"{domaine_name.lower()} among their practice areas, each with firm, city and contact "
            f"details.")


def ville_cross_intro(lang, domaine_name, canton_name, ville_name):
    """Variante de cross_intro() pour les pages ville x domaine : {ville_name}
    est une commune, jamais un canton -- contrairement a cross_intro(), qui
    suppose que son 3e argument est le nom du canton lui-meme. Reutiliser
    cross_intro() ici en lui passant la ville produirait "canton de {ville}",
    ce qui est factuellement faux (ex. Carouge, Petit-Lancy ne sont pas des
    cantons mais des communes genevoises)."""
    if lang == "fr":
        return (f"Liste des avocats de {ville_name}, dans le canton de {canton_name}, ayant indiqué "
                f"{domaine_name.lower()} parmi leurs domaines de compétence, avec étude et "
                f"coordonnées de contact pour chaque fiche.")
    if lang == "de":
        return (f"Liste der Anwältinnen und Anwälte in {ville_name} (Kanton {canton_name}) mit dem "
                f"angegebenen Fachgebiet {domaine_name}, jeweils mit Kanzlei und Kontaktangaben.")
    if lang == "it":
        return (f"Elenco degli avvocati di {ville_name}, nel Cantone {canton_name}, che indicano "
                f"{domaine_name.lower()} tra i propri ambiti di competenza, con studio e contatti "
                f"per ciascuna scheda.")
    return (f"List of lawyers in {ville_name}, canton of {canton_name}, who list "
            f"{domaine_name.lower()} among their practice areas, each with firm and contact "
            f"details.")


def cross_fallback_text(lang, domaine_name, canton_name):
    if lang == "fr":
        return (f"Aucun avocat de {canton_name} n'a encore de spécialité renseignée pour "
                f"{domaine_name.lower()} dans nos données. Voici l'ensemble des avocats inscrits au "
                f"registre du canton. Contactez-les directement pour vérifier leur domaine de "
                f"compétence.")
    if lang == "de":
        return (f"Für {domaine_name} liegen im Kanton {canton_name} noch keine erfassten "
                f"Fachgebietsangaben vor. Hier finden Sie das vollständige kantonale Register. Bitte "
                f"fragen Sie direkt nach dem Fachgebiet.")
    if lang == "it":
        return (f"Per {domaine_name.lower()} non risultano ancora ambiti di competenza registrati nel "
                f"Cantone {canton_name}. Ecco l'elenco completo del registro cantonale. Vi invitiamo a "
                f"verificare direttamente l'ambito di competenza.")
    return (f"No lawyer in {canton_name} yet has a recorded specialty for {domaine_name.lower()} in our "
            f"data. Here is the full cantonal register. Please confirm their practice area directly.")


def cross_h1(lang, domaine_name, canton_name):
    if lang == "fr":
        return f"{domaine_name} à {canton_name} : trouver un avocat"
    if lang == "de":
        return f"{domaine_name} in {canton_name}: Anwalt finden"
    if lang == "it":
        return f"{domaine_name} a {canton_name}: trova un avvocato"
    return f"{domaine_name} in {canton_name}: find a lawyer"


def langue_cross_intro(lang, langue_name, canton_name):
    """Intro des pages canton x langue parlee. Construction verbale
    deliberee ("parlant X"/"sprechen X"/"parla X"/"speak X") plutot qu'un
    simple adjectif : "avocat allemand" ou "German lawyer" se lit comme une
    nationalite en francais/anglais, pas comme une langue parlee -- source
    d'ambiguite que la formulation verbale evite dans les 4 langues."""
    if lang == "fr":
        return (f"Liste des avocats inscrits au registre du canton de {canton_name} parlant "
                f"{langue_name.lower()}, avec étude, ville et coordonnées de contact pour chaque fiche.")
    if lang == "de":
        return (f"Liste der im Register des Kantons {canton_name} eingetragenen Anwältinnen und "
                f"Anwälte, die {langue_name.lower()} sprechen, jeweils mit Kanzlei, Ort und Kontaktangaben.")
    if lang == "it":
        return (f"Elenco degli avvocati iscritti al registro del Cantone {canton_name} che parlano "
                f"{langue_name.lower()}, con studio, città e contatti per ciascuna scheda.")
    return (f"List of lawyers registered in the canton of {canton_name} who speak "
            f"{langue_name.lower()}, each with firm, city and contact details.")


def langue_ville_cross_intro(lang, langue_name, canton_name, ville_name):
    """Variante de langue_cross_intro() pour les pages ville x langue --
    meme raison que ville_cross_intro() : {ville_name} est une commune,
    jamais un canton."""
    if lang == "fr":
        return (f"Liste des avocats de {ville_name}, dans le canton de {canton_name}, parlant "
                f"{langue_name.lower()}, avec étude et coordonnées de contact pour chaque fiche.")
    if lang == "de":
        return (f"Liste der Anwältinnen und Anwälte in {ville_name} (Kanton {canton_name}), die "
                f"{langue_name.lower()} sprechen, jeweils mit Kanzlei und Kontaktangaben.")
    if lang == "it":
        return (f"Elenco degli avvocati di {ville_name}, nel Cantone {canton_name}, che parlano "
                f"{langue_name.lower()}, con studio e contatti per ciascuna scheda.")
    return (f"List of lawyers in {ville_name}, canton of {canton_name}, who speak "
            f"{langue_name.lower()}, each with firm and contact details.")


def langue_cross_h1(lang, langue_name, place_name):
    """H1/titre des pages langue (canton ou ville). Meme precaution que
    langue_cross_intro() sur l'ambiguite adjectif=nationalite : "-speaking"
    en anglais, "parlant" en francais/italien, "sprechend" en allemand
    (l'allemand n'a pas cette ambiguite mais garde une formulation
    coherente avec le reste du site, cf. "Anwältinnen und Anwälte")."""
    if lang == "fr":
        return f"Avocat parlant {langue_name.lower()} à {place_name}"
    if lang == "de":
        return f"{langue_name} sprechende Anwältinnen und Anwälte in {place_name}"
    if lang == "it":
        return f"Avvocato che parla {langue_name.lower()} a {place_name}"
    return f"{langue_name}-speaking lawyer in {place_name}"


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


_LANG_CODE_MAP = {"français": "fr", "allemand": "de", "italien": "it", "anglais": "en",
                   "espagnol": "es", "portugais": "pt", "arabe": "ar", "russe": "ru",
                   "romanche": "rm"}
_LANG_DISPLAY_NAMES = {
    "fr": {"fr": "Français", "de": "Allemand", "it": "Italien", "en": "Anglais",
           "es": "Espagnol", "pt": "Portugais", "ar": "Arabe", "ru": "Russe", "rm": "Romanche"},
    "de": {"fr": "Französisch", "de": "Deutsch", "it": "Italienisch", "en": "Englisch",
           "es": "Spanisch", "pt": "Portugiesisch", "ar": "Arabisch", "ru": "Russisch", "rm": "Rätoromanisch"},
    "it": {"fr": "Francese", "de": "Tedesco", "it": "Italiano", "en": "Inglese",
           "es": "Spagnolo", "pt": "Portoghese", "ar": "Arabo", "ru": "Russo", "rm": "Romancio"},
    "en": {"fr": "French", "de": "German", "it": "Italian", "en": "English",
           "es": "Spanish", "pt": "Portuguese", "ar": "Arabic", "ru": "Russian", "rm": "Romansh"},
}


def translate_langues(langues, lang):
    """Traduit une liste de noms de langues (mots bruts saisis en francais dans
    les registres source) vers la langue de la page affichee. Un mot non
    reconnu est conserve tel quel plutot que suppose ou supprime -- on ne
    fabrique jamais une traduction, on la trouve ou on garde l'original."""
    names = _LANG_DISPLAY_NAMES.get(lang, {})
    out = []
    for l in langues:
        code = _LANG_CODE_MAP.get(l.strip().lower())
        out.append(names.get(code, l) if code else l)
    return out


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


def lawyer_faq(lang, nom, canton_name, ville=None, domaines=None, langues=None,
                seniority_text=None, telephone=None, email=None, etude=None,
                review_avg=None, review_count=None):
    """FAQ personnalisee par fiche avocat individuelle, meme principe que
    ville_faq() dans build.py : uniquement des faits deja reels en base
    (registre cantonal officiel, enrichissement web deja verifie
    manuellement, avis approuves) -- jamais invente ni complete par defaut.
    Chaque question n'apparait que si la donnee correspondante existe
    reellement pour CETTE fiche : deux fiches peuvent donc avoir un nombre
    different de questions. Sert a la fois de contenu unique par fiche
    (au-dela de la courte presentation) et de schema.org FAQPage, pense pour
    etre facilement extrait/cite par les moteurs de recherche generatifs
    (AI Overviews, ChatGPT, Perplexity...) -- demande de Gregoire Giuliano
    du 2026-08-23."""
    domaines = domaines or []
    langues = langues or []
    items = []
    if lang == "fr":
        items.append({
            "q": f"{nom} est-il/elle un avocat vérifié ?",
            "a": f"Oui. {nom} est inscrit·e au registre officiel des avocats du canton de {canton_name}, seule source utilisée pour construire cette fiche.",
        })
        if domaines:
            items.append({
                "q": f"Quels domaines de compétence pratique {nom} ?",
                "a": f"Domaines de compétence indiqués pour {nom} : {', '.join(domaines)}.",
            })
        if langues:
            items.append({
                "q": f"Quelles langues parle {nom} ?",
                "a": f"{nom} parle : {', '.join(langues)}.",
            })
        if seniority_text:
            items.append({
                "q": f"Depuis quand {nom} est-il/elle inscrit·e au barreau ?",
                "a": f"{seniority_text}, selon le registre officiel du canton de {canton_name}.",
            })
        if telephone or email:
            bits = []
            if telephone:
                bits.append(f"par téléphone au {telephone}")
            if email:
                bits.append(f"par email à {email}")
            a = f"Vous pouvez contacter {nom} " + " ou ".join(bits) + "."
            if etude:
                a += f" {nom} exerce au sein de l'étude {etude}."
            items.append({"q": f"Comment contacter {nom} ?", "a": a})
        if review_count:
            items.append({
                "q": f"Que disent les avis publiés sur {nom} ?",
                "a": f"{nom} a reçu une note moyenne de {review_avg}/5 sur la base de {review_count} avis publiés sur Legatis.",
            })
        return items
    if lang == "de":
        items.append({
            "q": f"Ist {nom} eine geprüfte Anwältin bzw. ein geprüfter Anwalt?",
            "a": f"Ja. {nom} ist im offiziellen Anwaltsregister des Kantons {canton_name} eingetragen, der einzigen für diesen Eintrag verwendeten Quelle.",
        })
        if domaines:
            items.append({
                "q": f"In welchen Fachgebieten ist {nom} tätig?",
                "a": f"Für {nom} angegebene Fachgebiete: {', '.join(domaines)}.",
            })
        if langues:
            items.append({
                "q": f"Welche Sprachen spricht {nom}?",
                "a": f"{nom} spricht: {', '.join(langues)}.",
            })
        if seniority_text:
            items.append({
                "q": f"Seit wann ist {nom} im Anwaltsregister eingetragen?",
                "a": f"{seniority_text}, gemäss dem offiziellen Register des Kantons {canton_name}.",
            })
        if telephone or email:
            bits = []
            if telephone:
                bits.append(f"telefonisch unter {telephone}")
            if email:
                bits.append(f"per E-Mail an {email}")
            a = f"Sie können {nom} " + " oder ".join(bits) + " kontaktieren."
            if etude:
                a += f" {nom} ist bei {etude} tätig."
            items.append({"q": f"Wie kann man {nom} kontaktieren?", "a": a})
        if review_count:
            items.append({
                "q": f"Was sagen die Bewertungen zu {nom}?",
                "a": f"{nom} erhielt eine durchschnittliche Bewertung von {review_avg}/5, basierend auf {review_count} auf Legatis veröffentlichten Bewertungen.",
            })
        return items
    if lang == "it":
        items.append({
            "q": f"{nom} è un avvocato verificato?",
            "a": f"Sì. {nom} è iscritto/a all'albo ufficiale degli avvocati del Cantone {canton_name}, unica fonte utilizzata per costruire questa scheda.",
        })
        if domaines:
            items.append({
                "q": f"In quali ambiti di competenza esercita {nom} ?",
                "a": f"Ambiti di competenza indicati per {nom}: {', '.join(domaines)}.",
            })
        if langues:
            items.append({
                "q": f"Quali lingue parla {nom} ?",
                "a": f"{nom} parla: {', '.join(langues)}.",
            })
        if seniority_text:
            items.append({
                "q": f"Da quando {nom} è iscritto/a all'albo?",
                "a": f"{seniority_text}, secondo il registro ufficiale del Cantone {canton_name}.",
            })
        if telephone or email:
            bits = []
            if telephone:
                bits.append(f"telefonicamente al {telephone}")
            if email:
                bits.append(f"via email a {email}")
            a = f"Potete contattare {nom} " + " oppure ".join(bits) + "."
            if etude:
                a += f" {nom} esercita presso lo studio {etude}."
            items.append({"q": f"Come contattare {nom} ?", "a": a})
        if review_count:
            items.append({
                "q": f"Cosa dicono le recensioni su {nom} ?",
                "a": f"{nom} ha ricevuto una valutazione media di {review_avg}/5 sulla base di {review_count} recensioni pubblicate su Legatis.",
            })
        return items
    # en
    items.append({
        "q": f"Is {nom} a verified lawyer?",
        "a": f"Yes. {nom} is registered with the official register of lawyers of the canton of {canton_name}, the only source used to build this listing.",
    })
    if domaines:
        items.append({
            "q": f"What practice areas does {nom} cover?",
            "a": f"Listed practice areas for {nom}: {', '.join(domaines)}.",
        })
    if langues:
        items.append({
            "q": f"What languages does {nom} speak?",
            "a": f"{nom} speaks: {', '.join(langues)}.",
        })
    if seniority_text:
        items.append({
            "q": f"Since when has {nom} been registered with the bar?",
            "a": f"{seniority_text}, according to the official register of the canton of {canton_name}.",
        })
    if telephone or email:
        bits = []
        if telephone:
            bits.append(f"by phone at {telephone}")
        if email:
            bits.append(f"by email at {email}")
        a = f"You can contact {nom} " + " or ".join(bits) + "."
        if etude:
            a += f" {nom} practises at {etude}."
        items.append({"q": f"How to contact {nom}?", "a": a})
    if review_count:
        items.append({
            "q": f"What do reviews say about {nom}?",
            "a": f"{nom} received an average rating of {review_avg}/5 based on {review_count} reviews published on Legatis.",
        })
    return items


def firm_faq(lang, nom_etude, canton_name, ville=None, n_membres=0, founding_year=None,
             domaines=None, langues=None, telephone=None):
    """Meme principe que lawyer_faq() ci-dessus, pour les fiches etude/cabinet."""
    domaines = domaines or []
    langues = langues or []
    items = []
    if lang == "fr":
        items.append({
            "q": f"{nom_etude} est-elle une étude vérifiée ?",
            "a": f"Oui. {nom_etude} est enregistrée dans le registre officiel des avocats du canton de {canton_name}, seule source utilisée pour construire cette fiche.",
        })
        if n_membres:
            items.append({
                "q": f"Combien d'avocats travaillent chez {nom_etude} ?",
                "a": f"{n_membres} avocat(e)s de {nom_etude} figurent au registre Legatis.",
            })
        if founding_year:
            import datetime
            n = datetime.date.today().year - founding_year
            items.append({
                "q": f"Depuis quand {nom_etude} existe-t-elle ?",
                "a": f"{nom_etude} a été fondée en {founding_year}" + (f", soit {n} ans d'existence." if n > 0 else "."),
            })
        if domaines:
            items.append({
                "q": f"Quels domaines de compétence couvre {nom_etude} ?",
                "a": f"Domaines de compétence indiqués par les membres de {nom_etude} : {', '.join(domaines)}.",
            })
        if langues:
            items.append({
                "q": f"Quelles langues sont parlées chez {nom_etude} ?",
                "a": f"Langues parlées par les membres de {nom_etude} : {', '.join(langues)}.",
            })
        if telephone:
            items.append({
                "q": f"Comment contacter {nom_etude} ?",
                "a": f"Vous pouvez contacter {nom_etude} par téléphone au {telephone}.",
            })
        return items
    if lang == "de":
        items.append({
            "q": f"Ist {nom_etude} eine geprüfte Kanzlei?",
            "a": f"Ja. {nom_etude} ist im offiziellen Anwaltsregister des Kantons {canton_name} eingetragen, der einzigen für diesen Eintrag verwendeten Quelle.",
        })
        if n_membres:
            items.append({
                "q": f"Wie viele Anwältinnen und Anwälte arbeiten bei {nom_etude}?",
                "a": f"{n_membres} Anwältinnen und Anwälte von {nom_etude} sind im Legatis-Register erfasst.",
            })
        if founding_year:
            import datetime
            n = datetime.date.today().year - founding_year
            items.append({
                "q": f"Seit wann besteht {nom_etude}?",
                "a": f"{nom_etude} wurde {founding_year} gegründet" + (f", also seit {n} Jahren." if n > 0 else "."),
            })
        if domaines:
            items.append({
                "q": f"Welche Fachgebiete deckt {nom_etude} ab?",
                "a": f"Von den Mitgliedern von {nom_etude} angegebene Fachgebiete: {', '.join(domaines)}.",
            })
        if langues:
            items.append({
                "q": f"Welche Sprachen werden bei {nom_etude} gesprochen?",
                "a": f"Von den Mitgliedern von {nom_etude} gesprochene Sprachen: {', '.join(langues)}.",
            })
        if telephone:
            items.append({
                "q": f"Wie kann man {nom_etude} kontaktieren?",
                "a": f"Sie können {nom_etude} telefonisch unter {telephone} kontaktieren.",
            })
        return items
    if lang == "it":
        items.append({
            "q": f"{nom_etude} è uno studio verificato?",
            "a": f"Sì. {nom_etude} è registrato nell'albo ufficiale degli avvocati del Cantone {canton_name}, unica fonte utilizzata per costruire questa scheda.",
        })
        if n_membres:
            items.append({
                "q": f"Quanti avvocati lavorano presso {nom_etude} ?",
                "a": f"{n_membres} avvocati di {nom_etude} figurano nel registro Legatis.",
            })
        if founding_year:
            import datetime
            n = datetime.date.today().year - founding_year
            items.append({
                "q": f"Da quando esiste {nom_etude} ?",
                "a": f"{nom_etude} è stato fondato nel {founding_year}" + (f", ovvero {n} anni di attività." if n > 0 else "."),
            })
        if domaines:
            items.append({
                "q": f"Quali ambiti di competenza copre {nom_etude} ?",
                "a": f"Ambiti di competenza indicati dai membri di {nom_etude}: {', '.join(domaines)}.",
            })
        if langues:
            items.append({
                "q": f"Quali lingue si parlano presso {nom_etude} ?",
                "a": f"Lingue parlate dai membri di {nom_etude}: {', '.join(langues)}.",
            })
        if telephone:
            items.append({
                "q": f"Come contattare {nom_etude} ?",
                "a": f"Potete contattare {nom_etude} telefonicamente al {telephone}.",
            })
        return items
    # en
    items.append({
        "q": f"Is {nom_etude} a verified firm?",
        "a": f"Yes. {nom_etude} is registered with the official register of lawyers of the canton of {canton_name}, the only source used to build this listing.",
    })
    if n_membres:
        items.append({
            "q": f"How many lawyers work at {nom_etude}?",
            "a": f"{n_membres} lawyers from {nom_etude} are listed on Legatis.",
        })
    if founding_year:
        import datetime
        n = datetime.date.today().year - founding_year
        items.append({
            "q": f"Since when has {nom_etude} existed?",
            "a": f"{nom_etude} was founded in {founding_year}" + (f", {n} years of activity." if n > 0 else "."),
        })
    if domaines:
        items.append({
            "q": f"What practice areas does {nom_etude} cover?",
            "a": f"Practice areas indicated by {nom_etude}'s members: {', '.join(domaines)}.",
        })
    if langues:
        items.append({
            "q": f"What languages are spoken at {nom_etude}?",
            "a": f"Languages spoken by {nom_etude}'s members: {', '.join(langues)}.",
        })
    if telephone:
        items.append({
            "q": f"How to contact {nom_etude}?",
            "a": f"You can contact {nom_etude} by phone at {telephone}.",
        })
    return items
