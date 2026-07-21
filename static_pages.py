#!/usr/bin/env python3
"""
Contenu des pages statiques (methodologie, a propos, contact, mentions
legales, confidentialite, correction), dans les 4 langues. Texte ecrit a la
main, honnete sur les limites actuelles des donnees plutot que de les
habiller.
"""

import datetime

COVERED_CANTONS_FR = [
    "Genève", "Vaud", "Fribourg", "Neuchâtel", "Jura", "Zurich", "Bâle-Ville",
    "Argovie", "Grisons", "Lucerne", "Saint-Gall", "Soleure", "Schwytz",
    "Thurgovie", "Zoug", "Glaris", "Appenzell Rhodes-Interieures", "Obwald",
    "Nidwald", "Uri",
]
BLOCKED_CANTONS_FR = ["Berne", "Bâle-Campagne", "Schaffhouse", "Tessin", "Valais", "Appenzell Rhodes-Exterieures"]

TODAY = datetime.date.today().strftime("%d.%m.%Y")


def _p(*paragraphs):
    return list(paragraphs)


def get_page(page_id, lang):
    return _PAGES[page_id][lang]


_PAGES = {
    "methodologie": {
        "fr": {
            "title": "Méthodologie et sources",
            "sections": [
                {"heading": "D'où viennent les données", "paragraphs": _p(
                    "Legatis compile les registres officiels tenus par les ordres et autorités judiciaires "
                    f"cantonales, pour les {len(COVERED_CANTONS_FR)} cantons suisses actuellement couverts. "
                    "Les données sont extraites puis nettoyées de façon automatisée (déduplication, "
                    "normalisation des adresses, exclusion des entrées de test ou corrompues) : nous ne "
                    "devinons et n'inventons aucune information absente de la source d'origine.",
                )},
                {"heading": "Cantons couverts", "paragraphs": _p(
                    "20 cantons sont actuellement couverts : " + ", ".join(COVERED_CANTONS_FR) + ".",
                    "6 cantons ne sont pas encore couverts, faute d'accès à un registre public exploitable "
                    "à ce jour : " + ", ".join(BLOCKED_CANTONS_FR) + ". Ils seront ajoutés dès qu'un accès "
                    "légitime aux données sera possible.",
                )},
                {"heading": "Fraîcheur des données", "paragraphs": _p(
                    f"Cette version du registre a été générée le {TODAY}. La fréquence de resynchronisation "
                    "avec les registres officiels n'est pas encore fixée à intervalle régulier ; nous "
                    "l'indiquerons ici dès qu'elle le sera.",
                )},
                {"heading": "Limites connues", "paragraphs": _p(
                    "Les domaines de compétence ne sont renseignés que pour une partie des avocats "
                    "genevois, et pas encore pour les 19 autres cantons couverts : ces informations ne "
                    "figurent simplement pas dans les registres sources tels quels. Nous travaillons à "
                    "compléter cette donnée à partir de sources publiques supplémentaires plutôt que de "
                    "l'estimer.",
                    "Le statut « indépendant » d'un avocat reflète l'absence d'étude renseignée dans le "
                    "registre source, pas une vérification indépendante de son statut professionnel réel.",
                )},
                {"heading": "Une erreur sur une fiche ?", "paragraphs": _p(
                    "Chaque fiche peut contenir une inexactitude reprise du registre source, ou une "
                    "information devenue obsolète. Signalez-la depuis la page de correction.",
                )},
            ],
        },
        "de": {
            "title": "Methodik und Quellen",
            "sections": [
                {"heading": "Herkunft der Daten", "paragraphs": _p(
                    "Legatis stützt sich auf die offiziellen Register der kantonalen Anwaltskammern und "
                    f"Justizbehörden, für die derzeit {len(COVERED_CANTONS_FR)} erfassten Kantone. Die Daten "
                    "werden automatisiert bereinigt (Dublettenentfernung, Adressnormalisierung, Ausschluss "
                    "von Test- oder fehlerhaften Einträgen) — es werden keine Angaben erfunden oder "
                    "geschätzt, die nicht in der Quelle vorhanden sind.",
                )},
                {"heading": "Erfasste Kantone", "paragraphs": _p(
                    "20 Kantone sind derzeit erfasst: " + ", ".join(COVERED_CANTONS_FR) + ".",
                    "6 Kantone sind mangels zugänglichem öffentlichem Register noch nicht erfasst: "
                    + ", ".join(BLOCKED_CANTONS_FR) + ". Sie werden ergänzt, sobald ein legitimer "
                    "Datenzugang möglich ist.",
                )},
                {"heading": "Aktualität der Daten", "paragraphs": _p(
                    f"Diese Version des Registers wurde am {TODAY} erstellt. Ein fester Rhythmus für die "
                    "Neusynchronisation mit den offiziellen Registern ist noch nicht festgelegt.",
                )},
                {"heading": "Bekannte Einschränkungen", "paragraphs": _p(
                    "Fachgebiete sind nur für einen Teil der Genfer Anwältinnen und Anwälte erfasst, für "
                    "die übrigen 19 Kantone noch gar nicht — diese Angabe fehlt schlicht in den "
                    "Ursprungsregistern. Wir arbeiten daran, sie aus zusätzlichen öffentlichen Quellen zu "
                    "ergänzen, statt sie zu schätzen.",
                )},
                {"heading": "Fehler auf einer Seite?", "paragraphs": _p(
                    "Jede Seite kann eine aus der Quelle übernommene Ungenauigkeit oder veraltete Angabe "
                    "enthalten. Melden Sie diese über die Korrekturseite.",
                )},
            ],
        },
        "it": {
            "title": "Metodologia e fonti",
            "sections": [
                {"heading": "Origine dei dati", "paragraphs": _p(
                    "Legatis raccoglie i registri ufficiali tenuti dagli ordini degli avvocati e dalle "
                    f"autorità giudiziarie cantonali, per i {len(COVERED_CANTONS_FR)} cantoni svizzeri "
                    "attualmente coperti. I dati vengono ripuliti in modo automatizzato (deduplicazione, "
                    "normalizzazione degli indirizzi, esclusione di voci di test o corrotte): non "
                    "inventiamo né stimiamo alcuna informazione assente dalla fonte originale.",
                )},
                {"heading": "Cantoni coperti", "paragraphs": _p(
                    "20 cantoni sono attualmente coperti: " + ", ".join(COVERED_CANTONS_FR) + ".",
                    "6 cantoni non sono ancora coperti, per mancanza di un registro pubblico consultabile: "
                    + ", ".join(BLOCKED_CANTONS_FR) + ". Verranno aggiunti non appena sarà possibile un "
                    "accesso legittimo ai dati.",
                )},
                {"heading": "Aggiornamento dei dati", "paragraphs": _p(
                    f"Questa versione del registro è stata generata il {TODAY}. La frequenza di "
                    "risincronizzazione con i registri ufficiali non è ancora fissata a intervalli regolari.",
                )},
                {"heading": "Limiti noti", "paragraphs": _p(
                    "Gli ambiti di competenza sono indicati solo per una parte degli avvocati ginevrini, e "
                    "non ancora per gli altri 19 cantoni coperti: questa informazione è semplicemente "
                    "assente nei registri di origine. Stiamo lavorando per completarla da fonti pubbliche "
                    "aggiuntive, senza stimarla.",
                )},
                {"heading": "Un errore su una scheda?", "paragraphs": _p(
                    "Ogni scheda può contenere un'imprecisione ripresa dal registro di origine, o "
                    "un'informazione ormai obsoleta. Segnalatela dalla pagina delle correzioni.",
                )},
            ],
        },
        "en": {
            "title": "Methodology and sources",
            "sections": [
                {"heading": "Where the data comes from", "paragraphs": _p(
                    "Legatis compiles the official registers maintained by cantonal bar associations and "
                    f"judicial authorities, for the {len(COVERED_CANTONS_FR)} Swiss cantons currently "
                    "covered. Data is extracted and cleaned in an automated way (deduplication, address "
                    "normalisation, exclusion of test or corrupted entries): we do not guess or invent any "
                    "information absent from the original source.",
                )},
                {"heading": "Cantons covered", "paragraphs": _p(
                    "20 cantons are currently covered: " + ", ".join(COVERED_CANTONS_FR) + ".",
                    "6 cantons are not yet covered, for lack of an accessible public register: "
                    + ", ".join(BLOCKED_CANTONS_FR) + ". They will be added as soon as legitimate access "
                    "to the data becomes possible.",
                )},
                {"heading": "Data freshness", "paragraphs": _p(
                    f"This version of the register was generated on {TODAY}. A fixed resynchronisation "
                    "schedule with the official registers has not yet been set.",
                )},
                {"heading": "Known limitations", "paragraphs": _p(
                    "Practice areas are only recorded for a portion of Geneva lawyers, and not yet for the "
                    "other 19 covered cantons — this information is simply absent from the source registers "
                    "as they stand. We are working to complete it from additional public sources rather "
                    "than estimating it.",
                )},
                {"heading": "Found an error on a listing?", "paragraphs": _p(
                    "Any listing may contain an inaccuracy carried over from the source register, or "
                    "outdated information. Report it from the correction page.",
                )},
            ],
        },
    },
    "a-propos": {
        "fr": {"title": "À propos", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis est l'annuaire de référence des avocats en Suisse : un registre public et "
                "gratuit, construit à partir des registres officiels cantonaux, en français, allemand, "
                "italien et anglais.",
                "Pas de compte utilisateur, pas de classement payant, pas d'avis fabriqués. L'objectif est "
                "que n'importe qui puisse vérifier rapidement qu'un avocat est bien inscrit au barreau et "
                "retrouver ses coordonnées officielles — pas de générer des prospects payants pour les "
                "études.",
                "Le projet est encore jeune : certaines données restent incomplètes (voir la page "
                "méthodologie) et six cantons ne sont pas encore couverts. Il s'améliore progressivement.",
            )},
        ]},
        "de": {"title": "Über uns", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis ist das Referenzverzeichnis der Anwältinnen und Anwälte in der Schweiz: ein "
                "öffentliches, kostenloses Register auf Basis der offiziellen kantonalen Register, auf "
                "Französisch, Deutsch, Italienisch und Englisch.",
                "Kein Benutzerkonto, kein bezahltes Ranking, keine erfundenen Bewertungen. Ziel ist es, "
                "dass jede und jeder schnell prüfen kann, ob eine Anwältin oder ein Anwalt tatsächlich im "
                "Anwaltsregister eingetragen ist, und die offiziellen Kontaktdaten findet — nicht, "
                "kostenpflichtige Leads für Kanzleien zu generieren.",
                "Das Projekt ist noch jung: manche Daten sind noch unvollständig (siehe Methodik-Seite), "
                "und sechs Kantone sind noch nicht erfasst. Es wird laufend erweitert.",
            )},
        ]},
        "it": {"title": "Chi siamo", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis è l'elenco di riferimento degli avvocati in Svizzera: un registro pubblico e "
                "gratuito, costruito a partire dai registri ufficiali cantonali, in francese, tedesco, "
                "italiano e inglese.",
                "Nessun account utente, nessuna classifica a pagamento, nessuna recensione inventata. "
                "L'obiettivo è permettere a chiunque di verificare rapidamente che un avvocato sia "
                "effettivamente iscritto all'albo e di trovarne i contatti ufficiali — non generare "
                "contatti commerciali a pagamento per gli studi legali.",
                "Il progetto è ancora giovane: alcuni dati restano incompleti (vedi la pagina metodologia) "
                "e sei cantoni non sono ancora coperti. Viene migliorato progressivamente.",
            )},
        ]},
        "en": {"title": "About", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis is Switzerland's reference directory of lawyers: a free, public register built "
                "from official cantonal registers, in French, German, Italian and English.",
                "No user accounts, no paid ranking, no fabricated reviews. The goal is for anyone to "
                "quickly verify that a lawyer is genuinely registered with the bar and find their official "
                "contact details — not to generate paid leads for law firms.",
                "The project is still young: some data remains incomplete (see the methodology page) and "
                "six cantons are not yet covered. It is improved progressively.",
            )},
        ]},
    },
    "contact": {
        "fr": {"title": "Contact", "sections": [
            {"heading": None, "paragraphs": _p(
                "Pour toute question générale, demande de presse ou de partenariat : "
                "contact@legatis.ch.",
                "Pour signaler une erreur sur une fiche précise, utilisez plutôt la page « Signaler une "
                "correction », qui nous permet de traiter la demande plus rapidement.",
            )},
        ]},
        "de": {"title": "Kontakt", "sections": [
            {"heading": None, "paragraphs": _p(
                "Für allgemeine Fragen, Presseanfragen oder Partnerschaften: contact@legatis.ch.",
                "Um einen Fehler auf einer bestimmten Seite zu melden, nutzen Sie bitte die Seite "
                "\u201eFehler melden\u201c \u2014 so k\u00f6nnen wir die Anfrage schneller bearbeiten.",
            )},
        ]},
        "it": {"title": "Contatto", "sections": [
            {"heading": None, "paragraphs": _p(
                "Per qualsiasi domanda generale, richiesta stampa o di partnership: "
                "contact@legatis.ch.",
                "Per segnalare un errore su una scheda specifica, utilizzate invece la pagina "
                "«Segnala una correzione», che ci permette di gestire la richiesta più rapidamente.",
            )},
        ]},
        "en": {"title": "Contact", "sections": [
            {"heading": None, "paragraphs": _p(
                "For general questions, press or partnership enquiries: contact@legatis.ch.",
                "To report an error on a specific listing, please use the \"Report a correction\" page "
                "instead — it lets us handle the request faster.",
            )},
        ]},
    },
    "mentions-legales": {
        "fr": {"title": "Mentions légales", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis est actuellement en phase de pré-lancement. Les mentions légales complètes "
                "(raison sociale, adresse du siège, responsable de la publication) seront publiées ici "
                "avant la mise en production définitive sur legatis.ch.",
                "Les données publiées proviennent des registres officiels cantonaux des avocats (voir la "
                "page méthodologie) et sont republiées à titre d'information publique.",
            )},
        ]},
        "de": {"title": "Impressum", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis befindet sich derzeit in der Vorlaunch-Phase. Das vollständige Impressum "
                "(Firmenname, Sitz, presserechtlich Verantwortliche Person) wird hier vor dem endgültigen "
                "Launch unter legatis.ch veröffentlicht.",
                "Die veröffentlichten Daten stammen aus den offiziellen kantonalen Anwaltsregistern (siehe "
                "Methodik-Seite) und werden als öffentliche Information weiterveröffentlicht.",
            )},
        ]},
        "it": {"title": "Note legali", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis è attualmente in fase di pre-lancio. Le note legali complete (ragione sociale, "
                "sede legale, responsabile della pubblicazione) saranno pubblicate qui prima del lancio "
                "definitivo su legatis.ch.",
                "I dati pubblicati provengono dai registri ufficiali cantonali degli avvocati (vedi la "
                "pagina metodologia) e sono ripubblicati a titolo di informazione pubblica.",
            )},
        ]},
        "en": {"title": "Legal notice", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis is currently in a pre-launch phase. Full legal notice details (company name, "
                "registered address, publication manager) will be published here before the final launch "
                "on legatis.ch.",
                "The published data comes from official cantonal lawyer registers (see the methodology "
                "page) and is republished as public information.",
            )},
        ]},
    },
    "confidentialite": {
        "fr": {"title": "Confidentialité", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis ne demande la création d'aucun compte et ne collecte pas de données personnelles "
                "au-delà des informations techniques standard de navigation.",
                "Les données personnelles affichées sur les fiches (nom, étude, adresse professionnelle, "
                "téléphone, e-mail) proviennent des registres publics officiels des avocats et concernent "
                "l'exercice de leur profession, pas leur vie privée.",
                "Toute personne concernée peut demander une correction ou faire valoir ses droits via la "
                "page « Signaler une correction ».",
            )},
        ]},
        "de": {"title": "Datenschutz", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis verlangt keine Kontoerstellung und erhebt keine personenbezogenen Daten über die "
                "üblichen technischen Standard-Nutzungsdaten hinaus.",
                "Die auf den Profilen angezeigten personenbezogenen Daten (Name, Kanzlei, "
                "Geschäftsadresse, Telefon, E-Mail) stammen aus den offiziellen öffentlichen "
                "Anwaltsregistern und betreffen die Berufsausübung, nicht das Privatleben.",
                "Betroffene Personen können eine Korrektur beantragen oder ihre Rechte über die Seite "
                "\u201eFehler melden\u201c geltend machen.",
            )},
        ]},
        "it": {"title": "Privacy", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis non richiede la creazione di alcun account e non raccoglie dati personali oltre "
                "alle informazioni tecniche standard di navigazione.",
                "I dati personali visualizzati nelle schede (nome, studio, indirizzo professionale, "
                "telefono, e-mail) provengono dai registri pubblici ufficiali degli avvocati e riguardano "
                "l'esercizio della professione, non la vita privata.",
                "Chiunque sia interessato può richiedere una correzione o far valere i propri diritti "
                "tramite la pagina «Segnala una correzione».",
            )},
        ]},
        "en": {"title": "Privacy", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis does not require any account creation and does not collect personal data beyond "
                "standard technical browsing information.",
                "The personal data shown on listings (name, firm, professional address, phone, email) "
                "comes from official public lawyer registers and relates to the exercise of their "
                "profession, not their private life.",
                "Anyone concerned can request a correction or exercise their rights via the \"Report a "
                "correction\" page.",
            )},
        ]},
    },
    "correction": {
        "fr": {"title": "Signaler une correction", "sections": [
            {"heading": None, "paragraphs": _p(
                "Une information est inexacte ou obsolète sur une fiche ? Vous êtes avocat·e ou "
                "responsable d'étude et cette fiche vous concerne ?",
                "Écrivez-nous à contact@legatis.ch en précisant l'URL de la fiche concernée et la "
                "correction à apporter (adresse, téléphone, e-mail, domaines de compétence, etc.). Nous "
                "vérifions et mettons à jour la fiche dans les meilleurs délais.",
            )},
        ]},
        "de": {"title": "Fehler melden", "sections": [
            {"heading": None, "paragraphs": _p(
                "Ist eine Angabe auf einer Seite falsch oder veraltet? Sind Sie Anwältin, Anwalt oder "
                "Kanzleiverantwortliche·r und diese Seite betrifft Sie?",
                "Schreiben Sie uns an contact@legatis.ch mit der URL der betreffenden Seite und der "
                "gewünschten Korrektur (Adresse, Telefon, E-Mail, Fachgebiete usw.). Wir prüfen die Angabe "
                "und aktualisieren die Seite so schnell wie möglich.",
            )},
        ]},
        "it": {"title": "Segnala una correzione", "sections": [
            {"heading": None, "paragraphs": _p(
                "Un'informazione è imprecisa o obsoleta su una scheda? Siete un avvocato o un responsabile "
                "di studio e questa scheda vi riguarda?",
                "Scriveteci a contact@legatis.ch indicando l'URL della scheda interessata e la correzione "
                "da apportare (indirizzo, telefono, e-mail, ambiti di competenza, ecc.). Verifichiamo e "
                "aggiorniamo la scheda il prima possibile.",
            )},
        ]},
        "en": {"title": "Report a correction", "sections": [
            {"heading": None, "paragraphs": _p(
                "Is some information inaccurate or outdated on a listing? Are you a lawyer or firm "
                "administrator and this listing concerns you?",
                "Write to us at contact@legatis.ch with the URL of the listing and the correction needed "
                "(address, phone, email, practice areas, etc.). We verify and update the listing as soon "
                "as possible.",
            )},
        ]},
    },
}
