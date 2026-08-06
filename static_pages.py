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
                {"heading": "Nos règles éditoriales : ne jamais inventer un fait", "paragraphs": _p(
                    "C'est la règle non négociable qui gouverne tout le contenu du site, y compris les "
                    "textes de présentation générés automatiquement pour chaque avocat et chaque étude. "
                    "Nous documentons ces règles ici plutôt que de simplement les appliquer en silence, "
                    "parce que la façon dont un fait est établi compte autant que le fait lui-même.",
                    "Une ancienneté ou une année de fondation n'est affichée que si elle est explicitement "
                    "écrite dans le registre officiel ou sur le site du cabinet, jamais déduite d'une "
                    "formulation vague comme « depuis plus de 20 ans ». Un effectif d'équipe n'est affiché "
                    "que s'il est annoncé en toutes lettres par le cabinet, jamais compté à partir du "
                    "nombre de profils listés sur une page « équipe », qui peut être partielle ou datée.",
                    "Quand une information vient du site web d'un cabinet plutôt que du registre officiel, "
                    "la fiche l'indique explicitement et mentionne la date à laquelle le site a été "
                    "consulté. Pour les cabinets appartenant à un réseau international, seules les "
                    "statistiques spécifiquement suisses sont retenues : un chiffre mondial du groupe "
                    "(« 10 000 collaborateurs dans le monde ») n'est jamais utilisé pour décrire l'antenne "
                    "suisse.",
                    "Un cabinet dont le site montre des signes de compromission (contenu suspect, "
                    "injection publicitaire) est exclu entièrement de l'enrichissement plutôt qu'utilisé "
                    "partiellement.",
                    "Une fiche sans aucun signal réel (ni ancienneté, ni langue, ni domaine de compétence, "
                    "ni enrichissement vérifié) est automatiquement exclue des moteurs de recherche "
                    "(balise « noindex ») jusqu'à ce qu'une donnée réelle soit disponible. Nous préférons "
                    "une fiche incomplète mais honnête à une fiche complétée artificiellement.",
                )},
                {"heading": "Indépendance", "paragraphs": _p(
                    "Aucun cabinet ni avocat ne peut payer pour être mieux classé, apparaître en premier, "
                    "ou faire modifier son texte de présentation dans un sens plus favorable. Le classement "
                    "au sein d'un canton ou d'une ville suit un ordre alphabétique ou le nombre de membres "
                    "d'une étude, jamais un critère commercial. Aucun avis ni note n'est affiché sur les "
                    "fiches : nous n'en collectons pas, donc nous n'en inventons pas.",
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
                    "von Test- oder fehlerhaften Einträgen). Es werden keine Angaben erfunden oder "
                    "geschätzt, die nicht in der Quelle vorhanden sind.",
                )},
                {"heading": "Erfasste Kantone", "paragraphs": _p(
                    "20 Kantone sind derzeit erfasst: " + ", ".join(COVERED_CANTONS_FR) + ".",
                    "6 Kantone sind mangels zugänglichem öffentlichem Register noch nicht erfasst: "
                    + ", ".join(BLOCKED_CANTONS_FR) + ". Sie werden ergänzt, sobald ein legitimer "
                    "Datenzugang möglich ist.",
                )},
                {"heading": "Unsere redaktionellen Regeln: nie einen Fakt erfinden", "paragraphs": _p(
                    "Das ist die nicht verhandelbare Regel, die den gesamten Inhalt der Seite bestimmt, "
                    "einschliesslich der automatisch erzeugten Vorstellungstexte für jede Anwältin, jeden "
                    "Anwalt und jede Kanzlei. Wir dokumentieren diese Regeln hier, statt sie nur still "
                    "anzuwenden, weil die Art und Weise, wie ein Fakt belegt ist, ebenso zählt wie der Fakt "
                    "selbst.",
                    "Ein Gründungsjahr oder eine Berufserfahrung wird nur angezeigt, wenn sie ausdrücklich "
                    "im offiziellen Register oder auf der Website der Kanzlei steht, nie abgeleitet aus "
                    "einer vagen Formulierung wie «seit über 20 Jahren». Eine Teamgrösse wird nur "
                    "angezeigt, wenn sie von der Kanzlei ausdrücklich genannt wird, nie aus der Anzahl der "
                    "auf einer Team-Seite gelisteten Profile gezählt, die unvollständig oder veraltet sein "
                    "kann.",
                    "Stammt eine Angabe von der Website einer Kanzlei statt aus dem offiziellen Register, "
                    "weist die Seite dies ausdrücklich aus und nennt das Datum des Abrufs. Bei Kanzleien "
                    "eines internationalen Netzwerks werden nur spezifisch schweizerische Kennzahlen "
                    "verwendet: eine weltweite Konzernzahl («10'000 Mitarbeitende weltweit») beschreibt nie "
                    "den Schweizer Standort.",
                    "Eine Kanzlei, deren Website Anzeichen einer Kompromittierung aufweist (verdächtiger "
                    "Inhalt, Werbe-Injektion), wird vollständig von der Anreicherung ausgeschlossen, statt "
                    "teilweise genutzt zu werden.",
                    "Eine Seite ohne jedes reale Signal (weder Berufserfahrung noch Sprache, Fachgebiet "
                    "oder verifizierte Anreicherung) wird automatisch von Suchmaschinen ausgeschlossen "
                    "(«noindex»-Tag), bis eine reale Angabe verfügbar ist. Wir bevorzugen eine "
                    "unvollständige, aber ehrliche Seite gegenüber einer künstlich aufgefüllten.",
                )},
                {"heading": "Unabhängigkeit", "paragraphs": _p(
                    "Keine Kanzlei und keine Anwältin kann dafür bezahlen, besser platziert zu werden, "
                    "zuerst zu erscheinen, oder ihren Vorstellungstext in einem günstigeren Sinn ändern zu "
                    "lassen. Die Reihenfolge innerhalb eines Kantons oder einer Ortschaft folgt dem "
                    "Alphabet oder der Anzahl der Kanzleimitglieder, nie einem kommerziellen Kriterium. "
                    "Es werden keine Bewertungen oder Noten angezeigt: Wir erheben keine, also erfinden "
                    "wir keine.",
                )},
                {"heading": "Aktualität der Daten", "paragraphs": _p(
                    f"Diese Version des Registers wurde am {TODAY} erstellt. Ein fester Rhythmus für die "
                    "Neusynchronisation mit den offiziellen Registern ist noch nicht festgelegt.",
                )},
                {"heading": "Bekannte Einschränkungen", "paragraphs": _p(
                    "Fachgebiete sind nur für einen Teil der Genfer Anwältinnen und Anwälte erfasst, für "
                    "die übrigen 19 Kantone noch gar nicht. Diese Angabe fehlt schlicht in den "
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
                {"heading": "Le nostre regole editoriali: mai inventare un fatto", "paragraphs": _p(
                    "È la regola non negoziabile che governa tutto il contenuto del sito, compresi i testi "
                    "di presentazione generati automaticamente per ogni avvocato e ogni studio. "
                    "Documentiamo queste regole qui invece di applicarle semplicemente in silenzio, perché "
                    "il modo in cui un fatto viene stabilito conta quanto il fatto stesso.",
                    "Un'anzianità o un anno di fondazione è mostrato solo se scritto esplicitamente nel "
                    "registro ufficiale o sul sito dello studio, mai dedotto da una formulazione vaga come "
                    "«da oltre 20 anni». Un numero di collaboratori è mostrato solo se dichiarato "
                    "espressamente dallo studio, mai contato dal numero di profili elencati in una pagina "
                    "«team», che può essere parziale o non aggiornata.",
                    "Quando un'informazione proviene dal sito web di uno studio anziché dal registro "
                    "ufficiale, la scheda lo indica esplicitamente e menziona la data di consultazione del "
                    "sito. Per gli studi appartenenti a un network internazionale, si considerano solo le "
                    "statistiche specificamente svizzere: una cifra mondiale del gruppo («10'000 "
                    "collaboratori nel mondo») non viene mai usata per descrivere la sede svizzera.",
                    "Uno studio il cui sito mostra segni di compromissione (contenuto sospetto, iniezione "
                    "pubblicitaria) viene escluso interamente dall'arricchimento invece di essere utilizzato "
                    "parzialmente.",
                    "Una scheda priva di qualsiasi segnale reale (né anzianità, né lingua, né ambito di "
                    "competenza, né arricchimento verificato) viene automaticamente esclusa dai motori di "
                    "ricerca (tag «noindex») finché non è disponibile un dato reale. Preferiamo una scheda "
                    "incompleta ma onesta a una completata artificialmente.",
                )},
                {"heading": "Indipendenza", "paragraphs": _p(
                    "Nessuno studio o avvocato può pagare per essere classificato meglio, apparire per "
                    "primo, o far modificare il proprio testo di presentazione in senso più favorevole. "
                    "L'ordine all'interno di un cantone o di una città segue l'alfabeto o il numero di "
                    "membri di uno studio, mai un criterio commerciale. Nessuna recensione o valutazione "
                    "è mostrata sulle schede: non le raccogliamo, quindi non le inventiamo.",
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
                {"heading": "Our editorial rules: never invent a fact", "paragraphs": _p(
                    "This is the non-negotiable rule governing every piece of content on the site, "
                    "including the automatically generated presentation text for each lawyer and firm. We "
                    "document these rules here rather than simply applying them silently, because how a "
                    "fact is established matters as much as the fact itself.",
                    "A firm's seniority or founding year is only shown if explicitly written in the "
                    "official register or on the firm's website, never inferred from a vague phrase like "
                    "\"for over 20 years\". A team size is only shown if explicitly stated by the firm "
                    "itself, never counted from the number of profiles listed on a \"team\" page, which "
                    "may be partial or outdated.",
                    "When a piece of information comes from a firm's website rather than the official "
                    "register, the listing says so explicitly and states the date the website was "
                    "accessed. For firms belonging to an international network, only Switzerland-specific "
                    "figures are used: a global network statistic (\"10,000 staff worldwide\") is never "
                    "used to describe the Swiss office.",
                    "A firm whose website shows signs of compromise (suspicious content, ad injection) is "
                    "excluded entirely from enrichment rather than used partially.",
                    "A listing with no real signal at all (no seniority, language, practice area, or "
                    "verified enrichment) is automatically excluded from search engines (\"noindex\" tag) "
                    "until real data becomes available. We prefer an incomplete but honest listing over "
                    "one artificially filled in.",
                )},
                {"heading": "Independence", "paragraphs": _p(
                    "No firm or lawyer can pay to rank higher, appear first, or have their presentation "
                    "text edited in a more favourable direction. Ordering within a canton or city follows "
                    "the alphabet or firm size, never a commercial criterion. No reviews or ratings are "
                    "shown on listings: we don't collect any, so we don't invent any.",
                )},
                {"heading": "Data freshness", "paragraphs": _p(
                    f"This version of the register was generated on {TODAY}. A fixed resynchronisation "
                    "schedule with the official registers has not yet been set.",
                )},
                {"heading": "Known limitations", "paragraphs": _p(
                    "Practice areas are only recorded for a portion of Geneva lawyers, and not yet for the "
                    "other 19 covered cantons. This information is simply absent from the source registers "
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
            {"heading": "Notre mission", "paragraphs": _p(
                "Legatis est l'annuaire de référence des avocats en Suisse : un registre public et "
                "gratuit, construit à partir des registres officiels cantonaux, en français, allemand, "
                "italien et anglais. L'objectif est que n'importe qui puisse vérifier rapidement qu'un "
                "avocat est bien inscrit au barreau et retrouver ses coordonnées officielles.",
            )},
            {"heading": "Notre indépendance", "paragraphs": _p(
                "Pas de compte utilisateur, pas de classement payant, pas d'avis fabriqués. Un cabinet ne "
                "peut pas payer pour être mieux placé ni pour faire modifier sa fiche dans un sens plus "
                "favorable. Voir le détail de nos règles éditoriales sur la page méthodologie. Legatis "
                "n'a pas vocation à générer des prospects payants pour les études référencées.",
            )},
            {"heading": "Où en est le projet", "paragraphs": _p(
                "Le projet est encore jeune : certaines données restent incomplètes (voir la page "
                "méthodologie) et six cantons ne sont pas encore couverts. La collecte et l'enrichissement "
                "des données se poursuivent en continu ; le site s'améliore progressivement plutôt que de "
                "prétendre être terminé.",
                "Vous êtes avocat·e ou responsable d'étude et souhaitez signaler une inexactitude ou "
                "compléter votre fiche ? Rendez-vous sur la page « Signaler une correction ».",
            )},
        ]},
        "de": {"title": "Über uns", "sections": [
            {"heading": "Unsere Mission", "paragraphs": _p(
                "Legatis ist das Referenzverzeichnis der Anwältinnen und Anwälte in der Schweiz: ein "
                "öffentliches, kostenloses Register auf Basis der offiziellen kantonalen Register, auf "
                "Französisch, Deutsch, Italienisch und Englisch. Ziel ist es, dass jede und jeder schnell "
                "prüfen kann, ob eine Anwältin oder ein Anwalt tatsächlich im Register eingetragen ist, und "
                "die offiziellen Kontaktdaten findet.",
            )},
            {"heading": "Unsere Unabhängigkeit", "paragraphs": _p(
                "Kein Benutzerkonto, kein bezahltes Ranking, keine erfundenen Bewertungen. Eine Kanzlei "
                "kann nicht dafür bezahlen, besser platziert zu werden oder ihren Eintrag in einem "
                "günstigeren Sinn ändern zu lassen. Details zu unseren redaktionellen Regeln auf der "
                "Methodik-Seite. Legatis hat nicht zum Ziel, kostenpflichtige Leads für die erfassten "
                "Kanzleien zu generieren.",
            )},
            {"heading": "Stand des Projekts", "paragraphs": _p(
                "Das Projekt ist noch jung: manche Daten sind noch unvollständig (siehe Methodik-Seite), "
                "und sechs Kantone sind noch nicht erfasst. Die Datenerhebung und -anreicherung läuft "
                "laufend weiter; die Seite wird schrittweise verbessert, statt vorzugeben, fertig zu sein.",
                "Sind Sie Anwältin, Anwalt oder Kanzleiverantwortliche·r und möchten eine Ungenauigkeit "
                "melden oder Ihren Eintrag ergänzen? Nutzen Sie die Seite «Fehler melden».",
            )},
        ]},
        "it": {"title": "Chi siamo", "sections": [
            {"heading": "La nostra missione", "paragraphs": _p(
                "Legatis è l'elenco di riferimento degli avvocati in Svizzera: un registro pubblico e "
                "gratuito, costruito a partire dai registri ufficiali cantonali, in francese, tedesco, "
                "italiano e inglese. L'obiettivo è permettere a chiunque di verificare rapidamente che un "
                "avvocato sia effettivamente iscritto all'albo e di trovarne i contatti ufficiali.",
            )},
            {"heading": "La nostra indipendenza", "paragraphs": _p(
                "Nessun account utente, nessuna classifica a pagamento, nessuna recensione inventata. Uno "
                "studio non può pagare per essere posizionato meglio né per far modificare la propria "
                "scheda in senso più favorevole. Dettagli delle nostre regole editoriali sulla pagina "
                "metodologia. Legatis non ha lo scopo di generare contatti commerciali a pagamento per gli "
                "studi censiti.",
            )},
            {"heading": "A che punto è il progetto", "paragraphs": _p(
                "Il progetto è ancora giovane: alcuni dati restano incompleti (vedi la pagina metodologia) "
                "e sei cantoni non sono ancora coperti. La raccolta e l'arricchimento dei dati proseguono "
                "in continuo; il sito viene migliorato progressivamente invece di presentarsi come finito.",
                "Siete un avvocato o un responsabile di studio e volete segnalare un'imprecisione o "
                "completare la vostra scheda? Andate alla pagina «Segnala una correzione».",
            )},
        ]},
        "en": {"title": "About", "sections": [
            {"heading": "Our mission", "paragraphs": _p(
                "Legatis is Switzerland's reference directory of lawyers: a free, public register built "
                "from official cantonal registers, in French, German, Italian and English. The goal is "
                "for anyone to quickly verify that a lawyer is genuinely registered with the bar and find "
                "their official contact details.",
            )},
            {"heading": "Our independence", "paragraphs": _p(
                "No user accounts, no paid ranking, no fabricated reviews. A firm cannot pay to rank "
                "higher or to have its listing edited in a more favourable direction. See our editorial "
                "rules on the methodology page. Legatis is not built to generate paid leads for the firms "
                "it lists.",
            )},
            {"heading": "Where the project stands", "paragraphs": _p(
                "The project is still young: some data remains incomplete (see the methodology page) and "
                "six cantons are not yet covered. Data collection and enrichment continue on an ongoing "
                "basis; the site is improved progressively rather than presented as finished.",
                "Are you a lawyer or firm administrator and want to report an inaccuracy or complete your "
                "listing? Go to the \"Report a correction\" page.",
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
                "\u201eFehler melden\u201c, so k\u00f6nnen wir die Anfrage schneller bearbeiten.",
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
                "instead, it lets us handle the request faster.",
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
    "revendiquer": {
        "fr": {"title": "Revendiquer votre fiche", "sections": [
            {"heading": "Votre fiche vous appartient", "paragraphs": _p(
                "Chaque fiche avocat ou étude sur Legatis provient d'un registre cantonal officiel. Si "
                "vous êtes la personne ou le cabinet concerné, vous pouvez à tout moment demander une "
                "correction, un complément d'information, ou même le retrait de votre fiche, gratuitement "
                "et sans justification à fournir au-delà de la preuve de votre identité professionnelle.",
            )},
            {"heading": "Le badge « Référencé sur Legatis »", "paragraphs": _p(
                "Chaque fiche étude et avocat propose un badge et un code d'intégration prêts à copier, "
                "avec un lien direct vers votre fiche. L'ajouter à votre site indique à vos clients que "
                "votre inscription au barreau est vérifiable publiquement, et nous aide à faire connaître "
                "un annuaire indépendant, sans classement payant.",
                "Aucune inscription, aucun compte, aucun paiement n'est nécessaire pour utiliser ce badge : "
                "il suffit de copier le code présent sur votre fiche.",
            )},
            {"heading": "Ce que nous garantissons", "paragraphs": _p(
                "Revendiquer ou corriger votre fiche ne change jamais son classement : l'ordre d'affichage "
                "suit l'alphabet ou le nombre de membres d'une étude, jamais un critère commercial (voir "
                "notre page méthodologie). Nous ne vendons pas de mise en avant.",
            )},
            {"heading": "Une vitrine personnelle gratuite", "paragraphs": _p(
                "Vous pouvez aussi demander une page personnelle plus complète (photo, présentation, "
                "spécialités mises en avant), hébergée sur Legatis, que vous pouvez mettre en avant sur "
                "votre fiche Google Business Profile ou votre propre site. Gratuit, sans engagement, "
                "chaque demande est vérifiée avant publication. Le lien du formulaire figure sur chaque "
                "fiche avocat, à côté du badge.",
            )},
            {"heading": "Comment procéder", "paragraphs": _p(
                "Écrivez-nous à contact@legatis.ch avec l'URL de votre fiche et la nature de votre demande "
                "(correction, complément, retrait). Nous vérifions et traitons chaque demande "
                "individuellement.",
            )},
        ]},
        "de": {"title": "Ihren Eintrag beanspruchen", "sections": [
            {"heading": "Ihr Eintrag gehört Ihnen", "paragraphs": _p(
                "Jeder Anwalts- oder Kanzleieintrag auf Legatis stammt aus einem offiziellen kantonalen "
                "Register. Sind Sie die betroffene Person oder Kanzlei, können Sie jederzeit eine "
                "Korrektur, eine Ergänzung oder sogar die Entfernung Ihres Eintrags verlangen, "
                "kostenlos und ohne weitere Begründung als den Nachweis Ihrer beruflichen Identität.",
            )},
            {"heading": "Das Badge «Erfasst auf Legatis»", "paragraphs": _p(
                "Jeder Kanzlei- und Anwaltseintrag bietet ein Badge samt fertigem Einbindungscode mit "
                "direktem Link zu Ihrem Eintrag. Es auf Ihrer Website einzubinden zeigt Ihren Mandantinnen "
                "und Mandanten, dass Ihre Zulassung öffentlich überprüfbar ist, und hilft, ein "
                "unabhängiges Verzeichnis ohne bezahltes Ranking bekannter zu machen.",
                "Für die Nutzung des Badges ist keine Anmeldung, kein Konto und keine Zahlung nötig: "
                "kopieren Sie einfach den Code auf Ihrem Eintrag.",
            )},
            {"heading": "Was wir garantieren", "paragraphs": _p(
                "Die Beanspruchung oder Korrektur Ihres Eintrags ändert nie dessen Platzierung: Die "
                "Reihenfolge folgt dem Alphabet oder der Anzahl der Kanzleimitglieder, nie einem "
                "kommerziellen Kriterium (siehe unsere Methodik-Seite). Wir verkaufen keine "
                "Hervorhebung.",
            )},
            {"heading": "So gehen Sie vor", "paragraphs": _p(
                "Schreiben Sie uns an contact@legatis.ch mit der URL Ihres Eintrags und der Art Ihres "
                "Anliegens (Korrektur, Ergänzung, Entfernung). Wir prüfen und bearbeiten jede Anfrage "
                "einzeln.",
            )},
        ]},
        "it": {"title": "Rivendicare la vostra scheda", "sections": [
            {"heading": "La vostra scheda vi appartiene", "paragraphs": _p(
                "Ogni scheda avvocato o studio su Legatis proviene da un registro cantonale ufficiale. Se "
                "siete la persona o lo studio interessato, potete in qualsiasi momento richiedere una "
                "correzione, un'integrazione, o persino la rimozione della vostra scheda, gratuitamente e "
                "senza dover fornire giustificazioni oltre alla prova della vostra identità "
                "professionale.",
            )},
            {"heading": "Il badge «Censito su Legatis»", "paragraphs": _p(
                "Ogni scheda studio e avvocato propone un badge e un codice di integrazione pronti da "
                "copiare, con un link diretto alla vostra scheda. Aggiungerlo al vostro sito indica ai "
                "vostri clienti che la vostra iscrizione all'albo è verificabile pubblicamente, e ci aiuta "
                "a far conoscere un elenco indipendente, senza classifiche a pagamento.",
                "Non è necessaria alcuna registrazione, account o pagamento per usare questo badge: basta "
                "copiare il codice presente sulla vostra scheda.",
            )},
            {"heading": "Cosa garantiamo", "paragraphs": _p(
                "Rivendicare o correggere la vostra scheda non ne modifica mai la posizione: l'ordine "
                "segue l'alfabeto o il numero di membri di uno studio, mai un criterio commerciale (vedi "
                "la nostra pagina metodologia). Non vendiamo posizionamenti in evidenza.",
            )},
            {"heading": "Come procedere", "paragraphs": _p(
                "Scriveteci a contact@legatis.ch con l'URL della vostra scheda e la natura della richiesta "
                "(correzione, integrazione, rimozione). Verifichiamo e trattiamo ogni richiesta "
                "individualmente.",
            )},
        ]},
        "en": {"title": "Claim your listing", "sections": [
            {"heading": "Your listing belongs to you", "paragraphs": _p(
                "Every lawyer or firm listing on Legatis comes from an official cantonal register. If "
                "you're the person or firm concerned, you can request a correction, an addition, or even "
                "the removal of your listing at any time, free of charge and without needing to provide "
                "anything beyond proof of your professional identity.",
            )},
            {"heading": "The \"Listed on Legatis\" badge", "paragraphs": _p(
                "Every firm and lawyer listing offers a ready-to-copy badge and embed code linking "
                "directly to your listing. Adding it to your website tells your clients that your bar "
                "registration is publicly verifiable, and helps spread the word about an independent "
                "directory with no paid ranking.",
                "No sign-up, account, or payment is needed to use this badge: just copy the code shown on "
                "your listing.",
            )},
            {"heading": "What we guarantee", "paragraphs": _p(
                "Claiming or correcting your listing never changes its ranking: display order follows the "
                "alphabet or firm size, never a commercial criterion (see our methodology page). We do "
                "not sell featured placement.",
            )},
            {"heading": "How to proceed", "paragraphs": _p(
                "Write to us at contact@legatis.ch with your listing's URL and the nature of your request "
                "(correction, addition, removal). We review and handle every request individually.",
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
