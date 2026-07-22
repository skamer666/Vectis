#!/usr/bin/env python3
"""
Contenu des guides pratiques (couche editoriale SEO), dans les 4 langues.
Regle de non-fabrication : uniquement des informations juridiques generales,
stables et verifiables (bases legales citees : Cst., LLCA, CPC, CPP, CP).
Aucun chiffre invente (pas de tarifs horaires "moyens" non sources).
"""

GUIDES = {
    "choisir-avocat": {
        "fr": {
            "slug": "comment-choisir-son-avocat",
            "title": "Comment choisir son avocat en Suisse",
            "meta": "Registre cantonal, domaines de compétence, langues, honoraires : les critères concrets pour choisir un avocat en Suisse.",
            "sections": [
                {"heading": "Vérifier l'inscription au registre cantonal", "paragraphs": [
                    "En Suisse, seuls les avocats inscrits à un registre cantonal peuvent représenter des clients devant les tribunaux civils et pénaux. Cette inscription, régie par la loi fédérale sur la libre circulation des avocats (LLCA), garantit que l'avocat est titulaire du brevet, qu'il est soumis à la surveillance de l'autorité cantonale et qu'il dispose d'une assurance responsabilité civile professionnelle.",
                    "Un avocat inscrit dans un canton peut plaider dans toute la Suisse. L'inscription au registre est donc le premier critère à vérifier — c'est précisément la donnée de base que Legatis référence, canton par canton, à partir des registres officiels.",
                ]},
                {"heading": "Le domaine de compétence avant tout", "paragraphs": [
                    "Le droit suisse est vaste : un excellent avocat en droit des sociétés n'est pas nécessairement le bon choix pour un divorce. Cherchez un avocat qui traite régulièrement des affaires comparables à la vôtre — droit du travail, droit du bail, droit pénal, droit de la famille, etc.",
                    "Certains avocats portent le titre d'« avocat spécialiste FSA », décerné par la Fédération Suisse des Avocats dans des domaines déterminés après une formation approfondie et une pratique attestée. Ce titre est un signal fiable de spécialisation, mais son absence ne signifie pas incompétence : beaucoup d'excellents praticiens n'ont simplement pas entrepris cette certification.",
                ]},
                {"heading": "Langue, proximité et relation de confiance", "paragraphs": [
                    "La procédure se déroule dans la langue officielle du canton où siège le tribunal. Un avocat qui pratique cette langue — et qui peut vous expliquer le dossier dans la vôtre — est un atout concret. La proximité géographique compte aussi : un avocat local connaît les tribunaux, les usages et les délais du canton.",
                    "Enfin, la relation de confiance est déterminante. Un premier entretien permet de juger si l'avocat écoute, explique clairement votre situation juridique, vos chances de succès et sa méthode de facturation. N'hésitez pas à poser ces questions d'emblée : un avocat sérieux y répond volontiers.",
                ]},
            ],
            "faq": [
                {"q": "Un avocat inscrit dans un autre canton peut-il me représenter ?",
                 "a": "Oui. L'inscription à un registre cantonal permet de pratiquer la représentation en justice dans toute la Suisse. Un avocat genevois peut plaider à Zurich, et inversement. En pratique, un avocat local connaît toutefois mieux les usages du tribunal concerné."},
                {"q": "Que signifie le titre « avocat spécialiste FSA » ?",
                 "a": "C'est un titre décerné par la Fédération Suisse des Avocats, qui atteste d'une formation approfondie et d'une expérience pratique importante dans un domaine précis du droit (droit du travail, droit de la famille, droit pénal, etc.)."},
                {"q": "Suis-je obligé de prendre un avocat pour aller en justice ?",
                 "a": "Dans la plupart des procédures civiles suisses, vous pouvez agir seul, sans avocat. Un avocat devient obligatoire dans certains cas (notamment la défense pénale obligatoire prévue par l'art. 130 CPP). Même quand il n'est pas obligatoire, son assistance est souvent décisive dès que l'affaire est complexe ou que l'enjeu est important."},
                {"q": "Comment vérifier qu'un avocat est bien inscrit au registre ?",
                 "a": "Chaque canton tient un registre public de ses avocats, consultable auprès de l'autorité cantonale de surveillance. Legatis référence les avocats à partir de ces registres officiels et indique le canton d'inscription sur chaque fiche."},
            ],
        },
        "de": {
            "slug": "anwalt-auswaehlen",
            "title": "Wie wählt man in der Schweiz die richtige Anwältin oder den richtigen Anwalt?",
            "meta": "Kantonales Anwaltsregister, Fachgebiete, Sprachen, Honorar: die konkreten Kriterien für die Anwaltswahl in der Schweiz.",
            "sections": [
                {"heading": "Eintrag im kantonalen Anwaltsregister prüfen", "paragraphs": [
                    "In der Schweiz dürfen nur im kantonalen Anwaltsregister eingetragene Anwältinnen und Anwälte Parteien vor Zivil- und Strafgerichten vertreten. Der Registereintrag richtet sich nach dem Bundesgesetz über die Freizügigkeit der Anwältinnen und Anwälte (BGFA) und garantiert Anwaltspatent, kantonale Aufsicht und eine Berufshaftpflichtversicherung.",
                    "Wer in einem Kanton eingetragen ist, darf in der ganzen Schweiz vor Gericht auftreten. Der Registereintrag ist somit das erste Kriterium — genau diese Grundlage erfasst Legatis Kanton für Kanton aus den offiziellen Registern.",
                ]},
                {"heading": "Das Fachgebiet ist entscheidend", "paragraphs": [
                    "Das schweizerische Recht ist breit: Eine hervorragende Gesellschaftsrechtlerin ist nicht zwingend die richtige Wahl für eine Scheidung. Suchen Sie jemanden, der regelmässig Fälle wie Ihren bearbeitet — Arbeitsrecht, Mietrecht, Strafrecht, Familienrecht usw.",
                    "Einige tragen den Titel «Fachanwältin/Fachanwalt SAV», den der Schweizerische Anwaltsverband nach vertiefter Weiterbildung und nachgewiesener Praxis in bestimmten Rechtsgebieten verleiht. Der Titel ist ein verlässliches Spezialisierungssignal — sein Fehlen bedeutet aber keine Inkompetenz.",
                ]},
                {"heading": "Sprache, Nähe und Vertrauen", "paragraphs": [
                    "Das Verfahren wird in der Amtssprache des Gerichtskantons geführt. Eine Anwältin, die diese Sprache beherrscht und Ihnen den Fall in Ihrer Sprache erklären kann, ist ein konkreter Vorteil. Auch die örtliche Nähe zählt: Wer lokal praktiziert, kennt Gerichte, Gepflogenheiten und Fristen des Kantons.",
                    "Entscheidend ist schliesslich das Vertrauensverhältnis. Ein Erstgespräch zeigt, ob die Anwältin zuhört, Ihre Rechtslage und Erfolgsaussichten klar erklärt und die Abrechnung transparent darlegt. Fragen Sie das ruhig direkt — seriöse Anwältinnen und Anwälte antworten gern.",
                ]},
            ],
            "faq": [
                {"q": "Darf mich ein Anwalt aus einem anderen Kanton vertreten?",
                 "a": "Ja. Der Eintrag in einem kantonalen Register erlaubt die Parteivertretung in der ganzen Schweiz. Ein Genfer Anwalt darf in Zürich plädieren und umgekehrt. In der Praxis kennt eine lokale Anwältin die Gepflogenheiten des Gerichts allerdings besser."},
                {"q": "Was bedeutet der Titel «Fachanwalt SAV»?",
                 "a": "Ein vom Schweizerischen Anwaltsverband verliehener Titel, der eine vertiefte Weiterbildung und erhebliche praktische Erfahrung in einem bestimmten Rechtsgebiet belegt (Arbeitsrecht, Familienrecht, Strafrecht usw.)."},
                {"q": "Brauche ich zwingend einen Anwalt vor Gericht?",
                 "a": "In den meisten Zivilverfahren können Sie selbst handeln. In gewissen Fällen ist die Verteidigung obligatorisch (namentlich die notwendige Verteidigung nach Art. 130 StPO). Auch ohne Pflicht ist anwaltliche Unterstützung bei komplexen oder folgenreichen Fällen oft entscheidend."},
                {"q": "Wie prüfe ich den Registereintrag?",
                 "a": "Jeder Kanton führt ein öffentliches Anwaltsregister bei der kantonalen Aufsichtsbehörde. Legatis erfasst Anwältinnen und Anwälte aus diesen offiziellen Registern und nennt auf jedem Profil den Eintragungskanton."},
            ],
        },
        "it": {
            "slug": "come-scegliere-avvocato",
            "title": "Come scegliere il proprio avvocato in Svizzera",
            "meta": "Albo cantonale, ambiti di competenza, lingue, onorari: i criteri concreti per scegliere un avvocato in Svizzera.",
            "sections": [
                {"heading": "Verificare l'iscrizione all'albo cantonale", "paragraphs": [
                    "In Svizzera solo gli avvocati iscritti a un albo cantonale possono rappresentare le parti davanti ai tribunali civili e penali. L'iscrizione, disciplinata dalla legge federale sulla libera circolazione degli avvocati (LLCA), garantisce il possesso della patente, la vigilanza dell'autorità cantonale e un'assicurazione di responsabilità civile professionale.",
                    "Un avvocato iscritto in un cantone può patrocinare in tutta la Svizzera. L'iscrizione all'albo è dunque il primo criterio da verificare — ed è esattamente il dato di base che Legatis censisce, cantone per cantone, dagli albi ufficiali.",
                ]},
                {"heading": "Prima di tutto l'ambito di competenza", "paragraphs": [
                    "Il diritto svizzero è vasto: un eccellente avvocato societario non è necessariamente la scelta giusta per un divorzio. Cercate chi tratta regolarmente casi simili al vostro — diritto del lavoro, diritto di locazione, diritto penale, diritto di famiglia, ecc.",
                    "Alcuni portano il titolo di «avvocato specialista FSA», conferito dalla Federazione Svizzera degli Avvocati in ambiti determinati dopo una formazione approfondita e una pratica comprovata. È un segnale affidabile di specializzazione, ma la sua assenza non significa incompetenza.",
                ]},
                {"heading": "Lingua, vicinanza e fiducia", "paragraphs": [
                    "La procedura si svolge nella lingua ufficiale del cantone del tribunale. Un avvocato che padroneggia quella lingua — e può spiegarvi il caso nella vostra — è un vantaggio concreto. Conta anche la vicinanza: chi esercita localmente conosce tribunali, prassi e termini del cantone.",
                    "Infine è determinante il rapporto di fiducia. Un primo colloquio permette di capire se l'avvocato ascolta, spiega chiaramente la situazione giuridica, le probabilità di successo e le modalità di fatturazione. Ponete queste domande subito: un professionista serio risponde volentieri.",
                ]},
            ],
            "faq": [
                {"q": "Un avvocato iscritto in un altro cantone può rappresentarmi?",
                 "a": "Sì. L'iscrizione a un albo cantonale consente il patrocinio in tutta la Svizzera. Un avvocato ginevrino può patrocinare a Zurigo e viceversa. In pratica, però, un avvocato locale conosce meglio le prassi del tribunale."},
                {"q": "Cosa significa il titolo «avvocato specialista FSA»?",
                 "a": "È un titolo conferito dalla Federazione Svizzera degli Avvocati che attesta una formazione approfondita e un'esperienza pratica rilevante in un ambito preciso del diritto (diritto del lavoro, diritto di famiglia, diritto penale, ecc.)."},
                {"q": "Sono obbligato a prendere un avvocato per andare in tribunale?",
                 "a": "Nella maggior parte delle procedure civili potete agire da soli. In certi casi la difesa è obbligatoria (in particolare la difesa obbligatoria dell'art. 130 CPP). Anche quando non è imposta, l'assistenza di un avvocato è spesso decisiva nei casi complessi o con posta in gioco elevata."},
                {"q": "Come verifico l'iscrizione all'albo?",
                 "a": "Ogni cantone tiene un albo pubblico presso l'autorità cantonale di vigilanza. Legatis censisce gli avvocati a partire da questi albi ufficiali e indica su ogni scheda il cantone di iscrizione."},
            ],
        },
        "en": {
            "slug": "how-to-choose-a-lawyer",
            "title": "How to choose a lawyer in Switzerland",
            "meta": "Cantonal bar registry, practice areas, languages, fees: the practical criteria for choosing a lawyer in Switzerland.",
            "sections": [
                {"heading": "Check the cantonal bar registry", "paragraphs": [
                    "In Switzerland, only lawyers entered in a cantonal bar registry may represent clients before the civil and criminal courts. Registration is governed by the Federal Act on the Free Movement of Lawyers (BGFA/LLCA) and guarantees that the lawyer holds the bar licence, is supervised by the cantonal authority and carries professional liability insurance.",
                    "A lawyer registered in one canton may appear before courts anywhere in Switzerland. Registry status is therefore the first thing to verify — and it is precisely the base data Legatis lists, canton by canton, from the official registers.",
                ]},
                {"heading": "Practice area comes first", "paragraphs": [
                    "Swiss law is broad: an excellent corporate lawyer is not necessarily the right choice for a divorce. Look for someone who regularly handles cases like yours — employment law, tenancy law, criminal law, family law, and so on.",
                    "Some lawyers hold the title of \"Certified Specialist SBA\" (avocat spécialiste FSA / Fachanwalt SAV), awarded by the Swiss Bar Association in defined fields after advanced training and proven practice. The title is a reliable signal of specialisation, though its absence does not imply incompetence.",
                ]},
                {"heading": "Language, proximity and trust", "paragraphs": [
                    "Proceedings are conducted in the official language of the canton where the court sits. A lawyer who works in that language — and can explain your case in yours — is a concrete advantage. Local proximity also matters: a local practitioner knows the courts, customs and deadlines of the canton.",
                    "Finally, trust is decisive. A first meeting shows whether the lawyer listens, explains your legal position and prospects clearly, and is transparent about billing. Ask these questions upfront: a serious lawyer will answer them readily.",
                ]},
            ],
            "faq": [
                {"q": "Can a lawyer registered in another canton represent me?",
                 "a": "Yes. Registration in one cantonal registry allows court representation throughout Switzerland. A Geneva lawyer may plead in Zurich and vice versa. In practice, a local lawyer will know the habits of the court concerned better."},
                {"q": "What does \"Certified Specialist SBA\" mean?",
                 "a": "It is a title awarded by the Swiss Bar Association attesting to advanced training and substantial practical experience in a specific field of law (employment law, family law, criminal law, etc.)."},
                {"q": "Do I need a lawyer to go to court in Switzerland?",
                 "a": "In most Swiss civil proceedings you may act on your own. Representation is mandatory in certain cases (notably mandatory criminal defence under art. 130 of the Criminal Procedure Code). Even where not required, a lawyer's assistance is often decisive once a case is complex or the stakes are high."},
                {"q": "How can I verify a lawyer's registration?",
                 "a": "Each canton keeps a public registry of its lawyers with the cantonal supervisory authority. Legatis lists lawyers from these official registers and shows the canton of registration on each profile."},
            ],
        },
    },
    "cout-avocat": {
        "fr": {
            "slug": "combien-coute-un-avocat",
            "title": "Combien coûte un avocat en Suisse ?",
            "meta": "Honoraires au temps, provision, pacte de résultat, assurance de protection juridique : comment se calculent les frais d'avocat en Suisse.",
            "sections": [
                {"heading": "Pas de tarif unique : les facteurs qui comptent", "paragraphs": [
                    "Il n'existe pas de tarif horaire fédéral unique pour les avocats suisses. Les honoraires dépendent du canton, de l'expérience et de la spécialisation de l'avocat, de la complexité et de l'urgence de l'affaire, ainsi que de la valeur litigieuse. Plusieurs cantons connaissent des tarifs ou usages pour les dépens alloués en procédure, mais la facturation entre l'avocat et son client reste largement contractuelle.",
                    "La règle d'or : demander dès le premier entretien comment l'avocat facture (taux horaire, forfait, ou combinaison), à quelle fréquence il rend compte des heures effectuées, et à combien il estime — même grossièrement — le coût total prévisible de votre affaire.",
                ]},
                {"heading": "Provision, note d'honoraires et contestation", "paragraphs": [
                    "Il est usuel que l'avocat demande une provision, c'est-à-dire une avance sur honoraires, avant de commencer le travail. Les prestations sont ensuite décomptées au fur et à mesure. Vous avez droit à un décompte détaillé des opérations effectuées.",
                    "En cas de désaccord sur une note d'honoraires, la plupart des cantons et des ordres d'avocats offrent une procédure de modération ou de conciliation permettant de faire examiner la facture par une autorité ou une commission indépendante.",
                ]},
                {"heading": "Honoraires de résultat : ce qui est permis", "paragraphs": [
                    "Le droit suisse interdit le pactum de quota litis, c'est-à-dire l'accord par lequel l'avocat serait rémunéré exclusivement par une part du résultat obtenu. En revanche, une prime de résultat qui s'ajoute à des honoraires de base couvrant au moins les coûts de l'avocat (pactum de palmario) est admise à certaines conditions par la jurisprudence.",
                    "Pensez aussi à l'assurance de protection juridique : si vous en avez souscrit une avant le litige, elle peut prendre en charge tout ou partie des frais d'avocat, selon les conditions de la police. Vérifiez votre couverture avant d'engager des frais.",
                ]},
            ],
            "faq": [
                {"q": "Un avocat peut-il être payé uniquement au résultat ?",
                 "a": "Non. Le pactum de quota litis (rémunération exclusivement en pourcentage du résultat) est interdit en Suisse. Une prime de succès s'ajoutant à des honoraires de base raisonnables est en revanche possible à certaines conditions."},
                {"q": "Qu'est-ce qu'une provision ?",
                 "a": "Une avance sur honoraires demandée avant le début du travail, usuelle en Suisse. Elle est ensuite imputée sur les notes d'honoraires successives, qui doivent détailler les opérations effectuées."},
                {"q": "Que faire si je conteste la note d'honoraires ?",
                 "a": "Demandez d'abord un décompte détaillé. La plupart des cantons et des ordres d'avocats offrent ensuite une procédure de modération ou de conciliation pour faire examiner la facture par une instance indépendante."},
                {"q": "Qui paie les frais d'avocat si je gagne mon procès ?",
                 "a": "En procédure civile, la partie qui succombe est en principe condamnée aux frais, y compris une participation aux honoraires d'avocat de la partie adverse (dépens). Cette participation est fixée selon les tarifs cantonaux et ne couvre pas toujours l'intégralité des honoraires réellement facturés."},
                {"q": "Et si je n'ai pas les moyens de payer un avocat ?",
                 "a": "L'assistance judiciaire peut prendre en charge les frais de procédure et un avocat d'office si vous ne disposez pas des ressources nécessaires et que votre cause n'est pas dépourvue de chances de succès (art. 29 al. 3 Cst.). Voir notre guide dédié à l'assistance judiciaire."},
            ],
        },
        "de": {
            "slug": "was-kostet-ein-anwalt",
            "title": "Was kostet ein Anwalt in der Schweiz?",
            "meta": "Stundenhonorar, Kostenvorschuss, Erfolgshonorar, Rechtsschutzversicherung: wie sich Anwaltskosten in der Schweiz berechnen.",
            "sections": [
                {"heading": "Kein Einheitstarif: diese Faktoren zählen", "paragraphs": [
                    "Es gibt keinen schweizweiten Einheits-Stundenansatz für Anwältinnen und Anwälte. Das Honorar hängt vom Kanton, von Erfahrung und Spezialisierung, von Komplexität und Dringlichkeit des Falls sowie vom Streitwert ab. Mehrere Kantone kennen Tarife für die Parteientschädigung im Prozess; die Abrechnung zwischen Anwalt und Klient bleibt aber weitgehend Vertragssache.",
                    "Die goldene Regel: Fragen Sie schon im Erstgespräch, wie abgerechnet wird (Stundenansatz, Pauschale oder Kombination), wie oft über die geleisteten Stunden Rechenschaft abgelegt wird und wie hoch die Gesamtkosten voraussichtlich — auch grob — ausfallen dürften.",
                ]},
                {"heading": "Kostenvorschuss, Honorarnote und Beanstandung", "paragraphs": [
                    "Üblich ist ein Kostenvorschuss vor Arbeitsbeginn. Die Leistungen werden danach laufend abgerechnet. Sie haben Anspruch auf eine detaillierte Aufstellung der erbrachten Leistungen.",
                    "Bei Streit über eine Honorarnote bieten die meisten Kantone und Anwaltsverbände ein Moderations- oder Schlichtungsverfahren an, in dem eine unabhängige Stelle die Rechnung prüft.",
                ]},
                {"heading": "Erfolgshonorar: was zulässig ist", "paragraphs": [
                    "Das schweizerische Recht verbietet das pactum de quota litis — die Vergütung ausschliesslich durch eine Beteiligung am Prozessergebnis. Zulässig ist unter bestimmten Voraussetzungen hingegen eine Erfolgsprämie zusätzlich zu einem Grundhonorar, das mindestens die Kosten des Anwalts deckt (pactum de palmario).",
                    "Denken Sie auch an die Rechtsschutzversicherung: Wurde sie vor dem Streitfall abgeschlossen, kann sie die Anwaltskosten je nach Police ganz oder teilweise übernehmen. Prüfen Sie Ihre Deckung, bevor Kosten entstehen.",
                ]},
            ],
            "faq": [
                {"q": "Darf ein Anwalt rein erfolgsabhängig bezahlt werden?",
                 "a": "Nein. Das pactum de quota litis (Vergütung ausschliesslich als Anteil am Ergebnis) ist in der Schweiz verboten. Eine Erfolgsprämie zusätzlich zu einem angemessenen Grundhonorar ist unter Voraussetzungen zulässig."},
                {"q": "Was ist ein Kostenvorschuss?",
                 "a": "Eine vor Arbeitsbeginn verlangte Vorauszahlung auf das Honorar, in der Schweiz üblich. Sie wird mit den späteren, detaillierten Honorarnoten verrechnet."},
                {"q": "Was tun bei einer strittigen Honorarnote?",
                 "a": "Zuerst eine detaillierte Leistungsaufstellung verlangen. Danach bieten die meisten Kantone und Anwaltsverbände ein Moderations- oder Schlichtungsverfahren durch eine unabhängige Stelle an."},
                {"q": "Wer zahlt die Anwaltskosten, wenn ich gewinne?",
                 "a": "Im Zivilprozess trägt grundsätzlich die unterliegende Partei die Kosten, einschliesslich einer Parteientschädigung an die Gegenseite. Diese richtet sich nach kantonalen Tarifen und deckt das tatsächlich verrechnete Honorar nicht immer vollständig."},
                {"q": "Und wenn ich mir keinen Anwalt leisten kann?",
                 "a": "Die unentgeltliche Rechtspflege kann Verfahrenskosten und einen unentgeltlichen Rechtsbeistand übernehmen, wenn die nötigen Mittel fehlen und das Begehren nicht aussichtslos ist (Art. 29 Abs. 3 BV). Siehe unseren Ratgeber zur unentgeltlichen Rechtspflege."},
            ],
        },
        "it": {
            "slug": "quanto-costa-un-avvocato",
            "title": "Quanto costa un avvocato in Svizzera?",
            "meta": "Onorario orario, anticipo, patto di risultato, assicurazione di protezione giuridica: come si calcolano le spese legali in Svizzera.",
            "sections": [
                {"heading": "Nessuna tariffa unica: i fattori che contano", "paragraphs": [
                    "Non esiste una tariffa oraria federale unica per gli avvocati svizzeri. L'onorario dipende dal cantone, dall'esperienza e specializzazione dell'avvocato, dalla complessità e urgenza del caso e dal valore litigioso. Diversi cantoni prevedono tariffe per le ripetibili processuali, ma la fatturazione tra avvocato e cliente resta in gran parte contrattuale.",
                    "La regola d'oro: chiedere fin dal primo colloquio come l'avvocato fattura (tariffa oraria, forfait o combinazione), con quale frequenza rende conto delle ore svolte e a quanto stima — anche approssimativamente — il costo totale prevedibile.",
                ]},
                {"heading": "Anticipo, nota d'onorario e contestazione", "paragraphs": [
                    "È usuale che l'avvocato chieda un anticipo prima di iniziare il lavoro. Le prestazioni vengono poi conteggiate progressivamente. Avete diritto a un conteggio dettagliato delle operazioni svolte.",
                    "In caso di disaccordo su una nota d'onorario, la maggior parte dei cantoni e degli ordini degli avvocati offre una procedura di moderazione o conciliazione davanti a un'istanza indipendente.",
                ]},
                {"heading": "Onorario di risultato: cosa è permesso", "paragraphs": [
                    "Il diritto svizzero vieta il pactum de quota litis, cioè l'accordo con cui l'avvocato sarebbe remunerato esclusivamente con una quota del risultato. È invece ammesso, a certe condizioni, un premio di risultato che si aggiunge a un onorario di base che copra almeno i costi dell'avvocato (pactum de palmario).",
                    "Pensate anche all'assicurazione di protezione giuridica: se stipulata prima della controversia, può coprire in tutto o in parte le spese legali secondo la polizza. Verificate la copertura prima di impegnare spese.",
                ]},
            ],
            "faq": [
                {"q": "Un avvocato può essere pagato solo in base al risultato?",
                 "a": "No. Il pactum de quota litis (remunerazione esclusivamente in percentuale del risultato) è vietato in Svizzera. Un premio di successo in aggiunta a un onorario di base ragionevole è invece possibile a certe condizioni."},
                {"q": "Cos'è l'anticipo?",
                 "a": "Un versamento anticipato sull'onorario richiesto prima dell'inizio del lavoro, usuale in Svizzera. Viene poi imputato sulle note d'onorario successive, che devono dettagliare le operazioni svolte."},
                {"q": "Cosa fare se contesto la nota d'onorario?",
                 "a": "Chiedete prima un conteggio dettagliato. La maggior parte dei cantoni e degli ordini degli avvocati offre poi una procedura di moderazione o conciliazione davanti a un'istanza indipendente."},
                {"q": "Chi paga le spese legali se vinco la causa?",
                 "a": "Nella procedura civile la parte soccombente è di regola condannata alle spese, compresa un'indennità per le ripetibili della controparte, fissata secondo le tariffe cantonali; non sempre copre l'intero onorario effettivamente fatturato."},
                {"q": "E se non posso permettermi un avvocato?",
                 "a": "Il gratuito patrocinio può coprire le spese processuali e un patrocinatore d'ufficio se non disponete dei mezzi necessari e la causa non è priva di probabilità di successo (art. 29 cpv. 3 Cost.). Vedi la nostra guida dedicata."},
            ],
        },
        "en": {
            "slug": "how-much-does-a-lawyer-cost",
            "title": "How much does a lawyer cost in Switzerland?",
            "meta": "Hourly fees, retainers, success fees, legal expenses insurance: how lawyers' fees work in Switzerland.",
            "sections": [
                {"heading": "No single tariff: the factors that matter", "paragraphs": [
                    "There is no single federal hourly rate for Swiss lawyers. Fees depend on the canton, the lawyer's experience and specialisation, the complexity and urgency of the matter, and the amount in dispute. Several cantons have tariffs for court-awarded party costs, but billing between lawyer and client remains largely a matter of contract.",
                    "The golden rule: ask at the first meeting how the lawyer bills (hourly rate, flat fee or a combination), how often they report hours worked, and what — even roughly — the total foreseeable cost of your matter is likely to be.",
                ]},
                {"heading": "Retainer, invoices and disputes", "paragraphs": [
                    "It is customary for a Swiss lawyer to request a retainer — an advance on fees — before starting work. Services are then billed as the matter progresses, and you are entitled to a detailed statement of the work performed.",
                    "If you dispute an invoice, most cantons and bar associations offer a moderation or conciliation procedure through which an independent body reviews the bill.",
                ]},
                {"heading": "Success fees: what is allowed", "paragraphs": [
                    "Swiss law prohibits the pactum de quota litis — an agreement under which the lawyer is paid exclusively through a share of the outcome. However, case law allows, under certain conditions, a success premium on top of a base fee that at least covers the lawyer's costs (pactum de palmario).",
                    "Also consider legal expenses insurance: if taken out before the dispute arose, it may cover all or part of your lawyer's fees depending on the policy. Check your coverage before incurring costs.",
                ]},
            ],
            "faq": [
                {"q": "Can a Swiss lawyer work on a pure contingency basis?",
                 "a": "No. The pactum de quota litis (remuneration solely as a percentage of the outcome) is prohibited in Switzerland. A success premium on top of a reasonable base fee is possible under certain conditions."},
                {"q": "What is a retainer?",
                 "a": "An advance on fees requested before work begins, customary in Switzerland. It is credited against subsequent itemised invoices."},
                {"q": "What can I do about a disputed invoice?",
                 "a": "First request a detailed statement of services. Most cantons and bar associations then offer a moderation or conciliation procedure before an independent body."},
                {"q": "Who pays my lawyer if I win my case?",
                 "a": "In civil proceedings the losing party is generally ordered to pay costs, including a contribution to the winner's lawyer's fees set according to cantonal tariffs. That contribution does not always cover the fees actually billed."},
                {"q": "What if I cannot afford a lawyer?",
                 "a": "Legal aid can cover court costs and a court-appointed lawyer if you lack the necessary means and your case is not devoid of prospects of success (art. 29 para. 3 of the Federal Constitution). See our dedicated guide to legal aid."},
            ],
        },
    },
    "assistance-judiciaire": {
        "fr": {
            "slug": "assistance-judiciaire",
            "title": "L'assistance judiciaire en Suisse : qui y a droit et comment la demander",
            "meta": "Conditions, procédure et limites de l'assistance judiciaire gratuite en Suisse (art. 29 al. 3 Cst., art. 117 ss CPC, art. 132 CPP).",
            "sections": [
                {"heading": "Un droit constitutionnel", "paragraphs": [
                    "Toute personne qui ne dispose pas de ressources suffisantes a droit à l'assistance judiciaire gratuite, à moins que sa cause paraisse dépourvue de toute chance de succès. Ce droit est garanti par l'art. 29 al. 3 de la Constitution fédérale et concrétisé, en matière civile, par les art. 117 et suivants du Code de procédure civile (CPC).",
                    "L'assistance judiciaire comprend l'exonération d'avances et de frais judiciaires et, lorsque la défense des droits le requiert, la désignation d'un avocat d'office rémunéré par l'État.",
                ]},
                {"heading": "Les deux conditions : indigence et chances de succès", "paragraphs": [
                    "Première condition, l'indigence : vos revenus et votre fortune, après déduction du minimum vital élargi, ne vous permettent pas d'assumer les frais du procès sans entamer les moyens nécessaires à votre entretien et à celui de votre famille. L'examen est concret et tient compte de votre situation réelle.",
                    "Seconde condition : la cause ne doit pas être dépourvue de chances de succès. Il ne s'agit pas de garantir la victoire, mais d'écarter les procédures qu'une personne raisonnable, plaidant à ses propres frais, ne mènerait pas. En matière pénale, la défense d'office est régie par l'art. 132 du Code de procédure pénale (CPP).",
                ]},
                {"heading": "Comment déposer la demande — et ce qu'il faut savoir", "paragraphs": [
                    "La demande s'adresse au tribunal saisi de la cause (ou compétent pour la trancher), en règle générale par écrit, avec les justificatifs de votre situation financière : revenus, charges, fortune, dettes. Elle peut être déposée avant ou pendant la procédure.",
                    "Attention : l'assistance judiciaire n'est pas définitivement acquise. Si vous revenez à meilleure fortune, le canton peut vous demander le remboursement des prestations avancées (art. 123 CPC). Elle ne couvre par ailleurs pas, en principe, les dépens dus à la partie adverse si vous perdez le procès.",
                ]},
            ],
            "faq": [
                {"q": "L'assistance judiciaire couvre-t-elle tous les frais ?",
                 "a": "Elle couvre les frais judiciaires et, si nécessaire, un avocat d'office. Elle ne couvre en principe pas les dépens que vous pourriez devoir à la partie adverse en cas de perte du procès."},
                {"q": "Dois-je rembourser l'assistance judiciaire ?",
                 "a": "Oui, si vous revenez à meilleure fortune : le canton peut exiger le remboursement des prestations avancées (art. 123 CPC)."},
                {"q": "Puis-je choisir mon avocat d'office ?",
                 "a": "Vous pouvez proposer un avocat, et vos souhaits sont pris en compte dans la mesure du possible, mais la désignation appartient à l'autorité. L'avocat d'office est rémunéré par l'État selon un tarif souvent inférieur aux honoraires de marché."},
                {"q": "Où déposer la demande d'assistance judiciaire ?",
                 "a": "Auprès du tribunal saisi de votre cause, avec les justificatifs complets de votre situation financière. En matière pénale, la défense d'office est examinée par la direction de la procédure selon l'art. 132 CPP."},
            ],
        },
        "de": {
            "slug": "unentgeltliche-rechtspflege",
            "title": "Unentgeltliche Rechtspflege in der Schweiz: Wer hat Anspruch und wie stellt man das Gesuch?",
            "meta": "Voraussetzungen, Verfahren und Grenzen der unentgeltlichen Rechtspflege in der Schweiz (Art. 29 Abs. 3 BV, Art. 117 ff. ZPO, Art. 132 StPO).",
            "sections": [
                {"heading": "Ein verfassungsmässiges Recht", "paragraphs": [
                    "Wer nicht über die erforderlichen Mittel verfügt, hat Anspruch auf unentgeltliche Rechtspflege, sofern das Rechtsbegehren nicht aussichtslos erscheint. Dieses Recht garantiert Art. 29 Abs. 3 der Bundesverfassung; im Zivilverfahren konkretisieren es die Art. 117 ff. der Zivilprozessordnung (ZPO).",
                    "Die unentgeltliche Rechtspflege umfasst die Befreiung von Vorschüssen und Gerichtskosten sowie — wenn es zur Wahrung der Rechte notwendig ist — die Bestellung eines unentgeltlichen Rechtsbeistands, der vom Staat entschädigt wird.",
                ]},
                {"heading": "Die zwei Voraussetzungen: Mittellosigkeit und Erfolgsaussichten", "paragraphs": [
                    "Erste Voraussetzung ist die Mittellosigkeit: Einkommen und Vermögen erlauben es Ihnen — nach Abzug des erweiterten Existenzminimums — nicht, die Prozesskosten zu tragen, ohne die für Sie und Ihre Familie nötigen Mittel anzugreifen. Die Prüfung erfolgt konkret anhand Ihrer tatsächlichen Verhältnisse.",
                    "Zweite Voraussetzung: Das Begehren darf nicht aussichtslos sein. Verlangt wird kein sicherer Sieg; ausgeschlossen werden Verfahren, die eine vernünftige Partei auf eigene Kosten nicht führen würde. Im Strafverfahren richtet sich die amtliche Verteidigung nach Art. 132 der Strafprozessordnung (StPO).",
                ]},
                {"heading": "So stellen Sie das Gesuch — und das sollten Sie wissen", "paragraphs": [
                    "Das Gesuch ist beim mit der Sache befassten Gericht einzureichen, in der Regel schriftlich, mit Belegen zur finanziellen Situation: Einkommen, Auslagen, Vermögen, Schulden. Es kann vor oder während des Verfahrens gestellt werden.",
                    "Wichtig: Die unentgeltliche Rechtspflege ist nicht endgültig erworben. Gelangen Sie später zu besseren finanziellen Verhältnissen, kann der Kanton die Rückerstattung verlangen (Art. 123 ZPO). Sie deckt zudem grundsätzlich nicht die Parteientschädigung an die Gegenseite bei Prozessverlust.",
                ]},
            ],
            "faq": [
                {"q": "Deckt die unentgeltliche Rechtspflege alle Kosten?",
                 "a": "Sie deckt die Gerichtskosten und wenn nötig einen unentgeltlichen Rechtsbeistand. Die Parteientschädigung an die Gegenseite bei Prozessverlust ist grundsätzlich nicht gedeckt."},
                {"q": "Muss ich die Leistungen zurückzahlen?",
                 "a": "Ja, wenn Sie später in bessere finanzielle Verhältnisse gelangen: Der Kanton kann die Rückerstattung verlangen (Art. 123 ZPO)."},
                {"q": "Kann ich meinen amtlichen Anwalt wählen?",
                 "a": "Sie können eine Anwältin oder einen Anwalt vorschlagen; die Wünsche werden nach Möglichkeit berücksichtigt, die Bestellung obliegt aber der Behörde. Die Entschädigung durch den Staat liegt oft unter den Markthonoraren."},
                {"q": "Wo reiche ich das Gesuch ein?",
                 "a": "Beim Gericht, das mit Ihrer Sache befasst ist, mit vollständigen Belegen zur finanziellen Situation. Im Strafverfahren entscheidet die Verfahrensleitung über die amtliche Verteidigung nach Art. 132 StPO."},
            ],
        },
        "it": {
            "slug": "gratuito-patrocinio",
            "title": "Il gratuito patrocinio in Svizzera: chi ne ha diritto e come richiederlo",
            "meta": "Condizioni, procedura e limiti del gratuito patrocinio in Svizzera (art. 29 cpv. 3 Cost., art. 117 segg. CPC, art. 132 CPP).",
            "sections": [
                {"heading": "Un diritto costituzionale", "paragraphs": [
                    "Chi non dispone dei mezzi necessari ha diritto al gratuito patrocinio, a meno che la sua causa sembri priva di probabilità di successo. Questo diritto è garantito dall'art. 29 cpv. 3 della Costituzione federale e concretizzato, in materia civile, dagli art. 117 segg. del Codice di procedura civile (CPC).",
                    "Il gratuito patrocinio comprende l'esenzione dagli anticipi e dalle spese giudiziarie e, quando la tutela dei diritti lo richiede, la designazione di un patrocinatore d'ufficio retribuito dallo Stato.",
                ]},
                {"heading": "Le due condizioni: indigenza e probabilità di successo", "paragraphs": [
                    "Prima condizione, l'indigenza: reddito e patrimonio, dedotto il minimo vitale allargato, non permettono di sostenere le spese processuali senza intaccare i mezzi necessari al mantenimento proprio e della famiglia. L'esame è concreto e tiene conto della situazione reale.",
                    "Seconda condizione: la causa non deve essere priva di probabilità di successo. Non si esige la certezza della vittoria; si escludono le procedure che una persona ragionevole, a proprie spese, non intraprenderebbe. In materia penale, la difesa d'ufficio è retta dall'art. 132 del Codice di procedura penale (CPP).",
                ]},
                {"heading": "Come presentare la domanda — e cosa sapere", "paragraphs": [
                    "La domanda va presentata al tribunale investito della causa, di regola per scritto, con i giustificativi della situazione finanziaria: redditi, oneri, patrimonio, debiti. Può essere presentata prima o durante la procedura.",
                    "Attenzione: il gratuito patrocinio non è acquisito definitivamente. Se tornate a miglior fortuna, il cantone può chiedervi il rimborso delle prestazioni anticipate (art. 123 CPC). Di regola non copre inoltre le ripetibili dovute alla controparte in caso di soccombenza.",
                ]},
            ],
            "faq": [
                {"q": "Il gratuito patrocinio copre tutte le spese?",
                 "a": "Copre le spese giudiziarie e, se necessario, un patrocinatore d'ufficio. Di regola non copre le ripetibili dovute alla controparte in caso di perdita della causa."},
                {"q": "Devo rimborsare le prestazioni?",
                 "a": "Sì, se tornate a miglior fortuna: il cantone può esigere il rimborso delle prestazioni anticipate (art. 123 CPC)."},
                {"q": "Posso scegliere il mio patrocinatore d'ufficio?",
                 "a": "Potete proporre un avvocato e i vostri desideri sono considerati per quanto possibile, ma la designazione spetta all'autorità. La retribuzione statale è spesso inferiore agli onorari di mercato."},
                {"q": "Dove presento la domanda?",
                 "a": "Al tribunale investito della vostra causa, con i giustificativi completi della situazione finanziaria. In materia penale, la difesa d'ufficio è decisa da chi dirige il procedimento secondo l'art. 132 CPP."},
            ],
        },
        "en": {
            "slug": "legal-aid-switzerland",
            "title": "Legal aid in Switzerland: who qualifies and how to apply",
            "meta": "Conditions, procedure and limits of legal aid in Switzerland (art. 29 para. 3 Constitution, art. 117 ff. CPC, art. 132 CrimPC).",
            "sections": [
                {"heading": "A constitutional right", "paragraphs": [
                    "Any person who lacks the necessary means is entitled to free legal aid, unless their case appears devoid of any prospect of success. This right is guaranteed by art. 29 para. 3 of the Federal Constitution and implemented, in civil matters, by art. 117 ff. of the Civil Procedure Code (CPC).",
                    "Legal aid covers exemption from court advances and costs and, where necessary to protect the person's rights, the appointment of a court-appointed lawyer paid by the State.",
                ]},
                {"heading": "The two conditions: lack of means and prospects of success", "paragraphs": [
                    "First condition — lack of means: your income and assets, after deduction of an extended subsistence minimum, do not allow you to bear the costs of the proceedings without touching the resources needed to support yourself and your family. The assessment is concrete and based on your actual situation.",
                    "Second condition: the case must not be devoid of prospects of success. This does not require certain victory; it excludes proceedings that a reasonable person paying their own way would not pursue. In criminal matters, court-appointed defence is governed by art. 132 of the Criminal Procedure Code (CrimPC).",
                ]},
                {"heading": "How to apply — and what to keep in mind", "paragraphs": [
                    "The application is filed with the court dealing with the case, generally in writing, with full supporting evidence of your financial situation: income, expenses, assets, debts. It can be filed before or during proceedings.",
                    "Note that legal aid is not definitively acquired: if your financial situation later improves, the canton may claim reimbursement of the amounts advanced (art. 123 CPC). It also does not, as a rule, cover the party costs you may owe the opposing side if you lose.",
                ]},
            ],
            "faq": [
                {"q": "Does legal aid cover all costs?",
                 "a": "It covers court costs and, if necessary, a court-appointed lawyer. It does not, as a rule, cover the party costs you may owe the opposing party if you lose the case."},
                {"q": "Do I have to pay legal aid back?",
                 "a": "Yes, if your financial situation improves: the canton may claim reimbursement of the amounts advanced (art. 123 CPC)."},
                {"q": "Can I choose my court-appointed lawyer?",
                 "a": "You may propose a lawyer, and your wishes are taken into account where possible, but the appointment is made by the authority. State compensation is often below market rates."},
                {"q": "Where do I file the application?",
                 "a": "With the court dealing with your case, with complete evidence of your financial situation. In criminal matters, court-appointed defence is decided by the director of proceedings under art. 132 CrimPC."},
            ],
        },
    },
    "avocat-specialiste-fsa": {
        "fr": {
            "slug": "avocat-specialiste-fsa",
            "title": "Avocat spécialiste FSA : que garantit ce titre ?",
            "meta": "Ce que signifie le titre d'avocat spécialiste FSA décerné par la Fédération Suisse des Avocats, et comment l'utiliser dans votre recherche.",
            "sections": [
                {"heading": "Un titre officiel de spécialisation", "paragraphs": [
                    "Le titre d'« avocat spécialiste FSA » est décerné par la Fédération Suisse des Avocats (FSA), l'organisation faîtière de la profession. Il atteste qu'un avocat possède, dans un domaine déterminé du droit, une expérience pratique substantielle et une formation approfondie, validées selon les exigences de la FSA.",
                    "Les domaines de spécialisation couverts incluent notamment le droit du travail, le droit de la famille, le droit pénal, le droit de la construction et de l'immobilier, le droit des successions, le droit de la responsabilité civile et des assurances, ou encore le droit fiscal.",
                ]},
                {"heading": "Ce que le titre garantit — et ce qu'il ne dit pas", "paragraphs": [
                    "Le titre garantit un socle vérifié : un nombre significatif de dossiers traités dans le domaine, une formation spécialisée et un maintien à jour des connaissances. C'est un repère utile, en particulier pour des affaires complexes où la spécialisation fait la différence.",
                    "À l'inverse, l'absence du titre ne signifie pas qu'un avocat n'est pas spécialisé : de nombreux praticiens expérimentés concentrent de fait leur activité sur un ou deux domaines sans avoir entrepris la certification. Le titre est un signal positif fiable, pas un critère d'exclusion.",
                ]},
            ],
            "faq": [
                {"q": "Qui décerne le titre d'avocat spécialiste FSA ?",
                 "a": "La Fédération Suisse des Avocats (FSA), organisation faîtière des avocats suisses, selon ses propres exigences de pratique et de formation dans chaque domaine de spécialisation."},
                {"q": "Un avocat sans titre FSA peut-il être compétent dans un domaine ?",
                 "a": "Oui. Beaucoup d'avocats expérimentés concentrent leur pratique sur quelques domaines sans avoir entrepris la certification. Le titre est un signal positif fiable, mais son absence n'est pas un critère d'exclusion."},
                {"q": "Comment savoir si un avocat est spécialiste FSA ?",
                 "a": "Le titre figure généralement sur le site du cabinet et dans les communications de l'avocat. En cas de doute, la FSA et les ordres cantonaux peuvent confirmer la titularité du titre."},
            ],
        },
        "de": {
            "slug": "fachanwalt-sav",
            "title": "Fachanwalt SAV: Was garantiert dieser Titel?",
            "meta": "Was der vom Schweizerischen Anwaltsverband verliehene Titel «Fachanwalt SAV» bedeutet und wie Sie ihn bei der Anwaltssuche nutzen.",
            "sections": [
                {"heading": "Ein offizieller Spezialisierungstitel", "paragraphs": [
                    "Den Titel «Fachanwältin/Fachanwalt SAV» verleiht der Schweizerische Anwaltsverband (SAV), die Dachorganisation des Berufsstands. Er bescheinigt in einem bestimmten Rechtsgebiet substanzielle praktische Erfahrung und eine vertiefte Weiterbildung, geprüft nach den Anforderungen des SAV.",
                    "Zu den abgedeckten Fachgebieten gehören namentlich Arbeitsrecht, Familienrecht, Strafrecht, Bau- und Immobilienrecht, Erbrecht, Haftpflicht- und Versicherungsrecht sowie Steuerrecht.",
                ]},
                {"heading": "Was der Titel garantiert — und was nicht", "paragraphs": [
                    "Der Titel garantiert einen geprüften Sockel: eine erhebliche Zahl bearbeiteter Fälle im Gebiet, eine spezialisierte Ausbildung und aktuell gehaltenes Wissen. Er ist ein nützlicher Anhaltspunkt, besonders bei komplexen Fällen, in denen Spezialisierung den Unterschied macht.",
                    "Umgekehrt bedeutet das Fehlen des Titels nicht, dass jemand nicht spezialisiert wäre: Viele erfahrene Praktikerinnen und Praktiker konzentrieren ihre Tätigkeit faktisch auf ein bis zwei Gebiete, ohne die Zertifizierung absolviert zu haben. Der Titel ist ein verlässliches positives Signal, kein Ausschlusskriterium.",
                ]},
            ],
            "faq": [
                {"q": "Wer verleiht den Titel Fachanwalt SAV?",
                 "a": "Der Schweizerische Anwaltsverband (SAV), die Dachorganisation der schweizerischen Anwältinnen und Anwälte, nach eigenen Anforderungen an Praxis und Ausbildung im jeweiligen Fachgebiet."},
                {"q": "Kann ein Anwalt ohne SAV-Titel in einem Gebiet kompetent sein?",
                 "a": "Ja. Viele erfahrene Anwältinnen und Anwälte konzentrieren ihre Praxis auf wenige Gebiete, ohne die Zertifizierung absolviert zu haben. Der Titel ist ein verlässliches positives Signal, sein Fehlen aber kein Ausschlusskriterium."},
                {"q": "Wie erkenne ich, ob jemand Fachanwalt SAV ist?",
                 "a": "Der Titel wird üblicherweise auf der Kanzlei-Website und in der Kommunikation geführt. Im Zweifel können der SAV und die kantonalen Anwaltsverbände die Titelträgerschaft bestätigen."},
            ],
        },
        "it": {
            "slug": "avvocato-specialista-fsa",
            "title": "Avvocato specialista FSA: cosa garantisce questo titolo?",
            "meta": "Cosa significa il titolo di avvocato specialista FSA conferito dalla Federazione Svizzera degli Avvocati e come usarlo nella ricerca.",
            "sections": [
                {"heading": "Un titolo ufficiale di specializzazione", "paragraphs": [
                    "Il titolo di «avvocato specialista FSA» è conferito dalla Federazione Svizzera degli Avvocati (FSA), l'organizzazione mantello della professione. Attesta, in un ambito determinato del diritto, un'esperienza pratica sostanziale e una formazione approfondita, verificate secondo i requisiti della FSA.",
                    "Gli ambiti di specializzazione coperti comprendono in particolare il diritto del lavoro, il diritto di famiglia, il diritto penale, il diritto della costruzione e immobiliare, il diritto successorio, la responsabilità civile e le assicurazioni, nonché il diritto fiscale.",
                ]},
                {"heading": "Cosa garantisce il titolo — e cosa non dice", "paragraphs": [
                    "Il titolo garantisce una base verificata: un numero significativo di casi trattati nell'ambito, una formazione specializzata e conoscenze aggiornate. È un riferimento utile, soprattutto nei casi complessi in cui la specializzazione fa la differenza.",
                    "Al contrario, l'assenza del titolo non significa che un avvocato non sia specializzato: molti professionisti esperti concentrano di fatto la loro attività su uno o due ambiti senza aver intrapreso la certificazione. Il titolo è un segnale positivo affidabile, non un criterio di esclusione.",
                ]},
            ],
            "faq": [
                {"q": "Chi conferisce il titolo di avvocato specialista FSA?",
                 "a": "La Federazione Svizzera degli Avvocati (FSA), organizzazione mantello degli avvocati svizzeri, secondo i propri requisiti di pratica e formazione in ciascun ambito di specializzazione."},
                {"q": "Un avvocato senza titolo FSA può essere competente in un ambito?",
                 "a": "Sì. Molti avvocati esperti concentrano la loro pratica su pochi ambiti senza aver intrapreso la certificazione. Il titolo è un segnale positivo affidabile, ma la sua assenza non è un criterio di esclusione."},
                {"q": "Come so se un avvocato è specialista FSA?",
                 "a": "Il titolo figura di regola sul sito dello studio e nelle comunicazioni dell'avvocato. In caso di dubbio, la FSA e gli ordini cantonali possono confermarne la titolarità."},
            ],
        },
        "en": {
            "slug": "certified-specialist-lawyer-fsa",
            "title": "Certified Specialist SBA: what does the title guarantee?",
            "meta": "What the Certified Specialist title awarded by the Swiss Bar Association means, and how to use it when searching for a lawyer.",
            "sections": [
                {"heading": "An official specialisation title", "paragraphs": [
                    "The title of \"Certified Specialist SBA\" (avocat spécialiste FSA / Fachanwalt SAV) is awarded by the Swiss Bar Association (SBA), the umbrella organisation of the profession. It certifies that a lawyer has substantial practical experience and advanced training in a defined field of law, validated according to the SBA's requirements.",
                    "Covered specialisation fields notably include employment law, family law, criminal law, construction and real estate law, inheritance law, liability and insurance law, and tax law.",
                ]},
                {"heading": "What the title guarantees — and what it does not say", "paragraphs": [
                    "The title guarantees a verified foundation: a significant number of cases handled in the field, specialised training and up-to-date knowledge. It is a useful marker, especially for complex matters where specialisation makes the difference.",
                    "Conversely, the absence of the title does not mean a lawyer is not specialised: many experienced practitioners concentrate their work on one or two fields without having pursued certification. The title is a reliable positive signal, not an exclusion criterion.",
                ]},
            ],
            "faq": [
                {"q": "Who awards the Certified Specialist SBA title?",
                 "a": "The Swiss Bar Association (SBA), the umbrella organisation of Swiss lawyers, according to its own practice and training requirements in each specialisation field."},
                {"q": "Can a lawyer without the SBA title be competent in a field?",
                 "a": "Yes. Many experienced lawyers concentrate their practice on a few fields without pursuing certification. The title is a reliable positive signal, but its absence is not an exclusion criterion."},
                {"q": "How do I know whether a lawyer is a Certified Specialist SBA?",
                 "a": "The title usually appears on the firm's website and in the lawyer's communications. In case of doubt, the SBA and the cantonal bar associations can confirm it."},
            ],
        },
    },
    "premiere-consultation": {
        "fr": {
            "slug": "preparer-premiere-consultation",
            "title": "Préparer sa première consultation chez un avocat",
            "meta": "Documents à réunir, questions à poser, points à clarifier : comment tirer le meilleur parti d'un premier rendez-vous chez un avocat en Suisse.",
            "sections": [
                {"heading": "Réunir les documents et poser la chronologie", "paragraphs": [
                    "Avant le rendez-vous, rassemblez tous les documents liés à votre affaire : contrats, courriers et e-mails, décisions reçues, procès-verbaux, certificats, photos — même les pièces qui vous semblent défavorables. Un avocat conseille d'autant mieux qu'il a une vision complète, et le secret professionnel (art. 321 du Code pénal, art. 13 LLCA) protège tout ce que vous lui confiez.",
                    "Préparez aussi une chronologie écrite des faits, d'une page si possible : dates, événements, personnes impliquées. C'est le document qui fait gagner le plus de temps — donc d'honoraires — lors du premier entretien.",
                ]},
                {"heading": "Les questions à poser d'emblée", "paragraphs": [
                    "Clarifiez trois points dès la première consultation : l'évaluation de votre situation (quels sont mes droits, mes risques, mes chances ?), la stratégie envisagée (négociation, procédure, médiation ?) et le coût (mode de facturation, provision demandée, estimation du budget total).",
                    "Demandez aussi s'il existe des délais à respecter : en droit suisse, de nombreux droits se périment ou se prescrivent — délais pour contester un congé, agir en justice après une résiliation, faire opposition à une ordonnance pénale, etc. C'est souvent l'information la plus urgente d'un premier entretien.",
                ]},
                {"heading": "Après l'entretien", "paragraphs": [
                    "Un avocat sérieux vous confirme généralement par écrit le mandat, son étendue et les conditions de facturation. Lisez ce document avant de le signer, et n'hésitez pas à demander des explications sur les points obscurs. Vous restez libre de ne pas donner suite ou de consulter un autre avocat pour un second avis.",
                ]},
            ],
            "faq": [
                {"q": "La première consultation est-elle payante ?",
                 "a": "Cela dépend des cabinets : certains offrent un premier entretien bref, d'autres le facturent au tarif horaire ou à un forfait annoncé. Demandez-le explicitement lors de la prise de rendez-vous — un cabinet sérieux répond clairement."},
                {"q": "Que dois-je apporter au premier rendez-vous ?",
                 "a": "Tous les documents liés à l'affaire (contrats, courriers, décisions, preuves), une pièce d'identité, et si possible une chronologie écrite des faits. Apportez aussi les pièces qui vous semblent défavorables : l'avocat doit tout connaître pour bien vous conseiller."},
                {"q": "Ce que je dis à un avocat est-il confidentiel ?",
                 "a": "Oui. Le secret professionnel de l'avocat est protégé par l'art. 321 du Code pénal et l'art. 13 LLCA. Il couvre tout ce que vous confiez à l'avocat dans le cadre de son activité professionnelle, même si vous ne lui confiez finalement pas le mandat."},
                {"q": "Puis-je changer d'avocat en cours de procédure ?",
                 "a": "Oui, à tout moment. Vous devrez régler les honoraires dus pour le travail déjà effectué, et le nouvel avocat reprendra le dossier. Le premier avocat doit restituer les pièces du dossier."},
            ],
        },
        "de": {
            "slug": "erstberatung-vorbereiten",
            "title": "Die Erstberatung beim Anwalt richtig vorbereiten",
            "meta": "Unterlagen, Fragen, Kostenpunkte: So holen Sie in der Schweiz das Beste aus dem ersten Termin bei einer Anwältin oder einem Anwalt heraus.",
            "sections": [
                {"heading": "Unterlagen sammeln und Chronologie erstellen", "paragraphs": [
                    "Sammeln Sie vor dem Termin alle Unterlagen zu Ihrem Fall: Verträge, Briefe und E-Mails, erhaltene Entscheide, Protokolle, Zeugnisse, Fotos — auch Dokumente, die Ihnen ungünstig erscheinen. Je vollständiger das Bild, desto besser die Beratung; das Berufsgeheimnis (Art. 321 StGB, Art. 13 BGFA) schützt alles, was Sie anvertrauen.",
                    "Erstellen Sie zudem eine schriftliche Chronologie der Ereignisse, wenn möglich auf einer Seite: Daten, Vorgänge, beteiligte Personen. Kein anderes Dokument spart im Erstgespräch mehr Zeit — und damit Honorar.",
                ]},
                {"heading": "Diese Fragen gehören ins Erstgespräch", "paragraphs": [
                    "Klären Sie drei Punkte von Anfang an: die Einschätzung Ihrer Lage (Rechte, Risiken, Erfolgsaussichten), die Strategie (Verhandlung, Prozess, Mediation?) und die Kosten (Abrechnungsart, Kostenvorschuss, geschätztes Gesamtbudget).",
                    "Fragen Sie auch nach laufenden Fristen: Im schweizerischen Recht verwirken oder verjähren viele Ansprüche — Fristen zur Anfechtung einer Kündigung, für Klagen, für die Einsprache gegen einen Strafbefehl usw. Das ist oft die dringendste Information des ersten Gesprächs.",
                ]},
                {"heading": "Nach dem Gespräch", "paragraphs": [
                    "Eine seriöse Anwältin bestätigt Mandat, Umfang und Abrechnungskonditionen in der Regel schriftlich. Lesen Sie dieses Dokument vor der Unterschrift und fragen Sie bei Unklarheiten nach. Es steht Ihnen frei, nicht weiterzumachen oder für eine Zweitmeinung eine andere Kanzlei zu konsultieren.",
                ]},
            ],
            "faq": [
                {"q": "Ist die Erstberatung kostenpflichtig?",
                 "a": "Das hängt von der Kanzlei ab: Manche bieten ein kurzes Erstgespräch unentgeltlich an, andere verrechnen es zum Stundenansatz oder zu einer angekündigten Pauschale. Fragen Sie bei der Terminvereinbarung ausdrücklich danach."},
                {"q": "Was soll ich zum ersten Termin mitbringen?",
                 "a": "Alle Unterlagen zum Fall (Verträge, Korrespondenz, Entscheide, Beweismittel), einen Ausweis und wenn möglich eine schriftliche Chronologie. Bringen Sie auch ungünstig erscheinende Dokumente mit: Nur wer alles kennt, berät richtig."},
                {"q": "Ist das Gespräch mit einem Anwalt vertraulich?",
                 "a": "Ja. Das Anwaltsgeheimnis ist durch Art. 321 StGB und Art. 13 BGFA geschützt. Es umfasst alles, was Sie der Anwältin im Rahmen ihrer Berufstätigkeit anvertrauen — auch wenn kein Mandat zustande kommt."},
                {"q": "Kann ich den Anwalt während des Verfahrens wechseln?",
                 "a": "Ja, jederzeit. Sie schulden das Honorar für die bereits geleistete Arbeit; die neue Anwältin übernimmt das Dossier, und die bisherige muss die Akten herausgeben."},
            ],
        },
        "it": {
            "slug": "preparare-prima-consulenza",
            "title": "Preparare la prima consulenza da un avvocato",
            "meta": "Documenti da riunire, domande da porre, punti da chiarire: come sfruttare al meglio il primo appuntamento da un avvocato in Svizzera.",
            "sections": [
                {"heading": "Riunire i documenti e stendere la cronologia", "paragraphs": [
                    "Prima dell'appuntamento, raccogliete tutti i documenti legati al caso: contratti, lettere ed e-mail, decisioni ricevute, verbali, certificati, foto — anche i documenti che vi sembrano sfavorevoli. L'avvocato consiglia tanto meglio quanto più completo è il quadro, e il segreto professionale (art. 321 del Codice penale, art. 13 LLCA) protegge tutto ciò che gli confidate.",
                    "Preparate anche una cronologia scritta dei fatti, se possibile di una pagina: date, eventi, persone coinvolte. È il documento che fa risparmiare più tempo — e quindi onorari — nel primo colloquio.",
                ]},
                {"heading": "Le domande da porre subito", "paragraphs": [
                    "Chiarite tre punti fin dalla prima consulenza: la valutazione della situazione (diritti, rischi, probabilità di successo), la strategia prevista (trattativa, procedura, mediazione?) e i costi (modalità di fatturazione, anticipo richiesto, stima del budget totale).",
                    "Chiedete anche se vi sono termini da rispettare: nel diritto svizzero molti diritti si estinguono o si prescrivono — termini per contestare una disdetta, per agire in giudizio, per fare opposizione a un decreto d'accusa, ecc. È spesso l'informazione più urgente del primo colloquio.",
                ]},
                {"heading": "Dopo il colloquio", "paragraphs": [
                    "Un avvocato serio conferma di regola per scritto il mandato, la sua estensione e le condizioni di fatturazione. Leggete il documento prima di firmarlo e chiedete spiegazioni sui punti poco chiari. Restate liberi di non dare seguito o di consultare un altro avvocato per un secondo parere.",
                ]},
            ],
            "faq": [
                {"q": "La prima consulenza è a pagamento?",
                 "a": "Dipende dallo studio: alcuni offrono un breve primo colloquio, altri lo fatturano a tariffa oraria o a forfait annunciato. Chiedetelo esplicitamente al momento di fissare l'appuntamento."},
                {"q": "Cosa devo portare al primo appuntamento?",
                 "a": "Tutti i documenti del caso (contratti, corrispondenza, decisioni, prove), un documento d'identità e se possibile una cronologia scritta dei fatti. Portate anche i documenti che vi sembrano sfavorevoli: l'avvocato deve conoscere tutto per consigliarvi bene."},
                {"q": "Ciò che dico a un avvocato è confidenziale?",
                 "a": "Sì. Il segreto professionale dell'avvocato è protetto dall'art. 321 del Codice penale e dall'art. 13 LLCA. Copre tutto ciò che confidate all'avvocato nell'ambito della sua attività professionale, anche se poi non gli affidate il mandato."},
                {"q": "Posso cambiare avvocato durante la procedura?",
                 "a": "Sì, in ogni momento. Dovrete saldare gli onorari per il lavoro già svolto; il nuovo avvocato riprenderà l'incarto e il precedente deve restituire gli atti."},
            ],
        },
        "en": {
            "slug": "prepare-first-consultation",
            "title": "How to prepare for your first consultation with a lawyer",
            "meta": "Documents to gather, questions to ask, points to clarify: how to get the most out of a first meeting with a lawyer in Switzerland.",
            "sections": [
                {"heading": "Gather documents and write a timeline", "paragraphs": [
                    "Before the meeting, collect every document related to your matter: contracts, letters and e-mails, decisions received, minutes, certificates, photos — including documents that seem unfavourable to you. A lawyer advises best with the full picture, and professional secrecy (art. 321 of the Criminal Code, art. 13 BGFA/LLCA) protects everything you disclose.",
                    "Also prepare a written timeline of events, ideally one page: dates, facts, people involved. No other document saves more time — and therefore fees — in a first meeting.",
                ]},
                {"heading": "Questions to ask upfront", "paragraphs": [
                    "Clarify three things at the first consultation: the assessment of your situation (rights, risks, prospects), the proposed strategy (negotiation, litigation, mediation?) and the cost (billing method, retainer requested, estimated total budget).",
                    "Also ask about deadlines: under Swiss law many rights lapse or become time-barred — deadlines to challenge a termination, to file suit, to oppose a summary penalty order, and so on. This is often the most urgent information of a first meeting.",
                ]},
                {"heading": "After the meeting", "paragraphs": [
                    "A serious lawyer will generally confirm the mandate, its scope and billing terms in writing. Read that document before signing and ask about anything unclear. You remain free not to proceed, or to consult another lawyer for a second opinion.",
                ]},
            ],
            "faq": [
                {"q": "Is the first consultation free?",
                 "a": "It depends on the firm: some offer a brief first meeting, others bill it at their hourly rate or an announced flat fee. Ask explicitly when booking the appointment — a serious firm will answer clearly."},
                {"q": "What should I bring to the first meeting?",
                 "a": "All documents related to the matter (contracts, correspondence, decisions, evidence), an identity document and, if possible, a written timeline of events. Bring unfavourable documents too: the lawyer needs the full picture to advise you properly."},
                {"q": "Is what I tell a lawyer confidential?",
                 "a": "Yes. A lawyer's professional secrecy is protected by art. 321 of the Criminal Code and art. 13 of the Federal Act on the Free Movement of Lawyers. It covers everything you disclose in the course of the lawyer's professional activity, even if you end up not instructing them."},
                {"q": "Can I change lawyers during proceedings?",
                 "a": "Yes, at any time. You will owe fees for work already done; the new lawyer takes over the file and the previous one must hand over the case documents."},
            ],
        },
    },
}
