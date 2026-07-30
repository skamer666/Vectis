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
    },
}
