#!/usr/bin/env python3
"""
Contenu du blog juridique (couche editoriale SEO), dans les 4 langues.
Meme regle de non-fabrication que guides_content.py : uniquement des
informations juridiques generales, stables et verifiables (articles de loi
cites explicitement : CO, CC, CP, CPC, CPP, LCR, LP, LEI, LDIP, LAT, etc.).
Aucun chiffre invente, aucune statistique sans source.

Structure : BLOG_ARTICLES est un dict {article_id: {...}}. Chaque article a
un "domaine_id" (cle de i18n.DOMAINES, pour le maillage avec les hubs
domaines existants) et une entree par langue disponible -- toutes les
langues ne sont pas forcement deja ecrites pour chaque article (rediaction
prevue par lots, voir data/BLOG_PROGRESS.md), gen_blog() dans build.py gere
cette situation sans planter (seules les langues presentes sont generees).

Chaque entree de langue :
{
    "slug": str,
    "title": str,
    "meta": str (<=158 caracteres idealement),
    "sections": [{"heading": str|None, "paragraphs": [str, ...]}, ...],
    "faq": [{"q": str, "a": str}, ...],
}
"""

BLOG_ARTICLES = {
    "licenciement-delais-conge-abusif": {
        "domaine_id": "droit_travail",
        "published": "2026-07-30",
        "fr": {
            "slug": "licenciement-delais-preavis-conge-abusif",
            "title": "Licenciement en Suisse : délais et congé abusif",
            "meta": "Délais de préavis légaux, licenciement abusif, protection en cas de maladie ou grossesse, résiliation immédiate : ce que prévoit le Code des obligations.",
            "sections": [
                {"heading": "La liberté de résiliation et ses limites", "paragraphs": [
                    "En droit suisse, le contrat de travail peut en principe être résilié par l'une ou l'autre partie sans devoir invoquer de motif : c'est le principe de la liberté de résiliation. Cette liberté n'est toutefois pas absolue. Elle est encadrée par des délais de préavis à respecter (art. 335c CO), par l'interdiction du licenciement abusif (art. 336 CO) et par des périodes de protection pendant lesquelles l'employeur ne peut pas résilier le contrat (art. 336c CO).",
                    "Ces règles protègent le travailleur, partie généralement considérée comme la plus faible du rapport de travail, sans pour autant transformer le licenciement en une procédure nécessitant un motif justifié comme c'est le cas dans d'autres pays.",
                ]},
                {"heading": "Les délais de préavis légaux", "paragraphs": [
                    "Sauf accord contraire écrit, la loi fixe des délais minimaux de préavis qui augmentent avec l'ancienneté (art. 335c al. 1 CO) : un mois pendant la première année de service, deux mois de la deuxième à la neuvième année, trois mois dès la dixième année. Le congé doit en principe être donné pour la fin d'un mois.",
                    "Pendant le temps d'essai (au maximum trois mois, art. 335b CO), le délai de congé est réduit à sept jours, sauf accord contraire, et le contrat peut être résilié pour n'importe quel jour de la semaine.",
                    "Un contrat individuel, un contrat-type de travail ou une convention collective peuvent prévoir des délais différents, mais jamais inférieurs à un mois après la période d'essai (art. 335c al. 2 CO).",
                ]},
                {"heading": "Le licenciement abusif", "paragraphs": [
                    "L'art. 336 CO énumère des motifs qui rendent un licenciement abusif : congé donné en raison d'une caractéristique personnelle du travailleur sans lien avec le rapport de travail, en raison de l'exercice d'un droit constitutionnel, dans le seul but d'empêcher la naissance de prétentions découlant du contrat, en raison de l'appartenance ou de la non-appartenance à un syndicat, pendant que le travailleur représente le personnel, ou en représailles à une plainte de bonne foi déposée contre l'employeur.",
                    "Le licenciement abusif reste valable : il met bel et bien fin au contrat. La sanction est financière (art. 336a CO) : le juge peut allouer une indemnité pouvant atteindre six mois de salaire, fixée selon les circonstances. Pour la faire valoir, la partie qui reçoit le congé doit y faire opposition par écrit avant la fin du délai de congé (art. 336b CO), puis agir en justice dans les 180 jours suivant la fin du contrat.",
                ]},
                {"heading": "Les périodes de protection contre le licenciement en temps inopportun", "paragraphs": [
                    "L'art. 336c CO interdit à l'employeur de résilier le contrat pendant certaines périodes : durant un service militaire ou de protection civile suisse obligatoire (et les quatre semaines qui précèdent et suivent s'il dure plus de onze jours), durant une incapacité de travail totale ou partielle due à la maladie ou à un accident non imputable à la faute du travailleur (30 jours pendant la première année de service, 90 jours de la deuxième à la cinquième année, 180 jours à partir de la sixième année), et durant la grossesse ainsi que les seize semaines qui suivent l'accouchement.",
                    "Un congé donné avant le début d'une de ces périodes, mais dont le délai n'a pas expiré avant que la période commence, est suspendu : il reprend son cours une fois la période de protection terminée (art. 336c al. 2 CO). Cette protection ne s'applique toutefois pas pendant le temps d'essai, ni lorsque le contrat est résilié pour justes motifs, ni au congé donné par le travailleur lui-même.",
                ]},
                {"heading": "La résiliation immédiate pour justes motifs", "paragraphs": [
                    "L'art. 337 CO permet à chaque partie de résilier le contrat en tout temps, sans respecter de délai de préavis, en cas de justes motifs : des circonstances qui rendent la continuation des rapports de travail insupportable selon les règles de la bonne foi. La loi ne dresse pas de liste exhaustive ; le juge apprécie chaque situation concrètement, en tenant compte de la gravité du manquement et de la fonction du travailleur.",
                    "Une résiliation immédiate prononcée sans justes motifs reste valable, mais elle ouvre le droit à des dommages-intérêts pour la partie lésée, calculés notamment sur ce qu'elle aurait touché si le contrat avait pris fin de manière ordinaire (art. 337c CO).",
                ]},
            ],
            "faq": [
                {"q": "Mon employeur peut-il me licencier sans me donner de motif ?",
                 "a": "Oui, en principe. Le droit suisse ne rend pas le licenciement conditionnel à un motif justifié. L'employeur doit toutefois respecter les délais de préavis légaux, ne pas se trouver dans une période de protection (art. 336c CO), et ne pas invoquer l'un des motifs listés comme abusifs à l'art. 336 CO."},
                {"q": "Que se passe-t-il si mon licenciement est abusif ?",
                 "a": "Le contrat prend quand même fin au terme du délai de congé : un licenciement abusif n'est pas annulé. Le travailleur peut en revanche réclamer une indemnité pouvant aller jusqu'à six mois de salaire (art. 336a CO), à condition d'avoir fait opposition par écrit avant la fin du délai de congé, puis d'avoir agi en justice dans les 180 jours suivant la fin des rapports de travail."},
                {"q": "Suis-je protégé si je suis en arrêt maladie au moment où je reçois mon congé ?",
                 "a": "Si l'incapacité de travail est totale ou partielle et non imputable à votre faute, l'art. 336c CO suspend l'effet du congé pendant une durée qui dépend de votre ancienneté (30, 90 ou 180 jours selon les cas). Le délai de préavis ne recommence à courir qu'une fois la période de protection terminée. Cette protection ne s'applique pas pendant le temps d'essai."},
                {"q": "Le délai de préavis peut-il être raccourci par contrat ?",
                 "a": "Un contrat individuel, un contrat-type ou une convention collective peuvent modifier les délais légaux, mais jamais en dessous d'un mois après la période d'essai (art. 335c al. 2 CO). Pendant le temps d'essai lui-même, le délai légal de sept jours peut être modifié par accord des parties."},
            ],
        },
        "de": {
            "slug": "kuendigung-fristen-missbraeuchliche-kuendigung",
            "title": "Kündigung in der Schweiz: Fristen und Kündigungsschutz",
            "meta": "Gesetzliche Kündigungsfristen, missbräuchliche Kündigung, Schutz bei Krankheit oder Schwangerschaft, fristlose Kündigung: was das Obligationenrecht vorsieht.",
            "sections": [
                {"heading": "Kündigungsfreiheit und ihre Grenzen", "paragraphs": [
                    "Im schweizerischen Recht kann das Arbeitsverhältnis grundsätzlich von beiden Parteien ohne Angabe eines Grundes gekündigt werden: Dies ist der Grundsatz der Kündigungsfreiheit. Diese Freiheit ist jedoch nicht unbeschränkt. Sie wird durch einzuhaltende Kündigungsfristen (Art. 335c OR), das Verbot der missbräuchlichen Kündigung (Art. 336 OR) und Sperrfristen, während derer der Arbeitgeber nicht kündigen darf (Art. 336c OR), eingeschränkt.",
                    "Diese Regeln schützen die Arbeitnehmerin oder den Arbeitnehmer, ohne die Kündigung selbst von einem gerechtfertigten Grund abhängig zu machen, wie dies in anderen Ländern der Fall ist.",
                ]},
                {"heading": "Die gesetzlichen Kündigungsfristen", "paragraphs": [
                    "Sofern nichts anderes schriftlich vereinbart ist, gelten mit zunehmender Dienstdauer steigende Mindestfristen (Art. 335c Abs. 1 OR): ein Monat im ersten Dienstjahr, zwei Monate vom zweiten bis zum neunten Dienstjahr, drei Monate ab dem zehnten Dienstjahr. Die Kündigung erfolgt grundsätzlich auf das Ende eines Monats.",
                    "Während der Probezeit (höchstens drei Monate, Art. 335b OR) beträgt die Kündigungsfrist sieben Tage, sofern nichts anderes vereinbart ist, und die Kündigung kann auf jeden beliebigen Tag erfolgen.",
                    "Ein Einzelarbeitsvertrag, ein Normalarbeitsvertrag oder ein Gesamtarbeitsvertrag können andere Fristen vorsehen, jedoch nach der Probezeit nie weniger als einen Monat (Art. 335c Abs. 2 OR).",
                ]},
                {"heading": "Die missbräuchliche Kündigung", "paragraphs": [
                    "Art. 336 OR zählt Gründe auf, die eine Kündigung missbräuchlich machen: Kündigung wegen einer persönlichen Eigenschaft ohne Bezug zum Arbeitsverhältnis, wegen der Ausübung eines verfassungsmässigen Rechts, einzig um die Entstehung vertraglicher Ansprüche zu verhindern, wegen Zugehörigkeit oder Nichtzugehörigkeit zu einer Gewerkschaft, während der Arbeitnehmervertretung oder als Vergeltung für eine gutgläubig erhobene Beschwerde gegen den Arbeitgeber.",
                    "Eine missbräuchliche Kündigung bleibt dennoch gültig: Das Arbeitsverhältnis endet trotzdem. Die Sanktion ist finanzieller Natur (Art. 336a OR): Das Gericht kann eine Entschädigung von bis zu sechs Monatslöhnen zusprechen. Wer sich darauf berufen will, muss vor Ablauf der Kündigungsfrist schriftlich Einspruch erheben (Art. 336b OR) und innerhalb von 180 Tagen nach Beendigung des Arbeitsverhältnisses klagen.",
                ]},
                {"heading": "Die Sperrfristen gegen Kündigung zur Unzeit", "paragraphs": [
                    "Art. 336c OR verbietet dem Arbeitgeber die Kündigung während bestimmter Zeiträume: während eines obligatorischen schweizerischen Militär- oder Zivilschutzdienstes (sowie der vier Wochen davor und danach, falls der Dienst länger als elf Tage dauert), während einer durch Krankheit oder Unfall verursachten vollen oder teilweisen Arbeitsunfähigkeit ohne eigenes Verschulden (30 Tage im ersten Dienstjahr, 90 Tage vom zweiten bis zum fünften Dienstjahr, 180 Tage ab dem sechsten Dienstjahr) sowie während der Schwangerschaft und der sechzehn Wochen nach der Niederkunft.",
                    "Eine Kündigung, die vor Beginn einer solchen Frist ausgesprochen wurde, deren Frist aber noch nicht abgelaufen ist, wird unterbrochen und läuft erst nach Ende der Sperrfrist weiter (Art. 336c Abs. 2 OR). Dieser Schutz gilt jedoch nicht während der Probezeit, bei fristloser Kündigung aus wichtigem Grund oder bei einer Kündigung durch die Arbeitnehmerin oder den Arbeitnehmer selbst.",
                ]},
                {"heading": "Die fristlose Kündigung aus wichtigem Grund", "paragraphs": [
                    "Art. 337 OR erlaubt es beiden Parteien, das Arbeitsverhältnis jederzeit ohne Kündigungsfrist aus wichtigem Grund aufzulösen: Umstände, die die Fortsetzung des Arbeitsverhältnisses nach Treu und Glauben unzumutbar machen. Das Gesetz zählt keine abschliessende Liste auf; das Gericht beurteilt jeden Fall konkret, unter Berücksichtigung der Schwere der Pflichtverletzung und der Funktion der betroffenen Person.",
                    "Eine fristlose Kündigung ohne wichtigen Grund bleibt gültig, begründet jedoch einen Schadenersatzanspruch der geschädigten Partei, berechnet insbesondere anhand dessen, was sie bei ordentlicher Beendigung erhalten hätte (Art. 337c OR).",
                ]},
            ],
            "faq": [
                {"q": "Kann mein Arbeitgeber mir ohne Angabe eines Grundes kündigen?",
                 "a": "Grundsätzlich ja. Das schweizerische Recht macht die Kündigung nicht von einem gerechtfertigten Grund abhängig. Der Arbeitgeber muss jedoch die gesetzlichen Kündigungsfristen einhalten, darf sich nicht in einer Sperrfrist befinden (Art. 336c OR) und darf keinen der in Art. 336 OR als missbräuchlich aufgeführten Gründe geltend machen."},
                {"q": "Was passiert, wenn meine Kündigung missbräuchlich ist?",
                 "a": "Das Arbeitsverhältnis endet trotzdem mit Ablauf der Kündigungsfrist: Eine missbräuchliche Kündigung wird nicht aufgehoben. Die Arbeitnehmerin oder der Arbeitnehmer kann jedoch eine Entschädigung von bis zu sechs Monatslöhnen verlangen (Art. 336a OR), sofern sie oder er vor Ablauf der Kündigungsfrist schriftlich Einspruch erhoben und innerhalb von 180 Tagen nach Beendigung des Arbeitsverhältnisses geklagt hat."},
                {"q": "Bin ich geschützt, wenn ich zum Zeitpunkt der Kündigung krankgeschrieben bin?",
                 "a": "Ist die Arbeitsunfähigkeit ganz oder teilweise und nicht selbstverschuldet, unterbricht Art. 336c OR die Wirkung der Kündigung für eine von der Dienstdauer abhängige Frist (30, 90 oder 180 Tage). Die Kündigungsfrist beginnt erst nach Ende dieser Sperrfrist wieder zu laufen. Während der Probezeit gilt dieser Schutz nicht."},
                {"q": "Kann die Kündigungsfrist vertraglich verkürzt werden?",
                 "a": "Ein Einzelarbeitsvertrag, ein Normalarbeitsvertrag oder ein Gesamtarbeitsvertrag können die gesetzlichen Fristen anpassen, jedoch nach der Probezeit nie unter einen Monat (Art. 335c Abs. 2 OR). Während der Probezeit selbst kann die gesetzliche Frist von sieben Tagen durch Vereinbarung geändert werden."},
            ],
        },
        "it": {
            "slug": "licenziamento-termini-disdetta-abusiva",
            "title": "Licenziamento in Svizzera: termini e disdetta abusiva",
            "meta": "Termini di disdetta legali, licenziamento abusivo, protezione in caso di malattia o gravidanza, disdetta immediata: quanto previsto dal Codice delle obbligazioni.",
            "sections": [
                {"heading": "La libertà di disdetta e i suoi limiti", "paragraphs": [
                    "Nel diritto svizzero, il contratto di lavoro può in linea di principio essere disdetto da entrambe le parti senza dover invocare un motivo: è il principio della libertà di disdetta. Questa libertà non è tuttavia assoluta. È delimitata da termini di disdetta da rispettare (art. 335c CO), dal divieto di disdetta abusiva (art. 336 CO) e da periodi di protezione durante i quali il datore di lavoro non può disdire il contratto (art. 336c CO).",
                    "Queste regole tutelano il lavoratore senza tuttavia subordinare il licenziamento a un motivo giustificato, come avviene invece in altri paesi.",
                ]},
                {"heading": "I termini di disdetta legali", "paragraphs": [
                    "Salvo accordo scritto contrario, la legge fissa termini minimi che aumentano con l'anzianità di servizio (art. 335c cpv. 1 CO): un mese durante il primo anno di servizio, due mesi dal secondo al nono anno, tre mesi dal decimo anno. La disdetta va data di norma per la fine di un mese.",
                    "Durante il tempo di prova (al massimo tre mesi, art. 335b CO), il termine di disdetta è di sette giorni, salvo accordo contrario, e il contratto può essere disdetto per qualsiasi giorno.",
                    "Un contratto individuale, un contratto normale di lavoro o un contratto collettivo possono prevedere termini diversi, mai tuttavia inferiori a un mese dopo il tempo di prova (art. 335c cpv. 2 CO).",
                ]},
                {"heading": "Il licenziamento abusivo", "paragraphs": [
                    "L'art. 336 CO elenca i motivi che rendono abusiva una disdetta: disdetta data per una caratteristica personale del lavoratore senza relazione con il rapporto di lavoro, per l'esercizio di un diritto costituzionale, al solo scopo di impedire la nascita di pretese derivanti dal contratto, per l'appartenenza o la non appartenenza a un'organizzazione di lavoratori, durante la rappresentanza del personale, o come rappresaglia per un reclamo in buona fede contro il datore di lavoro.",
                    "Il licenziamento abusivo resta valido: il rapporto di lavoro termina comunque. La sanzione è di natura finanziaria (art. 336a CO): il giudice può assegnare un'indennità fino a sei mesi di salario. Per farla valere, la parte che riceve la disdetta deve opporsi per scritto prima della scadenza del termine di disdetta (art. 336b CO) e agire in giudizio entro 180 giorni dalla fine del rapporto di lavoro.",
                ]},
                {"heading": "I periodi di protezione contro la disdetta in tempo inopportuno", "paragraphs": [
                    "L'art. 336c CO vieta al datore di lavoro di disdire il contratto durante determinati periodi: durante un servizio militare o di protezione civile svizzero obbligatorio (e le quattro settimane precedenti e seguenti se dura più di undici giorni), durante un'incapacità lavorativa totale o parziale dovuta a malattia o infortunio non imputabile a colpa del lavoratore (30 giorni nel primo anno di servizio, 90 giorni dal secondo al quinto anno, 180 giorni dal sesto anno), e durante la gravidanza e le sedici settimane successive al parto.",
                    "Una disdetta data prima dell'inizio di uno di questi periodi, il cui termine non sia ancora scaduto, viene sospesa e riprende a decorrere solo dopo la fine del periodo di protezione (art. 336c cpv. 2 CO). Questa protezione non si applica tuttavia durante il tempo di prova, in caso di disdetta immediata per cause gravi, né alla disdetta data dal lavoratore stesso.",
                ]},
                {"heading": "La disdetta immediata per cause gravi", "paragraphs": [
                    "L'art. 337 CO permette a ciascuna parte di disdire il contratto in ogni tempo, senza rispettare un termine di disdetta, per cause gravi: circostanze che rendono insopportabile, secondo le regole della buona fede, la continuazione del rapporto di lavoro. La legge non elenca un catalogo esaustivo; il giudice valuta ogni situazione concretamente, tenendo conto della gravità della mancanza e della funzione del lavoratore.",
                    "Una disdetta immediata data senza cause gravi resta valida, ma dà diritto a un risarcimento per la parte lesa, calcolato in particolare su quanto essa avrebbe percepito se il contratto fosse terminato in modo ordinario (art. 337c CO).",
                ]},
            ],
            "faq": [
                {"q": "Il mio datore di lavoro può licenziarmi senza indicarmi un motivo?",
                 "a": "In linea di principio sì. Il diritto svizzero non subordina il licenziamento a un motivo giustificato. Il datore di lavoro deve tuttavia rispettare i termini di disdetta legali, non trovarsi in un periodo di protezione (art. 336c CO) e non invocare uno dei motivi elencati come abusivi dall'art. 336 CO."},
                {"q": "Cosa succede se il mio licenziamento è abusivo?",
                 "a": "Il rapporto di lavoro termina comunque alla scadenza del termine di disdetta: un licenziamento abusivo non viene annullato. Il lavoratore può tuttavia richiedere un'indennità fino a sei mesi di salario (art. 336a CO), a condizione di essersi opposto per scritto prima della scadenza del termine di disdetta e di aver agito in giudizio entro 180 giorni dalla fine del rapporto di lavoro."},
                {"q": "Sono protetto se sono in malattia nel momento in cui ricevo la disdetta?",
                 "a": "Se l'incapacità lavorativa è totale o parziale e non imputabile a colpa vostra, l'art. 336c CO sospende l'effetto della disdetta per una durata che dipende dalla vostra anzianità di servizio (30, 90 o 180 giorni). Il termine di disdetta riprende a decorrere solo dopo la fine del periodo di protezione. Questa protezione non si applica durante il tempo di prova."},
                {"q": "Il termine di disdetta può essere accorciato per contratto?",
                 "a": "Un contratto individuale, un contratto normale di lavoro o un contratto collettivo possono modificare i termini legali, mai tuttavia sotto un mese dopo il tempo di prova (art. 335c cpv. 2 CO). Durante il tempo di prova stesso, il termine legale di sette giorni può essere modificato per accordo delle parti."},
            ],
        },
        "en": {
            "slug": "termination-notice-periods-abusive-dismissal",
            "title": "Dismissal in Switzerland: notice periods and unfair dismissal",
            "meta": "Statutory notice periods, abusive dismissal, protection during illness or pregnancy, immediate termination: what the Swiss Code of Obligations provides.",
            "sections": [
                {"heading": "Freedom to terminate and its limits", "paragraphs": [
                    "Under Swiss law, an employment contract can in principle be terminated by either party without having to give a reason: this is the principle of freedom of termination. This freedom is not absolute, however. It is bounded by statutory notice periods (art. 335c CO), the prohibition of abusive dismissal (art. 336 CO), and protection periods during which the employer may not terminate the contract at all (art. 336c CO).",
                    "These rules protect the employee without making dismissal conditional on a justified reason, unlike in some other countries.",
                ]},
                {"heading": "Statutory notice periods", "paragraphs": [
                    "Unless otherwise agreed in writing, the law sets minimum notice periods that increase with seniority (art. 335c para. 1 CO): one month during the first year of service, two months from the second to the ninth year, three months from the tenth year onward. Notice must in principle be given for the end of a month.",
                    "During the probationary period (a maximum of three months, art. 335b CO), the notice period is seven days unless otherwise agreed, and notice may be given for any day.",
                    "An individual employment contract, a standard employment contract, or a collective bargaining agreement may set different periods, but never less than one month after the probationary period (art. 335c para. 2 CO).",
                ]},
                {"heading": "Abusive dismissal", "paragraphs": [
                    "Article 336 CO lists grounds that make a dismissal abusive: termination because of a personal characteristic unrelated to the employment relationship, because of the exercise of a constitutional right, solely to prevent claims arising from the contract, because of membership or non-membership of a workers' organisation, while the employee represents the workforce, or in retaliation for a good-faith complaint against the employer.",
                    "An abusive dismissal remains valid: the employment relationship still ends. The sanction is financial (art. 336a CO): the court may award compensation of up to six months' salary. To claim it, the party who received notice must object in writing before the notice period expires (art. 336b CO), then bring a claim within 180 days of the end of the employment relationship.",
                ]},
                {"heading": "Protection periods against dismissal at an inopportune time", "paragraphs": [
                    "Article 336c CO prohibits the employer from terminating the contract during certain periods: during compulsory Swiss military or civil protection service (and the four weeks before and after, if it lasts more than eleven days), during total or partial incapacity for work due to illness or accident not attributable to the employee's own fault (30 days during the first year of service, 90 days from the second to the fifth year, 180 days from the sixth year onward), and during pregnancy and the sixteen weeks following childbirth.",
                    "Notice given before the start of one of these periods, if the notice period has not yet expired, is suspended and resumes running once the protection period ends (art. 336c para. 2 CO). This protection does not apply during the probationary period, in case of termination for cause, or to notice given by the employee.",
                ]},
                {"heading": "Immediate termination for cause", "paragraphs": [
                    "Article 337 CO allows either party to terminate the contract at any time, without observing a notice period, for cause: circumstances that make continuing the employment relationship unreasonable under the rules of good faith. The law does not provide an exhaustive list; the court assesses each situation concretely, taking into account the seriousness of the breach and the employee's role.",
                    "Immediate termination given without cause remains valid, but it entitles the injured party to damages, calculated in particular on what they would have received had the contract ended through ordinary notice (art. 337c CO).",
                ]},
            ],
            "faq": [
                {"q": "Can my employer dismiss me without giving a reason?",
                 "a": "In principle, yes. Swiss law does not make dismissal conditional on a justified reason. The employer must, however, observe the statutory notice periods, must not be within a protection period (art. 336c CO), and must not rely on one of the grounds listed as abusive under art. 336 CO."},
                {"q": "What happens if my dismissal is abusive?",
                 "a": "The employment relationship still ends when the notice period expires: an abusive dismissal is not cancelled. The employee may, however, claim compensation of up to six months' salary (art. 336a CO), provided they objected in writing before the notice period expired and brought a claim within 180 days of the end of the employment relationship."},
                {"q": "Am I protected if I am on sick leave when I receive notice?",
                 "a": "If the incapacity for work is total or partial and not due to your own fault, art. 336c CO suspends the effect of the notice for a period depending on your seniority (30, 90, or 180 days). The notice period only starts running again once the protection period ends. This protection does not apply during the probationary period."},
                {"q": "Can the notice period be shortened by contract?",
                 "a": "An individual employment contract, a standard employment contract, or a collective bargaining agreement may adjust the statutory periods, but never below one month after the probationary period (art. 335c para. 2 CO). During the probationary period itself, the statutory seven-day period may be changed by agreement."},
            ],
        },
    },
    "heures-supplementaires-salaire-vacances": {
        "domaine_id": "droit_travail",
        "published": "2026-07-30",
        "fr": {
            "slug": "heures-supplementaires-salaire-vacances",
            "title": "Heures supplémentaires, salaire et vacances en Suisse",
            "meta": "Rémunération des heures supplémentaires, paiement du salaire, durée minimale des vacances : ce que prévoit le Code des obligations.",
            "sections": [
                {"heading": "Les heures supplémentaires", "paragraphs": [
                    "L'art. 321c CO oblige le travailleur à exécuter des heures supplémentaires dans la mesure où il peut s'en charger et où les règles de la bonne foi permettent de les exiger de lui. Ces heures supplémentaires, qui dépassent l'horaire convenu ou usuel, se distinguent du « travail supplémentaire » au sens de la loi sur le travail, qui vise le dépassement de la durée maximale légale de la semaine de travail et obéit à des règles propres.",
                    "Sauf accord écrit contraire, l'employeur compense les heures supplémentaires par un congé de même durée, avec l'accord du travailleur et dans un délai approprié. À défaut de compensation, il doit les payer avec une majoration de salaire d'au moins 25 % (art. 321c al. 3 CO). Un contrat écrit, un contrat-type de travail ou une convention collective peuvent prévoir une autre solution, y compris l'exclusion de toute majoration pour certaines catégories de personnel.",
                ]},
                {"heading": "Le paiement du salaire", "paragraphs": [
                    "Le salaire est dû dès que le travail convenu a été fourni ; sauf convention ou usage contraire, il est versé à la fin de chaque mois (art. 323 al. 1 CO). L'employeur ne peut pas retenir le salaire à titre de garantie, sauf disposition contraire d'une convention collective, et toute compensation avec une créance envers le travailleur est strictement limitée par la loi lorsque cela toucherait au minimum vital.",
                ]},
                {"heading": "La durée minimale des vacances", "paragraphs": [
                    "L'art. 329a CO garantit au moins quatre semaines de vacances par année de service, et cinq semaines jusqu'à l'âge de 20 ans révolus. Ce minimum est impératif : un contrat ne peut pas prévoir moins, même avec l'accord du travailleur.",
                    "Les vacances ne peuvent pas être remplacées par une prestation en argent tant que les rapports de travail durent (art. 329d al. 2 CO). Une exception existe pour le travail sur appel ou à temps partiel très irrégulier, où une indemnité de vacances peut être intégrée au salaire horaire, à condition d'être clairement mentionnée à part sur chaque décompte de salaire.",
                    "L'employeur fixe la date des vacances en tenant compte des désirs du travailleur dans la mesure compatible avec les intérêts de l'entreprise (art. 329c al. 2 CO), et doit les annoncer suffisamment à l'avance pour permettre au travailleur de s'organiser.",
                ]},
            ],
            "faq": [
                {"q": "Mon employeur peut-il m'imposer des heures supplémentaires ?",
                 "a": "Dans une certaine mesure : l'art. 321c CO oblige le travailleur à en effectuer si cela peut raisonnablement être exigé de lui selon les règles de la bonne foi. Il ne s'agit pas d'une obligation illimitée ; la charge de travail habituelle, la santé et la vie privée du travailleur entrent en ligne de compte."},
                {"q": "Puis-je me faire payer mes vacances non prises au lieu de les prendre ?",
                 "a": "Non, pas tant que le contrat de travail se poursuit : l'art. 329d al. 2 CO interdit de remplacer les vacances par une prestation en argent. Ce n'est qu'à la fin des rapports de travail, si des vacances n'ont pas pu être prises, qu'elles sont indemnisées en argent."},
                {"q": "Comment sont rémunérées les heures supplémentaires ?",
                 "a": "Par un congé de même durée en priorité, ou par un paiement avec une majoration d'au moins 25 % si aucune compensation n'est convenue, sauf accord écrit contraire (art. 321c al. 3 CO)."},
                {"q": "Mon employeur peut-il m'imposer les dates de mes vacances ?",
                 "a": "Oui, c'est en principe à lui de les fixer, mais il doit tenir compte de vos souhaits dans la mesure compatible avec le fonctionnement de l'entreprise (art. 329c al. 2 CO) et vous les annoncer suffisamment à l'avance."},
            ],
        },
        "de": {
            "slug": "ueberstunden-lohn-ferien-schweiz",
            "title": "Überstunden, Lohn und Ferien in der Schweiz",
            "meta": "Vergütung von Überstunden, Lohnzahlung, gesetzliche Mindestferien: was das Obligationenrecht vorsieht.",
            "sections": [
                {"heading": "Überstunden", "paragraphs": [
                    "Art. 321c OR verpflichtet die Arbeitnehmerin oder den Arbeitnehmer, Überstunden zu leisten, soweit sie ihr oder ihm zugemutet werden können und sie nach Treu und Glauben zu leisten sind. Überstunden, die die vereinbarte oder übliche Arbeitszeit überschreiten, unterscheiden sich von der Überzeit im Sinne des Arbeitsgesetzes, welche die Überschreitung der gesetzlichen Höchstarbeitszeit betrifft und eigenen Regeln folgt.",
                    "Ohne schriftliche Vereinbarung gleicht der Arbeitgeber Überstunden mit Freizeit von gleicher Dauer aus, mit Zustimmung der Arbeitnehmerin oder des Arbeitnehmers und innert angemessener Frist. Ohne Ausgleich sind sie mit einem Zuschlag von mindestens 25 Prozent zu entschädigen (Art. 321c Abs. 3 OR). Ein schriftlicher Vertrag, ein Normalarbeitsvertrag oder ein Gesamtarbeitsvertrag können eine andere Regelung vorsehen, einschliesslich des Ausschlusses jeglichen Zuschlags für bestimmte Personalkategorien.",
                ]},
                {"heading": "Die Lohnzahlung", "paragraphs": [
                    "Der Lohn ist geschuldet, sobald die vereinbarte Arbeit geleistet wurde; mangels anderer Vereinbarung oder Übung wird er am Ende jedes Monats ausbezahlt (Art. 323 Abs. 1 OR). Der Arbeitgeber darf den Lohn nicht als Sicherheit zurückbehalten, sofern ein Gesamtarbeitsvertrag nichts anderes vorsieht, und jede Verrechnung mit einer Forderung gegenüber der Arbeitnehmerin oder dem Arbeitnehmer ist gesetzlich stark eingeschränkt, soweit dies das Existenzminimum beeinträchtigen würde.",
                ]},
                {"heading": "Die gesetzliche Mindestdauer der Ferien", "paragraphs": [
                    "Art. 329a OR garantiert mindestens vier Wochen Ferien pro Dienstjahr, und fünf Wochen bis zum vollendeten 20. Altersjahr. Dieses Minimum ist zwingend: ein Vertrag darf auch mit Zustimmung der Arbeitnehmerin oder des Arbeitnehmers nicht weniger vorsehen.",
                    "Ferien dürfen während der Dauer des Arbeitsverhältnisses nicht durch eine Geldleistung ersetzt werden (Art. 329d Abs. 2 OR). Eine Ausnahme besteht bei sehr unregelmässiger Arbeit auf Abruf oder Teilzeitarbeit, wo eine Ferienentschädigung in den Stundenlohn eingerechnet werden kann, sofern sie auf jeder Lohnabrechnung klar gesondert ausgewiesen wird.",
                    "Der Arbeitgeber legt den Ferienzeitpunkt fest und berücksichtigt dabei die Wünsche der Arbeitnehmerin oder des Arbeitnehmers, soweit dies mit den Interessen des Betriebs vereinbar ist (Art. 329c Abs. 2 OR), und muss sie rechtzeitig genug ankündigen, damit sich die Arbeitnehmerin oder der Arbeitnehmer organisieren kann.",
                ]},
            ],
            "faq": [
                {"q": "Kann mein Arbeitgeber mir Überstunden auferlegen?",
                 "a": "In gewissem Umfang ja: Art. 321c OR verpflichtet die Arbeitnehmerin oder den Arbeitnehmer dazu, soweit dies nach Treu und Glauben zumutbar ist. Es handelt sich nicht um eine unbegrenzte Pflicht; die übliche Arbeitsbelastung, die Gesundheit und das Privatleben der Arbeitnehmerin oder des Arbeitnehmers sind zu berücksichtigen."},
                {"q": "Kann ich mir nicht bezogene Ferien auszahlen lassen, statt sie zu beziehen?",
                 "a": "Nein, nicht solange das Arbeitsverhältnis fortbesteht: Art. 329d Abs. 2 OR verbietet den Ersatz von Ferien durch eine Geldleistung. Erst am Ende des Arbeitsverhältnisses werden nicht bezogene Ferien in Geld entschädigt."},
                {"q": "Wie werden Überstunden entschädigt?",
                 "a": "Vorrangig durch Freizeit von gleicher Dauer, oder durch Auszahlung mit einem Zuschlag von mindestens 25 Prozent, wenn kein Ausgleich vereinbart ist, sofern kein schriftlicher Vertrag etwas anderes vorsieht (Art. 321c Abs. 3 OR)."},
                {"q": "Kann mein Arbeitgeber den Zeitpunkt meiner Ferien bestimmen?",
                 "a": "Ja, grundsätzlich obliegt es ihm, diesen festzulegen, doch muss er dabei Ihre Wünsche soweit mit dem Betriebsablauf vereinbar berücksichtigen (Art. 329c Abs. 2 OR) und Ihnen die Ferien rechtzeitig genug ankündigen."},
            ],
        },
        "it": {
            "slug": "straordinari-salario-vacanze-svizzera",
            "title": "Straordinari, salario e vacanze in Svizzera",
            "meta": "Retribuzione delle ore straordinarie, pagamento del salario, durata minima delle vacanze: quanto previsto dal Codice delle obbligazioni.",
            "sections": [
                {"heading": "Le ore di lavoro straordinario", "paragraphs": [
                    "L'art. 321c CO obbliga il lavoratore a prestare lavoro straordinario nella misura in cui può assumerlo e le regole della buona fede permettono di esigerlo da lui. Queste ore, che superano l'orario convenuto o usuale, si distinguono dal lavoro supplementare ai sensi della legge sul lavoro, che riguarda il superamento della durata massima legale della settimana lavorativa e segue regole proprie.",
                    "Salvo accordo scritto contrario, il datore di lavoro compensa le ore straordinarie con un congedo di durata corrispondente, con il consenso del lavoratore ed entro un termine adeguato. In mancanza di compensazione, deve pagarle con un supplemento salariale di almeno il 25% (art. 321c cpv. 3 CO). Un contratto scritto, un contratto normale di lavoro o un contratto collettivo possono prevedere un'altra soluzione, incluso l'esclusione di qualsiasi supplemento per determinate categorie di personale.",
                ]},
                {"heading": "Il pagamento del salario", "paragraphs": [
                    "Il salario è dovuto non appena il lavoro convenuto è stato fornito; salvo diverso accordo o uso, viene versato alla fine di ogni mese (art. 323 cpv. 1 CO). Il datore di lavoro non può trattenere il salario a titolo di garanzia, salvo disposizione contraria di un contratto collettivo, e qualsiasi compensazione con un credito verso il lavoratore è rigorosamente limitata dalla legge quando ciò pregiudicherebbe il minimo vitale.",
                ]},
                {"heading": "La durata minima delle vacanze", "paragraphs": [
                    "L'art. 329a CO garantisce almeno quattro settimane di vacanza per anno di servizio, e cinque settimane fino al compimento del 20esimo anno di età. Questo minimo è imperativo: un contratto non può prevedere di meno, anche con il consenso del lavoratore.",
                    "Le vacanze non possono essere sostituite da una prestazione in denaro finché dura il rapporto di lavoro (art. 329d cpv. 2 CO). Un'eccezione esiste per il lavoro su chiamata o a tempo parziale molto irregolare, dove un'indennità per vacanze può essere integrata nel salario orario, a condizione di essere chiaramente indicata separatamente su ogni conteggio salariale.",
                    "Il datore di lavoro fissa la data delle vacanze tenendo conto dei desideri del lavoratore nella misura compatibile con gli interessi dell'azienda (art. 329c cpv. 2 CO), e deve annunciarle con sufficiente anticipo per permettere al lavoratore di organizzarsi.",
                ]},
            ],
            "faq": [
                {"q": "Il mio datore di lavoro può impormi ore straordinarie?",
                 "a": "In una certa misura sì: l'art. 321c CO obbliga il lavoratore a prestarle se ciò può ragionevolmente essere richiesto secondo le regole della buona fede. Non si tratta di un obbligo illimitato; il carico di lavoro abituale, la salute e la vita privata del lavoratore entrano in considerazione."},
                {"q": "Posso farmi pagare le vacanze non godute invece di prenderle?",
                 "a": "No, non finché il contratto di lavoro prosegue: l'art. 329d cpv. 2 CO vieta di sostituire le vacanze con una prestazione in denaro. Solo alla fine del rapporto di lavoro, se le vacanze non hanno potuto essere godute, vengono indennizzate in denaro."},
                {"q": "Come vengono retribuite le ore straordinarie?",
                 "a": "Prioritariamente con un congedo di durata corrispondente, oppure con un pagamento maggiorato di almeno il 25% se non è convenuta alcuna compensazione, salvo accordo scritto contrario (art. 321c cpv. 3 CO)."},
                {"q": "Il mio datore di lavoro può impormi le date delle mie vacanze?",
                 "a": "Sì, in linea di principio spetta a lui fissarle, ma deve tenere conto dei vostri desideri nella misura compatibile con il funzionamento dell'azienda (art. 329c cpv. 2 CO) e comunicarvele con sufficiente anticipo."},
            ],
        },
        "en": {
            "slug": "overtime-salary-vacation-switzerland",
            "title": "Overtime, salary and vacation in Switzerland",
            "meta": "Overtime compensation, salary payment rules, minimum vacation entitlement: what the Swiss Code of Obligations provides.",
            "sections": [
                {"heading": "Overtime work", "paragraphs": [
                    "Art. 321c CO requires an employee to perform overtime work to the extent it can reasonably be expected of them and good faith requires it. Overtime, which exceeds the agreed or usual working hours, is distinct from excess hours under the Labour Act, which concerns exceeding the statutory maximum weekly working time and follows its own rules.",
                    "Unless otherwise agreed in writing, the employer compensates overtime with time off of equal length, with the employee's consent and within a reasonable period. Failing compensation, it must be paid with a supplement of at least 25% (art. 321c para. 3 CO). A written contract, standard employment contract, or collective agreement may provide for a different arrangement, including excluding any supplement for certain categories of staff.",
                ]},
                {"heading": "Salary payment", "paragraphs": [
                    "Salary is owed as soon as the agreed work has been performed; unless otherwise agreed or customary, it is paid at the end of each month (art. 323 para. 1 CO). The employer may not withhold salary as security, unless a collective agreement provides otherwise, and any offsetting against a claim owed by the employee is strictly limited by law where it would affect the subsistence minimum.",
                ]},
                {"heading": "Minimum vacation entitlement", "paragraphs": [
                    "Art. 329a CO guarantees at least four weeks of vacation per year of service, and five weeks until the age of 20. This minimum is mandatory: a contract may not provide for less, even with the employee's consent.",
                    "Vacation may not be replaced by a cash payment while the employment relationship continues (art. 329d para. 2 CO). An exception exists for on-call work or highly irregular part-time work, where a vacation allowance may be built into the hourly wage, provided it is clearly shown separately on each pay slip.",
                    "The employer sets the vacation dates, taking the employee's wishes into account to the extent compatible with the interests of the business (art. 329c para. 2 CO), and must announce them with enough advance notice for the employee to make arrangements.",
                ]},
            ],
            "faq": [
                {"q": "Can my employer require me to work overtime?",
                 "a": "To some extent, yes: art. 321c CO requires the employee to do so if it can reasonably be expected of them in good faith. It is not an unlimited obligation; the employee's usual workload, health and private life must be taken into account."},
                {"q": "Can I get paid for unused vacation instead of taking it?",
                 "a": "No, not while the employment relationship continues: art. 329d para. 2 CO prohibits replacing vacation with a cash payment. Only at the end of the employment relationship, if vacation could not be taken, is it compensated in cash."},
                {"q": "How is overtime compensated?",
                 "a": "Primarily by time off of equal length, or by payment with a supplement of at least 25% if no compensation is agreed, unless a written contract provides otherwise (art. 321c para. 3 CO)."},
                {"q": "Can my employer set the dates of my vacation?",
                 "a": "Yes, this is in principle up to them, but they must take your wishes into account to the extent compatible with the operation of the business (art. 329c para. 2 CO) and give you enough advance notice."},
            ],
        },
    },
    "autorite-parentale-garde-enfants": {
        "domaine_id": "droit_famille",
        "published": "2026-07-30",
        "fr": {
            "slug": "autorite-parentale-garde-enfants-separation",
            "title": "Autorité parentale et garde des enfants après une séparation",
            "meta": "Autorité parentale conjointe, garde exclusive ou alternée, droit aux relations personnelles : les règles du Code civil suisse après une séparation.",
            "sections": [
                {"heading": "L'autorité parentale conjointe, la règle depuis 2014", "paragraphs": [
                    "Depuis la révision du droit de l'autorité parentale entrée en vigueur en 2014, l'autorité parentale conjointe est le principe : le père et la mère exercent en commun l'autorité parentale, qu'ils soient mariés, séparés ou jamais mariés (art. 296 al. 2 CC). Une attribution exclusive à un seul parent reste possible, mais seulement si le bien de l'enfant l'exige.",
                    "L'autorité parentale porte sur les décisions importantes concernant l'enfant : lieu de vie, formation, questions médicales significatives, religion. Elle ne se confond pas avec la garde, qui concerne l'organisation concrète du quotidien.",
                ]},
                {"heading": "Garde exclusive ou garde alternée", "paragraphs": [
                    "La garde peut être confiée à un seul parent, avec un droit de visite pour l'autre, ou organisée en garde alternée entre les deux domiciles. Le tribunal ou l'autorité de protection de l'enfant tranche selon le bien de l'enfant, en tenant compte de la stabilité, de la disponibilité de chaque parent, de leur capacité à collaborer et, selon son âge, de l'avis de l'enfant lui-même.",
                ]},
                {"heading": "Le droit aux relations personnelles", "paragraphs": [
                    "Le parent qui n'a pas la garde a droit à des relations personnelles appropriées avec l'enfant (art. 273 CC), un droit qui appartient aussi à l'enfant lui-même, pas seulement au parent. Ce droit peut être limité ou suspendu par l'autorité si l'exercice des relations personnelles compromet le développement de l'enfant.",
                ]},
                {"heading": "Le déménagement avec l'enfant", "paragraphs": [
                    "En cas d'autorité parentale conjointe, le parent qui souhaite déménager avec l'enfant doit obtenir l'accord de l'autre parent, ou une décision du juge ou de l'autorité de protection de l'enfant, si le déménagement a un impact significatif sur l'exercice de l'autorité parentale ou sur les relations personnelles (art. 301a CC).",
                ]},
            ],
            "faq": [
                {"q": "L'autorité parentale conjointe signifie-t-elle une garde partagée à parts égales ?",
                 "a": "Non. L'autorité parentale conjointe porte sur le droit de codécision pour les questions importantes ; elle n'implique pas automatiquement une garde alternée. La garde peut rester exclusive à un parent même quand l'autorité parentale est conjointe."},
                {"q": "Puis-je déménager avec mon enfant sans l'accord de l'autre parent ?",
                 "a": "Si le déménagement a un impact significatif sur l'exercice de l'autorité parentale conjointe ou sur les relations personnelles, l'art. 301a CC exige l'accord de l'autre parent titulaire de l'autorité parentale, ou à défaut une décision du juge ou de l'autorité de protection de l'enfant."},
                {"q": "Que se passe-t-il si les parents ne s'entendent pas sur une question importante ?",
                 "a": "En l'absence d'accord, l'un des parents peut saisir l'autorité de protection de l'enfant, qui peut prendre les mesures nécessaires dans l'intérêt de l'enfant, y compris limiter l'autorité parentale conjointe si le désaccord persistant nuit à l'enfant."},
                {"q": "L'enfant peut-il donner son avis sur la garde ?",
                 "a": "Oui, l'enfant capable de discernement est entendu personnellement, en principe par le juge ou par une personne qu'il délègue, et son avis est pris en compte en fonction de son âge et de sa maturité."},
            ],
        },
        "de": {
            "slug": "elterliche-sorge-obhut-kinder-trennung",
            "title": "Elterliche Sorge und Obhut nach einer Trennung",
            "meta": "Gemeinsame elterliche Sorge, alleinige oder alternierende Obhut, persönlicher Verkehr: die Regeln des Zivilgesetzbuchs nach einer Trennung.",
            "sections": [
                {"heading": "Die gemeinsame elterliche Sorge, seit 2014 die Regel", "paragraphs": [
                    "Seit der 2014 in Kraft getretenen Revision des Rechts der elterlichen Sorge ist die gemeinsame elterliche Sorge der Grundsatz: Vater und Mutter üben die elterliche Sorge gemeinsam aus, unabhängig davon, ob sie verheiratet, getrennt oder nie verheiratet waren (Art. 296 Abs. 2 ZGB). Eine alleinige Zuteilung an einen Elternteil bleibt möglich, jedoch nur wenn dies zur Wahrung des Kindeswohls erforderlich ist.",
                    "Die elterliche Sorge betrifft wichtige Entscheidungen über das Kind: Wohnort, Ausbildung, bedeutende medizinische Fragen, Religion. Sie ist nicht mit der Obhut zu verwechseln, welche die konkrete Organisation des Alltags betrifft.",
                ]},
                {"heading": "Alleinige oder alternierende Obhut", "paragraphs": [
                    "Die Obhut kann einem Elternteil allein zugeteilt werden, mit einem Besuchsrecht für den anderen, oder als alternierende Obhut zwischen beiden Wohnsitzen organisiert werden. Das Gericht oder die Kindesschutzbehörde entscheidet nach dem Kindeswohl, unter Berücksichtigung von Stabilität, Verfügbarkeit jedes Elternteils, ihrer Fähigkeit zur Zusammenarbeit und, je nach Alter, der Meinung des Kindes selbst.",
                ]},
                {"heading": "Das Recht auf persönlichen Verkehr", "paragraphs": [
                    "Der Elternteil ohne Obhut hat Anspruch auf angemessenen persönlichen Verkehr mit dem Kind (Art. 273 ZGB), ein Recht, das auch dem Kind selbst zusteht, nicht nur dem Elternteil. Dieses Recht kann eingeschränkt oder ausgesetzt werden, wenn die Ausübung des persönlichen Verkehrs die Entwicklung des Kindes gefährdet.",
                ]},
                {"heading": "Der Umzug mit dem Kind", "paragraphs": [
                    "Bei gemeinsamer elterlicher Sorge muss der Elternteil, der mit dem Kind umziehen möchte, die Zustimmung des anderen Elternteils einholen oder eine Entscheidung des Gerichts oder der Kindesschutzbehörde erwirken, wenn der Umzug erhebliche Auswirkungen auf die Ausübung der elterlichen Sorge oder auf den persönlichen Verkehr hat (Art. 301a ZGB).",
                ]},
            ],
            "faq": [
                {"q": "Bedeutet gemeinsame elterliche Sorge eine hälftig geteilte Obhut?",
                 "a": "Nein. Die gemeinsame elterliche Sorge betrifft das Mitspracherecht bei wichtigen Fragen; sie führt nicht automatisch zu einer alternierenden Obhut. Die Obhut kann auch bei gemeinsamer elterlicher Sorge einem Elternteil allein zustehen."},
                {"q": "Kann ich mit meinem Kind ohne Zustimmung des anderen Elternteils umziehen?",
                 "a": "Wenn der Umzug erhebliche Auswirkungen auf die Ausübung der gemeinsamen elterlichen Sorge oder auf den persönlichen Verkehr hat, verlangt Art. 301a ZGB die Zustimmung des anderen sorgeberechtigten Elternteils, oder andernfalls eine Entscheidung des Gerichts oder der Kindesschutzbehörde."},
                {"q": "Was geschieht, wenn sich die Eltern bei einer wichtigen Frage nicht einigen?",
                 "a": "Bei fehlender Einigung kann ein Elternteil die Kindesschutzbehörde anrufen, welche die im Interesse des Kindes nötigen Massnahmen treffen kann, einschliesslich einer Einschränkung der gemeinsamen elterlichen Sorge, wenn die anhaltende Uneinigkeit dem Kind schadet."},
                {"q": "Kann das Kind seine Meinung zur Obhut äussern?",
                 "a": "Ja, das urteilsfähige Kind wird persönlich angehört, in der Regel durch das Gericht oder eine von ihm beauftragte Person, und seine Meinung wird je nach Alter und Reife berücksichtigt."},
            ],
        },
        "it": {
            "slug": "autorita-parentale-custodia-figli-separazione",
            "title": "Autorità parentale e custodia dei figli dopo la separazione",
            "meta": "Autorità parentale congiunta, custodia esclusiva o alternata, diritto alle relazioni personali: le regole del Codice civile dopo una separazione.",
            "sections": [
                {"heading": "L'autorità parentale congiunta, la regola dal 2014", "paragraphs": [
                    "Dalla revisione del diritto dell'autorità parentale entrata in vigore nel 2014, l'autorità parentale congiunta è il principio: il padre e la madre esercitano in comune l'autorità parentale, siano essi sposati, separati o mai stati sposati (art. 296 cpv. 2 CC). Un'attribuzione esclusiva a un solo genitore resta possibile, ma solo se il bene del figlio lo esige.",
                    "L'autorità parentale riguarda le decisioni importanti concernenti il figlio: luogo di residenza, formazione, questioni mediche significative, religione. Non va confusa con la custodia, che concerne l'organizzazione concreta della quotidianità.",
                ]},
                {"heading": "Custodia esclusiva o custodia alternata", "paragraphs": [
                    "La custodia può essere affidata a un solo genitore, con un diritto di visita per l'altro, oppure organizzata in custodia alternata tra i due domicili. Il tribunale o l'autorità di protezione dei minori decide secondo il bene del figlio, tenendo conto della stabilità, della disponibilità di ciascun genitore, della loro capacità di collaborare e, a seconda dell'età, dell'opinione del figlio stesso.",
                ]},
                {"heading": "Il diritto alle relazioni personali", "paragraphs": [
                    "Il genitore che non ha la custodia ha diritto a relazioni personali adeguate con il figlio (art. 273 CC), un diritto che spetta anche al figlio stesso, non solo al genitore. Questo diritto può essere limitato o sospeso dall'autorità se l'esercizio delle relazioni personali compromette lo sviluppo del figlio.",
                ]},
                {"heading": "Il trasferimento di domicilio con il figlio", "paragraphs": [
                    "In caso di autorità parentale congiunta, il genitore che desidera trasferirsi con il figlio deve ottenere il consenso dell'altro genitore, oppure una decisione del giudice o dell'autorità di protezione dei minori, se il trasferimento ha un impatto significativo sull'esercizio dell'autorità parentale o sulle relazioni personali (art. 301a CC).",
                ]},
            ],
            "faq": [
                {"q": "L'autorità parentale congiunta significa una custodia condivisa in parti uguali?",
                 "a": "No. L'autorità parentale congiunta riguarda il diritto di codecisione per le questioni importanti; non implica automaticamente una custodia alternata. La custodia può restare esclusiva a un genitore anche quando l'autorità parentale è congiunta."},
                {"q": "Posso trasferirmi con mio figlio senza il consenso dell'altro genitore?",
                 "a": "Se il trasferimento ha un impatto significativo sull'esercizio dell'autorità parentale congiunta o sulle relazioni personali, l'art. 301a CC esige il consenso dell'altro genitore titolare dell'autorità parentale, o in mancanza una decisione del giudice o dell'autorità di protezione dei minori."},
                {"q": "Cosa succede se i genitori non si accordano su una questione importante?",
                 "a": "In assenza di accordo, uno dei genitori può adire l'autorità di protezione dei minori, che può adottare le misure necessarie nell'interesse del figlio, incluso limitare l'autorità parentale congiunta se il disaccordo persistente nuoce al figlio."},
                {"q": "Il figlio può esprimere la propria opinione sulla custodia?",
                 "a": "Sì, il figlio capace di discernimento viene sentito personalmente, di regola dal giudice o da una persona da lui incaricata, e la sua opinione è presa in considerazione in funzione della sua età e maturità."},
            ],
        },
        "en": {
            "slug": "parental-authority-custody-children-separation",
            "title": "Parental authority and child custody after separation",
            "meta": "Joint parental authority, sole or alternating custody, right to personal relations: the Civil Code rules that apply after a separation.",
            "sections": [
                {"heading": "Joint parental authority, the rule since 2014", "paragraphs": [
                    "Since the revision of parental authority law that entered into force in 2014, joint parental authority is the principle: the father and mother exercise parental authority together, whether married, separated, or never married (art. 296 para. 2 CC). Sole allocation to one parent remains possible, but only where the child's best interests require it.",
                    "Parental authority covers important decisions about the child: place of residence, education, significant medical questions, religion. It should not be confused with custody, which concerns the day-to-day organisation of the child's life.",
                ]},
                {"heading": "Sole or alternating custody", "paragraphs": [
                    "Custody can be granted to one parent alone, with a right of visitation for the other, or organised as alternating custody between the two households. The court or the child protection authority decides based on the child's best interests, taking into account stability, each parent's availability, their ability to cooperate, and, depending on age, the child's own views.",
                ]},
                {"heading": "The right to personal relations", "paragraphs": [
                    "The parent without custody has a right to appropriate personal relations with the child (art. 273 CC), a right that also belongs to the child, not only to the parent. This right may be restricted or suspended by the authority if exercising personal relations would jeopardise the child's development.",
                ]},
                {"heading": "Moving with the child", "paragraphs": [
                    "Under joint parental authority, a parent who wishes to move with the child must obtain the other parent's consent, or a court or child protection authority decision, if the move significantly affects the exercise of parental authority or personal relations (art. 301a CC).",
                ]},
            ],
            "faq": [
                {"q": "Does joint parental authority mean equally shared custody?",
                 "a": "No. Joint parental authority concerns the right to co-decide important matters; it does not automatically mean alternating custody. Custody can remain sole to one parent even where parental authority is joint."},
                {"q": "Can I move with my child without the other parent's consent?",
                 "a": "If the move significantly affects the exercise of joint parental authority or personal relations, art. 301a CC requires the other parent's consent, or otherwise a court or child protection authority decision."},
                {"q": "What happens if the parents cannot agree on an important matter?",
                 "a": "Failing agreement, either parent may approach the child protection authority, which can take the necessary measures in the child's interest, including limiting joint parental authority if persistent disagreement harms the child."},
                {"q": "Can the child give their opinion on custody?",
                 "a": "Yes, a child capable of judgment is heard personally, usually by the court or a person it appoints, and their opinion is taken into account according to their age and maturity."},
            ],
        },
    },
    "pension-alimentaire-calcul": {
        "domaine_id": "droit_famille",
        "published": "2026-07-30",
        "fr": {
            "slug": "pension-alimentaire-calcul-suisse",
            "title": "Pension alimentaire : comment elle est calculée en Suisse",
            "meta": "Contribution d'entretien de l'enfant, contribution de prise en charge, méthode de calcul du Tribunal fédéral : les bases légales de la pension alimentaire.",
            "sections": [
                {"heading": "L'obligation d'entretien des parents", "paragraphs": [
                    "L'art. 276 CC pose le principe : le père et la mère doivent pourvoir à l'entretien de l'enfant, notamment en argent, en nature ou en soins, proportionnellement à leurs ressources. Cette obligation existe indépendamment de l'état civil des parents et se poursuit après une séparation ou un divorce.",
                ]},
                {"heading": "Ce que couvre la contribution d'entretien", "paragraphs": [
                    "La contribution d'entretien de l'enfant (art. 285 CC) couvre les frais directs liés à son entretien et à son éducation : nourriture, logement, santé, formation. Depuis 2017, elle peut aussi inclure une contribution de prise en charge (art. 285 al. 2 CC), destinée à couvrir les frais de subsistance du parent qui s'occupe personnellement de l'enfant lorsque celui-ci ne peut, de ce fait, exercer une activité lucrative à plein temps.",
                ]},
                {"heading": "La méthode de calcul", "paragraphs": [
                    "Le Tribunal fédéral a uniformisé en 2020 la méthode de calcul des contributions d'entretien à l'échelle du pays : une méthode en deux étapes qui détermine d'abord le minimum vital du droit des poursuites de chaque partie, puis répartit l'excédent disponible entre les membres de la famille selon des règles précises. Cette méthode remplace les approches cantonales auparavant divergentes et vise une plus grande prévisibilité.",
                ]},
                {"heading": "Révision et non-paiement", "paragraphs": [
                    "Une contribution d'entretien fixée par jugement ou convention peut être révisée si la situation financière ou personnelle de l'une des parties change de manière importante et durable. En cas de non-paiement, le parent créancier peut demander l'aide au recouvrement auprès du service cantonal compétent, et engager une poursuite pour dettes.",
                ]},
            ],
            "faq": [
                {"q": "Jusqu'à quel âge la pension alimentaire est-elle due ?",
                 "a": "En principe jusqu'à la majorité de l'enfant, et au-delà si l'enfant n'a pas encore de formation appropriée achevée à ce moment-là, dans les limites de ce qui peut raisonnablement être exigé des parents (art. 277 CC)."},
                {"q": "La pension alimentaire peut-elle être révisée ?",
                 "a": "Oui, si la situation financière ou personnelle de l'un des parents ou de l'enfant change de manière importante et durable, l'un ou l'autre parent peut demander au tribunal d'adapter le montant fixé."},
                {"q": "Que faire si l'autre parent ne paie pas la pension ?",
                 "a": "Vous pouvez demander l'aide au recouvrement auprès du service cantonal compétent, qui peut intervenir auprès du débiteur, et engager une poursuite pour dettes en cas d'échec des démarches amiables."},
                {"q": "Qu'est-ce que la contribution de prise en charge ?",
                 "a": "Introduite en 2017, elle couvre les frais de subsistance du parent qui s'occupe personnellement de l'enfant lorsque cette prise en charge l'empêche de travailler à plein temps (art. 285 al. 2 CC), en plus des frais directs de l'enfant."},
            ],
        },
        "de": {
            "slug": "unterhaltsbeitrag-berechnung-schweiz",
            "title": "Unterhaltsbeitrag: wie er in der Schweiz berechnet wird",
            "meta": "Kindesunterhalt, Betreuungsunterhalt, Berechnungsmethode des Bundesgerichts: die gesetzlichen Grundlagen des Unterhaltsbeitrags.",
            "sections": [
                {"heading": "Die Unterhaltspflicht der Eltern", "paragraphs": [
                    "Art. 276 ZGB legt den Grundsatz fest: Vater und Mutter haben, ein jeder nach seinen Kräften, für den Unterhalt des Kindes aufzukommen, namentlich durch Geld, Pflege und Erziehung. Diese Pflicht besteht unabhängig vom Zivilstand der Eltern und dauert nach einer Trennung oder Scheidung fort.",
                ]},
                {"heading": "Was der Unterhaltsbeitrag abdeckt", "paragraphs": [
                    "Der Kindesunterhaltsbeitrag (Art. 285 ZGB) deckt die direkten Kosten für Unterhalt und Erziehung des Kindes: Ernährung, Wohnen, Gesundheit, Ausbildung. Seit 2017 kann er auch einen Betreuungsunterhalt umfassen (Art. 285 Abs. 2 ZGB), der die Lebenshaltungskosten des Elternteils deckt, der das Kind persönlich betreut und deshalb nicht vollzeitlich erwerbstätig sein kann.",
                ]},
                {"heading": "Die Berechnungsmethode", "paragraphs": [
                    "Das Bundesgericht hat 2020 die Berechnungsmethode für Unterhaltsbeiträge schweizweit vereinheitlicht: eine zweistufige Methode, die zunächst das betreibungsrechtliche Existenzminimum jeder Partei ermittelt und anschliessend den verfügbaren Überschuss nach präzisen Regeln unter den Familienmitgliedern verteilt. Diese Methode ersetzt die zuvor abweichenden kantonalen Ansätze und bezweckt eine grössere Vorhersehbarkeit.",
                ]},
                {"heading": "Anpassung und Nichtzahlung", "paragraphs": [
                    "Ein durch Urteil oder Vereinbarung festgelegter Unterhaltsbeitrag kann angepasst werden, wenn sich die finanziellen oder persönlichen Verhältnisse einer Partei erheblich und dauerhaft ändern. Bei Nichtzahlung kann der berechtigte Elternteil Inkassohilfe bei der zuständigen kantonalen Stelle beantragen und eine Betreibung einleiten.",
                ]},
            ],
            "faq": [
                {"q": "Bis zu welchem Alter ist der Unterhaltsbeitrag geschuldet?",
                 "a": "Grundsätzlich bis zur Volljährigkeit des Kindes, und darüber hinaus, falls das Kind zu diesem Zeitpunkt noch keine angemessene Ausbildung abgeschlossen hat, im Rahmen dessen, was den Eltern zugemutet werden kann (Art. 277 ZGB)."},
                {"q": "Kann der Unterhaltsbeitrag angepasst werden?",
                 "a": "Ja, wenn sich die finanziellen oder persönlichen Verhältnisse eines Elternteils oder des Kindes erheblich und dauerhaft ändern, kann jeder Elternteil beim Gericht eine Anpassung des festgelegten Betrags beantragen."},
                {"q": "Was tun, wenn der andere Elternteil den Unterhaltsbeitrag nicht zahlt?",
                 "a": "Sie können Inkassohilfe bei der zuständigen kantonalen Stelle beantragen, die beim Schuldner vorstellig werden kann, und bei Scheitern der gütlichen Bemühungen eine Betreibung einleiten."},
                {"q": "Was ist der Betreuungsunterhalt?",
                 "a": "Der 2017 eingeführte Betreuungsunterhalt deckt die Lebenshaltungskosten des Elternteils, der das Kind persönlich betreut, wenn diese Betreuung ihn an einer Vollzeiterwerbstätigkeit hindert (Art. 285 Abs. 2 ZGB), zusätzlich zu den direkten Kosten des Kindes."},
            ],
        },
        "it": {
            "slug": "contributo-mantenimento-calcolo-svizzera",
            "title": "Contributo di mantenimento: come si calcola in Svizzera",
            "meta": "Mantenimento del figlio, contributo di presa a carico, metodo di calcolo del Tribunale federale: le basi legali del contributo di mantenimento.",
            "sections": [
                {"heading": "L'obbligo di mantenimento dei genitori", "paragraphs": [
                    "L'art. 276 CC pone il principio: il padre e la madre devono provvedere al mantenimento del figlio, segnatamente con prestazioni pecuniarie, cure e educazione, proporzionalmente alle loro risorse. Questo obbligo esiste indipendentemente dallo stato civile dei genitori e prosegue dopo una separazione o un divorzio.",
                ]},
                {"heading": "Cosa copre il contributo di mantenimento", "paragraphs": [
                    "Il contributo di mantenimento del figlio (art. 285 CC) copre le spese dirette legate al suo mantenimento e alla sua educazione: alimentazione, alloggio, salute, formazione. Dal 2017 può includere anche un contributo di presa a carico (art. 285 cpv. 2 CC), destinato a coprire le spese di sostentamento del genitore che si occupa personalmente del figlio quando ciò gli impedisce di esercitare un'attività lucrativa a tempo pieno.",
                ]},
                {"heading": "Il metodo di calcolo", "paragraphs": [
                    "Nel 2020 il Tribunale federale ha uniformato a livello nazionale il metodo di calcolo dei contributi di mantenimento: un metodo in due tappe che determina dapprima il minimo vitale del diritto esecutivo di ciascuna parte, poi ripartisce l'eccedenza disponibile tra i membri della famiglia secondo regole precise. Questo metodo sostituisce gli approcci cantonali in precedenza divergenti e mira a una maggiore prevedibilità.",
                ]},
                {"heading": "Revisione e mancato pagamento", "paragraphs": [
                    "Un contributo di mantenimento fissato per sentenza o convenzione può essere rivisto se la situazione finanziaria o personale di una delle parti cambia in modo importante e duraturo. In caso di mancato pagamento, il genitore creditore può chiedere l'aiuto all'incasso presso il servizio cantonale competente e avviare un'esecuzione.",
                ]},
            ],
            "faq": [
                {"q": "Fino a che età è dovuto il contributo di mantenimento?",
                 "a": "In linea di principio fino alla maggiore età del figlio, e oltre se il figlio non ha ancora concluso una formazione appropriata a quel momento, nei limiti di quanto può ragionevolmente essere richiesto ai genitori (art. 277 CC)."},
                {"q": "Il contributo di mantenimento può essere rivisto?",
                 "a": "Sì, se la situazione finanziaria o personale di un genitore o del figlio cambia in modo importante e duraturo, l'uno o l'altro genitore può chiedere al tribunale di adeguare l'importo fissato."},
                {"q": "Cosa fare se l'altro genitore non paga il contributo?",
                 "a": "Potete chiedere l'aiuto all'incasso presso il servizio cantonale competente, che può intervenire presso il debitore, e avviare un'esecuzione in caso di fallimento delle pratiche amichevoli."},
                {"q": "Cos'è il contributo di presa a carico?",
                 "a": "Introdotto nel 2017, copre le spese di sostentamento del genitore che si occupa personalmente del figlio quando questa presa a carico gli impedisce di lavorare a tempo pieno (art. 285 cpv. 2 CC), in aggiunta alle spese dirette del figlio."},
            ],
        },
        "en": {
            "slug": "child-maintenance-calculation-switzerland",
            "title": "Child maintenance: how it is calculated in Switzerland",
            "meta": "Child maintenance, care contribution, the Federal Supreme Court's calculation method: the legal basis for maintenance payments.",
            "sections": [
                {"heading": "The parents' duty of maintenance", "paragraphs": [
                    "Art. 276 CC sets out the principle: the father and mother must provide for the maintenance of the child, in particular through money, care and upbringing, in proportion to their means. This duty exists regardless of the parents' marital status and continues after a separation or divorce.",
                ]},
                {"heading": "What the maintenance contribution covers", "paragraphs": [
                    "The child maintenance contribution (art. 285 CC) covers the direct costs of the child's upkeep and education: food, housing, health, education. Since 2017 it may also include a care contribution (art. 285 para. 2 CC), intended to cover the subsistence costs of the parent who personally cares for the child when this prevents them from working full time.",
                ]},
                {"heading": "The calculation method", "paragraphs": [
                    "In 2020 the Federal Supreme Court standardised the method for calculating maintenance contributions nationwide: a two-step method that first determines each party's subsistence minimum under debt enforcement law, then distributes the available surplus among family members according to precise rules. This method replaces the previously divergent cantonal approaches and aims for greater predictability.",
                ]},
                {"heading": "Revision and non-payment", "paragraphs": [
                    "A maintenance contribution set by judgment or agreement can be revised if a party's financial or personal circumstances change significantly and lastingly. In the event of non-payment, the entitled parent can request collection assistance from the competent cantonal service and initiate debt collection proceedings.",
                ]},
            ],
            "faq": [
                {"q": "Until what age is child maintenance owed?",
                 "a": "In principle until the child reaches the age of majority, and beyond if the child has not yet completed an appropriate education at that point, within the limits of what can reasonably be required of the parents (art. 277 CC)."},
                {"q": "Can the maintenance contribution be revised?",
                 "a": "Yes, if a parent's or the child's financial or personal circumstances change significantly and lastingly, either parent can ask the court to adjust the amount set."},
                {"q": "What can I do if the other parent does not pay maintenance?",
                 "a": "You can request collection assistance from the competent cantonal service, which can approach the debtor, and initiate debt collection proceedings if amicable efforts fail."},
                {"q": "What is the care contribution?",
                 "a": "Introduced in 2017, it covers the subsistence costs of the parent who personally cares for the child when this prevents them from working full time (art. 285 para. 2 CC), in addition to the child's direct costs."},
            ],
        },
    },
    "divorce-procedure-delais": {
        "domaine_id": "droit_divorce",
        "published": "2026-07-30",
        "fr": {
            "slug": "divorce-suisse-procedure-delais",
            "title": "Divorce en Suisse : procédure et délais",
            "meta": "Divorce sur requête commune, divorce après deux ans de séparation, divorce pour rupture du lien conjugal : les voies prévues par le Code civil.",
            "sections": [
                {"heading": "Le divorce sur requête commune", "paragraphs": [
                    "Lorsque les deux époux sont d'accord de divorcer, ils peuvent déposer une requête commune (art. 111-112 CC). Si l'accord porte aussi sur les effets du divorce (entretien, biens, prévoyance, enfants), la procédure est simplifiée. À défaut d'accord complet, chaque époux peut faire valoir ses conclusions sur les points litigieux, et le tribunal statue sur ces points tout en prononçant le divorce.",
                ]},
                {"heading": "Le divorce après suspension de la vie commune", "paragraphs": [
                    "Si un seul des époux souhaite divorcer, l'art. 114 CC lui permet de demander le divorce après une séparation de deux ans. Ce délai court dès la cessation de la vie commune, qu'elle résulte d'un départ physique ou d'une séparation au sein du même logement dans certaines circonstances reconnues par la jurisprudence.",
                ]},
                {"heading": "Le divorce pour rupture du lien conjugal", "paragraphs": [
                    "À titre exceptionnel, l'art. 115 CC permet de demander le divorce avant l'écoulement du délai de deux ans, si la continuation du mariage est insupportable pour des motifs sérieux qui ne sont pas imputables au demandeur, par exemple des violences conjugales graves.",
                ]},
                {"heading": "Le déroulement de la procédure", "paragraphs": [
                    "La procédure se déroule devant le tribunal civil du domicile de l'un des époux. Elle règle, en même temps que le prononcé du divorce, les effets accessoires : entretien entre époux, partage des biens, partage de la prévoyance professionnelle, et le sort des enfants (autorité parentale, garde, contribution d'entretien).",
                ]},
            ],
            "faq": [
                {"q": "Peut-on divorcer sans l'accord de son conjoint ?",
                 "a": "Oui, après une séparation de deux ans (art. 114 CC), un époux peut demander le divorce même sans l'accord de l'autre. Avant ce délai, ce n'est possible qu'à titre exceptionnel pour rupture du lien conjugal (art. 115 CC)."},
                {"q": "Faut-il obligatoirement passer par un avocat pour divorcer ?",
                 "a": "Non, la représentation par un avocat n'est pas obligatoire en matière civile en Suisse. Elle est toutefois vivement recommandée dès que des questions patrimoniales ou parentales complexes sont en jeu."},
                {"q": "Combien de temps dure une procédure de divorce en Suisse ?",
                 "a": "Cela dépend fortement du degré d'accord entre les époux et de la charge du tribunal saisi : un divorce sur requête commune avec accord complet peut aboutir en quelques mois, tandis qu'une procédure contentieuse peut durer plusieurs années."},
                {"q": "Qu'est-ce que le divorce par consentement mutuel ?",
                 "a": "C'est le nom courant du divorce sur requête commune avec accord complet sur les effets du divorce (art. 111 CC) : les époux soumettent au tribunal une convention réglant tous les points, que le tribunal ratifie s'il la juge conforme au bien des parties et des enfants."},
            ],
        },
        "de": {
            "slug": "scheidung-schweiz-verfahren-fristen",
            "title": "Scheidung in der Schweiz: Verfahren und Fristen",
            "meta": "Scheidung auf gemeinsames Begehren, Scheidung nach zweijähriger Trennung, Zerrüttung: die im Zivilgesetzbuch vorgesehenen Wege.",
            "sections": [
                {"heading": "Die Scheidung auf gemeinsames Begehren", "paragraphs": [
                    "Sind sich beide Ehegatten über die Scheidung einig, können sie ein gemeinsames Begehren einreichen (Art. 111-112 ZGB). Besteht Einigkeit auch über die Scheidungsfolgen (Unterhalt, Vermögen, Vorsorge, Kinder), wird das Verfahren vereinfacht. Fehlt eine vollständige Einigung, kann jeder Ehegatte zu den strittigen Punkten Anträge stellen, worüber das Gericht zusammen mit der Scheidung entscheidet.",
                ]},
                {"heading": "Die Scheidung nach Aufhebung des gemeinsamen Haushalts", "paragraphs": [
                    "Wünscht nur ein Ehegatte die Scheidung, erlaubt ihm Art. 114 ZGB, die Scheidung nach einer zweijährigen Trennung zu verlangen. Diese Frist beginnt mit der Aufhebung der Haushaltsgemeinschaft, sei es durch einen physischen Auszug oder durch eine von der Rechtsprechung anerkannte Trennung innerhalb derselben Wohnung unter bestimmten Umständen.",
                ]},
                {"heading": "Die Scheidung wegen Unzumutbarkeit", "paragraphs": [
                    "Ausnahmsweise erlaubt Art. 115 ZGB, die Scheidung vor Ablauf der zweijährigen Frist zu verlangen, wenn die Fortsetzung der Ehe aus schwerwiegenden Gründen, die nicht dem Kläger zuzurechnen sind, unzumutbar ist, etwa bei schweren ehelichen Gewalttaten.",
                ]},
                {"heading": "Der Ablauf des Verfahrens", "paragraphs": [
                    "Das Verfahren findet vor dem Zivilgericht am Wohnsitz eines der Ehegatten statt. Es regelt zusammen mit dem Scheidungsurteil die Nebenfolgen: Unterhalt zwischen den Ehegatten, güterrechtliche Auseinandersetzung, Teilung der beruflichen Vorsorge, sowie das Schicksal der Kinder (elterliche Sorge, Obhut, Unterhaltsbeitrag).",
                ]},
            ],
            "faq": [
                {"q": "Kann man ohne Zustimmung des Ehepartners geschieden werden?",
                 "a": "Ja, nach einer zweijährigen Trennung (Art. 114 ZGB) kann ein Ehegatte die Scheidung auch ohne Zustimmung des anderen verlangen. Vor Ablauf dieser Frist ist dies nur ausnahmsweise wegen Unzumutbarkeit möglich (Art. 115 ZGB)."},
                {"q": "Muss man zwingend einen Anwalt für die Scheidung beiziehen?",
                 "a": "Nein, die Vertretung durch einen Anwalt ist im Zivilrecht in der Schweiz nicht obligatorisch. Sie wird jedoch dringend empfohlen, sobald komplexe vermögensrechtliche oder elterliche Fragen auf dem Spiel stehen."},
                {"q": "Wie lange dauert ein Scheidungsverfahren in der Schweiz?",
                 "a": "Dies hängt stark vom Grad der Einigkeit zwischen den Ehegatten und von der Belastung des angerufenen Gerichts ab: eine Scheidung auf gemeinsames Begehren mit vollständiger Einigung kann in wenigen Monaten abgeschlossen sein, während ein strittiges Verfahren mehrere Jahre dauern kann."},
                {"q": "Was ist die Scheidung im gegenseitigen Einvernehmen?",
                 "a": "So wird die Scheidung auf gemeinsames Begehren mit vollständiger Einigung über die Scheidungsfolgen bezeichnet (Art. 111 ZGB): die Ehegatten legen dem Gericht eine Vereinbarung vor, welche sämtliche Punkte regelt und die das Gericht genehmigt, sofern sie dem Wohl der Parteien und der Kinder entspricht."},
            ],
        },
        "it": {
            "slug": "divorzio-svizzera-procedura-termini",
            "title": "Divorzio in Svizzera: procedura e termini",
            "meta": "Divorzio su richiesta comune, divorzio dopo due anni di separazione, rottura del vincolo coniugale: le vie previste dal Codice civile.",
            "sections": [
                {"heading": "Il divorzio su richiesta comune", "paragraphs": [
                    "Quando entrambi i coniugi sono d'accordo di divorziare, possono presentare una richiesta comune (art. 111-112 CC). Se l'accordo riguarda anche gli effetti del divorzio (mantenimento, beni, previdenza, figli), la procedura è semplificata. In mancanza di un accordo completo, ciascun coniuge può far valere le proprie conclusioni sui punti controversi, e il tribunale decide su tali punti pronunciando al contempo il divorzio.",
                ]},
                {"heading": "Il divorzio dopo la sospensione della vita comune", "paragraphs": [
                    "Se solo uno dei coniugi desidera divorziare, l'art. 114 CC gli permette di chiedere il divorzio dopo una separazione di due anni. Questo termine decorre dalla cessazione della vita comune, che risulti da un allontanamento fisico o da una separazione all'interno della stessa abitazione riconosciuta dalla giurisprudenza in determinate circostanze.",
                ]},
                {"heading": "Il divorzio per rottura del vincolo coniugale", "paragraphs": [
                    "A titolo eccezionale, l'art. 115 CC permette di chiedere il divorzio prima dello scadere del termine di due anni, se la continuazione del matrimonio è intollerabile per motivi gravi non imputabili al richiedente, per esempio violenze coniugali gravi.",
                ]},
                {"heading": "Lo svolgimento della procedura", "paragraphs": [
                    "La procedura si svolge davanti al tribunale civile del domicilio di uno dei coniugi. Essa regola, insieme alla pronuncia del divorzio, gli effetti accessori: mantenimento tra coniugi, liquidazione del regime dei beni, divisione della previdenza professionale e la sorte dei figli (autorità parentale, custodia, contributo di mantenimento).",
                ]},
            ],
            "faq": [
                {"q": "Si può divorziare senza il consenso del coniuge?",
                 "a": "Sì, dopo una separazione di due anni (art. 114 CC), un coniuge può chiedere il divorzio anche senza il consenso dell'altro. Prima di questo termine, ciò è possibile solo eccezionalmente per rottura del vincolo coniugale (art. 115 CC)."},
                {"q": "Bisogna obbligatoriamente rivolgersi a un avvocato per divorziare?",
                 "a": "No, la rappresentanza da parte di un avvocato non è obbligatoria in materia civile in Svizzera. È tuttavia vivamente raccomandata non appena sono in gioco questioni patrimoniali o genitoriali complesse."},
                {"q": "Quanto dura una procedura di divorzio in Svizzera?",
                 "a": "Ciò dipende fortemente dal grado di accordo tra i coniugi e dal carico di lavoro del tribunale adito: un divorzio su richiesta comune con accordo completo può concludersi in pochi mesi, mentre una procedura contenziosa può durare diversi anni."},
                {"q": "Cos'è il divorzio consensuale?",
                 "a": "È il nome comune del divorzio su richiesta comune con accordo completo sugli effetti del divorzio (art. 111 CC): i coniugi sottopongono al tribunale una convenzione che regola tutti i punti, che il tribunale omologa se la ritiene conforme al bene delle parti e dei figli."},
            ],
        },
        "en": {
            "slug": "divorce-switzerland-procedure-deadlines",
            "title": "Divorce in Switzerland: procedure and deadlines",
            "meta": "Divorce by joint request, divorce after two years of separation, irretrievable breakdown: the paths provided by the Civil Code.",
            "sections": [
                {"heading": "Divorce by joint request", "paragraphs": [
                    "When both spouses agree to divorce, they can file a joint request (art. 111-112 CC). If they also agree on the effects of the divorce (maintenance, property, pension, children), the procedure is simplified. Absent full agreement, each spouse can put forward their own conclusions on the disputed points, and the court rules on those points while pronouncing the divorce.",
                ]},
                {"heading": "Divorce after suspension of the joint household", "paragraphs": [
                    "If only one spouse wishes to divorce, art. 114 CC allows them to request divorce after a two-year separation. This period runs from the cessation of the joint household, whether through physical departure or, under certain circumstances recognised by case law, separation within the same home.",
                ]},
                {"heading": "Divorce due to irretrievable breakdown", "paragraphs": [
                    "Exceptionally, art. 115 CC allows a request for divorce before the two-year period has elapsed, if continuing the marriage would be unbearable for serious reasons not attributable to the applicant, for example serious domestic violence.",
                ]},
                {"heading": "How the procedure unfolds", "paragraphs": [
                    "The procedure takes place before the civil court of either spouse's domicile. Alongside the divorce judgment, it settles the ancillary effects: maintenance between spouses, division of marital property, division of occupational pension assets, and arrangements for the children (parental authority, custody, maintenance contribution).",
                ]},
            ],
            "faq": [
                {"q": "Can you divorce without your spouse's consent?",
                 "a": "Yes, after a two-year separation (art. 114 CC), a spouse can request divorce even without the other's consent. Before that period elapses, this is only possible exceptionally due to irretrievable breakdown (art. 115 CC)."},
                {"q": "Is a lawyer mandatory to get divorced?",
                 "a": "No, representation by a lawyer is not mandatory in civil matters in Switzerland. It is, however, strongly recommended as soon as complex financial or parental questions are at stake."},
                {"q": "How long does a divorce procedure take in Switzerland?",
                 "a": "This depends heavily on how much the spouses agree and on the workload of the court seized: a joint-request divorce with full agreement can conclude within a few months, while a contested procedure can take several years."},
                {"q": "What is divorce by mutual consent?",
                 "a": "This is the common name for divorce by joint request with full agreement on the effects of the divorce (art. 111 CC): the spouses submit an agreement to the court covering all points, which the court approves if it finds it consistent with the interests of the parties and any children."},
            ],
        },
    },
    "partage-deuxieme-pilier-divorce": {
        "domaine_id": "droit_divorce",
        "published": "2026-07-30",
        "fr": {
            "slug": "partage-2e-pilier-divorce",
            "title": "Partage du 2e pilier en cas de divorce",
            "meta": "Partage par moitié de la prévoyance professionnelle, cas particuliers, dérogations possibles : ce que prévoit le Code civil en cas de divorce.",
            "sections": [
                {"heading": "Le principe du partage par moitié", "paragraphs": [
                    "Les avoirs de prévoyance professionnelle (2e pilier) accumulés par les deux époux pendant le mariage, jusqu'à l'introduction de la procédure de divorce, sont en principe partagés par moitié entre eux (art. 122 CC). Ce partage vise à compenser le désavantage de prévoyance que subit souvent l'époux qui a réduit ou cessé son activité lucrative pour se consacrer au ménage ou aux enfants.",
                ]},
                {"heading": "Quand l'un des époux est déjà retraité ou invalide", "paragraphs": [
                    "Si l'un des époux touche déjà une rente de vieillesse ou une rente d'invalidité au moment du divorce, un partage classique de l'avoir de prévoyance n'est plus possible : la loi prévoit alors un partage de la rente elle-même, sous forme d'une rente viagère versée à l'époux créancier (art. 124a CC).",
                ]},
                {"heading": "Les dérogations au partage par moitié", "paragraphs": [
                    "Le tribunal peut s'écarter du partage par moitié pour de justes motifs, notamment si ce partage est manifestement inéquitable au regard des besoins de prévoyance respectifs des époux, par exemple en raison d'une grande différence d'âge ou de la liquidation du régime matrimonial (art. 124b CC).",
                ]},
                {"heading": "L'exécution du partage", "paragraphs": [
                    "Le tribunal transmet le dossier aux institutions de prévoyance concernées, qui procèdent au transfert des montants. Si l'un des époux n'est affilié à aucune institution de prévoyance ou si le transfert n'est pas possible directement, la Fondation institution supplétive LPP intervient pour recevoir et gérer les montants transférés.",
                ]},
            ],
            "faq": [
                {"q": "Le partage du 2e pilier est-il automatique en cas de divorce ?",
                 "a": "Oui, sauf accord contraire des époux validé par le tribunal ou situation particulière (retraite, invalidité) : le partage par moitié de l'avoir accumulé pendant le mariage est le principe légal (art. 122 CC)."},
                {"q": "Que se passe-t-il si l'un des époux est déjà à la retraite ?",
                 "a": "Un partage classique de l'avoir n'est plus possible ; la loi prévoit alors un partage de la rente de vieillesse ou d'invalidité elle-même, versée à l'époux créancier sous forme de rente viagère (art. 124a CC)."},
                {"q": "Peut-on renoncer au partage du 2e pilier ?",
                 "a": "Les époux peuvent convenir d'un partage différent ou y renoncer partiellement dans une convention sur les effets du divorce, à condition qu'une prévoyance vieillesse et invalidité adéquate reste assurée pour chacun, ce que le tribunal vérifie avant d'homologuer la convention."},
                {"q": "Le 3e pilier est-il aussi partagé en cas de divorce ?",
                 "a": "Le 3e pilier lié (3a) et le 3e pilier libre (3b) ne relèvent pas du partage de la prévoyance professionnelle de l'art. 122 CC ; ils sont en principe traités dans le cadre de la liquidation du régime matrimonial, selon le régime matrimonial applicable."},
            ],
        },
        "de": {
            "slug": "teilung-zweite-saeule-scheidung",
            "title": "Teilung der beruflichen Vorsorge bei Scheidung",
            "meta": "Hälftige Teilung der beruflichen Vorsorge, Sonderfälle, mögliche Abweichungen: was das Zivilgesetzbuch bei einer Scheidung vorsieht.",
            "sections": [
                {"heading": "Der Grundsatz der hälftigen Teilung", "paragraphs": [
                    "Die während der Ehe bis zur Einleitung des Scheidungsverfahrens von beiden Ehegatten angesparten Guthaben der beruflichen Vorsorge (2. Säule) werden grundsätzlich hälftig zwischen ihnen geteilt (Art. 122 ZGB). Diese Teilung soll den Vorsorgenachteil ausgleichen, den häufig der Ehegatte erleidet, der seine Erwerbstätigkeit zugunsten des Haushalts oder der Kinder reduziert oder aufgegeben hat.",
                ]},
                {"heading": "Wenn ein Ehegatte bereits eine Rente bezieht", "paragraphs": [
                    "Bezieht ein Ehegatte im Zeitpunkt der Scheidung bereits eine Altersrente oder eine Invalidenrente, ist eine klassische Teilung des Vorsorgeguthabens nicht mehr möglich: das Gesetz sieht dann eine Teilung der Rente selbst vor, in Form einer lebenslänglichen Rente zugunsten des berechtigten Ehegatten (Art. 124a ZGB).",
                ]},
                {"heading": "Abweichungen von der hälftigen Teilung", "paragraphs": [
                    "Das Gericht kann aus wichtigen Gründen von der hälftigen Teilung abweichen, namentlich wenn diese Teilung angesichts der jeweiligen Vorsorgebedürfnisse der Ehegatten offensichtlich unbillig wäre, etwa bei einem grossen Altersunterschied oder infolge der güterrechtlichen Auseinandersetzung (Art. 124b ZGB).",
                ]},
                {"heading": "Der Vollzug der Teilung", "paragraphs": [
                    "Das Gericht übermittelt das Dossier den betroffenen Vorsorgeeinrichtungen, welche die Überweisung der Beträge vornehmen. Ist ein Ehegatte keiner Vorsorgeeinrichtung angeschlossen oder ist die direkte Überweisung nicht möglich, tritt die Stiftung Auffangeinrichtung BVG ein, um die überwiesenen Beträge entgegenzunehmen und zu verwalten.",
                ]},
            ],
            "faq": [
                {"q": "Ist die Teilung der 2. Säule bei Scheidung automatisch?",
                 "a": "Ja, sofern keine gegenteilige, vom Gericht genehmigte Vereinbarung der Ehegatten oder ein Sonderfall (Ruhestand, Invalidität) vorliegt: die hälftige Teilung des während der Ehe angesparten Guthabens ist der gesetzliche Grundsatz (Art. 122 ZGB)."},
                {"q": "Was geschieht, wenn ein Ehegatte bereits im Ruhestand ist?",
                 "a": "Eine klassische Teilung des Guthabens ist nicht mehr möglich; das Gesetz sieht dann eine Teilung der Alters- oder Invalidenrente selbst vor, die dem berechtigten Ehegatten in Form einer lebenslänglichen Rente ausbezahlt wird (Art. 124a ZGB)."},
                {"q": "Kann man auf die Teilung der 2. Säule verzichten?",
                 "a": "Die Ehegatten können in einer Scheidungsfolgenvereinbarung eine abweichende Teilung vereinbaren oder teilweise darauf verzichten, sofern für beide eine angemessene Alters- und Invalidenvorsorge gewährleistet bleibt, was das Gericht vor Genehmigung der Vereinbarung prüft."},
                {"q": "Wird auch die 3. Säule bei einer Scheidung geteilt?",
                 "a": "Die gebundene 3. Säule (3a) und die freie 3. Säule (3b) fallen nicht unter die Teilung der beruflichen Vorsorge nach Art. 122 ZGB; sie werden grundsätzlich im Rahmen der güterrechtlichen Auseinandersetzung behandelt, je nach anwendbarem Güterstand."},
            ],
        },
        "it": {
            "slug": "divisione-secondo-pilastro-divorzio",
            "title": "Divisione del secondo pilastro in caso di divorzio",
            "meta": "Divisione paritetica della previdenza professionale, casi particolari, deroghe possibili: quanto previsto dal Codice civile in caso di divorzio.",
            "sections": [
                {"heading": "Il principio della divisione paritetica", "paragraphs": [
                    "Gli averi di previdenza professionale (2° pilastro) accumulati da entrambi i coniugi durante il matrimonio fino all'avvio della procedura di divorzio sono in linea di principio divisi a metà tra loro (art. 122 CC). Questa divisione mira a compensare lo svantaggio previdenziale che spesso subisce il coniuge che ha ridotto o cessato la propria attività lucrativa per dedicarsi alla famiglia o ai figli.",
                ]},
                {"heading": "Quando uno dei coniugi è già in pensione o invalido", "paragraphs": [
                    "Se uno dei coniugi percepisce già una rendita di vecchiaia o una rendita d'invalidità al momento del divorzio, una divisione classica dell'avere di previdenza non è più possibile: la legge prevede allora una divisione della rendita stessa, sotto forma di una rendita vitalizia versata al coniuge creditore (art. 124a CC).",
                ]},
                {"heading": "Le deroghe alla divisione paritetica", "paragraphs": [
                    "Il tribunale può derogare alla divisione paritetica per motivi validi, in particolare se questa divisione è manifestamente iniqua rispetto ai bisogni previdenziali rispettivi dei coniugi, per esempio a causa di una grande differenza d'età o della liquidazione del regime dei beni (art. 124b CC).",
                ]},
                {"heading": "L'esecuzione della divisione", "paragraphs": [
                    "Il tribunale trasmette l'incarto agli istituti di previdenza interessati, che procedono al trasferimento degli importi. Se uno dei coniugi non è affiliato ad alcun istituto di previdenza o se il trasferimento diretto non è possibile, interviene la Fondazione istituto collettore LPP per ricevere e gestire gli importi trasferiti.",
                ]},
            ],
            "faq": [
                {"q": "La divisione del 2° pilastro è automatica in caso di divorzio?",
                 "a": "Sì, salvo accordo contrario dei coniugi validato dal tribunale o situazione particolare (pensionamento, invalidità): la divisione paritetica dell'avere accumulato durante il matrimonio è il principio legale (art. 122 CC)."},
                {"q": "Cosa succede se uno dei coniugi è già in pensione?",
                 "a": "Una divisione classica dell'avere non è più possibile; la legge prevede allora una divisione della rendita di vecchiaia o d'invalidità stessa, versata al coniuge creditore sotto forma di rendita vitalizia (art. 124a CC)."},
                {"q": "Si può rinunciare alla divisione del 2° pilastro?",
                 "a": "I coniugi possono convenire una divisione diversa o rinunciarvi parzialmente in una convenzione sugli effetti del divorzio, a condizione che rimanga garantita per entrambi una previdenza per la vecchiaia e l'invalidità adeguata, cosa che il tribunale verifica prima di omologare la convenzione."},
                {"q": "Anche il 3° pilastro viene diviso in caso di divorzio?",
                 "a": "Il 3° pilastro vincolato (3a) e il 3° pilastro libero (3b) non rientrano nella divisione della previdenza professionale dell'art. 122 CC; sono in linea di principio trattati nell'ambito della liquidazione del regime dei beni, secondo il regime applicabile."},
            ],
        },
        "en": {
            "slug": "division-second-pillar-divorce",
            "title": "Division of occupational pension assets in divorce",
            "meta": "Equal division of occupational pension assets, special cases, possible deviations: what the Civil Code provides in the event of divorce.",
            "sections": [
                {"heading": "The principle of equal division", "paragraphs": [
                    "Occupational pension assets (2nd pillar) accumulated by both spouses during the marriage up to the start of divorce proceedings are in principle divided equally between them (art. 122 CC). This division aims to offset the pension disadvantage often suffered by the spouse who reduced or gave up gainful employment to devote themselves to the household or children.",
                ]},
                {"heading": "When a spouse is already retired or disabled", "paragraphs": [
                    "If a spouse already receives an old-age or disability pension at the time of divorce, a conventional division of the pension assets is no longer possible: the law then provides for a division of the pension itself, in the form of a lifelong pension paid to the entitled spouse (art. 124a CC).",
                ]},
                {"heading": "Deviations from equal division", "paragraphs": [
                    "The court may deviate from equal division for good cause, in particular where such division would be manifestly inequitable given the spouses' respective pension needs, for example due to a large age gap or as a result of the division of marital property (art. 124b CC).",
                ]},
                {"heading": "Carrying out the division", "paragraphs": [
                    "The court forwards the file to the pension funds concerned, which carry out the transfer of the amounts. If a spouse is not affiliated with any pension fund, or if direct transfer is not possible, the Substitute Occupational Benefit Institution steps in to receive and manage the transferred amounts.",
                ]},
            ],
            "faq": [
                {"q": "Is the division of the 2nd pillar automatic in a divorce?",
                 "a": "Yes, unless the spouses agree otherwise and the court approves it, or a special situation applies (retirement, disability): equal division of the assets accumulated during the marriage is the statutory principle (art. 122 CC)."},
                {"q": "What happens if a spouse is already retired?",
                 "a": "A conventional division of the assets is no longer possible; the law then provides for a division of the old-age or disability pension itself, paid to the entitled spouse as a lifelong pension (art. 124a CC)."},
                {"q": "Can spouses waive the division of the 2nd pillar?",
                 "a": "Spouses can agree on a different division or partially waive it in an agreement on the effects of divorce, provided adequate old-age and disability provision remains guaranteed for both, which the court checks before approving the agreement."},
                {"q": "Is the 3rd pillar also divided in a divorce?",
                 "a": "Tied 3rd pillar assets (3a) and unrestricted 3rd pillar assets (3b) do not fall under the division of occupational pension assets in art. 122 CC; they are in principle dealt with as part of the division of marital property, depending on the matrimonial property regime that applies."},
            ],
        },
    },
    "casier-judiciaire-suisse": {
        "domaine_id": "droit_penal",
        "published": "2026-07-30",
        "fr": {
            "slug": "casier-judiciaire-suisse-inscription-radiation",
            "title": "Casier judiciaire suisse : inscription et radiation",
            "meta": "Ce qui figure au casier judiciaire, la différence entre extrait pour particuliers et extrait pour autorités, et comment les inscriptions sont radiées.",
            "sections": [
                {"heading": "Ce qui figure au casier judiciaire", "paragraphs": [
                    "Le casier judiciaire suisse, géré au niveau fédéral dans le système d'information VOSTRA, recense les jugements pénaux prononcés contre une personne : peines privatives de liberté, peines pécuniaires, travail d'intérêt général, ainsi que certaines décisions d'autorités administratives compétentes en matière pénale.",
                ]},
                {"heading": "Deux types d'extraits", "paragraphs": [
                    "L'extrait destiné à un particulier, que chacun peut demander pour lui-même, est plus limité que l'extrait complet réservé aux autorités de poursuite pénale et à certaines autorités administratives habilitées par la loi. Un employeur ne peut donc pas exiger de consulter directement le casier judiciaire : il peut seulement demander au candidat ou à l'employé de produire lui-même son extrait pour particuliers.",
                ]},
                {"heading": "La radiation des inscriptions", "paragraphs": [
                    "Les inscriptions ne restent pas indéfiniment au casier judiciaire : la loi prévoit des délais de radiation qui dépendent de la gravité de la peine prononcée, les sanctions les plus légères étant radiées plus rapidement que les peines privatives de liberté de longue durée. Une fois radiée, une inscription n'apparaît plus, y compris sur l'extrait destiné aux autorités, sauf exceptions prévues par la loi.",
                ]},
            ],
            "faq": [
                {"q": "Comment obtenir un extrait de son casier judiciaire ?",
                 "a": "La demande se fait en ligne auprès de l'Office fédéral de la justice, moyennant une pièce d'identité et le paiement d'un émolument. L'extrait est envoyé par courrier à l'adresse de domicile enregistrée."},
                {"q": "Un employeur peut-il consulter mon casier judiciaire sans mon accord ?",
                 "a": "Non. Seules les autorités habilitées par la loi ont un accès direct au système VOSTRA. Un employeur ne peut que demander au candidat de lui remettre lui-même son extrait pour particuliers."},
                {"q": "Toutes les condamnations pénales apparaissent-elles sur l'extrait pour particuliers ?",
                 "a": "Non, cet extrait est plus restreint que celui destiné aux autorités : certaines inscriptions, notamment les sanctions les plus légères ou anciennes, n'y figurent pas ou plus, selon les règles fixées par la loi sur le casier judiciaire."},
                {"q": "Combien de temps une condamnation reste-t-elle inscrite ?",
                 "a": "La durée dépend de la gravité de la peine prononcée : plus la sanction est lourde, plus le délai avant radiation est long. Pour connaître le délai applicable à une situation précise, il faut se référer à la loi fédérale sur le casier judiciaire ou consulter un avocat."},
            ],
        },
        "de": {
            "slug": "strafregister-schweiz-eintrag-loeschung",
            "title": "Strafregister Schweiz: Eintrag und Löschung",
            "meta": "Was im Strafregister erscheint, Unterschied zwischen Privatauszug und Behördenauszug, wie Einträge gelöscht werden.",
            "sections": [
                {"heading": "Was im Strafregister erscheint", "paragraphs": [
                    "Das schweizerische Strafregister, geführt auf Bundesebene im Informationssystem VOSTRA, erfasst die gegen eine Person ausgesprochenen Strafurteile: Freiheitsstrafen, Geldstrafen, gemeinnützige Arbeit, sowie bestimmte Entscheide zuständiger Verwaltungsbehörden im Strafbereich.",
                ]},
                {"heading": "Zwei Arten von Auszügen", "paragraphs": [
                    "Der Privatauszug, den jede Person für sich selbst verlangen kann, ist eingeschränkter als der vollständige Auszug, der den Strafverfolgungsbehörden und bestimmten gesetzlich ermächtigten Verwaltungsbehörden vorbehalten ist. Ein Arbeitgeber kann daher nicht direkt Einsicht ins Strafregister verlangen: er kann lediglich vom Bewerber oder der Angestellten verlangen, selbst den Privatauszug vorzulegen.",
                ]},
                {"heading": "Die Löschung von Einträgen", "paragraphs": [
                    "Einträge bleiben nicht unbegrenzt im Strafregister: das Gesetz sieht Löschungsfristen vor, die von der Schwere der ausgesprochenen Strafe abhängen, wobei leichtere Sanktionen schneller gelöscht werden als längere Freiheitsstrafen. Ein gelöschter Eintrag erscheint nicht mehr, auch nicht im Behördenauszug, ausser in den gesetzlich vorgesehenen Ausnahmen.",
                ]},
            ],
            "faq": [
                {"q": "Wie erhalte ich einen Auszug aus meinem Strafregister?",
                 "a": "Der Antrag erfolgt online beim Bundesamt für Justiz, gegen Vorlage eines Ausweises und Zahlung einer Gebühr. Der Auszug wird per Post an die registrierte Wohnadresse geschickt."},
                {"q": "Kann ein Arbeitgeber mein Strafregister ohne meine Zustimmung einsehen?",
                 "a": "Nein. Nur gesetzlich ermächtigte Behörden haben direkten Zugriff auf VOSTRA. Ein Arbeitgeber kann lediglich vom Bewerber verlangen, ihm selbst seinen Privatauszug vorzulegen."},
                {"q": "Erscheinen alle strafrechtlichen Verurteilungen im Privatauszug?",
                 "a": "Nein, dieser Auszug ist eingeschränkter als jener für Behörden: bestimmte Einträge, insbesondere leichtere oder ältere Sanktionen, erscheinen dort nicht oder nicht mehr, gemäss den Regeln des Strafregistergesetzes."},
                {"q": "Wie lange bleibt eine Verurteilung eingetragen?",
                 "a": "Die Dauer hängt von der Schwere der ausgesprochenen Strafe ab: je härter die Sanktion, desto länger die Frist bis zur Löschung. Für die im Einzelfall geltende Frist ist das Strafregistergesetz massgebend, oder man wendet sich an eine Anwältin oder einen Anwalt."},
            ],
        },
        "it": {
            "slug": "casellario-giudiziale-svizzero-iscrizione-radiazione",
            "title": "Casellario giudiziale svizzero: iscrizione e radiazione",
            "meta": "Cosa figura nel casellario giudiziale, differenza tra estratto per privati ed estratto per autorità, e come vengono radiate le iscrizioni.",
            "sections": [
                {"heading": "Cosa figura nel casellario giudiziale", "paragraphs": [
                    "Il casellario giudiziale svizzero, gestito a livello federale nel sistema d'informazione VOSTRA, registra le sentenze penali pronunciate contro una persona: pene detentive, pene pecuniarie, lavoro di pubblica utilità, nonché determinate decisioni di autorità amministrative competenti in materia penale.",
                ]},
                {"heading": "Due tipi di estratti", "paragraphs": [
                    "L'estratto destinato a un privato, che ognuno può richiedere per sé stesso, è più limitato rispetto all'estratto completo riservato alle autorità di perseguimento penale e a determinate autorità amministrative autorizzate dalla legge. Un datore di lavoro non può quindi esigere di consultare direttamente il casellario giudiziale: può solo chiedere al candidato o al dipendente di produrre lui stesso il proprio estratto per privati.",
                ]},
                {"heading": "La radiazione delle iscrizioni", "paragraphs": [
                    "Le iscrizioni non restano indefinitamente nel casellario giudiziale: la legge prevede termini di radiazione che dipendono dalla gravità della pena pronunciata, con le sanzioni più lievi radiate più rapidamente rispetto alle pene detentive di lunga durata. Una volta radiata, un'iscrizione non appare più, nemmeno nell'estratto destinato alle autorità, salvo eccezioni previste dalla legge.",
                ]},
            ],
            "faq": [
                {"q": "Come si ottiene un estratto del proprio casellario giudiziale?",
                 "a": "La richiesta si fa online presso l'Ufficio federale di giustizia, mediante un documento d'identità e il pagamento di un emolumento. L'estratto viene inviato per posta all'indirizzo di domicilio registrato."},
                {"q": "Un datore di lavoro può consultare il mio casellario giudiziale senza il mio accordo?",
                 "a": "No. Solo le autorità autorizzate dalla legge hanno un accesso diretto al sistema VOSTRA. Un datore di lavoro può solo chiedere al candidato di consegnargli personalmente il proprio estratto per privati."},
                {"q": "Tutte le condanne penali figurano nell'estratto per privati?",
                 "a": "No, questo estratto è più limitato rispetto a quello destinato alle autorità: alcune iscrizioni, in particolare le sanzioni più lievi o meno recenti, non vi figurano o non vi figurano più, secondo le regole fissate dalla legge sul casellario giudiziale."},
                {"q": "Per quanto tempo resta iscritta una condanna?",
                 "a": "La durata dipende dalla gravità della pena pronunciata: più severa è la sanzione, più lungo è il termine prima della radiazione. Per conoscere il termine applicabile a una situazione precisa, occorre fare riferimento alla legge federale sul casellario giudiziale o consultare un avvocato."},
            ],
        },
        "en": {
            "slug": "swiss-criminal-record-entry-removal",
            "title": "Swiss criminal record: entries and removal",
            "meta": "What appears on the criminal record, the difference between a private and an authorities' extract, and how entries are removed.",
            "sections": [
                {"heading": "What appears on the criminal record", "paragraphs": [
                    "The Swiss criminal record, managed at federal level in the VOSTRA information system, lists the criminal judgments issued against a person: custodial sentences, monetary penalties, community work, and certain decisions of administrative authorities competent in criminal matters.",
                ]},
                {"heading": "Two types of extracts", "paragraphs": [
                    "The extract available to a private individual, which anyone can request for themselves, is more limited than the full extract reserved for criminal prosecution authorities and certain administrative authorities authorised by law. An employer therefore cannot demand direct access to the criminal record: they can only ask a candidate or employee to produce their own private extract.",
                ]},
                {"heading": "Removal of entries", "paragraphs": [
                    "Entries do not remain on the criminal record indefinitely: the law sets removal periods that depend on the severity of the sentence imposed, with lighter sanctions removed more quickly than long custodial sentences. Once removed, an entry no longer appears, even on the extract intended for authorities, subject to exceptions provided by law.",
                ]},
            ],
            "faq": [
                {"q": "How do I obtain an extract of my criminal record?",
                 "a": "The request is made online with the Federal Office of Justice, with proof of identity and payment of a fee. The extract is sent by post to the registered home address."},
                {"q": "Can an employer check my criminal record without my consent?",
                 "a": "No. Only authorities authorised by law have direct access to VOSTRA. An employer can only ask a candidate to provide their own private extract."},
                {"q": "Do all criminal convictions appear on the private extract?",
                 "a": "No, this extract is more limited than the one for authorities: certain entries, particularly lighter or older sanctions, do not appear or no longer appear on it, according to the rules set by the criminal records law."},
                {"q": "How long does a conviction remain on record?",
                 "a": "The duration depends on the severity of the sentence imposed: the heavier the sanction, the longer the period before removal. To find the period applicable to a specific situation, refer to the federal law on criminal records or consult a lawyer."},
            ],
        },
    },
    "ordonnance-penale-opposition": {
        "domaine_id": "droit_penal",
        "published": "2026-07-30",
        "fr": {
            "slug": "ordonnance-penale-que-faire-opposition",
            "title": "Ordonnance pénale : que faire si vous en recevez une",
            "meta": "Délai d'opposition, motivation, conséquences de l'absence d'opposition : ce qu'il faut savoir sur l'ordonnance pénale selon le Code de procédure pénale.",
            "sections": [
                {"heading": "Qu'est-ce qu'une ordonnance pénale", "paragraphs": [
                    "L'ordonnance pénale (art. 352 CPP) est une décision rendue par le ministère public sans débats devant un tribunal, pour des infractions de gravité limitée. Elle suppose que le prévenu ait été entendu ou ait eu l'occasion de s'exprimer, que les faits soient établis, et que la sanction n'excède pas les limites fixées par la loi (notamment une peine privative de liberté de six mois au plus, combinée le cas échéant avec une peine pécuniaire ou une amende).",
                ]},
                {"heading": "Faire opposition", "paragraphs": [
                    "Le prévenu, ou toute autre personne directement touchée par l'ordonnance, peut y faire opposition par écrit dans les dix jours auprès du ministère public qui l'a rendue (art. 354 CPP). L'opposition doit en principe être motivée, sauf si elle porte uniquement sur la quotité de la peine, auquel cas une simple déclaration suffit.",
                ]},
                {"heading": "Les suites d'une opposition valable", "paragraphs": [
                    "Si l'opposition est recevable, le ministère public administre les preuves nécessaires pour statuer sur elle. Il peut ensuite maintenir l'ordonnance pénale, classer la procédure, rendre une nouvelle ordonnance pénale, ou porter l'accusation devant le tribunal de première instance si le désaccord persiste (art. 355-356 CPP).",
                ]},
                {"heading": "Ce qui se passe en l'absence d'opposition", "paragraphs": [
                    "Si aucune opposition n'est formée dans le délai de dix jours, l'ordonnance pénale devient un jugement entré en force, avec les mêmes effets qu'une condamnation pénale prononcée par un tribunal, y compris son inscription au casier judiciaire le cas échéant.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai dois-je faire opposition à une ordonnance pénale ?",
                 "a": "Dans les dix jours suivant sa notification, par écrit, auprès du ministère public qui l'a rendue (art. 354 CPP)."},
                {"q": "Que se passe-t-il si je ne fais pas opposition ?",
                 "a": "L'ordonnance pénale devient un jugement définitif et exécutoire, avec les mêmes effets qu'une condamnation prononcée par un tribunal, y compris l'inscription au casier judiciaire si la sanction le prévoit."},
                {"q": "L'opposition doit-elle être motivée ?",
                 "a": "En principe oui, sauf si elle porte uniquement sur la quotité de la peine (le montant ou la durée de la sanction), auquel cas une opposition non motivée suffit selon l'art. 354 CPP."},
                {"q": "Une ordonnance pénale figure-t-elle au casier judiciaire ?",
                 "a": "Si elle entre en force et que la sanction prononcée relève des cas soumis à inscription selon la loi sur le casier judiciaire, oui : une ordonnance pénale a les mêmes effets qu'un jugement pénal ordinaire."},
            ],
        },
        "de": {
            "slug": "strafbefehl-was-tun-einsprache",
            "title": "Strafbefehl: was tun, wenn Sie einen erhalten",
            "meta": "Einsprachefrist, Begründung, Folgen fehlender Einsprache: was Sie gemäss Strafprozessordnung zum Strafbefehl wissen müssen.",
            "sections": [
                {"heading": "Was ist ein Strafbefehl", "paragraphs": [
                    "Der Strafbefehl (Art. 352 StPO) ist ein Entscheid der Staatsanwaltschaft ohne gerichtliche Verhandlung, für Straftaten begrenzter Schwere. Er setzt voraus, dass die beschuldigte Person angehört wurde oder Gelegenheit dazu hatte, dass der Sachverhalt geklärt ist und die Sanktion die gesetzlichen Grenzen nicht übersteigt (insbesondere höchstens sechs Monate Freiheitsstrafe, gegebenenfalls verbunden mit einer Geldstrafe oder Busse).",
                ]},
                {"heading": "Einsprache erheben", "paragraphs": [
                    "Die beschuldigte Person, oder jede andere direkt betroffene Person, kann gegen den Strafbefehl innert zehn Tagen schriftlich Einsprache bei der ausstellenden Staatsanwaltschaft erheben (Art. 354 StPO). Die Einsprache muss grundsätzlich begründet werden, ausser sie betrifft nur das Strafmass, in welchem Fall eine blosse Erklärung genügt.",
                ]},
                {"heading": "Die Folgen einer gültigen Einsprache", "paragraphs": [
                    "Ist die Einsprache zulässig, erhebt die Staatsanwaltschaft die zur Beurteilung nötigen Beweise. Sie kann anschliessend am Strafbefehl festhalten, das Verfahren einstellen, einen neuen Strafbefehl erlassen oder bei fortbestehender Uneinigkeit Anklage vor dem erstinstanzlichen Gericht erheben (Art. 355-356 StPO).",
                ]},
                {"heading": "Was geschieht ohne Einsprache", "paragraphs": [
                    "Wird innert der zehntägigen Frist keine Einsprache erhoben, wird der Strafbefehl zu einem rechtskräftigen Urteil, mit denselben Wirkungen wie eine von einem Gericht ausgesprochene Verurteilung, einschliesslich gegebenenfalls des Eintrags ins Strafregister.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist muss ich gegen einen Strafbefehl Einsprache erheben?",
                 "a": "Innert zehn Tagen nach dessen Zustellung, schriftlich, bei der ausstellenden Staatsanwaltschaft (Art. 354 StPO)."},
                {"q": "Was geschieht, wenn ich keine Einsprache erhebe?",
                 "a": "Der Strafbefehl wird zu einem endgültigen und vollstreckbaren Urteil, mit denselben Wirkungen wie eine von einem Gericht ausgesprochene Verurteilung, einschliesslich des Eintrags ins Strafregister, falls die Sanktion dies vorsieht."},
                {"q": "Muss die Einsprache begründet werden?",
                 "a": "Grundsätzlich ja, ausser sie betrifft nur das Strafmass (Höhe oder Dauer der Sanktion), in welchem Fall eine unbegründete Einsprache gemäss Art. 354 StPO genügt."},
                {"q": "Wird ein Strafbefehl im Strafregister eingetragen?",
                 "a": "Wenn er rechtskräftig wird und die ausgesprochene Sanktion unter die eintragungspflichtigen Fälle gemäss dem Strafregistergesetz fällt, ja: ein Strafbefehl hat dieselben Wirkungen wie ein ordentliches Strafurteil."},
            ],
        },
        "it": {
            "slug": "decreto-accusa-cosa-fare-opposizione",
            "title": "Decreto d'accusa: cosa fare se ne ricevete uno",
            "meta": "Termine di opposizione, motivazione, conseguenze della mancata opposizione: quanto occorre sapere sul decreto d'accusa secondo il Codice di procedura penale.",
            "sections": [
                {"heading": "Cos'è un decreto d'accusa", "paragraphs": [
                    "Il decreto d'accusa (art. 352 CPP) è una decisione emessa dal pubblico ministero senza dibattimento davanti a un tribunale, per reati di gravità limitata. Presuppone che l'imputato sia stato sentito o abbia avuto la possibilità di esprimersi, che i fatti siano accertati e che la sanzione non superi i limiti fissati dalla legge (in particolare al massimo sei mesi di pena detentiva, eventualmente combinata con una pena pecuniaria o una multa).",
                ]},
                {"heading": "Fare opposizione", "paragraphs": [
                    "L'imputato, o qualsiasi altra persona direttamente toccata dal decreto, può fare opposizione per scritto entro dieci giorni presso il pubblico ministero che l'ha emesso (art. 354 CPP). L'opposizione deve in linea di principio essere motivata, salvo se riguarda unicamente la commisurazione della pena, nel qual caso è sufficiente una semplice dichiarazione.",
                ]},
                {"heading": "Le conseguenze di un'opposizione valida", "paragraphs": [
                    "Se l'opposizione è ricevibile, il pubblico ministero assume le prove necessarie per deciderne. Può quindi confermare il decreto d'accusa, abbandonare il procedimento, emettere un nuovo decreto d'accusa, o promuovere l'accusa davanti al tribunale di primo grado se il disaccordo persiste (art. 355-356 CPP).",
                ]},
                {"heading": "Cosa succede in assenza di opposizione", "paragraphs": [
                    "Se nessuna opposizione è formata entro il termine di dieci giorni, il decreto d'accusa diventa una sentenza passata in giudicato, con gli stessi effetti di una condanna penale pronunciata da un tribunale, inclusa l'eventuale iscrizione nel casellario giudiziale.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine devo fare opposizione a un decreto d'accusa?",
                 "a": "Entro dieci giorni dalla notifica, per scritto, presso il pubblico ministero che l'ha emesso (art. 354 CPP)."},
                {"q": "Cosa succede se non faccio opposizione?",
                 "a": "Il decreto d'accusa diventa una sentenza definitiva ed esecutiva, con gli stessi effetti di una condanna pronunciata da un tribunale, inclusa l'iscrizione nel casellario giudiziale se la sanzione lo prevede."},
                {"q": "L'opposizione deve essere motivata?",
                 "a": "In linea di principio sì, salvo se riguarda unicamente la commisurazione della pena (l'importo o la durata della sanzione), nel qual caso un'opposizione non motivata è sufficiente secondo l'art. 354 CPP."},
                {"q": "Un decreto d'accusa figura nel casellario giudiziale?",
                 "a": "Se passa in giudicato e la sanzione pronunciata rientra nei casi soggetti a iscrizione secondo la legge sul casellario giudiziale, sì: un decreto d'accusa ha gli stessi effetti di una sentenza penale ordinaria."},
            ],
        },
        "en": {
            "slug": "summary-penalty-order-what-to-do-objection",
            "title": "Summary penalty order: what to do if you receive one",
            "meta": "Time limit to object, reasoning requirements, consequences of not objecting: what to know about the summary penalty order under Swiss criminal procedure.",
            "sections": [
                {"heading": "What is a summary penalty order", "paragraphs": [
                    "The summary penalty order (art. 352 CPP) is a decision issued by the public prosecutor without a court hearing, for offences of limited severity. It requires that the accused has been heard or given the opportunity to be heard, that the facts are established, and that the sanction does not exceed the limits set by law (in particular a custodial sentence of at most six months, possibly combined with a monetary penalty or fine).",
                ]},
                {"heading": "Filing an objection", "paragraphs": [
                    "The accused, or any other person directly affected by the order, can file a written objection within ten days with the public prosecutor's office that issued it (art. 354 CPP). The objection must in principle be reasoned, unless it concerns only the amount of the sentence, in which case a simple statement suffices.",
                ]},
                {"heading": "What happens after a valid objection", "paragraphs": [
                    "If the objection is admissible, the public prosecutor gathers the evidence needed to rule on it. It can then uphold the summary penalty order, dismiss the case, issue a new summary penalty order, or bring the charge before the court of first instance if the disagreement persists (art. 355-356 CPP).",
                ]},
                {"heading": "What happens without an objection", "paragraphs": [
                    "If no objection is filed within the ten-day period, the summary penalty order becomes a final judgment, with the same effects as a conviction handed down by a court, including entry on the criminal record where applicable.",
                ]},
            ],
            "faq": [
                {"q": "Within what time limit must I object to a summary penalty order?",
                 "a": "Within ten days of its notification, in writing, with the public prosecutor's office that issued it (art. 354 CPP)."},
                {"q": "What happens if I don't object?",
                 "a": "The summary penalty order becomes a final and enforceable judgment, with the same effects as a conviction handed down by a court, including entry on the criminal record if the sanction provides for it."},
                {"q": "Does the objection need to be reasoned?",
                 "a": "In principle yes, unless it concerns only the amount of the sentence, in which case an unreasoned objection is sufficient under art. 354 CPP."},
                {"q": "Does a summary penalty order appear on the criminal record?",
                 "a": "If it becomes final and the sanction imposed falls within the cases subject to registration under the criminal records law, yes: a summary penalty order has the same effects as an ordinary criminal judgment."},
            ],
        },
    },
    "resiliation-bail-delais-contestation": {
        "domaine_id": "droit_bail",
        "published": "2026-07-30",
        "fr": {
            "slug": "resiliation-bail-delais-formulaire-contestation",
            "title": "Résiliation du bail : délais et contestation",
            "meta": "Formulaire officiel, délais de préavis, congé abusif et délai de contestation : les règles du Code des obligations sur la résiliation du bail.",
            "sections": [
                {"heading": "La forme de la résiliation", "paragraphs": [
                    "La résiliation d'un bail portant sur des locaux d'habitation ou commerciaux doit se faire par écrit et, du côté du bailleur, au moyen d'une formule officielle agréée par le canton (art. 266l CO). Une résiliation qui ne respecte pas cette forme est nulle et sans effet.",
                ]},
                {"heading": "Les délais et termes", "paragraphs": [
                    "Sauf accord contraire, un bail d'habitation peut être résilié moyennant un préavis d'au moins trois mois pour le prochain terme fixé par l'usage local (art. 266c CO). Les délais et termes applicables aux baux commerciaux ou mobiliers sont différents et fixés par les art. 266a-266e CO.",
                    "Le locataire peut aussi résilier le bail de façon anticipée, avant l'échéance contractuelle, s'il présente un locataire de remplacement solvable et prêt à reprendre le bail aux mêmes conditions (art. 264 CO).",
                ]},
                {"heading": "Le congé abusif", "paragraphs": [
                    "Un congé peut être annulé s'il contrevient aux règles de la bonne foi (art. 271-271a CO), notamment lorsqu'il est donné parce que le locataire a fait valoir de bonne foi des prétentions découlant du bail, pendant une procédure de conciliation ou judiciaire relative au bail, ou dans les trois ans suivant la fin d'une telle procédure si le bailleur a obtenu gain de cause pour l'essentiel, sauf exceptions prévues par la loi.",
                ]},
                {"heading": "Contester un congé", "paragraphs": [
                    "Le locataire qui estime son congé abusif doit saisir l'autorité de conciliation dans les 30 jours suivant sa réception (art. 273 CO). Passé ce délai, le congé ne peut plus être contesté sur ce motif.",
                ]},
            ],
            "faq": [
                {"q": "Mon bailleur doit-il justifier la résiliation de mon bail ?",
                 "a": "Non, la loi n'exige pas de motif pour une résiliation ordinaire. Le congé peut toutefois être annulé s'il est donné dans des circonstances contraires à la bonne foi visées par l'art. 271-271a CO."},
                {"q": "Que faire si je reçois un congé sans le formulaire officiel ?",
                 "a": "Un congé donné par le bailleur sans la formule officielle agréée par le canton est nul (art. 266l CO) : il est réputé n'avoir jamais été donné, sans qu'il soit même nécessaire de le contester devant l'autorité de conciliation."},
                {"q": "Puis-je résilier mon bail avant l'échéance contractuelle ?",
                 "a": "Oui, à condition de présenter un locataire de remplacement solvable, prêt à reprendre le bail aux mêmes conditions et acceptable pour le bailleur (art. 264 CO)."},
                {"q": "Dans quel délai dois-je contester un congé que je trouve abusif ?",
                 "a": "Dans les 30 jours suivant la réception du congé, en saisissant l'autorité de conciliation compétente (art. 273 CO)."},
            ],
        },
        "de": {
            "slug": "kuendigung-mietvertrag-fristen-anfechtung",
            "title": "Kündigung des Mietvertrags: Fristen und Anfechtung",
            "meta": "Amtliches Formular, Kündigungsfristen, missbräuchliche Kündigung und Anfechtungsfrist: die Regeln des Obligationenrechts zur Mietkündigung.",
            "sections": [
                {"heading": "Die Form der Kündigung", "paragraphs": [
                    "Die Kündigung eines Miet- oder Pachtverhältnisses über Wohn- oder Geschäftsräume muss schriftlich erfolgen und, seitens der Vermieterschaft, mittels eines vom Kanton genehmigten amtlichen Formulars (Art. 266l OR). Eine Kündigung, die diese Form nicht einhält, ist nichtig und unwirksam.",
                ]},
                {"heading": "Fristen und Termine", "paragraphs": [
                    "Mangels anderer Vereinbarung kann ein Wohnraummietvertrag mit einer Frist von mindestens drei Monaten auf den nächsten ortsüblichen Termin gekündigt werden (Art. 266c OR). Für Geschäfts- oder Fahrnismieten gelten andere Fristen und Termine gemäss Art. 266a-266e OR.",
                    "Die Mieterschaft kann den Mietvertrag auch vorzeitig kündigen, wenn sie eine zumutbare Ersatzmieterin oder einen zumutbaren Ersatzmieter stellt, die oder der zahlungsfähig ist und bereit ist, den Vertrag zu gleichen Bedingungen zu übernehmen (Art. 264 OR).",
                ]},
                {"heading": "Die missbräuchliche Kündigung", "paragraphs": [
                    "Eine Kündigung kann angefochten werden, wenn sie gegen Treu und Glauben verstösst (Art. 271-271a OR), namentlich wenn sie ausgesprochen wird, weil die Mieterschaft nach Treu und Glauben Ansprüche aus dem Mietverhältnis geltend gemacht hat, während eines Schlichtungs- oder Gerichtsverfahrens über das Mietverhältnis oder innert drei Jahren nach Abschluss eines solchen Verfahrens, falls die Vermieterschaft im Wesentlichen obsiegt hat, vorbehältlich gesetzlicher Ausnahmen.",
                ]},
                {"heading": "Eine Kündigung anfechten", "paragraphs": [
                    "Die Mieterschaft, die ihre Kündigung für missbräuchlich hält, muss innert 30 Tagen nach deren Erhalt die Schlichtungsbehörde anrufen (Art. 273 OR). Nach Ablauf dieser Frist kann die Kündigung aus diesem Grund nicht mehr angefochten werden.",
                ]},
            ],
            "faq": [
                {"q": "Muss meine Vermieterin oder mein Vermieter die Kündigung begründen?",
                 "a": "Nein, das Gesetz verlangt für eine ordentliche Kündigung keinen Grund. Die Kündigung kann jedoch für nichtig erklärt werden, wenn sie unter Umständen erfolgt, die gegen Treu und Glauben gemäss Art. 271-271a OR verstossen."},
                {"q": "Was tun, wenn ich eine Kündigung ohne amtliches Formular erhalte?",
                 "a": "Eine Kündigung der Vermieterschaft ohne das vom Kanton genehmigte amtliche Formular ist nichtig (Art. 266l OR): sie gilt als nie ausgesprochen, ohne dass es nötig wäre, sie vor der Schlichtungsbehörde anzufechten."},
                {"q": "Kann ich meinen Mietvertrag vor Ablauf der vertraglichen Frist kündigen?",
                 "a": "Ja, sofern ich eine zahlungsfähige Ersatzmieterin oder einen zahlungsfähigen Ersatzmieter stelle, die oder der bereit ist, den Vertrag zu gleichen Bedingungen zu übernehmen und für die Vermieterschaft zumutbar ist (Art. 264 OR)."},
                {"q": "Innert welcher Frist muss ich eine Kündigung anfechten, die ich für missbräuchlich halte?",
                 "a": "Innert 30 Tagen nach Erhalt der Kündigung, durch Anrufung der zuständigen Schlichtungsbehörde (Art. 273 OR)."},
            ],
        },
        "it": {
            "slug": "disdetta-locazione-termini-formulario-contestazione",
            "title": "Disdetta della locazione: termini e contestazione",
            "meta": "Formulario ufficiale, termini di preavviso, disdetta abusiva e termine di contestazione: le regole del Codice delle obbligazioni sulla disdetta.",
            "sections": [
                {"heading": "La forma della disdetta", "paragraphs": [
                    "La disdetta di una locazione riguardante locali d'abitazione o commerciali deve avvenire per scritto e, da parte del locatore, mediante un modulo ufficiale approvato dal Cantone (art. 266l CO). Una disdetta che non rispetta questa forma è nulla e priva di effetto.",
                ]},
                {"heading": "I termini e le scadenze", "paragraphs": [
                    "Salvo diverso accordo, una locazione d'abitazione può essere disdetta con un preavviso di almeno tre mesi per la prossima scadenza fissata dall'uso locale (art. 266c CO). I termini e le scadenze applicabili alle locazioni commerciali o mobiliari sono diversi e fissati dagli art. 266a-266e CO.",
                    "Il conduttore può anche disdire la locazione anticipatamente, prima della scadenza contrattuale, se presenta un conduttore sostitutivo solvibile e pronto a riprendere la locazione alle stesse condizioni (art. 264 CO).",
                ]},
                {"heading": "La disdetta abusiva", "paragraphs": [
                    "Una disdetta può essere annullata se contraria alle regole della buona fede (art. 271-271a CO), in particolare quando è data perché il conduttore ha fatto valere in buona fede pretese derivanti dalla locazione, durante una procedura di conciliazione o giudiziaria relativa alla locazione, o entro i tre anni successivi alla fine di tale procedura se il locatore ha ottenuto ragione in misura essenziale, salvo eccezioni previste dalla legge.",
                ]},
                {"heading": "Contestare una disdetta", "paragraphs": [
                    "Il conduttore che ritiene la propria disdetta abusiva deve adire l'autorità di conciliazione entro 30 giorni dal ricevimento (art. 273 CO). Trascorso questo termine, la disdetta non può più essere contestata per questo motivo.",
                ]},
            ],
            "faq": [
                {"q": "Il mio locatore deve giustificare la disdetta della mia locazione?",
                 "a": "No, la legge non richiede un motivo per una disdetta ordinaria. La disdetta può tuttavia essere annullata se data in circostanze contrarie alla buona fede previste dagli art. 271-271a CO."},
                {"q": "Cosa fare se ricevo una disdetta senza il modulo ufficiale?",
                 "a": "Una disdetta data dal locatore senza il modulo ufficiale approvato dal Cantone è nulla (art. 266l CO): è considerata come mai data, senza nemmeno la necessità di contestarla davanti all'autorità di conciliazione."},
                {"q": "Posso disdire la mia locazione prima della scadenza contrattuale?",
                 "a": "Sì, a condizione di presentare un conduttore sostitutivo solvibile, pronto a riprendere la locazione alle stesse condizioni e accettabile per il locatore (art. 264 CO)."},
                {"q": "Entro quale termine devo contestare una disdetta che ritengo abusiva?",
                 "a": "Entro 30 giorni dal ricevimento della disdetta, adendo l'autorità di conciliazione competente (art. 273 CO)."},
            ],
        },
        "en": {
            "slug": "terminating-lease-deadlines-challenge",
            "title": "Terminating a lease: deadlines and challenging notice",
            "meta": "Official form, notice periods, abusive termination and time limit to challenge: the Code of Obligations rules on ending a lease.",
            "sections": [
                {"heading": "The form of the termination notice", "paragraphs": [
                    "Terminating a lease of residential or commercial premises must be done in writing and, on the landlord's side, using an official form approved by the canton (art. 266l CO). Notice that does not comply with this form is null and void.",
                ]},
                {"heading": "Notice periods and dates", "paragraphs": [
                    "Unless otherwise agreed, a residential lease can be terminated with at least three months' notice for the next date fixed by local custom (art. 266c CO). The notice periods and dates applicable to commercial or movable-property leases differ and are set by art. 266a-266e CO.",
                    "A tenant can also terminate the lease early, before the contractual expiry date, by presenting a solvent replacement tenant ready to take over the lease on the same terms (art. 264 CO).",
                ]},
                {"heading": "Abusive termination", "paragraphs": [
                    "Notice can be annulled if it contravenes the rules of good faith (art. 271-271a CO), in particular when given because the tenant has, in good faith, asserted claims arising from the lease, during a conciliation or court procedure relating to the lease, or within three years of the end of such a procedure if the landlord largely prevailed, subject to exceptions provided by law.",
                ]},
                {"heading": "Challenging notice", "paragraphs": [
                    "A tenant who considers their notice abusive must approach the conciliation authority within 30 days of receiving it (art. 273 CO). After this period, the notice can no longer be challenged on this ground.",
                ]},
            ],
            "faq": [
                {"q": "Does my landlord have to justify terminating my lease?",
                 "a": "No, the law does not require a reason for ordinary termination. Notice can, however, be annulled if given in circumstances contrary to good faith under art. 271-271a CO."},
                {"q": "What should I do if I receive notice without the official form?",
                 "a": "Notice given by a landlord without the official form approved by the canton is null and void (art. 266l CO): it is deemed never to have been given, without even needing to challenge it before the conciliation authority."},
                {"q": "Can I terminate my lease before the contractual expiry date?",
                 "a": "Yes, provided I present a solvent replacement tenant, ready to take over the lease on the same terms and acceptable to the landlord (art. 264 CO)."},
                {"q": "Within what time limit must I challenge notice I consider abusive?",
                 "a": "Within 30 days of receiving the notice, by approaching the competent conciliation authority (art. 273 CO)."},
            ],
        },
    },
    "contester-augmentation-loyer": {
        "domaine_id": "droit_bail",
        "published": "2026-07-30",
        "fr": {
            "slug": "contester-augmentation-loyer-suisse",
            "title": "Contester une augmentation de loyer",
            "meta": "Formulaire officiel, motifs de hausse admis, délai de contestation : comment contester une augmentation de loyer selon le Code des obligations.",
            "sections": [
                {"heading": "Le principe du loyer abusif", "paragraphs": [
                    "L'art. 269 CO pose le principe : les loyers sont abusifs lorsqu'ils permettent au bailleur d'obtenir un rendement excessif de la chose louée, ou résultent d'un prix d'achat manifestement exagéré. C'est sur cette base que le locataire peut contester une hausse de loyer.",
                ]},
                {"heading": "La forme de l'avis de majoration", "paragraphs": [
                    "Toute majoration de loyer doit être notifiée au moyen d'une formule officielle agréée par le canton, indiquant les motifs de la hausse (art. 269d CO), au moins dix jours avant le début du délai de résiliation et pour le prochain terme de résiliation possible. Un avis qui ne respecte pas cette forme est nul.",
                ]},
                {"heading": "Les motifs usuels de hausse", "paragraphs": [
                    "Les hausses de loyer sont le plus souvent justifiées par l'adaptation au taux hypothécaire de référence, la hausse des charges ou des coûts d'entretien, des prestations supplémentaires fournies par le bailleur, ou, pour les baux indexés, l'évolution de l'indice suisse des prix à la consommation. Une hausse peut aussi être justifiée par l'adaptation aux loyers usuels du quartier.",
                ]},
                {"heading": "Contester la hausse", "paragraphs": [
                    "Le locataire qui estime la hausse injustifiée peut saisir l'autorité de conciliation dans les 30 jours suivant la réception de l'avis de majoration (art. 270b CO). C'est en principe au bailleur de démontrer que la hausse repose sur l'un des motifs reconnus par la loi.",
                ]},
            ],
            "faq": [
                {"q": "Mon bailleur peut-il augmenter mon loyer comme il le souhaite ?",
                 "a": "Non, toute majoration doit reposer sur un motif reconnu par la loi (adaptation au taux de référence, hausse des charges, prestations supplémentaires, etc.) et être notifiée dans les formes légales."},
                {"q": "Quel document dois-je recevoir en cas de hausse de loyer ?",
                 "a": "La formule officielle agréée par le canton, indiquant le nouveau loyer et les motifs de la hausse (art. 269d CO). Sans ce document, la hausse est nulle."},
                {"q": "Dans quel délai puis-je contester une augmentation de loyer ?",
                 "a": "Dans les 30 jours suivant la réception de l'avis de majoration, en saisissant l'autorité de conciliation compétente (art. 270b CO)."},
                {"q": "Une baisse du taux hypothécaire de référence me donne-t-elle droit à une baisse de loyer ?",
                 "a": "Si votre loyer avait été fixé ou augmenté en tenant compte d'un taux hypothécaire de référence plus élevé, une baisse de ce taux peut justifier une demande de baisse de loyer auprès du bailleur, éventuellement portée devant l'autorité de conciliation en cas de refus."},
            ],
        },
        "de": {
            "slug": "mietzinserhoehung-anfechten-schweiz",
            "title": "Eine Mietzinserhöhung anfechten",
            "meta": "Amtliches Formular, anerkannte Erhöhungsgründe, Anfechtungsfrist: wie eine Mietzinserhöhung gemäss Obligationenrecht angefochten wird.",
            "sections": [
                {"heading": "Der Grundsatz des missbräuchlichen Mietzinses", "paragraphs": [
                    "Art. 269 OR legt den Grundsatz fest: Mietzinse sind missbräuchlich, wenn damit ein übersetzter Ertrag aus der Mietsache erzielt wird oder wenn sie auf einem offensichtlich übersetzten Kaufpreis beruhen. Auf dieser Grundlage kann die Mieterschaft eine Mietzinserhöhung anfechten.",
                ]},
                {"heading": "Die Form der Erhöhungsanzeige", "paragraphs": [
                    "Jede Mietzinserhöhung muss mittels eines vom Kanton genehmigten amtlichen Formulars angezeigt werden, unter Angabe der Erhöhungsgründe (Art. 269d OR), mindestens zehn Tage vor Beginn der Kündigungsfrist und auf den nächstmöglichen Kündigungstermin. Eine Anzeige, die diese Form nicht einhält, ist nichtig.",
                ]},
                {"heading": "Die üblichen Erhöhungsgründe", "paragraphs": [
                    "Mietzinserhöhungen werden meist mit der Anpassung an den hypothekarischen Referenzzinssatz, gestiegenen Nebenkosten oder Unterhaltskosten, zusätzlichen von der Vermieterschaft erbrachten Leistungen oder, bei indexierten Mietverträgen, mit der Entwicklung des Landesindexes der Konsumentenpreise begründet. Eine Erhöhung kann auch mit der Anpassung an die orts- oder quartierüblichen Mietzinse gerechtfertigt werden.",
                ]},
                {"heading": "Die Erhöhung anfechten", "paragraphs": [
                    "Die Mieterschaft, die die Erhöhung für ungerechtfertigt hält, kann innert 30 Tagen nach Erhalt der Erhöhungsanzeige die Schlichtungsbehörde anrufen (Art. 270b OR). Es obliegt grundsätzlich der Vermieterschaft, nachzuweisen, dass die Erhöhung auf einem der gesetzlich anerkannten Gründe beruht.",
                ]},
            ],
            "faq": [
                {"q": "Kann meine Vermieterin oder mein Vermieter den Mietzins beliebig erhöhen?",
                 "a": "Nein, jede Erhöhung muss auf einem gesetzlich anerkannten Grund beruhen (Anpassung an den Referenzzinssatz, gestiegene Nebenkosten, zusätzliche Leistungen usw.) und in der gesetzlich vorgeschriebenen Form angezeigt werden."},
                {"q": "Welches Dokument muss ich bei einer Mietzinserhöhung erhalten?",
                 "a": "Das vom Kanton genehmigte amtliche Formular, mit Angabe des neuen Mietzinses und der Erhöhungsgründe (Art. 269d OR). Ohne dieses Dokument ist die Erhöhung nichtig."},
                {"q": "Innert welcher Frist kann ich eine Mietzinserhöhung anfechten?",
                 "a": "Innert 30 Tagen nach Erhalt der Erhöhungsanzeige, durch Anrufung der zuständigen Schlichtungsbehörde (Art. 270b OR)."},
                {"q": "Gibt mir ein sinkender hypothekarischer Referenzzinssatz Anspruch auf eine Mietzinssenkung?",
                 "a": "Wurde Ihr Mietzins unter Berücksichtigung eines höheren Referenzzinssatzes festgelegt oder erhöht, kann eine Senkung dieses Satzes ein Herabsetzungsbegehren bei der Vermieterschaft rechtfertigen, das bei Ablehnung gegebenenfalls vor die Schlichtungsbehörde gebracht werden kann."},
            ],
        },
        "it": {
            "slug": "contestare-aumento-pigione-svizzera",
            "title": "Contestare un aumento della pigione",
            "meta": "Formulario ufficiale, motivi di aumento ammessi, termine di contestazione: come contestare un aumento della pigione secondo il Codice delle obbligazioni.",
            "sections": [
                {"heading": "Il principio della pigione abusiva", "paragraphs": [
                    "L'art. 269 CO pone il principio: le pigioni sono abusive quando permettono al locatore di ottenere una resa eccessiva della cosa locata, o risultano da un prezzo d'acquisto manifestamente esagerato. È su questa base che il conduttore può contestare un aumento di pigione.",
                ]},
                {"heading": "La forma dell'avviso di aumento", "paragraphs": [
                    "Ogni aumento di pigione deve essere notificato mediante un modulo ufficiale approvato dal Cantone, indicando i motivi dell'aumento (art. 269d CO), almeno dieci giorni prima dell'inizio del termine di disdetta e per la prossima scadenza di disdetta possibile. Un avviso che non rispetta questa forma è nullo.",
                ]},
                {"heading": "I motivi usuali di aumento", "paragraphs": [
                    "Gli aumenti di pigione sono il più delle volte giustificati dall'adeguamento al tasso ipotecario di riferimento, dall'aumento delle spese accessorie o dei costi di manutenzione, da prestazioni supplementari fornite dal locatore, o, per le locazioni indicizzate, dall'evoluzione dell'indice svizzero dei prezzi al consumo. Un aumento può anche essere giustificato dall'adeguamento alle pigioni usuali del quartiere.",
                ]},
                {"heading": "Contestare l'aumento", "paragraphs": [
                    "Il conduttore che ritiene l'aumento ingiustificato può adire l'autorità di conciliazione entro 30 giorni dal ricevimento dell'avviso di aumento (art. 270b CO). Spetta in linea di principio al locatore dimostrare che l'aumento si fonda su uno dei motivi riconosciuti dalla legge.",
                ]},
            ],
            "faq": [
                {"q": "Il mio locatore può aumentare la pigione come vuole?",
                 "a": "No, ogni aumento deve fondarsi su un motivo riconosciuto dalla legge (adeguamento al tasso di riferimento, aumento delle spese, prestazioni supplementari, ecc.) ed essere notificato nelle forme legali."},
                {"q": "Quale documento devo ricevere in caso di aumento della pigione?",
                 "a": "Il modulo ufficiale approvato dal Cantone, indicante la nuova pigione e i motivi dell'aumento (art. 269d CO). Senza questo documento, l'aumento è nullo."},
                {"q": "Entro quale termine posso contestare un aumento della pigione?",
                 "a": "Entro 30 giorni dal ricevimento dell'avviso di aumento, adendo l'autorità di conciliazione competente (art. 270b CO)."},
                {"q": "Una diminuzione del tasso ipotecario di riferimento mi dà diritto a una diminuzione della pigione?",
                 "a": "Se la vostra pigione era stata fissata o aumentata tenendo conto di un tasso ipotecario di riferimento più elevato, una diminuzione di questo tasso può giustificare una richiesta di diminuzione della pigione presso il locatore, eventualmente portata davanti all'autorità di conciliazione in caso di rifiuto."},
            ],
        },
        "en": {
            "slug": "challenging-rent-increase-switzerland",
            "title": "Challenging a rent increase",
            "meta": "Official form, accepted grounds for increase, time limit to challenge: how to challenge a rent increase under the Code of Obligations.",
            "sections": [
                {"heading": "The principle of an abusive rent", "paragraphs": [
                    "Art. 269 CO sets out the principle: rents are abusive when they allow the landlord to obtain an excessive return on the leased property, or result from a manifestly excessive purchase price. It is on this basis that a tenant can challenge a rent increase.",
                ]},
                {"heading": "The form of the increase notice", "paragraphs": [
                    "Any rent increase must be notified using an official form approved by the canton, stating the grounds for the increase (art. 269d CO), at least ten days before the start of the notice period and effective on the next possible termination date. A notice that does not comply with this form is null and void.",
                ]},
                {"heading": "Common grounds for increase", "paragraphs": [
                    "Rent increases are most often justified by adjustment to the reference mortgage rate, an increase in ancillary costs or maintenance costs, additional services provided by the landlord, or, for index-linked leases, changes in the Swiss consumer price index. An increase can also be justified by adjustment to the usual rents in the neighbourhood.",
                ]},
                {"heading": "Challenging the increase", "paragraphs": [
                    "A tenant who considers the increase unjustified can approach the conciliation authority within 30 days of receiving the increase notice (art. 270b CO). It is in principle up to the landlord to show that the increase is based on one of the grounds recognised by law.",
                ]},
            ],
            "faq": [
                {"q": "Can my landlord raise my rent as they please?",
                 "a": "No, any increase must be based on a ground recognised by law (adjustment to the reference rate, higher costs, additional services, etc.) and be notified in the legally required form."},
                {"q": "What document should I receive when my rent is increased?",
                 "a": "The official form approved by the canton, stating the new rent and the grounds for the increase (art. 269d CO). Without this document, the increase is null and void."},
                {"q": "Within what time limit can I challenge a rent increase?",
                 "a": "Within 30 days of receiving the increase notice, by approaching the competent conciliation authority (art. 270b CO)."},
                {"q": "Does a drop in the reference mortgage rate entitle me to a rent reduction?",
                 "a": "If your rent was set or increased taking into account a higher reference mortgage rate, a drop in that rate can justify a request for a rent reduction to your landlord, which can be brought before the conciliation authority if refused."},
            ],
        },
    },
    "defauts-construction-garantie-delais": {
        "domaine_id": "droit_construction",
        "published": "2026-07-30",
        "fr": {
            "slug": "defauts-construction-garantie-delais-reclamation",
            "title": "Défauts de construction : garantie et délais",
            "meta": "Vérification, avis des défauts, délais de prescription : les règles du Code des obligations sur la garantie pour défauts d'un ouvrage.",
            "sections": [
                {"heading": "La vérification de l'ouvrage", "paragraphs": [
                    "Après la livraison d'un ouvrage, le maître doit en vérifier l'état aussitôt qu'il le peut d'après la marche habituelle des affaires, et signaler les défauts découverts à l'entrepreneur (art. 367 CO). Cette obligation de vérification s'applique surtout dans les rapports entre professionnels ; pour un maître d'ouvrage non professionnel, la jurisprudence se montre plus souple.",
                ]},
                {"heading": "L'avis des défauts", "paragraphs": [
                    "Le défaut doit être signalé à l'entrepreneur sans délai dès sa découverte. Un avis tardif peut faire perdre au maître ses droits de garantie, l'ouvrage étant alors réputé accepté avec ce défaut. Les défauts qui ne se manifestent que plus tard doivent être signalés dès leur découverte, même après la réception de l'ouvrage.",
                ]},
                {"heading": "Les droits du maître en cas de défaut", "paragraphs": [
                    "Selon l'art. 368 CO, le maître peut, selon la gravité du défaut, refuser l'ouvrage et demander des dommages-intérêts, exiger une réfection à la charge de l'entrepreneur, ou obtenir une réduction du prix proportionnelle à la moins-value. Le choix entre ces droits dépend de la gravité du défaut et des circonstances.",
                ]},
                {"heading": "Les délais de prescription", "paragraphs": [
                    "Les droits de garantie du maître se prescrivent par deux ans dès la réception de l'ouvrage pour les constructions mobilières, et par cinq ans pour les défauts d'un ouvrage immobilier tel qu'un bâtiment (art. 371 CO, renvoyant à l'art. 210 CO). Un dol de l'entrepreneur prolonge ce délai selon les règles générales de la prescription en cas de dol.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai dois-je signaler un défaut de construction ?",
                 "a": "Sans délai dès sa découverte (art. 367 CO). Un avis tardif risque de faire perdre au maître ses droits de garantie pour ce défaut."},
                {"q": "Quel est le délai de prescription pour un défaut de bâtiment ?",
                 "a": "Cinq ans dès la réception de l'ouvrage pour les constructions immobilières, contre deux ans pour les ouvrages mobiliers (art. 371 CO renvoyant à l'art. 210 CO)."},
                {"q": "Puis-je exiger la réparation du défaut plutôt qu'une réduction de prix ?",
                 "a": "Oui, l'art. 368 CO laisse en principe ce choix au maître selon la gravité du défaut : réfection à la charge de l'entrepreneur, réduction du prix, ou dans les cas graves refus de l'ouvrage avec dommages-intérêts."},
                {"q": "Que se passe-t-il si je ne vérifie pas l'ouvrage à la livraison ?",
                 "a": "L'ouvrage est présumé accepté tel quel pour les défauts qui auraient dû être découverts lors d'une vérification normale, sauf pour les défauts cachés qui ne se manifestent que plus tard et doivent alors être signalés dès leur découverte."},
            ],
        },
        "de": {
            "slug": "baumaengel-garantie-fristen",
            "title": "Baumängel: Garantie und Rügefristen",
            "meta": "Prüfung, Mängelrüge, Verjährungsfristen: die Regeln des Obligationenrechts zur Garantie für Mängel eines Werks.",
            "sections": [
                {"heading": "Die Prüfung des Werks", "paragraphs": [
                    "Nach Ablieferung eines Werks muss der Besteller dessen Beschaffenheit prüfen, sobald es nach dem üblichen Geschäftsgang tunlich ist, und entdeckte Mängel dem Unternehmer anzeigen (Art. 367 OR). Diese Prüfungspflicht gilt vor allem im Verhältnis zwischen Fachleuten; bei einem nicht fachkundigen Besteller zeigt sich die Rechtsprechung grosszügiger.",
                ]},
                {"heading": "Die Mängelrüge", "paragraphs": [
                    "Der Mangel muss dem Unternehmer unverzüglich nach seiner Entdeckung angezeigt werden. Eine verspätete Rüge kann dazu führen, dass der Besteller seine Garantierechte verliert, wobei das Werk dann mit diesem Mangel als genehmigt gilt. Mängel, die sich erst später zeigen, müssen bei ihrer Entdeckung angezeigt werden, auch nach der Abnahme des Werks.",
                ]},
                {"heading": "Die Rechte des Bestellers bei Mängeln", "paragraphs": [
                    "Gemäss Art. 368 OR kann der Besteller, je nach Schwere des Mangels, das Werk ablehnen und Schadenersatz verlangen, eine unentgeltliche Nachbesserung durch den Unternehmer fordern, oder eine dem Minderwert entsprechende Preisminderung erhalten. Die Wahl zwischen diesen Rechten hängt von der Schwere des Mangels und den Umständen ab.",
                ]},
                {"heading": "Die Verjährungsfristen", "paragraphs": [
                    "Die Garantierechte des Bestellers verjähren mit Ablauf von zwei Jahren nach der Abnahme des Werks bei beweglichen Bauwerken, und mit Ablauf von fünf Jahren bei Mängeln eines unbeweglichen Werks wie eines Gebäudes (Art. 371 OR i.V.m. Art. 210 OR). Eine arglistige Täuschung durch den Unternehmer verlängert diese Frist nach den allgemeinen Regeln der Verjährung bei Arglist.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist muss ich einen Baumangel rügen?",
                 "a": "Unverzüglich nach dessen Entdeckung (Art. 367 OR). Eine verspätete Rüge riskiert, dass der Besteller seine Garantierechte für diesen Mangel verliert."},
                {"q": "Wie lange ist die Verjährungsfrist für einen Mangel an einem Gebäude?",
                 "a": "Fünf Jahre ab Abnahme des Werks bei unbeweglichen Bauwerken, gegenüber zwei Jahren bei beweglichen Werken (Art. 371 OR i.V.m. Art. 210 OR)."},
                {"q": "Kann ich die Behebung des Mangels statt einer Preisminderung verlangen?",
                 "a": "Ja, grundsätzlich hat der Besteller je nach Schwere des Mangels die Wahl: Nachbesserung auf Kosten des Unternehmers, Preisminderung, oder in schweren Fällen Ablehnung des Werks mit Schadenersatz (Art. 368 OR)."},
                {"q": "Was geschieht, wenn ich das Werk bei der Ablieferung nicht prüfe?",
                 "a": "Das Werk gilt für Mängel, die bei einer normalen Prüfung hätten entdeckt werden müssen, als genehmigt, ausser bei versteckten Mängeln, die sich erst später zeigen und dann bei ihrer Entdeckung angezeigt werden müssen."},
            ],
        },
        "it": {
            "slug": "difetti-costruzione-garanzia-termini-reclamo",
            "title": "Difetti di costruzione: garanzia e termini",
            "meta": "Verifica, avviso dei difetti, termini di prescrizione: le regole del Codice delle obbligazioni sulla garanzia per i difetti di un'opera.",
            "sections": [
                {"heading": "La verifica dell'opera", "paragraphs": [
                    "Dopo la consegna di un'opera, il committente deve verificarne lo stato appena possibile secondo l'ordinario corso degli affari, e segnalare i difetti scoperti all'appaltatore (art. 367 CO). Questo obbligo di verifica si applica soprattutto nei rapporti tra professionisti; per un committente non professionista, la giurisprudenza si mostra più flessibile.",
                ]},
                {"heading": "L'avviso dei difetti", "paragraphs": [
                    "Il difetto deve essere segnalato all'appaltatore senza indugio dopo la sua scoperta. Un avviso tardivo può far perdere al committente i suoi diritti di garanzia, considerandosi allora l'opera accettata con tale difetto. I difetti che si manifestano solo più tardi devono essere segnalati al momento della loro scoperta, anche dopo la consegna dell'opera.",
                ]},
                {"heading": "I diritti del committente in caso di difetto", "paragraphs": [
                    "Secondo l'art. 368 CO, il committente può, a seconda della gravità del difetto, rifiutare l'opera e chiedere il risarcimento del danno, esigere una riparazione a carico dell'appaltatore, oppure ottenere una riduzione del prezzo proporzionale al minor valore. La scelta tra questi diritti dipende dalla gravità del difetto e dalle circostanze.",
                ]},
                {"heading": "I termini di prescrizione", "paragraphs": [
                    "I diritti di garanzia del committente si prescrivono in due anni dalla consegna dell'opera per le costruzioni mobiliari, e in cinque anni per i difetti di un'opera immobiliare come un edificio (art. 371 CO in rinvio all'art. 210 CO). Un dolo dell'appaltatore prolunga questo termine secondo le regole generali della prescrizione in caso di dolo.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine devo segnalare un difetto di costruzione?",
                 "a": "Senza indugio dopo la sua scoperta (art. 367 CO). Un avviso tardivo rischia di far perdere al committente i suoi diritti di garanzia per tale difetto."},
                {"q": "Qual è il termine di prescrizione per un difetto di un edificio?",
                 "a": "Cinque anni dalla consegna dell'opera per le costruzioni immobiliari, contro due anni per le opere mobiliari (art. 371 CO in rinvio all'art. 210 CO)."},
                {"q": "Posso esigere la riparazione del difetto invece di una riduzione del prezzo?",
                 "a": "Sì, in linea di principio questa scelta spetta al committente secondo la gravità del difetto: riparazione a carico dell'appaltatore, riduzione del prezzo, o nei casi gravi rifiuto dell'opera con risarcimento del danno (art. 368 CO)."},
                {"q": "Cosa succede se non verifico l'opera alla consegna?",
                 "a": "L'opera si presume accettata per i difetti che avrebbero dovuto essere scoperti con una verifica normale, salvo per i difetti occulti che si manifestano solo più tardi e devono allora essere segnalati al momento della loro scoperta."},
            ],
        },
        "en": {
            "slug": "construction-defects-warranty-deadlines",
            "title": "Construction defects: warranty and deadlines",
            "meta": "Inspection, notice of defects, limitation periods: the Code of Obligations rules on warranty for defects in a work.",
            "sections": [
                {"heading": "Inspecting the work", "paragraphs": [
                    "After a work is delivered, the client must inspect its condition as soon as feasible under the ordinary course of business, and notify the contractor of any defects found (art. 367 CO). This inspection duty applies mainly between professionals; courts tend to be more lenient with non-professional clients.",
                ]},
                {"heading": "Notice of defects", "paragraphs": [
                    "A defect must be reported to the contractor without delay upon discovery. Late notice can cause the client to lose their warranty rights, the work then being deemed accepted with that defect. Defects that only appear later must be reported as soon as discovered, even after the work has been accepted.",
                ]},
                {"heading": "The client's rights in case of defect", "paragraphs": [
                    "Under art. 368 CO, depending on the severity of the defect, the client can refuse the work and claim damages, demand free rectification by the contractor, or obtain a price reduction proportional to the loss in value. The choice between these rights depends on the severity of the defect and the circumstances.",
                ]},
                {"heading": "Limitation periods", "paragraphs": [
                    "The client's warranty rights are time-barred after two years from acceptance of the work for movable structures, and after five years for defects in an immovable work such as a building (art. 371 CO referring to art. 210 CO). Fraud by the contractor extends this period under the general rules on limitation in cases of fraud.",
                ]},
            ],
            "faq": [
                {"q": "Within what time limit must I report a construction defect?",
                 "a": "Without delay after discovering it (art. 367 CO). Late notice risks the client losing their warranty rights for that defect."},
                {"q": "What is the limitation period for a defect in a building?",
                 "a": "Five years from acceptance of the work for immovable structures, versus two years for movable works (art. 371 CO referring to art. 210 CO)."},
                {"q": "Can I demand that the defect be fixed rather than a price reduction?",
                 "a": "Yes, in principle this choice is up to the client depending on the severity of the defect: rectification at the contractor's expense, price reduction, or in serious cases refusal of the work with damages (art. 368 CO)."},
                {"q": "What happens if I don't inspect the work upon delivery?",
                 "a": "The work is presumed accepted for defects that should have been found on normal inspection, except for hidden defects that only appear later and must then be reported as soon as discovered."},
            ],
        },
    },
    "hypotheque-legale-artisans-entrepreneurs": {
        "domaine_id": "droit_construction",
        "published": "2026-07-30",
        "fr": {
            "slug": "hypotheque-legale-artisans-entrepreneurs",
            "title": "Hypothèque légale des artisans et entrepreneurs",
            "meta": "Garantie légale pour les travaux de construction non payés, délai d'inscription au registre foncier : ce que prévoit le Code civil.",
            "sections": [
                {"heading": "À quoi sert l'hypothèque légale", "paragraphs": [
                    "L'hypothèque légale des artisans et entrepreneurs (art. 837 ss CC) garantit le paiement des travaux de construction, de transformation ou de démolition effectués sur un bien-fonds. Elle protège l'entreprise qui a fourni des matériaux ou du travail contre le risque de non-paiement, en lui donnant un droit de gage sur l'immeuble lui-même, indépendamment de la solvabilité du maître de l'ouvrage.",
                ]},
                {"heading": "Les conditions d'inscription", "paragraphs": [
                    "L'inscription au registre foncier suppose que les travaux aient effectivement été exécutés et que la créance ne soit pas contestée de manière manifestement infondée. Elle peut être requise même sans l'accord du propriétaire de l'immeuble, ce qui la distingue d'un gage immobilier conventionnel.",
                ]},
                {"heading": "Le délai d'inscription", "paragraphs": [
                    "L'art. 839 al. 2 CC fixe un délai strict : l'inscription doit être requise au plus tard dans les quatre mois qui suivent l'achèvement des travaux. Passé ce délai, le droit à l'hypothèque légale s'éteint, même si la créance pour les travaux elle-même subsiste selon les règles ordinaires de la prescription.",
                ]},
                {"heading": "L'effet vis-à-vis des autres créanciers", "paragraphs": [
                    "Une fois inscrite, l'hypothèque légale prime en principe les autres gages inscrits postérieurement, ce qui en fait un outil de garantie particulièrement efficace pour les entreprises de construction face au risque d'insolvabilité du maître d'ouvrage.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai dois-je requérir l'inscription de l'hypothèque légale ?",
                 "a": "Au plus tard quatre mois après l'achèvement des travaux (art. 839 al. 2 CC). Ce délai est impératif et son dépassement fait perdre le droit à cette garantie."},
                {"q": "Le propriétaire de l'immeuble doit-il donner son accord ?",
                 "a": "Non, l'inscription peut être requise même sans l'accord du propriétaire, à condition que les travaux aient été exécutés et que la créance soit suffisamment établie."},
                {"q": "L'hypothèque légale s'applique-t-elle à tous les types de travaux ?",
                 "a": "Elle s'applique aux travaux de construction, transformation ou démolition d'un bâtiment ou d'autres ouvrages sur un bien-fonds, effectués par des artisans ou entrepreneurs au sens de l'art. 837 CC."},
                {"q": "Que se passe-t-il si le délai de quatre mois est dépassé ?",
                 "a": "Le droit à l'hypothèque légale s'éteint définitivement, mais la créance pour les travaux non payés subsiste et peut être poursuivie par les voies ordinaires (poursuite pour dettes, action en paiement)."},
            ],
        },
        "de": {
            "slug": "bauhandwerkerpfandrecht-handwerker-unternehmer",
            "title": "Bauhandwerkerpfandrecht der Handwerker und Unternehmer",
            "meta": "Gesetzliches Pfandrecht für unbezahlte Bauarbeiten, Eintragungsfrist im Grundbuch: was das Zivilgesetzbuch vorsieht.",
            "sections": [
                {"heading": "Wozu das Bauhandwerkerpfandrecht dient", "paragraphs": [
                    "Das Bauhandwerkerpfandrecht (Art. 837 ff. ZGB) sichert die Bezahlung von Bau-, Umbau- oder Abbrucharbeiten an einem Grundstück. Es schützt das Unternehmen, das Material oder Arbeit geliefert hat, gegen das Risiko der Nichtzahlung, indem es ihm ein Pfandrecht am Grundstück selbst einräumt, unabhängig von der Zahlungsfähigkeit des Bauherrn.",
                ]},
                {"heading": "Die Eintragungsvoraussetzungen", "paragraphs": [
                    "Die Eintragung im Grundbuch setzt voraus, dass die Arbeiten tatsächlich ausgeführt wurden und die Forderung nicht offensichtlich unbegründet bestritten wird. Sie kann selbst ohne Zustimmung der Grundeigentümerin oder des Grundeigentümers verlangt werden, was sie von einem vertraglichen Grundpfandrecht unterscheidet.",
                ]},
                {"heading": "Die Eintragungsfrist", "paragraphs": [
                    "Art. 839 Abs. 2 ZGB setzt eine strenge Frist: die Eintragung muss spätestens innert vier Monaten nach Vollendung der Arbeiten verlangt werden. Nach Ablauf dieser Frist erlischt der Anspruch auf das Bauhandwerkerpfandrecht, auch wenn die Forderung für die Arbeiten selbst nach den ordentlichen Verjährungsregeln fortbesteht.",
                ]},
                {"heading": "Die Wirkung gegenüber anderen Gläubigern", "paragraphs": [
                    "Einmal eingetragen, geht das Bauhandwerkerpfandrecht grundsätzlich später eingetragenen Pfandrechten vor, was es zu einem besonders wirksamen Sicherungsinstrument für Bauunternehmen gegenüber dem Insolvenzrisiko des Bauherrn macht.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist muss ich die Eintragung des Bauhandwerkerpfandrechts verlangen?",
                 "a": "Spätestens vier Monate nach Vollendung der Arbeiten (Art. 839 Abs. 2 ZGB). Diese Frist ist zwingend, und ihre Überschreitung führt zum Verlust des Anspruchs auf diese Sicherheit."},
                {"q": "Muss die Grundeigentümerin oder der Grundeigentümer zustimmen?",
                 "a": "Nein, die Eintragung kann auch ohne Zustimmung verlangt werden, sofern die Arbeiten ausgeführt wurden und die Forderung hinreichend belegt ist."},
                {"q": "Gilt das Bauhandwerkerpfandrecht für alle Arten von Arbeiten?",
                 "a": "Es gilt für Bau-, Umbau- oder Abbrucharbeiten an einem Gebäude oder anderen Bauwerken auf einem Grundstück, ausgeführt durch Handwerker oder Unternehmer im Sinne von Art. 837 ZGB."},
                {"q": "Was geschieht bei Überschreitung der Viermonatsfrist?",
                 "a": "Der Anspruch auf das Bauhandwerkerpfandrecht erlischt endgültig, doch die Forderung für die unbezahlten Arbeiten bleibt bestehen und kann auf ordentlichem Weg geltend gemacht werden (Betreibung, Zahlungsklage)."},
            ],
        },
        "it": {
            "slug": "ipoteca-legale-artigiani-imprenditori",
            "title": "Ipoteca legale degli artigiani e imprenditori",
            "meta": "Garanzia legale per i lavori di costruzione non pagati, termine di iscrizione nel registro fondiario: quanto previsto dal Codice civile.",
            "sections": [
                {"heading": "A cosa serve l'ipoteca legale", "paragraphs": [
                    "L'ipoteca legale degli artigiani e imprenditori (art. 837 segg. CC) garantisce il pagamento dei lavori di costruzione, trasformazione o demolizione eseguiti su un fondo. Protegge l'impresa che ha fornito materiali o lavoro contro il rischio di mancato pagamento, concedendole un diritto di pegno sull'immobile stesso, indipendentemente dalla solvibilità del committente.",
                ]},
                {"heading": "Le condizioni d'iscrizione", "paragraphs": [
                    "L'iscrizione nel registro fondiario presuppone che i lavori siano stati effettivamente eseguiti e che il credito non sia manifestamente infondato. Può essere richiesta anche senza il consenso del proprietario dell'immobile, il che la distingue da un pegno immobiliare convenzionale.",
                ]},
                {"heading": "Il termine d'iscrizione", "paragraphs": [
                    "L'art. 839 cpv. 2 CC fissa un termine rigoroso: l'iscrizione deve essere richiesta al più tardi entro quattro mesi dal compimento dei lavori. Trascorso questo termine, il diritto all'ipoteca legale si estingue, anche se il credito per i lavori stessi permane secondo le regole ordinarie della prescrizione.",
                ]},
                {"heading": "L'effetto verso gli altri creditori", "paragraphs": [
                    "Una volta iscritta, l'ipoteca legale prevale in linea di principio sugli altri pegni iscritti successivamente, il che ne fa uno strumento di garanzia particolarmente efficace per le imprese di costruzione di fronte al rischio d'insolvenza del committente.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine devo richiedere l'iscrizione dell'ipoteca legale?",
                 "a": "Al più tardi quattro mesi dopo il compimento dei lavori (art. 839 cpv. 2 CC). Questo termine è imperativo e il suo superamento fa perdere il diritto a questa garanzia."},
                {"q": "Il proprietario dell'immobile deve dare il suo consenso?",
                 "a": "No, l'iscrizione può essere richiesta anche senza il consenso del proprietario, a condizione che i lavori siano stati eseguiti e il credito sia sufficientemente comprovato."},
                {"q": "L'ipoteca legale si applica a tutti i tipi di lavori?",
                 "a": "Si applica ai lavori di costruzione, trasformazione o demolizione di un edificio o di altre opere su un fondo, eseguiti da artigiani o imprenditori ai sensi dell'art. 837 CC."},
                {"q": "Cosa succede se il termine di quattro mesi è superato?",
                 "a": "Il diritto all'ipoteca legale si estingue definitivamente, ma il credito per i lavori non pagati permane e può essere fatto valere per le vie ordinarie (esecuzione, azione di pagamento)."},
            ],
        },
        "en": {
            "slug": "statutory-lien-tradespeople-contractors",
            "title": "Statutory lien of tradespeople and contractors",
            "meta": "Statutory security for unpaid construction work, deadline to register with the land registry: what the Civil Code provides.",
            "sections": [
                {"heading": "The purpose of the statutory lien", "paragraphs": [
                    "The statutory lien of tradespeople and contractors (art. 837 ff. CC) secures payment for construction, alteration or demolition work carried out on a plot of land. It protects the business that supplied materials or labour against the risk of non-payment, by granting it a lien on the property itself, regardless of the client's solvency.",
                ]},
                {"heading": "Conditions for registration", "paragraphs": [
                    "Registration in the land registry requires that the work has actually been carried out and that the claim is not manifestly unfounded. It can be requested even without the property owner's consent, which distinguishes it from a conventional mortgage.",
                ]},
                {"heading": "The registration deadline", "paragraphs": [
                    "Art. 839 para. 2 CC sets a strict deadline: registration must be requested at the latest within four months of completion of the work. After this period, the right to the statutory lien lapses, even though the claim for the work itself remains under the ordinary limitation rules.",
                ]},
                {"heading": "Effect against other creditors", "paragraphs": [
                    "Once registered, the statutory lien in principle takes priority over other liens registered later, making it a particularly effective security tool for construction businesses facing the risk of a client's insolvency.",
                ]},
            ],
            "faq": [
                {"q": "Within what deadline must I request registration of the statutory lien?",
                 "a": "At the latest four months after completion of the work (art. 839 para. 2 CC). This deadline is mandatory, and missing it means losing the right to this security."},
                {"q": "Does the property owner need to consent?",
                 "a": "No, registration can be requested even without the owner's consent, provided the work was carried out and the claim is sufficiently substantiated."},
                {"q": "Does the statutory lien apply to all types of work?",
                 "a": "It applies to construction, alteration or demolition work on a building or other structure on a plot of land, carried out by tradespeople or contractors within the meaning of art. 837 CC."},
                {"q": "What happens if the four-month deadline is missed?",
                 "a": "The right to the statutory lien lapses permanently, but the claim for unpaid work remains and can be pursued through ordinary means (debt collection, payment action)."},
            ],
        },
    },
    "reserve-hereditaire-quotite-disponible": {
        "domaine_id": "droit_successions",
        "published": "2026-07-30",
        "fr": {
            "slug": "reserve-hereditaire-quotite-disponible-2023",
            "title": "Réserve héréditaire et quotité disponible depuis 2023",
            "meta": "Réserves des héritiers, part disponible du défunt, changements de la révision du droit successoral entrée en vigueur en 2023.",
            "sections": [
                {"heading": "Le principe de la réserve héréditaire", "paragraphs": [
                    "Le droit suisse protège certains héritiers proches par une réserve héréditaire : une part minimale de la succession qui leur revient et dont le défunt ne peut pas les priver, sauf exception légale telle que l'exhérédation pour justes motifs (art. 470 ss CC).",
                ]},
                {"heading": "Ce qui a changé au 1er janvier 2023", "paragraphs": [
                    "La révision du droit des successions entrée en vigueur le 1er janvier 2023 a réduit les réserves héréditaires afin d'élargir la liberté de disposer du défunt. La réserve des descendants est passée des trois quarts à la moitié de leur droit légal, et la réserve des parents a été supprimée. La réserve du conjoint ou du partenaire enregistré reste fixée à la moitié de son droit légal.",
                ]},
                {"heading": "La quotité disponible", "paragraphs": [
                    "La quotité disponible est la part de la succession dont le défunt peut librement disposer, par testament ou pacte successoral, en faveur de qui il souhaite : une autre personne, une fondation, ou un héritier légal au-delà de sa part réservataire. Avec la réduction des réserves en 2023, cette quotité disponible s'est mécaniquement élargie.",
                ]},
                {"heading": "L'action en réduction", "paragraphs": [
                    "Un héritier réservataire dont la réserve a été entamée par des libéralités du défunt peut agir en réduction (art. 522 ss CC) pour faire ramener ces libéralités dans les limites de la quotité disponible. Cette action se prescrit par des délais spécifiques dès l'ouverture de la succession.",
                ]},
            ],
            "faq": [
                {"q": "Quels héritiers ont droit à une réserve héréditaire ?",
                 "a": "Depuis 2023, les descendants et le conjoint ou partenaire enregistré survivant. La réserve des parents du défunt a été supprimée par la révision entrée en vigueur le 1er janvier 2023."},
                {"q": "Quelle est la réserve des descendants depuis 2023 ?",
                 "a": "La moitié de leur droit de succession légal, contre trois quarts avant la révision entrée en vigueur le 1er janvier 2023 (art. 471 CC)."},
                {"q": "Puis-je déshériter complètement mon enfant ?",
                 "a": "En principe non, sauf motif d'exhérédation reconnu par la loi (art. 477 CC), comme une infraction grave envers le défunt. En dehors de ces cas, la réserve héréditaire de l'enfant doit être respectée."},
                {"q": "Que puis-je faire si ma réserve n'a pas été respectée ?",
                 "a": "Vous pouvez intenter une action en réduction (art. 522 ss CC) pour faire ramener les libéralités excessives dans les limites de la quotité disponible, dans les délais de prescription applicables."},
            ],
        },
        "de": {
            "slug": "pflichtteil-verfuegbare-quote-seit-2023",
            "title": "Pflichtteil und verfügbare Quote seit 2023",
            "meta": "Pflichtteile der Erben, verfügbarer Teil des Erblassers, Änderungen durch die 2023 in Kraft getretene Erbrechtsrevision.",
            "sections": [
                {"heading": "Der Grundsatz des Pflichtteils", "paragraphs": [
                    "Das schweizerische Recht schützt bestimmte nahe Erben durch einen Pflichtteil: einen Mindestanteil am Nachlass, der ihnen zusteht und den der Erblasser ihnen nicht entziehen kann, ausser in gesetzlichen Ausnahmefällen wie der Enterbung aus wichtigen Gründen (Art. 470 ff. ZGB).",
                ]},
                {"heading": "Was sich am 1. Januar 2023 geändert hat", "paragraphs": [
                    "Die am 1. Januar 2023 in Kraft getretene Revision des Erbrechts hat die Pflichtteile verkleinert, um die Verfügungsfreiheit des Erblassers zu erweitern. Der Pflichtteil der Nachkommen sank von drei Vierteln auf die Hälfte ihres gesetzlichen Erbanspruchs, und der Pflichtteil der Eltern wurde abgeschafft. Der Pflichtteil des überlebenden Ehegatten oder der eingetragenen Partnerin bzw. des eingetragenen Partners bleibt bei der Hälfte ihres gesetzlichen Anspruchs.",
                ]},
                {"heading": "Die verfügbare Quote", "paragraphs": [
                    "Die verfügbare Quote ist der Teil des Nachlasses, über den der Erblasser frei verfügen kann, durch Testament oder Erbvertrag, zugunsten wer auch immer er möchte: eine andere Person, eine Stiftung, oder einen gesetzlichen Erben über seinen Pflichtteil hinaus. Mit der Verkleinerung der Pflichtteile 2023 hat sich diese verfügbare Quote automatisch vergrössert.",
                ]},
                {"heading": "Die Herabsetzungsklage", "paragraphs": [
                    "Ein pflichtteilsgeschützter Erbe, dessen Pflichtteil durch Zuwendungen des Erblassers verletzt wurde, kann Herabsetzungsklage erheben (Art. 522 ff. ZGB), um diese Zuwendungen auf das Mass der verfügbaren Quote zurückzuführen. Diese Klage verjährt innert bestimmter Fristen ab Eröffnung des Erbgangs.",
                ]},
            ],
            "faq": [
                {"q": "Welche Erben haben Anspruch auf einen Pflichtteil?",
                 "a": "Seit 2023 die Nachkommen sowie der überlebende Ehegatte oder die eingetragene Partnerin bzw. der eingetragene Partner. Der Pflichtteil der Eltern des Erblassers wurde durch die am 1. Januar 2023 in Kraft getretene Revision abgeschafft."},
                {"q": "Wie gross ist der Pflichtteil der Nachkommen seit 2023?",
                 "a": "Die Hälfte ihres gesetzlichen Erbanspruchs, gegenüber drei Vierteln vor der am 1. Januar 2023 in Kraft getretenen Revision (Art. 471 ZGB)."},
                {"q": "Kann ich mein Kind vollständig enterben?",
                 "a": "Grundsätzlich nicht, ausser bei einem gesetzlich anerkannten Enterbungsgrund (Art. 477 ZGB), etwa einer schweren Straftat gegenüber dem Erblasser. Ausserhalb dieser Fälle muss der Pflichtteil des Kindes respektiert werden."},
                {"q": "Was kann ich tun, wenn mein Pflichtteil nicht respektiert wurde?",
                 "a": "Sie können Herabsetzungsklage erheben (Art. 522 ff. ZGB), um übermässige Zuwendungen auf das Mass der verfügbaren Quote zurückzuführen, innert der geltenden Verjährungsfristen."},
            ],
        },
        "it": {
            "slug": "legittima-quota-disponibile-2023",
            "title": "Legittima e quota disponibile dal 2023",
            "meta": "Riserve degli eredi, quota disponibile del defunto, cambiamenti della revisione del diritto successorio entrata in vigore nel 2023.",
            "sections": [
                {"heading": "Il principio della legittima", "paragraphs": [
                    "Il diritto svizzero protegge determinati eredi stretti mediante una legittima: una quota minima della successione che spetta loro e di cui il defunto non può privarli, salvo eccezione legale come la diseredazione per motivi gravi (art. 470 segg. CC).",
                ]},
                {"heading": "Cosa è cambiato il 1° gennaio 2023", "paragraphs": [
                    "La revisione del diritto successorio entrata in vigore il 1° gennaio 2023 ha ridotto le legittime per ampliare la libertà di disporre del defunto. La legittima dei discendenti è passata da tre quarti alla metà del loro diritto successorio legale, e la legittima dei genitori è stata soppressa. La legittima del coniuge o del partner registrato superstite resta fissata alla metà del suo diritto legale.",
                ]},
                {"heading": "La quota disponibile", "paragraphs": [
                    "La quota disponibile è la parte della successione di cui il defunto può disporre liberamente, per testamento o contratto successorio, a favore di chi desidera: un'altra persona, una fondazione, o un erede legale oltre la sua quota legittima. Con la riduzione delle legittime nel 2023, questa quota disponibile si è meccanicamente ampliata.",
                ]},
                {"heading": "L'azione di riduzione", "paragraphs": [
                    "Un erede legittimario la cui legittima è stata lesa da liberalità del defunto può promuovere un'azione di riduzione (art. 522 segg. CC) per far ricondurre tali liberalità entro i limiti della quota disponibile. Questa azione si prescrive entro termini specifici dall'apertura della successione.",
                ]},
            ],
            "faq": [
                {"q": "Quali eredi hanno diritto a una legittima?",
                 "a": "Dal 2023, i discendenti e il coniuge o partner registrato superstite. La legittima dei genitori del defunto è stata soppressa dalla revisione entrata in vigore il 1° gennaio 2023."},
                {"q": "Qual è la legittima dei discendenti dal 2023?",
                 "a": "La metà del loro diritto successorio legale, contro tre quarti prima della revisione entrata in vigore il 1° gennaio 2023 (art. 471 CC)."},
                {"q": "Posso diseredare completamente mio figlio?",
                 "a": "In linea di principio no, salvo un motivo di diseredazione riconosciuto dalla legge (art. 477 CC), come un reato grave verso il defunto. Al di fuori di questi casi, la legittima del figlio deve essere rispettata."},
                {"q": "Cosa posso fare se la mia legittima non è stata rispettata?",
                 "a": "Potete promuovere un'azione di riduzione (art. 522 segg. CC) per far ricondurre le liberalità eccessive entro i limiti della quota disponibile, entro i termini di prescrizione applicabili."},
            ],
        },
        "en": {
            "slug": "forced-heirship-disposable-portion-2023",
            "title": "Forced heirship and disposable portion since 2023",
            "meta": "Statutory reserves for heirs, the disposable portion of an estate, changes from the inheritance law reform in force since 2023.",
            "sections": [
                {"heading": "The principle of forced heirship", "paragraphs": [
                    "Swiss law protects certain close heirs through a statutory reserve: a minimum share of the estate that belongs to them and which the deceased cannot take away, except in legal exceptions such as disinheritance for good cause (art. 470 ff. CC).",
                ]},
                {"heading": "What changed on 1 January 2023", "paragraphs": [
                    "The inheritance law reform that entered into force on 1 January 2023 reduced statutory reserves to expand the deceased's freedom to dispose of their estate. The descendants' reserve dropped from three-quarters to half of their statutory inheritance share, and the parents' reserve was abolished. The surviving spouse's or registered partner's reserve remains at half of their statutory share.",
                ]},
                {"heading": "The disposable portion", "paragraphs": [
                    "The disposable portion is the share of the estate the deceased may freely dispose of, by will or inheritance contract, in favour of whoever they wish: another person, a foundation, or a statutory heir beyond their reserved share. With the reduction of reserves in 2023, this disposable portion automatically expanded.",
                ]},
                {"heading": "The action for abatement", "paragraphs": [
                    "A forced heir whose reserve has been infringed by gifts from the deceased can bring an action for abatement (art. 522 ff. CC) to bring those gifts back within the limits of the disposable portion. This action is time-barred within specific periods from the opening of the estate.",
                ]},
            ],
            "faq": [
                {"q": "Which heirs are entitled to a statutory reserve?",
                 "a": "Since 2023, descendants and the surviving spouse or registered partner. The parents' reserve was abolished by the reform that entered into force on 1 January 2023."},
                {"q": "What is the descendants' reserve since 2023?",
                 "a": "Half of their statutory inheritance share, down from three-quarters before the reform that entered into force on 1 January 2023 (art. 471 CC)."},
                {"q": "Can I completely disinherit my child?",
                 "a": "In principle no, except for a ground of disinheritance recognised by law (art. 477 CC), such as a serious offence against the deceased. Outside these cases, the child's statutory reserve must be respected."},
                {"q": "What can I do if my reserve was not respected?",
                 "a": "You can bring an action for abatement (art. 522 ff. CC) to bring excessive gifts back within the limits of the disposable portion, within the applicable limitation periods."},
            ],
        },
    },
    "rediger-testament-valable": {
        "domaine_id": "droit_successions",
        "published": "2026-07-30",
        "fr": {
            "slug": "rediger-testament-valable-droit-suisse",
            "title": "Rédiger un testament valable en droit suisse",
            "meta": "Testament olographe, testament public, formes légales et conditions de validité selon le Code civil.",
            "sections": [
                {"heading": "Les formes de testament reconnues", "paragraphs": [
                    "Le droit suisse reconnaît principalement deux formes de testament : le testament olographe, rédigé entièrement à la main par le testateur, daté et signé par lui (art. 505 CC), et le testament public, dressé par un officier public avec le concours de deux témoins (art. 499 ss CC). Une troisième forme, le testament oral, n'est admise que dans des circonstances extraordinaires (art. 506 CC).",
                ]},
                {"heading": "Les conditions du testament olographe", "paragraphs": [
                    "Pour être valable, le testament olographe doit être écrit intégralement de la main du testateur : un texte tapé à l'ordinateur puis simplement signé n'est pas valable, même si le contenu reflète fidèlement la volonté du défunt. Il doit indiquer le jour, le mois et l'année de sa rédaction, et porter la signature du testateur.",
                ]},
                {"heading": "La capacité de discernement", "paragraphs": [
                    "Le testateur doit avoir l'exercice des droits civils, c'est-à-dire être capable de discernement au moment de la rédaction (art. 467 CC). Un testament rédigé par une personne durablement incapable de discernement peut être annulé par une action en nullité intentée par un héritier ou toute personne intéressée.",
                ]},
                {"heading": "La conservation et l'ouverture du testament", "paragraphs": [
                    "Un testament peut être déposé auprès d'un office compétent ou conservé par le testateur lui-même. À son décès, le testament doit être remis à l'autorité compétente, qui procède à son ouverture et informe les héritiers et légataires de son contenu.",
                ]},
            ],
            "faq": [
                {"q": "Un testament tapé à l'ordinateur et signé est-il valable ?",
                 "a": "Non, un testament olographe doit être écrit entièrement à la main (art. 505 CC). Un texte tapé à l'ordinateur n'est valable que sous la forme du testament public, dressé par un officier public."},
                {"q": "Que doit contenir un testament olographe pour être valable ?",
                 "a": "Il doit être écrit entièrement de la main du testateur, daté avec le jour, le mois et l'année, et signé par lui (art. 505 CC)."},
                {"q": "Puis-je modifier mon testament après l'avoir rédigé ?",
                 "a": "Oui, un testament peut être révoqué ou modifié à tout moment par le testateur tant qu'il conserve sa capacité de discernement, notamment en rédigeant un nouveau testament ou en détruisant l'ancien."},
                {"q": "Où puis-je conserver mon testament en toute sécurité ?",
                 "a": "Vous pouvez le conserver vous-même, le confier à une personne de confiance, ou le déposer auprès d'un office compétent (notaire ou autorité cantonale selon le canton), ce qui réduit le risque de perte ou de destruction."},
            ],
        },
        "de": {
            "slug": "gueltiges-testament-verfassen-schweizer-recht",
            "title": "Ein gültiges Testament nach Schweizer Recht verfassen",
            "meta": "Eigenhändiges Testament, öffentliches Testament, gesetzliche Formvorschriften gemäss Zivilgesetzbuch.",
            "sections": [
                {"heading": "Die anerkannten Testamentsformen", "paragraphs": [
                    "Das schweizerische Recht kennt hauptsächlich zwei Testamentsformen: das eigenhändige Testament, das vollständig von Hand geschrieben, datiert und von der erblassenden Person unterzeichnet wird (Art. 505 ZGB), und das öffentliche Testament, das von einer Urkundsperson unter Mitwirkung zweier Zeuginnen oder Zeugen errichtet wird (Art. 499 ff. ZGB). Eine dritte Form, das mündliche Testament, ist nur unter ausserordentlichen Umständen zulässig (Art. 506 ZGB).",
                ]},
                {"heading": "Die Voraussetzungen des eigenhändigen Testaments", "paragraphs": [
                    "Um gültig zu sein, muss das eigenhändige Testament vollständig von Hand der erblassenden Person geschrieben werden: ein am Computer getippter und lediglich unterschriebener Text ist nicht gültig, selbst wenn der Inhalt den Willen der verstorbenen Person getreu wiedergibt. Es muss Tag, Monat und Jahr der Errichtung angeben und die Unterschrift der erblassenden Person tragen.",
                ]},
                {"heading": "Die Urteilsfähigkeit", "paragraphs": [
                    "Die erblassende Person muss handlungsfähig sein, das heisst im Zeitpunkt der Errichtung urteilsfähig (Art. 467 ZGB). Ein von einer dauernd urteilsunfähigen Person verfasstes Testament kann durch eine Ungültigkeitsklage einer Erbin, eines Erben oder jeder interessierten Person angefochten werden.",
                ]},
                {"heading": "Die Aufbewahrung und Eröffnung des Testaments", "paragraphs": [
                    "Ein Testament kann bei einer zuständigen Stelle hinterlegt oder von der erblassenden Person selbst aufbewahrt werden. Bei ihrem Tod muss das Testament der zuständigen Behörde übergeben werden, welche es eröffnet und die Erbinnen und Erben sowie Vermächtnisnehmerinnen und Vermächtnisnehmer über seinen Inhalt informiert.",
                ]},
            ],
            "faq": [
                {"q": "Ist ein am Computer getipptes und unterschriebenes Testament gültig?",
                 "a": "Nein, ein eigenhändiges Testament muss vollständig von Hand geschrieben werden (Art. 505 ZGB). Ein am Computer getippter Text ist nur in der Form des öffentlichen Testaments gültig, errichtet von einer Urkundsperson."},
                {"q": "Was muss ein eigenhändiges Testament enthalten, um gültig zu sein?",
                 "a": "Es muss vollständig von Hand der erblassenden Person geschrieben, mit Tag, Monat und Jahr datiert und von ihr unterschrieben sein (Art. 505 ZGB)."},
                {"q": "Kann ich mein Testament nach der Errichtung ändern?",
                 "a": "Ja, ein Testament kann von der erblassenden Person jederzeit widerrufen oder geändert werden, solange sie urteilsfähig bleibt, namentlich durch Errichtung eines neuen Testaments oder Vernichtung des alten."},
                {"q": "Wo kann ich mein Testament sicher aufbewahren?",
                 "a": "Sie können es selbst aufbewahren, einer Vertrauensperson anvertrauen, oder bei einer zuständigen Stelle hinterlegen (Notariat oder kantonale Behörde je nach Kanton), was das Risiko eines Verlusts oder einer Vernichtung verringert."},
            ],
        },
        "it": {
            "slug": "redigere-testamento-valido-diritto-svizzero",
            "title": "Redigere un testamento valido secondo il diritto svizzero",
            "meta": "Testamento olografo, testamento pubblico, forme legali e condizioni di validità secondo il Codice civile.",
            "sections": [
                {"heading": "Le forme di testamento riconosciute", "paragraphs": [
                    "Il diritto svizzero riconosce principalmente due forme di testamento: il testamento olografo, redatto interamente a mano dal testatore, datato e firmato da lui (art. 505 CC), e il testamento pubblico, allestito da un pubblico ufficiale con il concorso di due testimoni (art. 499 segg. CC). Una terza forma, il testamento orale, è ammessa solo in circostanze straordinarie (art. 506 CC).",
                ]},
                {"heading": "Le condizioni del testamento olografo", "paragraphs": [
                    "Per essere valido, il testamento olografo deve essere scritto interamente a mano dal testatore: un testo digitato al computer e semplicemente firmato non è valido, anche se il contenuto riflette fedelmente la volontà del defunto. Deve indicare il giorno, il mese e l'anno della redazione, e recare la firma del testatore.",
                ]},
                {"heading": "La capacità di discernimento", "paragraphs": [
                    "Il testatore deve avere l'esercizio dei diritti civili, ossia essere capace di discernimento al momento della redazione (art. 467 CC). Un testamento redatto da una persona durevolmente incapace di discernimento può essere annullato mediante un'azione di nullità promossa da un erede o da qualsiasi persona interessata.",
                ]},
                {"heading": "La conservazione e l'apertura del testamento", "paragraphs": [
                    "Un testamento può essere depositato presso un ufficio competente o conservato dal testatore stesso. Alla sua morte, il testamento deve essere consegnato all'autorità competente, che procede alla sua apertura e informa gli eredi e i legatari del suo contenuto.",
                ]},
            ],
            "faq": [
                {"q": "Un testamento digitato al computer e firmato è valido?",
                 "a": "No, un testamento olografo deve essere scritto interamente a mano (art. 505 CC). Un testo digitato al computer è valido solo nella forma del testamento pubblico, allestito da un pubblico ufficiale."},
                {"q": "Cosa deve contenere un testamento olografo per essere valido?",
                 "a": "Deve essere scritto interamente a mano dal testatore, datato con giorno, mese e anno, e firmato da lui (art. 505 CC)."},
                {"q": "Posso modificare il mio testamento dopo averlo redatto?",
                 "a": "Sì, un testamento può essere revocato o modificato in qualsiasi momento dal testatore finché conserva la capacità di discernimento, in particolare redigendo un nuovo testamento o distruggendo quello vecchio."},
                {"q": "Dove posso conservare il mio testamento in sicurezza?",
                 "a": "Potete conservarlo voi stessi, affidarlo a una persona di fiducia, o depositarlo presso un ufficio competente (notaio o autorità cantonale a seconda del Cantone), il che riduce il rischio di perdita o distruzione."},
            ],
        },
        "en": {
            "slug": "drafting-valid-will-swiss-law",
            "title": "Drafting a valid will under Swiss law",
            "meta": "Holographic will, public will, legal formalities and conditions of validity under the Civil Code.",
            "sections": [
                {"heading": "Recognised forms of will", "paragraphs": [
                    "Swiss law mainly recognises two forms of will: the holographic will, written entirely by hand by the testator, dated and signed by them (art. 505 CC), and the public will, drawn up by a public official with the involvement of two witnesses (art. 499 ff. CC). A third form, the oral will, is only permitted in extraordinary circumstances (art. 506 CC).",
                ]},
                {"heading": "Requirements for a holographic will", "paragraphs": [
                    "To be valid, a holographic will must be written entirely by the testator's own hand: a typed text that is merely signed is not valid, even if its content faithfully reflects the deceased's wishes. It must state the day, month and year it was drawn up, and bear the testator's signature.",
                ]},
                {"heading": "Capacity of judgment", "paragraphs": [
                    "The testator must have full legal capacity, meaning capacity of judgment at the time the will is drawn up (art. 467 CC). A will drafted by a person who was permanently incapable of judgment can be challenged through an action for annulment brought by an heir or any interested person.",
                ]},
                {"heading": "Safekeeping and opening the will", "paragraphs": [
                    "A will can be deposited with a competent office or kept by the testator themselves. On their death, the will must be handed to the competent authority, which opens it and informs the heirs and legatees of its contents.",
                ]},
            ],
            "faq": [
                {"q": "Is a typed and signed will valid?",
                 "a": "No, a holographic will must be written entirely by hand (art. 505 CC). A typed text is only valid in the form of a public will, drawn up by a public official."},
                {"q": "What must a holographic will contain to be valid?",
                 "a": "It must be written entirely by the testator's own hand, dated with the day, month and year, and signed by them (art. 505 CC)."},
                {"q": "Can I change my will after drafting it?",
                 "a": "Yes, a will can be revoked or amended at any time by the testator as long as they retain capacity of judgment, in particular by drafting a new will or destroying the old one."},
                {"q": "Where can I safely keep my will?",
                 "a": "You can keep it yourself, entrust it to a trusted person, or deposit it with a competent office (a notary or cantonal authority depending on the canton), which reduces the risk of loss or destruction."},
            ],
        },
    },
    "resilier-contrat-justes-motifs": {
        "domaine_id": "droit_contrats",
        "published": "2026-07-30",
        "fr": {
            "slug": "resilier-contrat-justes-motifs-suisse",
            "title": "Résilier un contrat pour justes motifs",
            "meta": "Résiliation immédiate d'un contrat de durée, conditions reconnues par la jurisprudence, effets sur les dommages-intérêts.",
            "sections": [
                {"heading": "Un principe général non codifié uniformément", "paragraphs": [
                    "Le droit suisse des obligations ne contient pas de règle unique sur la résiliation pour justes motifs applicable à tous les contrats : certains contrats nommés prévoient une règle explicite, comme le contrat de travail (art. 337 CO) ou le mandat (art. 404 CO), tandis que pour d'autres contrats de durée, la jurisprudence du Tribunal fédéral a dégagé un principe général permettant une résiliation immédiate lorsque la poursuite du contrat devient insupportable pour une partie.",
                ]},
                {"heading": "Ce qui constitue un juste motif", "paragraphs": [
                    "Un juste motif suppose généralement une violation grave des obligations contractuelles par l'autre partie, une rupture du lien de confiance essentiel au contrat, ou des circonstances rendant la poursuite de la relation contractuelle objectivement insupportable selon les règles de la bonne foi. L'appréciation se fait au cas par cas, en tenant compte de la nature du contrat et de la gravité des faits invoqués.",
                ]},
                {"heading": "Les conséquences d'une résiliation immédiate", "paragraphs": [
                    "Une résiliation pour justes motifs met fin au contrat avec effet immédiat, sans respecter les délais de résiliation ordinaires. Si les justes motifs invoqués ne sont pas reconnus comme suffisants par un tribunal, la partie qui a résilié s'expose au paiement de dommages-intérêts pour résiliation injustifiée, calculés selon les règles propres au type de contrat concerné.",
                ]},
            ],
            "faq": [
                {"q": "Tout contrat peut-il être résilié pour justes motifs ?",
                 "a": "Les contrats de durée (bail, travail, mandat, société simple, etc.) s'y prêtent particulièrement. Pour les contrats sans règle légale explicite, la jurisprudence du Tribunal fédéral admet ce principe à des conditions strictes."},
                {"q": "Que risque-t-on si les justes motifs invoqués ne sont pas reconnus ?",
                 "a": "La résiliation immédiate peut être considérée comme injustifiée, exposant la partie qui l'a prononcée à des dommages-intérêts envers son cocontractant, selon les règles applicables au type de contrat en cause."},
                {"q": "Faut-il notifier les justes motifs par écrit ?",
                 "a": "La loi n'impose pas toujours une forme écrite selon le type de contrat, mais un écrit motivé est fortement recommandé pour pouvoir prouver la réalité et la gravité des motifs invoqués en cas de litige."},
            ],
        },
        "de": {
            "slug": "vertrag-kuendigen-wichtige-gruende",
            "title": "Einen Vertrag aus wichtigen Gründen kündigen",
            "meta": "Fristlose Kündigung eines Dauervertrags, von der Rechtsprechung anerkannte Voraussetzungen, Folgen für Schadenersatz.",
            "sections": [
                {"heading": "Ein allgemeiner, nicht einheitlich kodifizierter Grundsatz", "paragraphs": [
                    "Das schweizerische Obligationenrecht enthält keine für alle Verträge einheitliche Regel zur Kündigung aus wichtigen Gründen: bestimmte benannte Verträge sehen eine ausdrückliche Regel vor, wie der Arbeitsvertrag (Art. 337 OR) oder der Auftrag (Art. 404 OR), während für andere Dauerverträge die Rechtsprechung des Bundesgerichts einen allgemeinen Grundsatz entwickelt hat, der eine fristlose Kündigung erlaubt, wenn die Fortsetzung des Vertrags für eine Partei unzumutbar wird.",
                ]},
                {"heading": "Was einen wichtigen Grund darstellt", "paragraphs": [
                    "Ein wichtiger Grund setzt in der Regel eine schwere Verletzung der vertraglichen Pflichten durch die andere Partei, einen Bruch des für den Vertrag wesentlichen Vertrauensverhältnisses, oder Umstände voraus, die die Fortsetzung der Vertragsbeziehung nach Treu und Glauben objektiv unzumutbar machen. Die Beurteilung erfolgt im Einzelfall, unter Berücksichtigung der Art des Vertrags und der Schwere der geltend gemachten Tatsachen.",
                ]},
                {"heading": "Die Folgen einer fristlosen Kündigung", "paragraphs": [
                    "Eine Kündigung aus wichtigen Gründen beendet den Vertrag mit sofortiger Wirkung, ohne die ordentlichen Kündigungsfristen einzuhalten. Werden die geltend gemachten wichtigen Gründe von einem Gericht nicht als ausreichend anerkannt, setzt sich die kündigende Partei Schadenersatzforderungen wegen ungerechtfertigter Kündigung aus, berechnet nach den für die jeweilige Vertragsart geltenden Regeln.",
                ]},
            ],
            "faq": [
                {"q": "Kann jeder Vertrag aus wichtigen Gründen gekündigt werden?",
                 "a": "Dauerverträge (Miete, Arbeitsvertrag, Auftrag, einfache Gesellschaft usw.) eignen sich hierfür besonders. Bei Verträgen ohne ausdrückliche gesetzliche Regel anerkennt die Rechtsprechung des Bundesgerichts diesen Grundsatz unter strengen Voraussetzungen."},
                {"q": "Was riskiert man, wenn die geltend gemachten wichtigen Gründe nicht anerkannt werden?",
                 "a": "Die fristlose Kündigung kann als ungerechtfertigt gelten, was die kündigende Partei Schadenersatzforderungen der Vertragspartnerin oder des Vertragspartners nach den für die Vertragsart geltenden Regeln aussetzt."},
                {"q": "Müssen die wichtigen Gründe schriftlich mitgeteilt werden?",
                 "a": "Das Gesetz schreibt je nach Vertragsart nicht immer eine Schriftform vor, doch eine begründete schriftliche Mitteilung wird dringend empfohlen, um im Streitfall die Tatsächlichkeit und Schwere der geltend gemachten Gründe beweisen zu können."},
            ],
        },
        "it": {
            "slug": "disdire-contratto-motivi-gravi-svizzera",
            "title": "Disdire un contratto per motivi gravi",
            "meta": "Disdetta immediata di un contratto di durata, condizioni riconosciute dalla giurisprudenza, effetti sul risarcimento del danno.",
            "sections": [
                {"heading": "Un principio generale non codificato uniformemente", "paragraphs": [
                    "Il diritto svizzero delle obbligazioni non contiene una regola unica sulla disdetta per motivi gravi applicabile a tutti i contratti: alcuni contratti nominati prevedono una regola esplicita, come il contratto di lavoro (art. 337 CO) o il mandato (art. 404 CO), mentre per altri contratti di durata la giurisprudenza del Tribunale federale ha sviluppato un principio generale che permette una disdetta immediata quando la continuazione del contratto diventa intollerabile per una parte.",
                ]},
                {"heading": "Cosa costituisce un motivo grave", "paragraphs": [
                    "Un motivo grave presuppone generalmente una violazione grave degli obblighi contrattuali da parte dell'altra parte, una rottura del rapporto di fiducia essenziale al contratto, o circostanze che rendono la continuazione del rapporto contrattuale oggettivamente intollerabile secondo le regole della buona fede. La valutazione avviene caso per caso, tenendo conto della natura del contratto e della gravità dei fatti invocati.",
                ]},
                {"heading": "Le conseguenze di una disdetta immediata", "paragraphs": [
                    "Una disdetta per motivi gravi pone fine al contratto con effetto immediato, senza rispettare i termini di disdetta ordinari. Se i motivi gravi invocati non sono riconosciuti sufficienti da un tribunale, la parte che ha disdetto si espone al pagamento di un risarcimento per disdetta ingiustificata, calcolato secondo le regole proprie al tipo di contratto in questione.",
                ]},
            ],
            "faq": [
                {"q": "Ogni contratto può essere disdetto per motivi gravi?",
                 "a": "I contratti di durata (locazione, lavoro, mandato, società semplice, ecc.) vi si prestano particolarmente. Per i contratti senza regola legale esplicita, la giurisprudenza del Tribunale federale ammette questo principio a condizioni rigorose."},
                {"q": "Cosa si rischia se i motivi gravi invocati non sono riconosciuti?",
                 "a": "La disdetta immediata può essere considerata ingiustificata, esponendo la parte che l'ha pronunciata a un risarcimento del danno verso la controparte, secondo le regole applicabili al tipo di contratto in questione."},
                {"q": "I motivi gravi devono essere notificati per scritto?",
                 "a": "La legge non impone sempre una forma scritta a seconda del tipo di contratto, ma uno scritto motivato è vivamente raccomandato per poter provare la realtà e la gravità dei motivi invocati in caso di controversia."},
            ],
        },
        "en": {
            "slug": "terminating-contract-good-cause-switzerland",
            "title": "Terminating a contract for good cause",
            "meta": "Immediate termination of an ongoing contract, conditions recognised by case law, effects on damages.",
            "sections": [
                {"heading": "A general, not uniformly codified principle", "paragraphs": [
                    "Swiss contract law does not contain a single rule on termination for good cause applicable to all contracts: certain named contracts have an explicit rule, such as employment contracts (art. 337 CO) or agency contracts (art. 404 CO), while for other ongoing contracts, Federal Supreme Court case law has developed a general principle allowing immediate termination when continuing the contract becomes unbearable for a party.",
                ]},
                {"heading": "What constitutes good cause", "paragraphs": [
                    "Good cause generally requires a serious breach of contractual obligations by the other party, a breakdown of the trust essential to the contract, or circumstances making the continuation of the contractual relationship objectively unbearable under the rules of good faith. The assessment is made case by case, taking into account the nature of the contract and the severity of the facts invoked.",
                ]},
                {"heading": "The consequences of immediate termination", "paragraphs": [
                    "Termination for good cause ends the contract with immediate effect, without observing the ordinary notice periods. If the good cause invoked is not recognised as sufficient by a court, the terminating party is exposed to a claim for damages for unjustified termination, calculated according to the rules specific to the type of contract concerned.",
                ]},
            ],
            "faq": [
                {"q": "Can any contract be terminated for good cause?",
                 "a": "Ongoing contracts (lease, employment, agency, simple partnership, etc.) lend themselves particularly well to this. For contracts without an explicit legal rule, Federal Supreme Court case law recognises this principle under strict conditions."},
                {"q": "What is the risk if the good cause invoked is not recognised?",
                 "a": "Immediate termination may be considered unjustified, exposing the terminating party to a claim for damages from the other party, according to the rules applicable to the type of contract concerned."},
                {"q": "Does good cause need to be notified in writing?",
                 "a": "The law does not always require a written form depending on the type of contract, but a reasoned written notice is strongly recommended to be able to prove the reality and severity of the grounds invoked in the event of a dispute."},
            ],
        },
    },
    "clause-penale-dommages-interets": {
        "domaine_id": "droit_contrats",
        "published": "2026-07-30",
        "fr": {
            "slug": "clause-penale-dommages-interets-contractuels",
            "title": "Clause pénale et dommages-intérêts contractuels",
            "meta": "Fonction de la clause pénale, réduction judiciaire des peines excessives, articulation avec les dommages-intérêts selon le Code des obligations.",
            "sections": [
                {"heading": "La fonction de la clause pénale", "paragraphs": [
                    "Une clause pénale (art. 160-163 CO) est une stipulation contractuelle par laquelle une partie s'engage à verser un montant déterminé en cas d'inexécution ou de mauvaise exécution du contrat. Elle dispense en principe le créancier de prouver l'existence et le montant d'un dommage effectif : le montant convenu est dû du seul fait de l'inexécution, sauf clause contraire.",
                ]},
                {"heading": "Le pouvoir de réduction du juge", "paragraphs": [
                    "L'art. 163 al. 3 CO permet au juge de réduire une peine conventionnelle qu'il estime excessive, notamment lorsque le montant fixé est manifestement disproportionné par rapport à l'intérêt légitime du créancier ou au dommage réellement subi. Cette faculté protège la partie faible d'un contrat contre des clauses pénales abusives.",
                ]},
                {"heading": "Clause pénale et dommages-intérêts effectifs", "paragraphs": [
                    "Sauf convention contraire, le créancier ne peut pas cumuler la peine conventionnelle et la réparation intégrale du dommage effectif au-delà du montant de la peine (art. 161 CO), sauf s'il prouve un dommage supérieur au montant convenu et que le contrat le lui permet expressément.",
                ]},
            ],
            "faq": [
                {"q": "Dois-je prouver un dommage pour obtenir le paiement d'une clause pénale ?",
                 "a": "En principe non : le montant convenu est dû du seul fait de l'inexécution, sans devoir prouver l'existence ni le montant d'un dommage effectif, sauf clause contraire (art. 161 al. 1 CO)."},
                {"q": "Un juge peut-il réduire une clause pénale trop élevée ?",
                 "a": "Oui, l'art. 163 al. 3 CO permet au juge de réduire une peine conventionnelle qu'il estime excessive au regard des circonstances et de l'intérêt légitime du créancier."},
                {"q": "Puis-je réclamer plus que le montant de la clause pénale si mon dommage réel est supérieur ?",
                 "a": "En principe non, sauf si le contrat le prévoit expressément ou si vous prouvez un dommage supérieur et que la loi ou la convention vous permet de le réclamer en plus de la peine conventionnelle."},
            ],
        },
        "de": {
            "slug": "konventionalstrafe-schadenersatz-vertraglich",
            "title": "Konventionalstrafe und vertraglicher Schadenersatz",
            "meta": "Funktion der Konventionalstrafe, richterliche Herabsetzung übermässiger Strafen, Verhältnis zum tatsächlichen Schadenersatz gemäss Obligationenrecht.",
            "sections": [
                {"heading": "Die Funktion der Konventionalstrafe", "paragraphs": [
                    "Eine Konventionalstrafe (Art. 160-163 OR) ist eine vertragliche Vereinbarung, wonach eine Partei bei Nichterfüllung oder mangelhafter Erfüllung des Vertrags einen bestimmten Betrag zu zahlen verspricht. Sie befreit die Gläubigerin oder den Gläubiger grundsätzlich davon, das Bestehen und die Höhe eines tatsächlichen Schadens zu beweisen: der vereinbarte Betrag ist allein aufgrund der Nichterfüllung geschuldet, ausser bei abweichender Klausel.",
                ]},
                {"heading": "Das richterliche Herabsetzungsrecht", "paragraphs": [
                    "Art. 163 Abs. 3 OR erlaubt dem Gericht, eine als übermässig erachtete Konventionalstrafe herabzusetzen, namentlich wenn der festgelegte Betrag im Verhältnis zum berechtigten Interesse der Gläubigerin oder des Gläubigers oder zum tatsächlich erlittenen Schaden offensichtlich unverhältnismässig ist. Diese Befugnis schützt die schwächere Vertragspartei vor missbräuchlichen Konventionalstrafeklauseln.",
                ]},
                {"heading": "Konventionalstrafe und tatsächlicher Schadenersatz", "paragraphs": [
                    "Mangels anderer Vereinbarung kann die Gläubigerin oder der Gläubiger die Konventionalstrafe und den vollen Ersatz des tatsächlichen Schadens nicht über den Betrag der Strafe hinaus kumulieren (Art. 161 OR), ausser wenn sie einen höheren Schaden als den vereinbarten Betrag nachweist und der Vertrag dies ausdrücklich erlaubt.",
                ]},
            ],
            "faq": [
                {"q": "Muss ich einen Schaden nachweisen, um die Zahlung einer Konventionalstrafe zu erhalten?",
                 "a": "Grundsätzlich nicht: der vereinbarte Betrag ist allein aufgrund der Nichterfüllung geschuldet, ohne dass das Bestehen oder die Höhe eines tatsächlichen Schadens nachgewiesen werden muss, ausser bei abweichender Klausel (Art. 161 Abs. 1 OR)."},
                {"q": "Kann ein Gericht eine zu hohe Konventionalstrafe herabsetzen?",
                 "a": "Ja, Art. 163 Abs. 3 OR erlaubt dem Gericht, eine als übermässig erachtete Konventionalstrafe angesichts der Umstände und des berechtigten Interesses der Gläubigerin oder des Gläubigers herabzusetzen."},
                {"q": "Kann ich mehr verlangen als den Betrag der Konventionalstrafe, wenn mein tatsächlicher Schaden höher ist?",
                 "a": "Grundsätzlich nicht, ausser der Vertrag sieht dies ausdrücklich vor oder Sie weisen einen höheren Schaden nach und das Gesetz oder die Vereinbarung erlaubt Ihnen, diesen zusätzlich zur Strafe geltend zu machen."},
            ],
        },
        "it": {
            "slug": "clausola-penale-risarcimento-danno-contrattuale",
            "title": "Clausola penale e risarcimento del danno contrattuale",
            "meta": "Funzione della clausola penale, riduzione giudiziale delle pene eccessive, articolazione con il risarcimento effettivo secondo il Codice delle obbligazioni.",
            "sections": [
                {"heading": "La funzione della clausola penale", "paragraphs": [
                    "Una clausola penale (art. 160-163 CO) è una pattuizione contrattuale con cui una parte s'impegna a versare un importo determinato in caso d'inadempimento o cattiva esecuzione del contratto. Dispensa in linea di principio il creditore dal provare l'esistenza e l'importo di un danno effettivo: l'importo convenuto è dovuto per il solo fatto dell'inadempimento, salvo clausola contraria.",
                ]},
                {"heading": "Il potere di riduzione del giudice", "paragraphs": [
                    "L'art. 163 cpv. 3 CO permette al giudice di ridurre una pena convenzionale ritenuta eccessiva, in particolare quando l'importo fissato è manifestamente sproporzionato rispetto all'interesse legittimo del creditore o al danno effettivamente subito. Questa facoltà protegge la parte debole di un contratto contro clausole penali abusive.",
                ]},
                {"heading": "Clausola penale e risarcimento effettivo", "paragraphs": [
                    "Salvo diversa pattuizione, il creditore non può cumulare la pena convenzionale e il risarcimento integrale del danno effettivo oltre l'importo della pena (art. 161 CO), salvo che provi un danno superiore all'importo convenuto e il contratto glielo permetta espressamente.",
                ]},
            ],
            "faq": [
                {"q": "Devo provare un danno per ottenere il pagamento di una clausola penale?",
                 "a": "In linea di principio no: l'importo convenuto è dovuto per il solo fatto dell'inadempimento, senza dover provare l'esistenza né l'importo di un danno effettivo, salvo clausola contraria (art. 161 cpv. 1 CO)."},
                {"q": "Un giudice può ridurre una clausola penale troppo elevata?",
                 "a": "Sì, l'art. 163 cpv. 3 CO permette al giudice di ridurre una pena convenzionale ritenuta eccessiva rispetto alle circostanze e all'interesse legittimo del creditore."},
                {"q": "Posso reclamare più dell'importo della clausola penale se il mio danno reale è superiore?",
                 "a": "In linea di principio no, salvo che il contratto lo preveda espressamente o proviate un danno superiore e la legge o la pattuizione vi permetta di reclamarlo in aggiunta alla pena."},
            ],
        },
        "en": {
            "slug": "penalty-clause-contractual-damages",
            "title": "Penalty clause and contractual damages",
            "meta": "The purpose of a penalty clause, judicial reduction of excessive penalties, its relationship with actual damages under the Code of Obligations.",
            "sections": [
                {"heading": "The purpose of a penalty clause", "paragraphs": [
                    "A penalty clause (art. 160-163 CO) is a contractual provision under which a party undertakes to pay a set amount in the event of non-performance or defective performance of the contract. It in principle relieves the creditor of having to prove the existence and amount of actual loss: the agreed amount is owed by the mere fact of non-performance, unless otherwise agreed.",
                ]},
                {"heading": "The court's power of reduction", "paragraphs": [
                    "Art. 163 para. 3 CO allows a court to reduce a contractual penalty it considers excessive, in particular where the amount set is manifestly disproportionate to the creditor's legitimate interest or to the loss actually suffered. This power protects the weaker party to a contract against abusive penalty clauses.",
                ]},
                {"heading": "Penalty clause and actual damages", "paragraphs": [
                    "Unless otherwise agreed, the creditor cannot cumulate the contractual penalty with full compensation for actual loss beyond the amount of the penalty (art. 161 CO), unless they prove a loss greater than the agreed amount and the contract expressly allows it.",
                ]},
            ],
            "faq": [
                {"q": "Do I need to prove loss to obtain payment of a penalty clause?",
                 "a": "In principle no: the agreed amount is owed by the mere fact of non-performance, without having to prove the existence or amount of actual loss, unless otherwise agreed (art. 161 para. 1 CO)."},
                {"q": "Can a court reduce a penalty clause that is too high?",
                 "a": "Yes, art. 163 para. 3 CO allows a court to reduce a contractual penalty it considers excessive in light of the circumstances and the creditor's legitimate interest."},
                {"q": "Can I claim more than the penalty clause amount if my actual loss is higher?",
                 "a": "In principle no, unless the contract expressly provides for it or you prove a higher loss and the law or agreement allows you to claim it in addition to the penalty."},
            ],
        },
    },
    "creer-sarl-suisse": {
        "domaine_id": "droit_societes",
        "published": "2026-07-30",
        "fr": {
            "slug": "creer-sarl-suisse-capital-statuts-formalites",
            "title": "Créer une Sàrl en Suisse : capital et formalités",
            "meta": "Capital social minimum, rédaction des statuts, inscription au registre du commerce : les étapes pour créer une société à responsabilité limitée.",
            "sections": [
                {"heading": "Le capital social minimum", "paragraphs": [
                    "La société à responsabilité limitée (Sàrl) est régie par les art. 772 ss CO. Elle exige un capital social d'au moins 20 000 francs, entièrement libéré au moment de la fondation, contrairement à la société anonyme où seule une part du capital doit être libérée initialement.",
                ]},
                {"heading": "Les statuts", "paragraphs": [
                    "Les statuts doivent notamment indiquer la raison sociale et le siège de la société, son but, le montant du capital social et la valeur nominale de chaque part sociale, ainsi que la forme des publications de la société. Ils sont établis par acte authentique lors de la fondation.",
                ]},
                {"heading": "L'inscription au registre du commerce", "paragraphs": [
                    "La société n'acquiert la personnalité juridique qu'avec son inscription au registre du commerce (art. 779 CO). L'inscription requiert notamment les statuts, la preuve du dépôt du capital social auprès d'une banque, et la désignation des personnes autorisées à représenter la société.",
                ]},
                {"heading": "La responsabilité des associés", "paragraphs": [
                    "Les associés d'une Sàrl ne répondent en principe des dettes de la société que jusqu'à concurrence du capital social, sur les actifs de la société elle-même : leur patrimoine personnel n'est en principe pas engagé, sauf cas particuliers de responsabilité pour faute de gestion ou obligations statutaires de versements supplémentaires.",
                ]},
            ],
            "faq": [
                {"q": "Quel est le capital minimum pour créer une Sàrl ?",
                 "a": "20 000 francs, entièrement libérés au moment de la fondation (art. 773 CO)."},
                {"q": "À partir de quand une Sàrl existe-t-elle juridiquement ?",
                 "a": "Dès son inscription au registre du commerce (art. 779 CO) ; avant cette inscription, elle n'a pas la personnalité juridique."},
                {"q": "Les associés sont-ils personnellement responsables des dettes de la Sàrl ?",
                 "a": "En principe non : leur responsabilité se limite au capital social apporté à la société, sauf cas particuliers de responsabilité pour faute de gestion ou obligations statutaires spécifiques."},
                {"q": "Combien de personnes faut-il pour créer une Sàrl ?",
                 "a": "Une seule personne physique ou morale suffit : la Sàrl peut être fondée et détenue par un associé unique."},
            ],
        },
        "de": {
            "slug": "gmbh-gruenden-schweiz-kapital-formalitaeten",
            "title": "Eine GmbH in der Schweiz gründen: Kapital und Formalitäten",
            "meta": "Mindeststammkapital, Statutenerrichtung, Handelsregistereintrag: die Schritte zur Gründung einer Gesellschaft mit beschränkter Haftung.",
            "sections": [
                {"heading": "Das Mindeststammkapital", "paragraphs": [
                    "Die Gesellschaft mit beschränkter Haftung (GmbH) ist in Art. 772 ff. OR geregelt. Sie verlangt ein Stammkapital von mindestens 20'000 Franken, das im Zeitpunkt der Gründung vollständig einbezahlt sein muss, im Gegensatz zur Aktiengesellschaft, bei der zunächst nur ein Teil des Kapitals liberiert werden muss.",
                ]},
                {"heading": "Die Statuten", "paragraphs": [
                    "Die Statuten müssen namentlich die Firma und den Sitz der Gesellschaft, ihren Zweck, die Höhe des Stammkapitals und den Nennwert jedes Stammanteils sowie die Form der Publikationen der Gesellschaft angeben. Sie werden bei der Gründung öffentlich beurkundet.",
                ]},
                {"heading": "Der Handelsregistereintrag", "paragraphs": [
                    "Die Gesellschaft erlangt erst mit ihrer Eintragung im Handelsregister Rechtspersönlichkeit (Art. 779 OR). Die Eintragung setzt namentlich die Statuten, den Nachweis der Einzahlung des Stammkapitals bei einer Bank sowie die Bezeichnung der zur Vertretung der Gesellschaft befugten Personen voraus.",
                ]},
                {"heading": "Die Haftung der Gesellschafterinnen und Gesellschafter", "paragraphs": [
                    "Die Gesellschafterinnen und Gesellschafter einer GmbH haften für die Schulden der Gesellschaft grundsätzlich nur bis zur Höhe des Stammkapitals, mit dem Vermögen der Gesellschaft selbst: ihr persönliches Vermögen ist grundsätzlich nicht betroffen, ausser in besonderen Fällen der Haftung wegen Sorgfaltspflichtverletzung oder statutarischer Nachschusspflichten.",
                ]},
            ],
            "faq": [
                {"q": "Wie hoch ist das Mindestkapital für die Gründung einer GmbH?",
                 "a": "20'000 Franken, vollständig einbezahlt im Zeitpunkt der Gründung (Art. 773 OR)."},
                {"q": "Ab wann existiert eine GmbH rechtlich?",
                 "a": "Ab ihrer Eintragung im Handelsregister (Art. 779 OR); vor dieser Eintragung besitzt sie keine Rechtspersönlichkeit."},
                {"q": "Haften die Gesellschafterinnen und Gesellschafter persönlich für die Schulden der GmbH?",
                 "a": "Grundsätzlich nicht: ihre Haftung beschränkt sich auf das in die Gesellschaft eingebrachte Stammkapital, ausser in besonderen Fällen der Haftung wegen Sorgfaltspflichtverletzung oder besonderer statutarischer Verpflichtungen."},
                {"q": "Wie viele Personen braucht es zur Gründung einer GmbH?",
                 "a": "Eine einzige natürliche oder juristische Person genügt: die GmbH kann von einer einzigen Gesellschafterin oder einem einzigen Gesellschafter gegründet und gehalten werden."},
            ],
        },
        "it": {
            "slug": "creare-sagl-svizzera-capitale-statuti-formalita",
            "title": "Creare una Sagl in Svizzera: capitale e formalità",
            "meta": "Capitale sociale minimo, redazione degli statuti, iscrizione al registro di commercio: le tappe per creare una società a garanzia limitata.",
            "sections": [
                {"heading": "Il capitale sociale minimo", "paragraphs": [
                    "La società a garanzia limitata (Sagl) è disciplinata dagli art. 772 segg. CO. Richiede un capitale sociale di almeno 20'000 franchi, interamente liberato al momento della costituzione, a differenza della società anonima dove solo una parte del capitale deve essere liberata inizialmente.",
                ]},
                {"heading": "Gli statuti", "paragraphs": [
                    "Gli statuti devono in particolare indicare la ditta e la sede della società, il suo scopo, l'importo del capitale sociale e il valore nominale di ciascuna quota sociale, nonché la forma delle pubblicazioni della società. Sono redatti per atto pubblico al momento della costituzione.",
                ]},
                {"heading": "L'iscrizione al registro di commercio", "paragraphs": [
                    "La società acquisisce la personalità giuridica solo con la sua iscrizione al registro di commercio (art. 779 CO). L'iscrizione richiede in particolare gli statuti, la prova del versamento del capitale sociale presso una banca, e la designazione delle persone autorizzate a rappresentare la società.",
                ]},
                {"heading": "La responsabilità dei soci", "paragraphs": [
                    "I soci di una Sagl rispondono in linea di principio dei debiti della società solo fino a concorrenza del capitale sociale, sugli attivi della società stessa: il loro patrimonio personale non è in linea di principio coinvolto, salvo casi particolari di responsabilità per cattiva gestione o obblighi statutari di versamenti supplementari.",
                ]},
            ],
            "faq": [
                {"q": "Qual è il capitale minimo per creare una Sagl?",
                 "a": "20'000 franchi, interamente liberati al momento della costituzione (art. 773 CO)."},
                {"q": "Da quando esiste giuridicamente una Sagl?",
                 "a": "Dalla sua iscrizione al registro di commercio (art. 779 CO); prima di tale iscrizione non ha personalità giuridica."},
                {"q": "I soci sono personalmente responsabili dei debiti della Sagl?",
                 "a": "In linea di principio no: la loro responsabilità si limita al capitale sociale conferito alla società, salvo casi particolari di responsabilità per cattiva gestione o obblighi statutari specifici."},
                {"q": "Quante persone servono per creare una Sagl?",
                 "a": "Una sola persona fisica o giuridica è sufficiente: la Sagl può essere fondata e detenuta da un socio unico."},
            ],
        },
        "en": {
            "slug": "forming-llc-switzerland-capital-formalities",
            "title": "Forming an LLC in Switzerland: capital and formalities",
            "meta": "Minimum share capital, drafting the articles of association, registration with the commercial register: the steps to form a limited liability company.",
            "sections": [
                {"heading": "The minimum share capital", "paragraphs": [
                    "The limited liability company (GmbH/Sàrl) is governed by art. 772 ff. CO. It requires share capital of at least CHF 20,000, fully paid up at the time of formation, unlike a public limited company where only part of the capital must initially be paid in.",
                ]},
                {"heading": "The articles of association", "paragraphs": [
                    "The articles must state, among other things, the company's name and registered office, its purpose, the amount of share capital and the nominal value of each share, and the form of the company's publications. They are drawn up by public deed at the time of formation.",
                ]},
                {"heading": "Registration with the commercial register", "paragraphs": [
                    "The company only acquires legal personality upon its registration with the commercial register (art. 779 CO). Registration requires, among other things, the articles of association, proof that the share capital was deposited with a bank, and the designation of the persons authorised to represent the company.",
                ]},
                {"heading": "The shareholders' liability", "paragraphs": [
                    "Shareholders of an LLC are in principle liable for the company's debts only up to the amount of the share capital, on the assets of the company itself: their personal assets are in principle not affected, except in specific cases of liability for mismanagement or statutory obligations to make additional payments.",
                ]},
            ],
            "faq": [
                {"q": "What is the minimum capital to form an LLC?",
                 "a": "CHF 20,000, fully paid up at the time of formation (art. 773 CO)."},
                {"q": "From when does an LLC legally exist?",
                 "a": "From its registration with the commercial register (art. 779 CO); before that registration it has no legal personality."},
                {"q": "Are shareholders personally liable for the LLC's debts?",
                 "a": "In principle no: their liability is limited to the share capital contributed to the company, except in specific cases of liability for mismanagement or particular statutory obligations."},
                {"q": "How many people are needed to form an LLC?",
                 "a": "A single individual or legal entity is enough: the LLC can be formed and held by a sole shareholder."},
            ],
        },
    },
    "responsabilite-administrateurs-sa": {
        "domaine_id": "droit_societes",
        "published": "2026-07-30",
        "fr": {
            "slug": "responsabilite-administrateurs-societe-anonyme",
            "title": "Responsabilité des administrateurs de société anonyme",
            "meta": "Conditions de la responsabilité civile des administrateurs, devoir de diligence, action en responsabilité selon le Code des obligations.",
            "sections": [
                {"heading": "Le principe de la responsabilité", "paragraphs": [
                    "Les art. 754-755 CO prévoient que les membres du conseil d'administration et toutes les personnes qui s'occupent de la gestion ou de la liquidation d'une société anonyme répondent envers la société, les actionnaires et les créanciers du dommage qu'ils leur causent en manquant intentionnellement ou par négligence à leurs devoirs.",
                ]},
                {"heading": "Les conditions de la responsabilité", "paragraphs": [
                    "Une action en responsabilité suppose la réunion de quatre conditions cumulatives : un dommage, une violation d'un devoir légal ou statutaire (comme le devoir de diligence et de fidélité de l'art. 717 CO), une faute intentionnelle ou par négligence, et un lien de causalité entre la violation et le dommage.",
                ]},
                {"heading": "Le devoir de diligence des administrateurs", "paragraphs": [
                    "L'art. 717 CO impose aux administrateurs d'exercer leurs attributions avec toute la diligence nécessaire et de veiller fidèlement aux intérêts de la société. Ce devoir s'apprécie selon la nature de la fonction occupée et les circonstances concrètes, y compris la taille et la complexité de la société.",
                ]},
                {"heading": "Qui peut agir en responsabilité", "paragraphs": [
                    "La société elle-même, un actionnaire pour le dommage subi par la société, ou directement les créanciers en cas de faillite de la société peuvent intenter une action en responsabilité, selon des règles de légitimation propres à chaque situation (art. 756-757 CO).",
                ]},
            ],
            "faq": [
                {"q": "Un administrateur peut-il être tenu responsable pour une simple erreur de gestion ?",
                 "a": "Oui, si cette erreur constitue une violation du devoir de diligence de l'art. 717 CO et cause un dommage, même sans intention de nuire : la négligence suffit à engager la responsabilité (art. 754 CO)."},
                {"q": "Qui peut intenter une action en responsabilité contre un administrateur ?",
                 "a": "La société, un actionnaire pour le dommage causé à la société, ou les créanciers directement en cas de faillite, selon les règles de légitimation des art. 756-757 CO."},
                {"q": "Un administrateur peut-il limiter sa responsabilité par les statuts ?",
                 "a": "La responsabilité envers la société, les actionnaires et les créanciers découlant des art. 754-755 CO est de nature impérative et ne peut pas être exclue à l'avance par les statuts ou une convention."},
            ],
        },
        "de": {
            "slug": "haftung-verwaltungsrat-aktiengesellschaft",
            "title": "Haftung der Verwaltungsräte einer Aktiengesellschaft",
            "meta": "Voraussetzungen der zivilrechtlichen Haftung der Verwaltungsräte, Sorgfaltspflicht, Verantwortlichkeitsklage gemäss Obligationenrecht.",
            "sections": [
                {"heading": "Der Grundsatz der Haftung", "paragraphs": [
                    "Art. 754-755 OR sehen vor, dass die Mitglieder des Verwaltungsrats und alle mit der Geschäftsführung oder Liquidation einer Aktiengesellschaft befassten Personen der Gesellschaft, den Aktionärinnen und Aktionären sowie den Gläubigerinnen und Gläubigern für den Schaden haften, den sie ihnen durch absichtliche oder fahrlässige Pflichtverletzung zufügen.",
                ]},
                {"heading": "Die Voraussetzungen der Haftung", "paragraphs": [
                    "Eine Verantwortlichkeitsklage setzt vier kumulative Voraussetzungen voraus: einen Schaden, eine Verletzung einer gesetzlichen oder statutarischen Pflicht (wie die Sorgfalts- und Treuepflicht nach Art. 717 OR), ein absichtliches oder fahrlässiges Verschulden, sowie einen Kausalzusammenhang zwischen der Pflichtverletzung und dem Schaden.",
                ]},
                {"heading": "Die Sorgfaltspflicht der Verwaltungsräte", "paragraphs": [
                    "Art. 717 OR verpflichtet die Mitglieder des Verwaltungsrats, ihre Aufgaben mit aller Sorgfalt zu erfüllen und die Interessen der Gesellschaft in guten Treuen zu wahren. Diese Pflicht bemisst sich nach der Art der ausgeübten Funktion und den konkreten Umständen, einschliesslich der Grösse und Komplexität der Gesellschaft.",
                ]},
                {"heading": "Wer eine Verantwortlichkeitsklage erheben kann", "paragraphs": [
                    "Die Gesellschaft selbst, eine Aktionärin oder ein Aktionär für den der Gesellschaft zugefügten Schaden, oder direkt die Gläubigerinnen und Gläubiger im Falle des Konkurses der Gesellschaft können eine Verantwortlichkeitsklage erheben, nach besonderen Legitimationsregeln je nach Sachlage (Art. 756-757 OR).",
                ]},
            ],
            "faq": [
                {"q": "Kann ein Verwaltungsratsmitglied für einen blossen Führungsfehler haftbar gemacht werden?",
                 "a": "Ja, wenn dieser Fehler eine Verletzung der Sorgfaltspflicht nach Art. 717 OR darstellt und einen Schaden verursacht, auch ohne Schädigungsabsicht: bereits Fahrlässigkeit genügt, um die Haftung zu begründen (Art. 754 OR)."},
                {"q": "Wer kann eine Verantwortlichkeitsklage gegen ein Verwaltungsratsmitglied erheben?",
                 "a": "Die Gesellschaft, eine Aktionärin oder ein Aktionär für den der Gesellschaft zugefügten Schaden, oder die Gläubigerinnen und Gläubiger direkt im Konkursfall, nach den Legitimationsregeln der Art. 756-757 OR."},
                {"q": "Kann ein Verwaltungsratsmitglied seine Haftung durch die Statuten beschränken?",
                 "a": "Die Haftung gegenüber der Gesellschaft, den Aktionärinnen und Aktionären sowie den Gläubigerinnen und Gläubigern nach Art. 754-755 OR ist zwingender Natur und kann durch die Statuten oder eine Vereinbarung nicht im Voraus ausgeschlossen werden."},
            ],
        },
        "it": {
            "slug": "responsabilita-amministratori-societa-anonima",
            "title": "Responsabilità degli amministratori di società anonima",
            "meta": "Condizioni della responsabilità civile degli amministratori, dovere di diligenza, azione di responsabilità secondo il Codice delle obbligazioni.",
            "sections": [
                {"heading": "Il principio della responsabilità", "paragraphs": [
                    "Gli art. 754-755 CO prevedono che i membri del consiglio d'amministrazione e tutte le persone che si occupano della gestione o della liquidazione di una società anonima rispondono verso la società, gli azionisti e i creditori del danno che causano loro violando intenzionalmente o per negligenza i propri doveri.",
                ]},
                {"heading": "Le condizioni della responsabilità", "paragraphs": [
                    "Un'azione di responsabilità presuppone la riunione di quattro condizioni cumulative: un danno, una violazione di un dovere legale o statutario (come il dovere di diligenza e fedeltà dell'art. 717 CO), una colpa intenzionale o per negligenza, e un nesso di causalità tra la violazione e il danno.",
                ]},
                {"heading": "Il dovere di diligenza degli amministratori", "paragraphs": [
                    "L'art. 717 CO impone agli amministratori di adempiere i loro compiti con ogni diligenza necessaria e di tutelare con fedeltà gli interessi della società. Questo dovere si valuta secondo la natura della funzione occupata e le circostanze concrete, incluse le dimensioni e la complessità della società.",
                ]},
                {"heading": "Chi può agire in responsabilità", "paragraphs": [
                    "La società stessa, un azionista per il danno subito dalla società, o direttamente i creditori in caso di fallimento della società possono promuovere un'azione di responsabilità, secondo regole di legittimazione proprie a ciascuna situazione (art. 756-757 CO).",
                ]},
            ],
            "faq": [
                {"q": "Un amministratore può essere ritenuto responsabile per un semplice errore di gestione?",
                 "a": "Sì, se tale errore costituisce una violazione del dovere di diligenza dell'art. 717 CO e causa un danno, anche senza intenzione di nuocere: la negligenza è sufficiente per fondare la responsabilità (art. 754 CO)."},
                {"q": "Chi può promuovere un'azione di responsabilità contro un amministratore?",
                 "a": "La società, un azionista per il danno causato alla società, o i creditori direttamente in caso di fallimento, secondo le regole di legittimazione degli art. 756-757 CO."},
                {"q": "Un amministratore può limitare la propria responsabilità tramite gli statuti?",
                 "a": "La responsabilità verso la società, gli azionisti e i creditori derivante dagli art. 754-755 CO è di natura imperativa e non può essere esclusa in anticipo dagli statuti o da una convenzione."},
            ],
        },
        "en": {
            "slug": "liability-directors-public-limited-company",
            "title": "Liability of directors of a public limited company",
            "meta": "Conditions for civil liability of directors, duty of care, liability action under the Code of Obligations.",
            "sections": [
                {"heading": "The principle of liability", "paragraphs": [
                    "Art. 754-755 CO provide that members of the board of directors and everyone involved in the management or liquidation of a public limited company are liable to the company, its shareholders and its creditors for damage caused by intentional or negligent breach of their duties.",
                ]},
                {"heading": "The conditions for liability", "paragraphs": [
                    "A liability action requires four cumulative conditions: damage, a breach of a statutory or by-law duty (such as the duty of care and loyalty under art. 717 CO), intentional or negligent fault, and a causal link between the breach and the damage.",
                ]},
                {"heading": "Directors' duty of care", "paragraphs": [
                    "Art. 717 CO requires directors to perform their duties with all due care and to safeguard the company's interests in good faith. This duty is assessed according to the nature of the role held and the specific circumstances, including the size and complexity of the company.",
                ]},
                {"heading": "Who can bring a liability action", "paragraphs": [
                    "The company itself, a shareholder for damage suffered by the company, or creditors directly in the event of the company's bankruptcy can bring a liability action, according to standing rules specific to each situation (art. 756-757 CO).",
                ]},
            ],
            "faq": [
                {"q": "Can a director be held liable for a simple management error?",
                 "a": "Yes, if that error constitutes a breach of the duty of care under art. 717 CO and causes damage, even without intent to harm: negligence is enough to establish liability (art. 754 CO)."},
                {"q": "Who can bring a liability action against a director?",
                 "a": "The company, a shareholder for damage caused to the company, or creditors directly in the event of bankruptcy, according to the standing rules of art. 756-757 CO."},
                {"q": "Can a director limit their liability through the articles of association?",
                 "a": "Liability to the company, shareholders and creditors under art. 754-755 CO is mandatory in nature and cannot be excluded in advance by the articles of association or an agreement."},
            ],
        },
    },
    "retrait-permis-duree-infraction": {
        "domaine_id": "droit_circulation",
        "published": "2026-07-30",
        "fr": {
            "slug": "retrait-permis-conduire-duree-infraction",
            "title": "Retrait de permis : durées selon la gravité",
            "meta": "Infractions légères, moyennes et graves à la LCR, durées de retrait de permis, cas de récidive : ce que prévoit la loi sur la circulation routière.",
            "sections": [
                {"heading": "Les trois catégories d'infractions", "paragraphs": [
                    "La loi sur la circulation routière distingue les infractions légères (art. 16a LCR), moyennement graves (art. 16b LCR) et graves (art. 16c LCR), selon le degré de mise en danger de la sécurité routière et la faute du conducteur. Cette classification détermine directement les conséquences administratives applicables.",
                ]},
                {"heading": "L'infraction légère", "paragraphs": [
                    "Une infraction légère entraîne en principe un simple avertissement, sauf si le conducteur a fait l'objet d'un retrait de permis ou d'un avertissement au cours des deux années précédentes, auquel cas un retrait d'au moins un mois est prononcé (art. 16a LCR).",
                ]},
                {"heading": "L'infraction moyennement grave", "paragraphs": [
                    "Elle entraîne un retrait de permis d'au moins un mois (art. 16b LCR). En cas de récidive dans les délais fixés par la loi, la durée minimale du retrait augmente progressivement.",
                ]},
                {"heading": "L'infraction grave", "paragraphs": [
                    "Une infraction grave, telle que la conduite en état d'ébriété qualifiée ou un dépassement important de la vitesse autorisée, entraîne un retrait de permis d'au moins trois mois (art. 16c LCR). En cas de récidives répétées, la loi prévoit des durées minimales croissantes, pouvant aller jusqu'au retrait de sécurité pour une durée indéterminée.",
                ]},
            ],
            "faq": [
                {"q": "Quelle est la durée minimale de retrait pour une infraction grave ?",
                 "a": "Trois mois au minimum (art. 16c LCR), pouvant être prolongée en cas de récidive dans les délais fixés par la loi."},
                {"q": "Une infraction légère entraîne-t-elle toujours un retrait de permis ?",
                 "a": "Non, elle entraîne en principe un simple avertissement, sauf récidive dans les deux années précédentes, auquel cas un retrait d'au moins un mois est prononcé (art. 16a LCR)."},
                {"q": "Qui décide du retrait de permis ?",
                 "a": "L'autorité administrative cantonale compétente en matière de circulation routière, sur la base du rapport de police et, le cas échéant, de la décision pénale relative aux mêmes faits."},
                {"q": "Le retrait de permis est-il cumulé avec une sanction pénale ?",
                 "a": "Oui, ce sont deux procédures distinctes : la sanction pénale (amende, peine pécuniaire) est prononcée par le ministère public ou le tribunal pénal, tandis que le retrait de permis est une mesure administrative prononcée séparément par l'autorité cantonale."},
            ],
        },
        "de": {
            "slug": "fuehrerausweisentzug-dauer-schwere-widerhandlung",
            "title": "Führerausweisentzug: Dauer je nach Schwere",
            "meta": "Leichte, mittelschwere und schwere Widerhandlungen gegen das SVG, Entzugsdauern, Rückfall: was das Strassenverkehrsgesetz vorsieht.",
            "sections": [
                {"heading": "Die drei Kategorien von Widerhandlungen", "paragraphs": [
                    "Das Strassenverkehrsgesetz unterscheidet zwischen leichten (Art. 16a SVG), mittelschweren (Art. 16b SVG) und schweren (Art. 16c SVG) Widerhandlungen, je nach dem Grad der Gefährdung der Verkehrssicherheit und dem Verschulden der Lenkerin oder des Lenkers. Diese Einteilung bestimmt unmittelbar die anwendbaren verwaltungsrechtlichen Folgen.",
                ]},
                {"heading": "Die leichte Widerhandlung", "paragraphs": [
                    "Eine leichte Widerhandlung führt grundsätzlich zu einer blossen Verwarnung, ausser wenn die betroffene Person in den vorangegangenen zwei Jahren bereits einen Ausweisentzug oder eine Verwarnung erhalten hat, in welchem Fall ein Entzug von mindestens einem Monat ausgesprochen wird (Art. 16a SVG).",
                ]},
                {"heading": "Die mittelschwere Widerhandlung", "paragraphs": [
                    "Sie führt zu einem Führerausweisentzug von mindestens einem Monat (Art. 16b SVG). Bei Rückfall innerhalb der gesetzlich festgelegten Fristen erhöht sich die Mindestdauer des Entzugs progressiv.",
                ]},
                {"heading": "Die schwere Widerhandlung", "paragraphs": [
                    "Eine schwere Widerhandlung, wie qualifizierte Trunkenheitsfahrt oder erhebliche Geschwindigkeitsüberschreitung, führt zu einem Führerausweisentzug von mindestens drei Monaten (Art. 16c SVG). Bei wiederholten Rückfällen sieht das Gesetz progressiv steigende Mindestdauern vor, die bis zum Sicherungsentzug auf unbestimmte Zeit reichen können.",
                ]},
            ],
            "faq": [
                {"q": "Wie lange ist die Mindestentzugsdauer bei einer schweren Widerhandlung?",
                 "a": "Mindestens drei Monate (Art. 16c SVG), verlängerbar bei Rückfall innerhalb der gesetzlich festgelegten Fristen."},
                {"q": "Führt eine leichte Widerhandlung immer zu einem Führerausweisentzug?",
                 "a": "Nein, sie führt grundsätzlich zu einer blossen Verwarnung, ausser bei Rückfall innerhalb der vorangegangenen zwei Jahre, in welchem Fall ein Entzug von mindestens einem Monat ausgesprochen wird (Art. 16a SVG)."},
                {"q": "Wer entscheidet über den Führerausweisentzug?",
                 "a": "Die zuständige kantonale Verwaltungsbehörde für den Strassenverkehr, gestützt auf den Polizeirapport und gegebenenfalls den strafrechtlichen Entscheid zu denselben Tatsachen."},
                {"q": "Wird der Führerausweisentzug mit einer strafrechtlichen Sanktion kumuliert?",
                 "a": "Ja, es handelt sich um zwei getrennte Verfahren: die strafrechtliche Sanktion (Busse, Geldstrafe) wird von der Staatsanwaltschaft oder dem Strafgericht ausgesprochen, während der Führerausweisentzug eine separate verwaltungsrechtliche Massnahme der kantonalen Behörde ist."},
            ],
        },
        "it": {
            "slug": "revoca-licenza-durata-gravita-infrazione",
            "title": "Revoca della licenza: durata secondo la gravità",
            "meta": "Infrazioni lievi, medie e gravi alla LCStr, durate di revoca della licenza, casi di recidiva: quanto previsto dalla legge sulla circolazione stradale.",
            "sections": [
                {"heading": "Le tre categorie di infrazioni", "paragraphs": [
                    "La legge sulla circolazione stradale distingue le infrazioni lievi (art. 16a LCStr), medie (art. 16b LCStr) e gravi (art. 16c LCStr), secondo il grado di messa in pericolo della sicurezza stradale e la colpa del conducente. Questa classificazione determina direttamente le conseguenze amministrative applicabili.",
                ]},
                {"heading": "L'infrazione lieve", "paragraphs": [
                    "Un'infrazione lieve comporta in linea di principio un semplice avvertimento, salvo se il conducente ha già subito una revoca della licenza o un avvertimento nei due anni precedenti, nel qual caso viene pronunciata una revoca di almeno un mese (art. 16a LCStr).",
                ]},
                {"heading": "L'infrazione media", "paragraphs": [
                    "Comporta una revoca della licenza di almeno un mese (art. 16b LCStr). In caso di recidiva entro i termini fissati dalla legge, la durata minima della revoca aumenta progressivamente.",
                ]},
                {"heading": "L'infrazione grave", "paragraphs": [
                    "Un'infrazione grave, come la guida in stato di ebrietà qualificata o un notevole superamento della velocità consentita, comporta una revoca della licenza di almeno tre mesi (art. 16c LCStr). In caso di recidive ripetute, la legge prevede durate minime crescenti, che possono arrivare fino alla revoca a tempo indeterminato per motivi di sicurezza.",
                ]},
            ],
            "faq": [
                {"q": "Qual è la durata minima di revoca per un'infrazione grave?",
                 "a": "Almeno tre mesi (art. 16c LCStr), prorogabile in caso di recidiva entro i termini fissati dalla legge."},
                {"q": "Un'infrazione lieve comporta sempre una revoca della licenza?",
                 "a": "No, comporta in linea di principio un semplice avvertimento, salvo recidiva nei due anni precedenti, nel qual caso viene pronunciata una revoca di almeno un mese (art. 16a LCStr)."},
                {"q": "Chi decide sulla revoca della licenza?",
                 "a": "L'autorità amministrativa cantonale competente in materia di circolazione stradale, sulla base del rapporto di polizia e, se del caso, della decisione penale relativa agli stessi fatti."},
                {"q": "La revoca della licenza si cumula con una sanzione penale?",
                 "a": "Sì, si tratta di due procedure distinte: la sanzione penale (multa, pena pecuniaria) è pronunciata dal pubblico ministero o dal tribunale penale, mentre la revoca della licenza è una misura amministrativa pronunciata separatamente dall'autorità cantonale."},
            ],
        },
        "en": {
            "slug": "driving-licence-withdrawal-duration-offence",
            "title": "Driving licence withdrawal: duration by severity",
            "meta": "Minor, medium and serious traffic offences, withdrawal periods, repeat offences: what the Road Traffic Act provides.",
            "sections": [
                {"heading": "Three categories of offence", "paragraphs": [
                    "The Road Traffic Act distinguishes between minor (art. 16a LCR), medium (art. 16b LCR) and serious (art. 16c LCR) offences, according to the degree of danger to road safety and the driver's fault. This classification directly determines the applicable administrative consequences.",
                ]},
                {"heading": "The minor offence", "paragraphs": [
                    "A minor offence in principle results in a simple warning, unless the driver has already had a licence withdrawn or received a warning in the previous two years, in which case a withdrawal of at least one month is ordered (art. 16a LCR).",
                ]},
                {"heading": "The medium offence", "paragraphs": [
                    "It results in a licence withdrawal of at least one month (art. 16b LCR). In the event of a repeat offence within the periods set by law, the minimum withdrawal period increases progressively.",
                ]},
                {"heading": "The serious offence", "paragraphs": [
                    "A serious offence, such as qualified drink-driving or a significant speeding violation, results in a licence withdrawal of at least three months (art. 16c LCR). In the event of repeated offences, the law provides for increasing minimum periods, which can go up to withdrawal for an indefinite period on safety grounds.",
                ]},
            ],
            "faq": [
                {"q": "What is the minimum withdrawal period for a serious offence?",
                 "a": "At least three months (art. 16c LCR), which can be extended in the event of a repeat offence within the periods set by law."},
                {"q": "Does a minor offence always lead to a licence withdrawal?",
                 "a": "No, it in principle results in a simple warning, unless there was a repeat offence in the previous two years, in which case a withdrawal of at least one month is ordered (art. 16a LCR)."},
                {"q": "Who decides on licence withdrawal?",
                 "a": "The competent cantonal administrative authority for road traffic, based on the police report and, where applicable, the criminal decision relating to the same facts."},
                {"q": "Is licence withdrawal combined with a criminal sanction?",
                 "a": "Yes, these are two separate procedures: the criminal sanction (fine, monetary penalty) is imposed by the public prosecutor or criminal court, while licence withdrawal is a separate administrative measure imposed by the cantonal authority."},
            ],
        },
    },
    "accident-route-qui-paie-declaration": {
        "domaine_id": "droit_circulation",
        "published": "2026-07-30",
        "fr": {
            "slug": "accident-route-qui-paie-declaration-sinistre",
            "title": "Accident de la route : qui paie et comment déclarer",
            "meta": "Assurance responsabilité civile obligatoire, déclaration de sinistre, répartition des responsabilités : les règles applicables en cas d'accident.",
            "sections": [
                {"heading": "L'assurance responsabilité civile obligatoire", "paragraphs": [
                    "Tout véhicule automobile circulant en Suisse doit être couvert par une assurance responsabilité civile (art. 63 LCR), qui indemnise les tiers lésés par ce véhicule, indépendamment de la solvabilité personnelle du détenteur ou du conducteur responsable.",
                ]},
                {"heading": "La responsabilité du détenteur", "paragraphs": [
                    "L'art. 58 LCR pose une responsabilité causale du détenteur du véhicule pour les dommages causés par son usage, indépendamment d'une faute de sa part. Le détenteur ne peut se libérer qu'en prouvant que l'accident a été causé par force majeure, faute grave du lésé ou d'un tiers, sans faute de sa part ni défectuosité du véhicule.",
                ]},
                {"heading": "La déclaration du sinistre", "paragraphs": [
                    "Après un accident, il convient de constater les faits (échange des coordonnées, constat amiable ou intervention de la police selon la gravité), puis de déclarer le sinistre sans délai à son assurance, laquelle transmet le dossier à l'assureur responsabilité civile du véhicule responsable si celui-ci est identifié.",
                ]},
                {"heading": "Les accidents avec véhicule non identifié ou non assuré", "paragraphs": [
                    "Lorsque le véhicule responsable ne peut pas être identifié, ou n'était pas assuré, le Fonds national de garantie (art. 76 LCA) prend en charge l'indemnisation du lésé dans les limites fixées par la loi, afin d'éviter que la victime reste sans recours.",
                ]},
            ],
            "faq": [
                {"q": "Qui paie les dommages en cas d'accident de la route ?",
                 "a": "En principe l'assureur responsabilité civile du véhicule reconnu responsable de l'accident, sur la base de la responsabilité causale du détenteur prévue par l'art. 58 LCR."},
                {"q": "Que faire si le responsable de l'accident prend la fuite ?",
                 "a": "Il faut avertir la police et déclarer le sinistre à son propre assureur. Si le véhicule responsable reste non identifié, le Fonds national de garantie peut indemniser le lésé dans les limites légales."},
                {"q": "Dois-je toujours appeler la police après un accident ?",
                 "a": "Ce n'est pas systématiquement obligatoire pour un accrochage mineur sans blessé, mais fortement recommandé dès qu'il y a un désaccord sur les responsabilités, des blessés, ou des dommages importants."},
                {"q": "Le détenteur peut-il échapper à sa responsabilité ?",
                 "a": "Seulement en prouvant que l'accident résulte d'un cas de force majeure, d'une faute grave du lésé ou d'un tiers, sans faute de sa part ni défectuosité du véhicule (art. 59 LCR)."},
            ],
        },
        "de": {
            "slug": "verkehrsunfall-wer-zahlt-schadenmeldung",
            "title": "Verkehrsunfall: wer zahlt und wie melden",
            "meta": "Obligatorische Haftpflichtversicherung, Schadenmeldung, Aufteilung der Verantwortlichkeiten: die geltenden Regeln bei einem Verkehrsunfall.",
            "sections": [
                {"heading": "Die obligatorische Haftpflichtversicherung", "paragraphs": [
                    "Jedes in der Schweiz verkehrende Motorfahrzeug muss durch eine Haftpflichtversicherung gedeckt sein (Art. 63 SVG), welche geschädigte Dritte unabhängig von der persönlichen Zahlungsfähigkeit der halterin oder des Halters oder der verantwortlichen Lenkerin oder des verantwortlichen Lenkers entschädigt.",
                ]},
                {"heading": "Die Halterhaftung", "paragraphs": [
                    "Art. 58 SVG statuiert eine Kausalhaftung der Halterin oder des Halters eines Fahrzeugs für die durch dessen Betrieb verursachten Schäden, unabhängig von einem Verschulden ihrerseits. Die Halterin oder der Halter kann sich nur befreien, indem sie oder er nachweist, dass der Unfall durch höhere Gewalt, grobes Verschulden der geschädigten Person oder eines Dritten verursacht wurde, ohne eigenes Verschulden und ohne Fahrzeugmangel.",
                ]},
                {"heading": "Die Schadenmeldung", "paragraphs": [
                    "Nach einem Unfall gilt es, den Sachverhalt festzuhalten (Austausch der Kontaktdaten, europäischer Unfallbericht oder Polizeieinsatz je nach Schwere), und den Schaden unverzüglich der eigenen Versicherung zu melden, welche das Dossier an die Haftpflichtversicherung des verantwortlichen Fahrzeugs weiterleitet, sofern dieses identifiziert ist.",
                ]},
                {"heading": "Unfälle mit nicht identifiziertem oder nicht versichertem Fahrzeug", "paragraphs": [
                    "Kann das verantwortliche Fahrzeug nicht identifiziert werden oder war es nicht versichert, übernimmt der Nationale Garantiefonds (Art. 76 VVG) die Entschädigung der geschädigten Person im gesetzlich vorgesehenen Rahmen, um zu verhindern, dass das Opfer ohne Regressmöglichkeit bleibt.",
                ]},
            ],
            "faq": [
                {"q": "Wer bezahlt die Schäden bei einem Verkehrsunfall?",
                 "a": "Grundsätzlich die Haftpflichtversicherung des als verantwortlich anerkannten Fahrzeugs, gestützt auf die Kausalhaftung der Halterin oder des Halters nach Art. 58 SVG."},
                {"q": "Was tun, wenn die verantwortliche Person nach dem Unfall flüchtet?",
                 "a": "Es gilt, die Polizei zu benachrichtigen und den Schaden der eigenen Versicherung zu melden. Bleibt das verantwortliche Fahrzeug nicht identifiziert, kann der Nationale Garantiefonds die geschädigte Person im gesetzlichen Rahmen entschädigen."},
                {"q": "Muss ich nach einem Unfall immer die Polizei rufen?",
                 "a": "Dies ist bei einem geringfügigen Blechschaden ohne Verletzte nicht systematisch obligatorisch, wird jedoch dringend empfohlen, sobald Uneinigkeit über die Verantwortlichkeiten besteht, Verletzte zu beklagen sind oder erhebliche Schäden vorliegen."},
                {"q": "Kann sich die Halterin oder der Halter der Haftung entziehen?",
                 "a": "Nur durch den Nachweis, dass der Unfall auf höhere Gewalt, grobes Verschulden der geschädigten Person oder eines Dritten zurückzuführen ist, ohne eigenes Verschulden und ohne Fahrzeugmangel (Art. 59 SVG)."},
            ],
        },
        "it": {
            "slug": "incidente-stradale-chi-paga-denuncia-sinistro",
            "title": "Incidente stradale: chi paga e come denunciare",
            "meta": "Assicurazione di responsabilità civile obbligatoria, denuncia del sinistro, ripartizione delle responsabilità: le regole applicabili in caso di incidente.",
            "sections": [
                {"heading": "L'assicurazione di responsabilità civile obbligatoria", "paragraphs": [
                    "Ogni veicolo a motore circolante in Svizzera deve essere coperto da un'assicurazione di responsabilità civile (art. 63 LCStr), che indennizza i terzi lesi da tale veicolo, indipendentemente dalla solvibilità personale del detentore o del conducente responsabile.",
                ]},
                {"heading": "La responsabilità del detentore", "paragraphs": [
                    "L'art. 58 LCStr pone una responsabilità causale del detentore del veicolo per i danni causati dal suo utilizzo, indipendentemente da una sua colpa. Il detentore può liberarsi solo provando che l'incidente è stato causato da forza maggiore, colpa grave del leso o di un terzo, senza colpa da parte sua né difetto del veicolo.",
                ]},
                {"heading": "La denuncia del sinistro", "paragraphs": [
                    "Dopo un incidente, occorre accertare i fatti (scambio dei dati, constatazione amichevole o intervento della polizia secondo la gravità), poi denunciare il sinistro senza indugio alla propria assicurazione, la quale trasmette l'incarto all'assicuratore di responsabilità civile del veicolo responsabile se questo è identificato.",
                ]},
                {"heading": "Gli incidenti con veicolo non identificato o non assicurato", "paragraphs": [
                    "Quando il veicolo responsabile non può essere identificato, o non era assicurato, il Fondo nazionale di garanzia (art. 76 LCA) si assume l'indennizzo del leso nei limiti fissati dalla legge, per evitare che la vittima rimanga senza ricorso.",
                ]},
            ],
            "faq": [
                {"q": "Chi paga i danni in caso di incidente stradale?",
                 "a": "In linea di principio l'assicuratore di responsabilità civile del veicolo riconosciuto responsabile dell'incidente, sulla base della responsabilità causale del detentore prevista dall'art. 58 LCStr."},
                {"q": "Cosa fare se il responsabile dell'incidente fugge?",
                 "a": "Occorre avvisare la polizia e denunciare il sinistro alla propria assicurazione. Se il veicolo responsabile rimane non identificato, il Fondo nazionale di garanzia può indennizzare il leso entro i limiti legali."},
                {"q": "Devo sempre chiamare la polizia dopo un incidente?",
                 "a": "Non è sistematicamente obbligatorio per un tamponamento minore senza feriti, ma è fortemente raccomandato non appena vi è disaccordo sulle responsabilità, vi sono feriti, o i danni sono importanti."},
                {"q": "Il detentore può sfuggire alla propria responsabilità?",
                 "a": "Solo provando che l'incidente risulta da un caso di forza maggiore, da colpa grave del leso o di un terzo, senza colpa da parte sua né difetto del veicolo (art. 59 LCStr)."},
            ],
        },
        "en": {
            "slug": "road-accident-who-pays-reporting-claim",
            "title": "Road accident: who pays and how to report it",
            "meta": "Compulsory third-party liability insurance, reporting a claim, allocation of responsibility: the rules that apply after a road accident.",
            "sections": [
                {"heading": "Compulsory third-party liability insurance", "paragraphs": [
                    "Every motor vehicle driven in Switzerland must be covered by third-party liability insurance (art. 63 LCR), which compensates third parties harmed by that vehicle, regardless of the personal solvency of the responsible keeper or driver.",
                ]},
                {"heading": "The keeper's liability", "paragraphs": [
                    "Art. 58 LCR establishes strict liability for the vehicle's keeper for damage caused by its use, regardless of any fault on their part. The keeper can only be released from liability by proving that the accident was caused by force majeure, gross fault of the injured party or a third party, without any fault on their part and without any defect in the vehicle.",
                ]},
                {"heading": "Reporting the claim", "paragraphs": [
                    "After an accident, the facts should be recorded (exchange of contact details, a friendly accident report, or police involvement depending on severity), then the claim should be reported without delay to your own insurer, who forwards the file to the responsible vehicle's liability insurer once it has been identified.",
                ]},
                {"heading": "Accidents with an unidentified or uninsured vehicle", "paragraphs": [
                    "When the responsible vehicle cannot be identified, or was not insured, the National Guarantee Fund (art. 76 ICA) covers compensation for the injured party within the limits set by law, to prevent the victim from being left without recourse.",
                ]},
            ],
            "faq": [
                {"q": "Who pays for damage in a road accident?",
                 "a": "In principle the liability insurer of the vehicle found responsible for the accident, based on the keeper's strict liability under art. 58 LCR."},
                {"q": "What should I do if the person responsible for the accident flees?",
                 "a": "You should notify the police and report the claim to your own insurer. If the responsible vehicle remains unidentified, the National Guarantee Fund can compensate the injured party within the legal limits."},
                {"q": "Do I always have to call the police after an accident?",
                 "a": "This is not systematically mandatory for a minor collision without injuries, but it is strongly recommended as soon as there is disagreement over responsibility, injuries, or significant damage."},
                {"q": "Can the keeper escape liability?",
                 "a": "Only by proving that the accident resulted from force majeure, gross fault of the injured party or a third party, without any fault on their part and without any defect in the vehicle (art. 59 LCR)."},
            ],
        },
    },
    "recours-decision-administrative-delais": {
        "domaine_id": "droit_administratif",
        "published": "2026-07-30",
        "fr": {
            "slug": "recours-decision-administrative-delais-procedure",
            "title": "Recours contre une décision administrative",
            "meta": "Délai de recours de 30 jours, autorité compétente, effet suspensif : les règles de la procédure administrative fédérale et cantonale.",
            "sections": [
                {"heading": "Le principe : deux niveaux de règles", "paragraphs": [
                    "La procédure de recours contre une décision d'une autorité fédérale est régie par la loi fédérale sur la procédure administrative (PA). Les décisions des autorités cantonales et communales relèvent en revanche des lois cantonales de procédure administrative, dont le contenu varie d'un canton à l'autre, même si les principes généraux (droit d'être entendu, délai de recours, motivation) sont similaires.",
                ]},
                {"heading": "Le délai de recours", "paragraphs": [
                    "Au niveau fédéral, le délai de recours contre une décision est de 30 jours dès sa notification (art. 50 PA), sauf dispositions spéciales prévoyant un délai différent. Les délais cantonaux sont généralement proches de cette durée, mais peuvent différer : il faut impérativement vérifier le délai indiqué dans l'indication des voies de droit figurant au bas de la décision elle-même.",
                ]},
                {"heading": "La forme du recours", "paragraphs": [
                    "Le recours doit en principe être adressé par écrit à l'autorité de recours désignée dans la décision, contenir des conclusions et une motivation, et être accompagné de la décision attaquée. Une décision qui ne mentionne pas correctement les voies de droit (autorité compétente, délai, forme) ne peut en principe pas causer de préjudice à son destinataire s'il agit dans un délai raisonnable malgré cette lacune.",
                ]},
                {"heading": "L'effet suspensif", "paragraphs": [
                    "Un recours a en principe un effet suspensif, c'est-à-dire qu'il empêche l'exécution de la décision attaquée tant que l'autorité de recours n'a pas statué, sauf si la loi ou l'autorité qui a rendu la décision l'exclut expressément pour des motifs d'intérêt public ou d'urgence (art. 55 PA au niveau fédéral).",
                ]},
            ],
            "faq": [
                {"q": "Quel est le délai pour recourir contre une décision administrative fédérale ?",
                 "a": "30 jours dès la notification de la décision (art. 50 PA), sauf disposition spéciale contraire. Le délai exact applicable à une décision cantonale ou communale doit être vérifié dans l'indication des voies de droit de la décision elle-même."},
                {"q": "Le recours empêche-t-il l'exécution de la décision contestée ?",
                 "a": "En principe oui, un recours a un effet suspensif, sauf si la loi ou l'autorité l'exclut expressément pour des motifs d'intérêt public ou d'urgence."},
                {"q": "Que faire si la décision ne mentionne pas les voies de droit ?",
                 "a": "L'absence ou l'inexactitude de l'indication des voies de droit ne doit en principe causer aucun préjudice à son destinataire, à condition qu'il agisse dans un délai raisonnable dès qu'il a connaissance de la possibilité de recourir."},
                {"q": "Les règles de recours sont-elles les mêmes dans tous les cantons ?",
                 "a": "Non, seules les décisions d'autorités fédérales relèvent de la loi fédérale sur la procédure administrative (PA) ; chaque canton dispose de sa propre loi de procédure administrative, avec des délais et modalités qui peuvent différer."},
            ],
        },
        "de": {
            "slug": "beschwerde-verwaltungsentscheid-fristen-verfahren",
            "title": "Beschwerde gegen einen Verwaltungsentscheid",
            "meta": "30-tägige Beschwerdefrist, zuständige Behörde, aufschiebende Wirkung: die Regeln des Bundes- und kantonalen Verwaltungsverfahrensrechts.",
            "sections": [
                {"heading": "Der Grundsatz: zwei Regelungsebenen", "paragraphs": [
                    "Das Beschwerdeverfahren gegen einen Entscheid einer Bundesbehörde richtet sich nach dem Bundesgesetz über das Verwaltungsverfahren (VwVG). Entscheide kantonaler und kommunaler Behörden unterliegen hingegen den kantonalen Verwaltungsverfahrensgesetzen, deren Inhalt von Kanton zu Kanton variiert, auch wenn die allgemeinen Grundsätze (rechtliches Gehör, Beschwerdefrist, Begründungspflicht) ähnlich sind.",
                ]},
                {"heading": "Die Beschwerdefrist", "paragraphs": [
                    "Auf Bundesebene beträgt die Beschwerdefrist gegen einen Entscheid 30 Tage ab dessen Eröffnung (Art. 50 VwVG), vorbehältlich besonderer Bestimmungen mit abweichender Frist. Die kantonalen Fristen liegen meist in ähnlicher Grössenordnung, können jedoch abweichen: es ist unerlässlich, die im Rechtsmittelbelehrung des Entscheids selbst angegebene Frist zu prüfen.",
                ]},
                {"heading": "Die Form der Beschwerde", "paragraphs": [
                    "Die Beschwerde muss grundsätzlich schriftlich an die im Entscheid bezeichnete Beschwerdeinstanz gerichtet werden, Anträge und eine Begründung enthalten und mit dem angefochtenen Entscheid versehen sein. Ein Entscheid, der die Rechtsmittelbelehrung (zuständige Behörde, Frist, Form) fehlerhaft angibt, darf der oder dem Betroffenen grundsätzlich keinen Nachteil bringen, sofern sie oder er innert angemessener Frist trotz dieser Lücke handelt.",
                ]},
                {"heading": "Die aufschiebende Wirkung", "paragraphs": [
                    "Eine Beschwerde hat grundsätzlich aufschiebende Wirkung, das heisst, sie hindert den Vollzug des angefochtenen Entscheids, solange die Beschwerdeinstanz nicht entschieden hat, ausser wenn das Gesetz oder die verfügende Behörde diese Wirkung aus Gründen des öffentlichen Interesses oder der Dringlichkeit ausdrücklich ausschliesst (Art. 55 VwVG auf Bundesebene).",
                ]},
            ],
            "faq": [
                {"q": "Wie lange habe ich Zeit, um gegen einen Bundesverwaltungsentscheid Beschwerde zu erheben?",
                 "a": "30 Tage ab Eröffnung des Entscheids (Art. 50 VwVG), vorbehältlich abweichender besonderer Bestimmungen. Die genaue Frist für einen kantonalen oder kommunalen Entscheid muss anhand der Rechtsmittelbelehrung des Entscheids selbst geprüft werden."},
                {"q": "Verhindert die Beschwerde den Vollzug des angefochtenen Entscheids?",
                 "a": "Grundsätzlich ja, eine Beschwerde hat aufschiebende Wirkung, ausser das Gesetz oder die Behörde schliesst diese aus Gründen des öffentlichen Interesses oder der Dringlichkeit ausdrücklich aus."},
                {"q": "Was tun, wenn der Entscheid keine Rechtsmittelbelehrung enthält?",
                 "a": "Das Fehlen oder die Unrichtigkeit der Rechtsmittelbelehrung darf der oder dem Betroffenen grundsätzlich keinen Nachteil bringen, sofern sie oder er innert angemessener Frist handelt, sobald sie oder er von der Beschwerdemöglichkeit Kenntnis erlangt."},
                {"q": "Gelten in allen Kantonen dieselben Beschwerderegeln?",
                 "a": "Nein, nur Entscheide von Bundesbehörden unterliegen dem Bundesgesetz über das Verwaltungsverfahren (VwVG); jeder Kanton verfügt über sein eigenes Verwaltungsverfahrensgesetz, mit Fristen und Modalitäten, die abweichen können."},
            ],
        },
        "it": {
            "slug": "ricorso-decisione-amministrativa-termini-procedura",
            "title": "Ricorso contro una decisione amministrativa",
            "meta": "Termine di ricorso di 30 giorni, autorità competente, effetto sospensivo: le regole della procedura amministrativa federale e cantonale.",
            "sections": [
                {"heading": "Il principio: due livelli di regole", "paragraphs": [
                    "La procedura di ricorso contro una decisione di un'autorità federale è disciplinata dalla legge federale sulla procedura amministrativa (PA). Le decisioni delle autorità cantonali e comunali rientrano invece nelle leggi cantonali di procedura amministrativa, il cui contenuto varia da Cantone a Cantone, anche se i principi generali (diritto di essere sentiti, termine di ricorso, motivazione) sono simili.",
                ]},
                {"heading": "Il termine di ricorso", "paragraphs": [
                    "A livello federale, il termine di ricorso contro una decisione è di 30 giorni dalla sua notifica (art. 50 PA), salvo disposizioni speciali che prevedano un termine diverso. I termini cantonali sono generalmente vicini a questa durata, ma possono differire: occorre verificare imperativamente il termine indicato nell'indicazione dei rimedi giuridici che figura in calce alla decisione stessa.",
                ]},
                {"heading": "La forma del ricorso", "paragraphs": [
                    "Il ricorso deve in linea di principio essere indirizzato per scritto all'autorità di ricorso designata nella decisione, contenere conclusioni e una motivazione, ed essere accompagnato dalla decisione impugnata. Una decisione che non menziona correttamente i rimedi giuridici (autorità competente, termine, forma) non deve in linea di principio recare pregiudizio al suo destinatario se questi agisce entro un termine ragionevole nonostante tale lacuna.",
                ]},
                {"heading": "L'effetto sospensivo", "paragraphs": [
                    "Un ricorso ha in linea di principio effetto sospensivo, ossia impedisce l'esecuzione della decisione impugnata finché l'autorità di ricorso non si è pronunciata, salvo se la legge o l'autorità che ha emesso la decisione lo esclude espressamente per motivi di interesse pubblico o urgenza (art. 55 PA a livello federale).",
                ]},
            ],
            "faq": [
                {"q": "Qual è il termine per ricorrere contro una decisione amministrativa federale?",
                 "a": "30 giorni dalla notifica della decisione (art. 50 PA), salvo disposizione speciale contraria. Il termine esatto applicabile a una decisione cantonale o comunale va verificato nell'indicazione dei rimedi giuridici della decisione stessa."},
                {"q": "Il ricorso impedisce l'esecuzione della decisione contestata?",
                 "a": "In linea di principio sì, un ricorso ha effetto sospensivo, salvo che la legge o l'autorità lo escluda espressamente per motivi di interesse pubblico o urgenza."},
                {"q": "Cosa fare se la decisione non menziona i rimedi giuridici?",
                 "a": "L'assenza o l'inesattezza dell'indicazione dei rimedi giuridici non deve in linea di principio recare pregiudizio al destinatario, a condizione che agisca entro un termine ragionevole non appena viene a conoscenza della possibilità di ricorrere."},
                {"q": "Le regole di ricorso sono le stesse in tutti i Cantoni?",
                 "a": "No, solo le decisioni delle autorità federali rientrano nella legge federale sulla procedura amministrativa (PA); ogni Cantone dispone di una propria legge di procedura amministrativa, con termini e modalità che possono differire."},
            ],
        },
        "en": {
            "slug": "appeal-administrative-decision-deadlines-procedure",
            "title": "Appealing an administrative decision",
            "meta": "30-day appeal deadline, competent authority, suspensive effect: the rules of federal and cantonal administrative procedure.",
            "sections": [
                {"heading": "The principle: two levels of rules", "paragraphs": [
                    "The procedure for appealing a decision of a federal authority is governed by the federal Administrative Procedure Act (PA). Decisions of cantonal and municipal authorities, on the other hand, fall under cantonal administrative procedure laws, the content of which varies from canton to canton, even though the general principles (right to be heard, appeal deadline, reasoning) are similar.",
                ]},
                {"heading": "The appeal deadline", "paragraphs": [
                    "At federal level, the deadline to appeal a decision is 30 days from its notification (art. 50 PA), subject to special provisions setting a different deadline. Cantonal deadlines are generally close to this duration, but may differ: it is essential to check the deadline stated in the notice of legal remedies at the bottom of the decision itself.",
                ]},
                {"heading": "The form of the appeal", "paragraphs": [
                    "The appeal must in principle be addressed in writing to the appeal authority designated in the decision, contain submissions and reasoning, and be accompanied by the contested decision. A decision that incorrectly states the legal remedies (competent authority, deadline, form) should in principle cause no prejudice to its recipient if they act within a reasonable time despite this gap.",
                ]},
                {"heading": "Suspensive effect", "paragraphs": [
                    "An appeal in principle has suspensive effect, meaning it prevents enforcement of the contested decision until the appeal authority has ruled, unless the law or the authority that issued the decision expressly excludes this for reasons of public interest or urgency (art. 55 PA at federal level).",
                ]},
            ],
            "faq": [
                {"q": "What is the deadline to appeal a federal administrative decision?",
                 "a": "30 days from notification of the decision (art. 50 PA), subject to a contrary special provision. The exact deadline applicable to a cantonal or municipal decision must be checked in the notice of legal remedies in the decision itself."},
                {"q": "Does an appeal prevent enforcement of the contested decision?",
                 "a": "In principle yes, an appeal has suspensive effect, unless the law or the authority expressly excludes it for reasons of public interest or urgency."},
                {"q": "What should I do if the decision does not state the legal remedies?",
                 "a": "The absence or inaccuracy of the notice of legal remedies should in principle cause no prejudice to the recipient, provided they act within a reasonable time as soon as they become aware of the possibility of appealing."},
                {"q": "Are the appeal rules the same in every canton?",
                 "a": "No, only decisions of federal authorities fall under the federal Administrative Procedure Act (PA); each canton has its own administrative procedure law, with deadlines and procedures that may differ."},
            ],
        },
    },
    "marches-publics-soumissionnaires-evinces": {
        "domaine_id": "droit_administratif",
        "published": "2026-07-30",
        "fr": {
            "slug": "marches-publics-droits-soumissionnaires-evinces",
            "title": "Marchés publics : droits des soumissionnaires évincés",
            "meta": "Adjudication, recours contre l'attribution d'un marché public, délais courts : ce que prévoient l'AIMP et la loi fédérale sur les marchés publics.",
            "sections": [
                {"heading": "Le cadre légal", "paragraphs": [
                    "Les marchés publics en Suisse sont régis, selon le niveau concerné, par la loi fédérale sur les marchés publics (LMP) pour la Confédération, et par l'Accord intercantonal sur les marchés publics (AIMP) et les lois cantonales d'application pour les cantons et communes. Ces règles visent notamment à garantir une concurrence transparente et non discriminatoire entre soumissionnaires.",
                ]},
                {"heading": "La décision d'adjudication", "paragraphs": [
                    "L'attribution du marché à un soumissionnaire fait l'objet d'une décision d'adjudication, notifiée à tous les participants à la procédure. Cette décision doit indiquer les motifs essentiels de l'attribution et les voies de recours ouvertes aux soumissionnaires évincés.",
                ]},
                {"heading": "Le recours contre l'adjudication", "paragraphs": [
                    "Un soumissionnaire évincé peut contester la décision d'adjudication devant l'autorité de recours compétente (tribunal cantonal ou fédéral selon le niveau du marché), généralement dans un délai particulièrement court, de l'ordre de dix à vingt jours selon la législation applicable : il est essentiel de vérifier le délai exact indiqué dans la décision elle-même sans attendre.",
                ]},
                {"heading": "Les motifs de recours usuels", "paragraphs": [
                    "Les recours portent le plus souvent sur le non-respect des critères d'adjudication annoncés, une évaluation incohérente des offres, une exclusion injustifiée de la procédure, ou une violation des principes de transparence et d'égalité de traitement entre soumissionnaires.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai un soumissionnaire évincé peut-il recourir ?",
                 "a": "Le délai est particulièrement court en matière de marchés publics, généralement de l'ordre de dix à vingt jours selon la législation applicable. Il faut impérativement vérifier le délai exact indiqué dans la décision d'adjudication notifiée."},
                {"q": "Un marché public cantonal et un marché fédéral suivent-ils les mêmes règles ?",
                 "a": "Non, un marché fédéral relève de la loi fédérale sur les marchés publics (LMP), tandis qu'un marché cantonal ou communal relève de l'Accord intercantonal sur les marchés publics (AIMP) et de la loi cantonale d'application, dont les modalités procédurales peuvent différer."},
                {"q": "Sur quels motifs puis-je contester une adjudication ?",
                 "a": "Notamment le non-respect des critères d'adjudication annoncés, une évaluation incohérente des offres, une exclusion injustifiée, ou une violation des principes de transparence et d'égalité de traitement entre soumissionnaires."},
            ],
        },
        "de": {
            "slug": "oeffentliches-beschaffungswesen-rechte-abgewiesene-anbieter",
            "title": "Öffentliches Beschaffungswesen: Rechte abgewiesener Anbieter",
            "meta": "Zuschlagsverfügung, Beschwerde gegen die Vergabe eines öffentlichen Auftrags, kurze Fristen: was das interkantonale und Bundesrecht vorsehen.",
            "sections": [
                {"heading": "Der rechtliche Rahmen", "paragraphs": [
                    "Das öffentliche Beschaffungswesen in der Schweiz richtet sich, je nach Ebene, nach dem Bundesgesetz über das öffentliche Beschaffungswesen (BöB) für den Bund und nach der Interkantonalen Vereinbarung über das öffentliche Beschaffungswesen (IVöB) sowie den kantonalen Ausführungsgesetzen für Kantone und Gemeinden. Diese Regeln bezwecken namentlich einen transparenten und diskriminierungsfreien Wettbewerb zwischen den Anbietenden.",
                ]},
                {"heading": "Die Zuschlagsverfügung", "paragraphs": [
                    "Die Vergabe des Auftrags an eine anbietende Person erfolgt durch eine Zuschlagsverfügung, die allen am Verfahren Beteiligten eröffnet wird. Diese Verfügung muss die wesentlichen Gründe des Zuschlags sowie die den abgewiesenen Anbietenden offenstehenden Rechtsmittel angeben.",
                ]},
                {"heading": "Die Beschwerde gegen den Zuschlag", "paragraphs": [
                    "Eine abgewiesene anbietende Person kann die Zuschlagsverfügung bei der zuständigen Beschwerdeinstanz (kantonales oder Bundesgericht je nach Ebene des Auftrags) anfechten, in der Regel innert einer besonders kurzen Frist von etwa zehn bis zwanzig Tagen je nach anwendbarem Recht: es ist unerlässlich, die in der Verfügung selbst angegebene genaue Frist unverzüglich zu prüfen.",
                ]},
                {"heading": "Die üblichen Beschwerdegründe", "paragraphs": [
                    "Beschwerden betreffen meist die Nichteinhaltung der angekündigten Zuschlagskriterien, eine widersprüchliche Bewertung der Angebote, einen ungerechtfertigten Ausschluss vom Verfahren, oder eine Verletzung der Grundsätze der Transparenz und der Gleichbehandlung der Anbietenden.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist kann eine abgewiesene anbietende Person Beschwerde erheben?",
                 "a": "Die Frist ist im öffentlichen Beschaffungswesen besonders kurz, in der Regel etwa zehn bis zwanzig Tage je nach anwendbarem Recht. Es ist unerlässlich, die genaue in der eröffneten Zuschlagsverfügung angegebene Frist zu prüfen."},
                {"q": "Unterliegen ein kantonaler und ein Bundesauftrag denselben Regeln?",
                 "a": "Nein, ein Bundesauftrag richtet sich nach dem Bundesgesetz über das öffentliche Beschaffungswesen (BöB), während ein kantonaler oder kommunaler Auftrag der Interkantonalen Vereinbarung über das öffentliche Beschaffungswesen (IVöB) und dem kantonalen Ausführungsgesetz unterliegt, deren Verfahrensmodalitäten abweichen können."},
                {"q": "Aus welchen Gründen kann ich einen Zuschlag anfechten?",
                 "a": "Namentlich wegen Nichteinhaltung der angekündigten Zuschlagskriterien, widersprüchlicher Bewertung der Angebote, ungerechtfertigtem Ausschluss, oder Verletzung der Grundsätze der Transparenz und Gleichbehandlung der Anbietenden."},
            ],
        },
        "it": {
            "slug": "appalti-pubblici-diritti-offerenti-esclusi",
            "title": "Appalti pubblici: diritti degli offerenti esclusi",
            "meta": "Decisione di aggiudicazione, ricorso contro l'attribuzione di un appalto pubblico, termini brevi: quanto previsto dal diritto intercantonale e federale.",
            "sections": [
                {"heading": "Il quadro legale", "paragraphs": [
                    "Gli appalti pubblici in Svizzera sono disciplinati, a seconda del livello, dalla legge federale sugli appalti pubblici per la Confederazione, e dal Concordato intercantonale sugli appalti pubblici e dalle leggi cantonali di applicazione per i Cantoni e i Comuni. Queste regole mirano in particolare a garantire una concorrenza trasparente e non discriminatoria tra gli offerenti.",
                ]},
                {"heading": "La decisione di aggiudicazione", "paragraphs": [
                    "L'attribuzione dell'appalto a un offerente è oggetto di una decisione di aggiudicazione, notificata a tutti i partecipanti alla procedura. Questa decisione deve indicare i motivi essenziali dell'attribuzione e le vie di ricorso aperte agli offerenti esclusi.",
                ]},
                {"heading": "Il ricorso contro l'aggiudicazione", "paragraphs": [
                    "Un offerente escluso può contestare la decisione di aggiudicazione davanti all'autorità di ricorso competente (tribunale cantonale o federale a seconda del livello dell'appalto), generalmente entro un termine particolarmente breve, dell'ordine di dieci-venti giorni a seconda della legislazione applicabile: è essenziale verificare senza indugio il termine esatto indicato nella decisione stessa.",
                ]},
                {"heading": "I motivi di ricorso usuali", "paragraphs": [
                    "I ricorsi riguardano più spesso il mancato rispetto dei criteri di aggiudicazione annunciati, una valutazione incoerente delle offerte, un'esclusione ingiustificata dalla procedura, o una violazione dei principi di trasparenza e parità di trattamento tra offerenti.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine un offerente escluso può ricorrere?",
                 "a": "Il termine è particolarmente breve in materia di appalti pubblici, generalmente dell'ordine di dieci-venti giorni a seconda della legislazione applicabile. È essenziale verificare il termine esatto indicato nella decisione di aggiudicazione notificata."},
                {"q": "Un appalto cantonale e un appalto federale seguono le stesse regole?",
                 "a": "No, un appalto federale rientra nella legge federale sugli appalti pubblici, mentre un appalto cantonale o comunale rientra nel Concordato intercantonale sugli appalti pubblici e nella legge cantonale di applicazione, le cui modalità procedurali possono differire."},
                {"q": "Su quali motivi posso contestare un'aggiudicazione?",
                 "a": "In particolare il mancato rispetto dei criteri di aggiudicazione annunciati, una valutazione incoerente delle offerte, un'esclusione ingiustificata, o una violazione dei principi di trasparenza e parità di trattamento tra offerenti."},
            ],
        },
        "en": {
            "slug": "public-procurement-rights-unsuccessful-bidders",
            "title": "Public procurement: rights of unsuccessful bidders",
            "meta": "Award decision, appeal against a public contract award, short deadlines: what intercantonal and federal law provide.",
            "sections": [
                {"heading": "The legal framework", "paragraphs": [
                    "Public procurement in Switzerland is governed, depending on the level, by the federal Public Procurement Act for the Confederation, and by the Intercantonal Agreement on Public Procurement and cantonal implementing laws for cantons and municipalities. These rules aim in particular to ensure transparent, non-discriminatory competition among bidders.",
                ]},
                {"heading": "The award decision", "paragraphs": [
                    "The award of a contract to a bidder is the subject of an award decision, notified to all participants in the procedure. This decision must state the essential grounds for the award and the legal remedies available to unsuccessful bidders.",
                ]},
                {"heading": "Appealing the award", "paragraphs": [
                    "An unsuccessful bidder can challenge the award decision before the competent appeal authority (cantonal or federal court depending on the level of the contract), generally within a particularly short deadline, on the order of ten to twenty days depending on the applicable legislation: it is essential to check the exact deadline stated in the decision itself without delay.",
                ]},
                {"heading": "Common grounds for appeal", "paragraphs": [
                    "Appeals most often concern failure to comply with the announced award criteria, inconsistent evaluation of bids, unjustified exclusion from the procedure, or a violation of the principles of transparency and equal treatment of bidders.",
                ]},
            ],
            "faq": [
                {"q": "Within what deadline can an unsuccessful bidder appeal?",
                 "a": "The deadline is particularly short in public procurement matters, generally on the order of ten to twenty days depending on the applicable legislation. It is essential to check the exact deadline stated in the notified award decision."},
                {"q": "Do a cantonal contract and a federal contract follow the same rules?",
                 "a": "No, a federal contract falls under the federal Public Procurement Act, while a cantonal or municipal contract falls under the Intercantonal Agreement on Public Procurement and the cantonal implementing law, whose procedural details may differ."},
                {"q": "On what grounds can I challenge an award?",
                 "a": "In particular failure to comply with the announced award criteria, inconsistent evaluation of bids, unjustified exclusion, or a violation of the principles of transparency and equal treatment of bidders."},
            ],
        },
    },
    "permis-sejour-b-c-l-conditions": {
        "domaine_id": "droit_etrangers",
        "published": "2026-07-30",
        "fr": {
            "slug": "permis-sejour-b-c-l-conditions-differences",
            "title": "Permis de séjour B, C, L : conditions et différences",
            "meta": "Autorisation de courte durée, de séjour, d'établissement : les différents permis prévus par la loi sur les étrangers et l'intégration.",
            "sections": [
                {"heading": "Le permis L, autorisation de courte durée", "paragraphs": [
                    "Le permis L est délivré pour un séjour d'une durée limitée, généralement liée à un contrat de travail de courte durée ou à un but spécifique et temporaire. Sa durée de validité est en principe limitée à une année, avec possibilité de prolongation dans certaines limites selon la loi sur les étrangers et l'intégration (LEI).",
                ]},
                {"heading": "Le permis B, autorisation de séjour", "paragraphs": [
                    "Le permis B est délivré pour un séjour de plus longue durée, généralement dans le cadre d'une activité lucrative, d'études, ou d'un regroupement familial. Sa durée de validité initiale est en principe d'une année, renouvelable selon le maintien des conditions d'octroi, avec des règles différentes selon que le titulaire est ressortissant de l'UE/AELE ou d'un État tiers.",
                ]},
                {"heading": "Le permis C, autorisation d'établissement", "paragraphs": [
                    "Le permis C confère un droit de séjour stable et à durée indéterminée, avec un accès en principe équivalent à celui des citoyens suisses pour la plupart des activités économiques. Il est en principe accordé après une période de séjour préalable ininterrompue en Suisse, dont la durée varie selon la nationalité du requérant et l'existence d'accords bilatéraux, sous réserve d'un examen de l'intégration.",
                ]},
                {"heading": "Le renouvellement et les conditions de maintien", "paragraphs": [
                    "Le maintien d'un permis B ou L dépend du respect continu des conditions d'octroi (activité lucrative, moyens de subsistance suffisants, absence de motifs de révocation tels qu'une dépendance durable à l'aide sociale ou une atteinte grave à la sécurité et l'ordre publics). Un permis C peut également être révoqué dans des cas graves prévus par la loi.",
                ]},
            ],
            "faq": [
                {"q": "Quelle est la différence principale entre le permis B et le permis C ?",
                 "a": "Le permis B est une autorisation de séjour renouvelable, soumise au maintien des conditions d'octroi, tandis que le permis C est une autorisation d'établissement à durée indéterminée, offrant une plus grande stabilité et un accès en principe équivalent à celui des citoyens suisses pour la plupart des activités économiques."},
                {"q": "Combien de temps faut-il pour obtenir un permis C ?",
                 "a": "Cela dépend de la nationalité du requérant et des accords bilatéraux applicables : les durées de séjour préalable exigées varient sensiblement selon les situations. Il convient de vérifier sa situation précise auprès de l'autorité migratoire cantonale compétente."},
                {"q": "Un permis L peut-il être transformé en permis B ?",
                 "a": "Dans certains cas, oui, si les conditions d'octroi d'un permis B sont remplies avant l'échéance du permis L, mais cela n'est pas automatique et dépend de la situation individuelle et de la pratique de l'autorité migratoire cantonale."},
            ],
        },
        "de": {
            "slug": "aufenthaltsbewilligung-b-c-l-voraussetzungen-unterschiede",
            "title": "Aufenthaltsbewilligung B, C, L: Voraussetzungen",
            "meta": "Kurzaufenthaltsbewilligung, Aufenthaltsbewilligung, Niederlassungsbewilligung: die verschiedenen im Ausländer- und Integrationsgesetz vorgesehenen Bewilligungen.",
            "sections": [
                {"heading": "Der Ausweis L, die Kurzaufenthaltsbewilligung", "paragraphs": [
                    "Der Ausweis L wird für einen befristeten Aufenthalt erteilt, meist im Zusammenhang mit einem befristeten Arbeitsvertrag oder einem spezifischen, vorübergehenden Zweck. Seine Gültigkeitsdauer ist grundsätzlich auf ein Jahr beschränkt, mit Verlängerungsmöglichkeit innerhalb bestimmter Grenzen gemäss dem Ausländer- und Integrationsgesetz (AIG).",
                ]},
                {"heading": "Der Ausweis B, die Aufenthaltsbewilligung", "paragraphs": [
                    "Der Ausweis B wird für einen längeren Aufenthalt erteilt, meist im Rahmen einer Erwerbstätigkeit, eines Studiums, oder eines Familiennachzugs. Seine anfängliche Gültigkeitsdauer beträgt grundsätzlich ein Jahr, erneuerbar je nach Fortbestand der Erteilungsvoraussetzungen, mit unterschiedlichen Regeln, je nachdem ob die Inhaberin oder der Inhaber Staatsangehörige oder Staatsangehöriger eines EU/EFTA-Staates oder eines Drittstaates ist.",
                ]},
                {"heading": "Der Ausweis C, die Niederlassungsbewilligung", "paragraphs": [
                    "Der Ausweis C verleiht ein stabiles und unbefristetes Aufenthaltsrecht, mit einem Zugang zu den meisten Erwerbstätigkeiten, der grundsätzlich jenem der Schweizer Staatsangehörigen entspricht. Er wird grundsätzlich nach einer vorangehenden ununterbrochenen Aufenthaltsdauer in der Schweiz erteilt, deren Länge je nach Staatsangehörigkeit der Gesuchstellerin oder des Gesuchstellers und dem Bestehen bilateraler Abkommen variiert, vorbehältlich einer Integrationsprüfung.",
                ]},
                {"heading": "Die Erneuerung und die Aufrechterhaltungsvoraussetzungen", "paragraphs": [
                    "Die Aufrechterhaltung eines Ausweises B oder L hängt von der fortlaufenden Einhaltung der Erteilungsvoraussetzungen ab (Erwerbstätigkeit, ausreichende Mittel, Fehlen von Widerrufsgründen wie dauerhafte Sozialhilfeabhängigkeit oder schwere Gefährdung der Sicherheit und öffentlichen Ordnung). Auch ein Ausweis C kann in gesetzlich vorgesehenen schwerwiegenden Fällen widerrufen werden.",
                ]},
            ],
            "faq": [
                {"q": "Was ist der Hauptunterschied zwischen Ausweis B und Ausweis C?",
                 "a": "Der Ausweis B ist eine erneuerbare Aufenthaltsbewilligung, die an die fortlaufende Einhaltung der Erteilungsvoraussetzungen gebunden ist, während der Ausweis C eine unbefristete Niederlassungsbewilligung ist, die mehr Stabilität und einen grundsätzlich den Schweizer Staatsangehörigen gleichgestellten Zugang zu den meisten Erwerbstätigkeiten bietet."},
                {"q": "Wie lange dauert es, um den Ausweis C zu erhalten?",
                 "a": "Dies hängt von der Staatsangehörigkeit der Gesuchstellerin oder des Gesuchstellers und den anwendbaren bilateralen Abkommen ab: die erforderlichen vorangehenden Aufenthaltsdauern variieren erheblich je nach Situation. Es empfiehlt sich, die genaue Situation bei der zuständigen kantonalen Migrationsbehörde zu prüfen."},
                {"q": "Kann ein Ausweis L in einen Ausweis B umgewandelt werden?",
                 "a": "In bestimmten Fällen ja, wenn die Erteilungsvoraussetzungen für einen Ausweis B vor Ablauf des Ausweises L erfüllt sind, doch dies erfolgt nicht automatisch und hängt von der individuellen Situation und der Praxis der zuständigen kantonalen Migrationsbehörde ab."},
            ],
        },
        "it": {
            "slug": "permesso-soggiorno-b-c-l-condizioni-differenze",
            "title": "Permesso di soggiorno B, C, L: condizioni",
            "meta": "Permesso di dimora di breve durata, permesso di dimora annuale, permesso di domicilio: i diversi permessi previsti dalla legge sugli stranieri e la loro integrazione.",
            "sections": [
                {"heading": "Il permesso L, dimora di breve durata", "paragraphs": [
                    "Il permesso L viene rilasciato per un soggiorno di durata limitata, generalmente legato a un contratto di lavoro di breve durata o a uno scopo specifico e temporaneo. La sua durata di validità è in linea di principio limitata a un anno, con possibilità di proroga entro determinati limiti secondo la legge federale sugli stranieri e la loro integrazione (LStrI).",
                ]},
                {"heading": "Il permesso B, dimora annuale", "paragraphs": [
                    "Il permesso B viene rilasciato per un soggiorno di più lunga durata, generalmente nell'ambito di un'attività lucrativa, di studi, o di un ricongiungimento familiare. La sua durata di validità iniziale è in linea di principio di un anno, rinnovabile secondo il mantenimento delle condizioni di rilascio, con regole diverse a seconda che il titolare sia cittadino UE/AELS o di uno Stato terzo.",
                ]},
                {"heading": "Il permesso C, domicilio", "paragraphs": [
                    "Il permesso C conferisce un diritto di soggiorno stabile e a tempo indeterminato, con un accesso in linea di principio equivalente a quello dei cittadini svizzeri per la maggior parte delle attività economiche. È in linea di principio concesso dopo un periodo di soggiorno preliminare ininterrotto in Svizzera, la cui durata varia secondo la nazionalità del richiedente e l'esistenza di accordi bilaterali, con riserva di un esame dell'integrazione.",
                ]},
                {"heading": "Il rinnovo e le condizioni di mantenimento", "paragraphs": [
                    "Il mantenimento di un permesso B o L dipende dal rispetto continuo delle condizioni di rilascio (attività lucrativa, mezzi di sussistenza sufficienti, assenza di motivi di revoca come una dipendenza duratura dall'aiuto sociale o una minaccia grave alla sicurezza e all'ordine pubblici). Anche un permesso C può essere revocato in casi gravi previsti dalla legge.",
                ]},
            ],
            "faq": [
                {"q": "Qual è la differenza principale tra il permesso B e il permesso C?",
                 "a": "Il permesso B è un'autorizzazione di soggiorno rinnovabile, soggetta al mantenimento delle condizioni di rilascio, mentre il permesso C è un'autorizzazione di domicilio a tempo indeterminato, che offre maggiore stabilità e un accesso in linea di principio equivalente a quello dei cittadini svizzeri per la maggior parte delle attività economiche."},
                {"q": "Quanto tempo occorre per ottenere il permesso C?",
                 "a": "Ciò dipende dalla nazionalità del richiedente e dagli accordi bilaterali applicabili: le durate di soggiorno preliminare richieste variano notevolmente a seconda delle situazioni. Conviene verificare la propria situazione precisa presso l'autorità cantonale della migrazione competente."},
                {"q": "Un permesso L può essere trasformato in permesso B?",
                 "a": "In alcuni casi sì, se le condizioni di rilascio di un permesso B sono soddisfatte prima della scadenza del permesso L, ma ciò non è automatico e dipende dalla situazione individuale e dalla prassi dell'autorità cantonale della migrazione."},
            ],
        },
        "en": {
            "slug": "residence-permit-b-c-l-conditions-differences",
            "title": "Residence permits B, C, L: conditions and differences",
            "meta": "Short-term residence permit, residence permit, settlement permit: the different permits provided by the Foreign Nationals and Integration Act.",
            "sections": [
                {"heading": "Permit L, short-term residence", "paragraphs": [
                    "Permit L is issued for a limited period of residence, usually linked to a short-term employment contract or a specific, temporary purpose. Its validity is in principle limited to one year, with the possibility of extension within certain limits under the Foreign Nationals and Integration Act (FNIA).",
                ]},
                {"heading": "Permit B, residence permit", "paragraphs": [
                    "Permit B is issued for a longer stay, usually as part of gainful employment, studies, or family reunification. Its initial validity is in principle one year, renewable subject to the continued fulfilment of the conditions for issue, with different rules depending on whether the holder is a national of an EU/EFTA state or a third country.",
                ]},
                {"heading": "Permit C, settlement permit", "paragraphs": [
                    "Permit C confers a stable, indefinite right of residence, with access in principle equivalent to that of Swiss nationals for most economic activities. It is in principle granted after a prior uninterrupted period of residence in Switzerland, the length of which varies according to the applicant's nationality and the existence of bilateral agreements, subject to an integration assessment.",
                ]},
                {"heading": "Renewal and conditions for maintaining the permit", "paragraphs": [
                    "Maintaining a permit B or L depends on the continued fulfilment of the conditions for issue (gainful employment, sufficient means, absence of grounds for revocation such as lasting dependence on social assistance or a serious threat to security and public order). A permit C can also be revoked in serious cases provided by law.",
                ]},
            ],
            "faq": [
                {"q": "What is the main difference between permit B and permit C?",
                 "a": "Permit B is a renewable residence permit, subject to the continued fulfilment of the conditions for issue, while permit C is an indefinite settlement permit, offering greater stability and access in principle equivalent to that of Swiss nationals for most economic activities."},
                {"q": "How long does it take to obtain permit C?",
                 "a": "This depends on the applicant's nationality and the applicable bilateral agreements: the required prior periods of residence vary considerably depending on the situation. It is advisable to check your specific situation with the competent cantonal migration authority."},
                {"q": "Can a permit L be converted into a permit B?",
                 "a": "In certain cases yes, if the conditions for issuing a permit B are met before the permit L expires, but this is not automatic and depends on the individual situation and the practice of the competent cantonal migration authority."},
            ],
        },
    },
    "regroupement-familial-faire-venir-famille": {
        "domaine_id": "droit_etrangers",
        "published": "2026-07-30",
        "fr": {
            "slug": "regroupement-familial-faire-venir-sa-famille-suisse",
            "title": "Regroupement familial : faire venir sa famille",
            "meta": "Conditions du regroupement familial pour le conjoint et les enfants, délais légaux : ce que prévoit la loi sur les étrangers et l'intégration.",
            "sections": [
                {"heading": "Les personnes concernées", "paragraphs": [
                    "Les art. 42 à 52 LEI règlent le regroupement familial pour le conjoint, le partenaire enregistré et les enfants célibataires de moins de 18 ans d'un ressortissant suisse, d'un titulaire d'une autorisation d'établissement (permis C) ou d'une autorisation de séjour (permis B), avec des conditions qui varient selon le statut du regroupant.",
                ]},
                {"heading": "Les conditions générales", "paragraphs": [
                    "Le regroupement familial suppose en principe l'existence d'un logement approprié, l'absence de dépendance à l'aide sociale, et pour certaines catégories, le respect de délais légaux pour déposer la demande après l'octroi de l'autorisation du regroupant. Des exigences linguistiques peuvent également s'appliquer selon le statut concerné.",
                ]},
                {"heading": "Le délai pour déposer la demande", "paragraphs": [
                    "La loi prévoit des délais dans lesquels la demande de regroupement familial doit être déposée après l'octroi de l'autorisation de séjour ou d'établissement du regroupant, ou après le mariage ou la naissance de l'enfant si ces événements sont postérieurs. Passé ces délais, le regroupement n'est possible qu'en présence de raisons familiales majeures reconnues par la loi.",
                ]},
                {"heading": "Le regroupement familial des citoyens de l'UE/AELE", "paragraphs": [
                    "Les ressortissants de l'UE/AELE bénéficient de règles de regroupement familial plus favorables découlant de l'accord sur la libre circulation des personnes, avec un cercle de personnes pouvant être regroupées plus large que celui prévu par la LEI pour les ressortissants d'États tiers.",
                ]},
            ],
            "faq": [
                {"q": "Qui peut bénéficier du regroupement familial en Suisse ?",
                 "a": "Le conjoint, le partenaire enregistré et les enfants célibataires de moins de 18 ans d'un ressortissant suisse ou d'un étranger titulaire d'une autorisation de séjour ou d'établissement, selon les conditions des art. 42 à 52 LEI."},
                {"q": "Existe-t-il un délai pour demander le regroupement familial ?",
                 "a": "Oui, la loi fixe des délais après l'octroi de l'autorisation du regroupant ou après le mariage ou la naissance de l'enfant. Passé ce délai, le regroupement n'est possible qu'en présence de raisons familiales majeures reconnues par la loi."},
                {"q": "Les conditions sont-elles les mêmes pour un ressortissant de l'UE et d'un État tiers ?",
                 "a": "Non, les ressortissants de l'UE/AELE bénéficient de règles plus favorables découlant de l'accord sur la libre circulation des personnes, avec un cercle de personnes regroupables plus large que celui prévu par la LEI pour les États tiers."},
            ],
        },
        "de": {
            "slug": "familiennachzug-familie-schweiz-nachholen",
            "title": "Familiennachzug: die Familie in die Schweiz holen",
            "meta": "Voraussetzungen des Familiennachzugs für Ehepartner und Kinder, gesetzliche Fristen: was das Ausländer- und Integrationsgesetz vorsieht.",
            "sections": [
                {"heading": "Die betroffenen Personen", "paragraphs": [
                    "Art. 42-52 AIG regeln den Familiennachzug für die Ehegattin oder den Ehegatten, die eingetragene Partnerin oder den eingetragenen Partner sowie ledige Kinder unter 18 Jahren einer Schweizer Staatsangehörigen oder eines Schweizer Staatsangehörigen, einer Inhaberin oder eines Inhabers einer Niederlassungsbewilligung (Ausweis C) oder einer Aufenthaltsbewilligung (Ausweis B), mit Voraussetzungen, die je nach Status der nachziehenden Person variieren.",
                ]},
                {"heading": "Die allgemeinen Voraussetzungen", "paragraphs": [
                    "Der Familiennachzug setzt grundsätzlich eine angemessene Wohnung, das Fehlen einer Sozialhilfeabhängigkeit sowie für bestimmte Kategorien die Einhaltung gesetzlicher Fristen für die Gesuchseinreichung nach Erteilung der Bewilligung der nachziehenden Person voraus. Je nach betroffenem Status können auch sprachliche Anforderungen gelten.",
                ]},
                {"heading": "Die Frist zur Gesuchseinreichung", "paragraphs": [
                    "Das Gesetz sieht Fristen vor, innerhalb derer das Familiennachzugsgesuch nach Erteilung der Aufenthalts- oder Niederlassungsbewilligung der nachziehenden Person eingereicht werden muss, oder nach der Heirat oder Geburt des Kindes, falls diese Ereignisse später eintreten. Nach Ablauf dieser Fristen ist der Familiennachzug nur noch bei Vorliegen wichtiger familiärer Gründe gemäss Gesetz möglich.",
                ]},
                {"heading": "Der Familiennachzug für EU/EFTA-Staatsangehörige", "paragraphs": [
                    "Staatsangehörige der EU/EFTA profitieren von günstigeren Familiennachzugsregeln, die sich aus dem Freizügigkeitsabkommen ergeben, mit einem grösseren Kreis nachzugsberechtigter Personen als jenem, den das AIG für Staatsangehörige von Drittstaaten vorsieht.",
                ]},
            ],
            "faq": [
                {"q": "Wer kann in der Schweiz vom Familiennachzug profitieren?",
                 "a": "Die Ehegattin oder der Ehegatte, die eingetragene Partnerin oder der eingetragene Partner sowie ledige Kinder unter 18 Jahren einer Schweizer Staatsangehörigen oder eines Schweizer Staatsangehörigen oder einer ausländischen Person mit Aufenthalts- oder Niederlassungsbewilligung, gemäss den Voraussetzungen der Art. 42-52 AIG."},
                {"q": "Gibt es eine Frist zur Beantragung des Familiennachzugs?",
                 "a": "Ja, das Gesetz setzt Fristen nach Erteilung der Bewilligung der nachziehenden Person oder nach der Heirat oder Geburt des Kindes. Nach Ablauf dieser Frist ist der Nachzug nur bei Vorliegen wichtiger familiärer Gründe gemäss Gesetz möglich."},
                {"q": "Gelten für EU-Staatsangehörige und Drittstaatsangehörige dieselben Voraussetzungen?",
                 "a": "Nein, EU/EFTA-Staatsangehörige profitieren von günstigeren Regeln aus dem Freizügigkeitsabkommen, mit einem grösseren Kreis nachzugsberechtigter Personen als jenem, den das AIG für Drittstaaten vorsieht."},
            ],
        },
        "it": {
            "slug": "ricongiungimento-familiare-far-venire-famiglia-svizzera",
            "title": "Ricongiungimento familiare: far venire la famiglia",
            "meta": "Condizioni del ricongiungimento familiare per il coniuge e i figli, termini legali: quanto previsto dalla legge sugli stranieri e la loro integrazione.",
            "sections": [
                {"heading": "Le persone interessate", "paragraphs": [
                    "Gli art. 42-52 LStrI disciplinano il ricongiungimento familiare per il coniuge, il partner registrato e i figli celibi o nubili di meno di 18 anni di un cittadino svizzero, di un titolare di un permesso di domicilio (permesso C) o di un permesso di dimora (permesso B), con condizioni che variano secondo lo status della persona che chiede il ricongiungimento.",
                ]},
                {"heading": "Le condizioni generali", "paragraphs": [
                    "Il ricongiungimento familiare presuppone in linea di principio l'esistenza di un alloggio adeguato, l'assenza di dipendenza dall'aiuto sociale, e per determinate categorie, il rispetto di termini legali per presentare la domanda dopo il rilascio dell'autorizzazione della persona che chiede il ricongiungimento. Possono applicarsi anche requisiti linguistici a seconda dello status interessato.",
                ]},
                {"heading": "Il termine per presentare la domanda", "paragraphs": [
                    "La legge prevede termini entro i quali la domanda di ricongiungimento familiare deve essere presentata dopo il rilascio dell'autorizzazione di soggiorno o di domicilio della persona che chiede il ricongiungimento, o dopo il matrimonio o la nascita del figlio se questi eventi sono posteriori. Trascorsi questi termini, il ricongiungimento è possibile solo in presenza di gravi motivi familiari riconosciuti dalla legge.",
                ]},
                {"heading": "Il ricongiungimento familiare dei cittadini UE/AELS", "paragraphs": [
                    "I cittadini dell'UE/AELS beneficiano di regole di ricongiungimento familiare più favorevoli derivanti dall'accordo sulla libera circolazione delle persone, con una cerchia di persone ricongiungibili più ampia di quella prevista dalla LStrI per i cittadini di Stati terzi.",
                ]},
            ],
            "faq": [
                {"q": "Chi può beneficiare del ricongiungimento familiare in Svizzera?",
                 "a": "Il coniuge, il partner registrato e i figli celibi o nubili di meno di 18 anni di un cittadino svizzero o di uno straniero titolare di un permesso di dimora o di domicilio, secondo le condizioni degli art. 42-52 LStrI."},
                {"q": "Esiste un termine per chiedere il ricongiungimento familiare?",
                 "a": "Sì, la legge fissa termini dopo il rilascio dell'autorizzazione della persona che chiede il ricongiungimento o dopo il matrimonio o la nascita del figlio. Trascorso questo termine, il ricongiungimento è possibile solo in presenza di gravi motivi familiari riconosciuti dalla legge."},
                {"q": "Le condizioni sono le stesse per un cittadino UE e uno di uno Stato terzo?",
                 "a": "No, i cittadini dell'UE/AELS beneficiano di regole più favorevoli derivanti dall'accordo sulla libera circolazione delle persone, con una cerchia di persone ricongiungibili più ampia di quella prevista dalla LStrI per gli Stati terzi."},
            ],
        },
        "en": {
            "slug": "family-reunification-bringing-family-switzerland",
            "title": "Family reunification: bringing your family to Switzerland",
            "meta": "Conditions for family reunification of a spouse and children, statutory deadlines: what the Foreign Nationals and Integration Act provides.",
            "sections": [
                {"heading": "Who is covered", "paragraphs": [
                    "Art. 42-52 FNIA govern family reunification for the spouse, registered partner, and unmarried children under 18 of a Swiss national, a holder of a settlement permit (permit C), or a holder of a residence permit (permit B), with conditions that vary according to the status of the sponsoring person.",
                ]},
                {"heading": "The general conditions", "paragraphs": [
                    "Family reunification in principle requires suitable housing, no dependence on social assistance, and for certain categories, compliance with statutory deadlines for filing the application after the sponsor's permit is issued. Language requirements may also apply depending on the status concerned.",
                ]},
                {"heading": "The deadline to file the application", "paragraphs": [
                    "The law sets deadlines within which the family reunification application must be filed after the sponsor's residence or settlement permit is issued, or after the marriage or birth of the child if these events occur later. After these deadlines, reunification is only possible where important family reasons recognised by law exist.",
                ]},
                {"heading": "Family reunification for EU/EFTA nationals", "paragraphs": [
                    "EU/EFTA nationals benefit from more favourable family reunification rules arising from the agreement on the free movement of persons, with a broader circle of persons eligible for reunification than that provided for third-country nationals under the FNIA.",
                ]},
            ],
            "faq": [
                {"q": "Who can benefit from family reunification in Switzerland?",
                 "a": "The spouse, registered partner, and unmarried children under 18 of a Swiss national or of a foreign national holding a residence or settlement permit, under the conditions of art. 42-52 FNIA."},
                {"q": "Is there a deadline to apply for family reunification?",
                 "a": "Yes, the law sets deadlines after the sponsor's permit is issued or after the marriage or birth of the child. After this deadline, reunification is only possible where important family reasons recognised by law exist."},
                {"q": "Are the conditions the same for an EU national and a third-country national?",
                 "a": "No, EU/EFTA nationals benefit from more favourable rules arising from the agreement on the free movement of persons, with a broader circle of persons eligible for reunification than that provided for third countries under the FNIA."},
            ],
        },
    },
    "assurance-perte-gain-maladie-carence": {
        "domaine_id": "droit_assurances",
        "published": "2026-07-30",
        "fr": {
            "slug": "assurance-perte-gain-maladie-delai-carence",
            "title": "Assurance perte de gain maladie : droits et carence",
            "meta": "Assurance facultative régie par la LCA, délai de carence, durée des prestations : ce qu'il faut savoir sur la perte de gain maladie.",
            "sections": [
                {"heading": "Une assurance de nature contractuelle", "paragraphs": [
                    "Contrairement à l'assurance-maladie de base, l'assurance perte de gain en cas de maladie n'est en Suisse pas obligatoire pour les employés au niveau fédéral, sauf obligation prévue par une convention collective de travail ou un contrat individuel. Lorsqu'elle existe, elle relève le plus souvent de la loi fédérale sur le contrat d'assurance (LCA), ce qui la distingue des assurances sociales régies par la LPGA.",
                ]},
                {"heading": "Le délai de carence", "paragraphs": [
                    "Le délai de carence est la période, définie par le contrat d'assurance, pendant laquelle aucune prestation n'est versée après le début de l'incapacité de travail. Sa durée varie selon les contrats, allant généralement de quelques jours à plusieurs semaines : il faut se référer aux conditions générales du contrat concerné pour connaître le délai applicable.",
                ]},
                {"heading": "La durée des prestations", "paragraphs": [
                    "La durée pendant laquelle l'indemnité journalière est versée est également fixée par le contrat, le plus souvent limitée à une durée maximale de plusieurs mois à quelques années selon le produit d'assurance souscrit. Cette durée s'articule avec l'obligation de maintien du salaire par l'employeur prévue par l'art. 324a CO en l'absence d'une telle assurance.",
                ]},
                {"heading": "L'articulation avec l'obligation légale de l'employeur", "paragraphs": [
                    "En l'absence d'assurance perte de gain maladie, l'employeur reste tenu de verser le salaire pendant un temps limité en cas d'empêchement de travailler sans faute du travailleur (art. 324a CO), la durée dépendant de l'ancienneté et variant selon les échelles cantonales usuelles (échelle bernoise, bâloise, ou zurichoise selon le canton).",
                ]},
            ],
            "faq": [
                {"q": "L'assurance perte de gain maladie est-elle obligatoire ?",
                 "a": "Elle n'est en principe pas obligatoire au niveau fédéral pour les employés, sauf si une convention collective de travail applicable ou le contrat de travail individuel le prévoit."},
                {"q": "Qu'est-ce que le délai de carence ?",
                 "a": "La période, fixée par le contrat d'assurance, pendant laquelle aucune indemnité n'est versée après le début de l'incapacité de travail. Sa durée dépend entièrement des conditions contractuelles souscrites."},
                {"q": "Que se passe-t-il si mon employeur n'a pas souscrit d'assurance perte de gain ?",
                 "a": "Il reste tenu, selon l'art. 324a CO, de verser le salaire pendant un temps limité en cas d'incapacité de travail sans faute du travailleur, la durée dépendant de l'ancienneté et de l'échelle cantonale applicable."},
            ],
        },
        "de": {
            "slug": "krankentaggeldversicherung-rechte-wartefrist",
            "title": "Krankentaggeldversicherung: Rechte und Wartefrist",
            "meta": "Fakultative, dem VVG unterstehende Versicherung, Wartefrist, Leistungsdauer: was Sie zum Krankentaggeld wissen müssen.",
            "sections": [
                {"heading": "Eine Versicherung vertraglicher Natur", "paragraphs": [
                    "Im Gegensatz zur obligatorischen Krankenpflegeversicherung ist die Krankentaggeldversicherung in der Schweiz für Arbeitnehmende auf Bundesebene nicht obligatorisch, ausser eine anwendbare Gesamtarbeitsvertrag oder der Einzelarbeitsvertrag sieht dies vor. Sofern sie besteht, untersteht sie meist dem Bundesgesetz über den Versicherungsvertrag (VVG), was sie von den durch das ATSG geregelten Sozialversicherungen unterscheidet.",
                ]},
                {"heading": "Die Wartefrist", "paragraphs": [
                    "Die Wartefrist ist der im Versicherungsvertrag festgelegte Zeitraum, während dem nach Beginn der Arbeitsunfähigkeit keine Leistung ausgerichtet wird. Ihre Dauer variiert je nach Vertrag, in der Regel von wenigen Tagen bis mehreren Wochen: massgebend sind die allgemeinen Vertragsbedingungen des jeweiligen Vertrags.",
                ]},
                {"heading": "Die Leistungsdauer", "paragraphs": [
                    "Die Dauer, während der das Taggeld ausgerichtet wird, wird ebenfalls durch den Vertrag festgelegt, meist begrenzt auf eine Höchstdauer von mehreren Monaten bis wenigen Jahren je nach abgeschlossenem Versicherungsprodukt. Diese Dauer steht im Zusammenhang mit der gesetzlichen Lohnfortzahlungspflicht des Arbeitgebers, falls keine solche Versicherung besteht (Art. 324a OR).",
                ]},
                {"heading": "Das Zusammenspiel mit der gesetzlichen Pflicht des Arbeitgebers", "paragraphs": [
                    "Ohne Krankentaggeldversicherung bleibt der Arbeitgeber verpflichtet, den Lohn während begrenzter Zeit bei unverschuldeter Arbeitsverhinderung weiterzuzahlen (Art. 324a OR), wobei die Dauer von der Dienstdauer abhängt und je nach den üblichen kantonalen Skalen (Berner, Basler oder Zürcher Skala je nach Kanton) variiert.",
                ]},
            ],
            "faq": [
                {"q": "Ist die Krankentaggeldversicherung obligatorisch?",
                 "a": "Sie ist auf Bundesebene für Arbeitnehmende grundsätzlich nicht obligatorisch, ausser ein anwendbarer Gesamtarbeitsvertrag oder der Einzelarbeitsvertrag sieht dies vor."},
                {"q": "Was ist die Wartefrist?",
                 "a": "Der im Versicherungsvertrag festgelegte Zeitraum, während dem nach Beginn der Arbeitsunfähigkeit keine Entschädigung ausgerichtet wird. Ihre Dauer hängt vollständig von den abgeschlossenen Vertragsbedingungen ab."},
                {"q": "Was geschieht, wenn mein Arbeitgeber keine Krankentaggeldversicherung abgeschlossen hat?",
                 "a": "Er bleibt gemäss Art. 324a OR verpflichtet, den Lohn während begrenzter Zeit bei unverschuldeter Arbeitsunfähigkeit weiterzuzahlen, wobei die Dauer von der Dienstdauer und der anwendbaren kantonalen Skala abhängt."},
            ],
        },
        "it": {
            "slug": "assicurazione-indennita-perdita-guadagno-malattia-termine-attesa",
            "title": "Assicurazione perdita di guadagno malattia: diritti e attesa",
            "meta": "Assicurazione facoltativa disciplinata dalla LCA, termine di attesa, durata delle prestazioni: quanto occorre sapere sull'indennità di malattia.",
            "sections": [
                {"heading": "Un'assicurazione di natura contrattuale", "paragraphs": [
                    "A differenza dell'assicurazione malattia di base, l'assicurazione d'indennità giornaliera in caso di malattia non è in Svizzera obbligatoria per i dipendenti a livello federale, salvo obbligo previsto da un contratto collettivo di lavoro o da un contratto individuale. Quando esiste, rientra il più delle volte nella legge federale sul contratto d'assicurazione (LCA), il che la distingue dalle assicurazioni sociali disciplinate dalla LPGA.",
                ]},
                {"heading": "Il termine di attesa", "paragraphs": [
                    "Il termine di attesa è il periodo, definito dal contratto d'assicurazione, durante il quale nessuna prestazione viene versata dopo l'inizio dell'incapacità lavorativa. La sua durata varia a seconda dei contratti, generalmente da alcuni giorni a diverse settimane: occorre riferirsi alle condizioni generali del contratto interessato per conoscere il termine applicabile.",
                ]},
                {"heading": "La durata delle prestazioni", "paragraphs": [
                    "La durata durante la quale l'indennità giornaliera viene versata è anch'essa fissata dal contratto, il più delle volte limitata a una durata massima di diversi mesi fino a qualche anno a seconda del prodotto assicurativo sottoscritto. Questa durata si articola con l'obbligo di mantenimento del salario da parte del datore di lavoro previsto dall'art. 324a CO in assenza di tale assicurazione.",
                ]},
                {"heading": "L'articolazione con l'obbligo legale del datore di lavoro", "paragraphs": [
                    "In assenza di assicurazione d'indennità giornaliera per malattia, il datore di lavoro resta tenuto a versare il salario per un tempo limitato in caso di impedimento al lavoro senza colpa del lavoratore (art. 324a CO), con una durata che dipende dall'anzianità e varia secondo le scale cantonali usuali.",
                ]},
            ],
            "faq": [
                {"q": "L'assicurazione d'indennità per perdita di guadagno malattia è obbligatoria?",
                 "a": "In linea di principio non è obbligatoria a livello federale per i dipendenti, salvo se un contratto collettivo di lavoro applicabile o il contratto di lavoro individuale lo prevede."},
                {"q": "Cos'è il termine di attesa?",
                 "a": "Il periodo, fissato dal contratto d'assicurazione, durante il quale nessuna indennità viene versata dopo l'inizio dell'incapacità lavorativa. La sua durata dipende interamente dalle condizioni contrattuali sottoscritte."},
                {"q": "Cosa succede se il mio datore di lavoro non ha sottoscritto un'assicurazione d'indennità giornaliera?",
                 "a": "Resta tenuto, secondo l'art. 324a CO, a versare il salario per un tempo limitato in caso di incapacità lavorativa senza colpa del lavoratore, con una durata che dipende dall'anzianità e dalla scala cantonale applicabile."},
            ],
        },
        "en": {
            "slug": "sickness-daily-allowance-insurance-waiting-period",
            "title": "Sickness daily allowance insurance: rights and waiting period",
            "meta": "Optional insurance governed by the ICA, waiting period, duration of benefits: what to know about sickness daily allowance insurance.",
            "sections": [
                {"heading": "An insurance of a contractual nature", "paragraphs": [
                    "Unlike basic health insurance, sickness daily allowance insurance is not mandatory for employees at federal level in Switzerland, unless required by an applicable collective bargaining agreement or an individual employment contract. Where it exists, it most often falls under the federal Insurance Contract Act (ICA), which distinguishes it from social insurance governed by the ATSG.",
                ]},
                {"heading": "The waiting period", "paragraphs": [
                    "The waiting period is the time, defined by the insurance contract, during which no benefit is paid after the start of incapacity for work. Its duration varies from contract to contract, generally from a few days to several weeks: the general terms and conditions of the specific contract must be checked to find the applicable period.",
                ]},
                {"heading": "The duration of benefits", "paragraphs": [
                    "The period during which the daily allowance is paid is also set by the contract, most often limited to a maximum period of several months up to a few years depending on the insurance product taken out. This period interacts with the employer's statutory duty to continue paying salary under art. 324a CO in the absence of such insurance.",
                ]},
                {"heading": "Interaction with the employer's statutory duty", "paragraphs": [
                    "In the absence of sickness daily allowance insurance, the employer remains obliged to pay salary for a limited time in the event of incapacity for work through no fault of the employee (art. 324a CO), with the duration depending on seniority and varying according to the usual cantonal scales.",
                ]},
            ],
            "faq": [
                {"q": "Is sickness daily allowance insurance mandatory?",
                 "a": "It is in principle not mandatory at federal level for employees, unless an applicable collective bargaining agreement or the individual employment contract requires it."},
                {"q": "What is the waiting period?",
                 "a": "The period, set by the insurance contract, during which no allowance is paid after the start of incapacity for work. Its duration depends entirely on the contractual terms taken out."},
                {"q": "What happens if my employer has not taken out sickness daily allowance insurance?",
                 "a": "They remain obliged, under art. 324a CO, to pay salary for a limited time in the event of incapacity for work through no fault of the employee, with the duration depending on seniority and the applicable cantonal scale."},
            ],
        },
    },
    "contester-decision-assurance-invalidite": {
        "domaine_id": "droit_assurances",
        "published": "2026-07-30",
        "fr": {
            "slug": "contester-decision-assurance-invalidite",
            "title": "Contester une décision de l'assurance invalidité",
            "meta": "Opposition dans les 30 jours, recours devant le tribunal cantonal des assurances : la procédure pour contester une décision de l'AI.",
            "sections": [
                {"heading": "Le préavis et la décision", "paragraphs": [
                    "L'office de l'assurance invalidité (AI) notifie généralement un projet de décision, permettant à l'assuré de faire valoir ses objections avant la décision définitive. Une fois la décision rendue, elle indique les voies de droit disponibles pour la contester.",
                ]},
                {"heading": "L'opposition", "paragraphs": [
                    "L'assuré qui conteste une décision de l'AI peut former opposition par écrit dans les 30 jours suivant sa notification (art. 52 LPGA), en exposant les motifs de sa contestation. L'office AI réexamine alors le dossier et rend une décision sur opposition, qui peut confirmer, modifier ou annuler la décision initiale.",
                ]},
                {"heading": "Le recours devant le tribunal cantonal des assurances", "paragraphs": [
                    "Si la décision sur opposition ne satisfait pas l'assuré, il peut la porter devant le tribunal cantonal des assurances compétent, dans un délai de 30 jours dès sa notification. Un recours ultérieur au Tribunal fédéral reste possible dans les conditions générales du recours en matière de droit public.",
                ]},
                {"heading": "L'importance des expertises médicales", "paragraphs": [
                    "Les décisions de l'AI reposent très largement sur des expertises médicales. Contester une décision suppose souvent de discuter la valeur probante de ces expertises, éventuellement en produisant un avis médical contraire ou en sollicitant une contre-expertise, ce qui rend l'accompagnement par un avocat spécialisé particulièrement utile dans ces procédures.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai puis-je m'opposer à une décision de l'AI ?",
                 "a": "Dans les 30 jours suivant la notification de la décision, par une opposition écrite et motivée adressée à l'office AI (art. 52 LPGA)."},
                {"q": "Que se passe-t-il après une opposition ?",
                 "a": "L'office AI réexamine le dossier et rend une décision sur opposition, qui peut confirmer, modifier ou annuler la décision initiale. Cette nouvelle décision peut ensuite être portée devant le tribunal cantonal des assurances."},
                {"q": "Pourquoi les expertises médicales sont-elles si importantes dans ces procédures ?",
                 "a": "Parce que les décisions de l'AI reposent très largement sur elles pour évaluer le taux d'invalidité et la capacité de travail résiduelle. Contester une décision suppose souvent de discuter la valeur probante de ces expertises."},
            ],
        },
        "de": {
            "slug": "iv-entscheid-anfechten",
            "title": "Einen Entscheid der Invalidenversicherung anfechten",
            "meta": "Einsprache innert 30 Tagen, Beschwerde beim kantonalen Versicherungsgericht: das Verfahren zur Anfechtung eines IV-Entscheids.",
            "sections": [
                {"heading": "Der Vorbescheid und die Verfügung", "paragraphs": [
                    "Die IV-Stelle stellt in der Regel einen Vorbescheid zu, der es der versicherten Person erlaubt, vor dem endgültigen Entscheid ihre Einwände geltend zu machen. Ist die Verfügung einmal erlassen, gibt sie die zu ihrer Anfechtung verfügbaren Rechtsmittel an.",
                ]},
                {"heading": "Die Einsprache", "paragraphs": [
                    "Die versicherte Person, die einen IV-Entscheid anficht, kann innert 30 Tagen nach dessen Eröffnung schriftlich Einsprache erheben (Art. 52 ATSG), unter Darlegung der Gründe ihrer Beanstandung. Die IV-Stelle prüft das Dossier daraufhin erneut und erlässt einen Einspracheentscheid, der die ursprüngliche Verfügung bestätigen, ändern oder aufheben kann.",
                ]},
                {"heading": "Die Beschwerde beim kantonalen Versicherungsgericht", "paragraphs": [
                    "Befriedigt der Einspracheentscheid die versicherte Person nicht, kann sie ihn beim zuständigen kantonalen Versicherungsgericht anfechten, innert einer Frist von 30 Tagen ab dessen Eröffnung. Eine spätere Beschwerde ans Bundesgericht bleibt unter den allgemeinen Voraussetzungen der Beschwerde in öffentlich-rechtlichen Angelegenheiten möglich.",
                ]},
                {"heading": "Die Bedeutung medizinischer Gutachten", "paragraphs": [
                    "IV-Entscheide stützen sich sehr weitgehend auf medizinische Gutachten. Einen Entscheid anzufechten bedeutet häufig, den Beweiswert dieser Gutachten zu diskutieren, gegebenenfalls durch Vorlage einer gegenteiligen ärztlichen Stellungnahme oder durch Beantragung eines Gegengutachtens, weshalb die Begleitung durch eine spezialisierte Anwältin oder einen spezialisierten Anwalt in diesen Verfahren besonders nützlich ist.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist kann ich gegen einen IV-Entscheid Einsprache erheben?",
                 "a": "Innert 30 Tagen nach dessen Eröffnung, durch eine schriftliche und begründete Einsprache an die IV-Stelle (Art. 52 ATSG)."},
                {"q": "Was geschieht nach einer Einsprache?",
                 "a": "Die IV-Stelle prüft das Dossier erneut und erlässt einen Einspracheentscheid, der die ursprüngliche Verfügung bestätigen, ändern oder aufheben kann. Dieser neue Entscheid kann anschliessend beim kantonalen Versicherungsgericht angefochten werden."},
                {"q": "Warum sind medizinische Gutachten in diesen Verfahren so wichtig?",
                 "a": "Weil sich IV-Entscheide sehr weitgehend darauf stützen, um den Invaliditätsgrad und die verbleibende Arbeitsfähigkeit zu beurteilen. Einen Entscheid anzufechten bedeutet häufig, den Beweiswert dieser Gutachten zu diskutieren."},
            ],
        },
        "it": {
            "slug": "contestare-decisione-assicurazione-invalidita",
            "title": "Contestare una decisione dell'assicurazione invalidità",
            "meta": "Opposizione entro 30 giorni, ricorso davanti al tribunale cantonale delle assicurazioni: la procedura per contestare una decisione dell'AI.",
            "sections": [
                {"heading": "Il preavviso e la decisione", "paragraphs": [
                    "L'ufficio dell'assicurazione invalidità (AI) notifica generalmente un progetto di decisione, permettendo all'assicurato di far valere le proprie obiezioni prima della decisione definitiva. Una volta emessa la decisione, essa indica le vie di diritto disponibili per contestarla.",
                ]},
                {"heading": "L'opposizione", "paragraphs": [
                    "L'assicurato che contesta una decisione dell'AI può fare opposizione per scritto entro 30 giorni dalla notifica (art. 52 LPGA), esponendo i motivi della propria contestazione. L'ufficio AI riesamina allora l'incarto ed emette una decisione su opposizione, che può confermare, modificare o annullare la decisione iniziale.",
                ]},
                {"heading": "Il ricorso davanti al tribunale cantonale delle assicurazioni", "paragraphs": [
                    "Se la decisione su opposizione non soddisfa l'assicurato, questi può portarla davanti al tribunale cantonale delle assicurazioni competente, entro un termine di 30 giorni dalla sua notifica. Un ricorso successivo al Tribunale federale resta possibile alle condizioni generali del ricorso in materia di diritto pubblico.",
                ]},
                {"heading": "L'importanza delle perizie mediche", "paragraphs": [
                    "Le decisioni dell'AI si fondano molto largamente su perizie mediche. Contestare una decisione significa spesso discutere il valore probatorio di tali perizie, eventualmente producendo un parere medico contrario o richiedendo una controperizia, il che rende particolarmente utile l'assistenza di un avvocato specializzato in queste procedure.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine posso oppormi a una decisione dell'AI?",
                 "a": "Entro 30 giorni dalla notifica della decisione, tramite un'opposizione scritta e motivata indirizzata all'ufficio AI (art. 52 LPGA)."},
                {"q": "Cosa succede dopo un'opposizione?",
                 "a": "L'ufficio AI riesamina l'incarto ed emette una decisione su opposizione, che può confermare, modificare o annullare la decisione iniziale. Questa nuova decisione può quindi essere portata davanti al tribunale cantonale delle assicurazioni."},
                {"q": "Perché le perizie mediche sono così importanti in queste procedure?",
                 "a": "Perché le decisioni dell'AI si fondano molto largamente su di esse per valutare il grado d'invalidità e la capacità lavorativa residua. Contestare una decisione significa spesso discutere il valore probatorio di tali perizie."},
            ],
        },
        "en": {
            "slug": "challenging-disability-insurance-decision",
            "title": "Challenging a disability insurance decision",
            "meta": "Objection within 30 days, appeal to the cantonal insurance court: the procedure for challenging a disability insurance decision.",
            "sections": [
                {"heading": "The draft decision and the final decision", "paragraphs": [
                    "The disability insurance (IV/AI) office generally issues a draft decision, allowing the insured person to raise objections before the final decision. Once the decision has been issued, it states the legal remedies available to challenge it.",
                ]},
                {"heading": "The objection", "paragraphs": [
                    "An insured person who disputes a disability insurance decision can file a written objection within 30 days of its notification (art. 52 ATSG/LPGA), setting out the grounds for their objection. The disability insurance office then re-examines the file and issues a decision on the objection, which can confirm, amend, or annul the initial decision.",
                ]},
                {"heading": "Appeal to the cantonal insurance court", "paragraphs": [
                    "If the decision on the objection does not satisfy the insured person, they can bring it before the competent cantonal insurance court, within a 30-day period from its notification. A further appeal to the Federal Supreme Court remains possible under the general conditions for appeals in public law matters.",
                ]},
                {"heading": "The importance of medical expert opinions", "paragraphs": [
                    "Disability insurance decisions rely very heavily on medical expert opinions. Challenging a decision often means disputing the probative value of these opinions, possibly by submitting a contrary medical opinion or requesting a counter-assessment, which makes assistance from a specialised lawyer particularly useful in these proceedings.",
                ]},
            ],
            "faq": [
                {"q": "Within what deadline can I object to a disability insurance decision?",
                 "a": "Within 30 days of notification of the decision, through a written and reasoned objection addressed to the disability insurance office (art. 52 ATSG/LPGA)."},
                {"q": "What happens after an objection?",
                 "a": "The disability insurance office re-examines the file and issues a decision on the objection, which can confirm, amend, or annul the initial decision. This new decision can then be brought before the cantonal insurance court."},
                {"q": "Why are medical expert opinions so important in these proceedings?",
                 "a": "Because disability insurance decisions rely very heavily on them to assess the degree of disability and remaining working capacity. Challenging a decision often means disputing the probative value of these opinions."},
            ],
        },
    },
    "responsabilite-civile-indemnisation": {
        "domaine_id": "droit_responsabilite_civile",
        "published": "2026-07-30",
        "fr": {
            "slug": "responsabilite-civile-qui-est-responsable-indemnisation",
            "title": "Responsabilité civile : qui paie et comment être indemnisé",
            "meta": "Acte illicite, faute, lien de causalité et dommage : les conditions de la responsabilité civile selon le Code des obligations.",
            "sections": [
                {"heading": "Les conditions de la responsabilité pour faute", "paragraphs": [
                    "L'art. 41 CO pose le principe général de la responsabilité civile pour acte illicite : celui qui cause un dommage à autrui de manière illicite, intentionnellement ou par négligence, est tenu de le réparer. Cette responsabilité suppose la réunion de quatre conditions cumulatives : un acte illicite, une faute, un dommage, et un lien de causalité entre l'acte et le dommage.",
                ]},
                {"heading": "Les responsabilités causales", "paragraphs": [
                    "À côté de la responsabilité pour faute, le droit suisse connaît diverses responsabilités causales, où la faute n'a pas besoin d'être prouvée : responsabilité du détenteur de véhicule automobile (art. 58 LCR), du détenteur d'animal (art. 56 CO), du propriétaire d'ouvrage (art. 58 CO), ou encore la responsabilité du fait des produits.",
                ]},
                {"heading": "Le calcul du dommage", "paragraphs": [
                    "Le dommage réparable comprend en principe le dommage matériel (frais médicaux, perte de gain, dommage ménager), le tort moral en cas d'atteinte grave à la personnalité, et dans certains cas un dommage de rente pour perte de capacité de gain future. Son évaluation précise dépend fortement des circonstances concrètes de chaque cas.",
                ]},
                {"heading": "La déclaration et la prescription", "paragraphs": [
                    "Une créance en dommages-intérêts se prescrit en principe par trois ans à compter du jour où le lésé a eu connaissance du dommage et de la personne responsable, et dans tous les cas par vingt ans à compter du jour où le fait dommageable s'est produit (art. 60 CO), sous réserve de délais plus longs applicables en cas d'infraction pénale.",
                ]},
            ],
            "faq": [
                {"q": "Dois-je prouver une faute pour obtenir réparation d'un dommage ?",
                 "a": "Cela dépend du fondement juridique invoqué : la responsabilité pour faute de l'art. 41 CO exige de prouver une faute, tandis que les responsabilités causales (détenteur de véhicule, d'animal, propriétaire d'ouvrage) n'exigent en principe pas cette preuve."},
                {"q": "Dans quel délai dois-je agir pour réclamer des dommages-intérêts ?",
                 "a": "En principe dans les trois ans dès la connaissance du dommage et de la personne responsable, et au plus tard vingt ans après le fait dommageable (art. 60 CO), sous réserve de délais spécifiques en cas d'infraction pénale."},
                {"q": "Le tort moral est-il toujours indemnisé en cas de dommage ?",
                 "a": "Non, seulement en cas d'atteinte grave à la personnalité, appréciée selon les circonstances concrètes : gravité de l'atteinte, souffrances endurées, et autres éléments pertinents du cas d'espèce."},
            ],
        },
        "de": {
            "slug": "zivilhaftung-wer-haftet-entschaedigung",
            "title": "Zivilhaftung: wer haftet und wie man entschädigt wird",
            "meta": "Widerrechtliche Handlung, Verschulden, Kausalzusammenhang und Schaden: die Voraussetzungen der Zivilhaftung gemäss Obligationenrecht.",
            "sections": [
                {"heading": "Die Voraussetzungen der Verschuldenshaftung", "paragraphs": [
                    "Art. 41 OR stellt den allgemeinen Grundsatz der Zivilhaftung für widerrechtliche Handlung auf: wer einem anderen widerrechtlich, absichtlich oder fahrlässig, Schaden zufügt, wird ihm zum Ersatz verpflichtet. Diese Haftung setzt vier kumulative Voraussetzungen voraus: eine widerrechtliche Handlung, ein Verschulden, einen Schaden und einen Kausalzusammenhang zwischen der Handlung und dem Schaden.",
                ]},
                {"heading": "Die Kausalhaftungen", "paragraphs": [
                    "Neben der Verschuldenshaftung kennt das schweizerische Recht verschiedene Kausalhaftungen, bei denen kein Verschulden nachgewiesen werden muss: Haftung der Halterin oder des Halters eines Motorfahrzeugs (Art. 58 SVG), der Tierhalterin oder des Tierhalters (Art. 56 OR), der Werkeigentümerin oder des Werkeigentümers (Art. 58 OR), oder auch die Produktehaftung.",
                ]},
                {"heading": "Die Berechnung des Schadens", "paragraphs": [
                    "Der ersatzfähige Schaden umfasst grundsätzlich den materiellen Schaden (Heilungskosten, Erwerbsausfall, Haushaltsschaden), die Genugtuung bei schwerer Persönlichkeitsverletzung sowie in bestimmten Fällen einen Rentenschaden für künftigen Erwerbsausfall. Seine genaue Bewertung hängt stark von den konkreten Umständen jedes einzelnen Falles ab.",
                ]},
                {"heading": "Die Geltendmachung und Verjährung", "paragraphs": [
                    "Eine Schadenersatzforderung verjährt grundsätzlich mit Ablauf von drei Jahren ab dem Tag, an dem die geschädigte Person Kenntnis vom Schaden und von der ersatzpflichtigen Person erlangt hat, und in jedem Fall mit Ablauf von zwanzig Jahren ab dem Tag der schädigenden Handlung (Art. 60 OR), vorbehältlich längerer Fristen bei einer strafbaren Handlung.",
                ]},
            ],
            "faq": [
                {"q": "Muss ich ein Verschulden nachweisen, um einen Schaden ersetzt zu erhalten?",
                 "a": "Das hängt von der geltend gemachten Rechtsgrundlage ab: die Verschuldenshaftung nach Art. 41 OR verlangt den Nachweis eines Verschuldens, während die Kausalhaftungen (Halterin/Halter eines Fahrzeugs, Tierhalterin/Tierhalter, Werkeigentümerin/Werkeigentümer) diesen Nachweis grundsätzlich nicht verlangen."},
                {"q": "Innert welcher Frist muss ich Schadenersatz geltend machen?",
                 "a": "Grundsätzlich innert drei Jahren ab Kenntnis des Schadens und der ersatzpflichtigen Person, und spätestens zwanzig Jahre nach der schädigenden Handlung (Art. 60 OR), vorbehältlich besonderer Fristen bei einer strafbaren Handlung."},
                {"q": "Wird die Genugtuung bei jedem Schaden immer ausgerichtet?",
                 "a": "Nein, nur bei schwerer Persönlichkeitsverletzung, beurteilt nach den konkreten Umständen: Schwere der Verletzung, erlittene Leiden und weitere relevante Elemente des Einzelfalls."},
            ],
        },
        "it": {
            "slug": "responsabilita-civile-chi-e-responsabile-indennizzo",
            "title": "Responsabilità civile: chi paga e come farsi risarcire",
            "meta": "Atto illecito, colpa, nesso di causalità e danno: le condizioni della responsabilità civile secondo il Codice delle obbligazioni.",
            "sections": [
                {"heading": "Le condizioni della responsabilità per colpa", "paragraphs": [
                    "L'art. 41 CO pone il principio generale della responsabilità civile per atto illecito: chiunque cagiona ad altri un danno illecitamente, intenzionalmente o per negligenza, è tenuto a risarcirlo. Questa responsabilità presuppone la riunione di quattro condizioni cumulative: un atto illecito, una colpa, un danno, e un nesso di causalità tra l'atto e il danno.",
                ]},
                {"heading": "Le responsabilità causali", "paragraphs": [
                    "Accanto alla responsabilità per colpa, il diritto svizzero conosce diverse responsabilità causali, dove la colpa non deve essere provata: responsabilità del detentore di veicolo a motore (art. 58 LCStr), del detentore di animali (art. 56 CO), del proprietario dell'opera (art. 58 CO), o ancora la responsabilità per i prodotti.",
                ]},
                {"heading": "Il calcolo del danno", "paragraphs": [
                    "Il danno risarcibile comprende in linea di principio il danno materiale (spese mediche, perdita di guadagno, danno economico domestico), la riparazione morale in caso di grave lesione della personalità, e in determinati casi un danno di rendita per perdita futura della capacità di guadagno. La sua valutazione precisa dipende fortemente dalle circostanze concrete di ogni caso.",
                ]},
                {"heading": "La rivendicazione e la prescrizione", "paragraphs": [
                    "Un credito per risarcimento del danno si prescrive in linea di principio in tre anni dal giorno in cui il leso ha avuto conoscenza del danno e della persona responsabile, e in ogni caso in venti anni dal giorno in cui si è verificato il fatto dannoso (art. 60 CO), con riserva di termini più lunghi applicabili in caso di reato penale.",
                ]},
            ],
            "faq": [
                {"q": "Devo provare una colpa per ottenere il risarcimento di un danno?",
                 "a": "Ciò dipende dal fondamento giuridico invocato: la responsabilità per colpa dell'art. 41 CO esige di provare una colpa, mentre le responsabilità causali (detentore di veicolo, di animali, proprietario dell'opera) in linea di principio non esigono questa prova."},
                {"q": "Entro quale termine devo agire per reclamare un risarcimento del danno?",
                 "a": "In linea di principio entro tre anni dalla conoscenza del danno e della persona responsabile, e al più tardi venti anni dopo il fatto dannoso (art. 60 CO), con riserva di termini specifici in caso di reato penale."},
                {"q": "La riparazione morale viene sempre indennizzata in caso di danno?",
                 "a": "No, solo in caso di grave lesione della personalità, valutata secondo le circostanze concrete: gravità della lesione, sofferenze patite e altri elementi pertinenti del caso specifico."},
            ],
        },
        "en": {
            "slug": "civil-liability-who-is-liable-compensation",
            "title": "Civil liability: who is liable and how to get compensated",
            "meta": "Unlawful act, fault, causal link and damage: the conditions for civil liability under the Code of Obligations.",
            "sections": [
                {"heading": "The conditions for fault-based liability", "paragraphs": [
                    "Art. 41 CO sets out the general principle of civil liability for an unlawful act: a person who unlawfully causes damage to another, whether intentionally or through negligence, is liable to make good the loss. This liability requires four cumulative conditions: an unlawful act, fault, damage, and a causal link between the act and the damage.",
                ]},
                {"heading": "Strict liability", "paragraphs": [
                    "Alongside fault-based liability, Swiss law recognises various forms of strict liability, where fault does not need to be proven: liability of a motor vehicle keeper (art. 58 LCR), of an animal keeper (art. 56 CO), of a building owner (art. 58 CO), or product liability.",
                ]},
                {"heading": "Calculating the damage", "paragraphs": [
                    "Recoverable damage in principle includes material loss (medical expenses, loss of earnings, loss related to household work), moral compensation in the event of a serious personality violation, and in certain cases loss of future earning capacity as a pension-type loss. Its precise assessment depends heavily on the specific circumstances of each case.",
                ]},
                {"heading": "Bringing a claim and limitation", "paragraphs": [
                    "A claim for damages is in principle time-barred after three years from the day the injured party became aware of the damage and the liable person, and in any case after twenty years from the day of the harmful act (art. 60 CO), subject to longer periods applicable in the event of a criminal offence.",
                ]},
            ],
            "faq": [
                {"q": "Do I need to prove fault to be compensated for damage?",
                 "a": "This depends on the legal basis invoked: fault-based liability under art. 41 CO requires proof of fault, while strict liability (vehicle keeper, animal keeper, building owner) in principle does not require this proof."},
                {"q": "Within what deadline must I claim damages?",
                 "a": "In principle within three years from becoming aware of the damage and the liable person, and at the latest twenty years after the harmful act (art. 60 CO), subject to specific periods in the event of a criminal offence."},
                {"q": "Is moral compensation always awarded for damage?",
                 "a": "No, only in the event of a serious personality violation, assessed according to the specific circumstances: severity of the violation, suffering endured, and other relevant elements of the specific case."},
            ],
        },
    },
    "responsabilite-detenteur-animal-proprietaire": {
        "domaine_id": "droit_responsabilite_civile",
        "published": "2026-07-30",
        "fr": {
            "slug": "responsabilite-detenteur-animal-proprietaire-immobilier",
            "title": "Responsabilité du détenteur d'animal et du propriétaire",
            "meta": "Responsabilité causale pour les dommages causés par un animal ou un défaut d'entretien d'un bâtiment, selon le Code des obligations.",
            "sections": [
                {"heading": "La responsabilité du détenteur d'animal", "paragraphs": [
                    "L'art. 56 CO instaure une responsabilité causale du détenteur d'un animal pour le dommage que celui-ci cause, indépendamment d'une faute de sa part. Le détenteur ne peut se libérer qu'en prouvant qu'il a apporté tous les soins commandés par les circonstances pour prévenir le dommage, ou que le dommage se serait produit malgré cette diligence.",
                ]},
                {"heading": "La responsabilité du propriétaire d'ouvrage", "paragraphs": [
                    "L'art. 58 CO prévoit une responsabilité causale du propriétaire d'un bâtiment ou d'un autre ouvrage pour le dommage résultant d'un défaut de construction ou d'un défaut d'entretien. Cette responsabilité vise notamment les accidents causés par un escalier mal entretenu, une façade qui se détache, ou une installation défectueuse.",
                ]},
                {"heading": "Le recours contre un tiers responsable", "paragraphs": [
                    "Le propriétaire qui a indemnisé un lésé conserve en principe un droit de recours contre l'entrepreneur ou l'artisan dont les travaux défectueux sont à l'origine du dommage, selon les règles générales de la responsabilité contractuelle et les délais de prescription applicables à ce recours.",
                ]},
                {"heading": "L'importance de l'assurance responsabilité civile privée", "paragraphs": [
                    "Ces responsabilités causales expliquent l'intérêt d'une assurance responsabilité civile privée pour tout détenteur d'animal ou propriétaire immobilier, qui couvre en principe les dommages causés à des tiers dans les limites et exclusions prévues par le contrat souscrit.",
                ]},
            ],
            "faq": [
                {"q": "Suis-je responsable si mon chien mord quelqu'un même sans négligence de ma part ?",
                 "a": "En principe oui : l'art. 56 CO instaure une responsabilité causale du détenteur d'animal, qui ne peut se libérer qu'en prouvant avoir apporté tous les soins commandés par les circonstances pour prévenir le dommage."},
                {"q": "Qui est responsable si un escalier mal entretenu cause une chute ?",
                 "a": "Le propriétaire du bâtiment, sur la base de l'art. 58 CO qui institue une responsabilité causale pour les dommages résultant d'un défaut de construction ou d'entretien de l'ouvrage."},
                {"q": "Le propriétaire peut-il se retourner contre l'entrepreneur responsable du défaut ?",
                 "a": "Oui, il conserve en principe un droit de recours contre l'entrepreneur ou l'artisan à l'origine du défaut, selon les règles de la responsabilité contractuelle et dans les délais de prescription applicables."},
            ],
        },
        "de": {
            "slug": "haftung-tierhalter-grundeigentuemer",
            "title": "Haftung von Tierhaltern und Grundeigentümern",
            "meta": "Kausalhaftung für Schäden durch ein Tier oder mangelhafte Unterhaltung eines Gebäudes gemäss Obligationenrecht.",
            "sections": [
                {"heading": "Die Haftung der Tierhalterin oder des Tierhalters", "paragraphs": [
                    "Art. 56 OR statuiert eine Kausalhaftung der Tierhalterin oder des Tierhalters für den durch das Tier verursachten Schaden, unabhängig von einem Verschulden ihrerseits. Die Halterin oder der Halter kann sich nur befreien, indem sie oder er nachweist, alle nach den Umständen gebotene Sorgfalt in der Verwahrung und Beaufsichtigung des Tieres angewendet zu haben, oder dass der Schaden auch bei Anwendung dieser Sorgfalt eingetreten wäre.",
                ]},
                {"heading": "Die Werkeigentümerhaftung", "paragraphs": [
                    "Art. 58 OR sieht eine Kausalhaftung der Eigentümerin oder des Eigentümers eines Gebäudes oder eines anderen Werkes für den Schaden vor, der aus einem fehlerhaften Bau oder mangelhafter Unterhaltung entsteht. Diese Haftung betrifft namentlich Unfälle, die durch eine schlecht unterhaltene Treppe, eine sich lösende Fassade oder eine defekte Anlage verursacht werden.",
                ]},
                {"heading": "Der Rückgriff auf eine dritte Person", "paragraphs": [
                    "Die Eigentümerin oder der Eigentümer, die oder der eine geschädigte Person entschädigt hat, behält grundsätzlich ein Rückgriffsrecht gegen die Unternehmerin oder den Unternehmer oder die Handwerkerin oder den Handwerker, deren mangelhafte Arbeiten die Ursache des Schadens sind, nach den allgemeinen Regeln der vertraglichen Haftung und den für diesen Rückgriff geltenden Verjährungsfristen.",
                ]},
                {"heading": "Die Bedeutung der privaten Haftpflichtversicherung", "paragraphs": [
                    "Diese Kausalhaftungen erklären das Interesse einer privaten Haftpflichtversicherung für jede Tierhalterin, jeden Tierhalter oder jede Grundeigentümerschaft, welche grundsätzlich die Dritten zugefügten Schäden im Rahmen der im abgeschlossenen Vertrag vorgesehenen Grenzen und Ausschlüsse deckt.",
                ]},
            ],
            "faq": [
                {"q": "Hafte ich, wenn mein Hund jemanden beisst, auch ohne Nachlässigkeit meinerseits?",
                 "a": "Grundsätzlich ja: Art. 56 OR statuiert eine Kausalhaftung der Tierhalterin oder des Tierhalters, die sich nur befreien kann, indem sie nachweist, alle nach den Umständen gebotene Sorgfalt zur Verhinderung des Schadens angewendet zu haben."},
                {"q": "Wer haftet, wenn eine mangelhaft unterhaltene Treppe einen Sturz verursacht?",
                 "a": "Die Eigentümerin oder der Eigentümer des Gebäudes, gestützt auf Art. 58 OR, der eine Kausalhaftung für Schäden aus fehlerhaftem Bau oder mangelhafter Unterhaltung des Werks vorsieht."},
                {"q": "Kann sich die Eigentümerschaft an die für den Mangel verantwortliche Unternehmerin oder den verantwortlichen Unternehmer wenden?",
                 "a": "Ja, sie behält grundsätzlich ein Rückgriffsrecht gegen die Unternehmerin oder den Unternehmer oder die Handwerkerin oder den Handwerker, die oder der den Mangel verursacht hat, nach den Regeln der vertraglichen Haftung und innerhalb der geltenden Verjährungsfristen."},
            ],
        },
        "it": {
            "slug": "responsabilita-detentore-animale-proprietario-immobiliare",
            "title": "Responsabilità del detentore di animali e del proprietario",
            "meta": "Responsabilità causale per i danni causati da un animale o da un difetto di manutenzione di un edificio, secondo il Codice delle obbligazioni.",
            "sections": [
                {"heading": "La responsabilità del detentore di animali", "paragraphs": [
                    "L'art. 56 CO istituisce una responsabilità causale del detentore di un animale per il danno che questo cagiona, indipendentemente da una sua colpa. Il detentore può liberarsi solo provando di aver usato tutta la diligenza richiesta dalle circostanze per prevenire il danno, o che il danno si sarebbe verificato ugualmente nonostante tale diligenza.",
                ]},
                {"heading": "La responsabilità del proprietario dell'opera", "paragraphs": [
                    "L'art. 58 CO prevede una responsabilità causale del proprietario di un edificio o di un'altra opera per il danno risultante da un difetto di costruzione o di manutenzione. Questa responsabilità riguarda in particolare gli incidenti causati da una scala mal tenuta, una facciata che si stacca, o un impianto difettoso.",
                ]},
                {"heading": "Il regresso contro un terzo responsabile", "paragraphs": [
                    "Il proprietario che ha indennizzato un leso conserva in linea di principio un diritto di regresso contro l'appaltatore o l'artigiano i cui lavori difettosi sono all'origine del danno, secondo le regole generali della responsabilità contrattuale e i termini di prescrizione applicabili a tale regresso.",
                ]},
                {"heading": "L'importanza dell'assicurazione di responsabilità civile privata", "paragraphs": [
                    "Queste responsabilità causali spiegano l'interesse di un'assicurazione di responsabilità civile privata per ogni detentore di animali o proprietario immobiliare, che copre in linea di principio i danni causati a terzi entro i limiti e le esclusioni previste dal contratto sottoscritto.",
                ]},
            ],
            "faq": [
                {"q": "Sono responsabile se il mio cane morde qualcuno anche senza negligenza da parte mia?",
                 "a": "In linea di principio sì: l'art. 56 CO istituisce una responsabilità causale del detentore di animali, che può liberarsi solo provando di aver usato tutta la diligenza richiesta dalle circostanze per prevenire il danno."},
                {"q": "Chi è responsabile se una scala mal tenuta causa una caduta?",
                 "a": "Il proprietario dell'edificio, sulla base dell'art. 58 CO che istituisce una responsabilità causale per i danni risultanti da un difetto di costruzione o di manutenzione dell'opera."},
                {"q": "Il proprietario può rivalersi contro l'appaltatore responsabile del difetto?",
                 "a": "Sì, conserva in linea di principio un diritto di regresso contro l'appaltatore o l'artigiano all'origine del difetto, secondo le regole della responsabilità contrattuale ed entro i termini di prescrizione applicabili."},
            ],
        },
        "en": {
            "slug": "liability-animal-keeper-property-owner",
            "title": "Liability of an animal keeper and a property owner",
            "meta": "Strict liability for damage caused by an animal or a defect in maintaining a building, under the Code of Obligations.",
            "sections": [
                {"heading": "The animal keeper's liability", "paragraphs": [
                    "Art. 56 CO establishes strict liability for an animal's keeper for damage the animal causes, regardless of any fault on their part. The keeper can only be released from liability by proving they exercised all the care required by the circumstances to prevent the damage, or that the damage would have occurred even with such care.",
                ]},
                {"heading": "The building owner's liability", "paragraphs": [
                    "Art. 58 CO establishes strict liability for the owner of a building or other structure for damage resulting from a defect in its construction or maintenance. This liability covers, in particular, accidents caused by a poorly maintained staircase, a facade coming loose, or a defective installation.",
                ]},
                {"heading": "Recourse against a liable third party", "paragraphs": [
                    "An owner who has compensated an injured party in principle retains a right of recourse against the contractor or tradesperson whose defective work caused the damage, under the general rules of contractual liability and the limitation periods applicable to that recourse.",
                ]},
                {"heading": "The importance of private liability insurance", "paragraphs": [
                    "This strict liability explains the value of private liability insurance for any animal keeper or property owner, which in principle covers damage caused to third parties within the limits and exclusions provided by the policy taken out.",
                ]},
            ],
            "faq": [
                {"q": "Am I liable if my dog bites someone even without negligence on my part?",
                 "a": "In principle yes: art. 56 CO establishes strict liability for an animal's keeper, who can only be released from liability by proving they exercised all the care required by the circumstances to prevent the damage."},
                {"q": "Who is liable if a poorly maintained staircase causes a fall?",
                 "a": "The building's owner, based on art. 58 CO, which establishes strict liability for damage resulting from a defect in the construction or maintenance of the structure."},
                {"q": "Can the owner recover from the contractor responsible for the defect?",
                 "a": "Yes, they in principle retain a right of recourse against the contractor or tradesperson responsible for the defect, under the rules of contractual liability and within the applicable limitation periods."},
            ],
        },
    },
    "commandement-payer-opposition": {
        "domaine_id": "droit_poursuites_faillite",
        "published": "2026-07-30",
        "fr": {
            "slug": "commandement-payer-comment-faire-opposition",
            "title": "Commandement de payer : comment faire opposition",
            "meta": "Délai de dix jours, forme de l'opposition, conséquences sur la poursuite : ce que prévoit la loi sur la poursuite pour dettes et la faillite.",
            "sections": [
                {"heading": "Ce qu'est un commandement de payer", "paragraphs": [
                    "Le commandement de payer est l'acte par lequel l'office des poursuites notifie au débiteur, à la demande d'un créancier, une poursuite pour une somme d'argent déterminée (art. 69 ss LP). Il indique le montant réclamé, la cause de l'obligation, et informe le débiteur de son droit de faire opposition.",
                ]},
                {"heading": "Le délai et la forme de l'opposition", "paragraphs": [
                    "Le débiteur qui conteste tout ou partie de la dette peut former opposition dans les dix jours suivant la notification du commandement de payer (art. 74 LP). L'opposition peut être faite verbalement à l'office des poursuites au moment de la notification, ou par écrit dans le délai, sans devoir être motivée.",
                ]},
                {"heading": "Les effets de l'opposition", "paragraphs": [
                    "Une opposition valablement formée suspend la poursuite : le créancier ne peut pas continuer la procédure sans obtenir au préalable la mainlevée de l'opposition auprès du juge compétent, par une procédure de mainlevée provisoire ou définitive selon la nature de sa créance, ou par une action en reconnaissance de dette.",
                ]},
                {"heading": "Ne pas ignorer un commandement de payer", "paragraphs": [
                    "Même une dette contestée à tort ou une poursuite abusive doit être traitée par une opposition dans le délai légal : l'absence d'opposition permet en principe au créancier de continuer la poursuite sans que le débiteur puisse encore faire valoir ses objections sur le fond de la créance à ce stade de la procédure.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai dois-je faire opposition à un commandement de payer ?",
                 "a": "Dans les dix jours suivant sa notification (art. 74 LP), verbalement à l'office des poursuites ou par écrit, sans devoir motiver l'opposition."},
                {"q": "Que se passe-t-il si je ne fais pas opposition ?",
                 "a": "Le créancier peut en principe continuer la poursuite sans que vous puissiez encore contester la créance à ce stade de la procédure. Il est donc essentiel d'agir dans le délai même si vous estimez la poursuite infondée."},
                {"q": "L'opposition met-elle fin définitivement à la poursuite ?",
                 "a": "Non, elle la suspend : le créancier peut demander au juge la mainlevée de l'opposition, ou intenter une action en reconnaissance de dette, pour pouvoir continuer la poursuite."},
                {"q": "Dois-je motiver mon opposition ?",
                 "a": "Non, l'opposition n'a pas besoin d'être motivée pour être valable (art. 74 LP). Une simple déclaration d'opposition dans le délai suffit à suspendre la poursuite."},
            ],
        },
        "de": {
            "slug": "zahlungsbefehl-rechtsvorschlag-erheben",
            "title": "Zahlungsbefehl: wie Rechtsvorschlag erhoben wird",
            "meta": "Frist von zehn Tagen, Form des Rechtsvorschlags, Folgen für die Betreibung: was das Bundesgesetz über Schuldbetreibung und Konkurs vorsieht.",
            "sections": [
                {"heading": "Was ein Zahlungsbefehl ist", "paragraphs": [
                    "Der Zahlungsbefehl ist der Akt, mit dem das Betreibungsamt der Schuldnerin oder dem Schuldner auf Verlangen einer Gläubigerin oder eines Gläubigers eine Betreibung für einen bestimmten Geldbetrag zustellt (Art. 69 ff. SchKG). Er gibt den geforderten Betrag und den Forderungsgrund an und informiert die Schuldnerin oder den Schuldner über ihr oder sein Recht, Rechtsvorschlag zu erheben.",
                ]},
                {"heading": "Die Frist und die Form des Rechtsvorschlags", "paragraphs": [
                    "Die Schuldnerin oder der Schuldner, die oder der die Schuld ganz oder teilweise bestreitet, kann innert zehn Tagen nach Zustellung des Zahlungsbefehls Rechtsvorschlag erheben (Art. 74 SchKG). Der Rechtsvorschlag kann mündlich beim Betreibungsamt im Zeitpunkt der Zustellung erklärt werden oder schriftlich innert der Frist erfolgen, ohne begründet werden zu müssen.",
                ]},
                {"heading": "Die Wirkungen des Rechtsvorschlags", "paragraphs": [
                    "Ein gültig erhobener Rechtsvorschlag hemmt die Betreibung: die Gläubigerin oder der Gläubiger kann das Verfahren nicht fortsetzen, ohne vorgängig die Aufhebung des Rechtsvorschlags beim zuständigen Gericht zu erwirken, durch ein Verfahren der provisorischen oder definitiven Rechtsöffnung je nach Art ihrer oder seiner Forderung, oder durch eine Forderungsklage.",
                ]},
                {"heading": "Einen Zahlungsbefehl nicht ignorieren", "paragraphs": [
                    "Selbst eine zu Unrecht bestrittene Schuld oder eine missbräuchliche Betreibung muss durch einen fristgerechten Rechtsvorschlag behandelt werden: das Fehlen eines Rechtsvorschlags erlaubt der Gläubigerin oder dem Gläubiger grundsätzlich, die Betreibung fortzusetzen, ohne dass die Schuldnerin oder der Schuldner ihre oder seine Einwände gegen die Forderung in diesem Verfahrensstadium noch geltend machen könnte.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist muss ich gegen einen Zahlungsbefehl Rechtsvorschlag erheben?",
                 "a": "Innert zehn Tagen nach dessen Zustellung (Art. 74 SchKG), mündlich beim Betreibungsamt oder schriftlich, ohne den Rechtsvorschlag begründen zu müssen."},
                {"q": "Was geschieht, wenn ich keinen Rechtsvorschlag erhebe?",
                 "a": "Die Gläubigerin oder der Gläubiger kann die Betreibung grundsätzlich fortsetzen, ohne dass Sie die Forderung in diesem Verfahrensstadium noch bestreiten können. Es ist daher unerlässlich, innert Frist zu handeln, selbst wenn Sie die Betreibung für unbegründet halten."},
                {"q": "Beendet der Rechtsvorschlag die Betreibung endgültig?",
                 "a": "Nein, er hemmt sie: die Gläubigerin oder der Gläubiger kann beim Gericht die Aufhebung des Rechtsvorschlags verlangen, oder eine Forderungsklage erheben, um die Betreibung fortsetzen zu können."},
                {"q": "Muss ich meinen Rechtsvorschlag begründen?",
                 "a": "Nein, der Rechtsvorschlag muss nicht begründet werden, um gültig zu sein (Art. 74 SchKG). Eine blosse Rechtsvorschlagserklärung innert Frist genügt, um die Betreibung zu hemmen."},
            ],
        },
        "it": {
            "slug": "precetto-esecutivo-come-fare-opposizione",
            "title": "Precetto esecutivo: come fare opposizione",
            "meta": "Termine di dieci giorni, forma dell'opposizione, conseguenze sull'esecuzione: quanto previsto dalla legge sull'esecuzione e sul fallimento.",
            "sections": [
                {"heading": "Cos'è un precetto esecutivo", "paragraphs": [
                    "Il precetto esecutivo è l'atto con cui l'ufficio d'esecuzione notifica al debitore, su richiesta di un creditore, un'esecuzione per una somma di denaro determinata (art. 69 segg. LEF). Indica l'importo richiesto, la causa dell'obbligazione, e informa il debitore del suo diritto di fare opposizione.",
                ]},
                {"heading": "Il termine e la forma dell'opposizione", "paragraphs": [
                    "Il debitore che contesta in tutto o in parte il debito può fare opposizione entro dieci giorni dalla notifica del precetto esecutivo (art. 74 LEF). L'opposizione può essere fatta verbalmente all'ufficio d'esecuzione al momento della notifica, o per scritto entro il termine, senza dover essere motivata.",
                ]},
                {"heading": "Gli effetti dell'opposizione", "paragraphs": [
                    "Un'opposizione validamente formata sospende l'esecuzione: il creditore non può proseguire la procedura senza ottenere preliminarmente il rigetto dell'opposizione presso il giudice competente, tramite una procedura di rigetto provvisorio o definitivo secondo la natura del suo credito, o tramite un'azione di riconoscimento del debito.",
                ]},
                {"heading": "Non ignorare un precetto esecutivo", "paragraphs": [
                    "Anche un debito contestato a torto o un'esecuzione abusiva deve essere trattato con un'opposizione entro il termine legale: l'assenza di opposizione permette in linea di principio al creditore di proseguire l'esecuzione senza che il debitore possa più far valere le proprie obiezioni sul merito del credito in questa fase della procedura.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine devo fare opposizione a un precetto esecutivo?",
                 "a": "Entro dieci giorni dalla sua notifica (art. 74 LEF), verbalmente all'ufficio d'esecuzione o per scritto, senza dover motivare l'opposizione."},
                {"q": "Cosa succede se non faccio opposizione?",
                 "a": "Il creditore può in linea di principio proseguire l'esecuzione senza che possiate più contestare il credito in questa fase della procedura. È quindi essenziale agire entro il termine anche se ritenete l'esecuzione infondata."},
                {"q": "L'opposizione pone fine definitivamente all'esecuzione?",
                 "a": "No, la sospende: il creditore può chiedere al giudice il rigetto dell'opposizione, o promuovere un'azione di riconoscimento del debito, per poter proseguire l'esecuzione."},
                {"q": "Devo motivare la mia opposizione?",
                 "a": "No, l'opposizione non deve essere motivata per essere valida (art. 74 LEF). Una semplice dichiarazione di opposizione entro il termine è sufficiente per sospendere l'esecuzione."},
            ],
        },
        "en": {
            "slug": "payment-order-how-to-object",
            "title": "Payment order: how to file an objection",
            "meta": "Ten-day deadline, form of the objection, effect on debt collection: what the Federal Debt Enforcement and Bankruptcy Act provides.",
            "sections": [
                {"heading": "What a payment order is", "paragraphs": [
                    "The payment order is the act by which the debt collection office notifies the debtor, at the request of a creditor, of debt collection proceedings for a specific sum of money (art. 69 ff. DEBA). It states the amount claimed, the cause of the obligation, and informs the debtor of their right to object.",
                ]},
                {"heading": "The deadline and form of the objection", "paragraphs": [
                    "A debtor who disputes all or part of the debt can file an objection within ten days of notification of the payment order (art. 74 DEBA). The objection can be made verbally to the debt collection office at the time of notification, or in writing within the deadline, without needing to be reasoned.",
                ]},
                {"heading": "The effects of the objection", "paragraphs": [
                    "A validly filed objection suspends the debt collection proceedings: the creditor cannot continue the procedure without first obtaining the setting aside of the objection from the competent court, through provisional or definitive set-aside proceedings depending on the nature of their claim, or through an action for acknowledgment of debt.",
                ]},
                {"heading": "Do not ignore a payment order", "paragraphs": [
                    "Even a wrongly disputed debt or abusive debt collection must be dealt with by filing an objection within the legal deadline: the absence of an objection in principle allows the creditor to continue the proceedings without the debtor being able to raise objections on the merits of the claim at this stage of the procedure.",
                ]},
            ],
            "faq": [
                {"q": "Within what deadline must I object to a payment order?",
                 "a": "Within ten days of its notification (art. 74 DEBA), verbally to the debt collection office or in writing, without needing to give reasons for the objection."},
                {"q": "What happens if I don't object?",
                 "a": "The creditor can in principle continue the debt collection proceedings without you being able to dispute the claim at this stage of the procedure. It is therefore essential to act within the deadline even if you consider the proceedings unfounded."},
                {"q": "Does the objection permanently end the debt collection proceedings?",
                 "a": "No, it suspends them: the creditor can ask the court to set the objection aside, or bring an action for acknowledgment of debt, to be able to continue the proceedings."},
                {"q": "Do I need to give reasons for my objection?",
                 "a": "No, the objection does not need to be reasoned to be valid (art. 74 DEBA). A simple declaration of objection within the deadline is enough to suspend the proceedings."},
            ],
        },
    },
    "faillite-personnelle-procedure-consequences": {
        "domaine_id": "droit_poursuites_faillite",
        "published": "2026-07-30",
        "fr": {
            "slug": "faillite-personnelle-procedure-consequences",
            "title": "Faillite personnelle : procédure et conséquences",
            "meta": "Ouverture de la faillite, effets sur le patrimoine du débiteur, liquidation par l'office des faillites : ce que prévoit la LP.",
            "sections": [
                {"heading": "Comment une faillite personnelle est ouverte", "paragraphs": [
                    "La faillite d'une personne physique peut être prononcée à la suite d'une poursuite par voie de faillite, réservée à certaines catégories de débiteurs (notamment les personnes inscrites au registre du commerce), ou dans des cas particuliers prévus par la loi sur la poursuite pour dettes et la faillite (LP), sur décision du juge de la faillite (art. 171 ss LP).",
                ]},
                {"heading": "Les effets de l'ouverture de la faillite", "paragraphs": [
                    "Dès l'ouverture de la faillite, le débiteur perd le droit de disposer de ses biens saisissables, qui sont dévolus à la masse en faillite gérée par l'office des faillites. Les poursuites individuelles en cours contre le débiteur sont suspendues au profit de la procédure collective de faillite.",
                ]},
                {"heading": "La liquidation", "paragraphs": [
                    "L'office des faillites établit l'inventaire des biens du débiteur, procède à leur réalisation, et répartit le produit entre les créanciers selon l'ordre des classes de créanciers prévu par la loi (art. 219 LP), certaines créances comme les salaires ou les créances alimentaires bénéficiant d'un privilège de rang supérieur.",
                ]},
                {"heading": "L'acte de défaut de biens", "paragraphs": [
                    "Lorsque le produit de la liquidation ne suffit pas à couvrir l'intégralité des créances, les créanciers non désintéressés reçoivent un acte de défaut de biens, qui atteste du montant impayé et leur permet, sous certaines conditions et dans certains délais, d'introduire une nouvelle poursuite si le débiteur revient à meilleure fortune.",
                ]},
            ],
            "faq": [
                {"q": "Toute personne peut-elle faire l'objet d'une poursuite par voie de faillite ?",
                 "a": "Non, la poursuite par voie de faillite est réservée à certaines catégories de débiteurs, notamment les personnes inscrites au registre du commerce ; les autres personnes physiques sont en principe poursuivies par voie de saisie."},
                {"q": "Que se passe-t-il avec mes biens en cas de faillite personnelle ?",
                 "a": "Vos biens saisissables sont dévolus à la masse en faillite, gérée par l'office des faillites, qui les réalise et en répartit le produit entre les créanciers selon l'ordre légal des classes de créanciers."},
                {"q": "Qu'est-ce qu'un acte de défaut de biens ?",
                 "a": "Le document délivré à un créancier lorsque le produit de la liquidation ne suffit pas à couvrir sa créance, attestant du montant impayé et pouvant permettre, sous conditions, une nouvelle poursuite si le débiteur revient à meilleure fortune."},
            ],
        },
        "de": {
            "slug": "privatkonkurs-verfahren-folgen",
            "title": "Privatkonkurs: Verfahren und Folgen",
            "meta": "Eröffnung des Konkurses, Auswirkungen auf das Vermögen der Schuldnerin oder des Schuldners, Liquidation durch das Konkursamt: was das SchKG vorsieht.",
            "sections": [
                {"heading": "Wie ein Privatkonkurs eröffnet wird", "paragraphs": [
                    "Der Konkurs einer natürlichen Person kann infolge einer Betreibung auf Konkurs eröffnet werden, die bestimmten Schuldnerkategorien vorbehalten ist (namentlich im Handelsregister eingetragenen Personen), oder in besonderen, im Bundesgesetz über Schuldbetreibung und Konkurs (SchKG) vorgesehenen Fällen, auf Entscheid des Konkursrichters oder der Konkursrichterin (Art. 171 ff. SchKG).",
                ]},
                {"heading": "Die Wirkungen der Konkurseröffnung", "paragraphs": [
                    "Mit der Konkurseröffnung verliert die Schuldnerin oder der Schuldner das Verfügungsrecht über ihr oder sein pfändbares Vermögen, das der vom Konkursamt verwalteten Konkursmasse zufällt. Laufende Einzelbetreibungen gegen die Schuldnerin oder den Schuldner werden zugunsten des Konkursverfahrens sistiert.",
                ]},
                {"heading": "Die Liquidation", "paragraphs": [
                    "Das Konkursamt erstellt das Inventar des Vermögens der Schuldnerin oder des Schuldners, nimmt dessen Verwertung vor und verteilt den Erlös unter den Gläubigerinnen und Gläubigern gemäss der gesetzlich vorgesehenen Rangordnung der Gläubigerklassen (Art. 219 SchKG), wobei bestimmte Forderungen wie Löhne oder Unterhaltsforderungen von einem privilegierten Rang profitieren.",
                ]},
                {"heading": "Der Verlustschein", "paragraphs": [
                    "Reicht der Erlös der Liquidation nicht aus, um sämtliche Forderungen zu decken, erhalten die nicht befriedigten Gläubigerinnen und Gläubiger einen Verlustschein, der den unbezahlten Betrag bescheinigt und ihnen unter bestimmten Voraussetzungen und Fristen erlaubt, eine neue Betreibung einzuleiten, falls die Schuldnerin oder der Schuldner wieder zu besseren wirtschaftlichen Verhältnissen kommt.",
                ]},
            ],
            "faq": [
                {"q": "Kann jede Person Gegenstand einer Betreibung auf Konkurs sein?",
                 "a": "Nein, die Betreibung auf Konkurs ist bestimmten Schuldnerkategorien vorbehalten, namentlich im Handelsregister eingetragenen Personen; die übrigen natürlichen Personen werden grundsätzlich auf dem Weg der Pfändung betrieben."},
                {"q": "Was geschieht mit meinem Vermögen bei einem Privatkonkurs?",
                 "a": "Ihr pfändbares Vermögen fällt der vom Konkursamt verwalteten Konkursmasse zu, welche es verwertet und den Erlös unter den Gläubigerinnen und Gläubigern gemäss der gesetzlichen Rangordnung der Gläubigerklassen verteilt."},
                {"q": "Was ist ein Verlustschein?",
                 "a": "Das Dokument, das einer Gläubigerin oder einem Gläubiger ausgestellt wird, wenn der Erlös der Liquidation nicht ausreicht, um ihre oder seine Forderung zu decken; es bescheinigt den unbezahlten Betrag und kann unter bestimmten Voraussetzungen eine neue Betreibung ermöglichen, falls die Schuldnerin oder der Schuldner wieder zu besseren wirtschaftlichen Verhältnissen kommt."},
            ],
        },
        "it": {
            "slug": "fallimento-personale-procedura-conseguenze",
            "title": "Fallimento personale: procedura e conseguenze",
            "meta": "Apertura del fallimento, effetti sul patrimonio del debitore, liquidazione da parte dell'ufficio dei fallimenti: quanto previsto dalla LEF.",
            "sections": [
                {"heading": "Come viene aperto un fallimento personale", "paragraphs": [
                    "Il fallimento di una persona fisica può essere pronunciato a seguito di un'esecuzione in via di fallimento, riservata a determinate categorie di debitori (in particolare le persone iscritte al registro di commercio), o in casi particolari previsti dalla legge federale sull'esecuzione e sul fallimento (LEF), su decisione del giudice del fallimento (art. 171 segg. LEF).",
                ]},
                {"heading": "Gli effetti dell'apertura del fallimento", "paragraphs": [
                    "Con l'apertura del fallimento, il debitore perde il diritto di disporre dei suoi beni pignorabili, che vengono devoluti alla massa fallimentare gestita dall'ufficio dei fallimenti. Le esecuzioni individuali in corso contro il debitore vengono sospese a favore della procedura collettiva di fallimento.",
                ]},
                {"heading": "La liquidazione", "paragraphs": [
                    "L'ufficio dei fallimenti redige l'inventario dei beni del debitore, procede alla loro realizzazione, e ripartisce il ricavato tra i creditori secondo l'ordine delle classi di creditori previsto dalla legge (art. 219 LEF), con alcuni crediti come i salari o i crediti alimentari che beneficiano di un rango privilegiato.",
                ]},
                {"heading": "L'attestato di carenza di beni", "paragraphs": [
                    "Quando il ricavato della liquidazione non basta a coprire l'integralità dei crediti, i creditori non soddisfatti ricevono un attestato di carenza di beni, che attesta l'importo non pagato e permette loro, a determinate condizioni e entro determinati termini, di avviare una nuova esecuzione se il debitore torna a miglior fortuna.",
                ]},
            ],
            "faq": [
                {"q": "Chiunque può essere oggetto di un'esecuzione in via di fallimento?",
                 "a": "No, l'esecuzione in via di fallimento è riservata a determinate categorie di debitori, in particolare le persone iscritte al registro di commercio; le altre persone fisiche sono in linea di principio escusse per via di pignoramento."},
                {"q": "Cosa succede ai miei beni in caso di fallimento personale?",
                 "a": "I vostri beni pignorabili vengono devoluti alla massa fallimentare, gestita dall'ufficio dei fallimenti, che li realizza e ne ripartisce il ricavato tra i creditori secondo l'ordine legale delle classi di creditori."},
                {"q": "Cos'è un attestato di carenza di beni?",
                 "a": "Il documento rilasciato a un creditore quando il ricavato della liquidazione non basta a coprire il suo credito, che attesta l'importo non pagato e può permettere, a determinate condizioni, una nuova esecuzione se il debitore torna a miglior fortuna."},
            ],
        },
        "en": {
            "slug": "personal-bankruptcy-procedure-consequences",
            "title": "Personal bankruptcy: procedure and consequences",
            "meta": "Opening of bankruptcy, effects on the debtor's assets, liquidation by the bankruptcy office: what the Debt Enforcement and Bankruptcy Act provides.",
            "sections": [
                {"heading": "How personal bankruptcy is opened", "paragraphs": [
                    "The bankruptcy of an individual can be declared following bankruptcy proceedings, reserved for certain categories of debtors (in particular persons registered with the commercial register), or in special cases provided for by the Debt Enforcement and Bankruptcy Act (DEBA), by decision of the bankruptcy judge (art. 171 ff. DEBA).",
                ]},
                {"heading": "The effects of opening bankruptcy", "paragraphs": [
                    "Upon the opening of bankruptcy, the debtor loses the right to dispose of their seizable assets, which are transferred to the bankruptcy estate managed by the bankruptcy office. Individual debt collection proceedings against the debtor already underway are suspended in favour of the collective bankruptcy procedure.",
                ]},
                {"heading": "Liquidation", "paragraphs": [
                    "The bankruptcy office draws up an inventory of the debtor's assets, sells them, and distributes the proceeds among creditors according to the order of creditor classes set by law (art. 219 DEBA), with certain claims such as wages or maintenance claims benefiting from a privileged rank.",
                ]},
                {"heading": "The certificate of unpaid debt", "paragraphs": [
                    "When the proceeds of liquidation are insufficient to cover all claims in full, unpaid creditors receive a certificate of unpaid debt, which certifies the unpaid amount and allows them, under certain conditions and time limits, to initiate new debt collection proceedings if the debtor's financial situation improves.",
                ]},
            ],
            "faq": [
                {"q": "Can anyone be subject to bankruptcy proceedings?",
                 "a": "No, bankruptcy proceedings are reserved for certain categories of debtors, in particular persons registered with the commercial register; other individuals are in principle subject to seizure proceedings instead."},
                {"q": "What happens to my assets in personal bankruptcy?",
                 "a": "Your seizable assets are transferred to the bankruptcy estate, managed by the bankruptcy office, which sells them and distributes the proceeds among creditors according to the legal order of creditor classes."},
                {"q": "What is a certificate of unpaid debt?",
                 "a": "The document issued to a creditor when the proceeds of liquidation are insufficient to cover their claim, certifying the unpaid amount and allowing, under certain conditions, new debt collection proceedings if the debtor's financial situation improves."},
            ],
        },
    },
    "curatelle-quand-comment-prononcee": {
        "domaine_id": "droit_protection_enfant_adulte",
        "published": "2026-07-30",
        "fr": {
            "slug": "curatelle-quand-comment-elle-est-prononcee",
            "title": "Curatelle : quand et comment elle est prononcée",
            "meta": "Curatelle d'accompagnement, de représentation, de coopération ou de portée générale : les types de mesures prévues par le Code civil.",
            "sections": [
                {"heading": "Le principe de proportionnalité", "paragraphs": [
                    "Une curatelle ne peut être instituée que si l'aide apportée par la famille, les proches ou les services publics ou privés ne suffit pas ou n'est pas envisageable, et que la personne concernée a besoin d'aide en raison d'une déficience mentale, de troubles psychiques ou d'un autre état de faiblesse (art. 390 CC). L'autorité de protection de l'adulte (APEA) doit choisir la mesure la moins incisive possible pour les intérêts de la personne concernée.",
                ]},
                {"heading": "Les différents types de curatelle", "paragraphs": [
                    "Le Code civil distingue la curatelle d'accompagnement, la plus légère, où la personne concernée conserve l'exercice des droits civils et le curateur ne fait qu'apporter un soutien (art. 393 CC) ; la curatelle de représentation, où le curateur agit au nom de la personne pour certaines tâches définies (art. 394 CC) ; la curatelle de coopération, qui soumet certains actes à l'accord du curateur (art. 396 CC) ; et la curatelle de portée générale, la plus étendue, réservée aux cas de besoin d'aide durable et complet (art. 398 CC).",
                ]},
                {"heading": "La procédure devant l'APEA", "paragraphs": [
                    "L'APEA du domicile de la personne concernée instruit la demande, qui peut émaner de la personne elle-même, d'un proche, ou être ouverte d'office sur signalement. La personne concernée est en principe entendue personnellement, et une expertise peut être ordonnée pour évaluer précisément son état et ses besoins.",
                ]},
                {"heading": "Le réexamen de la mesure", "paragraphs": [
                    "Une curatelle n'est pas figée : elle doit être réexaminée périodiquement par l'APEA, et peut être levée dès que les conditions qui la justifiaient ont disparu, ou adaptée si les besoins de la personne concernée évoluent dans un sens ou dans l'autre.",
                ]},
            ],
            "faq": [
                {"q": "Une curatelle prive-t-elle automatiquement la personne de tous ses droits ?",
                 "a": "Non, cela dépend du type de curatelle prononcée : la curatelle d'accompagnement, la plus légère, n'entraîne aucune restriction des droits civils. Seule la curatelle de portée générale, réservée aux besoins les plus étendus, prive la personne de l'exercice des droits civils."},
                {"q": "Qui peut demander l'ouverture d'une curatelle ?",
                 "a": "La personne concernée elle-même, un proche, ou l'APEA peut agir d'office sur signalement d'un tiers (médecin, service social, voisin) si les conditions légales paraissent réunies."},
                {"q": "Une curatelle peut-elle être levée ?",
                 "a": "Oui, l'APEA doit réexaminer périodiquement la mesure et la lever dès que les conditions qui la justifiaient ont disparu, ou l'adapter si la situation de la personne concernée évolue."},
            ],
        },
        "de": {
            "slug": "beistandschaft-wann-wie-angeordnet",
            "title": "Beistandschaft: wann und wie sie angeordnet wird",
            "meta": "Begleitbeistandschaft, Vertretungsbeistandschaft, Mitwirkungs- oder umfassende Beistandschaft: die Massnahmen des Zivilgesetzbuchs.",
            "sections": [
                {"heading": "Der Grundsatz der Verhältnismässigkeit", "paragraphs": [
                    "Eine Beistandschaft kann nur errichtet werden, wenn die Unterstützung durch die Familie, nahestehende Personen oder öffentliche oder private Dienste nicht ausreicht oder nicht in Frage kommt, und die betroffene Person aufgrund einer geistigen Behinderung, psychischer Störung oder eines anderen Schwächezustands Unterstützung benötigt (Art. 390 ZGB). Die Kindes- und Erwachsenenschutzbehörde (KESB) muss die am wenigsten einschneidende, den Interessen der betroffenen Person gerecht werdende Massnahme wählen.",
                ]},
                {"heading": "Die verschiedenen Arten der Beistandschaft", "paragraphs": [
                    "Das Zivilgesetzbuch unterscheidet die Begleitbeistandschaft, die leichteste, bei der die betroffene Person die Ausübung der Handlungsfähigkeit behält und die Beiständin oder der Beistand lediglich Unterstützung leistet (Art. 393 ZGB); die Vertretungsbeistandschaft, bei der die Beiständin oder der Beistand im Namen der betroffenen Person für bestimmte festgelegte Aufgaben handelt (Art. 394 ZGB); die Mitwirkungsbeistandschaft, die bestimmte Handlungen der Zustimmung der Beiständin oder des Beistands unterstellt (Art. 396 ZGB); und die umfassende Beistandschaft, die weitestgehende, welche für dauerhaften und umfassenden Unterstützungsbedarf vorbehalten ist (Art. 398 ZGB).",
                ]},
                {"heading": "Das Verfahren vor der KESB", "paragraphs": [
                    "Die KESB am Wohnsitz der betroffenen Person untersucht das Gesuch, das von der betroffenen Person selbst, einer nahestehenden Person stammen kann, oder von Amtes wegen aufgrund einer Meldung eröffnet werden kann. Die betroffene Person wird grundsätzlich persönlich angehört, und ein Gutachten kann angeordnet werden, um ihren Zustand und ihre Bedürfnisse genau zu beurteilen.",
                ]},
                {"heading": "Die Überprüfung der Massnahme", "paragraphs": [
                    "Eine Beistandschaft ist nicht endgültig festgelegt: sie muss von der KESB periodisch überprüft werden und kann aufgehoben werden, sobald die Voraussetzungen, die sie rechtfertigten, weggefallen sind, oder angepasst werden, wenn sich die Bedürfnisse der betroffenen Person in die eine oder andere Richtung verändern.",
                ]},
            ],
            "faq": [
                {"q": "Entzieht eine Beistandschaft automatisch alle Rechte der betroffenen Person?",
                 "a": "Nein, das hängt von der angeordneten Art der Beistandschaft ab: die Begleitbeistandschaft, die leichteste, führt zu keiner Einschränkung der Handlungsfähigkeit. Nur die umfassende Beistandschaft, die für den weitestgehenden Unterstützungsbedarf vorbehalten ist, entzieht der Person die Ausübung der Handlungsfähigkeit."},
                {"q": "Wer kann die Errichtung einer Beistandschaft beantragen?",
                 "a": "Die betroffene Person selbst, eine nahestehende Person, oder die KESB kann von Amtes wegen aufgrund einer Meldung eines Dritten (Ärztin, Arzt, Sozialdienst, Nachbarin, Nachbar) handeln, wenn die gesetzlichen Voraussetzungen erfüllt scheinen."},
                {"q": "Kann eine Beistandschaft aufgehoben werden?",
                 "a": "Ja, die KESB muss die Massnahme periodisch überprüfen und aufheben, sobald die Voraussetzungen, die sie rechtfertigten, weggefallen sind, oder sie anpassen, wenn sich die Situation der betroffenen Person verändert."},
            ],
        },
        "it": {
            "slug": "curatela-quando-come-viene-decisa",
            "title": "Curatela: quando e come viene decisa",
            "meta": "Curatela di accompagnamento, di rappresentanza, di cooperazione o generale: le misure previste dal Codice civile.",
            "sections": [
                {"heading": "Il principio di proporzionalità", "paragraphs": [
                    "Una curatela può essere istituita solo se l'aiuto fornito dalla famiglia, da persone vicine o da servizi pubblici o privati non è sufficiente o non è ipotizzabile, e la persona interessata necessita di aiuto a causa di una disabilità mentale, di turbe psichiche o di un altro stato di debolezza (art. 390 CC). L'autorità di protezione degli adulti (APA) deve scegliere la misura meno incisiva possibile per gli interessi della persona interessata.",
                ]},
                {"heading": "I diversi tipi di curatela", "paragraphs": [
                    "Il Codice civile distingue la curatela di accompagnamento, la più leggera, dove la persona interessata conserva l'esercizio dei diritti civili e il curatore si limita a fornire un sostegno (art. 393 CC); la curatela di rappresentanza, dove il curatore agisce a nome della persona per determinati compiti definiti (art. 394 CC); la curatela di cooperazione, che sottopone determinati atti al consenso del curatore (art. 396 CC); e la curatela generale, la più estesa, riservata ai casi di bisogno d'aiuto duraturo e completo (art. 398 CC).",
                ]},
                {"heading": "La procedura davanti all'APA", "paragraphs": [
                    "L'APA del domicilio della persona interessata istruisce la domanda, che può provenire dalla persona stessa, da una persona vicina, o essere aperta d'ufficio su segnalazione. La persona interessata viene in linea di principio sentita personalmente, e può essere ordinata una perizia per valutare precisamente il suo stato e i suoi bisogni.",
                ]},
                {"heading": "Il riesame della misura", "paragraphs": [
                    "Una curatela non è definitiva: deve essere riesaminata periodicamente dall'APA, e può essere revocata non appena le condizioni che la giustificavano sono venute meno, o adattata se i bisogni della persona interessata evolvono in un senso o nell'altro.",
                ]},
            ],
            "faq": [
                {"q": "Una curatela priva automaticamente la persona di tutti i suoi diritti?",
                 "a": "No, dipende dal tipo di curatela pronunciata: la curatela di accompagnamento, la più leggera, non comporta alcuna restrizione dei diritti civili. Solo la curatela generale, riservata ai bisogni più estesi, priva la persona dell'esercizio dei diritti civili."},
                {"q": "Chi può chiedere l'istituzione di una curatela?",
                 "a": "La persona interessata stessa, una persona vicina, o l'APA può agire d'ufficio su segnalazione di un terzo (medico, servizio sociale, vicino) se le condizioni legali sembrano riunite."},
                {"q": "Una curatela può essere revocata?",
                 "a": "Sì, l'APA deve riesaminare periodicamente la misura e revocarla non appena le condizioni che la giustificavano sono venute meno, o adattarla se la situazione della persona interessata evolve."},
            ],
        },
        "en": {
            "slug": "deputyship-when-how-ordered",
            "title": "Deputyship: when and how it is ordered",
            "meta": "Companionship, representative, co-management and general deputyship: the measures provided by the Civil Code.",
            "sections": [
                {"heading": "The principle of proportionality", "paragraphs": [
                    "A deputyship can only be set up if support from family, close contacts, or public or private services is insufficient or not feasible, and the person concerned needs help due to a mental disability, psychiatric disorder, or another state of weakness (art. 390 CC). The adult protection authority must choose the least restrictive measure that serves the interests of the person concerned.",
                ]},
                {"heading": "The different types of deputyship", "paragraphs": [
                    "The Civil Code distinguishes companionship deputyship, the lightest form, where the person concerned retains the exercise of civil rights and the deputy merely provides support (art. 393 CC); representative deputyship, where the deputy acts on the person's behalf for certain defined tasks (art. 394 CC); co-management deputyship, which subjects certain acts to the deputy's consent (art. 396 CC); and general deputyship, the most extensive, reserved for lasting and comprehensive needs for help (art. 398 CC).",
                ]},
                {"heading": "The procedure before the adult protection authority", "paragraphs": [
                    "The adult protection authority of the domicile of the person concerned examines the request, which can come from the person themselves, a close contact, or be opened on its own initiative following a report. The person concerned is in principle heard in person, and an assessment can be ordered to precisely evaluate their condition and needs.",
                ]},
                {"heading": "Reviewing the measure", "paragraphs": [
                    "A deputyship is not fixed forever: it must be periodically reviewed by the adult protection authority and lifted as soon as the conditions justifying it have disappeared, or adjusted if the needs of the person concerned change in one direction or another.",
                ]},
            ],
            "faq": [
                {"q": "Does a deputyship automatically strip the person of all their rights?",
                 "a": "No, this depends on the type of deputyship ordered: companionship deputyship, the lightest form, involves no restriction of civil rights. Only general deputyship, reserved for the most extensive needs, deprives the person of the exercise of civil rights."},
                {"q": "Who can request that a deputyship be set up?",
                 "a": "The person concerned themselves, a close contact, or the adult protection authority can act on its own initiative following a report from a third party (doctor, social service, neighbour) if the legal conditions appear to be met."},
                {"q": "Can a deputyship be lifted?",
                 "a": "Yes, the adult protection authority must periodically review the measure and lift it as soon as the conditions justifying it have disappeared, or adjust it if the situation of the person concerned changes."},
            ],
        },
    },
    "mandat-cause-inaptitude-anticiper": {
        "domaine_id": "droit_protection_enfant_adulte",
        "published": "2026-07-30",
        "fr": {
            "slug": "mandat-cause-inaptitude-anticiper-incapacite",
            "title": "Mandat pour cause d'inaptitude : anticiper l'incapacité",
            "meta": "Désigner à l'avance une personne de confiance pour gérer ses affaires en cas de perte de discernement, selon le Code civil.",
            "sections": [
                {"heading": "À quoi sert le mandat pour cause d'inaptitude", "paragraphs": [
                    "Le mandat pour cause d'inaptitude (art. 360-369 CC) permet à toute personne capable de discernement de charger une ou plusieurs personnes physiques ou morales de s'occuper de ses affaires personnelles, de gérer son patrimoine et de la représenter juridiquement, pour le cas où elle deviendrait un jour incapable de discernement.",
                ]},
                {"heading": "La forme du mandat", "paragraphs": [
                    "Le mandat doit être rédigé entièrement à la main, daté et signé par le mandant, ou fait par acte authentique devant notaire (art. 361 CC). Un document simplement tapé et signé ne remplit pas les conditions de forme et n'est pas valable, à moins de passer par la voie notariée.",
                ]},
                {"heading": "La validation par l'autorité de protection de l'adulte", "paragraphs": [
                    "Lorsque l'incapacité de discernement du mandant survient effectivement, l'APEA vérifie que le mandat a été valablement constitué, que le mandataire est apte à remplir sa tâche, et procède à la validation du mandat, qui déploie alors ses effets. L'APEA peut, dans certains cas, exercer une surveillance sur l'exécution du mandat.",
                ]},
                {"heading": "L'articulation avec les directives anticipées", "paragraphs": [
                    "Le mandat pour cause d'inaptitude porte sur la gestion des affaires personnelles et patrimoniales ; il se distingue des directives anticipées du patient, qui concernent spécifiquement les décisions médicales et les traitements souhaités ou refusés en cas d'incapacité de discernement, régies par des dispositions propres du Code civil.",
                ]},
            ],
            "faq": [
                {"q": "Le mandat pour cause d'inaptitude doit-il être écrit à la main ?",
                 "a": "Oui, sauf s'il est fait par acte authentique devant notaire : un mandat manuscrit doit être rédigé entièrement à la main, daté et signé par le mandant (art. 361 CC)."},
                {"q": "Quand le mandat prend-il effet ?",
                 "a": "Seulement lorsque l'incapacité de discernement du mandant survient effectivement et que l'APEA a validé le mandat après avoir vérifié sa validité formelle et l'aptitude du mandataire désigné."},
                {"q": "Le mandat pour cause d'inaptitude remplace-t-il les directives anticipées du patient ?",
                 "a": "Non, ce sont deux instruments distincts et complémentaires : le mandat porte sur les affaires personnelles et patrimoniales, tandis que les directives anticipées concernent spécifiquement les décisions médicales."},
            ],
        },
        "de": {
            "slug": "vorsorgeauftrag-eigene-urteilsunfaehigkeit-vorsorgen",
            "title": "Vorsorgeauftrag: der eigenen Urteilsunfähigkeit vorsorgen",
            "meta": "Eine Vertrauensperson im Voraus bestimmen, um bei Verlust der Urteilsfähigkeit die eigenen Angelegenheiten zu regeln, gemäss Zivilgesetzbuch.",
            "sections": [
                {"heading": "Wozu der Vorsorgeauftrag dient", "paragraphs": [
                    "Der Vorsorgeauftrag (Art. 360-369 ZGB) erlaubt jeder urteilsfähigen Person, eine oder mehrere natürliche oder juristische Personen zu beauftragen, sich um ihre persönlichen Angelegenheiten zu kümmern, ihr Vermögen zu verwalten und sie rechtlich zu vertreten, für den Fall, dass sie eines Tages urteilsunfähig werden sollte.",
                ]},
                {"heading": "Die Form des Auftrags", "paragraphs": [
                    "Der Auftrag muss vollständig von Hand geschrieben, datiert und von der auftraggebenden Person unterschrieben werden, oder öffentlich beurkundet werden (Art. 361 ZGB). Ein blosser am Computer getippter und unterschriebener Text erfüllt die Formvoraussetzungen nicht und ist nicht gültig, ausser bei öffentlicher Beurkundung.",
                ]},
                {"heading": "Die Validierung durch die Erwachsenenschutzbehörde", "paragraphs": [
                    "Tritt die Urteilsunfähigkeit der auftraggebenden Person tatsächlich ein, prüft die KESB, ob der Auftrag gültig errichtet wurde, ob die beauftragte Person zur Erfüllung ihrer Aufgabe geeignet ist, und validiert den Auftrag, der dann seine Wirkung entfaltet. Die KESB kann in bestimmten Fällen eine Aufsicht über die Ausführung des Auftrags ausüben.",
                ]},
                {"heading": "Das Verhältnis zur Patientenverfügung", "paragraphs": [
                    "Der Vorsorgeauftrag betrifft die Verwaltung der persönlichen und vermögensrechtlichen Angelegenheiten; er unterscheidet sich von der Patientenverfügung, die sich speziell auf medizinische Entscheidungen und gewünschte oder abgelehnte Behandlungen bei Urteilsunfähigkeit bezieht, geregelt durch eigene Bestimmungen des Zivilgesetzbuchs.",
                ]},
            ],
            "faq": [
                {"q": "Muss der Vorsorgeauftrag von Hand geschrieben werden?",
                 "a": "Ja, ausser bei öffentlicher Beurkundung: ein eigenhändiger Vorsorgeauftrag muss vollständig von Hand geschrieben, datiert und von der auftraggebenden Person unterschrieben werden (Art. 361 ZGB)."},
                {"q": "Wann tritt der Auftrag in Kraft?",
                 "a": "Erst wenn die Urteilsunfähigkeit der auftraggebenden Person tatsächlich eintritt und die KESB den Auftrag validiert hat, nachdem sie dessen Gültigkeit und die Eignung der beauftragten Person geprüft hat."},
                {"q": "Ersetzt der Vorsorgeauftrag die Patientenverfügung?",
                 "a": "Nein, das sind zwei unterschiedliche und sich ergänzende Instrumente: der Auftrag betrifft die persönlichen und vermögensrechtlichen Angelegenheiten, während sich die Patientenverfügung speziell auf medizinische Entscheidungen bezieht."},
            ],
        },
        "it": {
            "slug": "mandato-precauzionale-anticipare-incapacita",
            "title": "Mandato precauzionale: anticipare l'incapacità",
            "meta": "Designare in anticipo una persona di fiducia per gestire i propri affari in caso di perdita del discernimento, secondo il Codice civile.",
            "sections": [
                {"heading": "A cosa serve il mandato precauzionale", "paragraphs": [
                    "Il mandato precauzionale (art. 360-369 CC) permette a chiunque sia capace di discernimento di incaricare una o più persone fisiche o giuridiche di occuparsi dei propri affari personali, di gestire il proprio patrimonio e di rappresentarlo giuridicamente, nel caso in cui diventi un giorno incapace di discernimento.",
                ]},
                {"heading": "La forma del mandato", "paragraphs": [
                    "Il mandato deve essere redatto interamente a mano, datato e firmato dal mandante, oppure fatto per atto pubblico davanti a notaio (art. 361 CC). Un documento semplicemente digitato e firmato non soddisfa le condizioni di forma e non è valido, salvo la via notarile.",
                ]},
                {"heading": "La validazione da parte dell'autorità di protezione degli adulti", "paragraphs": [
                    "Quando l'incapacità di discernimento del mandante sopraggiunge effettivamente, l'APA verifica che il mandato sia stato validamente costituito, che il mandatario sia idoneo a svolgere il suo compito, e procede alla validazione del mandato, che allora dispiega i suoi effetti. L'APA può, in determinati casi, esercitare una sorveglianza sull'esecuzione del mandato.",
                ]},
                {"heading": "L'articolazione con le direttive del paziente", "paragraphs": [
                    "Il mandato precauzionale riguarda la gestione degli affari personali e patrimoniali; si distingue dalle direttive anticipate del paziente, che concernono specificamente le decisioni mediche e i trattamenti desiderati o rifiutati in caso di incapacità di discernimento, disciplinate da disposizioni proprie del Codice civile.",
                ]},
            ],
            "faq": [
                {"q": "Il mandato precauzionale deve essere scritto a mano?",
                 "a": "Sì, salvo se fatto per atto pubblico davanti a notaio: un mandato olografo deve essere redatto interamente a mano, datato e firmato dal mandante (art. 361 CC)."},
                {"q": "Quando entra in vigore il mandato?",
                 "a": "Solo quando l'incapacità di discernimento del mandante sopraggiunge effettivamente e l'APA ha validato il mandato dopo averne verificato la validità e l'idoneità del mandatario designato."},
                {"q": "Il mandato precauzionale sostituisce le direttive anticipate del paziente?",
                 "a": "No, sono due strumenti distinti e complementari: il mandato riguarda gli affari personali e patrimoniali, mentre le direttive anticipate concernono specificamente le decisioni mediche."},
            ],
        },
        "en": {
            "slug": "power-of-attorney-incapacity-planning-ahead",
            "title": "Power of attorney for incapacity: planning ahead",
            "meta": "Appointing a trusted person in advance to manage your affairs if you lose capacity of judgment, under the Civil Code.",
            "sections": [
                {"heading": "The purpose of the power of attorney for incapacity", "paragraphs": [
                    "The power of attorney for incapacity (art. 360-369 CC) allows anyone with capacity of judgment to appoint one or more individuals or legal entities to take care of their personal affairs, manage their assets, and represent them legally, in case they should one day become incapable of judgment.",
                ]},
                {"heading": "The form of the power of attorney", "paragraphs": [
                    "The document must be written entirely by hand, dated and signed by the person granting it, or drawn up by public deed (art. 361 CC). A merely typed and signed document does not meet the formal requirements and is not valid, except via the notarial route.",
                ]},
                {"heading": "Validation by the adult protection authority", "paragraphs": [
                    "When the incapacity of judgment of the person who granted the power of attorney actually occurs, the adult protection authority checks that the document was validly drawn up, that the appointed person is suitable to carry out their task, and validates the power of attorney, which then takes effect. The authority can, in certain cases, exercise oversight over how the power of attorney is carried out.",
                ]},
                {"heading": "How it relates to patient directives", "paragraphs": [
                    "The power of attorney for incapacity concerns the management of personal and financial affairs; it is distinct from advance patient directives, which specifically concern medical decisions and desired or refused treatments in the event of incapacity of judgment, governed by their own provisions of the Civil Code.",
                ]},
            ],
            "faq": [
                {"q": "Does the power of attorney for incapacity need to be handwritten?",
                 "a": "Yes, unless drawn up by public deed: a handwritten power of attorney for incapacity must be written entirely by hand, dated and signed by the grantor (art. 361 CC)."},
                {"q": "When does the power of attorney take effect?",
                 "a": "Only when the grantor's incapacity of judgment actually occurs and the adult protection authority has validated the document after checking its validity and the suitability of the appointed person."},
                {"q": "Does the power of attorney for incapacity replace advance patient directives?",
                 "a": "No, these are two distinct, complementary instruments: the power of attorney concerns personal and financial affairs, while advance directives specifically concern medical decisions."},
            ],
        },
    },
    "contester-decision-taxation-reclamation": {
        "domaine_id": "droit_fiscal",
        "published": "2026-07-30",
        "fr": {
            "slug": "contester-decision-taxation-reclamation-delais",
            "title": "Contester une décision de taxation : réclamation",
            "meta": "Délai de 30 jours, forme de la réclamation, recours ultérieur : la procédure pour contester une taxation selon la LIFD.",
            "sections": [
                {"heading": "La réclamation, première étape obligatoire", "paragraphs": [
                    "Le contribuable qui conteste sa décision de taxation pour l'impôt fédéral direct doit d'abord déposer une réclamation écrite auprès de l'autorité de taxation, dans les 30 jours suivant la notification de la décision (art. 132 LIFD). La réclamation doit contenir des conclusions motivées et, si possible, les moyens de preuve à l'appui.",
                ]},
                {"heading": "Le contenu de la réclamation", "paragraphs": [
                    "La réclamation doit indiquer précisément les points contestés de la taxation et les motifs pour lesquels le contribuable estime la décision erronée : éléments de revenu ou de fortune mal évalués, déductions refusées à tort, erreur de calcul, ou violation d'une règle de procédure.",
                ]},
                {"heading": "Le traitement de la réclamation", "paragraphs": [
                    "L'autorité de taxation réexamine le dossier et peut confirmer, réduire ou même augmenter la taxation contestée (reformatio in pejus), sous réserve d'en informer le contribuable et de lui donner l'occasion de se déterminer avant une décision qui lui serait défavorable.",
                ]},
                {"heading": "Le recours ultérieur", "paragraphs": [
                    "Si la décision sur réclamation ne satisfait pas le contribuable, il peut la porter devant la commission cantonale de recours en matière fiscale, puis, selon les cas, devant le tribunal cantonal et enfin le Tribunal fédéral, dans les délais et formes prévus par la procédure applicable à chaque instance.",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai dois-je réclamer contre ma taxation ?",
                 "a": "Dans les 30 jours suivant la notification de la décision de taxation, par une réclamation écrite et motivée adressée à l'autorité de taxation (art. 132 LIFD)."},
                {"q": "La réclamation peut-elle aboutir à une taxation plus élevée ?",
                 "a": "Oui, l'autorité de taxation peut en principe réexaminer l'ensemble du dossier et augmenter la taxation contestée, à condition d'en informer le contribuable et de lui donner l'occasion de se déterminer au préalable."},
                {"q": "Que faire si la réclamation est rejetée ?",
                 "a": "Vous pouvez porter la décision sur réclamation devant la commission cantonale de recours en matière fiscale, puis, selon les cas, devant les instances judiciaires supérieures compétentes."},
            ],
        },
        "de": {
            "slug": "steuerveranlagung-anfechten-einsprache-fristen",
            "title": "Steuerveranlagung anfechten: Einsprache und Fristen",
            "meta": "30-tägige Frist, Form der Einsprache, weiteres Rechtsmittel: das Verfahren zur Anfechtung einer Veranlagung gemäss DBG.",
            "sections": [
                {"heading": "Die Einsprache, obligatorischer erster Schritt", "paragraphs": [
                    "Die steuerpflichtige Person, die ihre Veranlagung für die direkte Bundessteuer anficht, muss zunächst eine schriftliche Einsprache bei der Veranlagungsbehörde einreichen, innert 30 Tagen nach Eröffnung der Verfügung (Art. 132 DBG). Die Einsprache muss begründete Anträge und, soweit möglich, die zur Untermauerung dienenden Beweismittel enthalten.",
                ]},
                {"heading": "Der Inhalt der Einsprache", "paragraphs": [
                    "Die Einsprache muss genau angeben, welche Punkte der Veranlagung bestritten werden und aus welchen Gründen die steuerpflichtige Person die Verfügung für fehlerhaft hält: falsch bewertete Einkommens- oder Vermögenselemente, zu Unrecht verweigerte Abzüge, Rechenfehler, oder Verletzung einer Verfahrensregel.",
                ]},
                {"heading": "Die Behandlung der Einsprache", "paragraphs": [
                    "Die Veranlagungsbehörde prüft das Dossier erneut und kann die angefochtene Veranlagung bestätigen, herabsetzen oder sogar erhöhen (reformatio in peius), unter Vorbehalt, die steuerpflichtige Person darüber zu informieren und ihr Gelegenheit zur Stellungnahme zu geben, bevor ein für sie ungünstiger Entscheid ergeht.",
                ]},
                {"heading": "Das weitere Rechtsmittel", "paragraphs": [
                    "Befriedigt der Einspracheentscheid die steuerpflichtige Person nicht, kann sie ihn bei der kantonalen Steuerrekurskommission anfechten, danach je nach Fall beim kantonalen Verwaltungsgericht und schliesslich beim Bundesgericht, innert der für jede Instanz vorgesehenen Fristen und Formen.",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist muss ich gegen meine Veranlagung Einsprache erheben?",
                 "a": "Innert 30 Tagen nach Eröffnung der Veranlagungsverfügung, durch eine schriftliche und begründete Einsprache an die Veranlagungsbehörde (Art. 132 DBG)."},
                {"q": "Kann die Einsprache zu einer höheren Veranlagung führen?",
                 "a": "Ja, die Veranlagungsbehörde kann grundsätzlich das gesamte Dossier erneut prüfen und die angefochtene Veranlagung erhöhen, sofern sie die steuerpflichtige Person darüber informiert und ihr vorgängig Gelegenheit zur Stellungnahme gibt."},
                {"q": "Was tun, wenn die Einsprache abgelehnt wird?",
                 "a": "Sie können den Einspracheentscheid bei der zuständigen kantonalen Steuerrekurskommission anfechten, danach je nach Fall bei den zuständigen höheren Gerichtsinstanzen."},
            ],
        },
        "it": {
            "slug": "contestare-decisione-tassazione-reclamo-termini",
            "title": "Contestare una decisione di tassazione: il reclamo",
            "meta": "Termine di 30 giorni, forma del reclamo, ricorso successivo: la procedura per contestare una tassazione secondo la LIFD.",
            "sections": [
                {"heading": "Il reclamo, prima tappa obbligatoria", "paragraphs": [
                    "Il contribuente che contesta la propria tassazione per l'imposta federale diretta deve prima presentare un reclamo scritto presso l'autorità di tassazione, entro 30 giorni dalla notifica della decisione (art. 132 LIFD). Il reclamo deve contenere conclusioni motivate e, se possibile, i mezzi di prova a sostegno.",
                ]},
                {"heading": "Il contenuto del reclamo", "paragraphs": [
                    "Il reclamo deve indicare precisamente i punti contestati della tassazione e i motivi per cui il contribuente ritiene errata la decisione: elementi di reddito o di sostanza valutati male, deduzioni rifiutate a torto, errore di calcolo, o violazione di una regola procedurale.",
                ]},
                {"heading": "Il trattamento del reclamo", "paragraphs": [
                    "L'autorità di tassazione riesamina l'incarto e può confermare, ridurre o persino aumentare la tassazione contestata (reformatio in pejus), con riserva di informarne il contribuente e di dargli l'occasione di determinarsi prima di una decisione a lui sfavorevole.",
                ]},
                {"heading": "Il ricorso successivo", "paragraphs": [
                    "Se la decisione su reclamo non soddisfa il contribuente, questi può portarla davanti alla commissione cantonale di ricorso in materia fiscale, poi, secondo i casi, davanti al tribunale cantonale e infine al Tribunale federale, entro i termini e le forme previste per ciascuna istanza.",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine devo reclamare contro la mia tassazione?",
                 "a": "Entro 30 giorni dalla notifica della decisione di tassazione, tramite un reclamo scritto e motivato indirizzato all'autorità di tassazione (art. 132 LIFD)."},
                {"q": "Il reclamo può portare a una tassazione più elevata?",
                 "a": "Sì, l'autorità di tassazione può in linea di principio riesaminare l'intero incarto e aumentare la tassazione contestata, a condizione di informarne il contribuente e di dargli previamente l'occasione di determinarsi."},
                {"q": "Cosa fare se il reclamo viene respinto?",
                 "a": "Potete portare la decisione su reclamo davanti alla commissione cantonale di ricorso in materia fiscale, poi, secondo i casi, davanti alle istanze giudiziarie superiori competenti."},
            ],
        },
        "en": {
            "slug": "challenging-tax-assessment-objection-deadlines",
            "title": "Challenging a tax assessment: filing an objection",
            "meta": "30-day deadline, form of the objection, further appeal: the procedure for challenging a tax assessment under the DFTA.",
            "sections": [
                {"heading": "The objection, a mandatory first step", "paragraphs": [
                    "A taxpayer who disputes their direct federal tax assessment must first file a written objection with the assessment authority, within 30 days of notification of the decision (art. 132 DFTA). The objection must contain reasoned submissions and, where possible, supporting evidence.",
                ]},
                {"heading": "The content of the objection", "paragraphs": [
                    "The objection must precisely state the disputed points of the assessment and the reasons why the taxpayer considers the decision incorrect: income or wealth items wrongly assessed, deductions wrongly refused, a calculation error, or a breach of a procedural rule.",
                ]},
                {"heading": "How the objection is handled", "paragraphs": [
                    "The assessment authority re-examines the file and can confirm, reduce or even increase the disputed assessment (reformatio in pejus), subject to informing the taxpayer and giving them the opportunity to comment before a decision unfavourable to them is issued.",
                ]},
                {"heading": "Further appeal", "paragraphs": [
                    "If the decision on the objection does not satisfy the taxpayer, they can bring it before the cantonal tax appeals commission, then, depending on the case, before the cantonal administrative court and finally the Federal Supreme Court, within the deadlines and forms provided for each instance.",
                ]},
            ],
            "faq": [
                {"q": "Within what deadline must I object to my tax assessment?",
                 "a": "Within 30 days of notification of the assessment decision, through a written and reasoned objection addressed to the assessment authority (art. 132 DFTA)."},
                {"q": "Can an objection lead to a higher assessment?",
                 "a": "Yes, the assessment authority can in principle re-examine the entire file and increase the disputed assessment, provided it informs the taxpayer and gives them the opportunity to comment beforehand."},
                {"q": "What should I do if my objection is rejected?",
                 "a": "You can bring the decision on the objection before the competent cantonal tax appeals commission, then, depending on the case, before the competent higher courts."},
            ],
        },
    },
    "imposition-source-qui-concerne-fonctionnement": {
        "domaine_id": "droit_fiscal",
        "published": "2026-07-30",
        "fr": {
            "slug": "imposition-source-qui-concerne-fonctionnement",
            "title": "Imposition à la source : qui est concerné",
            "meta": "Travailleurs étrangers sans permis C, personnes domiciliées à l'étranger avec revenu suisse : le fonctionnement de l'impôt à la source.",
            "sections": [
                {"heading": "Qui est soumis à l'imposition à la source", "paragraphs": [
                    "L'imposition à la source (art. 83 ss LIFD) s'applique principalement aux travailleurs étrangers domiciliés ou en séjour en Suisse qui ne sont pas titulaires d'une autorisation d'établissement (permis C), ainsi qu'à certaines personnes domiciliées à l'étranger qui perçoivent un revenu de source suisse, comme un salaire, une pension, ou certaines prestations.",
                ]},
                {"heading": "Le mécanisme du prélèvement", "paragraphs": [
                    "L'impôt à la source est retenu directement par l'employeur sur le salaire, selon des barèmes fixés en fonction du revenu, de la situation familiale et du canton concerné, puis reversé à l'autorité fiscale cantonale. Ce mécanisme remplace, pour les personnes concernées, la procédure de taxation ordinaire par déclaration d'impôt.",
                ]},
                {"heading": "La taxation ordinaire ultérieure", "paragraphs": [
                    "Certaines personnes imposées à la source peuvent demander, ou dans certains cas sont automatiquement soumises, à une taxation ordinaire ultérieure, notamment lorsque le revenu dépasse certains seuils ou pour faire valoir des déductions supplémentaires (frais professionnels effectifs, rachats de prévoyance) que le barème forfaitaire ne prend pas en compte.",
                ]},
                {"heading": "L'obtention du permis C et la fin de l'imposition à la source", "paragraphs": [
                    "L'obtention d'une autorisation d'établissement (permis C) ou d'un mariage avec une personne de nationalité suisse ou titulaire d'un permis C met en principe fin à l'imposition à la source, la personne passant alors au régime de taxation ordinaire par déclaration.",
                ]},
            ],
            "faq": [
                {"q": "Qui est soumis à l'imposition à la source en Suisse ?",
                 "a": "Principalement les travailleurs étrangers sans permis C domiciliés ou en séjour en Suisse, ainsi que certaines personnes domiciliées à l'étranger percevant un revenu de source suisse."},
                {"q": "Puis-je déduire mes frais professionnels effectifs si je suis imposé à la source ?",
                 "a": "Le barème forfaitaire intègre déjà certaines déductions standard ; pour faire valoir des frais effectifs supérieurs ou d'autres déductions spécifiques, il faut généralement demander une taxation ordinaire ultérieure dans les conditions prévues par la loi."},
                {"q": "Que se passe-t-il quand j'obtiens le permis C ?",
                 "a": "L'imposition à la source prend fin en principe, et vous passez au régime de taxation ordinaire par déclaration d'impôt comme les contribuables suisses."},
            ],
        },
        "de": {
            "slug": "quellensteuer-wer-betroffen-funktionsweise",
            "title": "Quellensteuer: wer betroffen ist und wie sie funktioniert",
            "meta": "Ausländische Arbeitnehmende ohne Niederlassungsbewilligung, im Ausland wohnhafte Personen mit Schweizer Einkommen: die Funktionsweise der Quellensteuer.",
            "sections": [
                {"heading": "Wer der Quellensteuer unterliegt", "paragraphs": [
                    "Die Quellensteuer (Art. 83 ff. DBG) betrifft hauptsächlich ausländische Arbeitnehmende mit Wohnsitz oder Aufenthalt in der Schweiz, die keine Niederlassungsbewilligung (Ausweis C) besitzen, sowie bestimmte im Ausland wohnhafte Personen, die Einkommen aus schweizerischer Quelle beziehen, wie einen Lohn, eine Rente, oder bestimmte Leistungen.",
                ]},
                {"heading": "Der Mechanismus des Steuerabzugs", "paragraphs": [
                    "Die Quellensteuer wird direkt vom Arbeitgeber vom Lohn abgezogen, gemäss Tarifen, die nach Einkommen, familiärer Situation und betroffenem Kanton festgelegt werden, und anschliessend an die kantonale Steuerbehörde überwiesen. Dieser Mechanismus ersetzt für die betroffenen Personen das ordentliche Veranlagungsverfahren durch Steuererklärung.",
                ]},
                {"heading": "Die nachträgliche ordentliche Veranlagung", "paragraphs": [
                    "Bestimmte quellenbesteuerte Personen können eine nachträgliche ordentliche Veranlagung beantragen, oder unterliegen dieser in bestimmten Fällen automatisch, namentlich wenn das Einkommen bestimmte Schwellen überschreitet oder um zusätzliche Abzüge geltend zu machen (tatsächliche Berufsauslagen, Vorsorgeeinkäufe), die der pauschale Tarif nicht berücksichtigt.",
                ]},
                {"heading": "Der Erhalt des Ausweises C und das Ende der Quellensteuer", "paragraphs": [
                    "Der Erhalt einer Niederlassungsbewilligung (Ausweis C) oder eine Heirat mit einer Person schweizerischer Staatsangehörigkeit oder mit Ausweis C beendet grundsätzlich die Quellenbesteuerung, wobei die Person dann in das ordentliche Veranlagungsverfahren durch Steuererklärung wechselt.",
                ]},
            ],
            "faq": [
                {"q": "Wer unterliegt in der Schweiz der Quellensteuer?",
                 "a": "Hauptsächlich ausländische Arbeitnehmende ohne Ausweis C mit Wohnsitz oder Aufenthalt in der Schweiz, sowie bestimmte im Ausland wohnhafte Personen mit Einkommen aus schweizerischer Quelle."},
                {"q": "Kann ich meine tatsächlichen Berufsauslagen abziehen, wenn ich quellenbesteuert bin?",
                 "a": "Der Pauschaltarif berücksichtigt bereits bestimmte Standardabzüge; um höhere tatsächliche Kosten oder andere spezifische Abzüge geltend zu machen, muss in der Regel eine nachträgliche ordentliche Veranlagung unter den gesetzlichen Voraussetzungen beantragt werden."},
                {"q": "Was geschieht, wenn ich den Ausweis C erhalte?",
                 "a": "Die Quellenbesteuerung endet grundsätzlich, und Sie wechseln in das ordentliche Veranlagungsverfahren durch Steuererklärung wie die schweizerischen Steuerpflichtigen."},
            ],
        },
        "it": {
            "slug": "imposta-alla-fonte-chi-interessato-funzionamento",
            "title": "Imposta alla fonte: chi è interessato e come funziona",
            "meta": "Lavoratori stranieri senza permesso C, persone domiciliate all'estero con reddito svizzero: il funzionamento dell'imposta alla fonte.",
            "sections": [
                {"heading": "Chi è soggetto all'imposta alla fonte", "paragraphs": [
                    "L'imposta alla fonte (art. 83 segg. LIFD) riguarda principalmente i lavoratori stranieri domiciliati o dimoranti in Svizzera che non sono titolari di un permesso di domicilio (permesso C), nonché determinate persone domiciliate all'estero che percepiscono un reddito di fonte svizzera, come un salario, una rendita, o determinate prestazioni.",
                ]},
                {"heading": "Il meccanismo del prelievo", "paragraphs": [
                    "L'imposta alla fonte viene trattenuta direttamente dal datore di lavoro sul salario, secondo tariffe fissate in funzione del reddito, della situazione familiare e del Cantone interessato, poi versata all'autorità fiscale cantonale. Questo meccanismo sostituisce, per le persone interessate, la procedura di tassazione ordinaria tramite dichiarazione d'imposta.",
                ]},
                {"heading": "La tassazione ordinaria ulteriore", "paragraphs": [
                    "Determinate persone tassate alla fonte possono chiedere, o in certi casi sono automaticamente sottoposte, a una tassazione ordinaria ulteriore, in particolare quando il reddito supera determinate soglie o per far valere deduzioni supplementari (spese professionali effettive, riscatti di previdenza) che la tariffa forfettaria non prende in considerazione.",
                ]},
                {"heading": "L'ottenimento del permesso C e la fine dell'imposta alla fonte", "paragraphs": [
                    "L'ottenimento di un permesso di domicilio (permesso C) o un matrimonio con una persona di nazionalità svizzera o titolare di un permesso C pone in linea di principio fine all'imposizione alla fonte, e la persona passa allora al regime di tassazione ordinaria tramite dichiarazione.",
                ]},
            ],
            "faq": [
                {"q": "Chi è soggetto all'imposta alla fonte in Svizzera?",
                 "a": "Principalmente i lavoratori stranieri senza permesso C domiciliati o dimoranti in Svizzera, nonché determinate persone domiciliate all'estero che percepiscono un reddito di fonte svizzera."},
                {"q": "Posso dedurre le mie spese professionali effettive se sono tassato alla fonte?",
                 "a": "La tariffa forfettaria integra già determinate deduzioni standard; per far valere spese effettive superiori o altre deduzioni specifiche, occorre generalmente chiedere una tassazione ordinaria ulteriore alle condizioni previste dalla legge."},
                {"q": "Cosa succede quando ottengo il permesso C?",
                 "a": "L'imposizione alla fonte cessa in linea di principio, e passate al regime di tassazione ordinaria tramite dichiarazione d'imposta come i contribuenti svizzeri."},
            ],
        },
        "en": {
            "slug": "withholding-tax-who-affected-how-it-works",
            "title": "Withholding tax: who is affected and how it works",
            "meta": "Foreign employees without a settlement permit, persons resident abroad with Swiss income: how withholding tax works.",
            "sections": [
                {"heading": "Who is subject to withholding tax", "paragraphs": [
                    "Withholding tax (art. 83 ff. DFTA) mainly applies to foreign employees domiciled or residing in Switzerland who do not hold a settlement permit (permit C), as well as certain persons resident abroad who receive income from a Swiss source, such as a salary, pension, or certain benefits.",
                ]},
                {"heading": "How the deduction works", "paragraphs": [
                    "Withholding tax is deducted directly by the employer from the salary, according to rates set based on income, family situation and the canton concerned, and then paid to the cantonal tax authority. This mechanism replaces, for the persons concerned, the ordinary assessment procedure by tax return.",
                ]},
                {"heading": "Subsequent ordinary assessment", "paragraphs": [
                    "Certain persons taxed at source can request, or in certain cases are automatically subject to, a subsequent ordinary assessment, in particular when income exceeds certain thresholds or to claim additional deductions (actual professional expenses, pension buy-ins) that the flat-rate tariff does not take into account.",
                ]},
                {"heading": "Obtaining permit C and the end of withholding tax", "paragraphs": [
                    "Obtaining a settlement permit (permit C) or marrying a Swiss national or a permit C holder in principle ends withholding taxation, and the person then moves to the ordinary assessment procedure by tax return.",
                ]},
            ],
            "faq": [
                {"q": "Who is subject to withholding tax in Switzerland?",
                 "a": "Mainly foreign employees without a permit C domiciled or residing in Switzerland, as well as certain persons resident abroad who receive income from a Swiss source."},
                {"q": "Can I deduct my actual professional expenses if I am taxed at source?",
                 "a": "The flat-rate tariff already includes certain standard deductions; to claim higher actual expenses or other specific deductions, a subsequent ordinary assessment generally needs to be requested under the conditions set by law."},
                {"q": "What happens when I obtain permit C?",
                 "a": "Withholding taxation in principle ends, and you move to the ordinary assessment procedure by tax return like Swiss taxpayers."},
            ],
        },
    },
    "secret-bancaire-suisse-protection": {
        "domaine_id": "droit_bancaire",
        "published": "2026-07-30",
        "fr": {
            "slug": "secret-bancaire-suisse-ce-quil-protege",
            "title": "Secret bancaire suisse : ce qu'il protège aujourd'hui",
            "meta": "Portée actuelle du secret bancaire après l'échange automatique de renseignements, sanctions pénales : ce que prévoit la loi sur les banques.",
            "sections": [
                {"heading": "Le fondement légal", "paragraphs": [
                    "Le secret bancaire suisse repose sur l'art. 47 de la loi sur les banques (LB), qui sanctionne pénalement la violation du secret professionnel par un employé, un organe ou un mandataire d'une banque. Il protège la confidentialité de la relation entre la banque et son client à l'égard des tiers privés et, sous réserve des exceptions légales, des autorités.",
                ]},
                {"heading": "Ce qui a changé avec l'échange automatique de renseignements", "paragraphs": [
                    "Depuis 2017, la Suisse applique l'échange automatique de renseignements en matière fiscale (EAR) avec un nombre croissant de pays partenaires : les données de comptes bancaires des résidents fiscaux de ces pays sont transmises automatiquement aux autorités fiscales étrangères concernées, ce qui limite fortement la portée pratique du secret bancaire pour les questions fiscales transfrontalières avec ces États.",
                ]},
                {"heading": "Ce que le secret bancaire protège encore", "paragraphs": [
                    "Le secret bancaire conserve toute sa portée à l'égard des tiers privés (curiosité d'un concurrent, d'un voisin, d'un membre de la famille non autorisé) et, pour les résidents suisses ou les résidents de pays non partenaires de l'EAR, il continue à limiter l'accès aux informations bancaires en dehors des procédures légales prévues (entraide judiciaire, procédure pénale, poursuite pour dettes).",
                ]},
                {"heading": "Les exceptions légales", "paragraphs": [
                    "Le secret bancaire peut être levé dans le cadre d'une procédure pénale suisse, d'une demande d'entraide judiciaire internationale conforme aux traités applicables, d'une procédure de poursuite ou de faillite, ou encore avec le consentement exprès du client concerné.",
                ]},
            ],
            "faq": [
                {"q": "Le secret bancaire suisse existe-t-il encore ?",
                 "a": "Oui, mais sa portée s'est réduite depuis l'introduction de l'échange automatique de renseignements fiscaux (EAR) en 2017 avec de nombreux pays partenaires. Il protège toujours la confidentialité vis-à-vis des tiers privés et dans les situations non couvertes par l'EAR."},
                {"q": "Une banque peut-elle transmettre mes données à l'étranger sans mon accord ?",
                 "a": "Dans le cadre de l'échange automatique de renseignements avec un pays partenaire, oui, cette transmission aux autorités fiscales de votre pays de résidence fiscale est automatique et ne dépend pas de votre consentement."},
                {"q": "Que risque un employé de banque qui viole le secret bancaire ?",
                 "a": "Des sanctions pénales prévues par l'art. 47 LB, qui peuvent inclure une peine privative de liberté ou une peine pécuniaire selon la gravité de la violation."},
            ],
        },
        "de": {
            "slug": "bankgeheimnis-schweiz-was-es-heute-schuetzt",
            "title": "Bankgeheimnis Schweiz: was es heute noch schützt",
            "meta": "Tragweite des Bankgeheimnisses nach dem automatischen Informationsaustausch, strafrechtliche Sanktionen: was das Bankengesetz vorsieht.",
            "sections": [
                {"heading": "Die gesetzliche Grundlage", "paragraphs": [
                    "Das schweizerische Bankgeheimnis stützt sich auf Art. 47 des Bankengesetzes (BankG), welcher die Verletzung der Berufsgeheimnispflicht durch eine Angestellte, einen Angestellten, ein Organ oder eine Beauftragte oder einen Beauftragten einer Bank strafrechtlich sanktioniert. Es schützt die Vertraulichkeit der Beziehung zwischen der Bank und ihrer Kundschaft gegenüber Dritten und, vorbehältlich gesetzlicher Ausnahmen, gegenüber Behörden.",
                ]},
                {"heading": "Was sich mit dem automatischen Informationsaustausch geändert hat", "paragraphs": [
                    "Seit 2017 wendet die Schweiz den automatischen Informationsaustausch in Steuersachen (AIA) mit einer wachsenden Zahl von Partnerstaaten an: die Kontodaten von in diesen Ländern steuerlich ansässigen Personen werden automatisch an die betroffenen ausländischen Steuerbehörden übermittelt, was die praktische Tragweite des Bankgeheimnisses für grenzüberschreitende Steuerfragen mit diesen Staaten erheblich einschränkt.",
                ]},
                {"heading": "Was das Bankgeheimnis noch schützt", "paragraphs": [
                    "Das Bankgeheimnis behält seine volle Tragweite gegenüber privaten Dritten (Neugier einer Konkurrentin oder eines Konkurrenten, einer Nachbarin oder eines Nachbarn, eines nicht befugten Familienmitglieds), und für in der Schweiz ansässige Personen oder Ansässige von Staaten, die nicht am AIA teilnehmen, beschränkt es weiterhin den Zugang zu Bankinformationen ausserhalb der gesetzlich vorgesehenen Verfahren (Rechtshilfe, Strafverfahren, Schuldbetreibung).",
                ]},
                {"heading": "Die gesetzlichen Ausnahmen", "paragraphs": [
                    "Das Bankgeheimnis kann im Rahmen eines schweizerischen Strafverfahrens, eines mit den anwendbaren Staatsverträgen konformen internationalen Rechtshilfegesuchs, eines Betreibungs- oder Konkursverfahrens, oder mit ausdrücklicher Zustimmung der betroffenen Kundin oder des betroffenen Kunden aufgehoben werden.",
                ]},
            ],
            "faq": [
                {"q": "Gibt es das Schweizer Bankgeheimnis noch?",
                 "a": "Ja, aber seine Tragweite hat sich seit der Einführung des automatischen Informationsaustauschs in Steuersachen (AIA) 2017 mit zahlreichen Partnerstaaten verringert. Es schützt die Vertraulichkeit gegenüber Privaten und in nicht vom AIA erfassten Situationen weiterhin."},
                {"q": "Kann eine Bank meine Daten ohne meine Zustimmung ins Ausland übermitteln?",
                 "a": "Im Rahmen des automatischen Informationsaustauschs mit einem Partnerstaat ja, diese Übermittlung an die Steuerbehörden Ihres steuerlichen Wohnsitzstaates erfolgt automatisch und hängt nicht von Ihrer Zustimmung ab."},
                {"q": "Was riskiert eine Bankangestellte oder ein Bankangestellter, die oder der das Bankgeheimnis verletzt?",
                 "a": "Strafrechtliche Sanktionen gemäss Art. 47 BankG, die je nach Schwere der Verletzung eine Freiheitsstrafe oder eine Geldstrafe umfassen können."},
            ],
        },
        "it": {
            "slug": "segreto-bancario-svizzero-cosa-protegge-oggi",
            "title": "Segreto bancario svizzero: cosa protegge oggi",
            "meta": "Portata attuale del segreto bancario dopo lo scambio automatico di informazioni, sanzioni penali: quanto previsto dalla legge sulle banche.",
            "sections": [
                {"heading": "Il fondamento legale", "paragraphs": [
                    "Il segreto bancario svizzero si fonda sull'art. 47 della legge sulle banche (LBCR), che sanziona penalmente la violazione del segreto professionale da parte di un dipendente, un organo o un mandatario di una banca. Protegge la confidenzialità della relazione tra la banca e il suo cliente nei confronti di terzi privati e, con riserva delle eccezioni legali, delle autorità.",
                ]},
                {"heading": "Cosa è cambiato con lo scambio automatico di informazioni", "paragraphs": [
                    "Dal 2017 la Svizzera applica lo scambio automatico di informazioni in materia fiscale (SAI) con un numero crescente di Paesi partner: i dati dei conti bancari dei residenti fiscali di questi Paesi vengono trasmessi automaticamente alle autorità fiscali estere interessate, il che limita fortemente la portata pratica del segreto bancario per le questioni fiscali transfrontaliere con tali Stati.",
                ]},
                {"heading": "Cosa protegge ancora il segreto bancario", "paragraphs": [
                    "Il segreto bancario conserva tutta la sua portata nei confronti dei terzi privati (curiosità di un concorrente, di un vicino, di un familiare non autorizzato) e, per i residenti svizzeri o i residenti di Paesi non partner del SAI, continua a limitare l'accesso alle informazioni bancarie al di fuori delle procedure legali previste (assistenza giudiziaria, procedura penale, esecuzione).",
                ]},
                {"heading": "Le eccezioni legali", "paragraphs": [
                    "Il segreto bancario può essere revocato nell'ambito di una procedura penale svizzera, di una domanda di assistenza giudiziaria internazionale conforme ai trattati applicabili, di una procedura di esecuzione o di fallimento, oppure con il consenso espresso del cliente interessato.",
                ]},
            ],
            "faq": [
                {"q": "Il segreto bancario svizzero esiste ancora?",
                 "a": "Sì, ma la sua portata si è ridotta dall'introduzione dello scambio automatico di informazioni fiscali (SAI) nel 2017 con numerosi Paesi partner. Protegge ancora la confidenzialità nei confronti dei terzi privati e nelle situazioni non coperte dal SAI."},
                {"q": "Una banca può trasmettere i miei dati all'estero senza il mio accordo?",
                 "a": "Nell'ambito dello scambio automatico di informazioni con un Paese partner, sì, questa trasmissione alle autorità fiscali del vostro Paese di residenza fiscale è automatica e non dipende dal vostro consenso."},
                {"q": "Cosa rischia un dipendente di banca che viola il segreto bancario?",
                 "a": "Sanzioni penali previste dall'art. 47 LBCR, che possono includere una pena detentiva o una pena pecuniaria secondo la gravità della violazione."},
            ],
        },
        "en": {
            "slug": "swiss-banking-secrecy-what-it-still-protects",
            "title": "Swiss banking secrecy: what it still protects today",
            "meta": "The current scope of banking secrecy after automatic information exchange, criminal sanctions: what the Banking Act provides.",
            "sections": [
                {"heading": "The legal basis", "paragraphs": [
                    "Swiss banking secrecy rests on art. 47 of the Banking Act, which imposes criminal sanctions for breach of professional confidentiality by a bank employee, officer, or agent. It protects the confidentiality of the relationship between a bank and its client from private third parties and, subject to legal exceptions, from authorities.",
                ]},
                {"heading": "What changed with automatic information exchange", "paragraphs": [
                    "Since 2017, Switzerland has applied automatic exchange of information (AEOI) in tax matters with a growing number of partner countries: bank account data of tax residents of these countries is automatically transmitted to the foreign tax authorities concerned, which greatly limits the practical scope of banking secrecy for cross-border tax matters with these states.",
                ]},
                {"heading": "What banking secrecy still protects", "paragraphs": [
                    "Banking secrecy retains its full scope with respect to private third parties (a competitor's curiosity, a neighbour's, an unauthorised family member's) and, for Swiss residents or residents of countries not party to AEOI, it continues to limit access to banking information outside the legal procedures provided (mutual legal assistance, criminal proceedings, debt enforcement).",
                ]},
                {"heading": "Legal exceptions", "paragraphs": [
                    "Banking secrecy can be lifted as part of Swiss criminal proceedings, an international mutual legal assistance request compliant with applicable treaties, debt enforcement or bankruptcy proceedings, or with the express consent of the client concerned.",
                ]},
            ],
            "faq": [
                {"q": "Does Swiss banking secrecy still exist?",
                 "a": "Yes, but its scope has narrowed since the introduction of automatic exchange of tax information (AEOI) in 2017 with numerous partner countries. It still protects confidentiality with respect to private parties and in situations not covered by AEOI."},
                {"q": "Can a bank transmit my data abroad without my consent?",
                 "a": "Under automatic information exchange with a partner country, yes, this transmission to the tax authorities of your country of tax residence is automatic and does not depend on your consent."},
                {"q": "What does a bank employee risk for breaching banking secrecy?",
                 "a": "Criminal sanctions under art. 47 of the Banking Act, which can include a custodial sentence or a monetary penalty depending on the severity of the breach."},
            ],
        },
    },
    "litige-banque-ombudsman-recours": {
        "domaine_id": "droit_bancaire",
        "published": "2026-07-30",
        "fr": {
            "slug": "litige-avec-sa-banque-ombudsman-voies-recours",
            "title": "Litige avec sa banque : ombudsman et recours",
            "meta": "Médiation gratuite via l'Ombudsman des banques suisses, saisine du tribunal civil : les voies pour résoudre un litige bancaire.",
            "sections": [
                {"heading": "L'Ombudsman des banques suisses", "paragraphs": [
                    "L'Ombudsman des banques suisses est un organisme de médiation neutre et indépendant, gratuit pour le client, qui traite les litiges entre un client et sa banque : frais contestés, exécution incorrecte d'un ordre, conseil en placement insatisfaisant, ou autres différends contractuels. Sa saisine ne nécessite pas d'avocat et constitue une étape rapide avant, ou en alternative à, une procédure judiciaire.",
                ]},
                {"heading": "La portée de la médiation", "paragraphs": [
                    "L'Ombudsman formule une recommandation, non contraignante pour les parties : la banque n'est pas obligée de la suivre, et le client conserve dans tous les cas le droit de saisir la justice s'il n'est pas satisfait de l'issue de la médiation. La médiation interrompt en principe le délai de prescription de la créance pendant sa durée.",
                ]},
                {"heading": "Les autres voies de recours", "paragraphs": [
                    "En parallèle ou après la médiation, le client peut déposer une plainte auprès de l'Autorité fédérale de surveillance des marchés financiers (FINMA), qui ne traite toutefois pas les litiges individuels mais peut intervenir en cas de manquements systémiques d'un établissement. La voie judiciaire ordinaire, devant le tribunal civil compétent, reste toujours ouverte pour trancher un litige de manière contraignante.",
                ]},
                {"heading": "Bien documenter le litige", "paragraphs": [
                    "Avant toute démarche, il est utile de rassembler l'ensemble de la correspondance avec la banque, les relevés de compte concernés, et une chronologie précise des faits : ces éléments facilitent grandement le traitement du dossier, que ce soit par l'Ombudsman ou par un tribunal.",
                ]},
            ],
            "faq": [
                {"q": "La saisine de l'Ombudsman des banques suisses coûte-t-elle quelque chose ?",
                 "a": "Non, elle est gratuite pour le client et ne nécessite pas l'assistance d'un avocat, ce qui en fait une première étape accessible avant d'envisager une procédure judiciaire."},
                {"q": "La banque est-elle obligée de suivre la recommandation de l'Ombudsman ?",
                 "a": "Non, la recommandation n'est pas contraignante. Si la banque ne la suit pas ou si le client n'est pas satisfait, la voie judiciaire ordinaire reste ouverte."},
                {"q": "La FINMA peut-elle m'aider à résoudre mon litige individuel avec ma banque ?",
                 "a": "Pas directement : la FINMA surveille le respect des règles prudentielles par les établissements mais ne tranche pas les litiges individuels entre un client et sa banque, contrairement à l'Ombudsman des banques suisses."},
            ],
        },
        "de": {
            "slug": "streit-mit-bank-ombudsman-rechtsmittel",
            "title": "Streit mit der Bank: Ombudsman und Rechtsmittel",
            "meta": "Kostenlose Schlichtung durch den Bankenombudsman, Anrufung des Zivilgerichts: die Wege zur Lösung eines Bankenstreits.",
            "sections": [
                {"heading": "Der Schweizerische Bankenombudsman", "paragraphs": [
                    "Der Schweizerische Bankenombudsman ist eine neutrale und unabhängige, für die Kundschaft kostenlose Schlichtungsstelle, die Streitigkeiten zwischen einer Kundin oder einem Kunden und ihrer oder seiner Bank behandelt: bestrittene Gebühren, fehlerhafte Auftragsausführung, unbefriedigende Anlageberatung, oder andere vertragliche Differenzen. Seine Anrufung erfordert keine Anwältin oder keinen Anwalt und stellt einen raschen Schritt vor oder anstelle eines Gerichtsverfahrens dar.",
                ]},
                {"heading": "Die Tragweite der Schlichtung", "paragraphs": [
                    "Der Ombudsman formuliert eine Empfehlung, die für die Parteien nicht bindend ist: die Bank ist nicht verpflichtet, ihr zu folgen, und die Kundin oder der Kunde behält in jedem Fall das Recht, bei Unzufriedenheit mit dem Ausgang der Schlichtung den Rechtsweg zu beschreiten. Die Schlichtung unterbricht grundsätzlich während ihrer Dauer die Verjährung der Forderung.",
                ]},
                {"heading": "Die weiteren Rechtsmittel", "paragraphs": [
                    "Parallel zur oder nach der Schlichtung kann die Kundin oder der Kunde eine Beschwerde bei der Eidgenössischen Finanzmarktaufsicht (FINMA) einreichen, welche jedoch keine individuellen Streitigkeiten behandelt, sondern bei systemischen Mängeln einer Bank eingreifen kann. Der ordentliche Rechtsweg vor dem zuständigen Zivilgericht bleibt stets offen, um eine Streitigkeit verbindlich zu entscheiden.",
                ]},
                {"heading": "Den Streit gut dokumentieren", "paragraphs": [
                    "Vor jedem Schritt ist es nützlich, den gesamten Schriftverkehr mit der Bank, die betroffenen Kontoauszüge und eine genaue Chronologie der Tatsachen zusammenzustellen: diese Elemente erleichtern die Bearbeitung des Dossiers erheblich, ob durch den Ombudsman oder durch ein Gericht.",
                ]},
            ],
            "faq": [
                {"q": "Kostet die Anrufung des Schweizerischen Bankenombudsman etwas?",
                 "a": "Nein, sie ist für die Kundschaft kostenlos und erfordert keine anwaltliche Vertretung, was sie zu einem zugänglichen ersten Schritt vor einem allfälligen Gerichtsverfahren macht."},
                {"q": "Ist die Bank verpflichtet, der Empfehlung des Ombudsman zu folgen?",
                 "a": "Nein, die Empfehlung ist nicht bindend. Folgt die Bank ihr nicht oder ist die Kundin oder der Kunde unzufrieden, bleibt der ordentliche Rechtsweg offen."},
                {"q": "Kann mir die FINMA bei der Lösung meines individuellen Streits mit meiner Bank helfen?",
                 "a": "Nicht direkt: die FINMA überwacht die Einhaltung der aufsichtsrechtlichen Regeln durch die Institute, entscheidet aber keine individuellen Streitigkeiten zwischen einer Kundin oder einem Kunden und ihrer oder seiner Bank, im Gegensatz zum Schweizerischen Bankenombudsman."},
            ],
        },
        "it": {
            "slug": "controversia-banca-ombudsman-vie-ricorso",
            "title": "Controversia con la banca: ombudsman e ricorsi",
            "meta": "Mediazione gratuita tramite l'Ombudsman delle banche svizzere, adire il tribunale civile: le vie per risolvere una controversia bancaria.",
            "sections": [
                {"heading": "L'Ombudsman delle banche svizzere", "paragraphs": [
                    "L'Ombudsman delle banche svizzere è un organismo di mediazione neutrale e indipendente, gratuito per il cliente, che tratta le controversie tra un cliente e la sua banca: spese contestate, esecuzione errata di un ordine, consulenza in investimenti insoddisfacente, o altre controversie contrattuali. La sua adizione non richiede un avvocato e costituisce una tappa rapida prima, o in alternativa a, una procedura giudiziaria.",
                ]},
                {"heading": "La portata della mediazione", "paragraphs": [
                    "L'Ombudsman formula una raccomandazione, non vincolante per le parti: la banca non è obbligata a seguirla, e il cliente conserva in ogni caso il diritto di adire la giustizia se non è soddisfatto dell'esito della mediazione. La mediazione interrompe in linea di principio il termine di prescrizione del credito durante la sua durata.",
                ]},
                {"heading": "Le altre vie di ricorso", "paragraphs": [
                    "Parallelamente o dopo la mediazione, il cliente può presentare un reclamo presso l'Autorità federale di vigilanza sui mercati finanziari (FINMA), che tuttavia non tratta le controversie individuali ma può intervenire in caso di carenze sistemiche di un istituto. La via giudiziaria ordinaria, davanti al tribunale civile competente, resta sempre aperta per decidere in modo vincolante una controversia.",
                ]},
                {"heading": "Documentare bene la controversia", "paragraphs": [
                    "Prima di qualsiasi passo, è utile raccogliere l'insieme della corrispondenza con la banca, gli estratti conto interessati, e una cronologia precisa dei fatti: questi elementi facilitano notevolmente il trattamento dell'incarto, sia da parte dell'Ombudsman che di un tribunale.",
                ]},
            ],
            "faq": [
                {"q": "Adire l'Ombudsman delle banche svizzere costa qualcosa?",
                 "a": "No, è gratuito per il cliente e non richiede l'assistenza di un avvocato, il che ne fa una prima tappa accessibile prima di considerare una procedura giudiziaria."},
                {"q": "La banca è obbligata a seguire la raccomandazione dell'Ombudsman?",
                 "a": "No, la raccomandazione non è vincolante. Se la banca non la segue o se il cliente non è soddisfatto, la via giudiziaria ordinaria resta aperta."},
                {"q": "La FINMA può aiutarmi a risolvere la mia controversia individuale con la mia banca?",
                 "a": "Non direttamente: la FINMA vigila sul rispetto delle regole prudenziali da parte degli istituti ma non decide le controversie individuali tra un cliente e la sua banca, a differenza dell'Ombudsman delle banche svizzere."},
            ],
        },
        "en": {
            "slug": "dispute-with-bank-ombudsman-legal-remedies",
            "title": "Dispute with your bank: ombudsman and legal remedies",
            "meta": "Free mediation through the Swiss Banking Ombudsman, going to civil court: the ways to resolve a dispute with your bank.",
            "sections": [
                {"heading": "The Swiss Banking Ombudsman", "paragraphs": [
                    "The Swiss Banking Ombudsman is a neutral, independent mediation body, free of charge for the client, which handles disputes between a client and their bank: disputed fees, incorrect execution of an order, unsatisfactory investment advice, or other contractual disagreements. Approaching it does not require a lawyer and provides a quick step before, or as an alternative to, court proceedings.",
                ]},
                {"heading": "The scope of the mediation", "paragraphs": [
                    "The Ombudsman issues a recommendation, which is not binding on the parties: the bank is not obliged to follow it, and the client in any case retains the right to go to court if they are not satisfied with the outcome of the mediation. Mediation in principle suspends the limitation period for the claim while it is ongoing.",
                ]},
                {"heading": "Other legal remedies", "paragraphs": [
                    "In parallel with or after mediation, the client can file a complaint with the Swiss Financial Market Supervisory Authority (FINMA), which, however, does not handle individual disputes but can intervene in the event of systemic shortcomings at an institution. Ordinary court proceedings, before the competent civil court, always remain available to resolve a dispute in a binding way.",
                ]},
                {"heading": "Documenting the dispute well", "paragraphs": [
                    "Before taking any steps, it is useful to gather all correspondence with the bank, the relevant account statements, and a precise timeline of events: these elements greatly facilitate handling the case, whether by the Ombudsman or by a court.",
                ]},
            ],
            "faq": [
                {"q": "Does approaching the Swiss Banking Ombudsman cost anything?",
                 "a": "No, it is free for the client and does not require the assistance of a lawyer, making it an accessible first step before considering court proceedings."},
                {"q": "Is the bank obliged to follow the Ombudsman's recommendation?",
                 "a": "No, the recommendation is not binding. If the bank does not follow it, or if the client is not satisfied, ordinary court proceedings remain available."},
                {"q": "Can FINMA help me resolve my individual dispute with my bank?",
                 "a": "Not directly: FINMA supervises institutions' compliance with prudential rules but does not rule on individual disputes between a client and their bank, unlike the Swiss Banking Ombudsman."},
            ],
        },
    },
    "erreur-medicale-faire-valoir-droits": {
        "domaine_id": "droit_medical",
        "published": "2026-07-30",
        "fr": {
            "slug": "erreur-medicale-comment-faire-valoir-ses-droits",
            "title": "Erreur médicale : comment faire valoir ses droits",
            "meta": "Responsabilité du médecin privé ou de l'hôpital public, preuve de la faute et du dommage : les bases légales en cas d'erreur médicale.",
            "sections": [
                {"heading": "Deux régimes de responsabilité selon le statut du soignant", "paragraphs": [
                    "La base légale applicable dépend du cadre dans lequel les soins ont été prodigués : un médecin exerçant en pratique privée est lié à son patient par un contrat de mandat (art. 394 ss CO), et sa responsabilité relève des règles générales de la responsabilité contractuelle et de l'art. 41 CO. Un traitement dans un hôpital public relève en revanche généralement du droit cantonal de la responsabilité de l'État, dont les règles et délais diffèrent sensiblement du droit privé.",
                ]},
                {"heading": "Ce qu'il faut prouver", "paragraphs": [
                    "Faire valoir une erreur médicale suppose de démontrer une violation des règles de l'art médical (une faute dans le diagnostic, le traitement, ou l'information du patient), un dommage effectif, et un lien de causalité entre cette violation et le dommage subi. La simple survenance d'une complication connue et statistiquement possible d'un traitement correctement exécuté ne constitue pas en soi une erreur médicale.",
                ]},
                {"heading": "Le rôle central de l'expertise médicale", "paragraphs": [
                    "Ces litiges reposent presque toujours sur une expertise médicale indépendante, destinée à déterminer si les soins prodigués respectaient les règles de l'art en vigueur au moment des faits. Le patient peut demander une expertise judiciaire ou solliciter, selon le canton, l'intervention d'un organe cantonal de conciliation en matière médicale avant toute procédure judiciaire.",
                ]},
                {"heading": "Les délais à respecter", "paragraphs": [
                    "Les délais de prescription et les procédures préalables (réclamation, conciliation) varient sensiblement selon que le litige relève du droit privé ou du droit cantonal de la responsabilité de l'État applicable à un établissement public : il est essentiel de vérifier rapidement le régime applicable à sa situation pour ne pas manquer un délai.",
                ]},
            ],
            "faq": [
                {"q": "Les règles sont-elles les mêmes pour un médecin privé et un hôpital public ?",
                 "a": "Non, un médecin privé relève des règles du contrat de mandat et de la responsabilité contractuelle du CO, tandis qu'un hôpital public relève généralement du droit cantonal de la responsabilité de l'État, avec des règles et délais propres à chaque canton."},
                {"q": "Une complication connue d'un traitement est-elle automatiquement une erreur médicale ?",
                 "a": "Non, la survenance d'une complication statistiquement possible d'un traitement correctement exécuté selon les règles de l'art ne constitue pas en soi une erreur médicale engageant la responsabilité du soignant."},
                {"q": "Comment prouve-t-on une erreur médicale ?",
                 "a": "Le plus souvent par une expertise médicale indépendante, destinée à déterminer si les soins prodigués respectaient les règles de l'art en vigueur au moment des faits, complétée par le dossier médical et les témoignages pertinents."},
            ],
        },
        "de": {
            "slug": "arztfehler-rechte-geltend-machen",
            "title": "Arztfehler: wie Sie Ihre Rechte geltend machen",
            "meta": "Haftung der privaten Ärzteschaft oder des öffentlichen Spitals, Nachweis von Fehler und Schaden: die gesetzlichen Grundlagen bei einem Arztfehler.",
            "sections": [
                {"heading": "Zwei Haftungsregimes je nach Status der behandelnden Person", "paragraphs": [
                    "Die anwendbare gesetzliche Grundlage hängt vom Rahmen ab, in dem die Behandlung erfolgte: eine in privater Praxis tätige Ärztin oder ein privater Arzt ist mit der Patientin oder dem Patienten durch einen Auftrag verbunden (Art. 394 ff. OR), und ihre oder seine Haftung richtet sich nach den allgemeinen Regeln der vertraglichen Haftung und Art. 41 OR. Eine Behandlung in einem öffentlichen Spital unterliegt hingegen grundsätzlich dem kantonalen Staatshaftungsrecht, dessen Regeln und Fristen erheblich vom Privatrecht abweichen.",
                ]},
                {"heading": "Was nachzuweisen ist", "paragraphs": [
                    "Um einen Arztfehler geltend zu machen, müssen eine Verletzung der Regeln der ärztlichen Kunst (ein Fehler in Diagnose, Behandlung oder Aufklärung der Patientin oder des Patienten), ein tatsächlicher Schaden sowie ein Kausalzusammenhang zwischen dieser Verletzung und dem erlittenen Schaden nachgewiesen werden. Das blosse Eintreten einer bekannten und statistisch möglichen Komplikation einer korrekt durchgeführten Behandlung stellt für sich allein keinen Arztfehler dar.",
                ]},
                {"heading": "Die zentrale Rolle des medizinischen Gutachtens", "paragraphs": [
                    "Diese Streitigkeiten stützen sich fast immer auf ein unabhängiges medizinisches Gutachten, das beurteilen soll, ob die erbrachte Behandlung den zum Zeitpunkt der Ereignisse geltenden Regeln der ärztlichen Kunst entsprach. Die Patientin oder der Patient kann ein gerichtliches Gutachten beantragen oder sich, je nach Kanton, an ein kantonales Schlichtungsorgan in medizinischen Angelegenheiten wenden, bevor ein Gerichtsverfahren eingeleitet wird.",
                ]},
                {"heading": "Die einzuhaltenden Fristen", "paragraphs": [
                    "Die Verjährungsfristen und vorgängigen Verfahren (Reklamation, Schlichtung) variieren erheblich, je nachdem ob der Streit dem Privatrecht oder dem für ein öffentliches Spital anwendbaren kantonalen Staatshaftungsrecht untersteht: es ist unerlässlich, das auf die eigene Situation anwendbare Regime rasch zu prüfen, um keine Frist zu verpassen.",
                ]},
            ],
            "faq": [
                {"q": "Gelten für eine private Ärztin oder einen privaten Arzt und ein öffentliches Spital dieselben Regeln?",
                 "a": "Nein, eine private Ärztin oder ein privater Arzt untersteht den Regeln des Auftrags und der vertraglichen Haftung des OR, während ein öffentliches Spital grundsätzlich dem kantonalen Staatshaftungsrecht untersteht, mit Regeln und Fristen, die je nach Kanton eigen sind."},
                {"q": "Ist eine bekannte Komplikation einer Behandlung automatisch ein Arztfehler?",
                 "a": "Nein, das Eintreten einer statistisch möglichen Komplikation einer gemäss den Regeln der ärztlichen Kunst korrekt durchgeführten Behandlung stellt für sich allein keinen Arztfehler dar, der die Haftung der behandelnden Person begründet."},
                {"q": "Wie beweist man einen Arztfehler?",
                 "a": "Meist durch ein unabhängiges medizinisches Gutachten, das beurteilen soll, ob die erbrachte Behandlung den zum Zeitpunkt der Ereignisse geltenden Regeln der ärztlichen Kunst entsprach, ergänzt durch die Krankenakte und relevante Zeugenaussagen."},
            ],
        },
        "it": {
            "slug": "errore-medico-far-valere-diritti",
            "title": "Errore medico: come far valere i propri diritti",
            "meta": "Responsabilità del medico privato o dell'ospedale pubblico, prova della colpa e del danno: le basi legali in caso di errore medico.",
            "sections": [
                {"heading": "Due regimi di responsabilità secondo lo statuto del curante", "paragraphs": [
                    "La base legale applicabile dipende dal contesto in cui sono state prestate le cure: un medico che esercita in libera professione è legato al paziente da un contratto di mandato (art. 394 segg. CO), e la sua responsabilità rientra nelle regole generali della responsabilità contrattuale e dell'art. 41 CO. Un trattamento in un ospedale pubblico rientra invece generalmente nel diritto cantonale della responsabilità dello Stato, le cui regole e termini differiscono sensibilmente dal diritto privato.",
                ]},
                {"heading": "Cosa occorre provare", "paragraphs": [
                    "Far valere un errore medico presuppone di dimostrare una violazione delle regole dell'arte medica (un errore nella diagnosi, nel trattamento, o nell'informazione del paziente), un danno effettivo, e un nesso di causalità tra questa violazione e il danno subito. Il semplice sopraggiungere di una complicazione nota e statisticamente possibile di un trattamento correttamente eseguito non costituisce di per sé un errore medico.",
                ]},
                {"heading": "Il ruolo centrale della perizia medica", "paragraphs": [
                    "Queste controversie si fondano quasi sempre su una perizia medica indipendente, destinata a determinare se le cure prestate rispettavano le regole dell'arte in vigore al momento dei fatti. Il paziente può chiedere una perizia giudiziaria o rivolgersi, a seconda del Cantone, a un organo cantonale di conciliazione in materia medica prima di qualsiasi procedura giudiziaria.",
                ]},
                {"heading": "I termini da rispettare", "paragraphs": [
                    "I termini di prescrizione e le procedure preliminari (reclamo, conciliazione) variano sensibilmente a seconda che la controversia rientri nel diritto privato o nel diritto cantonale della responsabilità dello Stato applicabile a un istituto pubblico: è essenziale verificare rapidamente il regime applicabile alla propria situazione per non perdere un termine.",
                ]},
            ],
            "faq": [
                {"q": "Le regole sono le stesse per un medico privato e un ospedale pubblico?",
                 "a": "No, un medico privato rientra nelle regole del contratto di mandato e della responsabilità contrattuale del CO, mentre un ospedale pubblico rientra generalmente nel diritto cantonale della responsabilità dello Stato, con regole e termini propri a ciascun Cantone."},
                {"q": "Una complicazione nota di un trattamento è automaticamente un errore medico?",
                 "a": "No, il sopraggiungere di una complicazione statisticamente possibile di un trattamento correttamente eseguito secondo le regole dell'arte non costituisce di per sé un errore medico che impegna la responsabilità del curante."},
                {"q": "Come si prova un errore medico?",
                 "a": "Il più delle volte mediante una perizia medica indipendente, destinata a determinare se le cure prestate rispettavano le regole dell'arte in vigore al momento dei fatti, integrata dalla cartella medica e dalle testimonianze pertinenti."},
            ],
        },
        "en": {
            "slug": "medical-error-asserting-your-rights",
            "title": "Medical error: how to assert your rights",
            "meta": "Liability of a private doctor or a public hospital, proving fault and damage: the legal basis in the event of a medical error.",
            "sections": [
                {"heading": "Two liability regimes depending on the caregiver's status", "paragraphs": [
                    "The applicable legal basis depends on the setting in which care was provided: a doctor in private practice is bound to their patient by an agency contract (art. 394 ff. CO), and their liability falls under the general rules of contractual liability and art. 41 CO. Treatment at a public hospital, on the other hand, generally falls under cantonal state liability law, whose rules and deadlines differ significantly from private law.",
                ]},
                {"heading": "What needs to be proven", "paragraphs": [
                    "Asserting a medical error requires demonstrating a breach of the rules of medical practice (an error in diagnosis, treatment, or patient information), actual damage, and a causal link between that breach and the damage suffered. The mere occurrence of a known, statistically possible complication of a correctly performed treatment does not in itself constitute a medical error.",
                ]},
                {"heading": "The central role of medical expert opinion", "paragraphs": [
                    "These disputes almost always rely on an independent medical expert opinion, intended to determine whether the care provided complied with the rules of medical practice in force at the time. The patient can request a court-ordered expert opinion or, depending on the canton, approach a cantonal conciliation body for medical matters before any court proceedings.",
                ]},
                {"heading": "Deadlines to observe", "paragraphs": [
                    "Limitation periods and preliminary procedures (complaint, conciliation) vary significantly depending on whether the dispute falls under private law or the cantonal state liability law applicable to a public institution: it is essential to quickly check which regime applies to your situation so as not to miss a deadline.",
                ]},
            ],
            "faq": [
                {"q": "Are the rules the same for a private doctor and a public hospital?",
                 "a": "No, a private doctor falls under the rules of agency and contractual liability under the CO, while a public hospital generally falls under cantonal state liability law, with rules and deadlines specific to each canton."},
                {"q": "Is a known complication of a treatment automatically a medical error?",
                 "a": "No, the occurrence of a statistically possible complication of a treatment correctly performed according to the rules of medical practice does not in itself constitute a medical error engaging the caregiver's liability."},
                {"q": "How is a medical error proven?",
                 "a": "Most often through an independent medical expert opinion, intended to determine whether the care provided complied with the rules of medical practice in force at the time, supplemented by the medical record and relevant witness testimony."},
            ],
        },
    },
    "consentement-eclaire-patient-droits": {
        "domaine_id": "droit_medical",
        "published": "2026-07-30",
        "fr": {
            "slug": "consentement-eclaire-patient-droits-obligations",
            "title": "Consentement éclairé du patient : droits et devoirs",
            "meta": "Obligation d'information du médecin, conséquences d'un consentement insuffisamment éclairé : les règles issues de la protection de la personnalité.",
            "sections": [
                {"heading": "Le fondement du consentement éclairé", "paragraphs": [
                    "Toute atteinte à l'intégrité corporelle d'un patient, y compris un traitement médical nécessaire et correctement exécuté, constitue en principe une atteinte à la personnalité au sens de l'art. 28 CC, qui n'est licite que si le patient y a valablement consenti après avoir reçu une information suffisante, ou si un cas d'urgence le justifie exceptionnellement.",
                ]},
                {"heading": "L'étendue du devoir d'information du médecin", "paragraphs": [
                    "Le médecin doit informer le patient sur le diagnostic, la nature et le but du traitement proposé, ses risques significatifs, ainsi que les alternatives thérapeutiques raisonnables, dans une mesure suffisante pour permettre au patient de prendre une décision libre et éclairée. L'étendue exacte de cette information dépend de la gravité de l'intervention et de son caractère plus ou moins nécessaire.",
                ]},
                {"heading": "Les conséquences d'un consentement insuffisamment éclairé", "paragraphs": [
                    "Si un patient n'a pas reçu une information suffisante avant une intervention, celle-ci peut être considérée comme illicite même si elle a été exécutée sans faute technique, ce qui peut engager la responsabilité du soignant pour l'atteinte à la personnalité qui en résulte, indépendamment de toute erreur dans l'exécution technique du traitement.",
                ]},
                {"heading": "Le droit cantonal de la santé", "paragraphs": [
                    "Chaque canton dispose en outre de sa propre loi sur la santé, qui précise souvent les droits du patient (accès au dossier médical, droit de refuser un traitement, droit à une seconde opinion) de manière complémentaire aux principes généraux du Code civil applicables sur tout le territoire suisse.",
                ]},
            ],
            "faq": [
                {"q": "Un médecin peut-il traiter un patient sans son consentement ?",
                 "a": "En principe non, sauf cas d'urgence où le patient ne peut pas exprimer sa volonté et où l'intervention est nécessaire pour préserver sa vie ou sa santé, ou en présence de directives anticipées ou d'un représentant thérapeutique désigné."},
                {"q": "Que se passe-t-il si je n'ai pas été suffisamment informé avant une opération ?",
                 "a": "L'intervention peut être considérée comme illicite au regard de la protection de la personnalité, même sans faute technique, ce qui peut engager la responsabilité du soignant pour cette atteinte spécifique."},
                {"q": "Les règles sur le consentement sont-elles identiques dans tous les cantons ?",
                 "a": "Les principes généraux découlent du Code civil et s'appliquent partout en Suisse, mais chaque canton précise certains droits du patient dans sa propre loi cantonale sur la santé, qui peut varier d'un canton à l'autre."},
            ],
        },
        "de": {
            "slug": "informierte-einwilligung-patient-rechte-pflichten",
            "title": "Informierte Einwilligung: Rechte und Pflichten",
            "meta": "Aufklärungspflicht der Ärzteschaft, Folgen einer unzureichend aufgeklärten Einwilligung: die Regeln aus dem Persönlichkeitsschutz.",
            "sections": [
                {"heading": "Die Grundlage der informierten Einwilligung", "paragraphs": [
                    "Jeder Eingriff in die körperliche Integrität einer Patientin oder eines Patienten, einschliesslich einer notwendigen und korrekt durchgeführten medizinischen Behandlung, stellt grundsätzlich eine Persönlichkeitsverletzung im Sinne von Art. 28 ZGB dar, die nur rechtmässig ist, wenn die Patientin oder der Patient nach ausreichender Aufklärung gültig eingewilligt hat, oder wenn ein Notfall dies ausnahmsweise rechtfertigt.",
                ]},
                {"heading": "Der Umfang der ärztlichen Aufklärungspflicht", "paragraphs": [
                    "Die Ärztin oder der Arzt muss die Patientin oder den Patienten über die Diagnose, Art und Zweck der vorgeschlagenen Behandlung, ihre wesentlichen Risiken sowie vernünftige therapeutische Alternativen aufklären, in einem Ausmass, das der Patientin oder dem Patienten eine freie und informierte Entscheidung ermöglicht. Der genaue Umfang dieser Aufklärung hängt von der Schwere des Eingriffs und seiner mehr oder weniger zwingenden Notwendigkeit ab.",
                ]},
                {"heading": "Die Folgen einer unzureichend aufgeklärten Einwilligung", "paragraphs": [
                    "Hat eine Patientin oder ein Patient vor einem Eingriff keine ausreichende Aufklärung erhalten, kann dieser als widerrechtlich gelten, selbst wenn er technisch fehlerfrei durchgeführt wurde, was die Haftung der behandelnden Person für die daraus resultierende Persönlichkeitsverletzung begründen kann, unabhängig von einem allfälligen technischen Ausführungsfehler.",
                ]},
                {"heading": "Das kantonale Gesundheitsrecht", "paragraphs": [
                    "Jeder Kanton verfügt zudem über sein eigenes Gesundheitsgesetz, das oft die Patientenrechte (Zugang zur Krankenakte, Recht auf Ablehnung einer Behandlung, Recht auf eine Zweitmeinung) ergänzend zu den auf dem gesamten Schweizer Gebiet geltenden allgemeinen Grundsätzen des Zivilgesetzbuchs präzisiert.",
                ]},
            ],
            "faq": [
                {"q": "Darf eine Ärztin oder ein Arzt eine Patientin oder einen Patienten ohne deren Einwilligung behandeln?",
                 "a": "Grundsätzlich nicht, ausser in einem Notfall, in dem die Patientin oder der Patient ihren oder seinen Willen nicht äussern kann und der Eingriff zur Erhaltung von Leben oder Gesundheit notwendig ist, oder bei Vorliegen von Patientenverfügungen oder einer bezeichneten therapeutischen Vertretungsperson."},
                {"q": "Was geschieht, wenn ich vor einer Operation nicht ausreichend aufgeklärt wurde?",
                 "a": "Der Eingriff kann trotz technischer Fehlerfreiheit als widerrechtlich im Hinblick auf den Persönlichkeitsschutz gelten, was die Haftung der behandelnden Person für diese besondere Verletzung begründen kann."},
                {"q": "Sind die Regeln zur Einwilligung in allen Kantonen identisch?",
                 "a": "Die allgemeinen Grundsätze ergeben sich aus dem Zivilgesetzbuch und gelten in der ganzen Schweiz, doch jeder Kanton präzisiert bestimmte Patientenrechte in seinem eigenen kantonalen Gesundheitsgesetz, das von Kanton zu Kanton variieren kann."},
            ],
        },
        "it": {
            "slug": "consenso-informato-paziente-diritti-obblighi",
            "title": "Consenso informato del paziente: diritti e obblighi",
            "meta": "Obbligo d'informazione del medico, conseguenze di un consenso insufficientemente informato: le regole derivanti dalla protezione della personalità.",
            "sections": [
                {"heading": "Il fondamento del consenso informato", "paragraphs": [
                    "Qualsiasi lesione all'integrità corporale di un paziente, compreso un trattamento medico necessario e correttamente eseguito, costituisce in linea di principio una lesione della personalità ai sensi dell'art. 28 CC, lecita solo se il paziente vi ha validamente acconsentito dopo aver ricevuto un'informazione sufficiente, o se un caso di urgenza lo giustifica eccezionalmente.",
                ]},
                {"heading": "L'estensione dell'obbligo d'informazione del medico", "paragraphs": [
                    "Il medico deve informare il paziente sulla diagnosi, la natura e lo scopo del trattamento proposto, i suoi rischi significativi, nonché le alternative terapeutiche ragionevoli, in misura sufficiente a permettere al paziente di prendere una decisione libera e informata. L'estensione esatta di questa informazione dipende dalla gravità dell'intervento e dal suo carattere più o meno necessario.",
                ]},
                {"heading": "Le conseguenze di un consenso insufficientemente informato", "paragraphs": [
                    "Se un paziente non ha ricevuto un'informazione sufficiente prima di un intervento, questo può essere considerato illecito anche se eseguito senza errore tecnico, il che può impegnare la responsabilità del curante per la lesione della personalità che ne risulta, indipendentemente da qualsiasi errore nell'esecuzione tecnica del trattamento.",
                ]},
                {"heading": "Il diritto cantonale della sanità", "paragraphs": [
                    "Ogni Cantone dispone inoltre di una propria legge sulla sanità, che spesso precisa i diritti del paziente (accesso alla cartella medica, diritto di rifiutare un trattamento, diritto a un secondo parere) in modo complementare ai principi generali del Codice civile applicabili su tutto il territorio svizzero.",
                ]},
            ],
            "faq": [
                {"q": "Un medico può curare un paziente senza il suo consenso?",
                 "a": "In linea di principio no, salvo in caso di urgenza in cui il paziente non può esprimere la propria volontà e l'intervento è necessario per preservare la sua vita o la sua salute, o in presenza di direttive anticipate o di un rappresentante terapeutico designato."},
                {"q": "Cosa succede se non sono stato sufficientemente informato prima di un'operazione?",
                 "a": "L'intervento può essere considerato illecito rispetto alla protezione della personalità, anche senza errore tecnico, il che può impegnare la responsabilità del curante per questa specifica lesione."},
                {"q": "Le regole sul consenso sono identiche in tutti i Cantoni?",
                 "a": "I principi generali derivano dal Codice civile e si applicano in tutta la Svizzera, ma ogni Cantone precisa determinati diritti del paziente nella propria legge cantonale sulla sanità, che può variare da un Cantone all'altro."},
            ],
        },
        "en": {
            "slug": "informed-consent-patient-rights-obligations",
            "title": "Informed consent: patient rights and duties",
            "meta": "The doctor's duty to inform, consequences of insufficiently informed consent: the rules derived from the protection of personality.",
            "sections": [
                {"heading": "The basis of informed consent", "paragraphs": [
                    "Any interference with a patient's physical integrity, including necessary and correctly performed medical treatment, in principle constitutes a violation of personality rights under art. 28 CC, which is only lawful if the patient has validly consented after receiving sufficient information, or if an emergency exceptionally justifies it.",
                ]},
                {"heading": "The scope of the doctor's duty to inform", "paragraphs": [
                    "The doctor must inform the patient about the diagnosis, the nature and purpose of the proposed treatment, its significant risks, and reasonable therapeutic alternatives, to an extent sufficient to allow the patient to make a free and informed decision. The exact scope of this information depends on the severity of the procedure and how necessary it is.",
                ]},
                {"heading": "The consequences of insufficiently informed consent", "paragraphs": [
                    "If a patient did not receive sufficient information before a procedure, it can be considered unlawful even if performed without technical error, which can engage the caregiver's liability for the resulting violation of personality rights, regardless of any error in the technical execution of the treatment.",
                ]},
                {"heading": "Cantonal health law", "paragraphs": [
                    "Each canton also has its own health law, which often specifies patient rights (access to the medical record, right to refuse treatment, right to a second opinion) in addition to the general principles of the Civil Code applicable throughout Swiss territory.",
                ]},
            ],
            "faq": [
                {"q": "Can a doctor treat a patient without their consent?",
                 "a": "In principle no, except in an emergency where the patient cannot express their wishes and the procedure is necessary to preserve their life or health, or in the presence of advance directives or a designated therapeutic representative."},
                {"q": "What happens if I was not sufficiently informed before an operation?",
                 "a": "The procedure can be considered unlawful with respect to the protection of personality, even without technical error, which can engage the caregiver's liability for this specific violation."},
                {"q": "Are the rules on consent the same in every canton?",
                 "a": "The general principles derive from the Civil Code and apply throughout Switzerland, but each canton specifies certain patient rights in its own cantonal health law, which can vary from canton to canton."},
            ],
        },
    },
    "proteger-marque-suisse-depot-ipi": {
        "domaine_id": "propriete_intellectuelle",
        "published": "2026-07-30",
        "fr": {
            "slug": "proteger-marque-suisse-depot-ipi",
            "title": "Protéger une marque en Suisse : le dépôt à l'IPI",
            "meta": "Procédure de dépôt auprès de l'Institut fédéral de la propriété intellectuelle, durée de protection, opposition : ce que prévoit la LPM.",
            "sections": [
                {"heading": "Le dépôt auprès de l'IPI", "paragraphs": [
                    "La protection d'une marque en Suisse s'obtient par son enregistrement auprès de l'Institut fédéral de la propriété intellectuelle (IPI), conformément à la loi sur la protection des marques (LPM). La demande doit préciser le signe à protéger et la liste des produits ou services concernés, classés selon la classification internationale de Nice.",
                ]},
                {"heading": "L'examen effectué par l'IPI", "paragraphs": [
                    "L'IPI examine si la marque remplit les conditions formelles et absolues de protection (distinctivité suffisante, absence de caractère trompeur ou contraire à l'ordre public), mais ne vérifie en principe pas d'office l'existence de marques antérieures similaires ou identiques : cette vérification incombe au déposant lui-même, généralement au moyen d'une recherche d'antériorité préalable.",
                ]},
                {"heading": "La procédure d'opposition", "paragraphs": [
                    "Une fois la marque enregistrée et publiée, le titulaire d'une marque antérieure peut former opposition dans un délai de trois mois à compter de la publication, en faisant valoir un risque de confusion entre les deux signes pour des produits ou services identiques ou similaires.",
                ]},
                {"heading": "La durée de protection", "paragraphs": [
                    "La protection d'une marque suisse dure dix ans à compter du dépôt, et peut être renouvelée indéfiniment par périodes de dix ans moyennant le paiement des taxes de renouvellement, à condition que la marque continue d'être utilisée pour éviter le risque d'une radiation pour non-usage après un délai de carence de cinq ans.",
                ]},
            ],
            "faq": [
                {"q": "L'IPI vérifie-t-il si ma marque entre en conflit avec une marque déjà déposée ?",
                 "a": "Non, l'IPI n'effectue en principe pas d'examen d'office des marques antérieures : c'est au déposant de vérifier lui-même l'absence de conflit, généralement par une recherche d'antériorité préalable au dépôt."},
                {"q": "Combien de temps dure la protection d'une marque suisse ?",
                 "a": "Dix ans à compter du dépôt, renouvelable indéfiniment par périodes de dix ans moyennant le paiement des taxes de renouvellement."},
                {"q": "Que se passe-t-il si je n'utilise pas ma marque ?",
                 "a": "Une marque non utilisée pendant une période ininterrompue de cinq ans après l'échéance du délai de carence risque d'être radiée à la demande d'un tiers intéressé, sauf juste motif de non-usage."},
            ],
        },
        "de": {
            "slug": "marke-schweiz-schuetzen-anmeldung-ige",
            "title": "Eine Marke in der Schweiz schützen: Anmeldung beim IGE",
            "meta": "Anmeldeverfahren beim Eidgenössischen Institut für Geistiges Eigentum, Schutzdauer, Widerspruch: was das Markenschutzgesetz vorsieht.",
            "sections": [
                {"heading": "Die Anmeldung beim IGE", "paragraphs": [
                    "Der Markenschutz in der Schweiz wird durch die Eintragung beim Eidgenössischen Institut für Geistiges Eigentum (IGE) erlangt, gemäss dem Markenschutzgesetz (MSchG). Das Gesuch muss das zu schützende Zeichen sowie das Verzeichnis der betroffenen Waren oder Dienstleistungen, klassiert gemäss der internationalen Nizza-Klassifikation, angeben.",
                ]},
                {"heading": "Die vom IGE durchgeführte Prüfung", "paragraphs": [
                    "Das IGE prüft, ob die Marke die formellen und absoluten Schutzvoraussetzungen erfüllt (ausreichende Unterscheidungskraft, kein täuschender oder gegen die öffentliche Ordnung verstossender Charakter), untersucht jedoch grundsätzlich nicht von Amtes wegen das Bestehen ähnlicher oder identischer älterer Marken: diese Prüfung obliegt der anmeldenden Person selbst, meist mittels einer vorgängigen Ähnlichkeitsrecherche.",
                ]},
                {"heading": "Das Widerspruchsverfahren", "paragraphs": [
                    "Nach Eintragung und Publikation der Marke kann die Inhaberin oder der Inhaber einer älteren Marke innert einer Frist von drei Monaten ab Publikation Widerspruch erheben, unter Geltendmachung einer Verwechslungsgefahr zwischen den beiden Zeichen für identische oder ähnliche Waren oder Dienstleistungen.",
                ]},
                {"heading": "Die Schutzdauer", "paragraphs": [
                    "Der Schutz einer schweizerischen Marke dauert zehn Jahre ab Hinterlegung und kann durch Zahlung der Verlängerungsgebühren unbegrenzt um jeweils zehn Jahre verlängert werden, sofern die Marke weiterhin gebraucht wird, um das Risiko einer Löschung wegen Nichtgebrauchs nach Ablauf einer fünfjährigen Karenzfrist zu vermeiden.",
                ]},
            ],
            "faq": [
                {"q": "Prüft das IGE, ob meine Marke mit einer bereits eingetragenen Marke kollidiert?",
                 "a": "Nein, das IGE führt grundsätzlich keine amtliche Prüfung älterer Marken durch: es obliegt der anmeldenden Person selbst, das Fehlen einer Kollision zu prüfen, meist durch eine vorgängige Ähnlichkeitsrecherche vor der Anmeldung."},
                {"q": "Wie lange dauert der Schutz einer schweizerischen Marke?",
                 "a": "Zehn Jahre ab Hinterlegung, unbegrenzt verlängerbar um jeweils zehn Jahre gegen Zahlung der Verlängerungsgebühren."},
                {"q": "Was geschieht, wenn ich meine Marke nicht gebrauche?",
                 "a": "Eine Marke, die während einer ununterbrochenen Frist von fünf Jahren nach Ablauf der Karenzfrist nicht gebraucht wird, riskiert auf Antrag eines interessierten Dritten gelöscht zu werden, ausser bei rechtfertigendem Grund für den Nichtgebrauch."},
            ],
        },
        "it": {
            "slug": "proteggere-marchio-svizzera-deposito-ipi",
            "title": "Proteggere un marchio in Svizzera: il deposito all'IPI",
            "meta": "Procedura di deposito presso l'Istituto federale della proprietà intellettuale, durata di protezione, opposizione: quanto previsto dalla LPM.",
            "sections": [
                {"heading": "Il deposito presso l'IPI", "paragraphs": [
                    "La protezione di un marchio in Svizzera si ottiene tramite la sua registrazione presso l'Istituto federale della proprietà intellettuale (IPI), conformemente alla legge sulla protezione dei marchi (LPM). La domanda deve precisare il segno da proteggere e l'elenco dei prodotti o servizi interessati, classificati secondo la classificazione internazionale di Nizza.",
                ]},
                {"heading": "L'esame effettuato dall'IPI", "paragraphs": [
                    "L'IPI esamina se il marchio soddisfa le condizioni formali e assolute di protezione (sufficiente carattere distintivo, assenza di carattere ingannevole o contrario all'ordine pubblico), ma non verifica in linea di principio d'ufficio l'esistenza di marchi anteriori simili o identici: questa verifica spetta al depositante stesso, generalmente mediante una ricerca di anteriorità preliminare.",
                ]},
                {"heading": "La procedura di opposizione", "paragraphs": [
                    "Una volta registrato e pubblicato il marchio, il titolare di un marchio anteriore può fare opposizione entro un termine di tre mesi dalla pubblicazione, facendo valere un rischio di confusione tra i due segni per prodotti o servizi identici o simili.",
                ]},
                {"heading": "La durata di protezione", "paragraphs": [
                    "La protezione di un marchio svizzero dura dieci anni dal deposito, e può essere rinnovata indefinitamente per periodi di dieci anni mediante il pagamento delle tasse di rinnovo, a condizione che il marchio continui ad essere utilizzato per evitare il rischio di una radiazione per mancato uso dopo un termine di carenza di cinque anni.",
                ]},
            ],
            "faq": [
                {"q": "L'IPI verifica se il mio marchio entra in conflitto con un marchio già depositato?",
                 "a": "No, l'IPI non effettua in linea di principio un esame d'ufficio dei marchi anteriori: spetta al depositante verificare da sé l'assenza di conflitto, generalmente tramite una ricerca di anteriorità preliminare al deposito."},
                {"q": "Quanto dura la protezione di un marchio svizzero?",
                 "a": "Dieci anni dal deposito, rinnovabile indefinitamente per periodi di dieci anni mediante il pagamento delle tasse di rinnovo."},
                {"q": "Cosa succede se non utilizzo il mio marchio?",
                 "a": "Un marchio non utilizzato per un periodo ininterrotto di cinque anni dopo lo scadere del termine di carenza rischia di essere radiato su richiesta di un terzo interessato, salvo giusto motivo di non uso."},
            ],
        },
        "en": {
            "slug": "protecting-trademark-switzerland-ipi-filing",
            "title": "Protecting a trademark in Switzerland: filing with the IPI",
            "meta": "Filing procedure with the Swiss Federal Institute of Intellectual Property, term of protection, opposition: what the Trademark Protection Act provides.",
            "sections": [
                {"heading": "Filing with the IPI", "paragraphs": [
                    "Trademark protection in Switzerland is obtained by registering with the Swiss Federal Institute of Intellectual Property (IPI), under the Trademark Protection Act (TPA). The application must specify the sign to be protected and the list of goods or services concerned, classified according to the international Nice Classification.",
                ]},
                {"heading": "The examination carried out by the IPI", "paragraphs": [
                    "The IPI examines whether the trademark meets the formal and absolute conditions for protection (sufficient distinctiveness, no deceptive character or conflict with public policy), but does not, in principle, examine ex officio the existence of similar or identical earlier trademarks: this check is up to the applicant themselves, usually through a prior availability search.",
                ]},
                {"heading": "The opposition procedure", "paragraphs": [
                    "Once the trademark is registered and published, the holder of an earlier trademark can file an opposition within three months of publication, claiming a likelihood of confusion between the two signs for identical or similar goods or services.",
                ]},
                {"heading": "The term of protection", "paragraphs": [
                    "Protection of a Swiss trademark lasts ten years from filing, and can be renewed indefinitely for ten-year periods upon payment of renewal fees, provided the trademark continues to be used to avoid the risk of cancellation for non-use after a five-year grace period.",
                ]},
            ],
            "faq": [
                {"q": "Does the IPI check whether my trademark conflicts with an already registered trademark?",
                 "a": "No, the IPI does not, in principle, carry out an ex officio examination of earlier trademarks: it is up to the applicant to check for themselves that there is no conflict, usually through a prior availability search before filing."},
                {"q": "How long does protection of a Swiss trademark last?",
                 "a": "Ten years from filing, renewable indefinitely for ten-year periods upon payment of renewal fees."},
                {"q": "What happens if I don't use my trademark?",
                 "a": "A trademark not used for an uninterrupted period of five years after the grace period expires risks being cancelled at the request of an interested third party, unless there is good cause for non-use."},
            ],
        },
    },
    "droit-auteur-duree-protection-exceptions": {
        "domaine_id": "propriete_intellectuelle",
        "published": "2026-07-30",
        "fr": {
            "slug": "droit-auteur-duree-protection-exceptions",
            "title": "Droit d'auteur : durée de protection et exceptions",
            "meta": "Protection automatique sans formalité, durée de 70 ans après la mort de l'auteur, usage privé et citation : les règles de la LDA.",
            "sections": [
                {"heading": "Une protection automatique", "paragraphs": [
                    "Contrairement à une marque ou un brevet, le droit d'auteur naît automatiquement dès la création d'une œuvre présentant un caractère individuel, sans aucune formalité de dépôt ou d'enregistrement (loi sur le droit d'auteur, LDA). L'œuvre doit toutefois atteindre un seuil minimal d'originalité pour être protégée.",
                ]},
                {"heading": "La durée de protection", "paragraphs": [
                    "En règle générale, le droit d'auteur protège une œuvre pendant 70 ans à compter du décès de l'auteur, ce qu'on appelle la règle post mortem auctoris. Des durées différentes peuvent s'appliquer à certaines catégories d'œuvres, comme les logiciels informatiques, soumis à des règles spécifiques de la LDA.",
                ]},
                {"heading": "Les principales exceptions", "paragraphs": [
                    "La LDA prévoit des utilisations autorisées sans l'accord de l'auteur, notamment l'usage strictement privé dans le cercle des personnes étroitement liées, la citation à des fins d'illustration ou de discussion dans une mesure justifiée par le but poursuivi, et certains usages pédagogiques ou pour les personnes en situation de handicap, dans les limites fixées par la loi.",
                ]},
                {"heading": "Les droits moraux et patrimoniaux", "paragraphs": [
                    "Le droit d'auteur comprend des droits patrimoniaux (reproduction, mise à disposition, adaptation de l'œuvre), qui peuvent être cédés ou faire l'objet d'une licence, et des droits moraux (droit à la paternité de l'œuvre, droit à son intégrité), qui restent en principe attachés à la personne de l'auteur et ne peuvent pas être cédés de la même manière.",
                ]},
            ],
            "faq": [
                {"q": "Dois-je déposer mon œuvre pour bénéficier du droit d'auteur ?",
                 "a": "Non, le droit d'auteur naît automatiquement dès la création d'une œuvre présentant un caractère individuel, sans aucune formalité de dépôt ou d'enregistrement."},
                {"q": "Combien de temps dure la protection d'une œuvre par le droit d'auteur ?",
                 "a": "En règle générale 70 ans à compter du décès de l'auteur, avec des règles particulières pour certaines catégories d'œuvres comme les logiciels."},
                {"q": "Puis-je citer un extrait d'une œuvre protégée sans autorisation ?",
                 "a": "Oui, dans une mesure justifiée par le but d'illustration ou de discussion poursuivi, la citation est une exception reconnue par la LDA, à condition de respecter les usages en matière de citation (source, étendue raisonnable)."},
            ],
        },
        "de": {
            "slug": "urheberrecht-schutzdauer-ausnahmen",
            "title": "Urheberrecht: Schutzdauer und Ausnahmen",
            "meta": "Automatischer Schutz ohne Formalität, Dauer von 70 Jahren nach dem Tod der Urheberin oder des Urhebers, Eigengebrauch und Zitat: die Regeln des URG.",
            "sections": [
                {"heading": "Ein automatischer Schutz", "paragraphs": [
                    "Im Gegensatz zu einer Marke oder einem Patent entsteht das Urheberrecht automatisch mit der Schaffung eines Werks mit individuellem Charakter, ohne jegliche Anmeldung oder Registrierung (Urheberrechtsgesetz, URG). Das Werk muss jedoch eine Mindestschwelle an Originalität erreichen, um geschützt zu sein.",
                ]},
                {"heading": "Die Schutzdauer", "paragraphs": [
                    "In der Regel schützt das Urheberrecht ein Werk während 70 Jahren nach dem Tod der Urheberin oder des Urhebers, was als Regel post mortem auctoris bezeichnet wird. Für bestimmte Werkkategorien, wie Computerprogramme, können abweichende Dauern gelten, die besonderen Bestimmungen des URG unterliegen.",
                ]},
                {"heading": "Die wichtigsten Ausnahmen", "paragraphs": [
                    "Das URG sieht Nutzungen vor, die ohne Zustimmung der Urheberin oder des Urhebers zulässig sind, namentlich den Eigengebrauch im engen Kreis nahestehender Personen, das Zitat zu Illustrations- oder Diskussionszwecken in einem durch den verfolgten Zweck gerechtfertigten Ausmass, sowie bestimmte pädagogische Nutzungen oder Nutzungen zugunsten von Menschen mit Behinderung, innerhalb der gesetzlich festgelegten Grenzen.",
                ]},
                {"heading": "Persönlichkeits- und Vermögensrechte", "paragraphs": [
                    "Das Urheberrecht umfasst Vermögensrechte (Vervielfältigung, Zugänglichmachung, Bearbeitung des Werks), die abgetreten oder lizenziert werden können, sowie Persönlichkeitsrechte (Anerkennung der Urheberschaft, Recht auf die Werkintegrität), die grundsätzlich an die Person der Urheberin oder des Urhebers gebunden bleiben und nicht auf dieselbe Weise abgetreten werden können.",
                ]},
            ],
            "faq": [
                {"q": "Muss ich mein Werk anmelden, um vom Urheberrecht zu profitieren?",
                 "a": "Nein, das Urheberrecht entsteht automatisch mit der Schaffung eines Werks mit individuellem Charakter, ohne jegliche Anmeldung oder Registrierung."},
                {"q": "Wie lange dauert der Schutz eines Werks durch das Urheberrecht?",
                 "a": "In der Regel 70 Jahre nach dem Tod der Urheberin oder des Urhebers, mit besonderen Regeln für bestimmte Werkkategorien wie Computerprogramme."},
                {"q": "Darf ich einen Auszug aus einem geschützten Werk ohne Erlaubnis zitieren?",
                 "a": "Ja, in einem durch den Illustrations- oder Diskussionszweck gerechtfertigten Ausmass ist das Zitat eine vom URG anerkannte Ausnahme, sofern die Gepflogenheiten des Zitierens (Quellenangabe, angemessener Umfang) eingehalten werden."},
            ],
        },
        "it": {
            "slug": "diritto-autore-durata-protezione-eccezioni",
            "title": "Diritto d'autore: durata di protezione ed eccezioni",
            "meta": "Protezione automatica senza formalità, durata di 70 anni dopo la morte dell'autore, uso privato e citazione: le regole della LDA.",
            "sections": [
                {"heading": "Una protezione automatica", "paragraphs": [
                    "A differenza di un marchio o di un brevetto, il diritto d'autore nasce automaticamente dalla creazione di un'opera dal carattere individuale, senza alcuna formalità di deposito o registrazione (legge sul diritto d'autore, LDA). L'opera deve tuttavia raggiungere una soglia minima di originalità per essere protetta.",
                ]},
                {"heading": "La durata di protezione", "paragraphs": [
                    "In generale, il diritto d'autore protegge un'opera per 70 anni dalla morte dell'autore, quanto viene chiamato la regola post mortem auctoris. Durate diverse possono applicarsi a determinate categorie di opere, come i programmi per computer, soggetti a regole specifiche della LDA.",
                ]},
                {"heading": "Le principali eccezioni", "paragraphs": [
                    "La LDA prevede utilizzazioni consentite senza il consenso dell'autore, in particolare l'uso strettamente privato nella cerchia di persone strettamente legate, la citazione a scopo illustrativo o di discussione nella misura giustificata dallo scopo perseguito, e determinati usi pedagogici o a favore di persone con disabilità, nei limiti fissati dalla legge.",
                ]},
                {"heading": "I diritti morali e patrimoniali", "paragraphs": [
                    "Il diritto d'autore comprende diritti patrimoniali (riproduzione, messa a disposizione, adattamento dell'opera), che possono essere ceduti o oggetto di licenza, e diritti morali (diritto alla paternità dell'opera, diritto alla sua integrità), che restano in linea di principio legati alla persona dell'autore e non possono essere ceduti allo stesso modo.",
                ]},
            ],
            "faq": [
                {"q": "Devo depositare la mia opera per beneficiare del diritto d'autore?",
                 "a": "No, il diritto d'autore nasce automaticamente dalla creazione di un'opera dal carattere individuale, senza alcuna formalità di deposito o registrazione."},
                {"q": "Quanto dura la protezione di un'opera tramite il diritto d'autore?",
                 "a": "In generale 70 anni dalla morte dell'autore, con regole particolari per determinate categorie di opere come i programmi per computer."},
                {"q": "Posso citare un estratto di un'opera protetta senza autorizzazione?",
                 "a": "Sì, nella misura giustificata dallo scopo illustrativo o di discussione perseguito, la citazione è un'eccezione riconosciuta dalla LDA, a condizione di rispettare gli usi in materia di citazione (fonte, estensione ragionevole)."},
            ],
        },
        "en": {
            "slug": "copyright-term-protection-exceptions",
            "title": "Copyright: term of protection and exceptions",
            "meta": "Automatic protection without formalities, 70-year term after the author's death, private use and quotation: the rules of the Copyright Act.",
            "sections": [
                {"heading": "Automatic protection", "paragraphs": [
                    "Unlike a trademark or a patent, copyright arises automatically upon the creation of a work with individual character, without any filing or registration formality (Copyright Act). The work must, however, reach a minimum threshold of originality to be protected.",
                ]},
                {"heading": "The term of protection", "paragraphs": [
                    "As a general rule, copyright protects a work for 70 years from the author's death, known as the post mortem auctoris rule. Different terms may apply to certain categories of works, such as computer programs, which are subject to specific provisions of the Copyright Act.",
                ]},
                {"heading": "The main exceptions", "paragraphs": [
                    "The Copyright Act provides for uses permitted without the author's consent, in particular strictly private use within a circle of closely connected persons, quotation for illustration or discussion purposes to the extent justified by the purpose pursued, and certain educational uses or uses for the benefit of people with disabilities, within the limits set by law.",
                ]},
                {"heading": "Moral and economic rights", "paragraphs": [
                    "Copyright includes economic rights (reproduction, making available, adaptation of the work), which can be assigned or licensed, and moral rights (right of attribution, right to the integrity of the work), which in principle remain attached to the author personally and cannot be assigned in the same way.",
                ]},
            ],
            "faq": [
                {"q": "Do I need to register my work to benefit from copyright?",
                 "a": "No, copyright arises automatically upon the creation of a work with individual character, without any filing or registration formality."},
                {"q": "How long does copyright protection of a work last?",
                 "a": "As a general rule 70 years from the author's death, with special rules for certain categories of works such as computer programs."},
                {"q": "Can I quote an excerpt from a protected work without permission?",
                 "a": "Yes, to the extent justified by the illustration or discussion purpose pursued, quotation is an exception recognised by the Copyright Act, provided the customary practices for quotation (source, reasonable extent) are respected."},
            ],
        },
    },
    "reconnaissance-divorce-etranger": {
        "domaine_id": "droit_international_prive",
        "published": "2026-07-30",
        "fr": {
            "slug": "reconnaissance-divorce-prononce-etranger",
            "title": "Reconnaissance d'un divorce prononcé à l'étranger",
            "meta": "Conditions générales de reconnaissance des décisions étrangères, procédure et registre de l'état civil : ce que prévoit la LDIP.",
            "sections": [
                {"heading": "Le principe de la reconnaissance", "paragraphs": [
                    "Une décision de divorce rendue à l'étranger n'a d'effet en Suisse que si elle y est reconnue, conformément à la loi fédérale sur le droit international privé (LDIP). Cette reconnaissance n'est en principe pas automatique dans tous les cas : elle peut nécessiter une démarche formelle, notamment lorsqu'une inscription au registre suisse de l'état civil est requise.",
                ]},
                {"heading": "Les conditions générales de reconnaissance", "paragraphs": [
                    "La LDIP pose des conditions générales pour la reconnaissance d'une décision étrangère (art. 25 ss LDIP), notamment la compétence des autorités ou juridictions de l'État où la décision a été rendue selon les critères reconnus par le droit suisse, l'absence de recours ordinaire encore possible contre la décision dans cet État, et l'absence de motif de refus tel qu'une violation de l'ordre public suisse.",
                ]},
                {"heading": "Les règles particulières applicables au divorce", "paragraphs": [
                    "L'art. 65 LDIP prévoit des règles spécifiques pour la reconnaissance des décisions étrangères de divorce ou de séparation de corps, en tenant notamment compte de la nationalité et du domicile des époux au moment de la procédure à l'étranger.",
                ]},
                {"heading": "La procédure pratique", "paragraphs": [
                    "En pratique, la reconnaissance et la transcription d'un divorce étranger passent le plus souvent par l'autorité cantonale de surveillance de l'état civil du canton d'origine ou de domicile de la personne concernée, à laquelle il convient de soumettre la décision étrangère accompagnée des traductions et légalisations requises.",
                ]},
            ],
            "faq": [
                {"q": "Un divorce prononcé à l'étranger est-il automatiquement valable en Suisse ?",
                 "a": "Pas nécessairement : sa reconnaissance dépend des conditions générales posées par la LDIP (compétence de l'autorité étrangère, absence de recours encore ouvert, respect de l'ordre public suisse), et peut nécessiter une démarche formelle auprès de l'autorité de l'état civil."},
                {"q": "À qui dois-je m'adresser pour faire reconnaître mon divorce étranger ?",
                 "a": "En général à l'autorité cantonale de surveillance de l'état civil du canton d'origine ou de domicile, à laquelle il faut soumettre la décision étrangère avec les traductions et légalisations requises."},
                {"q": "Que se passe-t-il si mon divorce étranger n'est pas reconnu en Suisse ?",
                 "a": "Le mariage reste en principe considéré comme non dissous pour les autorités suisses tant que la reconnaissance n'a pas été obtenue, ce qui peut avoir des conséquences importantes, notamment pour un remariage ou des questions patrimoniales."},
            ],
        },
        "de": {
            "slug": "anerkennung-scheidung-ausland-ausgesprochen",
            "title": "Anerkennung einer im Ausland ausgesprochenen Scheidung",
            "meta": "Allgemeine Anerkennungsvoraussetzungen für ausländische Entscheide, Verfahren und Zivilstandsregister: was das IPRG vorsieht.",
            "sections": [
                {"heading": "Der Grundsatz der Anerkennung", "paragraphs": [
                    "Ein im Ausland ergangener Scheidungsentscheid entfaltet in der Schweiz nur Wirkung, wenn er dort anerkannt wird, gemäss dem Bundesgesetz über das Internationale Privatrecht (IPRG). Diese Anerkennung erfolgt nicht in allen Fällen automatisch: sie kann einen förmlichen Schritt erfordern, namentlich wenn eine Eintragung im schweizerischen Zivilstandsregister nötig ist.",
                ]},
                {"heading": "Die allgemeinen Anerkennungsvoraussetzungen", "paragraphs": [
                    "Das IPRG stellt allgemeine Voraussetzungen für die Anerkennung eines ausländischen Entscheids auf (Art. 25 ff. IPRG), namentlich die Zuständigkeit der Behörden oder Gerichte des Staates, in dem der Entscheid ergangen ist, gemäss den vom schweizerischen Recht anerkannten Kriterien, das Fehlen eines dort noch möglichen ordentlichen Rechtsmittels, sowie das Fehlen eines Ablehnungsgrundes wie einer Verletzung des schweizerischen Ordre public.",
                ]},
                {"heading": "Die auf die Scheidung anwendbaren besonderen Regeln", "paragraphs": [
                    "Art. 65 IPRG sieht besondere Regeln für die Anerkennung ausländischer Scheidungs- oder Trennungsentscheide vor, wobei namentlich die Staatsangehörigkeit und der Wohnsitz der Ehegatten zum Zeitpunkt des Verfahrens im Ausland berücksichtigt werden.",
                ]},
                {"heading": "Das praktische Verfahren", "paragraphs": [
                    "In der Praxis erfolgen die Anerkennung und Eintragung einer ausländischen Scheidung meist über die kantonale Zivilstandsaufsichtsbehörde des Heimat- oder Wohnsitzkantons der betroffenen Person, welcher der ausländische Entscheid samt den erforderlichen Übersetzungen und Beglaubigungen einzureichen ist.",
                ]},
            ],
            "faq": [
                {"q": "Ist eine im Ausland ausgesprochene Scheidung automatisch in der Schweiz gültig?",
                 "a": "Nicht zwingend: ihre Anerkennung hängt von den allgemeinen Voraussetzungen des IPRG ab (Zuständigkeit der ausländischen Behörde, Fehlen eines noch offenen Rechtsmittels, Einhaltung des schweizerischen Ordre public) und kann einen förmlichen Schritt bei der Zivilstandsbehörde erfordern."},
                {"q": "An wen muss ich mich wenden, um meine ausländische Scheidung anerkennen zu lassen?",
                 "a": "In der Regel an die kantonale Zivilstandsaufsichtsbehörde des Heimat- oder Wohnsitzkantons, der der ausländische Entscheid samt den erforderlichen Übersetzungen und Beglaubigungen einzureichen ist."},
                {"q": "Was geschieht, wenn meine ausländische Scheidung in der Schweiz nicht anerkannt wird?",
                 "a": "Die Ehe gilt für die schweizerischen Behörden grundsätzlich weiterhin als nicht aufgelöst, solange die Anerkennung nicht erfolgt ist, was erhebliche Folgen haben kann, namentlich für eine Wiederverheiratung oder vermögensrechtliche Fragen."},
            ],
        },
        "it": {
            "slug": "riconoscimento-divorzio-pronunciato-estero",
            "title": "Riconoscimento di un divorzio pronunciato all'estero",
            "meta": "Condizioni generali di riconoscimento delle decisioni straniere, procedura e registro dello stato civile: quanto previsto dalla LDIP.",
            "sections": [
                {"heading": "Il principio del riconoscimento", "paragraphs": [
                    "Una decisione di divorzio pronunciata all'estero non ha effetto in Svizzera se non vi viene riconosciuta, conformemente alla legge federale sul diritto internazionale privato (LDIP). Questo riconoscimento non è in linea di principio automatico in tutti i casi: può richiedere una procedura formale, in particolare quando è necessaria un'iscrizione nel registro svizzero dello stato civile.",
                ]},
                {"heading": "Le condizioni generali di riconoscimento", "paragraphs": [
                    "La LDIP pone condizioni generali per il riconoscimento di una decisione straniera (art. 25 segg. LDIP), in particolare la competenza delle autorità o giurisdizioni dello Stato in cui la decisione è stata resa secondo i criteri riconosciuti dal diritto svizzero, l'assenza di un rimedio ordinario ancora possibile contro la decisione in tale Stato, e l'assenza di un motivo di rifiuto come una violazione dell'ordine pubblico svizzero.",
                ]},
                {"heading": "Le regole particolari applicabili al divorzio", "paragraphs": [
                    "L'art. 65 LDIP prevede regole specifiche per il riconoscimento delle decisioni straniere di divorzio o separazione, tenendo conto in particolare della nazionalità e del domicilio dei coniugi al momento della procedura all'estero.",
                ]},
                {"heading": "La procedura pratica", "paragraphs": [
                    "In pratica, il riconoscimento e la trascrizione di un divorzio straniero avvengono il più delle volte tramite l'autorità cantonale di vigilanza sullo stato civile del Cantone d'origine o di domicilio della persona interessata, alla quale va sottoposta la decisione straniera accompagnata dalle traduzioni e legalizzazioni richieste.",
                ]},
            ],
            "faq": [
                {"q": "Un divorzio pronunciato all'estero è automaticamente valido in Svizzera?",
                 "a": "Non necessariamente: il suo riconoscimento dipende dalle condizioni generali poste dalla LDIP (competenza dell'autorità straniera, assenza di rimedio ancora possibile, rispetto dell'ordine pubblico svizzero), e può richiedere una procedura formale presso l'autorità dello stato civile."},
                {"q": "A chi devo rivolgermi per far riconoscere il mio divorzio straniero?",
                 "a": "Generalmente all'autorità cantonale di vigilanza sullo stato civile del Cantone d'origine o di domicilio, alla quale va sottoposta la decisione straniera con le traduzioni e legalizzazioni richieste."},
                {"q": "Cosa succede se il mio divorzio straniero non viene riconosciuto in Svizzera?",
                 "a": "Il matrimonio resta in linea di principio considerato non sciolto per le autorità svizzere finché il riconoscimento non è stato ottenuto, il che può avere conseguenze importanti, in particolare per un nuovo matrimonio o questioni patrimoniali."},
            ],
        },
        "en": {
            "slug": "recognition-divorce-granted-abroad",
            "title": "Recognition of a divorce granted abroad",
            "meta": "General conditions for recognising foreign decisions, procedure and civil registry: what the Federal Act on Private International Law provides.",
            "sections": [
                {"heading": "The principle of recognition", "paragraphs": [
                    "A divorce decision issued abroad has no effect in Switzerland unless it is recognised there, under the Federal Act on Private International Law (PILA). This recognition is not automatic in all cases: it may require a formal procedure, in particular when an entry in the Swiss civil registry is required.",
                ]},
                {"heading": "The general conditions for recognition", "paragraphs": [
                    "The PILA sets general conditions for recognising a foreign decision (art. 25 ff. PILA), in particular the competence of the authorities or courts of the state where the decision was issued according to criteria recognised by Swiss law, the absence of an ordinary remedy still available against the decision in that state, and the absence of a ground for refusal such as a violation of Swiss public policy.",
                ]},
                {"heading": "Special rules applicable to divorce", "paragraphs": [
                    "Art. 65 PILA provides specific rules for recognising foreign divorce or legal separation decisions, taking into account in particular the nationality and domicile of the spouses at the time of the proceedings abroad.",
                ]},
                {"heading": "The practical procedure", "paragraphs": [
                    "In practice, recognition and registration of a foreign divorce most often go through the cantonal civil registry supervisory authority of the person's canton of origin or domicile, to which the foreign decision must be submitted along with the required translations and legalisations.",
                ]},
            ],
            "faq": [
                {"q": "Is a divorce granted abroad automatically valid in Switzerland?",
                 "a": "Not necessarily: its recognition depends on the general conditions set by the PILA (competence of the foreign authority, absence of a remedy still available, compliance with Swiss public policy), and may require a formal procedure with the civil registry authority."},
                {"q": "Who should I approach to have my foreign divorce recognised?",
                 "a": "Generally the cantonal civil registry supervisory authority of the canton of origin or domicile, to which the foreign decision must be submitted with the required translations and legalisations."},
                {"q": "What happens if my foreign divorce is not recognised in Switzerland?",
                 "a": "The marriage is in principle still considered undissolved by the Swiss authorities until recognition has been obtained, which can have significant consequences, particularly for remarriage or financial matters."},
            ],
        },
    },
    "droit-applicable-contrat-international": {
        "domaine_id": "droit_international_prive",
        "published": "2026-07-30",
        "fr": {
            "slug": "quel-droit-applique-contrat-international",
            "title": "Quel droit s'applique à un contrat international",
            "meta": "Élection de droit par les parties, rattachement à la prestation caractéristique en l'absence de choix : les règles de la LDIP.",
            "sections": [
                {"heading": "La liberté de choix des parties", "paragraphs": [
                    "L'art. 116 LDIP permet aux parties à un contrat international de choisir librement le droit applicable à leur relation contractuelle, que ce droit ait ou non un lien objectif avec le contrat. Ce choix peut être exprès ou résulter de façon certaine des dispositions du contrat ou des circonstances.",
                ]},
                {"heading": "Le rattachement en l'absence de choix", "paragraphs": [
                    "À défaut de choix des parties, l'art. 117 LDIP soumet le contrat au droit de l'État avec lequel il présente les liens les plus étroits, présumés être ceux de l'État de résidence habituelle ou de l'établissement de la partie qui doit fournir la prestation caractéristique du contrat (par exemple le vendeur dans un contrat de vente, ou le prestataire dans un contrat de service).",
                ]},
                {"heading": "Les limites à la liberté de choix", "paragraphs": [
                    "Cette liberté de choix n'est pas absolue : certaines dispositions impératives du droit suisse ou du droit d'un autre État peuvent s'appliquer malgré le choix des parties, notamment dans des domaines protégeant une partie considérée comme plus faible (contrats de consommation, contrats de travail), selon les règles spécifiques prévues par la LDIP pour ces catégories de contrats.",
                ]},
                {"heading": "Le for judiciaire", "paragraphs": [
                    "Le droit applicable au contrat est une question distincte de celle du tribunal compétent en cas de litige : les parties peuvent, dans certaines limites, également convenir d'une clause d'élection de for, désignant les tribunaux compétents en cas de différend, indépendamment du droit matériel choisi pour régir le fond du contrat.",
                ]},
            ],
            "faq": [
                {"q": "Les parties peuvent-elles choisir n'importe quel droit pour leur contrat international ?",
                 "a": "En principe oui, l'art. 116 LDIP laisse une grande liberté de choix, même sans lien objectif entre le droit choisi et le contrat, sous réserve de certaines dispositions impératives protégeant une partie faible dans certains types de contrats."},
                {"q": "Quel droit s'applique si le contrat ne prévoit aucune clause de choix ?",
                 "a": "Le droit de l'État avec lequel le contrat présente les liens les plus étroits, présumé être celui de la partie qui fournit la prestation caractéristique du contrat, selon l'art. 117 LDIP."},
                {"q": "Le choix du droit applicable détermine-t-il aussi le tribunal compétent ?",
                 "a": "Non, ce sont deux questions distinctes : le droit applicable régit le fond du litige, tandis que la compétence judiciaire dépend de règles propres, éventuellement précisées par une clause d'élection de for distincte dans le contrat."},
            ],
        },
        "de": {
            "slug": "anwendbares-recht-internationaler-vertrag",
            "title": "Welches Recht auf einen internationalen Vertrag anwendbar ist",
            "meta": "Rechtswahl durch die Parteien, Anknüpfung an die charakteristische Leistung mangels Wahl: die Regeln des IPRG.",
            "sections": [
                {"heading": "Die Wahlfreiheit der Parteien", "paragraphs": [
                    "Art. 116 IPRG erlaubt den Parteien eines internationalen Vertrags, das auf ihre Vertragsbeziehung anwendbare Recht frei zu wählen, unabhängig davon, ob dieses Recht einen objektiven Bezug zum Vertrag aufweist oder nicht. Diese Wahl kann ausdrücklich erfolgen oder sich eindeutig aus den Vertragsbestimmungen oder den Umständen ergeben.",
                ]},
                {"heading": "Die Anknüpfung mangels Wahl", "paragraphs": [
                    "Mangels Rechtswahl durch die Parteien unterstellt Art. 117 IPRG den Vertrag dem Recht des Staates, mit dem er am engsten zusammenhängt, wobei vermutet wird, dass dies das Recht des Staates des gewöhnlichen Aufenthalts oder der Niederlassung der Partei ist, welche die für den Vertrag charakteristische Leistung erbringen muss (etwa die Verkäuferin oder der Verkäufer bei einem Kaufvertrag, oder die Dienstleisterin oder der Dienstleister bei einem Dienstleistungsvertrag).",
                ]},
                {"heading": "Die Grenzen der Wahlfreiheit", "paragraphs": [
                    "Diese Wahlfreiheit ist nicht unbeschränkt: bestimmte zwingende Bestimmungen des schweizerischen Rechts oder des Rechts eines anderen Staates können trotz der Rechtswahl der Parteien Anwendung finden, namentlich in Bereichen, die eine als schwächer geltende Partei schützen (Konsumentenverträge, Arbeitsverträge), gemäss den vom IPRG für diese Vertragskategorien vorgesehenen besonderen Regeln.",
                ]},
                {"heading": "Der Gerichtsstand", "paragraphs": [
                    "Das auf den Vertrag anwendbare Recht ist eine von der Frage des im Streitfall zuständigen Gerichts getrennte Frage: die Parteien können innerhalb bestimmter Grenzen auch eine Gerichtsstandsklausel vereinbaren, welche die im Streitfall zuständigen Gerichte bezeichnet, unabhängig vom für den Vertragsinhalt gewählten materiellen Recht.",
                ]},
            ],
            "faq": [
                {"q": "Können die Parteien für ihren internationalen Vertrag ein beliebiges Recht wählen?",
                 "a": "Grundsätzlich ja, Art. 116 IPRG lässt eine grosse Wahlfreiheit zu, selbst ohne objektiven Bezug zwischen dem gewählten Recht und dem Vertrag, vorbehältlich bestimmter zwingender Bestimmungen zum Schutz einer schwächeren Partei bei bestimmten Vertragsarten."},
                {"q": "Welches Recht gilt, wenn der Vertrag keine Rechtswahlklausel enthält?",
                 "a": "Das Recht des Staates, mit dem der Vertrag am engsten zusammenhängt, vermutungsweise jenes der Partei, welche die charakteristische Leistung des Vertrags erbringt, gemäss Art. 117 IPRG."},
                {"q": "Bestimmt die Wahl des anwendbaren Rechts auch das zuständige Gericht?",
                 "a": "Nein, das sind zwei getrennte Fragen: das anwendbare Recht regelt den Inhalt des Streits, während die gerichtliche Zuständigkeit eigenen Regeln folgt, gegebenenfalls präzisiert durch eine gesonderte Gerichtsstandsklausel im Vertrag."},
            ],
        },
        "it": {
            "slug": "diritto-applicabile-contratto-internazionale",
            "title": "Quale diritto si applica a un contratto internazionale",
            "meta": "Scelta del diritto da parte delle parti, collegamento alla prestazione caratteristica in assenza di scelta: le regole della LDIP.",
            "sections": [
                {"heading": "La libertà di scelta delle parti", "paragraphs": [
                    "L'art. 116 LDIP permette alle parti di un contratto internazionale di scegliere liberamente il diritto applicabile al loro rapporto contrattuale, che tale diritto abbia o meno un legame oggettivo con il contratto. Questa scelta può essere espressa o risultare in modo certo dalle disposizioni del contratto o dalle circostanze.",
                ]},
                {"heading": "Il collegamento in assenza di scelta", "paragraphs": [
                    "In mancanza di scelta delle parti, l'art. 117 LDIP sottopone il contratto al diritto dello Stato con cui presenta il legame più stretto, presunto essere quello dello Stato di residenza abituale o di stabilimento della parte che deve fornire la prestazione caratteristica del contratto (per esempio il venditore in un contratto di vendita, o il prestatore in un contratto di servizio).",
                ]},
                {"heading": "I limiti alla libertà di scelta", "paragraphs": [
                    "Questa libertà di scelta non è assoluta: determinate disposizioni imperative del diritto svizzero o del diritto di un altro Stato possono applicarsi nonostante la scelta delle parti, in particolare in ambiti che proteggono una parte considerata più debole (contratti di consumo, contratti di lavoro), secondo le regole specifiche previste dalla LDIP per queste categorie di contratti.",
                ]},
                {"heading": "Il foro giudiziario", "paragraphs": [
                    "Il diritto applicabile al contratto è una questione distinta da quella del tribunale competente in caso di controversia: le parti possono, entro certi limiti, convenire anche una clausola di elezione del foro, designando i tribunali competenti in caso di controversia, indipendentemente dal diritto materiale scelto per disciplinare il contenuto del contratto.",
                ]},
            ],
            "faq": [
                {"q": "Le parti possono scegliere qualsiasi diritto per il loro contratto internazionale?",
                 "a": "In linea di principio sì, l'art. 116 LDIP lascia un'ampia libertà di scelta, anche senza legame oggettivo tra il diritto scelto e il contratto, con riserva di determinate disposizioni imperative a protezione di una parte debole in certi tipi di contratti."},
                {"q": "Quale diritto si applica se il contratto non prevede alcuna clausola di scelta?",
                 "a": "Il diritto dello Stato con cui il contratto presenta il legame più stretto, presunto essere quello della parte che fornisce la prestazione caratteristica del contratto, secondo l'art. 117 LDIP."},
                {"q": "La scelta del diritto applicabile determina anche il tribunale competente?",
                 "a": "No, sono due questioni distinte: il diritto applicabile disciplina il merito della controversia, mentre la competenza giudiziaria dipende da regole proprie, eventualmente precisate da una clausola di elezione del foro distinta nel contratto."},
            ],
        },
        "en": {
            "slug": "law-applicable-international-contract",
            "title": "Which law applies to an international contract",
            "meta": "Choice of law by the parties, connection to the characteristic performance absent a choice: the rules of the Private International Law Act.",
            "sections": [
                {"heading": "The parties' freedom of choice", "paragraphs": [
                    "Art. 116 PILA allows parties to an international contract to freely choose the law applicable to their contractual relationship, whether or not that law has an objective connection to the contract. This choice can be express or result clearly from the terms of the contract or the circumstances.",
                ]},
                {"heading": "Connection absent a choice", "paragraphs": [
                    "Absent a choice by the parties, art. 117 PILA subjects the contract to the law of the state with which it has the closest connection, presumed to be that of the habitual residence or place of business of the party who must provide the performance characteristic of the contract (for example, the seller in a sales contract, or the service provider in a service contract).",
                ]},
                {"heading": "Limits on freedom of choice", "paragraphs": [
                    "This freedom of choice is not unlimited: certain mandatory provisions of Swiss law or the law of another state may apply despite the parties' choice, particularly in areas protecting a party considered weaker (consumer contracts, employment contracts), according to the specific rules the PILA provides for these categories of contract.",
                ]},
                {"heading": "The forum", "paragraphs": [
                    "The law applicable to the contract is a separate question from that of the court with jurisdiction in the event of a dispute: the parties can, within certain limits, also agree on a choice-of-forum clause, designating the courts with jurisdiction in the event of a dispute, independently of the substantive law chosen to govern the content of the contract.",
                ]},
            ],
            "faq": [
                {"q": "Can the parties choose any law for their international contract?",
                 "a": "In principle yes, art. 116 PILA allows broad freedom of choice, even without an objective connection between the chosen law and the contract, subject to certain mandatory provisions protecting a weaker party in certain types of contracts."},
                {"q": "What law applies if the contract contains no choice-of-law clause?",
                 "a": "The law of the state with which the contract has the closest connection, presumed to be that of the party providing the performance characteristic of the contract, under art. 117 PILA."},
                {"q": "Does the choice of applicable law also determine the competent court?",
                 "a": "No, these are two separate questions: the applicable law governs the substance of the dispute, while court jurisdiction depends on its own rules, possibly specified by a separate choice-of-forum clause in the contract."},
            ],
        },
    },
    "conciliation-obligatoire-avant-proces-civil": {
        "domaine_id": "procedure_civile",
        "published": "2026-07-30",
        "fr": {
            "slug": "conciliation-obligatoire-avant-proces-civil",
            "title": "Conciliation obligatoire avant un procès civil",
            "meta": "Tentative de conciliation préalable, autorisation de procéder, exceptions légales : ce que prévoit le Code de procédure civile.",
            "sections": [
                {"heading": "Le principe de la conciliation préalable", "paragraphs": [
                    "Pour la plupart des litiges civils, le CPC impose une tentative de conciliation devant l'autorité de conciliation compétente avant de pouvoir saisir le tribunal (art. 197 CPC). Cette étape vise à favoriser un règlement amiable du différend avant d'engager une procédure judiciaire souvent plus longue et coûteuse.",
                ]},
                {"heading": "Le déroulement de l'audience de conciliation", "paragraphs": [
                    "L'audience de conciliation se déroule devant l'autorité de conciliation, en présence des parties, qui peuvent y être accompagnées d'un avocat. L'autorité tente de rapprocher les positions des parties et peut, dans certains cas et avec l'accord des parties, statuer elle-même sur le litige si sa valeur litigieuse ne dépasse pas un certain montant.",
                ]},
                {"heading": "L'autorisation de procéder", "paragraphs": [
                    "Si aucun accord n'est trouvé, l'autorité de conciliation délivre une autorisation de procéder, qui permet au demandeur de porter le litige devant le tribunal compétent dans un délai fixé par la loi. Sans cette autorisation, une action portée directement devant le tribunal est en principe irrecevable.",
                ]},
                {"heading": "Les exceptions à l'obligation de conciliation", "paragraphs": [
                    "L'art. 198 CPC prévoit des exceptions où la conciliation préalable n'est pas requise, notamment pour certaines procédures sommaires, certains litiges relevant d'une instance cantonale unique, ou lorsque les parties renoncent conjointement à la conciliation dans les litiges patrimoniaux d'une valeur litigieuse suffisamment élevée.",
                ]},
            ],
            "faq": [
                {"q": "Puis-je saisir directement le tribunal sans passer par la conciliation ?",
                 "a": "En principe non pour la plupart des litiges civils : une autorisation de procéder délivrée par l'autorité de conciliation est nécessaire, sauf dans les cas d'exception prévus par l'art. 198 CPC."},
                {"q": "L'autorité de conciliation peut-elle rendre une décision sur le fond du litige ?",
                 "a": "Dans certains cas, oui, avec l'accord des parties et si la valeur litigieuse ne dépasse pas le montant fixé par la loi, l'autorité de conciliation peut statuer elle-même plutôt que de renvoyer l'affaire devant le tribunal."},
                {"q": "Que se passe-t-il si aucun accord n'est trouvé en conciliation ?",
                 "a": "L'autorité de conciliation délivre une autorisation de procéder, qui permet de porter le litige devant le tribunal compétent dans le délai fixé par la loi."},
            ],
        },
        "de": {
            "slug": "obligatorisches-schlichtungsverfahren-vor-zivilprozess",
            "title": "Obligatorisches Schlichtungsverfahren vor einem Zivilprozess",
            "meta": "Vorgängiger Schlichtungsversuch, Klagebewilligung, gesetzliche Ausnahmen: was die Zivilprozessordnung vorsieht.",
            "sections": [
                {"heading": "Der Grundsatz der vorgängigen Schlichtung", "paragraphs": [
                    "Für die meisten Zivilstreitigkeiten schreibt die ZPO einen Schlichtungsversuch vor der zuständigen Schlichtungsbehörde vor, bevor das Gericht angerufen werden kann (Art. 197 ZPO). Dieser Schritt soll eine gütliche Beilegung der Streitigkeit fördern, bevor ein oft längeres und kostspieligeres Gerichtsverfahren eingeleitet wird.",
                ]},
                {"heading": "Der Ablauf der Schlichtungsverhandlung", "paragraphs": [
                    "Die Schlichtungsverhandlung findet vor der Schlichtungsbehörde in Anwesenheit der Parteien statt, die dabei von einer Anwältin oder einem Anwalt begleitet werden können. Die Behörde versucht, die Positionen der Parteien anzunähern, und kann in bestimmten Fällen mit Zustimmung der Parteien selbst über die Streitigkeit entscheiden, sofern deren Streitwert einen bestimmten Betrag nicht übersteigt.",
                ]},
                {"heading": "Die Klagebewilligung", "paragraphs": [
                    "Kommt keine Einigung zustande, stellt die Schlichtungsbehörde eine Klagebewilligung aus, welche der klagenden Partei erlaubt, die Streitigkeit innert der gesetzlich vorgesehenen Frist beim zuständigen Gericht anhängig zu machen. Ohne diese Bewilligung ist eine direkt beim Gericht eingereichte Klage grundsätzlich unzulässig.",
                ]},
                {"heading": "Die Ausnahmen von der Schlichtungspflicht", "paragraphs": [
                    "Art. 198 ZPO sieht Ausnahmen vor, bei denen die vorgängige Schlichtung nicht erforderlich ist, namentlich für bestimmte summarische Verfahren, bestimmte Streitigkeiten, die einer einzigen kantonalen Instanz unterliegen, oder wenn die Parteien bei vermögensrechtlichen Streitigkeiten mit ausreichend hohem Streitwert gemeinsam auf die Schlichtung verzichten.",
                ]},
            ],
            "faq": [
                {"q": "Kann ich direkt das Gericht anrufen, ohne den Schlichtungsweg zu durchlaufen?",
                 "a": "Grundsätzlich nicht bei den meisten Zivilstreitigkeiten: eine von der Schlichtungsbehörde ausgestellte Klagebewilligung ist erforderlich, ausser in den Ausnahmefällen gemäss Art. 198 ZPO."},
                {"q": "Kann die Schlichtungsbehörde einen Entscheid in der Sache selbst fällen?",
                 "a": "In bestimmten Fällen ja, mit Zustimmung der Parteien und sofern der Streitwert den gesetzlich festgelegten Betrag nicht übersteigt, kann die Schlichtungsbehörde selbst entscheiden, statt die Sache ans Gericht zu verweisen."},
                {"q": "Was geschieht, wenn in der Schlichtung keine Einigung erzielt wird?",
                 "a": "Die Schlichtungsbehörde stellt eine Klagebewilligung aus, welche erlaubt, die Streitigkeit innert der gesetzlichen Frist beim zuständigen Gericht anhängig zu machen."},
            ],
        },
        "it": {
            "slug": "conciliazione-obbligatoria-prima-processo-civile",
            "title": "Conciliazione obbligatoria prima di un processo civile",
            "meta": "Tentativo di conciliazione preliminare, autorizzazione ad agire, eccezioni legali: quanto previsto dal Codice di procedura civile.",
            "sections": [
                {"heading": "Il principio della conciliazione preliminare", "paragraphs": [
                    "Per la maggior parte delle controversie civili, il CPC impone un tentativo di conciliazione davanti all'autorità di conciliazione competente prima di poter adire il tribunale (art. 197 CPC). Questa tappa mira a favorire una composizione amichevole della controversia prima di avviare una procedura giudiziaria spesso più lunga e costosa.",
                ]},
                {"heading": "Lo svolgimento dell'udienza di conciliazione", "paragraphs": [
                    "L'udienza di conciliazione si svolge davanti all'autorità di conciliazione, in presenza delle parti, che possono esservi accompagnate da un avvocato. L'autorità tenta di avvicinare le posizioni delle parti e può, in determinati casi e con l'accordo delle parti, decidere essa stessa sulla controversia se il suo valore litigioso non supera un determinato importo.",
                ]},
                {"heading": "L'autorizzazione ad agire", "paragraphs": [
                    "Se non si raggiunge alcun accordo, l'autorità di conciliazione rilascia un'autorizzazione ad agire, che permette all'attore di portare la controversia davanti al tribunale competente entro un termine fissato dalla legge. Senza questa autorizzazione, un'azione promossa direttamente davanti al tribunale è in linea di principio irricevibile.",
                ]},
                {"heading": "Le eccezioni all'obbligo di conciliazione", "paragraphs": [
                    "L'art. 198 CPC prevede eccezioni in cui la conciliazione preliminare non è richiesta, in particolare per determinate procedure sommarie, determinate controversie soggette a un'istanza cantonale unica, o quando le parti rinunciano congiuntamente alla conciliazione nelle controversie patrimoniali di valore litigioso sufficientemente elevato.",
                ]},
            ],
            "faq": [
                {"q": "Posso adire direttamente il tribunale senza passare dalla conciliazione?",
                 "a": "In linea di principio no per la maggior parte delle controversie civili: è necessaria un'autorizzazione ad agire rilasciata dall'autorità di conciliazione, salvo nei casi di eccezione previsti dall'art. 198 CPC."},
                {"q": "L'autorità di conciliazione può emettere una decisione sul merito della controversia?",
                 "a": "In determinati casi sì, con l'accordo delle parti e se il valore litigioso non supera l'importo fissato dalla legge, l'autorità di conciliazione può decidere essa stessa invece di rinviare la causa al tribunale."},
                {"q": "Cosa succede se non si raggiunge alcun accordo in conciliazione?",
                 "a": "L'autorità di conciliazione rilascia un'autorizzazione ad agire, che permette di portare la controversia davanti al tribunale competente entro il termine fissato dalla legge."},
            ],
        },
        "en": {
            "slug": "mandatory-conciliation-before-civil-lawsuit",
            "title": "Mandatory conciliation before a civil lawsuit",
            "meta": "Prior conciliation attempt, authorisation to proceed, statutory exceptions: what the Code of Civil Procedure provides.",
            "sections": [
                {"heading": "The principle of prior conciliation", "paragraphs": [
                    "For most civil disputes, the CCP requires a conciliation attempt before the competent conciliation authority before the court can be approached (art. 197 CCP). This step aims to encourage an amicable settlement of the dispute before initiating often longer and more costly court proceedings.",
                ]},
                {"heading": "How the conciliation hearing unfolds", "paragraphs": [
                    "The conciliation hearing takes place before the conciliation authority, with the parties present, who may be accompanied by a lawyer. The authority tries to bring the parties' positions closer together and, in certain cases and with the parties' agreement, can rule on the dispute itself if its amount in dispute does not exceed a certain threshold.",
                ]},
                {"heading": "Authorisation to proceed", "paragraphs": [
                    "If no agreement is reached, the conciliation authority issues an authorisation to proceed, which allows the plaintiff to bring the dispute before the competent court within the deadline set by law. Without this authorisation, an action filed directly with the court is in principle inadmissible.",
                ]},
                {"heading": "Exceptions to the conciliation requirement", "paragraphs": [
                    "Art. 198 CCP provides exceptions where prior conciliation is not required, in particular for certain summary proceedings, certain disputes subject to a single cantonal instance, or when the parties jointly waive conciliation in property disputes with a sufficiently high amount in dispute.",
                ]},
            ],
            "faq": [
                {"q": "Can I go directly to court without going through conciliation?",
                 "a": "In principle no for most civil disputes: an authorisation to proceed issued by the conciliation authority is required, except in the exceptional cases provided by art. 198 CCP."},
                {"q": "Can the conciliation authority rule on the substance of the dispute itself?",
                 "a": "In certain cases yes, with the parties' agreement and if the amount in dispute does not exceed the threshold set by law, the conciliation authority can rule itself rather than referring the matter to court."},
                {"q": "What happens if no agreement is reached in conciliation?",
                 "a": "The conciliation authority issues an authorisation to proceed, which allows the dispute to be brought before the competent court within the deadline set by law."},
            ],
        },
    },
    "frais-justice-depens-qui-paie": {
        "domaine_id": "procedure_civile",
        "published": "2026-07-30",
        "fr": {
            "slug": "frais-justice-depens-qui-paie-proces",
            "title": "Frais de justice et dépens : qui paie en cas de procès",
            "meta": "Avance de frais, répartition selon l'issue du procès, assistance judiciaire : les règles du Code de procédure civile sur les frais.",
            "sections": [
                {"heading": "Les deux catégories de frais", "paragraphs": [
                    "Le CPC distingue les frais judiciaires (émoluments du tribunal, frais d'expertise, de témoins) des dépens, qui correspondent aux frais d'avocat et autres débours nécessaires exposés par une partie pour défendre ses intérêts dans la procédure (art. 95 CPC).",
                ]},
                {"heading": "L'avance de frais", "paragraphs": [
                    "Le tribunal peut exiger du demandeur une avance destinée à couvrir les frais judiciaires présumés, avant l'ouverture de la procédure sur le fond. À défaut de paiement de cette avance dans le délai imparti, la demande peut être déclarée irrecevable.",
                ]},
                {"heading": "La règle générale de répartition", "paragraphs": [
                    "Selon l'art. 106 CPC, les frais sont en principe mis à la charge de la partie qui succombe. En cas de succès partiel de chaque partie, les frais sont répartis proportionnellement selon le sort de la cause. Le tribunal peut s'écarter de cette règle générale pour des motifs d'équité dans certaines situations.",
                ]},
                {"heading": "L'assistance judiciaire", "paragraphs": [
                    "Une personne ne disposant pas de ressources suffisantes pour assumer les frais d'un procès sans porter atteinte au minimum vital nécessaire à son entretien peut demander l'assistance judiciaire (art. 117 ss CPC), qui peut couvrir tout ou partie des frais judiciaires et, si nécessaire, la désignation d'un avocat d'office, à condition que la cause ne paraisse pas dépourvue de toute chance de succès.",
                ]},
            ],
            "faq": [
                {"q": "Qui paie les frais si je perds mon procès ?",
                 "a": "En principe la partie qui succombe supporte les frais judiciaires et les dépens de la partie adverse (art. 106 CPC), sous réserve d'une répartition proportionnelle en cas de succès partiel de chaque partie."},
                {"q": "Puis-je obtenir une aide si je n'ai pas les moyens de payer les frais de justice ?",
                 "a": "Oui, l'assistance judiciaire (art. 117 ss CPC) peut couvrir tout ou partie des frais judiciaires et la désignation d'un avocat d'office, à condition de ne pas disposer de ressources suffisantes et que la cause ne paraisse pas dépourvue de chance de succès."},
                {"q": "Que se passe-t-il si je ne paie pas l'avance de frais demandée par le tribunal ?",
                 "a": "Le tribunal peut, à défaut de paiement dans le délai imparti, déclarer la demande irrecevable sans examiner le fond du litige."},
            ],
        },
        "de": {
            "slug": "gerichtskosten-parteientschaedigung-wer-zahlt",
            "title": "Gerichtskosten und Parteientschädigung: wer zahlt",
            "meta": "Kostenvorschuss, Verteilung je nach Verfahrensausgang, unentgeltliche Rechtspflege: die Regeln der Zivilprozessordnung zu den Kosten.",
            "sections": [
                {"heading": "Die zwei Kostenkategorien", "paragraphs": [
                    "Die ZPO unterscheidet die Gerichtskosten (Gebühren des Gerichts, Kosten für Gutachten, Zeuginnen und Zeugen) von der Parteientschädigung, welche den Anwaltskosten und anderen notwendigen Auslagen entspricht, die eine Partei zur Wahrung ihrer Interessen im Verfahren aufgewendet hat (Art. 95 ZPO).",
                ]},
                {"heading": "Der Kostenvorschuss", "paragraphs": [
                    "Das Gericht kann von der klagenden Partei einen Vorschuss zur Deckung der voraussichtlichen Gerichtskosten verlangen, vor Eröffnung des Verfahrens in der Sache. Wird dieser Vorschuss nicht innert der gesetzten Frist geleistet, kann die Klage für unzulässig erklärt werden.",
                ]},
                {"heading": "Die allgemeine Verteilungsregel", "paragraphs": [
                    "Gemäss Art. 106 ZPO werden die Kosten grundsätzlich der unterliegenden Partei auferlegt. Bei teilweisem Obsiegen jeder Partei werden die Kosten anteilsmässig nach Ausgang der Sache verteilt. Das Gericht kann aus Billigkeitsgründen in bestimmten Situationen von dieser allgemeinen Regel abweichen.",
                ]},
                {"heading": "Die unentgeltliche Rechtspflege", "paragraphs": [
                    "Eine Person, die nicht über ausreichende Mittel verfügt, um die Kosten eines Prozesses zu tragen, ohne das für ihren Unterhalt notwendige Existenzminimum zu beeinträchtigen, kann unentgeltliche Rechtspflege beantragen (Art. 117 ff. ZPO), welche die Gerichtskosten ganz oder teilweise decken kann und nötigenfalls die Bestellung einer unentgeltlichen Rechtsvertretung, sofern die Sache nicht als aussichtslos erscheint.",
                ]},
            ],
            "faq": [
                {"q": "Wer trägt die Kosten, wenn ich meinen Prozess verliere?",
                 "a": "Grundsätzlich trägt die unterliegende Partei die Gerichtskosten und die Parteientschädigung der Gegenpartei (Art. 106 ZPO), unter Vorbehalt einer anteilsmässigen Verteilung bei teilweisem Obsiegen jeder Partei."},
                {"q": "Kann ich Hilfe erhalten, wenn ich nicht über die Mittel verfüge, um die Gerichtskosten zu bezahlen?",
                 "a": "Ja, die unentgeltliche Rechtspflege (Art. 117 ff. ZPO) kann die Gerichtskosten ganz oder teilweise decken und die Bestellung einer unentgeltlichen Rechtsvertretung ermöglichen, sofern Sie nicht über ausreichende Mittel verfügen und die Sache nicht aussichtslos erscheint."},
                {"q": "Was geschieht, wenn ich den vom Gericht verlangten Kostenvorschuss nicht bezahle?",
                 "a": "Das Gericht kann die Klage bei Nichtzahlung innert der gesetzten Frist für unzulässig erklären, ohne die Sache zu prüfen."},
            ],
        },
        "it": {
            "slug": "spese-giudiziarie-ripetibili-chi-paga",
            "title": "Spese giudiziarie e ripetibili: chi paga nel processo",
            "meta": "Anticipo delle spese, ripartizione secondo l'esito del processo, assistenza giudiziaria: le regole del Codice di procedura civile sulle spese.",
            "sections": [
                {"heading": "Le due categorie di spese", "paragraphs": [
                    "Il CPC distingue le spese giudiziarie (emolumenti del tribunale, spese per perizie, testimoni) dalle ripetibili, che corrispondono alle spese legali e ad altri esborsi necessari sostenuti da una parte per difendere i propri interessi nella procedura (art. 95 CPC).",
                ]},
                {"heading": "L'anticipo delle spese", "paragraphs": [
                    "Il tribunale può esigere dall'attore un anticipo destinato a coprire le spese giudiziarie presunte, prima dell'apertura della procedura sul merito. In mancanza del pagamento di tale anticipo entro il termine impartito, la domanda può essere dichiarata irricevibile.",
                ]},
                {"heading": "La regola generale di ripartizione", "paragraphs": [
                    "Secondo l'art. 106 CPC, le spese sono in linea di principio poste a carico della parte soccombente. In caso di vittoria parziale di ciascuna parte, le spese sono ripartite proporzionalmente secondo l'esito della causa. Il tribunale può discostarsi da questa regola generale per motivi di equità in determinate situazioni.",
                ]},
                {"heading": "L'assistenza giudiziaria", "paragraphs": [
                    "Una persona che non dispone di risorse sufficienti per sostenere le spese di un processo senza pregiudicare il minimo vitale necessario al proprio sostentamento può chiedere l'assistenza giudiziaria (art. 117 segg. CPC), che può coprire in tutto o in parte le spese giudiziarie e, se necessario, la designazione di un avvocato d'ufficio, a condizione che la causa non appaia priva di ogni possibilità di successo.",
                ]},
            ],
            "faq": [
                {"q": "Chi paga le spese se perdo il mio processo?",
                 "a": "In linea di principio la parte soccombente sostiene le spese giudiziarie e le ripetibili della controparte (art. 106 CPC), con riserva di una ripartizione proporzionale in caso di vittoria parziale di ciascuna parte."},
                {"q": "Posso ottenere un aiuto se non ho i mezzi per pagare le spese di giustizia?",
                 "a": "Sì, l'assistenza giudiziaria (art. 117 segg. CPC) può coprire in tutto o in parte le spese giudiziarie e permettere la designazione di un avvocato d'ufficio, a condizione di non disporre di risorse sufficienti e che la causa non appaia priva di possibilità di successo."},
                {"q": "Cosa succede se non pago l'anticipo delle spese richiesto dal tribunale?",
                 "a": "Il tribunale può, in mancanza di pagamento entro il termine impartito, dichiarare la domanda irricevibile senza esaminare il merito della controversia."},
            ],
        },
        "en": {
            "slug": "court-costs-legal-fees-who-pays",
            "title": "Court costs and legal fees: who pays in a lawsuit",
            "meta": "Advance payment of costs, allocation based on the outcome, legal aid: the Code of Civil Procedure rules on costs.",
            "sections": [
                {"heading": "The two categories of costs", "paragraphs": [
                    "The CCP distinguishes court costs (court fees, expert and witness costs) from party compensation, which corresponds to legal fees and other necessary expenses incurred by a party to defend their interests in the proceedings (art. 95 CCP).",
                ]},
                {"heading": "The advance payment of costs", "paragraphs": [
                    "The court can require the plaintiff to make an advance payment to cover the estimated court costs, before opening proceedings on the merits. If this advance is not paid within the deadline set, the claim can be declared inadmissible.",
                ]},
                {"heading": "The general allocation rule", "paragraphs": [
                    "Under art. 106 CCP, costs are in principle borne by the losing party. Where each party partially prevails, costs are allocated proportionally according to the outcome of the case. The court can deviate from this general rule on equitable grounds in certain situations.",
                ]},
                {"heading": "Legal aid", "paragraphs": [
                    "A person who does not have sufficient means to bear the costs of a lawsuit without affecting the subsistence minimum necessary for their support can apply for legal aid (art. 117 ff. CCP), which can cover all or part of the court costs and, if necessary, the appointment of a court-appointed lawyer, provided the case does not appear devoid of any chance of success.",
                ]},
            ],
            "faq": [
                {"q": "Who pays the costs if I lose my lawsuit?",
                 "a": "In principle the losing party bears the court costs and the other party's legal fees (art. 106 CCP), subject to proportional allocation where each party partially prevails."},
                {"q": "Can I get help if I don't have the means to pay court costs?",
                 "a": "Yes, legal aid (art. 117 ff. CCP) can cover all or part of the court costs and allow for the appointment of a court-appointed lawyer, provided you lack sufficient means and the case does not appear devoid of any chance of success."},
                {"q": "What happens if I don't pay the advance on costs requested by the court?",
                 "a": "The court can, if payment is not made within the deadline set, declare the claim inadmissible without examining the merits of the dispute."},
            ],
        },
    },
    "entendu-prevenu-droits-audition": {
        "domaine_id": "procedure_penale",
        "published": "2026-07-30",
        "fr": {
            "slug": "etre-entendu-prevenu-droits-audition",
            "title": "Être entendu comme prévenu : vos droits en audition",
            "meta": "Information sur les charges, droit de se taire, droit à un avocat : les garanties prévues par le Code de procédure pénale lors d'une audition.",
            "sections": [
                {"heading": "Le droit d'être informé des charges", "paragraphs": [
                    "Avant sa première audition, le prévenu doit être informé, dans une langue qu'il comprend, des faits qui lui sont reprochés et des infractions qui entrent en considération (art. 158 CPP). Cette information est une condition de validité de l'audition : à défaut, celle-ci ne peut en principe pas être exploitée contre le prévenu.",
                ]},
                {"heading": "Le droit de se taire", "paragraphs": [
                    "Le prévenu doit également être informé qu'il a le droit de refuser de déposer et de collaborer, sans que son silence puisse être retenu contre lui. Ce droit s'applique dès le premier contact avec les autorités de poursuite pénale, indépendamment du stade de la procédure.",
                ]},
                {"heading": "Le droit à un avocat", "paragraphs": [
                    "Le prévenu a le droit de faire appel à un avocat de son choix ou, s'il n'en a pas les moyens, de demander un défenseur d'office dans les cas de défense obligatoire prévus par la loi. Ce droit doit lui être signalé avant l'audition, et il peut en principe demander un report de courte durée pour organiser sa défense.",
                ]},
                {"heading": "Les conséquences d'une violation de ces droits", "paragraphs": [
                    "Une audition menée en violation de ces droits fondamentaux (absence d'information sur les charges, absence d'information sur le droit de se taire ou de faire appel à un avocat) est en principe inexploitable comme moyen de preuve, ce qui peut avoir des conséquences importantes sur la suite de la procédure pénale.",
                ]},
            ],
            "faq": [
                {"q": "Suis-je obligé de répondre aux questions de la police ou du procureur ?",
                 "a": "Non, vous avez le droit de vous taire à tout moment de la procédure, et ce silence ne peut pas être retenu contre vous (art. 158 CPP)."},
                {"q": "Ai-je droit à un avocat dès la première audition ?",
                 "a": "Oui, vous avez le droit de faire appel à un avocat de votre choix, ou de demander un défenseur d'office si vous n'en avez pas les moyens dans les cas de défense obligatoire prévus par la loi, et ce droit doit vous être signalé avant l'audition."},
                {"q": "Que se passe-t-il si ces droits ne m'ont pas été signalés avant l'audition ?",
                 "a": "L'audition menée en violation de ces garanties est en principe inexploitable comme moyen de preuve dans la procédure."},
            ],
        },
        "de": {
            "slug": "einvernahme-beschuldigte-rechte-befragung",
            "title": "Als beschuldigte Person einvernommen: Ihre Rechte",
            "meta": "Information über den Tatvorwurf, Aussageverweigerungsrecht, Recht auf eine Verteidigung: die Garantien der Strafprozessordnung bei einer Einvernahme.",
            "sections": [
                {"heading": "Das Recht auf Information über den Tatvorwurf", "paragraphs": [
                    "Vor ihrer ersten Einvernahme muss die beschuldigte Person in einer ihr verständlichen Sprache über den ihr vorgeworfenen Sachverhalt und die in Betracht kommenden Straftatbestände informiert werden (Art. 158 StPO). Diese Information ist eine Gültigkeitsvoraussetzung der Einvernahme: fehlt sie, kann diese grundsätzlich nicht gegen die beschuldigte Person verwertet werden.",
                ]},
                {"heading": "Das Aussageverweigerungsrecht", "paragraphs": [
                    "Die beschuldigte Person muss zudem darüber informiert werden, dass sie die Aussage und die Mitwirkung verweigern darf, ohne dass ihr Schweigen gegen sie verwendet werden kann. Dieses Recht gilt vom ersten Kontakt mit den Strafverfolgungsbehörden an, unabhängig vom Verfahrensstadium.",
                ]},
                {"heading": "Das Recht auf eine Verteidigung", "paragraphs": [
                    "Die beschuldigte Person hat das Recht, eine Anwältin oder einen Anwalt ihrer Wahl beizuziehen oder, wenn sie nicht über die nötigen Mittel verfügt, in den Fällen der notwendigen Verteidigung eine amtliche Verteidigung zu verlangen. Dieses Recht muss ihr vor der Einvernahme mitgeteilt werden, und sie kann grundsätzlich eine kurze Verschiebung verlangen, um ihre Verteidigung zu organisieren.",
                ]},
                {"heading": "Die Folgen einer Verletzung dieser Rechte", "paragraphs": [
                    "Eine unter Verletzung dieser Grundrechte durchgeführte Einvernahme (fehlende Information über den Tatvorwurf, fehlende Information über das Aussageverweigerungsrecht oder das Recht auf eine Anwältin oder einen Anwalt) ist grundsätzlich als Beweismittel unverwertbar, was erhebliche Folgen für den weiteren Verlauf des Strafverfahrens haben kann.",
                ]},
            ],
            "faq": [
                {"q": "Bin ich verpflichtet, die Fragen der Polizei oder der Staatsanwaltschaft zu beantworten?",
                 "a": "Nein, Sie haben zu jedem Zeitpunkt des Verfahrens das Recht zu schweigen, und dieses Schweigen darf nicht gegen Sie verwendet werden (Art. 158 StPO)."},
                {"q": "Habe ich bereits bei der ersten Einvernahme Anspruch auf eine Anwältin oder einen Anwalt?",
                 "a": "Ja, Sie haben das Recht, eine Anwältin oder einen Anwalt Ihrer Wahl beizuziehen, oder eine amtliche Verteidigung zu verlangen, wenn Sie nicht über die nötigen Mittel verfügen, in den Fällen der notwendigen Verteidigung, und dieses Recht muss Ihnen vor der Einvernahme mitgeteilt werden."},
                {"q": "Was geschieht, wenn mir diese Rechte vor der Einvernahme nicht mitgeteilt wurden?",
                 "a": "Die unter Verletzung dieser Garantien durchgeführte Einvernahme ist grundsätzlich als Beweismittel im Verfahren unverwertbar."},
            ],
        },
        "it": {
            "slug": "essere-sentito-imputato-diritti-interrogatorio",
            "title": "Essere sentito come imputato: i vostri diritti",
            "meta": "Informazione sui capi d'accusa, diritto al silenzio, diritto a un difensore: le garanzie previste dal Codice di procedura penale durante l'interrogatorio.",
            "sections": [
                {"heading": "Il diritto ad essere informato dei capi d'accusa", "paragraphs": [
                    "Prima del primo interrogatorio, l'imputato deve essere informato, in una lingua che comprende, dei fatti che gli vengono rimproverati e dei reati che entrano in considerazione (art. 158 CPP). Questa informazione è una condizione di validità dell'interrogatorio: in sua mancanza, questo non può in linea di principio essere utilizzato contro l'imputato.",
                ]},
                {"heading": "Il diritto al silenzio", "paragraphs": [
                    "L'imputato deve inoltre essere informato del suo diritto di rifiutare di deporre e di collaborare, senza che il suo silenzio possa essere ritenuto contro di lui. Questo diritto si applica dal primo contatto con le autorità di perseguimento penale, indipendentemente dallo stadio della procedura.",
                ]},
                {"heading": "Il diritto a un difensore", "paragraphs": [
                    "L'imputato ha il diritto di fare appello a un avvocato di sua scelta o, se non ne ha i mezzi, di chiedere un difensore d'ufficio nei casi di difesa obbligatoria previsti dalla legge. Questo diritto deve essergli segnalato prima dell'interrogatorio, e può in linea di principio chiedere un breve rinvio per organizzare la propria difesa.",
                ]},
                {"heading": "Le conseguenze di una violazione di questi diritti", "paragraphs": [
                    "Un interrogatorio condotto in violazione di questi diritti fondamentali (assenza di informazione sui capi d'accusa, assenza di informazione sul diritto al silenzio o sul diritto a un avvocato) è in linea di principio inutilizzabile come mezzo di prova, il che può avere conseguenze importanti sul seguito della procedura penale.",
                ]},
            ],
            "faq": [
                {"q": "Sono obbligato a rispondere alle domande della polizia o del pubblico ministero?",
                 "a": "No, avete il diritto di tacere in qualsiasi momento della procedura, e questo silenzio non può essere ritenuto contro di voi (art. 158 CPP)."},
                {"q": "Ho diritto a un avvocato già dal primo interrogatorio?",
                 "a": "Sì, avete il diritto di fare appello a un avvocato di vostra scelta, o di chiedere un difensore d'ufficio se non ne avete i mezzi nei casi di difesa obbligatoria previsti dalla legge, e questo diritto deve esservi segnalato prima dell'interrogatorio."},
                {"q": "Cosa succede se questi diritti non mi sono stati segnalati prima dell'interrogatorio?",
                 "a": "L'interrogatorio condotto in violazione di queste garanzie è in linea di principio inutilizzabile come mezzo di prova nella procedura."},
            ],
        },
        "en": {
            "slug": "being-heard-accused-rights-interrogation",
            "title": "Being questioned as the accused: your rights",
            "meta": "Information on the charges, right to remain silent, right to a defence lawyer: the guarantees under the Code of Criminal Procedure during questioning.",
            "sections": [
                {"heading": "The right to be informed of the charges", "paragraphs": [
                    "Before their first interview, the accused must be informed, in a language they understand, of the facts alleged against them and the offences under consideration (art. 158 CCP). This information is a condition for the validity of the interview: without it, the interview in principle cannot be used against the accused.",
                ]},
                {"heading": "The right to remain silent", "paragraphs": [
                    "The accused must also be informed of their right to refuse to make a statement and to cooperate, without their silence being held against them. This right applies from the first contact with the criminal prosecution authorities, regardless of the stage of the proceedings.",
                ]},
                {"heading": "The right to a defence lawyer", "paragraphs": [
                    "The accused has the right to call on a lawyer of their choice or, if they lack the means, to request a court-appointed defence lawyer in the cases of mandatory defence provided by law. This right must be pointed out to them before questioning, and they can in principle request a short postponement to organise their defence.",
                ]},
                {"heading": "The consequences of a violation of these rights", "paragraphs": [
                    "An interview conducted in violation of these fundamental rights (no information on the charges, no information on the right to remain silent or the right to a lawyer) is in principle inadmissible as evidence, which can have significant consequences for the rest of the criminal proceedings.",
                ]},
            ],
            "faq": [
                {"q": "Am I required to answer questions from the police or the public prosecutor?",
                 "a": "No, you have the right to remain silent at any stage of the proceedings, and this silence cannot be held against you (art. 158 CCP)."},
                {"q": "Am I entitled to a lawyer from the first interview?",
                 "a": "Yes, you have the right to call on a lawyer of your choice, or to request a court-appointed defence lawyer if you lack the means in cases of mandatory defence provided by law, and this right must be pointed out to you before questioning."},
                {"q": "What happens if these rights were not pointed out to me before questioning?",
                 "a": "An interview conducted in violation of these guarantees is in principle inadmissible as evidence in the proceedings."},
            ],
        },
    },
    "plainte-penale-delais-difference-denonciation": {
        "domaine_id": "procedure_penale",
        "published": "2026-07-30",
        "fr": {
            "slug": "plainte-penale-delais-difference-denonciation",
            "title": "Plainte pénale : délais et différence avec la dénonciation",
            "meta": "Délai de trois mois pour porter plainte, infractions poursuivies sur plainte ou d'office : les distinctions posées par le Code pénal.",
            "sections": [
                {"heading": "Ce qu'est une plainte pénale", "paragraphs": [
                    "La plainte pénale est la déclaration par laquelle le lésé exprime sa volonté que l'auteur d'une infraction soit poursuivi. Elle est indispensable pour certaines infractions, dites poursuivies sur plainte, que le ministère public ne peut instruire que si le lésé la dépose (art. 30 ss CP).",
                ]},
                {"heading": "Le délai pour porter plainte", "paragraphs": [
                    "L'art. 31 CP fixe un délai de trois mois pour déposer plainte, à compter du jour où l'ayant droit a connu l'auteur de l'infraction. Ce délai est un délai de péremption : passé ce délai, le droit de porter plainte pour cette infraction s'éteint définitivement.",
                ]},
                {"heading": "La différence avec la dénonciation", "paragraphs": [
                    "La dénonciation, contrairement à la plainte, peut être faite par n'importe quelle personne ayant connaissance d'une infraction, et concerne principalement les infractions poursuivies d'office, pour lesquelles le ministère public doit agir dès qu'il a connaissance des faits, sans qu'une manifestation de volonté du lésé soit nécessaire.",
                ]},
                {"heading": "Le retrait de la plainte", "paragraphs": [
                    "Une plainte peut en principe être retirée tant qu'un jugement de première instance n'a pas été rendu, ce qui met fin à la poursuite pour l'infraction concernée, sauf accord contraire entre le plaignant et la personne visée par le retrait dans certains cas prévus par la loi (art. 33 CP).",
                ]},
            ],
            "faq": [
                {"q": "Dans quel délai dois-je porter plainte ?",
                 "a": "Dans les trois mois à compter du jour où vous avez connu l'auteur de l'infraction (art. 31 CP). Passé ce délai, le droit de porter plainte pour cette infraction s'éteint définitivement."},
                {"q": "Quelle est la différence entre une plainte et une dénonciation ?",
                 "a": "La plainte est réservée au lésé et nécessaire pour les infractions poursuivies sur plainte, tandis que la dénonciation peut être faite par n'importe qui et concerne surtout les infractions poursuivies d'office, pour lesquelles aucune manifestation de volonté du lésé n'est requise."},
                {"q": "Puis-je retirer ma plainte après l'avoir déposée ?",
                 "a": "Oui, en principe tant qu'un jugement de première instance n'a pas été rendu, ce qui met fin à la poursuite pour l'infraction concernée, sous réserve de règles particulières dans certains cas (art. 33 CP)."},
            ],
        },
        "de": {
            "slug": "strafantrag-fristen-unterschied-anzeige",
            "title": "Strafantrag: Fristen und Unterschied zur Strafanzeige",
            "meta": "Dreimonatige Antragsfrist, Offizial- und Antragsdelikte: die vom Strafgesetzbuch vorgesehenen Unterscheidungen.",
            "sections": [
                {"heading": "Was ein Strafantrag ist", "paragraphs": [
                    "Der Strafantrag ist die Erklärung, mit der die geschädigte Person ihren Willen zum Ausdruck bringt, dass die Täterin oder der Täter einer Straftat verfolgt wird. Er ist für bestimmte Straftaten, sogenannte Antragsdelikte, unerlässlich, welche die Staatsanwaltschaft nur untersuchen kann, wenn die geschädigte Person ihn stellt (Art. 30 ff. StGB).",
                ]},
                {"heading": "Die Frist zur Stellung des Strafantrags", "paragraphs": [
                    "Art. 31 StGB setzt eine Frist von drei Monaten für die Stellung des Strafantrags, ab dem Tag, an dem die antragsberechtigte Person von der Täterin oder dem Täter Kenntnis erhalten hat. Diese Frist ist eine Verwirkungsfrist: nach ihrem Ablauf erlischt das Antragsrecht für diese Straftat endgültig.",
                ]},
                {"heading": "Der Unterschied zur Strafanzeige", "paragraphs": [
                    "Die Strafanzeige kann im Gegensatz zum Strafantrag von jeder Person erstattet werden, die von einer Straftat Kenntnis hat, und betrifft hauptsächlich Offizialdelikte, für welche die Staatsanwaltschaft handeln muss, sobald sie vom Sachverhalt Kenntnis erlangt, ohne dass eine Willensäusserung der geschädigten Person erforderlich wäre.",
                ]},
                {"heading": "Der Rückzug des Strafantrags", "paragraphs": [
                    "Ein Strafantrag kann grundsätzlich zurückgezogen werden, solange kein erstinstanzliches Urteil ergangen ist, was die Verfolgung der betreffenden Straftat beendet, vorbehältlich einer gegenteiligen Vereinbarung zwischen der antragstellenden Person und der vom Rückzug betroffenen Person in bestimmten gesetzlich vorgesehenen Fällen (Art. 33 StGB).",
                ]},
            ],
            "faq": [
                {"q": "Innert welcher Frist muss ich Strafantrag stellen?",
                 "a": "Innert drei Monaten ab dem Tag, an dem Sie von der Täterin oder dem Täter Kenntnis erhalten haben (Art. 31 StGB). Nach Ablauf dieser Frist erlischt das Antragsrecht für diese Straftat endgültig."},
                {"q": "Was ist der Unterschied zwischen einem Strafantrag und einer Strafanzeige?",
                 "a": "Der Strafantrag ist der geschädigten Person vorbehalten und für Antragsdelikte erforderlich, während die Strafanzeige von jeder Person erstattet werden kann und hauptsächlich Offizialdelikte betrifft, für welche keine Willensäusserung der geschädigten Person erforderlich ist."},
                {"q": "Kann ich meinen Strafantrag nach dessen Stellung zurückziehen?",
                 "a": "Ja, grundsätzlich solange kein erstinstanzliches Urteil ergangen ist, was die Verfolgung der betreffenden Straftat beendet, vorbehältlich besonderer Regeln in bestimmten Fällen (Art. 33 StGB)."},
            ],
        },
        "it": {
            "slug": "querela-penale-termini-differenza-denuncia",
            "title": "Querela penale: termini e differenza con la denuncia",
            "meta": "Termine di tre mesi per sporgere querela, reati perseguibili d'ufficio o a querela: le distinzioni poste dal Codice penale.",
            "sections": [
                {"heading": "Cos'è la querela penale", "paragraphs": [
                    "La querela penale è la dichiarazione con cui il leso esprime la propria volontà che l'autore di un reato sia perseguito. È indispensabile per determinati reati, detti perseguibili a querela, che il pubblico ministero può istruire solo se il leso la sporge (art. 30 segg. CP).",
                ]},
                {"heading": "Il termine per sporgere querela", "paragraphs": [
                    "L'art. 31 CP fissa un termine di tre mesi per sporgere querela, a decorrere dal giorno in cui l'avente diritto ha conosciuto l'autore del reato. Questo termine è un termine di perenzione: trascorso tale termine, il diritto di querela per tale reato si estingue definitivamente.",
                ]},
                {"heading": "La differenza con la denuncia", "paragraphs": [
                    "La denuncia, a differenza della querela, può essere fatta da qualsiasi persona a conoscenza di un reato, e riguarda principalmente i reati perseguibili d'ufficio, per i quali il pubblico ministero deve agire non appena viene a conoscenza dei fatti, senza che sia necessaria una manifestazione di volontà del leso.",
                ]},
                {"heading": "Il ritiro della querela", "paragraphs": [
                    "Una querela può in linea di principio essere ritirata finché non è stata resa una sentenza di primo grado, il che pone fine al perseguimento del reato in questione, salvo accordo contrario tra il querelante e la persona interessata dal ritiro in determinati casi previsti dalla legge (art. 33 CP).",
                ]},
            ],
            "faq": [
                {"q": "Entro quale termine devo sporgere querela?",
                 "a": "Entro tre mesi dal giorno in cui avete conosciuto l'autore del reato (art. 31 CP). Trascorso questo termine, il diritto di querela per tale reato si estingue definitivamente."},
                {"q": "Qual è la differenza tra una querela e una denuncia?",
                 "a": "La querela è riservata al leso ed è necessaria per i reati perseguibili a querela, mentre la denuncia può essere fatta da chiunque e riguarda principalmente i reati perseguibili d'ufficio, per i quali non è richiesta alcuna manifestazione di volontà del leso."},
                {"q": "Posso ritirare la mia querela dopo averla sporta?",
                 "a": "Sì, in linea di principio finché non è stata resa una sentenza di primo grado, il che pone fine al perseguimento del reato in questione, salvo regole particolari in determinati casi (art. 33 CP)."},
            ],
        },
        "en": {
            "slug": "criminal-complaint-deadlines-difference-report",
            "title": "Criminal complaint: deadlines and difference from a report",
            "meta": "Three-month deadline to file a complaint, offences prosecuted ex officio or on complaint: the distinctions set by the Criminal Code.",
            "sections": [
                {"heading": "What a criminal complaint is", "paragraphs": [
                    "A criminal complaint is the declaration by which the injured party expresses their wish that the perpetrator of an offence be prosecuted. It is essential for certain offences, known as offences prosecuted on complaint, which the public prosecutor can only investigate if the injured party files it (art. 30 ff. CC/PC).",
                ]},
                {"heading": "The deadline to file a complaint", "paragraphs": [
                    "Art. 31 CC/PC sets a three-month deadline to file a complaint, from the day the entitled person became aware of the perpetrator. This is a forfeiture deadline: once it has passed, the right to file a complaint for that offence is permanently extinguished.",
                ]},
                {"heading": "The difference from a report", "paragraphs": [
                    "A report, unlike a complaint, can be made by anyone aware of an offence, and mainly concerns offences prosecuted ex officio, for which the public prosecutor must act as soon as it becomes aware of the facts, without any expression of will from the injured party being necessary.",
                ]},
                {"heading": "Withdrawing a complaint", "paragraphs": [
                    "A complaint can in principle be withdrawn as long as no first-instance judgment has been issued, which ends prosecution for the offence concerned, subject to a contrary agreement between the complainant and the person affected by the withdrawal in certain cases provided by law (art. 33 CC/PC).",
                ]},
            ],
            "faq": [
                {"q": "Within what deadline must I file a criminal complaint?",
                 "a": "Within three months from the day you became aware of the perpetrator (art. 31 CC/PC). Once this deadline has passed, the right to file a complaint for that offence is permanently extinguished."},
                {"q": "What is the difference between a complaint and a report?",
                 "a": "A complaint is reserved to the injured party and is necessary for offences prosecuted on complaint, while a report can be made by anyone and mainly concerns offences prosecuted ex officio, for which no expression of will from the injured party is required."},
                {"q": "Can I withdraw my complaint after filing it?",
                 "a": "Yes, in principle as long as no first-instance judgment has been issued, which ends prosecution for the offence concerned, subject to specific rules in certain cases (art. 33 CC/PC)."},
            ],
        },
    },
    "mediation-familiale-quand-pourquoi": {
        "domaine_id": "mediation",
        "published": "2026-07-30",
        "fr": {
            "slug": "mediation-familiale-quand-pourquoi-y-recourir",
            "title": "Médiation familiale : quand et pourquoi y recourir",
            "meta": "Résoudre un conflit familial hors du tribunal, rôle du médiateur, articulation avec la procédure judiciaire : ce que prévoit le CPC.",
            "sections": [
                {"heading": "Ce qu'est la médiation familiale", "paragraphs": [
                    "La médiation familiale est un processus volontaire dans lequel un tiers neutre et impartial, le médiateur, aide les parties (couple en séparation, parents en désaccord sur la garde des enfants) à trouver elles-mêmes une solution à leur conflit, plutôt que de la faire trancher par un juge.",
                ]},
                {"heading": "Le rôle du tribunal", "paragraphs": [
                    "Le CPC (art. 214-218) permet au tribunal saisi d'un litige familial de suggérer aux parties de recourir à la médiation, sans pouvoir toutefois les y contraindre : la médiation reste un processus fondé sur la volonté des parties d'y participer et de s'y engager de bonne foi.",
                ]},
                {"heading": "Les avantages de la médiation", "paragraphs": [
                    "La médiation permet souvent de préserver la relation entre les parties, particulièrement importante lorsque des enfants sont concernés et que les parents devront continuer à collaborer après la séparation. Elle est en principe plus rapide et moins coûteuse qu'une procédure judiciaire contentieuse.",
                ]},
                {"heading": "L'homologation de l'accord", "paragraphs": [
                    "Un accord trouvé en médiation portant sur des questions comme la garde des enfants ou la contribution d'entretien doit en principe être soumis au tribunal ou à l'autorité compétente pour être homologué et devenir juridiquement contraignant, le tribunal vérifiant que l'accord respecte le bien de l'enfant et l'ordre public.",
                ]},
            ],
            "faq": [
                {"q": "Le tribunal peut-il m'obliger à faire une médiation familiale ?",
                 "a": "Non, la médiation reste un processus volontaire : le tribunal peut la suggérer (art. 214 ss CPC), mais ne peut pas contraindre les parties à y participer contre leur gré."},
                {"q": "Un accord trouvé en médiation est-il juridiquement contraignant ?",
                 "a": "Il le devient une fois homologué par le tribunal ou l'autorité compétente, qui vérifie notamment que l'accord respecte le bien de l'enfant s'il porte sur des questions parentales."},
                {"q": "La médiation familiale convient-elle à toutes les situations ?",
                 "a": "Non, elle suppose que les deux parties soient en mesure de dialoguer de bonne foi sur un pied d'égalité ; elle n'est en principe pas adaptée en présence de violences conjugales ou d'un déséquilibre de pouvoir important entre les parties."},
            ],
        },
        "de": {
            "slug": "familienmediation-wann-warum-nutzen",
            "title": "Familienmediation: wann und warum sie nutzen",
            "meta": "Einen Familienkonflikt ausserhalb des Gerichts lösen, Rolle der Mediatorin oder des Mediators, Verhältnis zum Gerichtsverfahren gemäss ZPO.",
            "sections": [
                {"heading": "Was Familienmediation ist", "paragraphs": [
                    "Die Familienmediation ist ein freiwilliger Prozess, bei dem eine neutrale und unparteiische dritte Person, die Mediatorin oder der Mediator, den Parteien (sich trennendes Paar, uneinige Eltern bezüglich der Kinderbetreuung) hilft, selbst eine Lösung für ihren Konflikt zu finden, statt sie von einer Richterin oder einem Richter entscheiden zu lassen.",
                ]},
                {"heading": "Die Rolle des Gerichts", "paragraphs": [
                    "Die ZPO (Art. 214-218) erlaubt dem mit einer Familienstreitigkeit befassten Gericht, den Parteien die Mediation vorzuschlagen, ohne sie jedoch dazu zwingen zu können: die Mediation bleibt ein Prozess, der auf dem Willen der Parteien beruht, daran teilzunehmen und sich nach Treu und Glauben darauf einzulassen.",
                ]},
                {"heading": "Die Vorteile der Mediation", "paragraphs": [
                    "Die Mediation erlaubt es häufig, die Beziehung zwischen den Parteien zu wahren, was besonders wichtig ist, wenn Kinder betroffen sind und die Eltern auch nach der Trennung weiter zusammenarbeiten müssen. Sie ist grundsätzlich rascher und kostengünstiger als ein streitiges Gerichtsverfahren.",
                ]},
                {"heading": "Die Homologation der Vereinbarung", "paragraphs": [
                    "Eine in der Mediation erzielte Vereinbarung über Fragen wie die Kinderbetreuung oder den Unterhaltsbeitrag muss grundsätzlich dem Gericht oder der zuständigen Behörde zur Genehmigung vorgelegt werden, um rechtlich verbindlich zu werden, wobei das Gericht prüft, ob die Vereinbarung dem Kindeswohl und der öffentlichen Ordnung entspricht.",
                ]},
            ],
            "faq": [
                {"q": "Kann mich das Gericht zu einer Familienmediation zwingen?",
                 "a": "Nein, die Mediation bleibt ein freiwilliger Prozess: das Gericht kann sie vorschlagen (Art. 214 ff. ZPO), die Parteien aber nicht gegen ihren Willen dazu verpflichten."},
                {"q": "Ist eine in der Mediation erzielte Vereinbarung rechtlich verbindlich?",
                 "a": "Sie wird es nach der Homologation durch das Gericht oder die zuständige Behörde, welche namentlich prüft, ob die Vereinbarung dem Kindeswohl entspricht, sofern sie elterliche Fragen betrifft."},
                {"q": "Eignet sich die Familienmediation für alle Situationen?",
                 "a": "Nein, sie setzt voraus, dass beide Parteien nach Treu und Glauben auf gleicher Augenhöhe miteinander sprechen können; sie ist grundsätzlich nicht geeignet bei häuslicher Gewalt oder einem erheblichen Machtungleichgewicht zwischen den Parteien."},
            ],
        },
        "it": {
            "slug": "mediazione-familiare-quando-perche-ricorrere",
            "title": "Mediazione familiare: quando e perché ricorrervi",
            "meta": "Risolvere un conflitto familiare fuori dal tribunale, ruolo del mediatore, articolazione con la procedura giudiziaria secondo il CPC.",
            "sections": [
                {"heading": "Cos'è la mediazione familiare", "paragraphs": [
                    "La mediazione familiare è un processo volontario in cui un terzo neutrale e imparziale, il mediatore, aiuta le parti (coppia in separazione, genitori in disaccordo sulla custodia dei figli) a trovare esse stesse una soluzione al loro conflitto, piuttosto che farla decidere da un giudice.",
                ]},
                {"heading": "Il ruolo del tribunale", "paragraphs": [
                    "Il CPC (art. 214-218) permette al tribunale adito con una controversia familiare di suggerire alle parti di ricorrere alla mediazione, senza tuttavia poterle costringere: la mediazione resta un processo fondato sulla volontà delle parti di parteciparvi e di impegnarvisi in buona fede.",
                ]},
                {"heading": "I vantaggi della mediazione", "paragraphs": [
                    "La mediazione permette spesso di preservare la relazione tra le parti, particolarmente importante quando sono coinvolti dei figli e i genitori dovranno continuare a collaborare dopo la separazione. È in linea di principio più rapida e meno costosa di una procedura giudiziaria contenziosa.",
                ]},
                {"heading": "L'omologazione dell'accordo", "paragraphs": [
                    "Un accordo trovato in mediazione riguardante questioni come la custodia dei figli o il contributo di mantenimento deve in linea di principio essere sottoposto al tribunale o all'autorità competente per essere omologato e diventare giuridicamente vincolante, con il tribunale che verifica che l'accordo rispetti il bene del figlio e l'ordine pubblico.",
                ]},
            ],
            "faq": [
                {"q": "Il tribunale può obbligarmi a fare una mediazione familiare?",
                 "a": "No, la mediazione resta un processo volontario: il tribunale può suggerirla (art. 214 segg. CPC), ma non può costringere le parti a parteciparvi contro la loro volontà."},
                {"q": "Un accordo trovato in mediazione è giuridicamente vincolante?",
                 "a": "Lo diventa una volta omologato dal tribunale o dall'autorità competente, che verifica in particolare che l'accordo rispetti il bene del figlio se riguarda questioni genitoriali."},
                {"q": "La mediazione familiare è adatta a tutte le situazioni?",
                 "a": "No, presuppone che entrambe le parti siano in grado di dialogare in buona fede su un piano di parità; non è in linea di principio adatta in presenza di violenza domestica o di un notevole squilibrio di potere tra le parti."},
            ],
        },
        "en": {
            "slug": "family-mediation-when-why-use-it",
            "title": "Family mediation: when and why to use it",
            "meta": "Resolving a family conflict outside court, the mediator's role, its relationship with court proceedings under the Code of Civil Procedure.",
            "sections": [
                {"heading": "What family mediation is", "paragraphs": [
                    "Family mediation is a voluntary process in which a neutral, impartial third party, the mediator, helps the parties (a separating couple, parents disagreeing over child custody) find a solution to their conflict themselves, rather than having it decided by a judge.",
                ]},
                {"heading": "The court's role", "paragraphs": [
                    "The CCP (art. 214-218) allows a court dealing with a family dispute to suggest mediation to the parties, without being able to compel them to do so: mediation remains a process based on the parties' willingness to take part and engage in it in good faith.",
                ]},
                {"heading": "The benefits of mediation", "paragraphs": [
                    "Mediation often helps preserve the relationship between the parties, which is particularly important when children are involved and the parents will need to keep cooperating after the separation. It is in principle faster and less costly than contested court proceedings.",
                ]},
                {"heading": "Approval of the agreement", "paragraphs": [
                    "An agreement reached through mediation on matters such as child custody or maintenance must in principle be submitted to the court or the competent authority for approval to become legally binding, with the court checking that the agreement respects the child's best interests and public policy.",
                ]},
            ],
            "faq": [
                {"q": "Can the court force me into family mediation?",
                 "a": "No, mediation remains a voluntary process: the court can suggest it (art. 214 ff. CCP), but cannot compel the parties to take part against their will."},
                {"q": "Is an agreement reached through mediation legally binding?",
                 "a": "It becomes so once approved by the court or the competent authority, which checks in particular that the agreement respects the child's best interests if it concerns parental matters."},
                {"q": "Is family mediation suitable for every situation?",
                 "a": "No, it requires both parties to be able to discuss matters in good faith on an equal footing; it is in principle not suitable in the presence of domestic violence or a significant power imbalance between the parties."},
            ],
        },
    },
    "mediation-commerciale-alternative-proces": {
        "domaine_id": "mediation",
        "published": "2026-07-30",
        "fr": {
            "slug": "mediation-commerciale-alternative-proces-entreprises",
            "title": "Médiation commerciale : alternative au procès",
            "meta": "Résoudre un litige entre entreprises hors tribunal, confidentialité, rapidité : les avantages de la médiation commerciale en Suisse.",
            "sections": [
                {"heading": "Un mode de résolution volontaire", "paragraphs": [
                    "Contrairement à la médiation familiale, la médiation commerciale entre entreprises ne fait pas l'objet d'un cadre légal spécifique dédié dans le CPC : elle repose principalement sur l'accord des parties de recourir à un médiateur, souvent prévu par une clause contractuelle de médiation, ou décidée d'un commun accord une fois le litige survenu.",
                ]},
                {"heading": "Les avantages pour les entreprises", "paragraphs": [
                    "La médiation commerciale offre une confidentialité que la procédure judiciaire, en principe publique, ne garantit pas toujours, un contrôle des parties sur l'issue du litige plutôt qu'une décision imposée par un tiers, et une rapidité généralement supérieure à celle d'un procès civil, ce qui permet souvent de préserver une relation d'affaires que les parties souhaitent poursuivre.",
                ]},
                {"heading": "L'articulation avec l'arbitrage", "paragraphs": [
                    "De nombreux contrats commerciaux, notamment internationaux, prévoient des clauses combinant médiation et arbitrage, la médiation intervenant comme tentative préalable de règlement amiable avant le recours, en cas d'échec, à une procédure d'arbitrage contraignante devant un tribunal arbitral.",
                ]},
                {"heading": "La force de l'accord trouvé", "paragraphs": [
                    "Un accord trouvé en médiation commerciale prend en principe la forme d'un contrat de transaction entre les parties, dont le caractère contraignant repose sur les règles générales du droit des contrats, et non sur une homologation judiciaire systématique comme c'est parfois le cas en matière familiale.",
                ]},
            ],
            "faq": [
                {"q": "Une entreprise peut-elle être obligée de recourir à la médiation ?",
                 "a": "En principe non, sauf si une clause contractuelle de médiation, librement acceptée au moment de la signature du contrat, prévoit cette étape préalable en cas de litige."},
                {"q": "Un accord de médiation commerciale a-t-il la même force qu'un jugement ?",
                 "a": "Il prend en principe la forme d'un contrat de transaction entre les parties, contraignant selon les règles générales du droit des contrats, mais ne bénéficie pas automatiquement de la force exécutoire d'un jugement sauf démarche complémentaire prévue par la loi."},
                {"q": "Pourquoi combiner médiation et arbitrage dans un contrat commercial ?",
                 "a": "Pour tenter d'abord un règlement amiable rapide et confidentiel par la médiation, tout en conservant, en cas d'échec, une procédure d'arbitrage contraignante permettant de trancher définitivement le litige sans passer par les tribunaux étatiques."},
            ],
        },
        "de": {
            "slug": "wirtschaftsmediation-alternative-zum-prozess",
            "title": "Wirtschaftsmediation: Alternative zum Prozess",
            "meta": "Eine Streitigkeit zwischen Unternehmen ausserhalb des Gerichts lösen, Vertraulichkeit, Schnelligkeit: die Vorteile der Wirtschaftsmediation in der Schweiz.",
            "sections": [
                {"heading": "Ein freiwilliges Streitbeilegungsmittel", "paragraphs": [
                    "Im Gegensatz zur Familienmediation ist die Wirtschaftsmediation zwischen Unternehmen nicht Gegenstand eines besonderen gesetzlichen Rahmens in der ZPO: sie beruht hauptsächlich auf der Vereinbarung der Parteien, eine Mediatorin oder einen Mediator beizuziehen, häufig vorgesehen durch eine vertragliche Mediationsklausel, oder gemeinsam beschlossen, sobald der Streit entstanden ist.",
                ]},
                {"heading": "Die Vorteile für Unternehmen", "paragraphs": [
                    "Die Wirtschaftsmediation bietet eine Vertraulichkeit, die das grundsätzlich öffentliche Gerichtsverfahren nicht immer gewährleistet, eine Kontrolle der Parteien über den Ausgang des Streits statt eines von einer dritten Person auferlegten Entscheids, sowie eine im Allgemeinen höhere Schnelligkeit als bei einem Zivilprozess, was es häufig erlaubt, eine Geschäftsbeziehung zu erhalten, welche die Parteien fortsetzen möchten.",
                ]},
                {"heading": "Das Zusammenspiel mit der Schiedsgerichtsbarkeit", "paragraphs": [
                    "Zahlreiche Wirtschaftsverträge, insbesondere internationale, sehen Klauseln vor, welche Mediation und Schiedsgerichtsbarkeit kombinieren, wobei die Mediation als vorgängiger Versuch einer gütlichen Streitbeilegung dient, bevor bei Scheitern auf ein verbindliches Schiedsverfahren vor einem Schiedsgericht zurückgegriffen wird.",
                ]},
                {"heading": "Die Verbindlichkeit der erzielten Vereinbarung", "paragraphs": [
                    "Eine in der Wirtschaftsmediation erzielte Vereinbarung nimmt grundsätzlich die Form eines Vergleichsvertrags zwischen den Parteien an, dessen Verbindlichkeit sich aus den allgemeinen Regeln des Vertragsrechts ergibt, und nicht aus einer systematischen gerichtlichen Homologation wie dies teilweise im Familienrecht der Fall ist.",
                ]},
            ],
            "faq": [
                {"q": "Kann ein Unternehmen zur Mediation gezwungen werden?",
                 "a": "Grundsätzlich nicht, ausser eine vertragliche Mediationsklausel, die bei Vertragsabschluss frei akzeptiert wurde, sieht diesen vorgängigen Schritt bei einer Streitigkeit vor."},
                {"q": "Hat eine wirtschaftsmediative Vereinbarung dieselbe Kraft wie ein Urteil?",
                 "a": "Sie nimmt grundsätzlich die Form eines Vergleichsvertrags zwischen den Parteien an, verbindlich nach den allgemeinen Regeln des Vertragsrechts, geniesst aber nicht automatisch die Vollstreckbarkeit eines Urteils, ausser bei einem zusätzlichen, gesetzlich vorgesehenen Schritt."},
                {"q": "Warum Mediation und Schiedsgerichtsbarkeit in einem Wirtschaftsvertrag kombinieren?",
                 "a": "Um zunächst eine rasche und vertrauliche gütliche Einigung durch Mediation zu versuchen, wobei bei Scheitern ein verbindliches Schiedsverfahren erhalten bleibt, das erlaubt, den Streit endgültig zu entscheiden, ohne die staatlichen Gerichte anzurufen."},
            ],
        },
        "it": {
            "slug": "mediazione-commerciale-alternativa-processo",
            "title": "Mediazione commerciale: alternativa al processo",
            "meta": "Risolvere una controversia tra imprese fuori dal tribunale, confidenzialità, rapidità: i vantaggi della mediazione commerciale in Svizzera.",
            "sections": [
                {"heading": "Un modo di risoluzione volontario", "paragraphs": [
                    "A differenza della mediazione familiare, la mediazione commerciale tra imprese non è oggetto di un quadro legale specifico dedicato nel CPC: si fonda principalmente sull'accordo delle parti di ricorrere a un mediatore, spesso previsto da una clausola contrattuale di mediazione, o deciso di comune accordo una volta sorta la controversia.",
                ]},
                {"heading": "I vantaggi per le imprese", "paragraphs": [
                    "La mediazione commerciale offre una confidenzialità che la procedura giudiziaria, in linea di principio pubblica, non garantisce sempre, un controllo delle parti sull'esito della controversia piuttosto che una decisione imposta da un terzo, e una rapidità generalmente superiore a quella di un processo civile, il che permette spesso di preservare un rapporto d'affari che le parti desiderano proseguire.",
                ]},
                {"heading": "L'articolazione con l'arbitrato", "paragraphs": [
                    "Numerosi contratti commerciali, in particolare internazionali, prevedono clausole che combinano mediazione e arbitrato, con la mediazione che interviene come tentativo preliminare di composizione amichevole prima del ricorso, in caso di fallimento, a una procedura arbitrale vincolante davanti a un tribunale arbitrale.",
                ]},
                {"heading": "La forza dell'accordo trovato", "paragraphs": [
                    "Un accordo trovato in mediazione commerciale assume in linea di principio la forma di un contratto di transazione tra le parti, il cui carattere vincolante si fonda sulle regole generali del diritto dei contratti, e non su un'omologazione giudiziaria sistematica come talvolta avviene in materia familiare.",
                ]},
            ],
            "faq": [
                {"q": "Un'impresa può essere obbligata a ricorrere alla mediazione?",
                 "a": "In linea di principio no, salvo se una clausola contrattuale di mediazione, liberamente accettata al momento della firma del contratto, prevede questa tappa preliminare in caso di controversia."},
                {"q": "Un accordo di mediazione commerciale ha la stessa forza di una sentenza?",
                 "a": "Assume in linea di principio la forma di un contratto di transazione tra le parti, vincolante secondo le regole generali del diritto dei contratti, ma non beneficia automaticamente della forza esecutiva di una sentenza salvo un passo supplementare previsto dalla legge."},
                {"q": "Perché combinare mediazione e arbitrato in un contratto commerciale?",
                 "a": "Per tentare dapprima una composizione amichevole rapida e confidenziale tramite la mediazione, conservando, in caso di fallimento, una procedura arbitrale vincolante che permette di decidere definitivamente la controversia senza passare dai tribunali statali."},
            ],
        },
        "en": {
            "slug": "commercial-mediation-alternative-litigation",
            "title": "Commercial mediation: an alternative to litigation",
            "meta": "Resolving a business dispute outside court, confidentiality, speed: the benefits of commercial mediation in Switzerland.",
            "sections": [
                {"heading": "A voluntary means of resolution", "paragraphs": [
                    "Unlike family mediation, commercial mediation between businesses is not the subject of a dedicated legal framework in the CCP: it mainly relies on the parties' agreement to use a mediator, often provided for by a contractual mediation clause, or decided jointly once the dispute has arisen.",
                ]},
                {"heading": "The benefits for businesses", "paragraphs": [
                    "Commercial mediation offers a confidentiality that court proceedings, in principle public, do not always guarantee, control by the parties over the outcome of the dispute rather than a decision imposed by a third party, and generally greater speed than civil litigation, which often makes it possible to preserve a business relationship the parties wish to continue.",
                ]},
                {"heading": "How it interacts with arbitration", "paragraphs": [
                    "Many commercial contracts, particularly international ones, provide for clauses combining mediation and arbitration, with mediation acting as a preliminary attempt at amicable settlement before resorting, if it fails, to binding arbitration proceedings before an arbitral tribunal.",
                ]},
                {"heading": "The binding force of the agreement reached", "paragraphs": [
                    "An agreement reached through commercial mediation in principle takes the form of a settlement contract between the parties, whose binding nature rests on the general rules of contract law, and not on systematic court approval as is sometimes the case in family matters.",
                ]},
            ],
            "faq": [
                {"q": "Can a business be forced to use mediation?",
                 "a": "In principle no, unless a contractual mediation clause, freely accepted when the contract was signed, provides for this preliminary step in the event of a dispute."},
                {"q": "Does a commercial mediation agreement have the same force as a judgment?",
                 "a": "It in principle takes the form of a settlement contract between the parties, binding under the general rules of contract law, but does not automatically benefit from the enforceability of a judgment unless an additional step provided by law is taken."},
                {"q": "Why combine mediation and arbitration in a commercial contract?",
                 "a": "To first attempt a quick, confidential amicable settlement through mediation, while retaining, if it fails, binding arbitration proceedings that make it possible to finally resolve the dispute without going through the state courts."},
            ],
        },
    },
    "permis-construire-procedure-opposition-voisins": {
        "domaine_id": "droit_construction_amenagement",
        "published": "2026-07-30",
        "fr": {
            "slug": "permis-construire-procedure-opposition-voisins",
            "title": "Permis de construire : procédure et opposition",
            "meta": "Dépôt de la demande, mise à l'enquête publique, droit d'opposition des voisins : la procédure prévue par le droit cantonal et la LAT.",
            "sections": [
                {"heading": "Une procédure essentiellement cantonale", "paragraphs": [
                    "La procédure d'octroi du permis de construire relève principalement du droit cantonal et communal, la loi fédérale sur l'aménagement du territoire (LAT) posant surtout les principes généraux d'affectation du sol que les plans d'affectation cantonaux et communaux doivent respecter. Les délais et modalités précises varient donc sensiblement d'un canton à l'autre.",
                ]},
                {"heading": "La mise à l'enquête publique", "paragraphs": [
                    "La plupart des projets de construction font l'objet d'une mise à l'enquête publique, généralement par publication officielle et affichage sur le terrain concerné, permettant aux tiers intéressés de prendre connaissance du projet et, le cas échéant, de faire opposition dans le délai fixé par le droit cantonal.",
                ]},
                {"heading": "Le droit d'opposition des voisins", "paragraphs": [
                    "Un voisin peut faire opposition à un projet de construction s'il dispose de la qualité pour agir, généralement reconnue à toute personne directement touchée par le projet et ayant un intérêt digne de protection à sa modification ou son annulation, par exemple en raison d'une atteinte à l'ensoleillement, à la vue, ou d'un non-respect des règles de construction applicables (gabarit, distances aux limites).",
                ]},
                {"heading": "Les voies de recours", "paragraphs": [
                    "Si l'opposition est écartée par l'autorité communale ou cantonale compétente, l'opposant peut en principe porter la décision devant l'instance de recours cantonale compétente en matière de construction, puis, selon les cas, devant le Tribunal fédéral pour les questions relevant du droit fédéral de l'aménagement du territoire.",
                ]},
            ],
            "faq": [
                {"q": "Tout voisin peut-il s'opposer à un projet de construction ?",
                 "a": "Non, il faut disposer de la qualité pour agir, généralement reconnue à toute personne directement touchée par le projet et ayant un intérêt digne de protection à sa modification ou son annulation."},
                {"q": "Les règles de procédure sont-elles les mêmes dans tous les cantons ?",
                 "a": "Non, la procédure d'octroi du permis de construire relève principalement du droit cantonal et communal, avec des délais et modalités qui varient sensiblement d'un canton à l'autre."},
                {"q": "Que faire si mon opposition est rejetée ?",
                 "a": "Vous pouvez en principe porter la décision devant l'instance de recours cantonale compétente en matière de construction, puis, selon les cas, devant le Tribunal fédéral pour les questions relevant du droit fédéral de l'aménagement du territoire."},
            ],
        },
        "de": {
            "slug": "baubewilligung-verfahren-einsprache-nachbarn",
            "title": "Baubewilligung: Verfahren und Einsprache",
            "meta": "Gesuchseinreichung, öffentliche Auflage, Einspracherecht der Nachbarschaft: das vom kantonalen Recht und RPG vorgesehene Verfahren.",
            "sections": [
                {"heading": "Ein hauptsächlich kantonales Verfahren", "paragraphs": [
                    "Das Verfahren zur Erteilung der Baubewilligung fällt hauptsächlich in den Bereich des kantonalen und kommunalen Rechts, wobei das Bundesgesetz über die Raumplanung (RPG) vor allem die allgemeinen Grundsätze der Bodennutzung festlegt, welche die kantonalen und kommunalen Nutzungspläne einhalten müssen. Die genauen Fristen und Modalitäten variieren daher erheblich von Kanton zu Kanton.",
                ]},
                {"heading": "Die öffentliche Auflage", "paragraphs": [
                    "Die meisten Bauvorhaben werden öffentlich aufgelegt, in der Regel durch amtliche Publikation und Anschlag auf dem betroffenen Grundstück, was interessierten Dritten erlaubt, vom Vorhaben Kenntnis zu nehmen und gegebenenfalls innert der vom kantonalen Recht festgelegten Frist Einsprache zu erheben.",
                ]},
                {"heading": "Das Einspracherecht der Nachbarschaft", "paragraphs": [
                    "Eine Nachbarin oder ein Nachbar kann gegen ein Bauvorhaben Einsprache erheben, sofern sie oder er über die Beschwerdelegitimation verfügt, in der Regel anerkannt für jede vom Vorhaben unmittelbar betroffene Person mit einem schutzwürdigen Interesse an dessen Änderung oder Aufhebung, etwa wegen einer Beeinträchtigung der Besonnung, der Aussicht, oder der Nichteinhaltung der anwendbaren Bauvorschriften (Gebäudehöhe, Grenzabstände).",
                ]},
                {"heading": "Die Rechtsmittel", "paragraphs": [
                    "Wird die Einsprache von der zuständigen kommunalen oder kantonalen Behörde abgewiesen, kann die einsprechende Person den Entscheid grundsätzlich bei der zuständigen kantonalen Baurekursinstanz anfechten, danach je nach Fall beim Bundesgericht für Fragen des Bundesraumplanungsrechts.",
                ]},
            ],
            "faq": [
                {"q": "Kann jede Nachbarin oder jeder Nachbar gegen ein Bauvorhaben Einsprache erheben?",
                 "a": "Nein, es braucht die Beschwerdelegitimation, in der Regel anerkannt für jede vom Vorhaben unmittelbar betroffene Person mit einem schutzwürdigen Interesse an dessen Änderung oder Aufhebung."},
                {"q": "Sind die Verfahrensregeln in allen Kantonen gleich?",
                 "a": "Nein, das Verfahren zur Erteilung der Baubewilligung fällt hauptsächlich in den Bereich des kantonalen und kommunalen Rechts, mit Fristen und Modalitäten, die von Kanton zu Kanton erheblich variieren."},
                {"q": "Was tun, wenn meine Einsprache abgewiesen wird?",
                 "a": "Sie können den Entscheid grundsätzlich bei der zuständigen kantonalen Baurekursinstanz anfechten, danach je nach Fall beim Bundesgericht für Fragen des Bundesraumplanungsrechts."},
            ],
        },
        "it": {
            "slug": "licenza-edilizia-procedura-opposizione-vicini",
            "title": "Licenza edilizia: procedura e opposizione",
            "meta": "Presentazione della domanda, pubblicazione, diritto di opposizione dei vicini: la procedura prevista dal diritto cantonale e dalla LPT.",
            "sections": [
                {"heading": "Una procedura essenzialmente cantonale", "paragraphs": [
                    "La procedura di rilascio della licenza edilizia rientra principalmente nel diritto cantonale e comunale, mentre la legge federale sulla pianificazione del territorio (LPT) pone soprattutto i principi generali di destinazione del suolo che i piani di utilizzazione cantonali e comunali devono rispettare. I termini e le modalità precise variano quindi sensibilmente da un Cantone all'altro.",
                ]},
                {"heading": "La pubblicazione", "paragraphs": [
                    "La maggior parte dei progetti di costruzione è oggetto di pubblicazione, generalmente tramite pubblicazione ufficiale e affissione sul terreno interessato, che permette ai terzi interessati di prendere conoscenza del progetto e, se del caso, di fare opposizione entro il termine fissato dal diritto cantonale.",
                ]},
                {"heading": "Il diritto di opposizione dei vicini", "paragraphs": [
                    "Un vicino può fare opposizione a un progetto di costruzione se dispone della legittimazione ad agire, generalmente riconosciuta a qualsiasi persona direttamente toccata dal progetto e avente un interesse degno di protezione alla sua modifica o al suo annullamento, per esempio a causa di un pregiudizio all'irraggiamento solare, alla vista, o del mancato rispetto delle norme edilizie applicabili (altezza, distanze dai confini).",
                ]},
                {"heading": "Le vie di ricorso", "paragraphs": [
                    "Se l'opposizione viene respinta dall'autorità comunale o cantonale competente, l'opponente può in linea di principio portare la decisione davanti all'istanza di ricorso cantonale competente in materia edilizia, poi, secondo i casi, davanti al Tribunale federale per le questioni rientranti nel diritto federale della pianificazione del territorio.",
                ]},
            ],
            "faq": [
                {"q": "Qualsiasi vicino può opporsi a un progetto di costruzione?",
                 "a": "No, occorre disporre della legittimazione ad agire, generalmente riconosciuta a qualsiasi persona direttamente toccata dal progetto e avente un interesse degno di protezione alla sua modifica o al suo annullamento."},
                {"q": "Le regole procedurali sono le stesse in tutti i Cantoni?",
                 "a": "No, la procedura di rilascio della licenza edilizia rientra principalmente nel diritto cantonale e comunale, con termini e modalità che variano sensibilmente da un Cantone all'altro."},
                {"q": "Cosa fare se la mia opposizione viene respinta?",
                 "a": "Potete in linea di principio portare la decisione davanti all'istanza di ricorso cantonale competente in materia edilizia, poi, secondo i casi, davanti al Tribunale federale per le questioni rientranti nel diritto federale della pianificazione del territorio."},
            ],
        },
        "en": {
            "slug": "building-permit-procedure-neighbour-opposition",
            "title": "Building permits: procedure and opposition",
            "meta": "Filing the application, public notice, neighbours' right to object: the procedure under cantonal law and the Spatial Planning Act.",
            "sections": [
                {"heading": "A mainly cantonal procedure", "paragraphs": [
                    "The procedure for granting a building permit mainly falls under cantonal and municipal law, with the federal Spatial Planning Act (SPA) primarily setting the general principles of land use that cantonal and municipal zoning plans must comply with. The precise deadlines and procedures therefore vary considerably from canton to canton.",
                ]},
                {"heading": "Public notice", "paragraphs": [
                    "Most construction projects are subject to public notice, generally through official publication and posting on the site concerned, allowing interested third parties to learn of the project and, where applicable, to file an objection within the deadline set by cantonal law.",
                ]},
                {"heading": "Neighbours' right to object", "paragraphs": [
                    "A neighbour can object to a construction project if they have standing, generally recognised for any person directly affected by the project with a legitimate interest in its modification or cancellation, for example due to an impact on sunlight, views, or non-compliance with applicable building regulations (height, setback distances).",
                ]},
                {"heading": "Legal remedies", "paragraphs": [
                    "If the objection is dismissed by the competent municipal or cantonal authority, the objector can in principle bring the decision before the competent cantonal building appeals body, then, depending on the case, before the Federal Supreme Court for matters falling under federal spatial planning law.",
                ]},
            ],
            "faq": [
                {"q": "Can any neighbour object to a construction project?",
                 "a": "No, standing is required, generally recognised for any person directly affected by the project with a legitimate interest in its modification or cancellation."},
                {"q": "Are the procedural rules the same in every canton?",
                 "a": "No, the procedure for granting a building permit mainly falls under cantonal and municipal law, with deadlines and procedures that vary considerably from canton to canton."},
                {"q": "What should I do if my objection is dismissed?",
                 "a": "You can in principle bring the decision before the competent cantonal building appeals body, then, depending on the case, before the Federal Supreme Court for matters falling under federal spatial planning law."},
            ],
        },
    },
    "zone-batir-hors-zone-consequences": {
        "domaine_id": "droit_construction_amenagement",
        "published": "2026-07-30",
        "fr": {
            "slug": "zone-batir-hors-zone-batir-consequences-terrain",
            "title": "Zone à bâtir et hors zone à bâtir : les différences",
            "meta": "Constructibilité d'un terrain selon son affectation, dérogations pour les constructions hors zone à bâtir : les règles de la LAT.",
            "sections": [
                {"heading": "La zone à bâtir", "paragraphs": [
                    "La LAT (art. 15) définit la zone à bâtir comme les terrains propres à la construction déjà largement bâtis, ou dont le besoin pour les quinze années à venir est démontré, et qui seront équipés dans ce délai. Un terrain classé en zone à bâtir peut en principe faire l'objet d'une construction conforme à l'affectation prévue par le plan de zone communal (habitat, activités, mixte).",
                ]},
                {"heading": "Le hors zone à bâtir", "paragraphs": [
                    "Un terrain situé hors zone à bâtir (zone agricole, zone forestière, zone protégée) n'est en principe pas constructible, la LAT visant à limiter le mitage du territoire et à préserver les terres agricoles et les espaces naturels de constructions dispersées.",
                ]},
                {"heading": "Les dérogations possibles", "paragraphs": [
                    "L'art. 24 LAT permet, à titre exceptionnel et à des conditions strictes, une autorisation dérogatoire pour des constructions hors zone à bâtir dont l'implantation est imposée par leur destination (comme certaines constructions agricoles) et qui ne s'opposent à aucun intérêt prépondérant. Ces dérogations sont interprétées restrictivement par les autorités et les tribunaux.",
                ]},
                {"heading": "L'impact sur la valeur et l'usage d'un terrain", "paragraphs": [
                    "L'affectation d'un terrain (à bâtir ou non) a un impact déterminant sur sa valeur et les possibilités concrètes de l'utiliser : avant tout projet ou acquisition, il est essentiel de vérifier précisément le régime applicable auprès du service cantonal ou communal de l'aménagement du territoire, le plan de zone communal faisant foi.",
                ]},
            ],
            "faq": [
                {"q": "Puis-je construire sur un terrain classé hors zone à bâtir ?",
                 "a": "En principe non, sauf dérogation exceptionnelle au sens de l'art. 24 LAT, réservée aux constructions dont l'implantation est imposée par leur destination et qui ne s'opposent à aucun intérêt prépondérant."},
                {"q": "Comment savoir si mon terrain est en zone à bâtir ?",
                 "a": "En consultant le plan de zone (plan d'affectation) de la commune où se situe le terrain, disponible auprès du service communal ou cantonal de l'aménagement du territoire."},
                {"q": "Une zone à bâtir peut-elle être modifiée ultérieurement ?",
                 "a": "Oui, les plans d'affectation peuvent être révisés par les autorités communales et cantonales compétentes, dans le respect des principes fédéraux de la LAT, ce qui peut faire évoluer le statut constructible d'un terrain avec le temps."},
            ],
        },
        "de": {
            "slug": "bauzone-ausserhalb-bauzone-unterschiede",
            "title": "Bauzone und Nichtbauzone: die Unterschiede",
            "meta": "Baumöglichkeiten eines Grundstücks je nach Zonenzugehörigkeit, Ausnahmebewilligungen ausserhalb der Bauzone: die Regeln des RPG.",
            "sections": [
                {"heading": "Die Bauzone", "paragraphs": [
                    "Das RPG (Art. 15) definiert die Bauzone als Land, das sich für die Überbauung eignet und weitgehend überbaut ist, oder dessen Bedarf für die nächsten fünfzehn Jahre nachgewiesen ist und das innerhalb dieser Frist erschlossen wird. Ein in der Bauzone gelegenes Grundstück kann grundsätzlich mit einer dem kommunalen Zonenplan entsprechenden Nutzung überbaut werden (Wohnen, Gewerbe, Mischnutzung).",
                ]},
                {"heading": "Die Nichtbauzone", "paragraphs": [
                    "Ein ausserhalb der Bauzone gelegenes Grundstück (Landwirtschaftszone, Waldzone, Schutzzone) ist grundsätzlich nicht überbaubar, wobei das RPG die Zersiedelung des Gebiets begrenzen und die landwirtschaftlichen Flächen sowie natürlichen Räume vor verstreuten Bauten schützen soll.",
                ]},
                {"heading": "Die möglichen Ausnahmebewilligungen", "paragraphs": [
                    "Art. 24 RPG erlaubt ausnahmsweise und unter strengen Voraussetzungen eine Ausnahmebewilligung für Bauten ausserhalb der Bauzone, deren Standort durch ihren Zweck bedingt ist (wie bestimmte landwirtschaftliche Bauten) und die keinen überwiegenden Interessen entgegenstehen. Diese Ausnahmen werden von den Behörden und Gerichten restriktiv ausgelegt.",
                ]},
                {"heading": "Die Auswirkung auf Wert und Nutzung eines Grundstücks", "paragraphs": [
                    "Die Zuordnung eines Grundstücks (zur Bauzone oder nicht) hat einen entscheidenden Einfluss auf seinen Wert und die konkreten Nutzungsmöglichkeiten: vor jedem Vorhaben oder Erwerb ist es unerlässlich, das anwendbare Regime genau bei der kantonalen oder kommunalen Raumplanungsstelle zu prüfen, wobei der kommunale Zonenplan massgebend ist.",
                ]},
            ],
            "faq": [
                {"q": "Darf ich auf einem als Nichtbauzone eingestuften Grundstück bauen?",
                 "a": "Grundsätzlich nicht, ausser bei einer ausnahmsweisen Bewilligung gemäss Art. 24 RPG, vorbehalten für Bauten, deren Standort durch ihren Zweck bedingt ist und die keinen überwiegenden Interessen entgegenstehen."},
                {"q": "Wie erfahre ich, ob mein Grundstück in der Bauzone liegt?",
                 "a": "Durch Konsultation des Zonenplans (Nutzungsplans) der Gemeinde, in der sich das Grundstück befindet, erhältlich bei der kommunalen oder kantonalen Raumplanungsstelle."},
                {"q": "Kann eine Bauzone später geändert werden?",
                 "a": "Ja, die Nutzungspläne können von den zuständigen kommunalen und kantonalen Behörden im Rahmen der bundesrechtlichen Grundsätze des RPG revidiert werden, was den Baustatus eines Grundstücks im Laufe der Zeit verändern kann."},
            ],
        },
        "it": {
            "slug": "zona-edificabile-fuori-zona-conseguenze-terreno",
            "title": "Zona edificabile e fuori zona: le differenze",
            "meta": "Edificabilità di un terreno secondo la sua destinazione, deroghe per le costruzioni fuori zona edificabile: le regole della LPT.",
            "sections": [
                {"heading": "La zona edificabile", "paragraphs": [
                    "La LPT (art. 15) definisce la zona edificabile come i terreni adatti all'edificazione già ampiamente edificati, o il cui bisogno per i prossimi quindici anni è dimostrato, e che saranno urbanizzati entro tale termine. Un terreno classificato in zona edificabile può in linea di principio essere oggetto di una costruzione conforme alla destinazione prevista dal piano di zona comunale (abitativo, attività, misto).",
                ]},
                {"heading": "Il fuori zona edificabile", "paragraphs": [
                    "Un terreno situato fuori zona edificabile (zona agricola, zona forestale, zona protetta) non è in linea di principio edificabile, poiché la LPT mira a limitare la dispersione insediativa e a preservare i terreni agricoli e gli spazi naturali da costruzioni disperse.",
                ]},
                {"heading": "Le deroghe possibili", "paragraphs": [
                    "L'art. 24 LPT permette, a titolo eccezionale e a condizioni rigorose, un'autorizzazione derogatoria per costruzioni fuori zona edificabile la cui ubicazione è imposta dalla loro destinazione (come determinate costruzioni agricole) e che non si oppongono ad alcun interesse preponderante. Queste deroghe sono interpretate restrittivamente dalle autorità e dai tribunali.",
                ]},
                {"heading": "L'impatto sul valore e sull'uso di un terreno", "paragraphs": [
                    "La destinazione di un terreno (edificabile o meno) ha un impatto determinante sul suo valore e sulle possibilità concrete di utilizzarlo: prima di qualsiasi progetto o acquisto, è essenziale verificare precisamente il regime applicabile presso il servizio cantonale o comunale della pianificazione del territorio, facendo fede il piano di zona comunale.",
                ]},
            ],
            "faq": [
                {"q": "Posso costruire su un terreno classificato fuori zona edificabile?",
                 "a": "In linea di principio no, salvo deroga eccezionale ai sensi dell'art. 24 LPT, riservata alle costruzioni la cui ubicazione è imposta dalla loro destinazione e che non si oppongono ad alcun interesse preponderante."},
                {"q": "Come posso sapere se il mio terreno è in zona edificabile?",
                 "a": "Consultando il piano di zona (piano di utilizzazione) del Comune in cui si trova il terreno, disponibile presso il servizio comunale o cantonale della pianificazione del territorio."},
                {"q": "Una zona edificabile può essere modificata successivamente?",
                 "a": "Sì, i piani di utilizzazione possono essere rivisti dalle autorità comunali e cantonali competenti, nel rispetto dei principi federali della LPT, il che può far evolvere lo statuto edificabile di un terreno nel tempo."},
            ],
        },
        "en": {
            "slug": "building-zone-outside-building-zone-consequences",
            "title": "Building zone and non-building zone: the differences",
            "meta": "Whether a plot can be built on depending on its zoning, exceptions for construction outside the building zone: the Spatial Planning Act rules.",
            "sections": [
                {"heading": "The building zone", "paragraphs": [
                    "The Spatial Planning Act (art. 15) defines the building zone as land suitable for construction that is already largely built up, or whose need for the next fifteen years is demonstrated, and which will be serviced within that period. A plot classified in the building zone can in principle be built on in accordance with the use provided for by the municipal zoning plan (residential, business, mixed).",
                ]},
                {"heading": "Outside the building zone", "paragraphs": [
                    "A plot located outside the building zone (agricultural zone, forest zone, protected zone) is in principle not buildable, as the Spatial Planning Act aims to limit urban sprawl and preserve agricultural land and natural areas from scattered construction.",
                ]},
                {"heading": "Possible exceptions", "paragraphs": [
                    "Art. 24 SPA exceptionally allows, under strict conditions, an exceptional authorisation for construction outside the building zone whose location is required by its purpose (such as certain agricultural buildings) and which does not conflict with any overriding interest. These exceptions are interpreted restrictively by authorities and courts.",
                ]},
                {"heading": "The impact on the value and use of a plot", "paragraphs": [
                    "A plot's zoning (buildable or not) has a decisive impact on its value and the concrete possibilities for using it: before any project or purchase, it is essential to precisely check the applicable regime with the cantonal or municipal spatial planning department, with the municipal zoning plan being authoritative.",
                ]},
            ],
            "faq": [
                {"q": "Can I build on a plot classified outside the building zone?",
                 "a": "In principle no, except for an exceptional authorisation under art. 24 SPA, reserved for construction whose location is required by its purpose and which does not conflict with any overriding interest."},
                {"q": "How do I find out if my plot is in the building zone?",
                 "a": "By consulting the zoning plan of the municipality where the plot is located, available from the municipal or cantonal spatial planning department."},
                {"q": "Can a building zone be changed later?",
                 "a": "Yes, zoning plans can be revised by the competent municipal and cantonal authorities, in compliance with the federal principles of the Spatial Planning Act, which can change a plot's buildable status over time."},
            ],
        },
    },
    'certificat-travail-contenu-contestation': {'domaine_id': 'droit_travail', 'published': '2026-08-01', 'fr': {'slug': 'certificat-travail-contenu-refus-contestation', 'title': 'Certificat de travail : contenu, refus et contestation', 'meta': "Certificat complet ou simple attestation, principe de vérité et de bienveillance, que faire en cas de refus ou de formulation contestable : l'art. 330a CO.", 'sections': [{'heading': 'Le droit au certificat de travail', 'paragraphs': ["L'art. 330a CO donne à tout travailleur le droit d'exiger de son employeur, en tout temps pendant les rapports de travail ou à leur fin, un certificat portant sur la nature et la durée des rapports de travail ainsi que sur la qualité de son travail et sa conduite. Ce droit existe indépendamment du motif de la fin des rapports de travail, y compris en cas de licenciement.", "Le travailleur peut demander soit un certificat complet (dit qualifiant), qui décrit la nature du poste et évalue les prestations et le comportement, soit une simple attestation de travail limitée à la nature et à la durée de l'emploi, sans appréciation. Le choix appartient au travailleur, pas à l'employeur."]}, {'heading': 'Les principes de vérité, de bienveillance et de clarté', 'paragraphs': ["Le certificat doit être véridique et complet : il ne peut pas taire des faits pertinents dont l'omission donnerait une image inexacte, ni contenir des indications inexactes ou trompeuses. Il doit dans le même temps rester formulé de façon bienveillante, dans la mesure compatible avec la vérité, sans termes ambigus ou codés destinés à nuire au travailleur dans ses recherches futures.", 'Ces deux exigences peuvent entrer en tension lorsque les prestations ont été insuffisantes ou que des manquements graves ont émaillé les rapports de travail : la jurisprudence admet alors que le certificat en fasse état, à condition de rester factuel et proportionné plutôt que dénigrant.']}, {'heading': 'Que faire en cas de refus ou de contenu contesté', 'paragraphs': ["Si l'employeur refuse purement et simplement d'établir un certificat, le travailleur peut agir en justice pour en obtenir la délivrance. Si un certificat est délivré mais que son contenu est jugé inexact, incomplet ou rédigé de manière à nuire injustement, une action en rectification peut être intentée devant le tribunal compétent en matière de droit du travail.", "Dans les deux cas, il appartient en principe à l'employeur de prouver que les éléments contestés du certificat correspondent à la réalité, notamment lorsque le travailleur conteste une appréciation défavorable de ses prestations."]}, {'heading': 'Délai et conseils pratiques', 'paragraphs': ["Il est recommandé de vérifier le certificat dès sa réception et de réagir rapidement en cas de désaccord, la crédibilité d'une contestation tardive, plusieurs mois après le départ, étant généralement plus difficile à établir. Une négociation directe avec l'ancien employeur permet souvent de corriger une formulation maladroite sans passer par une procédure judiciaire."]}], 'faq': [{'q': 'Mon employeur peut-il refuser de me délivrer un certificat de travail ?', 'a': "Non : l'art. 330a CO donne un droit inconditionnel au certificat, quel que soit le motif de la fin des rapports de travail. En cas de refus, le travailleur peut agir en justice pour en obtenir la délivrance."}, {'q': "Puis-je demander une simple attestation plutôt qu'un certificat complet ?", 'a': "Oui, le choix entre le certificat complet (avec appréciation des prestations et de la conduite) et la simple attestation de travail (nature et durée uniquement) appartient au travailleur, pas à l'employeur."}, {'q': 'Que faire si je trouve mon certificat de travail injuste ?', 'a': "Vous pouvez d'abord tenter une négociation directe avec l'employeur, puis, en l'absence d'accord, intenter une action en rectification devant le tribunal compétent. C'est en principe à l'employeur de prouver que les éléments contestés sont exacts."}]}},
    'harcelement-discrimination-travail-recours': {'domaine_id': 'droit_travail', 'published': '2026-08-01', 'fr': {'slug': 'harcelement-discrimination-travail-recours', 'title': 'Discrimination et harcèlement au travail : recours possibles', 'meta': "Protection de la personnalité du travailleur, loi sur l'égalité, mobbing et harcèlement sexuel : les recours civils et pénaux disponibles en Suisse.", 'sections': [{'heading': "Le devoir de protection de l'employeur", 'paragraphs': ["L'art. 328 CO impose à l'employeur de protéger la personnalité du travailleur et de veiller au respect des bonnes mœurs, notamment en prenant les mesures nécessaires pour prévenir le harcèlement et le mobbing sur le lieu de travail. Ce devoir s'applique indépendamment de la source du harcèlement, qu'il émane d'un supérieur, d'un collègue ou d'un tiers.", "Un manquement grave et persistant à ce devoir peut engager la responsabilité contractuelle de l'employeur et, dans les cas les plus sérieux, justifier une résiliation immédiate du contrat par le travailleur pour justes motifs au sens de l'art. 337 CO."]}, {'heading': 'La discrimination fondée sur le sexe', 'paragraphs': ["La loi sur l'égalité (LEg) interdit toute discrimination fondée sur le sexe dans les rapports de travail, notamment en matière de salaire, de formation, de promotion ou de résiliation, ainsi que le harcèlement sexuel, expressément défini comme une forme de discrimination.", "Cette loi facilite la position de la personne discriminée : lorsqu'une discrimination est rendue vraisemblable, il appartient à l'employeur de prouver qu'elle n'existe pas, un allègement du fardeau de la preuve qui ne s'applique toutefois pas de la même manière à toutes les prétentions, notamment celle liée à l'embauche."]}, {'heading': 'Les recours civils', 'paragraphs': ["La victime peut réclamer la cessation de l'atteinte, des dommages-intérêts pour le préjudice matériel subi ainsi qu'une indemnité pour tort moral (art. 49 CO) en cas d'atteinte grave à sa personnalité. En matière de discrimination au sens de la LEg, une procédure de conciliation devant l'office cantonal compétent est en principe préalable à toute action judiciaire.", "Documenter les faits au fur et à mesure (échanges écrits, témoins, journal des incidents) renforce considérablement les chances de succès d'une démarche, qu'elle reste interne à l'entreprise ou qu'elle débouche sur une procédure."]}, {'heading': 'Les recours pénaux', 'paragraphs': ["Selon la gravité des faits, une plainte pénale peut être envisagée en parallèle : le harcèlement sexuel peut par exemple constituer une contrainte sexuelle ou des voies de fait, tandis que des menaces ou une atteinte à l'honneur relèvent d'autres dispositions du Code pénal. Ces infractions sont généralement poursuivies sur plainte, dans un délai de trois mois dès la connaissance de l'auteur."]}], 'faq': [{'q': 'Que puis-je faire si mon employeur ne réagit pas face à une situation de harcèlement signalée ?', 'a': "L'inaction de l'employeur peut constituer une violation de son devoir de protection (art. 328 CO), engageant sa responsabilité et pouvant, dans les cas graves, justifier une résiliation immédiate du contrat par le travailleur pour justes motifs."}, {'q': "La loi sur l'égalité facilite-t-elle vraiment la preuve d'une discrimination ?", 'a': "Oui, dans une certaine mesure : une fois la discrimination rendue vraisemblable, c'est à l'employeur de prouver son absence. Ce mécanisme ne s'applique toutefois pas de façon identique à toutes les prétentions prévues par la loi."}, {'q': "Puis-je porter plainte pénalement en plus d'agir civilement ?", 'a': "Oui, les deux voies ne s'excluent pas. Selon la nature des faits, une plainte pénale (par exemple pour contrainte sexuelle, voies de fait ou menaces) peut être déposée en parallèle d'une action civile fondée sur le droit du travail."}]}},
    'concubinage-droits-couple-non-marie': {'domaine_id': 'droit_famille', 'published': '2026-08-01', 'fr': {'slug': 'concubinage-droits-couple-non-marie-suisse', 'title': 'Concubinage en Suisse : quels droits pour le couple non marié', 'meta': "Absence de régime légal automatique, autorité parentale, succession, prévoyance : ce que le concubinage protège et ce qu'il ne protège pas en Suisse.", 'sections': [{'heading': "L'absence de régime légal propre", 'paragraphs': ["Contrairement au mariage ou au partenariat enregistré, le concubinage n'est encadré par aucun régime légal spécifique en droit suisse. Les concubins ne se doivent en principe aucune obligation d'entretien réciproque, ne bénéficient d'aucun régime matrimonial et ne sont pas automatiquement héritiers l'un de l'autre.", 'Cette absence de cadre légal peut être compensée, dans une certaine mesure, par un contrat de concubinage réglant les aspects patrimoniaux de la vie commune, mais un tel contrat ne crée pas les protections propres au statut marital, notamment en matière de prévoyance ou de droit successoral impératif.']}, {'heading': 'Les enfants nés hors mariage', 'paragraphs': ["La filiation paternelle d'un enfant né hors mariage n'est pas automatique : elle doit être établie par une reconnaissance de paternité auprès de l'état civil ou, à défaut, par une action en justice. Depuis la réforme de l'autorité parentale, les parents non mariés peuvent obtenir l'autorité parentale conjointe par une déclaration commune, qui est devenue la règle plutôt que l'exception.", "En cas de séparation, les questions de garde, de droit de visite et de contribution d'entretien de l'enfant sont traitées selon les mêmes principes que pour un couple marié, l'intérêt de l'enfant restant le critère déterminant, indépendamment du statut matrimonial des parents."]}, {'heading': "Succession : l'absence de protection automatique", 'paragraphs': ["Le concubin survivant n'est pas un héritier légal : sans testament ou pacte successoral en sa faveur, il n'hérite rien de son partenaire décédé, même après plusieurs décennies de vie commune. Et même avec un testament, les héritiers réservataires (descendants, parfois le conjoint s'il y en a un) conservent une part protégée qui limite ce que le concubin peut recevoir.", 'Une planification successorale adaptée, testament ou pacte successoral rédigé avec un professionnel, est donc essentielle pour un couple non marié souhaitant se protéger mutuellement.']}, {'heading': 'Prévoyance et assurances', 'paragraphs': ["Le 2e et le 3e pilier permettent en revanche souvent de désigner un concubin comme bénéficiaire en cas de décès, sous certaines conditions fixées par le règlement de la caisse de pension ou du produit de prévoyance concerné, notamment une durée minimale de vie commune ou l'absence d'autres bénéficiaires prioritaires. Il est essentiel de vérifier ces conditions et de faire les démarches de désignation, qui ne sont jamais automatiques."]}], 'faq': [{'q': 'Un concubin hérite-t-il automatiquement de son partenaire décédé ?', 'a': "Non. Le concubin n'est pas un héritier légal en droit suisse. Sans testament ou pacte successoral en sa faveur, il n'a droit à rien, quelle que soit la durée de la vie commune."}, {'q': "Un couple non marié peut-il obtenir l'autorité parentale conjointe ?", 'a': "Oui, par une déclaration commune des parents à l'état civil, qui est aujourd'hui le régime le plus courant pour les enfants nés hors mariage, une fois la filiation paternelle établie."}, {'q': 'Comment protéger financièrement son concubin en cas de décès ?', 'a': 'En rédigeant un testament ou un pacte successoral dans les limites de la réserve héréditaire des autres héritiers, et en vérifiant les possibilités de désignation de bénéficiaire offertes par le 2e et le 3e pilier.'}]}},
    'adoption-suisse-conditions-procedure': {'domaine_id': 'droit_famille', 'published': '2026-08-01', 'fr': {'slug': 'adoption-suisse-conditions-procedure', 'title': 'Adoption en Suisse : conditions et procédure', 'meta': "Adoption conjointe, adoption de l'enfant du conjoint, période de garde probatoire : les conditions et les étapes de la procédure d'adoption en droit suisse.", 'sections': [{'heading': 'Qui peut adopter', 'paragraphs': ["L'adoption conjointe d'un enfant est en principe réservée aux couples mariés vivant en ménage commun depuis un certain temps, tandis qu'une personne seule peut également adopter, à titre individuel, à partir d'un âge minimal fixé par la loi. L'adoption de l'enfant du conjoint ou du partenaire est également possible, dans des conditions assouplies par rapport à l'adoption conjointe classique.", "Dans tous les cas, une différence d'âge minimale entre l'adoptant et l'enfant est exigée, ainsi qu'un examen approfondi de l'aptitude des futurs parents adoptifs à assumer l'entretien et l'éducation de l'enfant."]}, {'heading': 'La période de garde probatoire', 'paragraphs': ["Avant qu'une adoption puisse être prononcée, l'art. 264 CC exige en principe que les futurs parents adoptifs aient déjà fourni à l'enfant des soins et une éducation pendant une période suffisante, permettant de juger si le lien créé correspond au bien de l'enfant. Cette période probatoire varie selon les situations et fait l'objet d'un suivi par l'autorité compétente."]}, {'heading': 'Le consentement des parents biologiques', 'paragraphs': ["L'adoption requiert en principe le consentement des parents biologiques de l'enfant, sauf circonstances exceptionnelles prévues par la loi permettant de s'en dispenser, par exemple en cas d'incapacité durable de discernement ou de résidence inconnue. Ce consentement ne peut être donné qu'après la naissance de l'enfant et un délai de réflexion est prévu."]}, {'heading': "La procédure et l'autorité compétente", 'paragraphs': ["L'adoption est prononcée par l'autorité cantonale compétente, généralement après une instruction menée par les services sociaux cantonaux et un préavis de l'autorité de protection de l'enfant. Une fois l'adoption prononcée, l'enfant acquiert le statut d'enfant des parents adoptifs à tous égards, y compris pour la filiation, le nom et les droits successoraux, et les liens de filiation avec la famille biologique sont en principe rompus, sous réserve de l'adoption de l'enfant du conjoint."]}], 'faq': [{'q': 'Une personne seule peut-elle adopter en Suisse ?', 'a': "Oui, l'adoption individuelle est possible à partir d'un âge minimal fixé par la loi, alors que l'adoption conjointe d'un enfant reste en principe réservée aux couples mariés."}, {'q': 'Faut-il obligatoirement le consentement des parents biologiques ?', 'a': "En principe oui, sauf circonstances exceptionnelles prévues par la loi (incapacité durable de discernement, résidence inconnue notamment) permettant à l'autorité de s'en dispenser."}, {'q': "L'enfant adopté conserve-t-il des liens juridiques avec sa famille biologique ?", 'a': "En règle générale non : l'adoption rompt le lien de filiation avec la famille d'origine et crée un lien de filiation complet avec la famille adoptive, sous réserve du cas particulier de l'adoption de l'enfant du conjoint."}]}},
    'divorce-amiable-contentieux-differences': {'domaine_id': 'droit_divorce', 'published': '2026-08-02', 'fr': {'slug': 'divorce-amiable-contentieux-differences-couts', 'title': "Divorce à l'amiable vs contentieux : différences et coûts", 'meta': 'Divorce sur requête commune ou sur demande unilatérale après séparation : procédure, durée et coûts comparés des deux voies de divorce en Suisse.', 'sections': [{'heading': 'Le divorce sur requête commune', 'paragraphs': ["Lorsque les époux sont d'accord sur le principe du divorce, ils peuvent déposer une requête commune (art. 111-112 CC). S'ils s'entendent également sur l'ensemble des effets du divorce (biens, entretien, enfants), ils soumettent au juge une convention complète que celui-ci ratifie après s'être assuré qu'elle a été conclue librement et qu'elle n'est pas manifestement inéquitable.", "S'ils sont d'accord sur le principe mais pas sur tous les effets, le juge tranche uniquement les points litigieux, ce qui reste généralement plus rapide qu'une procédure entièrement contentieuse."]}, {'heading': 'Le divorce sur demande unilatérale', 'paragraphs': ["En l'absence d'accord, un époux peut demander le divorce après une séparation de deux ans (art. 114 CC), ou avant ce délai s'il établit que la continuation du mariage est devenue insupportable pour des motifs sérieux qui ne lui sont pas imputables (art. 115 CC). Cette voie implique en principe une instruction plus longue, avec échanges d'écritures, éventuelles expertises et audiences contradictoires."]}, {'heading': 'Différences de durée et de charge émotionnelle', 'paragraphs': ["Un divorce sur requête commune avec convention complète peut aboutir en quelques mois, parfois en une seule audience, tandis qu'une procédure contentieuse, surtout si elle porte sur la garde des enfants ou d'importants intérêts patrimoniaux, peut s'étendre sur plusieurs années, y compris en cas de recours.", 'Au-delà du temps, la procédure contentieuse expose davantage les parties, et le cas échéant les enfants, à un climat conflictuel prolongé, ce qui pousse de nombreux couples à recourir à la médiation pour tenter de trouver un accord avant ou pendant la procédure.']}, {'heading': 'Coûts comparés', 'paragraphs': ["Les frais de justice sont généralement calculés en fonction de la valeur litigieuse et sont souvent répartis par moitié en cas de requête commune. Les honoraires d'avocat dépendent surtout du temps consacré au dossier : une procédure contentieuse avec expertises, auditions et recours engendre logiquement des coûts nettement supérieurs à un accord négocié en amont."]}], 'faq': [{'q': "Faut-il être séparés depuis longtemps pour divorcer d'un commun accord ?", 'a': 'Non, le divorce sur requête commune ne suppose aucune durée de séparation préalable, contrairement au divorce sur demande unilatérale qui exige en principe deux ans de séparation, sauf motifs sérieux justifiant une demande anticipée.'}, {'q': 'Le juge est-il lié par la convention conclue entre les époux ?', 'a': "Non : il doit vérifier qu'elle a été conclue librement, en pleine connaissance de cause, et qu'elle n'est pas manifestement inéquitable, en particulier lorsqu'elle concerne des enfants mineurs."}, {'q': "Un divorce contentieux coûte-t-il toujours plus cher qu'un divorce amiable ?", 'a': "En règle générale oui, car les honoraires d'avocat et les frais de justice augmentent avec la complexité et la durée de la procédure, elles-mêmes accrues par l'absence d'accord entre les parties."}]}},
    'pension-alimentaire-enfant-majeur-formation': {'domaine_id': 'droit_divorce', 'published': '2026-08-02', 'fr': {'slug': 'pension-alimentaire-enfant-majeur-formation', 'title': "Pension alimentaire de l'enfant majeur en formation", 'meta': "L'obligation d'entretien des parents ne s'arrête pas toujours à la majorité : ce que prévoit l'art. 277 CC pour un enfant en formation initiale appropriée.", 'sections': [{'heading': "Le principe : l'entretien au-delà de la majorité", 'paragraphs': ["L'art. 277 al. 2 CC prévoit que l'obligation d'entretien des parents envers leur enfant se prolonge au-delà de la majorité aussi longtemps que dure une formation initiale appropriée, pour autant qu'elle soit menée dans des délais normaux. Cette règle vise à permettre à l'enfant d'achever un premier cursus de formation lui donnant accès à une activité professionnelle adaptée à ses capacités.", "L'obligation ne dépend donc pas d'un âge fixe, mais de la poursuite effective et diligente d'une formation appropriée, ce qui explique pourquoi elle peut s'étendre au-delà de vingt-cinq ans dans certaines situations, notamment en cas de cursus long ou de réorientation justifiée."]}, {'heading': 'Ce que recouvre une formation initiale appropriée', 'paragraphs': ["La notion de formation appropriée s'apprécie au regard des aptitudes, des goûts et de la situation de l'enfant : elle peut correspondre à un apprentissage, une maturité suivie d'études supérieures, ou tout autre parcours cohérent avec le profil de l'enfant. Une réorientation ponctuelle peut rester couverte si elle demeure raisonnable, mais des changements répétés ou un cursus mené sans diligence suffisante peuvent conduire à une réduction, voire une suppression de la contribution."]}, {'heading': 'Le montant et sa fixation', 'paragraphs': ["Une fois la majorité atteinte, la contribution d'entretien peut être adaptée pour tenir compte des revenus propres de l'enfant, notamment s'il exerce une activité accessoire ou perçoit une bourse. Le montant est fixé en tenant compte des besoins concrets de l'enfant en formation et de la situation financière de chacun des parents, l'enfant majeur pouvant lui-même agir en justice pour réclamer sa contribution."]}, {'heading': "La fin de l'obligation d'entretien", 'paragraphs': ["L'obligation prend fin à l'achèvement de la première formation donnant accès à une activité professionnelle permettant à l'enfant de subvenir à ses besoins, sans que les parents soient tenus de financer une seconde formation ou des études complémentaires de perfectionnement, sauf accord contraire ou circonstances particulières."]}], 'faq': [{'q': "Jusqu'à quel âge un parent doit-il verser une pension pour un enfant en formation ?", 'a': "Il n'y a pas d'âge fixe : l'obligation dure aussi longtemps que la formation initiale appropriée se poursuit dans des délais normaux, ce qui peut dépasser vingt-cinq ans selon le parcours suivi."}, {'q': 'Un enfant majeur peut-il réclamer lui-même sa pension alimentaire ?', 'a': "Oui, une fois majeur, c'est en principe à l'enfant lui-même d'agir en justice pour faire valoir son droit à l'entretien, et non plus au parent qui en avait la garde."}, {'q': "Que se passe-t-il si l'enfant change plusieurs fois d'orientation ?", 'a': "Des réorientations répétées ou un manque de diligence dans la formation peuvent amener les tribunaux à réduire, voire supprimer, l'obligation d'entretien, celle-ci restant conditionnée à une formation menée sérieusement et dans des délais raisonnables."}]}},
    'legitime-defense-etat-necessite-droit-penal': {'domaine_id': 'droit_penal', 'published': '2026-08-02', 'fr': {'slug': 'legitime-defense-etat-necessite-droit-penal-suisse', 'title': 'Légitime défense et état de nécessité en droit pénal suisse', 'meta': "Repousser une attaque, agir face à un danger imminent : les conditions de la légitime défense (art. 15 CP) et de l'état de nécessité (art. 17-18 CP).", 'sections': [{'heading': 'La légitime défense', 'paragraphs': ["L'art. 15 CP autorise quiconque à repousser de manière appropriée une attaque illicite dirigée contre lui-même ou contre autrui, à condition que l'attaque soit imminente ou en cours. La réaction doit rester proportionnée à la gravité et à la nature de l'attaque : une riposte manifestement excessive n'est plus couverte par la légitime défense.", "L'art. 16 CP traite de l'excès de légitime défense : si la personne agressée dépasse les limites d'une défense appropriée, le juge peut atténuer la peine, voire y renoncer si cet excès provient d'un état excusable d'excitation ou de saisissement causé par l'attaque elle-même."]}, {'heading': "L'état de nécessité licite", 'paragraphs': ["L'art. 17 CP prévoit que quiconque commet un acte punissable pour préserver d'un danger imminent et impossible à détourner autrement un bien juridique lui appartenant ou appartenant à un tiers agit de manière licite, à condition que le sacrifice consenti soit proportionné aux intérêts en jeu. Cette justification suppose une véritable mise en balance entre le mal évité et le mal causé."]}, {'heading': "L'état de nécessité excusable", 'paragraphs': ["L'art. 18 CP couvre les situations où l'auteur agit pour préserver un bien juridique lui appartenant d'un danger imminent, mais sans que le sacrifice consenti soit proportionné aux intérêts en présence. Dans ce cas, l'acte reste illicite mais le juge atténue la peine si l'auteur pouvait raisonnablement se déterminer autrement, ou l'exempte de toute peine si l'on ne pouvait exiger de lui un comportement différent compte tenu des circonstances."]}, {'heading': 'Une appréciation toujours concrète', 'paragraphs': ["Ces notions ne s'appliquent jamais de manière automatique : les tribunaux examinent au cas par cas l'imminence du danger, l'absence d'alternative raisonnable et la proportionnalité de la réaction. Une personne qui invoque la légitime défense ou l'état de nécessité doit généralement pouvoir en démontrer les circonstances concrètes."]}], 'faq': [{'q': 'Puis-je invoquer la légitime défense si je réagis de façon disproportionnée à une agression ?', 'a': "Une réaction manifestement excessive sort du cadre de la légitime défense proprement dite, mais l'art. 16 CP permet une atténuation, voire une exemption de peine, si cet excès résulte d'un état excusable d'excitation ou de saisissement causé par l'attaque."}, {'q': 'Quelle est la différence entre état de nécessité licite et excusable ?', 'a': "L'état de nécessité licite (art. 17 CP) suppose que le sacrifice consenti soit proportionné aux intérêts en jeu, ce qui rend l'acte pleinement licite. L'état de nécessité excusable (art. 18 CP) s'applique lorsque cette proportionnalité fait défaut : l'acte reste illicite mais la peine peut être atténuée ou supprimée."}, {'q': "La légitime défense suppose-t-elle que l'attaque ait déjà commencé ?", 'a': "Elle couvre l'attaque imminente ou en cours, mais pas une menace future ou déjà terminée : agir après la fin de l'attaque relève d'une autre logique, souvent celle de la vengeance, qui n'est plus couverte par l'art. 15 CP."}]}},
    'sursis-peine-conditions-revocation': {'domaine_id': 'droit_penal', 'published': '2026-08-02', 'fr': {'slug': 'sursis-peine-conditions-revocation-suisse', 'title': 'Sursis et peine avec sursis : comment ça fonctionne', 'meta': "Sursis complet, sursis partiel, délai d'épreuve et révocation en cas de récidive : le fonctionnement du sursis à l'exécution de la peine en droit suisse.", 'sections': [{'heading': 'Le sursis complet', 'paragraphs': ["L'art. 42 CP permet au juge de suspendre entièrement l'exécution d'une peine pécuniaire, d'un travail d'intérêt général ou d'une peine privative de liberté ne dépassant en principe pas deux ans, lorsqu'il n'existe pas de pronostic défavorable quant au comportement futur du condamné. Le juge tient compte des antécédents, de la réputation et de la situation personnelle de l'auteur pour évaluer ce pronostic.", "Le sursis complet signifie que la peine n'est pas exécutée tant que le condamné respecte le délai d'épreuve fixé par le juge, en principe entre deux et cinq ans, éventuellement assorti de règles de conduite."]}, {'heading': 'Le sursis partiel', 'paragraphs': ["Pour une peine privative de liberté comprise entre un et trois ans, l'art. 43 CP permet un sursis partiel : une partie de la peine est suspendue et une autre partie doit être exécutée ferme, cette solution intermédiaire s'appliquant notamment lorsque le pronostic n'est ni clairement favorable ni clairement défavorable."]}, {'heading': "Le délai d'épreuve et les règles de conduite", 'paragraphs': ["Pendant le délai d'épreuve, le condamné peut être soumis à une assistance de probation ou à des règles de conduite, par exemple une obligation de suivre un traitement ou d'exercer une activité professionnelle régulière. Le non-respect de ces règles peut entraîner un avertissement, une prolongation du délai d'épreuve ou, dans les cas graves, la révocation du sursis."]}, {'heading': 'La révocation du sursis', 'paragraphs': ["Si le condamné commet un nouveau crime ou délit pendant le délai d'épreuve, le juge qui statue sur cette nouvelle infraction peut révoquer le sursis accordé précédemment si l'on doit s'attendre à ce que le condamné commette de nouvelles infractions pour contrer ce pronostic défavorable, ce qui entraîne l'exécution de la peine initialement suspendue, en plus de la nouvelle sanction."]}], 'faq': [{'q': "Un sursis signifie-t-il que je n'ai commis aucune infraction ?", 'a': "Non, le sursis suspend uniquement l'exécution de la peine : la condamnation elle-même reste inscrite, notamment au casier judiciaire selon les règles applicables à ce type d'inscription."}, {'q': "Que se passe-t-il si je récidive pendant le délai d'épreuve ?", 'a': "Le juge saisi de la nouvelle infraction peut révoquer le sursis initial s'il estime que le pronostic est devenu défavorable, ce qui entraîne l'exécution de la peine suspendue en plus de la sanction pour les nouveaux faits."}, {'q': 'Le sursis partiel est-il automatique pour une peine de deux ans ?', 'a': "Non, le juge dispose d'un pouvoir d'appréciation : il choisit entre sursis complet, sursis partiel ou absence de sursis selon le pronostic concret porté sur le comportement futur du condamné, dans les limites fixées par les art. 42 et 43 CP."}]}},
    'sous-location-airbnb-loi-bail': {'domaine_id': 'droit_bail', 'published': '2026-08-03', 'fr': {'slug': 'sous-location-airbnb-consentement-bailleur', 'title': 'Sous-location et Airbnb : ce que dit la loi', 'meta': "Consentement du bailleur, motifs de refus, risques en cas de sous-location non autorisée : le régime de l'art. 262 CO appliqué aux locations courte durée.", 'sections': [{'heading': 'Le principe : un consentement nécessaire', 'paragraphs': ["L'art. 262 CO permet au locataire de sous-louer tout ou partie de son logement, mais seulement avec le consentement du bailleur. Ce consentement n'est toutefois pas purement discrétionnaire : le bailleur ne peut le refuser que pour des motifs précis prévus par la loi.", 'Le bailleur peut ainsi refuser si le locataire refuse de lui communiquer les conditions de la sous-location, si ces conditions sont abusives par rapport à celles du bail principal, si la sous-location présente pour lui des inconvénients majeurs, ou si le logement est sous-loué pour une durée notablement plus longue que celle du bail principal.']}, {'heading': 'Le cas particulier des locations de courte durée', 'paragraphs': ["Louer son appartement pour quelques nuits via une plateforme de type Airbnb constitue une forme de sous-location au sens de l'art. 262 CO, même de très courte durée, et nécessite donc en principe l'accord préalable du bailleur. Une activité répétée et de nature quasi commerciale peut en outre constituer un inconvénient majeur justifiant un refus, notamment en raison du va-et-vient de personnes dans l'immeuble.", 'Certaines communes ou cantons imposent par ailleurs des règles complémentaires, parfois une autorisation spécifique ou des restrictions selon le zonage, indépendamment du droit du bail lui-même.']}, {'heading': "Les conséquences d'une sous-location non autorisée", 'paragraphs': ["Sous-louer sans en informer le bailleur ou malgré son refus justifié constitue une violation des obligations du locataire, qui peut recevoir un avis comminatoire puis, en cas de persistance, une résiliation du bail principal. Dans les cas les plus graves, une résiliation immédiate pour justes motifs au sens de l'art. 257f CO peut même être envisagée par le bailleur."]}, {'heading': 'La responsabilité du locataire principal', 'paragraphs': ["Même une sous-location valablement autorisée ne libère pas le locataire principal de ses obligations envers le bailleur : il répond de l'usage fait des locaux par le sous-locataire comme du sien propre, ce qui suppose de bien encadrer contractuellement la relation avec les personnes accueillies."]}], 'faq': [{'q': 'Puis-je louer mon appartement sur Airbnb sans en parler à mon bailleur ?', 'a': "Non, une location de courte durée constitue juridiquement une sous-location, qui nécessite en principe le consentement préalable du bailleur au sens de l'art. 262 CO."}, {'q': 'Le bailleur peut-il refuser une sous-location sans raison ?', 'a': "Non, la loi limite les motifs de refus admissibles : conditions abusives, inconvénients majeurs pour le bailleur, ou durée notablement plus longue que celle du bail principal. Un refus arbitraire, hors de ces motifs, n'est en principe pas valable."}, {'q': 'Que risque un locataire qui sous-loue sans autorisation ?', 'a': "Il s'expose à un avis comminatoire puis, en cas de persistance, à une résiliation ordinaire ou, dans les cas graves, à une résiliation immédiate du bail pour justes motifs."}]}},
    'garantie-loyer-montant-formes-restitution': {'domaine_id': 'droit_bail', 'published': '2026-08-03', 'fr': {'slug': 'garantie-loyer-montant-formes-restitution', 'title': 'Garantie de loyer : montant, formes et restitution', 'meta': "Plafond légal de trois mois, compte de garantie bloqué au nom du locataire, restitution un an après le départ : ce que prévoit l'art. 257e CO.", 'sections': [{'heading': 'Le plafond légal', 'paragraphs': ["Pour un logement, l'art. 257e CO plafonne la garantie de loyer exigible par le bailleur à trois mois de loyer net, c'est-à-dire hors charges. Ce plafond est impératif : une clause contractuelle prévoyant un montant supérieur n'est pas valable pour la part excédentaire. Pour les locaux commerciaux, ce plafond légal spécifique ne s'applique en revanche pas."]}, {'heading': 'Les formes de garantie', 'paragraphs': ["La garantie prend le plus souvent la forme d'un dépôt en espèces déposé sur un compte bancaire séparé, ouvert au nom du locataire et bloqué au profit du bailleur. D'autres formes existent en pratique, comme la caution bancaire ou l'assurance de garantie de loyer, qui évitent au locataire d'immobiliser une somme importante mais impliquent une prime périodique non remboursable.", 'Quelle que soit la forme choisie, le compte ou la garantie doit rester identifiable comme appartenant au locataire, et non se confondre avec le patrimoine du bailleur.']}, {'heading': 'Les intérêts', 'paragraphs': ["Les intérêts produits par le compte de garantie reviennent au locataire, et non au bailleur, et s'ajoutent en principe au capital garanti au fil du temps."]}, {'heading': 'La restitution en fin de bail', 'paragraphs': ["À la fin du bail, le bailleur dispose d'un délai d'une année pour faire valoir une prétention contre le locataire, par exemple pour des dégâts constatés lors de l'état des lieux de sortie ou des loyers impayés. Passé ce délai, si aucune prétention n'a été formulée ou qu'aucune procédure n'est en cours, le locataire peut exiger la libération intégrale de la garantie, en s'adressant le cas échéant directement à la banque avec l'accord du bailleur ou une décision judiciaire."]}], 'faq': [{'q': 'Le bailleur peut-il exiger plus de trois mois de loyer comme garantie ?', 'a': "Non pour un logement : l'art. 257e CO plafonne la garantie à trois mois de loyer net, une clause prévoyant davantage étant nulle pour la part excédentaire."}, {'q': 'Qui reçoit les intérêts du compte de garantie ?', 'a': "Les intérêts reviennent au locataire, propriétaire économique de la garantie, et viennent s'ajouter au montant garanti."}, {'q': 'Combien de temps le bailleur peut-il retenir la garantie après mon départ ?', 'a': "En principe jusqu'à un an après la fin du bail pour faire valoir une prétention. Passé ce délai sans réclamation ni procédure en cours, la garantie doit en principe être restituée intégralement."}]}},
    'norme-sia-118-maitre-ouvrage': {'domaine_id': 'droit_construction', 'published': '2026-08-03', 'fr': {'slug': 'norme-sia-118-maitre-ouvrage-consequences', 'title': "Norme SIA 118 : ce qu'elle change pour le maître d'ouvrage", 'meta': "Conditions générales pour l'exécution des travaux, applicable seulement si intégrée au contrat : ce que la norme SIA 118 modifie par rapport au CO.", 'sections': [{'heading': 'Une norme contractuelle, pas une loi', 'paragraphs': ["La norme SIA 118 est un ensemble de conditions générales élaborées par la Société suisse des ingénieurs et des architectes pour régir l'exécution des travaux de construction. Elle n'a aucune force légale automatique : elle ne s'applique que si les parties l'intègrent expressément à leur contrat d'entreprise, généralement par simple référence dans le contrat signé avec l'entrepreneur.", "En l'absence d'une telle référence, c'est le régime ordinaire du contrat d'entreprise prévu par les art. 363 et suivants CO qui s'applique seul, avec des règles parfois sensiblement différentes."]}, {'heading': 'Les différences principales avec le régime du CO', 'paragraphs': ["La norme SIA 118 modifie notamment les règles relatives à l'avis des défauts : elle prévoit généralement une obligation de vérification et de signalement plus rapide de l'ouvrage après sa réception, avec des délais de garantie propres, différents de ceux du droit ordinaire du contrat d'entreprise.", "Elle encadre également la réception de l'ouvrage par une procédure formalisée, ainsi que les modalités de résiliation, de facturation intermédiaire et de règlement des différends, souvent par le biais d'une procédure d'expertise ou d'arbitrage propre au secteur de la construction."]}, {'heading': "Ce que cela implique pour le maître d'ouvrage", 'paragraphs': ["Un maître d'ouvrage qui accepte l'intégration de la norme SIA 118 dans son contrat doit être attentif aux délais de vérification et d'avis des défauts, souvent plus courts et plus stricts que ceux qu'il pourrait imaginer intuitivement, sous peine de perdre certains droits en cas de défaut non signalé à temps.", "Il est donc recommandé de faire réviser le contrat par un professionnel avant signature, en particulier lorsque la norme SIA 118 est associée à des clauses complémentaires ou dérogatoires négociées avec l'entrepreneur."]}, {'heading': 'Faut-il toujours accepter son intégration', 'paragraphs': ["L'intégration de la norme SIA 118 n'est pas systématiquement défavorable au maître d'ouvrage : elle offre un cadre standardisé et éprouvé, reconnu par l'ensemble du secteur, ce qui peut faciliter le dialogue avec des entrepreneurs habitués à cette norme. L'essentiel est d'en comprendre les implications concrètes avant de signer, plutôt que de la considérer comme une simple formalité."]}], 'faq': [{'q': "La norme SIA 118 s'applique-t-elle automatiquement à tout contrat de construction ?", 'a': "Non, elle ne s'applique que si le contrat y fait expressément référence. Sans cette intégration contractuelle, c'est le régime ordinaire des art. 363 et suivants CO qui régit seul la relation."}, {'q': "La norme SIA 118 est-elle plus favorable au maître d'ouvrage ou à l'entrepreneur ?", 'a': "Elle établit un équilibre différent de celui du Code des obligations, avec notamment des délais d'avis des défauts souvent plus courts. Son intérêt dépend largement du projet et des clauses complémentaires négociées."}, {'q': 'Que se passe-t-il si je ne signale pas un défaut dans les délais prévus par la norme SIA 118 ?', 'a': "Un défaut non signalé dans les délais applicables peut être considéré comme accepté, ce qui peut faire perdre au maître d'ouvrage le droit de réclamer une réparation ou une réduction de prix pour ce défaut."}]}},
    'retard-chantier-penalites-recours': {'domaine_id': 'droit_construction', 'published': '2026-08-03', 'fr': {'slug': 'retard-chantier-penalites-recours-suisse', 'title': 'Retard de chantier : pénalités et recours', 'meta': "Mise en demeure, clause pénale, résiliation du contrat d'entreprise : les recours du maître d'ouvrage face à un retard de chantier imputable à l'entrepreneur.", 'sections': [{'heading': "Quand l'entrepreneur est-il en retard", 'paragraphs': ["Le contrat d'entreprise fixe généralement un délai d'exécution, contractuel ou à défaut raisonnable au regard de la nature des travaux. Lorsque ce délai n'est pas respecté sans motif justifié, l'entrepreneur tombe en demeure, ce qui ouvre au maître d'ouvrage plusieurs voies d'action selon la gravité et les conséquences du retard."]}, {'heading': 'La clause pénale de retard', 'paragraphs': ["De nombreux contrats de construction prévoient une clause pénale fixant un montant, souvent journalier ou hebdomadaire, dû par l'entrepreneur en cas de dépassement du délai convenu. Cette clause dispense en principe le maître d'ouvrage de devoir prouver l'existence et l'étendue exacte de son dommage, tout en plafonnant généralement le montant total exigible, sauf clause contraire.", "Le juge conserve toutefois la faculté de réduire une peine conventionnelle qu'il estimerait excessive, en application des principes généraux du droit des contrats."]}, {'heading': 'Les dommages-intérêts pour retard', 'paragraphs': ["En l'absence de clause pénale, le maître d'ouvrage peut réclamer réparation du dommage effectivement subi en raison du retard, selon les règles générales de la demeure du débiteur (art. 102 et suivants CO), ce qui suppose d'en établir l'existence et le montant, par exemple des frais de logement provisoire ou une perte de loyer."]}, {'heading': 'La résiliation anticipée du contrat', 'paragraphs': ["Dans les cas les plus graves, notamment lorsque le retard rend hautement probable que l'ouvrage ne sera pas achevé à temps ou que des défauts sérieux se dessinent, l'art. 366 CO permet au maître d'ouvrage de résilier le contrat avant l'achèvement de l'ouvrage, sans attendre l'échéance du délai. Cette faculté doit s'exercer avec prudence, une résiliation injustifiée exposant le maître d'ouvrage à ses propres responsabilités contractuelles.", "Avant d'en arriver là, une mise en demeure écrite fixant un délai supplémentaire raisonnable reste généralement la première étape, suivie le cas échéant d'une expertise permettant de documenter précisément l'état d'avancement du chantier."]}], 'faq': [{'q': 'Ai-je automatiquement droit à une indemnité en cas de retard de chantier ?', 'a': "Seulement si le retard est imputable à l'entrepreneur et que vous pouvez établir un dommage, sauf si une clause pénale de retard a été prévue au contrat, auquel cas vous n'avez en principe pas à prouver le montant exact du préjudice."}, {'q': 'Puis-je résilier le contrat si le chantier prend trop de retard ?', 'a': "Oui, dans certaines conditions : l'art. 366 CO permet une résiliation anticipée lorsque le retard rend hautement probable un achèvement hors délai, mais cette faculté doit être exercée avec prudence pour éviter d'engager sa propre responsabilité en cas de résiliation injustifiée."}, {'q': 'Le juge peut-il réduire une clause pénale de retard jugée trop élevée ?', 'a': "Oui, les tribunaux disposent d'un pouvoir de réduction des peines conventionnelles qu'ils estiment excessives, indépendamment du montant fixé au contrat par les parties."}]}},
    'pacte-successoral-contenu-validite': {'domaine_id': 'droit_successions', 'published': '2026-08-04', 'fr': {'slug': 'pacte-successoral-contenu-validite-forme', 'title': 'Pacte successoral : contenu et validité', 'meta': "Institution d'héritier, legs, renonciation à une succession future : forme notariée obligatoire et caractère en principe irrévocable du pacte successoral.", 'sections': [{'heading': 'Un contrat, pas un acte unilatéral', 'paragraphs': ['Contrairement au testament, qui est un acte unilatéral révocable en tout temps, le pacte successoral est un véritable contrat conclu entre le disposant et un ou plusieurs héritiers ou tiers, régi par les art. 512 et suivants CC. Cette nature contractuelle en fait un outil de planification successorale plus stable, mais aussi plus contraignant.']}, {'heading': 'Les deux grandes catégories', 'paragraphs': ["Le pacte successoral positif institue un ou plusieurs héritiers, fixe des legs ou d'autres dispositions pour cause de mort, de façon contractuelle plutôt que par testament. Le pacte de renonciation, à l'inverse, permet à un héritier de renoncer par avance, en tout ou en partie, à sa succession future, généralement contre une contre-prestation reçue du vivant du disposant."]}, {'heading': 'La forme authentique obligatoire', 'paragraphs': ['Le pacte successoral doit être passé en la forme authentique, devant notaire, avec la présence de deux témoins, sous les mêmes conditions de forme que le testament public. Cette exigence stricte vise à garantir la réflexion et la liberté de consentement des parties sur un acte aux conséquences potentiellement lourdes et durables.']}, {'heading': 'Le caractère en principe irrévocable', 'paragraphs': ["À la différence du testament, le pacte successoral ne peut en principe pas être révoqué unilatéralement par le disposant une fois conclu, sauf si le contrat lui-même réserve cette possibilité, ou dans des cas exceptionnels prévus par la loi, comme l'indignité de l'héritier institué. Cette irrévocabilité de principe en fait un engagement à ne pas prendre à la légère, mais aussi un outil précieux pour sécuriser une transmission convenue entre les parties, par exemple dans le cadre d'une succession d'entreprise familiale."]}], 'faq': [{'q': 'Un pacte successoral peut-il être annulé unilatéralement par le disposant ?', 'a': "En principe non, sauf clause contractuelle le prévoyant expressément, ou dans des cas exceptionnels prévus par la loi tels que l'indignité de l'héritier institué."}, {'q': 'Faut-il obligatoirement passer devant un notaire pour conclure un pacte successoral ?', 'a': 'Oui, la forme authentique est une condition de validité impérative, avec la présence de deux témoins, selon les mêmes règles de forme que le testament public.'}, {'q': 'Quelle est la différence entre un pacte successoral et un testament ?', 'a': 'Le testament est un acte unilatéral révocable librement par son auteur en tout temps, tandis que le pacte successoral est un contrat conclu avec un ou plusieurs héritiers ou tiers, en principe irrévocable une fois signé.'}]}},
    'executeur-testamentaire-role-designation': {'domaine_id': 'droit_successions', 'published': '2026-08-04', 'fr': {'slug': 'executeur-testamentaire-role-designation-mission', 'title': 'Exécuteur testamentaire : rôle et désignation', 'meta': "Administrer la succession, payer les dettes, exécuter les legs : le rôle de l'exécuteur testamentaire désigné selon les art. 517-518 CC.", 'sections': [{'heading': 'La désignation', 'paragraphs': ["L'art. 517 CC permet à toute personne de désigner, par disposition testamentaire, une ou plusieurs personnes chargées d'exécuter ses dernières volontés. L'exécuteur testamentaire peut être un proche, un héritier, ou un professionnel indépendant tel qu'un avocat ou un notaire, selon la complexité de la succession envisagée.", "La personne désignée n'est pas obligée d'accepter le mandat : elle doit en principe communiquer sa décision à l'autorité compétente dans un délai raisonnable après avoir eu connaissance de sa nomination."]}, {'heading': "L'étendue de la mission", 'paragraphs': ["Sauf disposition contraire du testateur, l'art. 518 CC confère à l'exécuteur testamentaire les pouvoirs d'administrer la succession, de payer les dettes, d'exécuter les legs et de procéder au partage conformément à la volonté du défunt ou, à défaut d'indication, selon les règles légales. Il agit avec les droits et les obligations d'un représentant de la succession."]}, {'heading': 'Les rapports avec les héritiers', 'paragraphs': ["Tant que sa mission n'est pas achevée, les héritiers ne peuvent en principe pas disposer librement des biens soumis à l'administration de l'exécuteur testamentaire, ce qui peut limiter leur marge de manœuvre, notamment en cas de désaccord sur la manière dont la succession est gérée. L'exécuteur doit rendre compte de sa gestion et agir dans l'intérêt de la succession, avec la diligence requise."]}, {'heading': 'La rémunération et la fin de la mission', 'paragraphs': ["L'exécuteur testamentaire a droit à une indemnité équitable pour son activité, sauf s'il s'agit d'un mandat gratuit expressément prévu. Sa mission prend fin une fois la succession liquidée et partagée conformément aux dernières volontés, ou peut être révoquée par l'autorité compétente en cas de manquement grave à ses devoirs."]}], 'faq': [{'q': 'Un héritier peut-il être désigné comme exécuteur testamentaire ?', 'a': "Oui, rien n'empêche de désigner un héritier, un proche ou un professionnel externe. Le choix appartient entièrement au testateur, qui peut aussi prévoir plusieurs exécuteurs conjoints."}, {'q': "Les héritiers peuvent-ils s'opposer aux décisions de l'exécuteur testamentaire ?", 'a': "Ils peuvent contester une gestion contraire à la loi ou aux volontés du défunt devant l'autorité compétente, mais ne peuvent en principe pas disposer librement des biens soumis à l'administration de l'exécuteur tant que sa mission dure."}, {'q': "L'exécuteur testamentaire est-il rémunéré ?", 'a': 'En principe oui : il a droit à une indemnité équitable pour son activité, sauf disposition contraire prévoyant un mandat gratuit.'}]}},
    'vices-consentement-erreur-dol-crainte': {'domaine_id': 'droit_contrats', 'published': '2026-08-04', 'fr': {'slug': 'vices-consentement-erreur-dol-crainte-fondee', 'title': 'Vices du consentement : erreur, dol et crainte fondée', 'meta': "Contrat conclu par erreur, tromperie ou sous la menace : les conditions de l'invalidation d'un contrat pour vice du consentement selon les art. 23-31 CO.", 'sections': [{'heading': "L'erreur essentielle", 'paragraphs': ["L'art. 24 CO définit les cas d'erreur essentielle permettant d'invalider un contrat : erreur sur la nature du contrat, sur son objet, sur la personne du cocontractant lorsque celle-ci était déterminante, ou sur des faits que la partie qui se trompe considérait de bonne foi, selon les règles de la loyauté en affaires, comme un élément nécessaire du contrat.", "Une simple erreur sur les motifs qui ont conduit à contracter, sans porter sur un élément objectivement essentiel, ne suffit en revanche pas à invalider l'accord."]}, {'heading': 'Le dol', 'paragraphs': ["L'art. 28 CO vise la partie qui a été amenée à contracter par la tromperie intentionnelle de son cocontractant, ou d'un tiers si l'autre partie en avait connaissance ou aurait dû en avoir connaissance. Le dol peut résulter d'affirmations mensongères, mais aussi du silence gardé sur un fait que la loyauté imposait de révéler."]}, {'heading': 'La crainte fondée', 'paragraphs': ["Les art. 29 et 30 CO couvrent les situations où une partie a été amenée à contracter sous l'effet d'une crainte fondée, provoquée intentionnellement et illicitement par l'autre partie ou un tiers, en faisant naître la menace d'un danger grave et imminent pour elle-même, ses proches ou ses biens."]}, {'heading': 'Les conséquences et le délai pour agir', 'paragraphs': ["Un contrat entaché d'un de ces vices n'est pas automatiquement nul : il reste valable tant que la partie lésée ne l'a pas invalidé. Selon l'art. 31 CO, celle-ci dispose d'un délai d'un an, dès la découverte de l'erreur ou du dol, ou dès la cessation de la crainte, pour déclarer invalider le contrat ou exécuter la prestation promise sous réserve de répétition. Passé ce délai sans réaction, le contrat est réputé ratifié."]}], 'faq': [{'q': 'Un contrat conclu par erreur est-il automatiquement nul ?', 'a': "Non, il reste valable tant que la partie lésée ne l'invalide pas expressément, dans un délai d'un an dès la découverte de l'erreur, conformément à l'art. 31 CO."}, {'q': 'Le silence peut-il constituer un dol ?', 'a': "Oui, taire un fait que la loyauté en affaires imposait de révéler peut constituer un dol au sens de l'art. 28 CO, au même titre qu'une affirmation mensongère active."}, {'q': "Que se passe-t-il si je découvre l'erreur plus d'un an après avoir signé le contrat ?", 'a': "Le délai d'un an pour invalider le contrat court dès la découverte de l'erreur, et non dès la signature. Passé ce délai depuis la découverte, le contrat est en principe réputé ratifié et ne peut plus être invalidé pour ce motif."}]}},
    'demeure-debiteur-mise-en-demeure-consequences': {'domaine_id': 'droit_contrats', 'published': '2026-08-04', 'fr': {'slug': 'demeure-debiteur-mise-en-demeure-consequences', 'title': 'Demeure du débiteur : mise en demeure et conséquences', 'meta': 'Interpellation, intérêts moratoires, résolution du contrat : les conséquences de la demeure du débiteur selon les art. 102 et suivants CO.', 'sections': [{'heading': 'Quand le débiteur tombe-t-il en demeure', 'paragraphs': ["L'art. 102 CO prévoit que le débiteur d'une obligation exigible ne tombe en demeure, en principe, qu'après avoir été interpellé par le créancier, c'est-à-dire sommé de s'exécuter. Une exception importante existe toutefois lorsqu'un terme précis a été fixé pour l'exécution : dans ce cas, la demeure survient automatiquement dès l'échéance de ce terme, sans qu'une interpellation supplémentaire soit nécessaire."]}, {'heading': 'Les intérêts moratoires', 'paragraphs': ["Dès qu'il est en demeure pour le paiement d'une somme d'argent, le débiteur doit des intérêts moratoires, fixés à 5% l'an sauf taux conventionnel différent ou taux usuel supérieur (art. 104 CO). Ces intérêts sont dus indépendamment de toute faute du débiteur et même si le créancier ne prouve aucun dommage particulier."]}, {'heading': 'Les dommages-intérêts pour retard', 'paragraphs': ["Au-delà des intérêts moratoires, le créancier peut réclamer réparation d'un dommage supplémentaire effectivement subi en raison du retard, à condition de l'établir, sauf si le débiteur prouve qu'aucune faute ne lui est imputable dans ce retard."]}, {'heading': 'La résolution du contrat', 'paragraphs': ["Dans les contrats bilatéraux, les art. 107 à 109 CO permettent au créancier, après avoir fixé au débiteur en demeure un délai convenable pour s'exécuter, de renoncer à l'exécution tardive et de se départir du contrat, réclamant alors la restitution des prestations déjà fournies et, le cas échéant, des dommages-intérêts pour inexécution plutôt que pour simple retard. Ce délai supplémentaire n'est pas nécessaire lorsqu'il ressort de l'attitude du débiteur qu'il serait inutile de le fixer, ou lorsque l'exécution tardive serait sans intérêt pour le créancier."]}], 'faq': [{'q': 'Dois-je toujours envoyer une sommation pour mettre mon débiteur en demeure ?', 'a': "Pas si un terme précis a été fixé au contrat pour l'exécution : la demeure survient alors automatiquement à l'échéance. Une interpellation n'est nécessaire que si aucun terme précis n'avait été convenu."}, {'q': 'Ai-je droit à des intérêts moratoires même sans prouver de dommage ?', 'a': "Oui, les intérêts moratoires de l'art. 104 CO sont dus dès la demeure pour le paiement d'une somme d'argent, sans que le créancier ait à démontrer l'existence ou l'étendue d'un dommage."}, {'q': "Puis-je résilier un contrat simplement parce que l'autre partie est en retard ?", 'a': "En principe, il faut d'abord lui fixer un délai supplémentaire convenable pour s'exécuter avant de pouvoir se départir du contrat, sauf si ce délai apparaît manifestement inutile au vu des circonstances."}]}},
    'raison-individuelle-sarl-sa-comparaison': {'domaine_id': 'droit_societes', 'published': '2026-08-05', 'fr': {'slug': 'raison-individuelle-sarl-sa-comparaison-suisse', 'title': 'Raison individuelle, Sàrl ou SA : quelle forme choisir', 'meta': 'Capital minimum, responsabilité, confidentialité, formalités : comparatif des trois formes juridiques les plus courantes pour lancer une activité en Suisse.', 'sections': [{'heading': 'La raison individuelle', 'paragraphs': ["La raison individuelle ne requiert aucun capital minimum et peut être créée sans grande formalité, l'inscription au registre du commerce ne devenant obligatoire qu'à partir d'un chiffre d'affaires annuel de CHF 100'000. Sa contrepartie est une responsabilité illimitée : l'entrepreneur répond des dettes de son activité sur l'ensemble de son patrimoine personnel, y compris ses biens privés.", 'Cette forme convient généralement à une activité individuelle à risque limité, où la simplicité administrative prime sur la protection patrimoniale.']}, {'heading': 'La société à responsabilité limitée (Sàrl)', 'paragraphs': ["La Sàrl exige un capital social minimum de CHF 20'000, entièrement libéré à la constitution. La responsabilité des associés se limite en principe à leurs apports, ce qui protège leur patrimoine personnel des dettes de la société. Les associés sont en revanche inscrits nominativement au registre du commerce, ce qui limite la confidentialité par rapport à une société anonyme."]}, {'heading': 'La société anonyme (SA)', 'paragraphs': ["La SA requiert un capital minimum de CHF 100'000, dont au moins CHF 50'000 doivent être libérés à la constitution. Elle offre une meilleure confidentialité, les actionnaires n'étant en principe pas publiés au registre du commerce, ainsi qu'une structure plus adaptée à des projets ambitieux ou à l'entrée future d'investisseurs. Cette souplesse a pour contrepartie une gouvernance plus lourde, avec un conseil d'administration et, selon la taille de la société, une obligation de révision."]}, {'heading': 'Comment choisir', 'paragraphs': ["Le choix dépend du niveau de risque de l'activité, du besoin de protection patrimoniale, du capital disponible au démarrage et des perspectives de développement, notamment l'arrivée d'associés ou d'investisseurs externes. Une raison individuelle peut être transformée ultérieurement en Sàrl ou en SA à mesure que l'activité se développe, ce qui permet souvent de démarrer simplement avant de structurer davantage le projet."]}], 'faq': [{'q': 'Puis-je créer une Sàrl seul, sans associé ?', 'a': 'Oui, une Sàrl peut être constituée par une seule personne, tout comme une société anonyme peut avoir un actionnaire unique.'}, {'q': 'Quelle forme protège le mieux mon patrimoine personnel ?', 'a': "La Sàrl et la SA limitent en principe la responsabilité au capital de la société, contrairement à la raison individuelle où l'entrepreneur répond des dettes sur l'ensemble de ses biens personnels."}, {'q': 'Peut-on transformer une raison individuelle en Sàrl plus tard ?', 'a': "Oui, il est courant de démarrer en raison individuelle pour limiter les formalités initiales, puis de transférer l'activité vers une Sàrl ou une SA lorsque le volume d'activité ou le besoin de protection patrimoniale le justifie."}]}},
    'dissolution-liquidation-societe-suisse': {'domaine_id': 'droit_societes', 'published': '2026-08-05', 'fr': {'slug': 'dissolution-liquidation-societe-suisse-procedure', 'title': "Dissolution et liquidation d'une société en Suisse", 'meta': "Décision de l'assemblée générale, appel aux créanciers, radiation du registre du commerce : les étapes de la dissolution et de la liquidation d'une société.", 'sections': [{'heading': 'Les causes de dissolution', 'paragraphs': ["Une société peut être dissoute par une décision de l'assemblée générale, à l'échéance d'une durée statutaire limitée, par un jugement de faillite, ou pour d'autres motifs prévus par la loi ou les statuts. La dissolution ouvre la phase de liquidation, sauf en cas de fusion, transformation ou reprise par un autre sujet de droit qui suivent des règles particulières."]}, {'heading': 'La société en liquidation', 'paragraphs': ["Une fois dissoute, la société ne disparaît pas immédiatement : elle continue d'exister durant la liquidation, avec la mention en liquidation ajoutée à sa raison sociale. Un ou plusieurs liquidateurs, souvent les administrateurs en fonction sauf décision contraire, sont chargés de mener les opérations jusqu'à leur terme."]}, {'heading': "L'appel aux créanciers et le règlement des dettes", 'paragraphs': ["Les liquidateurs réalisent l'actif de la société, encaissent les créances et paient les dettes. Une publication officielle, généralement à trois reprises, informe les créanciers de la dissolution et les invite à produire leurs prétentions dans un délai déterminé, ce qui protège la société contre des réclamations tardives une fois la répartition effectuée."]}, {'heading': 'La répartition du solde et la radiation', 'paragraphs': ['Une fois toutes les dettes réglées, le solde éventuel de la liquidation est réparti entre les ayants droit selon les règles statutaires et légales applicables. La liquidation achevée, la société est radiée du registre du commerce, ce qui met fin à son existence juridique.']}], 'faq': [{'q': "Une société dissoute cesse-t-elle immédiatement d'exister ?", 'a': "Non, elle continue d'exister durant toute la phase de liquidation, sous la mention en liquidation, jusqu'à sa radiation définitive du registre du commerce."}, {'q': "Pourquoi une publication officielle est-elle nécessaire lors d'une liquidation ?", 'a': "Elle permet d'informer les créanciers potentiels et de leur fixer un délai pour produire leurs prétentions, protégeant ainsi la société et ses ayants droit contre des réclamations tardives une fois les actifs répartis."}, {'q': 'Qui peut être désigné comme liquidateur ?', 'a': "En principe les administrateurs en fonction au moment de la dissolution, sauf décision contraire de l'assemblée générale désignant d'autres personnes pour mener les opérations de liquidation."}]}},
    'alcool-volant-taux-sanctions-retrait-permis': {'domaine_id': 'droit_circulation', 'published': '2026-08-05', 'fr': {'slug': 'alcool-volant-taux-sanctions-retrait-permis-suisse', 'title': 'Alcool au volant : taux, sanctions et retrait de permis', 'meta': "Ébriété simple, ébriété qualifiée, conducteurs novices : les seuils d'alcoolémie et les conséquences pénales et administratives en droit suisse.", 'sections': [{'heading': "Les seuils d'alcoolémie", 'paragraphs': ["La législation sur la circulation routière distingue plusieurs seuils d'alcoolémie. Dès 0,5 pour mille, on parle d'ébriété simple. Dès 0,8 pour mille, il s'agit d'ébriété qualifiée, entraînant des conséquences pénales et administratives plus sévères. Pour les nouveaux titulaires du permis en période probatoire, ainsi que pour certains conducteurs professionnels, des règles plus strictes s'appliquent, avec une tolérance quasiment nulle."]}, {'heading': 'Les sanctions pénales', 'paragraphs': ["Conduire en état d'ébriété expose à une amende ou une peine pécuniaire, dont la sévérité augmente avec le taux d'alcoolémie constaté et les antécédents du conducteur. L'ébriété qualifiée est traitée plus sévèrement que l'ébriété simple, et une récidive dans un délai rapproché aggrave généralement encore la sanction retenue."]}, {'heading': 'Le retrait de permis', 'paragraphs': ["En parallèle de la sanction pénale, l'autorité administrative cantonale prononce un retrait du permis de conduire, dont la durée dépend de la gravité de l'infraction, du taux d'alcoolémie et des antécédents du conducteur. Ce retrait est une mesure administrative distincte de la sanction pénale, prononcée par une autorité différente selon une procédure propre.", "En cas de récidive ou de taux particulièrement élevé, l'autorité peut également ordonner une expertise visant à évaluer l'aptitude à la conduite, condition parfois nécessaire à la restitution du permis."]}, {'heading': 'Que faire en cas de contrôle positif', 'paragraphs': ["Un contrôle d'alcoolémie positif ouvre en principe un délai pour contester la mesure de retrait devant l'autorité compétente. Faire appel à un avocat rapidement permet de vérifier la régularité du contrôle effectué et d'évaluer les chances de contestation, notamment lorsque des doutes existent sur la fiabilité de la mesure ou les circonstances du contrôle."]}], 'faq': [{'q': 'Quelle est la différence entre ébriété simple et ébriété qualifiée ?', 'a': "L'ébriété simple correspond à un taux dès 0,5 pour mille, l'ébriété qualifiée à un taux dès 0,8 pour mille, cette dernière entraînant des sanctions pénales et administratives plus sévères."}, {'q': 'Le retrait de permis est-il automatique après un contrôle positif ?', 'a': "Le retrait est prononcé par l'autorité administrative cantonale selon la gravité de l'infraction constatée. Sa durée varie selon le taux d'alcoolémie, les circonstances et les antécédents du conducteur."}, {'q': 'Puis-je contester un retrait de permis ?', 'a': "Oui, un recours est en principe possible devant l'autorité compétente dans un délai déterminé. Il est recommandé de consulter rapidement un avocat pour évaluer les chances de succès d'une contestation."}]}},
    'leasing-automobile-litige-resiliation': {'domaine_id': 'droit_circulation', 'published': '2026-08-05', 'fr': {'slug': 'leasing-automobile-litige-resiliation-anticipee', 'title': 'Leasing automobile : litiges et résiliation anticipée', 'meta': "Loi sur le crédit à la consommation, indemnité de résiliation, valeur résiduelle : ce qu'il faut savoir avant de résilier un contrat de leasing de véhicule.", 'sections': [{'heading': 'La nature du contrat de leasing', 'paragraphs': ["Le leasing automobile est un contrat qui ne correspond ni exactement à un bail ni à une vente à crédit classique, mais qui emprunte des éléments aux deux. Lorsqu'il est conclu par un consommateur, il tombe généralement dans le champ d'application de la loi sur le crédit à la consommation, qui impose certaines obligations d'information et de transparence au bailleur, notamment sur le coût total du financement."]}, {'heading': 'Le droit de révocation', 'paragraphs': ["La loi sur le crédit à la consommation prévoit un droit de révocation dans un court délai après la signature, permettant au preneur de renoncer au contrat sans justification particulière. Ce délai et ses modalités précises figurent dans le contrat lui-même et méritent d'être vérifiés attentivement avant toute signature."]}, {'heading': 'La résiliation anticipée', 'paragraphs': ["Mettre fin à un contrat de leasing avant son terme est généralement possible mais coûteux : le preneur doit souvent verser une indemnité de résiliation couvrant la différence entre les mensualités restant dues et la valeur résiduelle du véhicule au moment de la résiliation. Les conditions générales du contrat définissent précisément ce calcul, qu'il est essentiel de lire avant de s'engager."]}, {'heading': 'Les recours en cas de litige', 'paragraphs': ["En cas de désaccord avec la société de leasing, notamment sur le montant réclamé à la résiliation ou sur l'état du véhicule restitué, une médiation auprès d'un organisme de conciliation du secteur automobile ou financier peut permettre de trouver une solution sans passer par une procédure judiciaire. À défaut d'accord, une action civile reste possible devant le tribunal compétent."]}], 'faq': [{'q': "Puis-je annuler un contrat de leasing juste après l'avoir signé ?", 'a': 'Un droit de révocation existe généralement dans un court délai après la signature, sous réserve des conditions et du délai précis fixés par le contrat et la loi sur le crédit à la consommation.'}, {'q': 'Résilier un leasing avant son terme coûte-t-il cher ?', 'a': 'Généralement oui : une indemnité couvrant la différence entre les mensualités restantes et la valeur résiduelle du véhicule est en principe due, selon les modalités prévues par les conditions générales du contrat.'}, {'q': "Que faire en cas de désaccord avec la société de leasing sur l'état du véhicule restitué ?", 'a': "Une médiation auprès d'un organisme de conciliation compétent peut être tentée avant d'envisager une action civile devant le tribunal compétent."}]}},
    'effet-suspensif-recours-administratif': {'domaine_id': 'droit_administratif', 'published': '2026-08-06', 'fr': {'slug': 'effet-suspensif-recours-administratif-suisse', 'title': "Effet suspensif d'un recours administratif", 'meta': "Une décision attaquée reste-t-elle exécutoire pendant le recours ? Principe de l'effet suspensif, retrait et restitution en droit administratif suisse.", 'sections': [{'heading': "Le principe de l'effet suspensif", 'paragraphs': ["En principe, un recours ordinaire déployé contre une décision administrative a un effet suspensif : la décision attaquée n'est pas exécutoire tant que l'autorité de recours ne s'est pas prononcée définitivement. Ce principe protège le recourant contre l'exécution d'une décision dont la validité est encore contestée."]}, {'heading': "Le retrait de l'effet suspensif", 'paragraphs': ["La loi ou l'autorité qui a rendu la décision peut prévoir ou ordonner le retrait de l'effet suspensif, généralement pour des motifs d'intérêt public, d'urgence ou de sécurité, lorsque l'exécution immédiate de la décision paraît nécessaire malgré le recours pendant. Ce retrait doit en principe être motivé et respecter le principe de proportionnalité."]}, {'heading': "La restitution de l'effet suspensif", 'paragraphs': ["Lorsque l'effet suspensif a été retiré, le recourant peut demander sa restitution à l'autorité de recours, qui procède alors à une pesée des intérêts en présence entre l'intérêt public à une exécution immédiate et l'intérêt privé du recourant à ne pas subir les conséquences d'une décision encore contestée."]}, {'heading': "L'importance pratique de cette question", 'paragraphs': ["La question de l'effet suspensif peut s'avérer décisive dans de nombreux litiges administratifs, par exemple en matière de retrait de permis, de fermeture d'établissement ou de mesures d'exécution immédiate, où l'issue du recours au fond peut arriver trop tard si la décision a déjà pu être exécutée entre-temps."]}], 'faq': [{'q': 'Une décision administrative attaquée peut-elle être exécutée pendant le recours ?', 'a': "En principe non, le recours ordinaire ayant un effet suspensif automatique, sauf si la loi en dispose autrement ou si l'autorité a expressément retiré cet effet pour des motifs d'intérêt public ou d'urgence."}, {'q': "Puis-je demander la restitution de l'effet suspensif s'il a été retiré ?", 'a': "Oui, cette demande s'adresse à l'autorité de recours, qui statue après une pesée des intérêts entre l'urgence de l'exécution et le préjudice que subirait le recourant."}, {'q': "Pourquoi l'effet suspensif est-il si important en pratique ?", 'a': "Parce que dans certains litiges, l'exécution immédiate d'une décision peut rendre le recours sans objet ou trop tardif, même si celui-ci aboutit finalement en faveur du recourant."}]}},
    'responsabilite-etat-collectivites-publiques': {'domaine_id': 'droit_administratif', 'published': '2026-08-06', 'fr': {'slug': 'responsabilite-etat-collectivites-publiques-suisse', 'title': "Responsabilité de l'État et des collectivités publiques", 'meta': "Acte illicite d'un agent public, dommage et lien de causalité : les conditions pour engager la responsabilité de l'État ou d'une commune en Suisse.", 'sections': [{'heading': 'Le principe de la responsabilité étatique', 'paragraphs': ["La responsabilité de la Confédération est régie par la loi sur la responsabilité (LRCF), tandis que les cantons et les communes disposent en principe de leurs propres lois cantonales analogues. Le principe commun est que l'État répond du dommage causé de manière illicite par ses agents dans l'exercice de leurs fonctions, sans que le lésé ait besoin de rechercher personnellement l'agent responsable."]}, {'heading': 'Les conditions de la responsabilité', 'paragraphs': ["Trois conditions sont généralement requises : un acte illicite commis par un agent de l'État dans l'exercice de ses fonctions, un dommage effectivement subi par le lésé, et un lien de causalité entre l'acte illicite et ce dommage. Contrairement à la responsabilité civile ordinaire, une faute de l'agent n'est en principe pas une condition nécessaire dans de nombreux régimes de responsabilité étatique, l'illicéité de l'acte suffisant."]}, {'heading': "L'action contre l'État plutôt que contre l'agent", 'paragraphs': ["Le lésé doit en principe diriger sa demande contre la collectivité publique elle-même, et non contre l'agent personnellement, ce qui simplifie sa position procédurale. Un recours interne de l'État contre l'agent fautif reste possible en cas de faute grave ou intentionnelle, mais cette question relève des rapports internes entre l'État et son agent, sans concerner directement le lésé."]}, {'heading': 'Les délais et la procédure', 'paragraphs': ["Les demandes en responsabilité contre l'État sont généralement soumises à des délais de prescription ou de péremption particuliers, souvent plus courts que ceux du droit civil ordinaire, ainsi qu'à des règles de compétence spécifiques selon qu'il s'agit de la Confédération, d'un canton ou d'une commune. Il est recommandé de consulter rapidement un avocat pour ne pas manquer ces délais souvent stricts."]}], 'faq': [{'q': "Dois-je agir contre l'agent public fautif ou contre l'État ?", 'a': "En principe contre l'État ou la collectivité publique concernée elle-même, et non contre l'agent personnellement, ce qui simplifie la position du lésé face à un dommage."}, {'q': "Faut-il prouver une faute de l'agent pour engager la responsabilité de l'État ?", 'a': "Pas nécessairement : de nombreux régimes de responsabilité étatique se contentent d'un acte illicite, sans exiger la preuve d'une faute personnelle de l'agent concerné."}, {'q': "Les délais pour agir contre l'État sont-ils les mêmes qu'en responsabilité civile ordinaire ?", 'a': "Non, ils sont souvent plus courts et spécifiques selon la collectivité publique concernée, ce qui justifie de consulter rapidement un avocat en cas de dommage imputable à l'État."}]}},
    'naturalisation-suisse-conditions-procedure': {'domaine_id': 'droit_etrangers', 'published': '2026-08-06', 'fr': {'slug': 'naturalisation-suisse-conditions-procedure-integration', 'title': 'Naturalisation en Suisse : conditions et procédure', 'meta': "Durée de séjour, critères d'intégration, niveau de langue requis : les conditions de la naturalisation ordinaire selon la loi sur la nationalité (LN).", 'sections': [{'heading': 'La durée de séjour requise', 'paragraphs': ["La naturalisation ordinaire suppose en principe dix ans de séjour en Suisse au bénéfice d'une autorisation d'établissement (permis C), les années passées entre 8 et 18 ans comptant double, ce qui peut réduire d'autant la durée effectivement nécessaire pour les personnes arrivées enfants ou adolescentes en Suisse."]}, {'heading': "Les critères d'intégration", 'paragraphs': ["La loi sur la nationalité de 2018 exige une intégration réussie, appréciée notamment à travers le respect de l'ordre juridique suisse, la participation à la vie économique ou l'acquisition d'une formation, l'encouragement de l'intégration des membres de la famille, ainsi que des connaissances linguistiques minimales dans une langue nationale, généralement fixées à un niveau oral A2 et écrit A1 selon le cadre européen commun de référence.", "L'absence de dépendance durable à l'aide sociale et l'absence de condamnations pénales significatives font également partie des éléments pris en compte par les autorités compétentes."]}, {'heading': 'Une procédure à trois niveaux', 'paragraphs': ["La naturalisation ordinaire implique une autorisation fédérale, puis un examen cantonal et communal, chaque niveau pouvant imposer des exigences complémentaires en matière de durée de résidence locale ou de procédure d'audition, dans les limites fixées par le droit fédéral. Cette structure explique pourquoi les délais et les modalités concrètes varient sensiblement d'un canton à l'autre."]}, {'heading': 'Les autres voies de naturalisation', 'paragraphs': ["Des voies facilitées existent pour certaines situations particulières, notamment pour le conjoint d'un ressortissant suisse remplissant des conditions de mariage et de séjour spécifiques, ou pour les enfants et petits-enfants de personnes ayant perdu la nationalité suisse dans certaines circonstances historiques. Ces procédures facilitées suivent des règles et des délais propres, distincts de la naturalisation ordinaire."]}], 'faq': [{'q': 'Les années passées en Suisse comme enfant comptent-elles double pour la naturalisation ?', 'a': 'Oui, les années de séjour entre 8 et 18 ans comptent double, ce qui peut réduire significativement la durée de résidence encore nécessaire pour atteindre les dix ans requis par la naturalisation ordinaire.'}, {'q': 'Quel niveau de langue faut-il pour se faire naturaliser ?', 'a': 'La loi sur la nationalité fixe des exigences minimales, généralement un niveau oral A2 et écrit A1 dans une langue nationale selon le cadre européen commun de référence pour les langues.'}, {'q': 'La naturalisation dépend-elle uniquement de critères fédéraux ?', 'a': 'Non, la procédure se déroule à trois niveaux, fédéral, cantonal et communal, chaque échelon pouvant imposer des exigences complémentaires dans les limites fixées par le droit fédéral, ce qui explique les différences de pratique entre cantons.'}]}},
    'permis-frontalier-g-conditions': {'domaine_id': 'droit_etrangers', 'published': '2026-08-06', 'fr': {'slug': 'permis-frontalier-g-conditions-travailleurs', 'title': 'Permis frontalier G : conditions pour travailleurs frontaliers', 'meta': "Résidence à l'étranger, retour hebdomadaire, distinction UE/AELE et États tiers : les conditions d'obtention du permis frontalier G en Suisse.", 'sections': [{'heading': 'Le principe du permis frontalier', 'paragraphs': ["Le permis G est délivré aux personnes qui résident dans un pays voisin de la Suisse mais y exercent une activité lucrative, tout en conservant leur domicile principal à l'étranger. Il suppose en principe un retour régulier au lieu de résidence, généralement au moins une fois par semaine."]}, {'heading': "Les ressortissants de l'UE et de l'AELE", 'paragraphs': ["Pour les ressortissants des États membres de l'Union européenne ou de l'AELE, l'accord sur la libre circulation des personnes facilite l'obtention du permis frontalier, sans limitation de durée pour un contrat de travail à durée indéterminée, le permis étant renouvelable tant que les conditions restent remplies."]}, {'heading': "Les ressortissants d'États tiers", 'paragraphs': ["Pour les personnes ressortissantes d'un État hors UE/AELE, le régime est nettement plus restrictif : le permis frontalier est en principe soumis à des contingents et à une priorité accordée aux travailleurs déjà présents sur le marché du travail suisse et européen, selon les mêmes règles générales que celles applicables à l'admission de la main-d'œuvre étrangère hors UE/AELE."]}, {'heading': "Les obligations de l'employeur", 'paragraphs': ["L'employeur qui engage un travailleur frontalier doit en principe respecter les mêmes conditions de travail et de salaire que celles applicables aux travailleurs résidant en Suisse, afin d'éviter tout dumping salarial, et se conformer aux obligations d'annonce applicables selon la situation du poste concerné."]}], 'faq': [{'q': "Un titulaire d'un permis G doit-il rentrer chez lui tous les jours ?", 'a': "Non, mais un retour régulier à son lieu de résidence à l'étranger est en principe attendu, généralement au moins une fois par semaine, selon les règles applicables au statut de frontalier."}, {'q': "Le permis frontalier est-il plus facile à obtenir pour un ressortissant de l'UE ?", 'a': "Oui, l'accord sur la libre circulation des personnes facilite nettement l'accès au permis G pour les ressortissants UE/AELE par rapport aux ressortissants d'États tiers, soumis à des règles beaucoup plus restrictives."}, {'q': "Un employeur peut-il payer un frontalier moins qu'un résident suisse pour le même poste ?", 'a': "Non, les conditions de salaire et de travail doivent en principe être équivalentes à celles applicables aux travailleurs résidant en Suisse, afin d'éviter toute forme de dumping salarial."}]}},
    'lamal-changer-caisse-maladie-franchise': {'domaine_id': 'droit_assurances', 'published': '2026-08-07', 'fr': {'slug': 'lamal-changer-caisse-maladie-franchise-delais', 'title': 'LAMal : changer de caisse maladie et franchise', 'meta': "Délai de résiliation, franchises à option, hausse de prime : ce qu'il faut savoir pour changer d'assureur maladie de base en Suisse.", 'sections': [{'heading': "Le principe de l'assurance obligatoire", 'paragraphs': ["L'assurance obligatoire des soins, régie par la LAMal, garantit un catalogue de prestations identique quel que soit l'assureur choisi. Cette uniformité des prestations rend la comparaison entre assureurs pertinente principalement sur le plan du montant des primes, chaque assureur fixant librement ses tarifs dans les limites fixées par la loi."]}, {'heading': 'Le délai de résiliation ordinaire', 'paragraphs': ["En règle générale, la résiliation pour changer d'assureur au 1er janvier suivant doit parvenir à l'ancien assureur au plus tard fin novembre de l'année en cours, un préavis d'un mois étant prévu par la loi. Il est recommandé d'obtenir la confirmation d'affiliation du nouvel assureur avant de résilier l'ancien contrat, afin d'éviter toute interruption de couverture."]}, {'heading': 'Le délai spécial en cas de hausse de prime', 'paragraphs': ["Lorsque l'assureur annonce une hausse de prime pour l'année suivante, un délai de résiliation spécial et plus court s'ouvre, permettant à l'assuré de changer d'assureur jusqu'à la fin du mois précédant l'entrée en vigueur de la nouvelle prime, sans devoir respecter le délai ordinaire de fin novembre."]}, {'heading': 'Le choix de la franchise', 'paragraphs': ["L'assuré choisit sa franchise annuelle parmi plusieurs options, la franchise ordinaire étant fixée à CHF 300, avec des franchises à option plus élevées permettant de réduire la prime mensuelle en contrepartie d'une participation plus importante aux frais de santé en cas de besoin. Au-delà de la franchise, une quote-part de 10% des coûts reste généralement à la charge de l'assuré jusqu'à un plafond annuel fixé par la loi."]}], 'faq': [{'q': "Jusqu'à quand puis-je résilier ma caisse maladie pour changer au 1er janvier ?", 'a': "En principe jusqu'à fin novembre de l'année en cours, la résiliation devant parvenir à l'assureur avec un préavis d'un mois avant la fin de l'année."}, {'q': "Puis-je changer d'assureur en cours d'année si ma prime augmente ?", 'a': "Oui, une hausse de prime ouvre un délai de résiliation spécial, plus court que le délai ordinaire, permettant de changer d'assureur avant l'entrée en vigueur de la nouvelle prime."}, {'q': 'Une franchise plus élevée réduit-elle toujours ma prime ?', 'a': "En général oui, les franchises à option permettent de réduire la prime mensuelle en contrepartie d'une prise en charge personnelle plus importante des frais de santé en cas de besoin effectif de soins."}]}},
    'assurance-accident-laa-couverture': {'domaine_id': 'droit_assurances', 'published': '2026-08-07', 'fr': {'slug': 'assurance-accident-laa-couverture-prestations', 'title': 'Assurance accident LAA : ce qui est couvert', 'meta': "Accidents professionnels et non professionnels, indemnités journalières, rente d'invalidité : les prestations de l'assurance-accidents obligatoire en Suisse.", 'sections': [{'heading': 'Le champ de la couverture', 'paragraphs': ["L'assurance-accidents obligatoire, régie par la LAA, couvre en principe tous les salariés en Suisse contre les accidents professionnels et, selon le nombre d'heures de travail hebdomadaires effectuées chez le même employeur, également contre les accidents non professionnels, ainsi que contre certaines maladies professionnelles reconnues comme telles.", "Lorsque le volume d'activité chez l'employeur est trop faible pour ouvrir droit à la couverture des accidents non professionnels, ce risque doit généralement être couvert par ailleurs, par exemple via l'assurance maladie de base."]}, {'heading': "Les prestations en cas d'accident", 'paragraphs': ["L'assurance prend en charge les frais de traitement médical liés à l'accident, sans franchise ni quote-part à la charge de l'assuré, ce qui la distingue de l'assurance maladie de base. Elle verse également une indemnité journalière en cas d'incapacité de travail, généralement fixée à 80% du salaire assuré, dès le début du droit à cette prestation."]}, {'heading': "Les prestations en cas d'atteinte durable", 'paragraphs': ["Si l'accident entraîne une invalidité durable, l'assuré peut avoir droit à une rente d'invalidité, calculée en fonction du degré d'incapacité de gain reconnu. Une atteinte importante et durable à l'intégrité physique, mentale ou psychique peut également donner droit à une indemnité pour atteinte à l'intégrité, indépendante du taux d'invalidité retenu pour la rente."]}, {'heading': 'Les prestations aux survivants', 'paragraphs': ["En cas de décès consécutif à un accident couvert, l'assurance verse des rentes de survivants au conjoint et aux enfants, selon des règles et des montants qui dépendent de la situation familiale concrète de la victime au moment du décès."]}], 'faq': [{'q': "L'assurance accident couvre-t-elle les accidents survenus en dehors du travail ?", 'a': "Oui, si le nombre d'heures de travail hebdomadaires chez l'employeur atteint le seuil requis, la LAA couvre également les accidents non professionnels, survenus par exemple pendant les loisirs."}, {'q': 'Faut-il payer une franchise pour les frais de traitement après un accident couvert par la LAA ?', 'a': "En principe non, contrairement à l'assurance maladie de base, l'assurance-accidents prend en charge les frais de traitement sans franchise ni quote-part à la charge de l'assuré."}, {'q': "Qu'est-ce que l'indemnité pour atteinte à l'intégrité ?", 'a': "C'est une prestation distincte de la rente d'invalidité, versée en cas d'atteinte importante et durable à l'intégrité physique, mentale ou psychique de l'assuré, indépendamment de sa capacité de gain future."}]}},
    'dommages-corporels-calcul-indemnisation': {'domaine_id': 'droit_responsabilite_civile', 'published': '2026-08-07', 'fr': {'slug': 'dommages-corporels-calcul-indemnisation-suisse', 'title': "Dommages corporels : comment est calculée l'indemnisation", 'meta': "Frais médicaux, perte de gain, tort moral, faute concomitante : les postes de dommage pris en compte dans le calcul d'une indemnisation en cas de blessure.", 'sections': [{'heading': 'Les postes de dommage matériel', 'paragraphs': ["L'indemnisation d'un dommage corporel couvre en principe les frais médicaux et paramédicaux non pris en charge par les assurances sociales, la perte de gain actuelle durant l'incapacité de travail, ainsi que la perte de gain future si l'atteinte a des conséquences durables sur la capacité de travail de la victime.", "Le dommage ménager, correspondant à l'incapacité d'accomplir les tâches domestiques habituelles, constitue également un poste de dommage reconnu, y compris pour une personne sans activité lucrative."]}, {'heading': 'Le tort moral', 'paragraphs': ["L'art. 47 CO permet d'allouer une indemnité pour tort moral en cas de lésions corporelles, destinée à compenser les souffrances physiques et psychiques endurées par la victime, indépendamment du dommage matériel. Son montant est fixé par le juge en tenant compte de la gravité de l'atteinte et de ses répercussions concrètes sur la vie de la victime."]}, {'heading': 'La méthode de calcul du dommage futur', 'paragraphs': ["Lorsque l'atteinte a des conséquences durables, le dommage futur, notamment la perte de gain future, est généralement calculé par capitalisation, à l'aide de tables actuarielles qui tiennent compte de l'espérance de vie professionnelle restante et d'un taux d'intérêt technique, afin d'aboutir à un capital représentant la valeur actuelle des pertes futures."]}, {'heading': 'La réduction pour faute concomitante', 'paragraphs': ["Si la victime a elle-même contribué à la survenance ou à l'aggravation du dommage par son propre comportement, l'art. 44 CO permet au juge de réduire l'indemnisation en proportion de cette faute concomitante. L'indemnisation est également coordonnée avec les prestations déjà versées par les assurances sociales, qui disposent souvent d'un droit de recours contre le responsable pour les montants qu'elles ont eux-mêmes versés à la victime."]}], 'faq': [{'q': "Le tort moral s'ajoute-t-il toujours à l'indemnisation du dommage matériel ?", 'a': "Il peut s'y ajouter en cas de lésions corporelles suffisamment graves, sur la base de l'art. 47 CO, mais son octroi et son montant dépendent d'une appréciation concrète des souffrances endurées par la victime."}, {'q': 'Comment est calculée la perte de gain future ?', 'a': "Généralement par capitalisation, à l'aide de tables actuarielles tenant compte de l'espérance de vie professionnelle restante, afin d'aboutir à un capital représentant la valeur actuelle des pertes de revenu futures."}, {'q': "Puis-je être moins bien indemnisé si j'ai contribué moi-même à l'accident ?", 'a': "Oui, une faute concomitante de la victime peut entraîner une réduction de l'indemnisation en proportion de cette faute, conformément à l'art. 44 CO."}]}},
    'responsabilite-produits-defectueux-suisse': {'domaine_id': 'droit_responsabilite_civile', 'published': '2026-08-07', 'fr': {'slug': 'responsabilite-produits-defectueux-suisse-lrfp', 'title': 'Responsabilité du fait des produits défectueux', 'meta': 'Sécurité légitimement attendue, responsabilité objective, délais de prescription : ce que prévoit la loi sur la responsabilité du fait des produits (LRFP).', 'sections': [{'heading': 'Le principe de la responsabilité objective', 'paragraphs': ["La loi fédérale sur la responsabilité du fait des produits (LRFP) instaure une responsabilité objective du producteur : celui-ci répond du dommage causé par un défaut de son produit, indépendamment de toute faute de sa part. Il suffit d'établir l'existence d'un défaut, d'un dommage et d'un lien de causalité entre les deux."]}, {'heading': 'La notion de défaut', 'paragraphs': ["Un produit est considéré comme défectueux lorsqu'il ne présente pas la sécurité à laquelle on peut légitimement s'attendre, compte tenu de sa présentation, de l'usage qui peut raisonnablement en être attendu et du moment de sa mise en circulation. Un produit n'est pas nécessairement défectueux du seul fait qu'un modèle plus sûr a été mis en circulation ultérieurement."]}, {'heading': 'Qui peut être recherché', 'paragraphs': ["Le producteur au sens de la loi comprend non seulement le fabricant du produit fini, mais aussi, selon les circonstances, celui qui appose sa marque sur le produit ou l'importateur qui le met en circulation en Suisse, ce qui élargit le cercle des personnes potentiellement responsables envers la victime."]}, {'heading': 'Les délais de prescription et de péremption', 'paragraphs': ["L'action se prescrit en principe dans un délai de trois ans dès la connaissance du dommage, du défaut et de l'identité du producteur, mais s'éteint dans tous les cas dix ans après la mise en circulation du produit concerné, indépendamment de la connaissance qu'en avait la victime."]}], 'faq': [{'q': 'Dois-je prouver une faute du fabricant pour être indemnisé ?', 'a': "Non, la LRFP instaure une responsabilité objective : il suffit d'établir le défaut du produit, le dommage subi et le lien de causalité entre les deux, sans devoir démontrer une faute du producteur."}, {'q': "Puis-je agir contre l'importateur plutôt que le fabricant étranger ?", 'a': "Oui, la notion de producteur au sens de la loi peut inclure l'importateur qui met le produit en circulation en Suisse, ce qui facilite l'action de la victime lorsque le fabricant se trouve à l'étranger."}, {'q': 'Après combien de temps ne puis-je plus agir contre un fabricant ?', 'a': "L'action se prescrit trois ans après la connaissance du dommage, du défaut et du producteur, mais s'éteint dans tous les cas dix ans après la mise en circulation du produit, même si le dommage n'était pas encore connu."}]}},
    'mainlevee-opposition-provisoire-definitive': {'domaine_id': 'droit_poursuites_faillite', 'published': '2026-08-08', 'fr': {'slug': 'mainlevee-opposition-provisoire-definitive-lp', 'title': "Mainlevée d'opposition : provisoire ou définitive", 'meta': "Faire lever l'opposition à un commandement de payer grâce à un jugement ou une reconnaissance de dette : les art. 80 et 82 LP expliqués.", 'sections': [{'heading': 'Pourquoi une mainlevée est nécessaire', 'paragraphs': ["Lorsque le débiteur fait opposition au commandement de payer qui lui a été notifié, la poursuite est suspendue : le créancier ne peut pas continuer la procédure tant que cette opposition n'a pas été levée. La mainlevée est la procédure judiciaire, généralement rapide, permettant précisément de faire lever cette opposition."]}, {'heading': 'La mainlevée définitive', 'paragraphs': ["L'art. 80 LP permet d'obtenir la mainlevée définitive lorsque la créance repose sur un jugement exécutoire ou un titre qui lui est légalement assimilé. Le débiteur ne peut alors s'opposer qu'en invoquant des moyens limités, comme l'extinction ou la prescription de la dette survenue depuis le jugement, sans pouvoir rediscuter le fond de la créance elle-même."]}, {'heading': 'La mainlevée provisoire', 'paragraphs': ["L'art. 82 LP permet d'obtenir la mainlevée provisoire lorsque la créance repose sur une reconnaissance de dette signée par le débiteur, par exemple un contrat de prêt ou une facture reconnue. Le juge de la mainlevée examine alors seulement l'existence formelle de ce titre, sans trancher le fond du litige."]}, {'heading': "L'action en libération de dette", 'paragraphs': ["Contrairement à la mainlevée définitive, la mainlevée provisoire n'est jamais définitive pour le débiteur : celui-ci dispose d'un délai de vingt jours dès son prononcé pour intenter une action en libération de dette, procédure au fond permettant de contester réellement l'existence ou le montant de la créance devant le tribunal ordinaire compétent."]}], 'faq': [{'q': 'Quelle est la différence entre mainlevée provisoire et définitive ?', 'a': 'La mainlevée définitive repose sur un jugement déjà exécutoire et laisse peu de moyens de défense au débiteur, tandis que la mainlevée provisoire repose sur une simple reconnaissance de dette et peut encore être contestée au fond par une action en libération de dette.'}, {'q': 'Que se passe-t-il si je ne fais rien après une mainlevée provisoire ?', 'a': "Si vous ne saisissez pas le tribunal d'une action en libération de dette dans les vingt jours suivant le prononcé de la mainlevée provisoire, la poursuite se poursuit normalement, comme si la créance était définitivement établie."}, {'q': 'Le juge de la mainlevée examine-t-il le fond du litige ?', 'a': "Non, la procédure de mainlevée est volontairement sommaire : le juge vérifie l'existence formelle d'un titre suffisant (jugement ou reconnaissance de dette), sans trancher toutes les questions de fond, qui peuvent faire l'objet d'une procédure séparée."}]}},
    'sequestre-biens-debiteur-procedure': {'domaine_id': 'droit_poursuites_faillite', 'published': '2026-08-08', 'fr': {'slug': 'sequestre-biens-debiteur-procedure-suisse', 'title': "Séquestre : bloquer les biens d'un débiteur", 'meta': "Mesure conservatoire avant jugement, cas d'application, validation par une poursuite : le régime du séquestre selon les art. 271 et suivants LP.", 'sections': [{'heading': 'Une mesure conservatoire avant jugement', 'paragraphs': ["Le séquestre, régi par les art. 271 et suivants LP, permet à un créancier de faire bloquer des biens déterminés de son débiteur avant même d'avoir obtenu un jugement définitif, lorsqu'il existe un risque concret que ce débiteur fasse disparaître ses actifs avant la fin d'une procédure ordinaire, souvent longue."]}, {'heading': "Les cas d'application", 'paragraphs': ["La loi énumère plusieurs situations permettant de requérir un séquestre : le débiteur n'a pas de domicile fixe, il dissimule ses biens ou s'apprête à quitter la Suisse pour se soustraire à ses obligations, la créance repose sur un acte de défaut de biens, ou encore le débiteur n'est pas domicilié en Suisse, cette dernière situation étant fréquente en matière commerciale internationale."]}, {'heading': "La procédure d'obtention", 'paragraphs': ["Le créancier doit s'adresser au juge compétent du lieu où se trouvent les biens à séquestrer, en rendant vraisemblable sa créance ainsi que l'existence d'un cas de séquestre. La procédure est rapide et se déroule généralement sans entendre le débiteur au préalable, afin de préserver l'effet de surprise indispensable à l'efficacité de la mesure."]}, {'heading': 'La validation du séquestre', 'paragraphs': ["Un séquestre n'est pas une fin en soi : le créancier doit le valider, en principe dans un délai de dix jours suivant son exécution, en introduisant une poursuite ou une action judiciaire visant à faire reconnaître définitivement sa créance. À défaut, le séquestre devient caduc et les biens bloqués sont libérés."]}], 'faq': [{'q': 'Puis-je obtenir un séquestre sans jugement préalable contre mon débiteur ?', 'a': "Oui, c'est précisément la fonction du séquestre : bloquer des biens avant même l'obtention d'un jugement définitif, dans les cas prévus par la loi, pour éviter que le débiteur ne les fasse disparaître entre-temps."}, {'q': "Le débiteur est-il informé avant l'exécution du séquestre ?", 'a': "En principe non, la procédure se déroulant rapidement et sans audition préalable du débiteur, afin de préserver l'effet de surprise nécessaire à l'efficacité de la mesure."}, {'q': "Que se passe-t-il si je n'engage aucune poursuite après un séquestre obtenu ?", 'a': "Le séquestre doit être validé, en principe dans les dix jours suivant son exécution, par l'introduction d'une poursuite ou d'une action judiciaire. À défaut, il devient caduc et les biens bloqués sont libérés."}]}},
    'directives-anticipees-patient-redaction': {'domaine_id': 'droit_protection_enfant_adulte', 'published': '2026-08-08', 'fr': {'slug': 'directives-anticipees-patient-redaction-suisse', 'title': 'Directives anticipées du patient : comment les rédiger', 'meta': "Refuser ou accepter un traitement en cas d'incapacité future, désigner un représentant thérapeutique : les règles des art. 370 et suivants CC.", 'sections': [{'heading': 'Le principe des directives anticipées', 'paragraphs': ["L'art. 370 CC permet à toute personne capable de discernement de déterminer, par un document écrit, daté et signé, les traitements médicaux auxquels elle consent ou qu'elle refuse pour le cas où elle deviendrait incapable de discernement. Ce dispositif garantit que la volonté de la personne continue d'être respectée même lorsqu'elle n'est plus en mesure de s'exprimer elle-même."]}, {'heading': 'Désigner un représentant thérapeutique', 'paragraphs': ["Les directives anticipées peuvent également désigner une personne physique chargée de discuter des soins avec l'équipe médicale et de prendre les décisions nécessaires au nom du patient devenu incapable de discernement, dans le respect des directives déjà exprimées ou, à défaut d'instructions précises, de la volonté présumée du patient."]}, {'heading': 'La force obligatoire pour le corps médical', 'paragraphs': ["Le médecin doit en principe respecter les directives anticipées du patient, sauf s'il existe un doute sérieux sur le fait qu'elles correspondent à la volonté libre du patient ou à la situation médicale actuelle, ou si elles violent des dispositions légales. En cas de doute, l'autorité de protection de l'adulte peut être saisie pour trancher."]}, {'heading': 'Conserver et faire connaître ses directives', 'paragraphs': ["Pour être utiles, les directives anticipées doivent pouvoir être retrouvées au moment opportun : il est recommandé d'en informer ses proches et son médecin traitant, de les déposer auprès d'un tiers de confiance ou d'un registre cantonal lorsqu'il existe, et de faire mentionner leur existence sur la carte d'assuré, souvent consultée en urgence par les équipes médicales."]}], 'faq': [{'q': 'Les directives anticipées sont-elles obligatoirement respectées par le médecin ?', 'a': "En principe oui, sauf doute sérieux sur leur conformité à la volonté actuelle et libre du patient ou violation de dispositions légales, auquel cas l'autorité de protection de l'adulte peut être saisie."}, {'q': "Puis-je désigner quelqu'un pour décider à ma place en cas d'incapacité ?", 'a': "Oui, les directives anticipées permettent de désigner un représentant thérapeutique chargé de dialoguer avec l'équipe médicale et de prendre les décisions nécessaires, dans le respect de vos instructions ou de votre volonté présumée."}, {'q': 'Où faut-il conserver ses directives anticipées ?', 'a': "Il est recommandé de les déposer auprès d'un proche de confiance, de son médecin traitant, ou d'un registre cantonal lorsqu'il existe, et de faire mentionner leur existence sur sa carte d'assuré afin qu'elles soient retrouvées rapidement en cas d'urgence."}]}},
    'apea-role-protection-adulte-enfant': {'domaine_id': 'droit_protection_enfant_adulte', 'published': '2026-08-08', 'fr': {'slug': 'apea-role-quand-intervient-protection', 'title': 'APEA : rôle et quand elle intervient', 'meta': "Autorité de protection de l'enfant et de l'adulte : quand elle est saisie, quelles mesures elle peut ordonner, principes de subsidiarité et proportionnalité.", 'sections': [{'heading': 'Une autorité interdisciplinaire', 'paragraphs': ["L'autorité de protection de l'enfant et de l'adulte (APEA) est une autorité cantonale ou régionale composée de professionnels de différentes disciplines, généralement issus du droit, du social et de la psychologie, chargée de veiller au bien-être des personnes mineures ou adultes qui ne peuvent, en tout ou en partie, assurer seules la sauvegarde de leurs intérêts."]}, {'heading': "L'intervention en matière de protection de l'enfant", 'paragraphs': ["L'APEA peut être saisie, sur signalement ou requête, lorsque le développement d'un enfant paraît menacé, par exemple en cas de conflit parental important, de négligence ou de mise en danger. Elle dispose d'un éventail de mesures graduées, allant du simple conseil à la curatelle éducative, jusqu'au retrait de l'autorité parentale dans les cas les plus graves."]}, {'heading': "L'intervention en matière de protection de l'adulte", 'paragraphs': ["Pour un adulte qui ne peut plus, en raison d'une maladie, d'un handicap ou d'une autre cause, gérer certains aspects de sa vie ou de son patrimoine, l'APEA peut instituer une curatelle, dont l'étendue est adaptée aux besoins concrets de la personne concernée, conformément aux art. 390 et suivants CC."]}, {'heading': 'Les principes de subsidiarité et de proportionnalité', 'paragraphs': ["Toute mesure ordonnée par l'APEA doit respecter le principe de subsidiarité, ce qui signifie qu'elle n'intervient que si l'aide de la famille ou d'autres formes de soutien ne suffit pas, ainsi que le principe de proportionnalité, la mesure retenue devant toujours être la moins incisive possible tout en atteignant le but de protection recherché."]}], 'faq': [{'q': "Qui peut saisir l'APEA en cas de doute sur la situation d'un enfant ou d'un adulte vulnérable ?", 'a': "En principe toute personne peut signaler une situation préoccupante à l'APEA, qui évalue ensuite si une intervention est nécessaire, dans le respect des principes de subsidiarité et de proportionnalité."}, {'q': "L'APEA retire-t-elle systématiquement l'autorité parentale en cas de signalement ?", 'a': "Non, elle dispose d'un éventail de mesures graduées et privilégie toujours la solution la moins incisive possible, le retrait de l'autorité parentale restant réservé aux situations les plus graves."}, {'q': "Une curatelle pour un adulte signifie-t-elle qu'il perd tous ses droits ?", 'a': "Non, l'étendue de la curatelle est adaptée aux besoins concrets de la personne, conformément au principe de proportionnalité, et peut se limiter à certains aspects précis de sa vie ou de son patrimoine."}]}},
    'donation-succession-fiscalite-cantonale': {'domaine_id': 'droit_fiscal', 'published': '2026-08-08', 'fr': {'slug': 'donation-succession-fiscalite-cantonale-suisse', 'title': 'Donation vs succession : quelle fiscalité cantonale', 'meta': "Aucun impôt fédéral sur les successions, mais des règles cantonales très variables : ce qu'il faut savoir avant une donation ou une transmission successorale.", 'sections': [{'heading': 'Une compétence exclusivement cantonale', 'paragraphs': ["Contrairement à de nombreux pays voisins, la Suisse ne connaît pas d'impôt fédéral sur les successions ou les donations : cette matière relève exclusivement de la compétence des cantons, ce qui explique des différences parfois marquées d'un canton à l'autre, tant sur les taux applicables que sur les exonérations prévues."]}, {'heading': 'Le traitement du conjoint et des descendants', 'paragraphs': ["Dans la grande majorité des cantons, le conjoint survivant est totalement exonéré d'impôt sur les successions et les donations. Les descendants directs, enfants et petits-enfants, bénéficient également d'une exonération ou d'un taux très réduit dans la plupart des cantons, bien que ce ne soit pas une règle universelle : quelques cantons appliquent encore une imposition, même limitée, aux descendants directs."]}, {'heading': 'Le traitement des tiers et des concubins', 'paragraphs': ["Les héritiers ou donataires sans lien de parenté proche, y compris le plus souvent le concubin, sont généralement soumis à des taux nettement plus élevés, parfois progressifs selon le montant transmis, ce qui rend une planification patrimoniale d'autant plus importante pour les couples non mariés."]}, {'heading': 'Donation et rapport successoral', 'paragraphs': ['Une donation faite du vivant du disposant peut, indépendamment de sa fiscalité propre, être soumise à un rapport à la succession selon les art. 626 et suivants CC : elle est alors réintégrée fictivement dans la masse successorale pour le calcul des parts entre héritiers, sauf si le disposant en a expressément dispensé le bénéficiaire. Cette question civile est distincte de la question fiscale, mais les deux doivent être anticipées ensemble dans toute planification successorale.']}], 'faq': [{'q': 'Existe-t-il un impôt fédéral sur les successions en Suisse ?', 'a': "Non, cette matière relève exclusivement des cantons, ce qui explique des règles et des taux très différents d'un canton à l'autre."}, {'q': 'Le conjoint paie-t-il toujours des impôts sur une succession ou une donation ?', 'a': "Dans la grande majorité des cantons, le conjoint survivant est totalement exonéré, mais il reste utile de vérifier la règle applicable dans le canton concerné, les pratiques n'étant pas strictement identiques partout."}, {'q': 'Une donation faite avant un décès échappe-t-elle au calcul de la succession ?', 'a': 'Pas nécessairement sur le plan civil : elle peut devoir être rapportée à la succession selon les art. 626 et suivants CC, sauf dispense expresse du disposant, indépendamment de son traitement fiscal propre.'}]}},
    'tva-independants-immatriculation-suisse': {'domaine_id': 'droit_fiscal', 'published': '2026-08-08', 'fr': {'slug': 'tva-independants-immatriculation-suisse-seuil', 'title': "TVA pour indépendants : quand s'immatriculer", 'meta': "Seuil de CHF 100'000 de chiffre d'affaires, assujettissement volontaire, récupération de l'impôt préalable : ce qu'un indépendant doit savoir sur la TVA.", 'sections': [{'heading': "Le seuil d'assujettissement obligatoire", 'paragraphs': ["Un indépendant devient en principe obligatoirement assujetti à la TVA dès que son chiffre d'affaires annuel provenant de prestations imposables en Suisse atteint CHF 100'000, ce seuil s'appliquant de la même manière aux entreprises étrangères qui fournissent des prestations imposables sur le territoire suisse.", "Certaines catégories d'acteurs, notamment les associations et institutions d'utilité publique, bénéficient d'un seuil relevé, généralement fixé à CHF 250'000, avant de devenir obligatoirement assujettis."]}, {'heading': "L'assujettissement volontaire", 'paragraphs': ["Un indépendant dont le chiffre d'affaires reste en dessous du seuil obligatoire peut néanmoins choisir de s'assujettir volontairement à la TVA, ce qui lui permet de récupérer l'impôt préalable payé sur ses propres achats et investissements professionnels, un choix souvent judicieux pour une activité impliquant des charges importantes en phase de démarrage."]}, {'heading': "Les conséquences pratiques de l'assujettissement", 'paragraphs': ["Une fois assujetti, l'indépendant doit facturer la TVA à ses clients selon les taux applicables à ses prestations, tenir une comptabilité permettant de justifier les décomptes périodiques, et reverser régulièrement à l'administration fiscale la différence entre la TVA encaissée sur ses ventes et celle payée sur ses propres achats professionnels."]}, {'heading': 'Anticiper le changement de statut', 'paragraphs': ["Il est recommandé de surveiller l'évolution de son chiffre d'affaires en cours d'année afin d'anticiper le franchissement du seuil obligatoire, l'assujettissement rétroactif ou tardif pouvant entraîner des complications administratives et financières, notamment si la TVA n'a pas été correctement répercutée sur les clients pendant la période concernée."]}], 'faq': [{'q': "Dois-je m'immatriculer à la TVA dès mes premiers revenus d'indépendant ?", 'a': "Non, l'assujettissement obligatoire n'intervient qu'à partir de CHF 100'000 de chiffre d'affaires annuel provenant de prestations imposables en Suisse, sauf choix d'un assujettissement volontaire en dessous de ce seuil."}, {'q': "Pourquoi s'assujettir volontairement en dessous du seuil obligatoire ?", 'a': "Cela permet de récupérer l'impôt préalable payé sur ses propres achats et investissements professionnels, ce qui peut être avantageux pour une activité impliquant des charges importantes, notamment en phase de démarrage."}, {'q': "Que se passe-t-il si je dépasse le seuil en cours d'année sans m'en apercevoir ?", 'a': "L'assujettissement peut devenir rétroactif ou tardif, ce qui peut créer des complications administratives et financières, notamment si la TVA due n'a pas été répercutée sur les clients pendant la période concernée. Il est recommandé de surveiller son chiffre d'affaires en continu."}]}},
    'hypotheque-taux-variable-litige-banque': {'domaine_id': 'droit_bancaire', 'published': '2026-08-08', 'fr': {'slug': 'hypotheque-taux-variable-litige-renegociation-banque', 'title': 'Hypothèque à taux variable : litige et renégociation', 'meta': "Préavis de résiliation, calcul du taux, ombudsman des banques : ce qu'il faut savoir en cas de désaccord avec sa banque sur une hypothèque variable.", 'sections': [{'heading': "Le fonctionnement de l'hypothèque à taux variable", 'paragraphs': ["Contrairement à l'hypothèque fixe, qui lie les parties pour toute une durée déterminée à un taux figé, l'hypothèque à taux variable suit l'évolution du marché ou d'un taux de référence propre à la banque, et peut en principe être résiliée par l'une ou l'autre partie moyennant un préavis, souvent de trois ou six mois selon les conditions contractuelles applicables."]}, {'heading': 'Les litiges fréquents', 'paragraphs': ["Les désaccords portent le plus souvent sur la méthode de calcul du taux appliqué par la banque, sur l'information transmise à l'emprunteur lors d'une hausse, ou sur un refus de la banque de renégocier les conditions alors que le marché a évolué favorablement. La transparence contractuelle sur la méthode de fixation du taux est un point central à vérifier avant la signature."]}, {'heading': 'La renégociation', 'paragraphs': ["Rien n'oblige juridiquement une banque à accepter de renégocier une hypothèque en cours, mais la mise en concurrence avec d'autres établissements reste souvent le levier le plus efficace pour obtenir de meilleures conditions, notamment lors d'un renouvellement ou d'une échéance intermédiaire prévue au contrat."]}, {'heading': 'Les voies de recours en cas de litige', 'paragraphs': ["L'Ombudsman des banques suisses offre une procédure de médiation gratuite pour tenter de résoudre un différend avec un établissement bancaire sans passer par une procédure judiciaire, notamment sur des questions de transparence ou de bonne foi contractuelle. À défaut d'accord, une action civile devant le tribunal compétent reste possible pour trancher le litige."]}], 'faq': [{'q': 'Une banque peut-elle modifier librement le taux de mon hypothèque variable ?', 'a': "Elle doit respecter la méthode de calcul prévue par le contrat et informer l'emprunteur des modifications, ce qui rend essentiel de bien comprendre cette méthode avant de signer."}, {'q': 'Puis-je résilier une hypothèque à taux variable à tout moment ?', 'a': "En principe moyennant un préavis, souvent de trois ou six mois selon les conditions contractuelles, contrairement à une hypothèque fixe qui lie généralement les parties jusqu'à son échéance sauf pénalité de sortie anticipée."}, {'q': 'Que faire en cas de désaccord avec ma banque sur mon hypothèque ?', 'a': "L'Ombudsman des banques suisses propose une médiation gratuite, souvent utile avant d'envisager une action civile devant le tribunal compétent."}]}},
    'cautionnement-solidaire-risques-caution': {'domaine_id': 'droit_bancaire', 'published': '2026-08-08', 'fr': {'slug': 'cautionnement-solidaire-risques-caution-suisse', 'title': 'Cautionnement solidaire : risques pour la caution', 'meta': "Responsabilité directe sans épuisement préalable du débiteur, formalités protectrices, risque de devoir payer l'intégralité de la dette : l'art. 492 CO.", 'sections': [{'heading': 'Le principe du cautionnement', 'paragraphs': ["Le cautionnement, régi par les art. 492 et suivants CO, est l'engagement par lequel une personne, la caution, s'engage envers un créancier à répondre du paiement de la dette d'un tiers, le débiteur principal, si celui-ci n'exécute pas ses obligations."]}, {'heading': 'La spécificité du cautionnement solidaire', 'paragraphs': ["Dans un cautionnement simple, le créancier doit en principe d'abord poursuivre le débiteur principal et épuiser certaines voies contre lui avant de pouvoir s'adresser à la caution. Le cautionnement solidaire supprime cette protection : le créancier peut rechercher directement la caution dès que le débiteur est en demeure, sans devoir au préalable exercer des poursuites contre lui ni épuiser ses garanties."]}, {'heading': 'Les exigences de forme protectrices', 'paragraphs': ["Lorsque la caution est une personne physique, la loi impose des exigences de forme strictes, notamment la forme authentique lorsque le montant garanti dépasse un certain seuil, sauf si la caution agit pour des raisons de commerce. Ces exigences visent à s'assurer que la caution mesure pleinement la portée de son engagement avant de le signer."]}, {'heading': 'Le risque concret pour la caution', 'paragraphs': ["La caution solidaire peut se retrouver tenue de payer l'intégralité de la dette garantie, même si elle n'a personnellement tiré aucun avantage de l'opération financée, par exemple lorsqu'elle a cautionné le prêt professionnel d'un proche ou d'une société dans laquelle elle n'a pas de rôle actif. Elle dispose ensuite d'un droit de recours contre le débiteur principal, mais ce recours reste souvent illusoire si celui-ci est devenu insolvable, ce qui explique la prudence nécessaire avant de signer un tel engagement."]}], 'faq': [{'q': 'Quelle est la différence entre cautionnement simple et cautionnement solidaire ?', 'a': "Dans le cautionnement simple, le créancier doit en principe d'abord agir contre le débiteur principal avant de s'adresser à la caution. Le cautionnement solidaire supprime cette protection, permettant au créancier de rechercher directement la caution dès la demeure du débiteur."}, {'q': "Puis-je être tenu de payer toute la dette même si je n'en ai tiré aucun avantage ?", 'a': "Oui, c'est précisément le risque du cautionnement solidaire : la caution peut devoir payer l'intégralité de la dette garantie, indépendamment de l'usage qui a été fait des fonds par le débiteur principal."}, {'q': 'Existe-t-il des règles de forme pour protéger la caution ?', 'a': "Oui, lorsque la caution est une personne physique, la loi impose des exigences de forme strictes, notamment la forme authentique au-delà d'un certain montant, sauf engagement pris pour des raisons de commerce."}]}},
    'secret-medical-portee-exceptions-suisse': {'domaine_id': 'droit_medical', 'published': '2026-08-08', 'fr': {'slug': 'secret-medical-portee-exceptions-suisse', 'title': 'Secret médical : portée et exceptions', 'meta': "Ce que couvre le secret professionnel du médecin, les cas de levée légitime et les sanctions pénales prévues par l'art. 321 du Code pénal.", 'sections': [{'heading': 'Une protection pénale du secret', 'paragraphs': ["L'art. 321 CP sanctionne pénalement la violation du secret professionnel par les médecins et leurs auxiliaires. Le secret couvre tout ce qui a été confié au praticien ou constaté par lui dans l'exercice de sa profession, qu'il s'agisse d'un diagnostic, d'un traitement, ou de toute information relative à la vie privée du patient obtenue dans ce cadre."]}, {'heading': 'Le consentement du patient', 'paragraphs': ['Le patient peut délier son médecin du secret professionnel, en tout ou en partie, généralement par une déclaration écrite. Ce consentement doit rester éclairé et spécifique : une autorisation générale et ancienne ne couvre pas nécessairement toute information ultérieure sans lien avec son objet initial.']}, {'heading': "L'autorisation de l'autorité cantonale compétente", 'paragraphs': ["En l'absence de consentement du patient, le médecin peut demander à l'autorité cantonale compétente de le délier du secret professionnel, notamment lorsque la révélation d'informations paraît nécessaire à la sauvegarde d'intérêts légitimes, par exemple dans le cadre d'une procédure judiciaire ou pour protéger un tiers."]}, {'heading': "L'état de nécessité et les obligations légales de dénoncer", 'paragraphs': ["Dans des situations exceptionnelles, un médecin peut se prévaloir de l'état de nécessité au sens de l'art. 17 CP pour justifier une révélation non autorisée, par exemple en présence d'un danger grave et imminent pour la vie d'un tiers. Certaines lois spéciales imposent par ailleurs des obligations de signalement dans des cas définis, notamment en matière de maladies transmissibles, qui priment alors sur le secret médical ordinaire."]}], 'faq': [{'q': 'Un médecin peut-il transmettre mon dossier à mon employeur sans mon accord ?', 'a': "En principe non, sauf consentement spécifique de votre part, autorisation de l'autorité cantonale compétente, ou obligation légale particulière applicable à la situation concernée."}, {'q': "Le secret médical s'applique-t-il aussi aux auxiliaires du médecin ?", 'a': "Oui, l'art. 321 CP couvre également les auxiliaires du médecin qui ont accès à des informations confidentielles dans l'exercice de leur activité, et non uniquement le praticien lui-même."}, {'q': "Un médecin peut-il révéler une information sans autorisation en cas d'urgence vitale pour un tiers ?", 'a': "Dans certaines situations exceptionnelles, l'état de nécessité (art. 17 CP) peut justifier une révélation non autorisée, par exemple face à un danger grave et imminent pour la vie d'un tiers."}]}},
    'assistance-suicide-fin-vie-droit-suisse': {'domaine_id': 'droit_medical', 'published': '2026-08-08', 'fr': {'slug': 'assistance-suicide-fin-vie-droit-suisse', 'title': 'Assistance au suicide et fin de vie en droit suisse', 'meta': "Ce que punit l'art. 115 CP, la condition du mobile égoïste, et la différence avec l'euthanasie active directe, qui reste punissable en droit suisse.", 'sections': [{'heading': "Le cadre légal de l'art. 115 CP", 'paragraphs': ["Le droit suisse ne réglemente pas l'assistance au suicide par une loi spécifique dédiée : c'est l'art. 115 du Code pénal, qui punit l'incitation et l'assistance au suicide, qui définit en creux ce qui reste licite. Cette disposition ne sanctionne l'incitation ou l'assistance au suicide que si son auteur agit pour un mobile égoïste."]}, {'heading': 'Ce que cela signifie en pratique', 'paragraphs': ["Une assistance apportée sans mobile égoïste, par exemple par une organisation d'aide au suicide agissant selon ses conditions habituelles, n'est en principe pas punissable au sens de cette disposition, à condition notamment que la personne accomplisse elle-même le geste fatal et dispose de sa capacité de discernement au moment de sa décision. Cette exigence que le geste final soit accompli par la personne elle-même est déterminante pour distinguer l'assistance au suicide d'autres actes."]}, {'heading': "La distinction avec l'euthanasie active directe", 'paragraphs': ["L'euthanasie active directe, dans laquelle un tiers accomplit lui-même l'acte qui provoque la mort, reste en revanche punissable en droit suisse, en principe comme meurtre ou homicide selon les circonstances concrètes, y compris lorsque la personne concernée avait exprimé le souhait de mourir. Cette distinction entre l'assistance, où la personne agit elle-même, et l'acte accompli par un tiers, est centrale en droit pénal suisse."]}, {'heading': 'Le rôle des directives anticipées', 'paragraphs': ["Les directives anticipées du patient (art. 370 CC) permettent d'exprimer à l'avance son refus de certains traitements ou de mesures de maintien en vie en cas d'incapacité future, une démarche juridiquement distincte de l'assistance au suicide mais qui participe également à la maîtrise de sa fin de vie par le patient lui-même."]}], 'faq': [{'q': "L'assistance au suicide est-elle légale en Suisse ?", 'a': "Elle n'est pas punissable au sens de l'art. 115 CP tant qu'elle n'est pas motivée par un mobile égoïste et que la personne accomplit elle-même le geste fatal en disposant de sa capacité de discernement."}, {'q': 'Quelle est la différence entre assistance au suicide et euthanasie active ?', 'a': "Dans l'assistance au suicide, la personne accomplit elle-même le geste final. Dans l'euthanasie active directe, c'est un tiers qui accomplit l'acte provoquant la mort, ce qui reste punissable en droit suisse même en présence d'un souhait exprimé par la personne concernée."}, {'q': 'Les directives anticipées permettent-elles de demander une euthanasie active ?', 'a': "Non, elles permettent de refuser à l'avance certains traitements ou mesures de maintien en vie, mais ne constituent pas une base légale pour une euthanasie active, qui reste distincte et punissable en droit suisse."}]}},
    'proteger-brevet-suisse-procedure-ipi': {'domaine_id': 'propriete_intellectuelle', 'published': '2026-08-08', 'fr': {'slug': 'proteger-brevet-suisse-procedure-ipi', 'title': 'Protéger un brevet en Suisse : procédure IPI', 'meta': "Dépôt auprès de l'Institut fédéral de la propriété intellectuelle, examen limité, durée de protection de 20 ans : la procédure du brevet suisse.", 'sections': [{'heading': "Le dépôt auprès de l'IPI", 'paragraphs': ["Une demande de brevet suisse se dépose auprès de l'Institut fédéral de la propriété intellectuelle (IPI), qui procède à un examen formel de la demande ainsi qu'à un examen limité de nouveauté, sans toutefois effectuer un examen complet de fond de la nouveauté et de l'activité inventive comme le fait l'Office européen des brevets."]}, {'heading': 'Les limites du brevet suisse', 'paragraphs': ["Cette absence d'examen complet de fond signifie qu'un brevet suisse délivré n'offre pas la même garantie de validité qu'un brevet ayant fait l'objet d'un examen approfondi : sa solidité peut être contestée ultérieurement, notamment dans le cadre d'un litige, si l'on découvre un état de la technique antérieur pertinent qui n'avait pas été examiné lors du dépôt.", "Pour cette raison, de nombreux déposants suisses choisissent de passer par la voie du brevet européen auprès de l'Office européen des brevets, qui peut ensuite déployer ses effets en Suisse, offrant un examen de fond plus complet malgré une procédure plus longue et coûteuse."]}, {'heading': 'La durée de protection', 'paragraphs': ['Un brevet suisse valablement délivré offre une protection maximale de vingt ans à compter de la date de dépôt, sous réserve du paiement régulier des taxes annuelles de maintien en vigueur, qui augmentent progressivement avec les années.']}, {'heading': 'Avant de déposer une demande', 'paragraphs': ["Il est vivement recommandé de procéder à une recherche d'antériorité approfondie avant tout dépôt, ainsi que de solliciter un conseil en brevets ou un avocat spécialisé, notamment pour déterminer la stratégie la plus adaptée entre brevet national, européen ou international selon les marchés visés par l'invention."]}], 'faq': [{'q': "L'IPI vérifie-t-il complètement la nouveauté de mon invention avant de délivrer un brevet ?", 'a': "Non, l'examen pratiqué par l'IPI est limité et ne constitue pas un examen complet de fond, contrairement à celui effectué par l'Office européen des brevets. Un brevet suisse délivré peut donc être contesté ultérieurement sur cette base."}, {'q': "Combien de temps dure la protection d'un brevet suisse ?", 'a': 'En principe vingt ans à compter de la date de dépôt, sous réserve du paiement régulier des taxes annuelles de maintien en vigueur.'}, {'q': 'Vaut-il mieux déposer un brevet suisse ou un brevet européen ?', 'a': "Cela dépend de la stratégie visée : le brevet suisse est plus rapide et moins coûteux mais moins solide faute d'examen de fond complet, tandis que le brevet européen offre un examen plus approfondi et peut couvrir plusieurs pays, dont la Suisse."}]}},
    'droit-auteur-intelligence-artificielle-suisse': {'domaine_id': 'propriete_intellectuelle', 'published': '2026-08-08', 'fr': {'slug': 'droit-auteur-intelligence-artificielle-suisse', 'title': "Droit d'auteur et intelligence artificielle", 'meta': "Une création générée par une IA est-elle protégée ? Ce que dit la loi sur le droit d'auteur suisse (LDA) face à un domaine juridique encore en évolution.", 'sections': [{'heading': "Le critère de la création de l'esprit avec caractère individuel", 'paragraphs': ["La loi suisse sur le droit d'auteur (LDA) protège les œuvres définies comme des créations de l'esprit, littéraires ou artistiques, qui ont un caractère individuel. Ce critère suppose traditionnellement une intervention créative humaine, ce qui soulève une question encore débattue lorsqu'un contenu est généré, en tout ou en grande partie, par un système d'intelligence artificielle sans apport créatif humain substantiel."]}, {'heading': "La situation d'un contenu généré par IA", 'paragraphs': ["En l'état actuel du droit suisse, une création entièrement produite par une intelligence artificielle, sans intervention humaine créative suffisante, n'est en principe pas protégée par le droit d'auteur, faute d'auteur humain identifiable et de caractère individuel au sens classique retenu par la loi et la jurisprudence. La situation peut toutefois être différente lorsque l'utilisateur apporte une contribution créative significative dans la conception ou le choix du résultat final obtenu à l'aide de l'outil."]}, {'heading': "L'entraînement des modèles sur des œuvres protégées", 'paragraphs': ["L'utilisation d'œuvres protégées par le droit d'auteur pour entraîner des systèmes d'intelligence artificielle soulève des questions juridiques encore largement ouvertes, notamment sur le point de savoir si une telle utilisation constitue une reproduction au sens de la loi nécessitant une autorisation, ou si elle peut être couverte par une exception légale existante. Cette question fait l'objet de débats et d'évolutions législatives dans plusieurs pays, dont la Suisse suit attentivement les développements."]}, {'heading': 'Un domaine à surveiller de près', 'paragraphs': ["Compte tenu de l'évolution rapide de la technologie et des réflexions législatives en cours, tant en Suisse qu'au niveau international, les entreprises et créateurs qui utilisent des outils d'intelligence artificielle dans leur activité créative ont intérêt à documenter précisément leur propre contribution créative et à suivre attentivement l'évolution du cadre légal applicable."]}], 'faq': [{'q': "Une image entièrement générée par une IA est-elle protégée par le droit d'auteur en Suisse ?", 'a': "En principe non, si aucune intervention créative humaine suffisante n'a été apportée, faute d'auteur humain identifiable et de caractère individuel au sens retenu par la loi suisse sur le droit d'auteur."}, {'q': "Puis-je revendiquer un droit d'auteur si j'ai guidé la génération d'un contenu par IA avec des choix créatifs précis ?", 'a': "C'est possible selon les circonstances, si votre contribution créative dans la conception ou la sélection du résultat final est jugée suffisamment significative, mais cette appréciation reste au cas par cas dans un domaine juridique encore en évolution."}, {'q': 'Entraîner une IA sur des œuvres protégées nécessite-t-il une autorisation ?', 'a': "La question reste juridiquement ouverte et débattue en droit suisse comme ailleurs. Il est recommandé de suivre attentivement l'évolution du cadre légal et de consulter un spécialiste pour toute utilisation à des fins commerciales."}]}},
    'reconnaissance-jugement-etranger-suisse': {'domaine_id': 'droit_international_prive', 'published': '2026-08-08', 'fr': {'slug': 'reconnaissance-jugement-etranger-suisse-conditions', 'title': "Reconnaissance d'un jugement étranger en Suisse", 'meta': 'Compétence indirecte, ordre public, Convention de Lugano : les conditions pour faire reconnaître et exécuter un jugement étranger en Suisse.', 'sections': [{'heading': 'Le cadre légal applicable', 'paragraphs': ["La reconnaissance et l'exécution des jugements étrangers en Suisse sont régies soit par des traités internationaux, notamment la Convention de Lugano pour l'espace formé par l'Union européenne et l'AELE, soit, à défaut de traité applicable, par la loi fédérale sur le droit international privé (LDIP), qui pose les conditions générales de reconnaissance."]}, {'heading': 'Les conditions générales de reconnaissance', 'paragraphs': ["Pour être reconnu en Suisse, un jugement étranger doit en principe émaner d'une autorité compétente selon les règles de compétence indirecte retenues par le droit suisse, être définitif et exécutoire dans l'État où il a été rendu, avoir respecté le droit d'être entendu des parties, et ne pas être manifestement contraire à l'ordre public suisse."]}, {'heading': "L'absence de contrariété avec une procédure suisse", 'paragraphs': ['La reconnaissance peut également être refusée si une procédure entre les mêmes parties et sur le même objet est déjà pendante en Suisse, ou si un jugement suisse déjà rendu sur la même affaire entre en contradiction avec le jugement étranger dont la reconnaissance est demandée.']}, {'heading': 'La procédure pratique', 'paragraphs': ["Selon les cas, la reconnaissance peut intervenir directement, de façon incidente dans une autre procédure, ou faire l'objet d'une procédure d'exequatur spécifique visant à obtenir formellement la reconnaissance et le caractère exécutoire du jugement en Suisse, notamment lorsque des mesures d'exécution forcée sont ensuite nécessaires sur des biens situés en Suisse."]}], 'faq': [{'q': "Un jugement rendu dans un pays de l'Union européenne est-il automatiquement reconnu en Suisse ?", 'a': "La Convention de Lugano facilite sa reconnaissance entre la Suisse et les États de l'UE et de l'AELE, mais certaines conditions, notamment l'absence de contrariété à l'ordre public suisse, restent applicables."}, {'q': 'Que se passe-t-il si le jugement étranger contredit une décision déjà rendue en Suisse ?', 'a': 'La reconnaissance peut être refusée dans ce cas, la Suisse donnant en principe la priorité à ses propres décisions déjà rendues sur le même objet entre les mêmes parties.'}, {'q': 'Faut-il une procédure spéciale pour exécuter un jugement étranger en Suisse ?', 'a': "Selon les cas, oui : une procédure d'exequatur peut être nécessaire, en particulier lorsque des mesures d'exécution forcée doivent être menées sur des biens situés en Suisse."}]}},
    'succession-internationale-droit-applicable': {'domaine_id': 'droit_international_prive', 'published': '2026-08-08', 'fr': {'slug': 'succession-internationale-droit-applicable-suisse', 'title': "Succession internationale : quel droit s'applique", 'meta': 'Domicile du défunt, choix du droit national par testament : les règles de la LDIP pour déterminer le droit applicable à une succession internationale.', 'sections': [{'heading': 'Le principe du domicile', 'paragraphs': ["Pour une personne domiciliée en Suisse au moment de son décès, les art. 90 et suivants LDIP prévoient en principe que les autorités et le droit suisses sont compétents pour régler l'ensemble de sa succession, quelle que soit sa nationalité, sous réserve des exceptions prévues par la loi."]}, {'heading': 'Le choix du droit national par un étranger domicilié en Suisse', 'paragraphs': ["Un ressortissant étranger domicilié en Suisse peut, par testament ou pacte successoral, soumettre l'ensemble de sa succession au droit de l'un de ses États nationaux plutôt qu'au droit suisse, une possibilité qui permet d'aligner sa planification successorale sur un système juridique dont il connaît mieux les règles, notamment en matière de réserve héréditaire."]}, {'heading': "Le cas du Suisse domicilié à l'étranger", 'paragraphs': ["Pour un ressortissant suisse domicilié à l'étranger, c'est en principe le droit de son domicile qui s'applique à sa succession, sous réserve d'une compétence spéciale des autorités suisses pouvant subsister pour les immeubles situés en Suisse dans certaines circonstances, ainsi que de la possibilité, selon les cas, de choisir le droit suisse pour l'ensemble de sa succession."]}, {'heading': "L'articulation avec le droit européen", 'paragraphs': ["La révision de la LDIP entrée en vigueur en 2018 a renforcé les possibilités de choix du droit applicable, notamment en cohérence avec le règlement européen sur les successions internationales, facilitant la coordination entre les systèmes suisse et européens pour les successions comportant un élément d'extranéité. Compte tenu de la complexité de cette matière, une planification successorale internationale mérite toujours l'accompagnement d'un professionnel connaissant les systèmes juridiques concernés."]}], 'faq': [{'q': 'Un étranger domicilié en Suisse est-il automatiquement soumis au droit successoral suisse ?', 'a': "En principe oui, sauf s'il choisit expressément, par testament ou pacte successoral, de soumettre sa succession au droit de l'un de ses États nationaux, une possibilité offerte par la LDIP."}, {'q': "Un Suisse vivant à l'étranger reste-t-il soumis au droit suisse pour sa succession ?", 'a': "Pas nécessairement : c'est en principe le droit de son domicile étranger qui s'applique, sous réserve d'exceptions notamment pour les immeubles situés en Suisse, et de la possibilité de choisir le droit suisse dans certains cas."}, {'q': 'Pourquoi choisir son droit national plutôt que le droit suisse pour sa succession ?', 'a': "Cela permet souvent d'aligner sa planification successorale sur un système juridique mieux connu, notamment en matière de réserve héréditaire, dont les règles varient sensiblement d'un pays à l'autre."}]}},
    'preuve-a-futur-procedure-civile-suisse': {'domaine_id': 'procedure_civile', 'published': '2026-08-08', 'fr': {'slug': 'preuve-a-futur-procedure-civile-suisse-art158', 'title': 'Preuve à futur : sécuriser une preuve avant un procès', 'meta': "Faire constater un état de fait avant qu'il ne disparaisse : les conditions de la preuve à futur selon l'art. 158 du Code de procédure civile (CPC).", 'sections': [{'heading': "L'objectif de la preuve à futur", 'paragraphs': ["L'art. 158 CPC permet de faire administrer une preuve, par exemple une expertise ou une inspection locale, avant même l'ouverture d'un procès ou en cours de procédure, lorsque certaines conditions sont remplies. L'objectif est d'éviter la perte d'un moyen de preuve important, par exemple un état des lieux appelé à disparaître ou à se modifier avec le temps."]}, {'heading': "Les conditions d'obtention", 'paragraphs': ["La loi prévoit deux hypothèses principales : soit la loi elle-même confère un droit à l'administration anticipée de la preuve, soit le requérant rend vraisemblable l'existence d'un intérêt digne de protection, ce qui inclut notamment le risque que la preuve disparaisse ou se détériore, ou encore le besoin d'évaluer ses chances de succès avant d'introduire une action."]}, {'heading': 'Un usage fréquent en matière de construction et de responsabilité civile', 'paragraphs': ["La preuve à futur est particulièrement utilisée en matière de défauts de construction ou d'accidents, où l'état des lieux ou des dommages évolue rapidement, par exemple lors de réparations urgentes ou de la démolition d'un ouvrage endommagé. Faire constater rapidement l'état des choses par un expert judiciaire permet de préserver des éléments de preuve qui seraient sinon perdus au moment du procès."]}, {'heading': 'Les effets de la preuve administrée', 'paragraphs': ['Une preuve valablement administrée par cette voie peut ensuite être utilisée dans le procès au fond, sans devoir être répétée, ce qui représente un gain de temps et de coûts appréciable, tout en garantissant la fiabilité de la preuve recueillie à un moment où les faits étaient encore vérifiables.']}], 'faq': [{'q': "Puis-je demander une preuve à futur même avant d'avoir décidé d'ouvrir un procès ?", 'a': "Oui, la preuve à futur peut notamment servir à évaluer ses chances de succès avant d'introduire une action, dès lors qu'un intérêt digne de protection est rendu vraisemblable."}, {'q': 'Dans quels domaines la preuve à futur est-elle le plus souvent utilisée ?', 'a': "Elle est particulièrement fréquente en matière de défauts de construction et de responsabilité civile, où l'état des lieux ou des dommages risque d'évoluer rapidement avant l'ouverture d'un procès."}, {'q': 'La preuve administrée en amont doit-elle être répétée lors du procès au fond ?', 'a': "Non, une preuve valablement administrée selon l'art. 158 CPC peut être utilisée directement dans le procès au fond, sans nouvelle administration."}]}},
    'recusation-juge-motifs-procedure': {'domaine_id': 'procedure_civile', 'published': '2026-08-08', 'fr': {'slug': 'recusation-juge-motifs-procedure-cpc', 'title': "Récusation d'un juge : motifs et procédure", 'meta': "Intérêt personnel, lien de parenté, apparence de prévention : les motifs de récusation d'un juge et le délai pour les invoquer selon le CPC.", 'sections': [{'heading': 'Le droit à un tribunal impartial', 'paragraphs': ["Le droit à un tribunal indépendant et impartial est un principe fondamental de la procédure, garanti tant par la Constitution fédérale que par les traités internationaux applicables en Suisse. La récusation est le mécanisme procédural permettant à une partie de demander qu'un juge donné ne siège pas dans une cause déterminée lorsque son impartialité paraît compromise."]}, {'heading': 'Les motifs de récusation', 'paragraphs': ["L'art. 47 CPC énumère plusieurs motifs de récusation : un intérêt personnel du juge dans la cause, un lien de parenté ou d'alliance avec une partie ou son représentant, le fait d'avoir agi comme représentant d'une partie dans une autre procédure, ou plus généralement toute autre circonstance de nature à faire redouter une prévention, ce qui recouvre notamment l'apparence objective de partialité, indépendamment d'une partialité effective démontrée."]}, {'heading': 'Le délai pour agir', 'paragraphs': ["Une demande de récusation doit en principe être déposée dès que la partie a connaissance du motif invoqué, sous peine de forclusion : attendre sans réagir alors que le motif est déjà connu prive généralement la partie de la possibilité de s'en prévaloir ultérieurement, notamment après une décision défavorable."]}, {'heading': 'Qui tranche la demande de récusation', 'paragraphs': ["La demande de récusation n'est pas tranchée par le juge visé lui-même, mais par une autre autorité, généralement une instance ou une composition différente au sein du même tribunal, afin de garantir l'objectivité de l'examen de la demande."]}], 'faq': [{'q': "Puis-je demander la récusation d'un juge simplement parce que je pense qu'il va statuer contre moi ?", 'a': 'Non, une simple crainte subjective sans fondement objectif ne suffit pas : il faut un motif prévu par la loi ou une circonstance concrète de nature à faire redouter objectivement une prévention.'}, {'q': 'Puis-je demander la récusation après avoir reçu un jugement défavorable ?', 'a': 'En principe non si le motif de récusation était déjà connu avant le jugement : la demande doit être déposée dès la connaissance du motif, sous peine de forclusion.'}, {'q': 'Le juge visé décide-t-il lui-même de sa propre récusation ?', 'a': 'Non, la demande est tranchée par une autre autorité, généralement une composition différente au sein du même tribunal, afin de garantir un examen objectif de la demande.'}]}},
    'detention-provisoire-conditions-duree': {'domaine_id': 'procedure_penale', 'published': '2026-08-08', 'fr': {'slug': 'detention-provisoire-conditions-duree-maximale', 'title': 'Détention provisoire : conditions et durée maximale', 'meta': 'Soupçons graves, risque de fuite ou de collusion, principe de proportionnalité : les conditions de la détention provisoire selon les art. 221 et suivants CPP.', 'sections': [{'heading': 'Les conditions de base', 'paragraphs': ["L'art. 221 CPP subordonne la détention provisoire à l'existence de soupçons graves laissant présumer que la personne concernée a commis un crime ou un délit, ainsi qu'à l'existence d'un risque particulier : risque de fuite, risque de collusion consistant à influencer des témoins ou détruire des preuves, ou risque de récidive pour certaines infractions graves. Pour certaines infractions particulièrement graves, la loi permet exceptionnellement de retenir la seule gravité des faits pour justifier la détention."]}, {'heading': "L'autorité compétente", 'paragraphs': ["La détention provisoire est ordonnée par le tribunal des mesures de contrainte, sur demande motivée du ministère public, à la suite d'une audience contradictoire au cours de laquelle la personne concernée peut faire valoir ses arguments, assistée d'un avocat."]}, {'heading': 'Le principe de proportionnalité et le réexamen périodique', 'paragraphs': ['La détention provisoire ne doit jamais excéder la durée probable de la peine encourue et doit être levée dès que les motifs qui la justifient disparaissent, ou remplacée par des mesures de substitution moins incisives, comme une obligation de se présenter régulièrement à la police, lorsque celles-ci suffisent à écarter le risque identifié. La loi ne fixe pas de durée maximale absolue, mais impose un réexamen périodique de sa justification.']}, {'heading': 'Les mesures de substitution', 'paragraphs': ["Le CPP prévoit un ensemble de mesures de substitution à la détention provisoire, telles que la fourniture de sûretés, la saisie de documents d'identité, une assignation à résidence ou une obligation de se présenter périodiquement à une autorité, permettant de répondre au risque identifié sans recourir à une privation de liberté complète."]}], 'faq': [{'q': 'Existe-t-il une durée maximale fixe pour la détention provisoire en Suisse ?', 'a': "La loi ne fixe pas de plafond absolu, mais impose le respect du principe de proportionnalité : la détention ne doit jamais excéder la durée probable de la peine encourue et fait l'objet d'un réexamen périodique."}, {'q': 'Qui décide de placer une personne en détention provisoire ?', 'a': "Le tribunal des mesures de contrainte, sur demande motivée du ministère public, à l'issue d'une audience contradictoire où la personne concernée peut faire valoir ses arguments avec l'assistance d'un avocat."}, {'q': 'Existe-t-il des alternatives à la détention provisoire ?', 'a': "Oui, le CPP prévoit des mesures de substitution comme la fourniture de sûretés, la saisie de documents d'identité ou une obligation de se présenter périodiquement à une autorité, applicables lorsqu'elles suffisent à écarter le risque identifié."}]}},
    'partie-plaignante-droits-procedure-penale': {'domaine_id': 'procedure_penale', 'published': '2026-08-08', 'fr': {'slug': 'partie-plaignante-droits-procedure-penale-suisse', 'title': 'Partie plaignante : droits dans la procédure pénale', 'meta': 'Consulter le dossier, proposer des preuves, faire valoir des conclusions civiles : les droits de la partie plaignante selon les art. 118 et suivants CPP.', 'sections': [{'heading': 'Devenir partie plaignante', 'paragraphs': ["Le lésé par une infraction peut déclarer vouloir participer à la procédure pénale comme accusateur privé, faire valoir des prétentions civiles découlant de l'infraction, ou les deux à la fois. Cette déclaration, prévue par l'art. 118 CPP, doit en principe intervenir avant la clôture de la procédure préliminaire pour permettre une participation pleine et entière."]}, {'heading': 'Les droits procéduraux', 'paragraphs': ["Une fois constituée, la partie plaignante peut consulter le dossier de la procédure, assister aux auditions et y participer, proposer l'administration de preuves complémentaires, et recourir contre certaines décisions qui la concernent directement, notamment une ordonnance de classement qu'elle estimerait injustifiée."]}, {'heading': "L'action civile adhésive", 'paragraphs': ["L'un des principaux intérêts du statut de partie plaignante est de pouvoir faire valoir ses conclusions civiles, par exemple une demande de dommages-intérêts ou de tort moral, directement dans le cadre de la procédure pénale plutôt que dans une action civile séparée devant un autre tribunal, ce qui simplifie considérablement les démarches de la victime."]}, {'heading': 'Les limites de ce statut', 'paragraphs': ["Le juge pénal peut, dans certains cas, renvoyer les conclusions civiles au juge civil s'il estime que leur traitement dans le cadre du procès pénal complique excessivement la procédure ou retarde son issue. La partie plaignante ne dispose par ailleurs pas des mêmes droits que le prévenu ou le ministère public sur l'ensemble des questions strictement pénales, son rôle restant centré sur la défense de ses propres intérêts liés à l'infraction."]}], 'faq': [{'q': 'Dois-je porter plainte pour devenir partie plaignante ?', 'a': "Pas nécessairement de manière formelle si l'infraction est poursuivie d'office, mais il faut en principe déclarer vouloir participer à la procédure comme accusateur privé et/ou faire valoir des conclusions civiles, avant la clôture de la procédure préliminaire."}, {'q': 'Puis-je réclamer des dommages-intérêts directement dans le procès pénal ?', 'a': "Oui, c'est l'un des principaux avantages du statut de partie plaignante : faire valoir ses conclusions civiles directement dans la procédure pénale, sans devoir engager une action civile séparée."}, {'q': "Puis-je recourir si le ministère public classe l'affaire ?", 'a': "Oui, la partie plaignante dispose en principe d'un droit de recours contre une ordonnance de classement qu'elle estimerait injustifiée, ce qui constitue l'un des droits procéduraux importants attachés à ce statut."}]}},
    'mediation-penale-quand-possible-suisse': {'domaine_id': 'mediation', 'published': '2026-08-08', 'fr': {'slug': 'mediation-penale-reparation-classement-suisse', 'title': 'Médiation pénale : quand elle est possible', 'meta': 'Médiation pour les mineurs, classement pour réparation du dommage chez les adultes : ce que le droit suisse permet en matière de résolution amiable au pénal.', 'sections': [{'heading': 'La médiation prévue pour les mineurs', 'paragraphs': ["Le droit pénal des mineurs prévoit expressément la possibilité de recourir à une médiation entre l'auteur mineur et la victime, encadrée par un médiateur formé à cette fonction, dans le but de favoriser la responsabilisation du jeune et une forme de réparation concrète envers la victime, en alternative ou en complément d'une sanction éducative classique."]}, {'heading': "L'absence de médiation pénale formalisée pour les adultes", 'paragraphs': ["Pour les auteurs majeurs, le droit pénal suisse ne prévoit pas de procédure de médiation pénale formalisée comparable à celle applicable aux mineurs. La logique de réparation entre auteur et victime existe néanmoins sous une autre forme, à travers la possibilité d'un classement de la procédure en cas de réparation du dommage."]}, {'heading': 'Le classement pour réparation du dommage', 'paragraphs': ["L'art. 53 CP permet au ministère public de classer une procédure lorsque l'auteur a réparé le dommage ou accompli tous les efforts que l'on pouvait raisonnablement attendre de lui pour compenser le tort causé, à condition que l'infraction soit poursuivie sur plainte ou reste de peu de gravité, et que l'intérêt public ainsi que celui de la victime à la poursuite pénale soient peu importants.", "Ce mécanisme se rapproche dans ses effets d'une médiation réussie, sans en suivre pour autant le même formalisme procédural que celui prévu pour les mineurs."]}, {'heading': 'Les limites de cette approche', 'paragraphs': ["Ce classement pour réparation reste réservé à des infractions de gravité limitée et suppose une réparation réelle et suffisante du dommage causé : il ne s'applique pas aux infractions graves poursuivies d'office dans l'intérêt public prépondérant, où la seule volonté des parties de trouver un accord ne suffit pas à écarter la poursuite pénale."]}], 'faq': [{'q': 'La médiation pénale existe-t-elle pour les adultes en Suisse ?', 'a': "Pas sous la forme formalisée prévue pour les mineurs. Pour les adultes, une logique de réparation peut néanmoins conduire à un classement de la procédure selon l'art. 53 CP, dans des conditions limitées."}, {'q': "Toute infraction peut-elle être classée si l'auteur répare le dommage ?", 'a': "Non, ce mécanisme suppose une infraction poursuivie sur plainte ou de peu de gravité, ainsi qu'un intérêt public et un intérêt de la victime à la poursuite qui restent peu importants."}, {'q': 'Comment fonctionne la médiation prévue pour les mineurs ?', 'a': "Elle se déroule entre l'auteur mineur et la victime, encadrée par un médiateur formé à cette fonction, dans le but de favoriser la responsabilisation du jeune et une réparation concrète, en alternative ou en complément d'une sanction éducative classique."}]}},
    'devenir-mediateur-agree-suisse': {'domaine_id': 'mediation', 'published': '2026-08-08', 'fr': {'slug': 'devenir-mediateur-agree-suisse-formation', 'title': 'Devenir médiateur agréé en Suisse', 'meta': "Pas de titre fédéral protégé, mais des certifications reconnues par les associations professionnelles : ce qu'il faut savoir pour devenir médiateur en Suisse.", 'sections': [{'heading': "L'absence de titre fédéral unique", 'paragraphs': ["Contrairement à certaines professions réglementées, le titre de médiateur n'est pas protégé de manière uniforme au niveau fédéral en Suisse. Il n'existe donc pas d'autorisation étatique unique conditionnant l'exercice de cette activité, ce qui a conduit les associations professionnelles du secteur à développer leurs propres standards de certification, largement reconnus sur le marché."]}, {'heading': 'Les certifications des associations professionnelles', 'paragraphs': ["Plusieurs associations, notamment au niveau des fédérations professionnelles de médiation actives en Suisse, délivrent des certifications reconnues, généralement conditionnées à un nombre déterminé d'heures de formation théorique et pratique, à des stages ou supervisions encadrées, et au respect d'un code de déontologie propre à la profession."]}, {'heading': 'Le cas particulier de la médiation familiale', 'paragraphs': ['En matière familiale, certains tribunaux ou autorités recommandent, voire orientent les parties vers des médiateurs ayant suivi une formation spécifique reconnue, notamment lorsque les enjeux touchent à des enfants mineurs. Se former spécifiquement à la médiation familiale constitue souvent un atout déterminant pour exercer dans ce domaine particulier.']}, {'heading': 'Construire une pratique professionnelle crédible', 'paragraphs': ["Au-delà de la certification elle-même, une pratique reconnue de la médiation suppose généralement une formation de base solide dans un domaine connexe, droit, psychologie ou travail social, complétée par la formation spécifique de médiateur, ainsi qu'une pratique régulière permettant de développer une expérience concrète reconnue par les pairs et les mandants potentiels."]}], 'faq': [{'q': "Faut-il un diplôme d'État pour devenir médiateur en Suisse ?", 'a': "Non, il n'existe pas de titre fédéral protégé de manière uniforme. Les certifications reconnues proviennent principalement des associations professionnelles du secteur, avec leurs propres exigences de formation."}, {'q': 'Une formation juridique est-elle nécessaire pour devenir médiateur ?', 'a': 'Pas obligatoirement, mais une formation de base dans un domaine connexe comme le droit, la psychologie ou le travail social, complétée par une formation spécifique de médiateur, est généralement recommandée pour construire une pratique crédible.'}, {'q': 'La médiation familiale requiert-elle une formation particulière ?', 'a': 'Oui, une formation spécifique reconnue en médiation familiale constitue souvent un atout déterminant, certains tribunaux et autorités orientant les parties vers des médiateurs ayant suivi ce type de formation, en particulier lorsque des enfants mineurs sont concernés.'}]}},
    'plan-affectation-zone-reservee-suisse': {'domaine_id': 'droit_construction_amenagement', 'published': '2026-08-08', 'fr': {'slug': 'plan-affectation-zone-reservee-suisse-lat', 'title': "Plan d'affectation et zone réservée : ce qu'ils impliquent", 'meta': "Ce que le plan de zones communal règle, et pourquoi une zone réservée peut geler temporairement la constructibilité d'un secteur selon l'art. 27 LAT.", 'sections': [{'heading': "Le plan d'affectation communal", 'paragraphs': ["Le plan d'affectation, généralement appelé plan de zones au niveau communal, détermine l'utilisation autorisée du sol sur le territoire de la commune : zone à bâtir résidentielle, mixte ou d'activités, zone agricole, zone protégée. Ce document est contraignant pour les propriétaires et détermine concrètement ce qu'il est possible de construire, et où, sur une parcelle donnée."]}, {'heading': 'La révision périodique des plans', 'paragraphs': ["Les plans d'affectation ne sont pas figés définitivement : ils peuvent être révisés par les autorités communales et cantonales compétentes, dans le respect des principes fédéraux d'aménagement du territoire, notamment pour s'adapter à l'évolution des besoins en matière de logement ou pour mieux respecter les objectifs de limitation de l'étalement urbain fixés par la loi."]}, {'heading': 'La zone réservée : une mesure provisoire', 'paragraphs': ["L'art. 27 LAT permet à l'autorité compétente d'instaurer une zone réservée dans les territoires dont l'affectation doit être précisée ou modifiée : cette mesure gèle temporairement, en principe pour une durée maximale de cinq ans, prolongeable dans certains cas, la constructibilité d'un secteur, le temps que la planification définitive soit élaborée ou révisée."]}, {'heading': 'Pourquoi cette mesure existe', 'paragraphs': ["Sans une telle mesure provisoire, des projets de construction pourraient être réalisés pendant la phase d'élaboration d'un nouveau plan et compromettre définitivement les objectifs poursuivis par celui-ci, par exemple en construisant précisément dans une zone que la nouvelle planification entend préserver. La zone réservée protège ainsi la cohérence du processus de planification en cours."]}], 'faq': [{'q': "Un plan d'affectation communal peut-il être modifié après son adoption ?", 'a': "Oui, les plans d'affectation peuvent être révisés par les autorités compétentes, dans le respect des principes fédéraux d'aménagement du territoire, ce qui peut modifier la constructibilité d'une parcelle au fil du temps."}, {'q': 'Que signifie concrètement une zone réservée pour un propriétaire ?', 'a': "Elle gèle temporairement, en principe pour une durée maximale de cinq ans, la possibilité de construire ou de modifier significativement l'affectation d'un bien-fonds, le temps que la nouvelle planification soit élaborée."}, {'q': "Pourquoi instaurer une zone réservée plutôt que d'attendre la nouvelle planification ?", 'a': "Pour éviter que des projets de construction réalisés pendant la phase d'élaboration ne compromettent définitivement les objectifs poursuivis par le futur plan d'affectation, notamment dans des secteurs appelés à être préservés."}]}},
    'expropriation-formelle-indemnisation-procedure': {'domaine_id': 'droit_construction_amenagement', 'published': '2026-08-08', 'fr': {'slug': 'expropriation-formelle-indemnisation-procedure-suisse', 'title': 'Expropriation formelle : indemnisation et procédure', 'meta': "Indemnité pleine et entière, Commission fédérale d'estimation, recours possibles : la procédure d'expropriation pour un projet d'intérêt public en Suisse.", 'sections': [{'heading': "Le cadre légal de l'expropriation", 'paragraphs': ["L'expropriation permet à la collectivité publique ou à un tiers habilité par la loi d'acquérir de force la propriété ou certains droits sur un bien-fonds, lorsque cela s'avère nécessaire à la réalisation d'un projet d'intérêt public reconnu, tel qu'une infrastructure routière ou ferroviaire. Au niveau fédéral, la loi sur l'expropriation (LEx) encadre cette procédure ; les cantons disposent de leurs propres lois analogues pour les projets d'intérêt cantonal ou communal."]}, {'heading': "Le principe de l'indemnité pleine et entière", 'paragraphs': ["Le propriétaire excusé doit recevoir une indemnité pleine et entière, censée compenser intégralement le préjudice subi : la valeur vénale du bien excusé lui-même, mais aussi les dommages supplémentaires éventuels, comme la perte de rendement d'une activité exercée sur le bien, les frais de déménagement, ou la moins-value affectant la partie restante d'une parcelle partiellement expropriée."]}, {'heading': "La Commission fédérale d'estimation", 'paragraphs': ["Au niveau fédéral, c'est la Commission fédérale d'estimation (CFE) qui est compétente pour fixer le montant de l'indemnité lorsque les parties ne parviennent pas à un accord amiable, à l'issue d'une procédure permettant à chacune de faire valoir ses arguments et, le cas échéant, de recourir à une expertise."]}, {'heading': 'Les voies de recours', 'paragraphs': ["Les décisions rendues en matière d'expropriation peuvent en principe faire l'objet d'un recours au Tribunal administratif fédéral, puis, en dernier ressort, au Tribunal fédéral, ce qui permet un contrôle juridictionnel complet tant sur le principe de l'expropriation que sur le montant de l'indemnité fixée."]}], 'faq': [{'q': "Puis-je m'opposer au principe même de l'expropriation ?", 'a': "Oui, dans le cadre de la procédure, il est possible de contester la nécessité ou la légalité du projet justifiant l'expropriation, avec des voies de recours jusqu'au Tribunal fédéral en dernier ressort."}, {'q': "L'indemnité couvre-t-elle uniquement la valeur du terrain excusé ?", 'a': "Non, elle doit être pleine et entière et couvrir également les dommages supplémentaires, comme la perte de rendement d'une activité, les frais de déménagement ou la moins-value du solde de la parcelle."}, {'q': "Qui fixe le montant de l'indemnité en cas de désaccord ?", 'a': "Au niveau fédéral, c'est la Commission fédérale d'estimation (CFE) qui tranche en l'absence d'accord amiable entre les parties, sa décision pouvant ensuite faire l'objet d'un recours."}]}},
}
