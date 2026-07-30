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
}
