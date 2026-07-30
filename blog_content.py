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
        "fr": {
            "slug": "licenciement-delais-preavis-conge-abusif",
            "title": "Licenciement en Suisse : délais de préavis et protection contre le congé abusif",
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
            "title": "Kündigung in der Schweiz: Kündigungsfristen und Schutz vor missbräuchlicher Kündigung",
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
            "title": "Licenziamento in Svizzera: termini di disdetta e protezione contro il licenziamento abusivo",
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
            "title": "Termination of employment in Switzerland: notice periods and protection against abusive dismissal",
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
}
