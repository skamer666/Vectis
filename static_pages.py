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
                "gregoiregiuliano@hotmail.com.",
                "Pour signaler une erreur sur une fiche précise, utilisez plutôt la page « Signaler une "
                "correction », qui nous permet de traiter la demande plus rapidement.",
            )},
        ]},
        "de": {"title": "Kontakt", "sections": [
            {"heading": None, "paragraphs": _p(
                "Für allgemeine Fragen, Presseanfragen oder Partnerschaften: gregoiregiuliano@hotmail.com.",
                "Um einen Fehler auf einer bestimmten Seite zu melden, nutzen Sie bitte die Seite "
                "„Fehler melden“, so können wir die Anfrage schneller bearbeiten.",
            )},
        ]},
        "it": {"title": "Contatto", "sections": [
            {"heading": None, "paragraphs": _p(
                "Per qualsiasi domanda generale, richiesta stampa o di partnership: "
                "gregoiregiuliano@hotmail.com.",
                "Per segnalare un errore su una scheda specifica, utilizzate invece la pagina "
                "«Segnala una correzione», che ci permette di gestire la richiesta più rapidamente.",
            )},
        ]},
        "en": {"title": "Contact", "sections": [
            {"heading": None, "paragraphs": _p(
                "For general questions, press or partnership enquiries: gregoiregiuliano@hotmail.com.",
                "To report an error on a specific listing, please use the \"Report a correction\" page "
                "instead, it lets us handle the request faster.",
            )},
        ]},
    },
    "mentions-legales": {
        "fr": {"title": "Mentions légales", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis est édité par Grégoire Giuliano, à titre individuel. Le site n'est à ce jour "
                "rattaché à aucune structure juridique enregistrée (pas de raison de commerce inscrite au "
                "registre du commerce, pas de numéro IDE) ; cette page sera mise à jour dès qu'une telle "
                "structure existera.",
                "Contact : gregoiregiuliano@hotmail.com",
            )},
            {"heading": "Hébergement", "paragraphs": _p(
                "Le site est hébergé par Cloudflare, Inc. (San Francisco, États-Unis) au moyen de son offre "
                "Workers. La base de données et l'authentification sont hébergées par Supabase Inc., sur "
                "des serveurs situés dans l'Union européenne (Irlande). Les emails transactionnels sont "
                "envoyés via Resend.",
            )},
            {"heading": "Contenu du site", "paragraphs": _p(
                "Les données publiées sur les fiches avocats et études proviennent des registres cantonaux "
                "officiels des avocats (voir la page méthodologie) et sont republiées à titre d'information "
                "publique.",
                "Les articles de blog et guides pratiques s'appuient sur les textes de loi suisses en "
                "vigueur (Code des obligations, Code civil, Code de procédure civile et pénale, etc.). Ils "
                "ont une valeur informative générale et ne constituent pas un conseil juridique personnalisé "
                ": pour une situation particulière, consultez un avocat inscrit sur l'un des registres "
                "référencés par Legatis.",
            )},
            {"heading": "Propriété intellectuelle", "paragraphs": _p(
                "Le contenu éditorial propre à Legatis (articles, guides, outils) peut être cité avec "
                "attribution et lien vers la page d'origine ; toute reproduction intégrale nécessite un "
                "accord préalable.",
            )},
        ]},
        "de": {"title": "Impressum", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis wird von Grégoire Giuliano in eigenem Namen betrieben. Die Website ist derzeit "
                "keiner eingetragenen juristischen Struktur zugeordnet (keine Eintragung im Handelsregister, "
                "keine UID-Nummer); diese Seite wird aktualisiert, sobald eine solche Struktur besteht.",
                "Kontakt: gregoiregiuliano@hotmail.com",
            )},
            {"heading": "Hosting", "paragraphs": _p(
                "Die Website wird von Cloudflare, Inc. (San Francisco, USA) über deren Workers-Angebot "
                "gehostet. Datenbank und Authentifizierung werden von Supabase Inc. auf Servern in der "
                "Europäischen Union (Irland) gehostet. Transaktions-E-Mails werden über Resend versendet.",
            )},
            {"heading": "Inhalt der Website", "paragraphs": _p(
                "Die auf den Anwalts- und Kanzleiprofilen veröffentlichten Daten stammen aus den offiziellen "
                "kantonalen Anwaltsregistern (siehe Methodik-Seite) und werden als öffentliche Information "
                "weiterveröffentlicht.",
                "Die Blogartikel und praktischen Ratgeber stützen sich auf geltendes Schweizer Recht "
                "(Obligationenrecht, Zivilgesetzbuch, Zivil- und Strafprozessordnung usw.). Sie haben "
                "allgemeinen informativen Wert und stellen keine individuelle Rechtsberatung dar: Wenden Sie "
                "sich für Ihre persönliche Situation an eine Anwältin oder einen Anwalt, die bzw. der in "
                "einem der von Legatis referenzierten Register eingetragen ist.",
            )},
            {"heading": "Geistiges Eigentum", "paragraphs": _p(
                "Die redaktionellen Inhalte von Legatis (Artikel, Ratgeber, Tools) dürfen mit Quellenangabe "
                "und Link zur Originalseite zitiert werden; eine vollständige Vervielfältigung bedarf einer "
                "vorherigen Zustimmung.",
            )},
        ]},
        "it": {"title": "Note legali", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis è gestito da Grégoire Giuliano, a titolo individuale. Il sito non è ad oggi "
                "collegato ad alcuna struttura giuridica registrata (nessuna iscrizione al registro di "
                "commercio, nessun numero IDI); questa pagina sarà aggiornata non appena tale struttura "
                "esisterà.",
                "Contatto: gregoiregiuliano@hotmail.com",
            )},
            {"heading": "Hosting", "paragraphs": _p(
                "Il sito è ospitato da Cloudflare, Inc. (San Francisco, Stati Uniti) tramite la sua offerta "
                "Workers. Il database e l'autenticazione sono ospitati da Supabase Inc., su server situati "
                "nell'Unione Europea (Irlanda). Le email transazionali sono inviate tramite Resend.",
            )},
            {"heading": "Contenuto del sito", "paragraphs": _p(
                "I dati pubblicati sulle schede di avvocati e studi provengono dai registri cantonali "
                "ufficiali degli avvocati (vedi la pagina metodologia) e sono ripubblicati a titolo di "
                "informazione pubblica.",
                "Gli articoli del blog e le guide pratiche si basano sui testi di legge svizzeri in vigore "
                "(Codice delle obbligazioni, Codice civile, Codice di procedura civile e penale, ecc.). Hanno "
                "un valore informativo generale e non costituiscono una consulenza legale personalizzata: "
                "per una situazione particolare, consultate un avvocato iscritto in uno dei registri "
                "referenziati da Legatis.",
            )},
            {"heading": "Proprietà intellettuale", "paragraphs": _p(
                "I contenuti editoriali propri di Legatis (articoli, guide, strumenti) possono essere citati "
                "con attribuzione e link alla pagina originale; qualsiasi riproduzione integrale richiede "
                "un accordo preventivo.",
            )},
        ]},
        "en": {"title": "Legal notice", "sections": [
            {"heading": None, "paragraphs": _p(
                "Legatis is published by Grégoire Giuliano, in an individual capacity. The site is not "
                "currently attached to any registered legal entity (no registration with the commercial "
                "register, no business identification number); this page will be updated once such a "
                "structure exists.",
                "Contact: gregoiregiuliano@hotmail.com",
            )},
            {"heading": "Hosting", "paragraphs": _p(
                "The site is hosted by Cloudflare, Inc. (San Francisco, USA) via its Workers offering. The "
                "database and authentication are hosted by Supabase Inc., on servers located in the "
                "European Union (Ireland). Transactional emails are sent via Resend.",
            )},
            {"heading": "Site content", "paragraphs": _p(
                "The data published on lawyer and firm listings comes from official cantonal lawyer "
                "registers (see the methodology page) and is republished as public information.",
                "The blog articles and practical guides are based on Swiss law currently in force (Code of "
                "Obligations, Civil Code, Civil and Criminal Procedure Codes, etc.). They provide general "
                "informational value and do not constitute personalised legal advice: for your specific "
                "situation, consult a lawyer registered in one of the registers Legatis references.",
            )},
            {"heading": "Intellectual property", "paragraphs": _p(
                "Legatis's own editorial content (articles, guides, tools) may be quoted with attribution "
                "and a link to the original page; any full reproduction requires prior agreement.",
            )},
        ]},
    },
    "confidentialite": {
        "fr": {"title": "Confidentialité", "sections": [
            {"heading": None, "paragraphs": _p(
                "Consulter l'annuaire, rechercher un avocat, lire les articles et guides, ou utiliser les "
                "outils gratuits ne nécessite jamais de compte ni de donnée personnelle.",
                "Les données personnelles affichées sur les fiches (nom, étude, adresse professionnelle, "
                "téléphone, e-mail) proviennent des registres publics officiels des avocats et concernent "
                "l'exercice de leur profession, pas leur vie privée. Toute personne concernée peut demander "
                "une correction, un complément ou le retrait de sa fiche via la page « Signaler une "
                "correction ».",
                "Le responsable du traitement des données décrites ci-dessous est Grégoire Giuliano (voir "
                "mentions légales). Contact : gregoiregiuliano@hotmail.com.",
            )},
            {"heading": "Compte avocat et vérification d'identité", "paragraphs": _p(
                "La création d'un compte n'est nécessaire que pour les avocats souhaitant revendiquer et "
                "gérer leur propre fiche : elle demande une adresse e-mail professionnelle et un mot de "
                "passe, vérifiés avant activation.",
                "Selon le palier de vérification choisi, confirmer son identité peut nécessiter l'envoi "
                "d'une pièce d'identité et d'un selfie. Ces documents sont stockés dans un espace privé, "
                "utilisés uniquement pour cette vérification, et supprimés immédiatement après la décision "
                "(compte activé ou refusé) — ils ne sont jamais conservés au-delà, quelle que soit l'issue.",
            )},
            {"heading": "Consentements (emails, avis)", "paragraphs": _p(
                "Deux cases à cocher facultatives et décochées par défaut existent sur le site : recevoir "
                "des emails Legatis (actualités, conseils) lors de la création d'un compte avocat, et être "
                "recontacté pour laisser un avis après avoir consulté une fiche. Aucune des deux n'est "
                "jamais cochée automatiquement.",
                "Pour chaque consentement donné, ainsi que pour l'acceptation du contrat de l'offre « site "
                "web gratuit » (proposée uniquement aux avocats ayant déjà un compte vérifié), nous "
                "conservons l'horodatage et l'adresse IP au moment de l'action, en plus de l'identité ou de "
                "l'adresse email associée — cela sert uniquement de preuve que le consentement a bien été "
                "donné, jamais à un autre usage. Vous pouvez retirer votre consentement à tout moment en "
                "nous écrivant.",
            )},
            {"heading": "Avis et demandes de contact", "paragraphs": _p(
                "Les avis publiés sur les fiches sont soumis par leurs auteurs (nom optionnel, email requis "
                "mais jamais publié) et modérés avant publication. Une demande de recevoir une sélection de "
                "fiches par email (formulaire présent sur les fiches à forte intention) enregistre "
                "l'adresse email fournie, utilisée uniquement pour cet envoi et, en cas de consentement "
                "explicite, pour une relance ultérieure (voir ci-dessus).",
            )},
            {"heading": "Statistiques de fréquentation", "paragraphs": _p(
                "Legatis mesure de façon agrégée la fréquentation du site (pages consultées, temps passé, "
                "provenance) au moyen d'un outil interne, sans recourir à Google Analytics ni à aucun "
                "service publicitaire tiers.",
                "Cette mesure ne repose sur aucun cookie et ne conserve jamais d'adresse IP. Un identifiant "
                "aléatoire, généré et stocké uniquement dans le navigateur (jamais transmis à un tiers, "
                "jamais relié à un nom, un e-mail ou un compte), permet uniquement de calculer des "
                "compteurs globaux tels que le taux de visiteurs revenus un autre jour ; aucune page interne "
                "de Legatis n'affiche de statistiques individuelles par visiteur.",
                "Un système distinct et purement technique de limitation de débit (anti-abus, contre le "
                "spam sur les formulaires publics) conserve une adresse IP de façon très brève (quelques "
                "minutes), sans lien avec les statistiques ci-dessus ni avec un profil individuel.",
            )},
            {"heading": "Cookies et stockage local", "paragraphs": _p(
                "Legatis n'utilise aucun cookie de suivi ni service publicitaire tiers. Certaines "
                "fonctionnalités (favoris, comparatif d'avocats, session d'un avocat connecté) utilisent le "
                "stockage local de votre navigateur (localStorage) : ces données restent sur votre appareil, "
                "ne sont jamais transmises à un tiers, et sont accessibles uniquement par vous. Vous pouvez "
                "les effacer à tout moment via les réglages de votre navigateur.",
            )},
            {"heading": "Sous-traitants", "paragraphs": _p(
                "Pour fonctionner, Legatis fait appel aux prestataires suivants, chacun agissant comme "
                "sous-traitant : Supabase Inc. pour la base de données et l'authentification, hébergées "
                "dans l'Union européenne (Irlande) ; Resend pour l'envoi des emails transactionnels ; "
                "Cloudflare, Inc. pour l'hébergement et la diffusion du site.",
            )},
            {"heading": "Vos droits", "paragraphs": _p(
                "Vous pouvez demander l'accès, la rectification ou la suppression des données vous "
                "concernant, ou retirer un consentement donné, en écrivant à gregoiregiuliano@hotmail.com.",
            )},
        ]},
        "de": {"title": "Datenschutz", "sections": [
            {"heading": None, "paragraphs": _p(
                "Das Verzeichnis zu durchsuchen, eine Anwältin oder einen Anwalt zu suchen, Artikel und "
                "Ratgeber zu lesen oder die kostenlosen Tools zu nutzen, erfordert nie ein Konto oder "
                "personenbezogene Daten.",
                "Die auf den Profilen angezeigten personenbezogenen Daten (Name, Kanzlei, Geschäftsadresse, "
                "Telefon, E-Mail) stammen aus den offiziellen öffentlichen Anwaltsregistern und betreffen "
                "die Berufsausübung, nicht das Privatleben. Betroffene Personen können eine Korrektur, eine "
                "Ergänzung oder die Entfernung ihres Eintrags über die Seite „Fehler melden“ beantragen.",
                "Verantwortlich für die unten beschriebene Datenverarbeitung ist Grégoire Giuliano (siehe "
                "Impressum). Kontakt: gregoiregiuliano@hotmail.com.",
            )},
            {"heading": "Anwaltskonto und Identitätsprüfung", "paragraphs": _p(
                "Eine Kontoerstellung ist nur für Anwältinnen und Anwälte erforderlich, die ihr eigenes "
                "Profil beanspruchen und verwalten möchten: sie erfordert eine berufliche E-Mail-Adresse "
                "und ein Passwort, die vor Aktivierung überprüft werden.",
                "Je nach gewählter Prüfstufe kann die Identitätsbestätigung das Hochladen eines "
                "Ausweisdokuments und eines Selfies erfordern. Diese Dokumente werden in einem privaten "
                "Bereich gespeichert, ausschliesslich für diese Prüfung verwendet und unmittelbar nach der "
                "Entscheidung gelöscht (Konto aktiviert oder abgelehnt) — sie werden unabhängig vom Ausgang "
                "nie darüber hinaus aufbewahrt.",
            )},
            {"heading": "Einwilligungen (E-Mails, Bewertungen)", "paragraphs": _p(
                "Auf der Website gibt es zwei freiwillige, standardmässig nicht angehakte Kontrollkästchen: "
                "Legatis-E-Mails erhalten (Neuigkeiten, Tipps) bei der Erstellung eines Anwaltskontos, und "
                "erneut kontaktiert werden, um nach dem Ansehen eines Profils eine Bewertung abzugeben. "
                "Keines der beiden wird je automatisch angehakt.",
                "Für jede erteilte Einwilligung sowie für die Annahme des Vertrags des Angebots „kostenlose "
                "Website“ (nur Anwältinnen und Anwälten mit bereits verifiziertem Konto angeboten) speichern "
                "wir den Zeitstempel und die IP-Adresse zum Zeitpunkt der Handlung, zusätzlich zur "
                "verknüpften Identität oder E-Mail-Adresse — dies dient ausschliesslich als Nachweis der "
                "erteilten Einwilligung, nie einem anderen Zweck. Sie können Ihre Einwilligung jederzeit "
                "widerrufen, indem Sie uns schreiben.",
            )},
            {"heading": "Bewertungen und Kontaktanfragen", "paragraphs": _p(
                "Die auf den Profilen veröffentlichten Bewertungen werden von ihren Verfasserinnen und "
                "Verfassern eingereicht (Name optional, E-Mail erforderlich, aber nie veröffentlicht) und "
                "vor der Veröffentlichung moderiert. Eine Anfrage, eine Auswahl von Profilen per E-Mail zu "
                "erhalten (Formular auf Profilen mit hoher Kaufabsicht), speichert die angegebene "
                "E-Mail-Adresse, die nur für diesen Versand und, bei ausdrücklicher Einwilligung, für eine "
                "spätere Erinnerung verwendet wird (siehe oben).",
            )},
            {"heading": "Nutzungsstatistiken", "paragraphs": _p(
                "Legatis misst die Besucherzahlen der Website in aggregierter Form (aufgerufene Seiten, "
                "Verweildauer, Herkunft) mit einem internen Werkzeug, ohne Google Analytics oder einen "
                "anderen Werbedienst eines Drittanbieters zu verwenden.",
                "Diese Messung basiert auf keinem Cookie und speichert niemals eine IP-Adresse. Eine "
                "zufällige, nur im Browser gespeicherte Kennung (nie an Dritte übermittelt, nie mit einem "
                "Namen, einer E-Mail-Adresse oder einem Konto verknüpft) dient ausschliesslich der "
                "Berechnung globaler Kennzahlen wie dem Anteil der an einem anderen Tag wiederkehrenden "
                "Besucherinnen und Besucher; keine interne Seite von Legatis zeigt individuelle "
                "Besucherstatistiken an.",
                "Ein separates, rein technisches System zur Ratenbegrenzung (Missbrauchsschutz gegen Spam "
                "auf öffentlichen Formularen) speichert eine IP-Adresse für sehr kurze Zeit (einige "
                "Minuten), ohne Zusammenhang mit den obigen Statistiken oder einem individuellen Profil.",
            )},
            {"heading": "Cookies und lokaler Speicher", "paragraphs": _p(
                "Legatis verwendet weder Tracking-Cookies noch Werbedienste Dritter. Einige Funktionen "
                "(Favoriten, Anwaltsvergleich, Sitzung eines eingeloggten Anwalts) nutzen den lokalen "
                "Speicher Ihres Browsers (localStorage): Diese Daten verbleiben auf Ihrem Gerät, werden nie "
                "an Dritte übermittelt und sind ausschliesslich für Sie zugänglich. Sie können sie "
                "jederzeit über die Einstellungen Ihres Browsers löschen.",
            )},
            {"heading": "Auftragsverarbeiter", "paragraphs": _p(
                "Für den Betrieb nutzt Legatis folgende Dienstleister, die jeweils als Auftragsverarbeiter "
                "handeln: Supabase Inc. für Datenbank und Authentifizierung, gehostet in der Europäischen "
                "Union (Irland); Resend für den Versand von Transaktions-E-Mails; Cloudflare, Inc. für das "
                "Hosting und die Auslieferung der Website.",
            )},
            {"heading": "Ihre Rechte", "paragraphs": _p(
                "Sie können Auskunft, Berichtigung oder Löschung der Sie betreffenden Daten verlangen oder "
                "eine erteilte Einwilligung widerrufen, indem Sie an gregoiregiuliano@hotmail.com schreiben.",
            )},
        ]},
        "it": {"title": "Privacy", "sections": [
            {"heading": None, "paragraphs": _p(
                "Consultare l'elenco, cercare un avvocato, leggere gli articoli e le guide, o utilizzare "
                "gli strumenti gratuiti non richiede mai un account né dati personali.",
                "I dati personali visualizzati nelle schede (nome, studio, indirizzo professionale, "
                "telefono, e-mail) provengono dai registri pubblici ufficiali degli avvocati e riguardano "
                "l'esercizio della professione, non la vita privata. Chiunque sia interessato può "
                "richiedere una correzione, un'integrazione o la rimozione della propria scheda tramite la "
                "pagina «Segnala una correzione».",
                "Il responsabile del trattamento dei dati descritti di seguito è Grégoire Giuliano (vedi "
                "note legali). Contatto: gregoiregiuliano@hotmail.com.",
            )},
            {"heading": "Account avvocato e verifica dell'identità", "paragraphs": _p(
                "La creazione di un account è necessaria solo per gli avvocati che desiderano rivendicare e "
                "gestire la propria scheda: richiede un indirizzo e-mail professionale e una password, "
                "verificati prima dell'attivazione.",
                "A seconda del livello di verifica scelto, confermare la propria identità può richiedere "
                "l'invio di un documento d'identità e di un selfie. Questi documenti sono conservati in "
                "uno spazio privato, utilizzati unicamente per questa verifica, ed eliminati "
                "immediatamente dopo la decisione (account attivato o rifiutato) — non vengono mai "
                "conservati oltre, indipendentemente dall'esito.",
            )},
            {"heading": "Consensi (email, recensioni)", "paragraphs": _p(
                "Sul sito esistono due caselle facoltative e deselezionate per impostazione predefinita: "
                "ricevere email Legatis (novità, consigli) al momento della creazione di un account "
                "avvocato, ed essere ricontattati per lasciare una recensione dopo aver consultato una "
                "scheda. Nessuna delle due è mai selezionata automaticamente.",
                "Per ogni consenso fornito, così come per l'accettazione del contratto dell'offerta "
                "«sito web gratuito» (proposta solo agli avvocati con un account già verificato), "
                "conserviamo la data e ora e l'indirizzo IP al momento dell'azione, oltre all'identità o "
                "all'indirizzo email associato — questo serve unicamente come prova che il consenso è "
                "stato effettivamente fornito, mai per un altro scopo. Potete revocare il vostro consenso "
                "in qualsiasi momento scrivendoci.",
            )},
            {"heading": "Recensioni e richieste di contatto", "paragraphs": _p(
                "Le recensioni pubblicate sulle schede sono inviate dai loro autori (nome facoltativo, "
                "email richiesta ma mai pubblicata) e moderate prima della pubblicazione. Una richiesta di "
                "ricevere una selezione di schede via email (modulo presente sulle schede ad alta "
                "intenzione) registra l'indirizzo email fornito, utilizzato unicamente per questo invio e, "
                "in caso di consenso esplicito, per un successivo sollecito (vedi sopra).",
            )},
            {"heading": "Statistiche di frequentazione", "paragraphs": _p(
                "Legatis misura in forma aggregata la frequentazione del sito (pagine consultate, tempo "
                "trascorso, provenienza) tramite uno strumento interno, senza ricorrere a Google Analytics "
                "né ad alcun servizio pubblicitario di terzi.",
                "Questa misurazione non si basa su alcun cookie e non conserva mai indirizzi IP. Un "
                "identificativo casuale, generato e conservato unicamente nel browser (mai trasmesso a "
                "terzi, mai collegato a un nome, un'e-mail o un account), serve unicamente a calcolare "
                "contatori globali come la percentuale di visitatori tornati in un altro giorno; nessuna "
                "pagina interna di Legatis mostra statistiche individuali per visitatore.",
                "Un sistema distinto e puramente tecnico di limitazione della frequenza (anti-abuso, contro "
                "lo spam sui moduli pubblici) conserva un indirizzo IP per un tempo molto breve (alcuni "
                "minuti), senza alcun legame con le statistiche sopra indicate né con un profilo "
                "individuale.",
            )},
            {"heading": "Cookie e archiviazione locale", "paragraphs": _p(
                "Legatis non utilizza alcun cookie di tracciamento né servizi pubblicitari di terzi. Alcune "
                "funzionalità (preferiti, confronto tra avvocati, sessione di un avvocato collegato) "
                "utilizzano l'archiviazione locale del vostro browser (localStorage): questi dati restano "
                "sul vostro dispositivo, non sono mai trasmessi a terzi, e sono accessibili solo da voi. "
                "Potete cancellarli in qualsiasi momento tramite le impostazioni del vostro browser.",
            )},
            {"heading": "Subappaltatori", "paragraphs": _p(
                "Per funzionare, Legatis si avvale dei seguenti fornitori, ciascuno agente come "
                "subappaltatore: Supabase Inc. per il database e l'autenticazione, ospitati nell'Unione "
                "Europea (Irlanda); Resend per l'invio delle email transazionali; Cloudflare, Inc. per "
                "l'hosting e la distribuzione del sito.",
            )},
            {"heading": "I vostri diritti", "paragraphs": _p(
                "Potete richiedere l'accesso, la rettifica o la cancellazione dei dati che vi riguardano, "
                "o revocare un consenso fornito, scrivendo a gregoiregiuliano@hotmail.com.",
            )},
        ]},
        "en": {"title": "Privacy", "sections": [
            {"heading": None, "paragraphs": _p(
                "Browsing the directory, searching for a lawyer, reading the articles and guides, or using "
                "the free tools never requires an account or any personal data.",
                "The personal data shown on listings (name, firm, professional address, phone, email) "
                "comes from official public lawyer registers and relates to the exercise of their "
                "profession, not their private life. Anyone concerned can request a correction, an "
                "addition, or the removal of their listing via the \"Report a correction\" page.",
                "The controller for the data described below is Grégoire Giuliano (see legal notice). "
                "Contact: gregoiregiuliano@hotmail.com.",
            )},
            {"heading": "Lawyer account and identity verification", "paragraphs": _p(
                "Creating an account is only required for lawyers who wish to claim and manage their own "
                "listing: it requires a professional email address and a password, verified before "
                "activation.",
                "Depending on the verification tier chosen, confirming your identity may require "
                "submitting an ID document and a selfie. These documents are stored in a private area, "
                "used only for this verification, and deleted immediately after the decision (account "
                "activated or declined) — they are never kept beyond that, regardless of the outcome.",
            )},
            {"heading": "Consents (emails, reviews)", "paragraphs": _p(
                "Two optional checkboxes, unchecked by default, exist on the site: receiving Legatis "
                "emails (news, tips) when creating a lawyer account, and being contacted again to leave a "
                "review after viewing a listing. Neither is ever checked automatically.",
                "For each consent given, as well as for accepting the contract for the \"free website\" "
                "offer (only presented to lawyers who already have a verified account), we keep the "
                "timestamp and IP address at the moment of the action, in addition to the associated "
                "identity or email address — this is used solely as proof that consent was actually given, "
                "never for any other purpose. You can withdraw your consent at any time by writing to us.",
            )},
            {"heading": "Reviews and contact requests", "paragraphs": _p(
                "Reviews published on listings are submitted by their authors (name optional, email "
                "required but never published) and moderated before publication. A request to receive a "
                "selection of listings by email (a form present on high-intent listings) stores the email "
                "address provided, used only for that email and, with explicit consent, for a later "
                "reminder (see above).",
            )},
            {"heading": "Usage statistics", "paragraphs": _p(
                "Legatis measures site traffic in aggregate form (pages viewed, time spent, referral "
                "source) using an in-house tool, without relying on Google Analytics or any third-party "
                "advertising service.",
                "This measurement does not rely on any cookie and never stores an IP address. A random "
                "identifier, generated and stored only in the browser (never transmitted to a third party, "
                "never linked to a name, email, or account), is used solely to compute aggregate counters "
                "such as the share of visitors who return on a different day; no internal Legatis page "
                "displays per-visitor statistics.",
                "A separate, purely technical rate-limiting system (anti-abuse, against spam on public "
                "forms) stores an IP address very briefly (a few minutes), unrelated to the statistics "
                "above or to any individual profile.",
            )},
            {"heading": "Cookies and local storage", "paragraphs": _p(
                "Legatis does not use any tracking cookies or third-party advertising services. Some "
                "features (favorites, lawyer comparison, a logged-in lawyer's session) use your browser's "
                "local storage (localStorage): this data stays on your device, is never transmitted to a "
                "third party, and is only accessible to you. You can clear it at any time via your "
                "browser's settings.",
            )},
            {"heading": "Sub-processors", "paragraphs": _p(
                "To operate, Legatis relies on the following providers, each acting as a sub-processor: "
                "Supabase Inc. for the database and authentication, hosted in the European Union (Ireland); "
                "Resend for sending transactional emails; Cloudflare, Inc. for hosting and delivering the "
                "site.",
            )},
            {"heading": "Your rights", "paragraphs": _p(
                "You can request access to, correction of, or deletion of data concerning you, or withdraw "
                "a consent you gave, by writing to gregoiregiuliano@hotmail.com.",
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
                "Écrivez-nous à gregoiregiuliano@hotmail.com avec l'URL de votre fiche et la nature de votre demande "
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
                "Schreiben Sie uns an gregoiregiuliano@hotmail.com mit der URL Ihres Eintrags und der Art Ihres "
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
                "Scriveteci a gregoiregiuliano@hotmail.com con l'URL della vostra scheda e la natura della richiesta "
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
                "Write to us at gregoiregiuliano@hotmail.com with your listing's URL and the nature of your request "
                "(correction, addition, removal). We review and handle every request individually.",
            )},
        ]},
    },
    "correction": {
        "fr": {"title": "Signaler une correction", "sections": [
            {"heading": None, "paragraphs": _p(
                "Une information est inexacte ou obsolète sur une fiche ? Vous êtes avocat·e ou "
                "responsable d'étude et cette fiche vous concerne ?",
                "Écrivez-nous à gregoiregiuliano@hotmail.com en précisant l'URL de la fiche concernée et la "
                "correction à apporter (adresse, téléphone, e-mail, domaines de compétence, etc.). Nous "
                "vérifions et mettons à jour la fiche dans les meilleurs délais.",
            )},
        ]},
        "de": {"title": "Fehler melden", "sections": [
            {"heading": None, "paragraphs": _p(
                "Ist eine Angabe auf einer Seite falsch oder veraltet? Sind Sie Anwältin, Anwalt oder "
                "Kanzleiverantwortliche·r und diese Seite betrifft Sie?",
                "Schreiben Sie uns an gregoiregiuliano@hotmail.com mit der URL der betreffenden Seite und der "
                "gewünschten Korrektur (Adresse, Telefon, E-Mail, Fachgebiete usw.). Wir prüfen die Angabe "
                "und aktualisieren die Seite so schnell wie möglich.",
            )},
        ]},
        "it": {"title": "Segnala una correzione", "sections": [
            {"heading": None, "paragraphs": _p(
                "Un'informazione è imprecisa o obsoleta su una scheda? Siete un avvocato o un responsabile "
                "di studio e questa scheda vi riguarda?",
                "Scriveteci a gregoiregiuliano@hotmail.com indicando l'URL della scheda interessata e la correzione "
                "da apportare (indirizzo, telefono, e-mail, ambiti di competenza, ecc.). Verifichiamo e "
                "aggiorniamo la scheda il prima possibile.",
            )},
        ]},
        "en": {"title": "Report a correction", "sections": [
            {"heading": None, "paragraphs": _p(
                "Is some information inaccurate or outdated on a listing? Are you a lawyer or firm "
                "administrator and this listing concerns you?",
                "Write to us at gregoiregiuliano@hotmail.com with the URL of the listing and the correction needed "
                "(address, phone, email, practice areas, etc.). We verify and update the listing as soon "
                "as possible.",
            )},
        ]},
    },
}
