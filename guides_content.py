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
                    "Un avocat inscrit dans un canton peut plaider dans toute la Suisse. L'inscription au registre est donc le premier critère à vérifier. C'est précisément la donnée de base que Legatis référence, canton par canton, à partir des registres officiels.",
                ]},
                {"heading": "Le domaine de compétence avant tout", "paragraphs": [
                    "Le droit suisse est vaste : un excellent avocat en droit des sociétés n'est pas nécessairement le bon choix pour un divorce. Cherchez un avocat qui traite régulièrement des affaires comparables à la vôtre : droit du travail, droit du bail, droit pénal, droit de la famille, etc.",
                    "Certains avocats portent le titre d'« avocat spécialiste FSA », décerné par la Fédération Suisse des Avocats dans des domaines déterminés après une formation approfondie et une pratique attestée. Ce titre est un signal fiable de spécialisation, mais son absence ne signifie pas incompétence : beaucoup d'excellents praticiens n'ont simplement pas entrepris cette certification.",
                ]},
                {"heading": "Langue, proximité et relation de confiance", "paragraphs": [
                    "La procédure se déroule dans la langue officielle du canton où siège le tribunal. Un avocat qui pratique cette langue (et qui peut vous expliquer le dossier dans la vôtre) est un atout concret. La proximité géographique compte aussi : un avocat local connaît les tribunaux, les usages et les délais du canton.",
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
                    "Wer in einem Kanton eingetragen ist, darf in der ganzen Schweiz vor Gericht auftreten. Der Registereintrag ist somit das erste Kriterium. Genau diese Grundlage erfasst Legatis Kanton für Kanton aus den offiziellen Registern.",
                ]},
                {"heading": "Das Fachgebiet ist entscheidend", "paragraphs": [
                    "Das schweizerische Recht ist breit: Eine hervorragende Gesellschaftsrechtlerin ist nicht zwingend die richtige Wahl für eine Scheidung. Suchen Sie jemanden, der regelmässig Fälle wie Ihren bearbeitet: Arbeitsrecht, Mietrecht, Strafrecht, Familienrecht usw.",
                    "Einige tragen den Titel «Fachanwältin/Fachanwalt SAV», den der Schweizerische Anwaltsverband nach vertiefter Weiterbildung und nachgewiesener Praxis in bestimmten Rechtsgebieten verleiht. Der Titel ist ein verlässliches Spezialisierungssignal. Sein Fehlen bedeutet aber keine Inkompetenz.",
                ]},
                {"heading": "Sprache, Nähe und Vertrauen", "paragraphs": [
                    "Das Verfahren wird in der Amtssprache des Gerichtskantons geführt. Eine Anwältin, die diese Sprache beherrscht und Ihnen den Fall in Ihrer Sprache erklären kann, ist ein konkreter Vorteil. Auch die örtliche Nähe zählt: Wer lokal praktiziert, kennt Gerichte, Gepflogenheiten und Fristen des Kantons.",
                    "Entscheidend ist schliesslich das Vertrauensverhältnis. Ein Erstgespräch zeigt, ob die Anwältin zuhört, Ihre Rechtslage und Erfolgsaussichten klar erklärt und die Abrechnung transparent darlegt. Fragen Sie das ruhig direkt. Seriöse Anwältinnen und Anwälte antworten gern.",
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
                    "Un avvocato iscritto in un cantone può patrocinare in tutta la Svizzera. L'iscrizione all'albo è dunque il primo criterio da verificare, ed è esattamente il dato di base che Legatis censisce, cantone per cantone, dagli albi ufficiali.",
                ]},
                {"heading": "Prima di tutto l'ambito di competenza", "paragraphs": [
                    "Il diritto svizzero è vasto: un eccellente avvocato societario non è necessariamente la scelta giusta per un divorzio. Cercate chi tratta regolarmente casi simili al vostro: diritto del lavoro, diritto di locazione, diritto penale, diritto di famiglia, ecc.",
                    "Alcuni portano il titolo di «avvocato specialista FSA», conferito dalla Federazione Svizzera degli Avvocati in ambiti determinati dopo una formazione approfondita e una pratica comprovata. È un segnale affidabile di specializzazione, ma la sua assenza non significa incompetenza.",
                ]},
                {"heading": "Lingua, vicinanza e fiducia", "paragraphs": [
                    "La procedura si svolge nella lingua ufficiale del cantone del tribunale. Un avvocato che padroneggia quella lingua (e può spiegarvi il caso nella vostra) è un vantaggio concreto. Conta anche la vicinanza: chi esercita localmente conosce tribunali, prassi e termini del cantone.",
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
                    "A lawyer registered in one canton may appear before courts anywhere in Switzerland. Registry status is therefore the first thing to verify, and it is precisely the base data Legatis lists, canton by canton, from the official registers.",
                ]},
                {"heading": "Practice area comes first", "paragraphs": [
                    "Swiss law is broad: an excellent corporate lawyer is not necessarily the right choice for a divorce. Look for someone who regularly handles cases like yours: employment law, tenancy law, criminal law, family law, and so on.",
                    "Some lawyers hold the title of \"Certified Specialist SBA\" (avocat spécialiste FSA / Fachanwalt SAV), awarded by the Swiss Bar Association in defined fields after advanced training and proven practice. The title is a reliable signal of specialisation, though its absence does not imply incompetence.",
                ]},
                {"heading": "Language, proximity and trust", "paragraphs": [
                    "Proceedings are conducted in the official language of the canton where the court sits. A lawyer who works in that language (and can explain your case in yours) is a concrete advantage. Local proximity also matters: a local practitioner knows the courts, customs and deadlines of the canton.",
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
                    "La règle d'or : demander dès le premier entretien comment l'avocat facture (taux horaire, forfait, ou combinaison), à quelle fréquence il rend compte des heures effectuées, et à combien il estime (même grossièrement) le coût total prévisible de votre affaire.",
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
                    "Die goldene Regel: Fragen Sie schon im Erstgespräch, wie abgerechnet wird (Stundenansatz, Pauschale oder Kombination), wie oft über die geleisteten Stunden Rechenschaft abgelegt wird und wie hoch die Gesamtkosten voraussichtlich (auch grob) ausfallen dürften.",
                ]},
                {"heading": "Kostenvorschuss, Honorarnote und Beanstandung", "paragraphs": [
                    "Üblich ist ein Kostenvorschuss vor Arbeitsbeginn. Die Leistungen werden danach laufend abgerechnet. Sie haben Anspruch auf eine detaillierte Aufstellung der erbrachten Leistungen.",
                    "Bei Streit über eine Honorarnote bieten die meisten Kantone und Anwaltsverbände ein Moderations- oder Schlichtungsverfahren an, in dem eine unabhängige Stelle die Rechnung prüft.",
                ]},
                {"heading": "Erfolgshonorar: was zulässig ist", "paragraphs": [
                    "Das schweizerische Recht verbietet das pactum de quota litis: die Vergütung ausschliesslich durch eine Beteiligung am Prozessergebnis. Zulässig ist unter bestimmten Voraussetzungen hingegen eine Erfolgsprämie zusätzlich zu einem Grundhonorar, das mindestens die Kosten des Anwalts deckt (pactum de palmario).",
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
                    "La regola d'oro: chiedere fin dal primo colloquio come l'avvocato fattura (tariffa oraria, forfait o combinazione), con quale frequenza rende conto delle ore svolte e a quanto stima (anche approssimativamente) il costo totale prevedibile.",
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
                    "The golden rule: ask at the first meeting how the lawyer bills (hourly rate, flat fee or a combination), how often they report hours worked, and what (even roughly) the total foreseeable cost of your matter is likely to be.",
                ]},
                {"heading": "Retainer, invoices and disputes", "paragraphs": [
                    "It is customary for a Swiss lawyer to request a retainer (an advance on fees) before starting work. Services are then billed as the matter progresses, and you are entitled to a detailed statement of the work performed.",
                    "If you dispute an invoice, most cantons and bar associations offer a moderation or conciliation procedure through which an independent body reviews the bill.",
                ]},
                {"heading": "Success fees: what is allowed", "paragraphs": [
                    "Swiss law prohibits the pactum de quota litis: an agreement under which the lawyer is paid exclusively through a share of the outcome. However, case law allows, under certain conditions, a success premium on top of a base fee that at least covers the lawyer's costs (pactum de palmario).",
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
                {"heading": "Comment déposer la demande, et ce qu'il faut savoir", "paragraphs": [
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
                    "Die unentgeltliche Rechtspflege umfasst die Befreiung von Vorschüssen und Gerichtskosten sowie (wenn es zur Wahrung der Rechte notwendig ist) die Bestellung eines unentgeltlichen Rechtsbeistands, der vom Staat entschädigt wird.",
                ]},
                {"heading": "Die zwei Voraussetzungen: Mittellosigkeit und Erfolgsaussichten", "paragraphs": [
                    "Erste Voraussetzung ist die Mittellosigkeit: Einkommen und Vermögen erlauben es Ihnen (nach Abzug des erweiterten Existenzminimums) nicht, die Prozesskosten zu tragen, ohne die für Sie und Ihre Familie nötigen Mittel anzugreifen. Die Prüfung erfolgt konkret anhand Ihrer tatsächlichen Verhältnisse.",
                    "Zweite Voraussetzung: Das Begehren darf nicht aussichtslos sein. Verlangt wird kein sicherer Sieg; ausgeschlossen werden Verfahren, die eine vernünftige Partei auf eigene Kosten nicht führen würde. Im Strafverfahren richtet sich die amtliche Verteidigung nach Art. 132 der Strafprozessordnung (StPO).",
                ]},
                {"heading": "So stellen Sie das Gesuch, und das sollten Sie wissen", "paragraphs": [
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
                {"heading": "Come presentare la domanda, e cosa sapere", "paragraphs": [
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
                    "First condition, lack of means: your income and assets, after deduction of an extended subsistence minimum, do not allow you to bear the costs of the proceedings without touching the resources needed to support yourself and your family. The assessment is concrete and based on your actual situation.",
                    "Second condition: the case must not be devoid of prospects of success. This does not require certain victory; it excludes proceedings that a reasonable person paying their own way would not pursue. In criminal matters, court-appointed defence is governed by art. 132 of the Criminal Procedure Code (CrimPC).",
                ]},
                {"heading": "How to apply, and what to keep in mind", "paragraphs": [
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
                {"heading": "Ce que le titre garantit, et ce qu'il ne dit pas", "paragraphs": [
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
                {"heading": "Was der Titel garantiert, und was nicht", "paragraphs": [
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
                {"heading": "Cosa garantisce il titolo, e cosa non dice", "paragraphs": [
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
                {"heading": "What the title guarantees, and what it does not say", "paragraphs": [
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
                    "Avant le rendez-vous, rassemblez tous les documents liés à votre affaire : contrats, courriers et e-mails, décisions reçues, procès-verbaux, certificats, photos, même les pièces qui vous semblent défavorables. Un avocat conseille d'autant mieux qu'il a une vision complète, et le secret professionnel (art. 321 du Code pénal, art. 13 LLCA) protège tout ce que vous lui confiez.",
                    "Préparez aussi une chronologie écrite des faits, d'une page si possible : dates, événements, personnes impliquées. C'est le document qui fait gagner le plus de temps (donc d'honoraires) lors du premier entretien.",
                ]},
                {"heading": "Les questions à poser d'emblée", "paragraphs": [
                    "Clarifiez trois points dès la première consultation : l'évaluation de votre situation (quels sont mes droits, mes risques, mes chances ?), la stratégie envisagée (négociation, procédure, médiation ?) et le coût (mode de facturation, provision demandée, estimation du budget total).",
                    "Demandez aussi s'il existe des délais à respecter : en droit suisse, de nombreux droits se périment ou se prescrivent : délais pour contester un congé, agir en justice après une résiliation, faire opposition à une ordonnance pénale, etc. C'est souvent l'information la plus urgente d'un premier entretien.",
                ]},
                {"heading": "Après l'entretien", "paragraphs": [
                    "Un avocat sérieux vous confirme généralement par écrit le mandat, son étendue et les conditions de facturation. Lisez ce document avant de le signer, et n'hésitez pas à demander des explications sur les points obscurs. Vous restez libre de ne pas donner suite ou de consulter un autre avocat pour un second avis.",
                ]},
            ],
            "faq": [
                {"q": "La première consultation est-elle payante ?",
                 "a": "Cela dépend des cabinets : certains offrent un premier entretien bref, d'autres le facturent au tarif horaire ou à un forfait annoncé. Demandez-le explicitement lors de la prise de rendez-vous. Un cabinet sérieux répond clairement."},
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
                    "Sammeln Sie vor dem Termin alle Unterlagen zu Ihrem Fall: Verträge, Briefe und E-Mails, erhaltene Entscheide, Protokolle, Zeugnisse, Fotos, auch Dokumente, die Ihnen ungünstig erscheinen. Je vollständiger das Bild, desto besser die Beratung; das Berufsgeheimnis (Art. 321 StGB, Art. 13 BGFA) schützt alles, was Sie anvertrauen.",
                    "Erstellen Sie zudem eine schriftliche Chronologie der Ereignisse, wenn möglich auf einer Seite: Daten, Vorgänge, beteiligte Personen. Kein anderes Dokument spart im Erstgespräch mehr Zeit, und damit Honorar.",
                ]},
                {"heading": "Diese Fragen gehören ins Erstgespräch", "paragraphs": [
                    "Klären Sie drei Punkte von Anfang an: die Einschätzung Ihrer Lage (Rechte, Risiken, Erfolgsaussichten), die Strategie (Verhandlung, Prozess, Mediation?) und die Kosten (Abrechnungsart, Kostenvorschuss, geschätztes Gesamtbudget).",
                    "Fragen Sie auch nach laufenden Fristen: Im schweizerischen Recht verwirken oder verjähren viele Ansprüche: Fristen zur Anfechtung einer Kündigung, für Klagen, für die Einsprache gegen einen Strafbefehl usw. Das ist oft die dringendste Information des ersten Gesprächs.",
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
                 "a": "Ja. Das Anwaltsgeheimnis ist durch Art. 321 StGB und Art. 13 BGFA geschützt. Es umfasst alles, was Sie der Anwältin im Rahmen ihrer Berufstätigkeit anvertrauen, auch wenn kein Mandat zustande kommt."},
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
                    "Prima dell'appuntamento, raccogliete tutti i documenti legati al caso: contratti, lettere ed e-mail, decisioni ricevute, verbali, certificati, foto, anche i documenti che vi sembrano sfavorevoli. L'avvocato consiglia tanto meglio quanto più completo è il quadro, e il segreto professionale (art. 321 del Codice penale, art. 13 LLCA) protegge tutto ciò che gli confidate.",
                    "Preparate anche una cronologia scritta dei fatti, se possibile di una pagina: date, eventi, persone coinvolte. È il documento che fa risparmiare più tempo (e quindi onorari) nel primo colloquio.",
                ]},
                {"heading": "Le domande da porre subito", "paragraphs": [
                    "Chiarite tre punti fin dalla prima consulenza: la valutazione della situazione (diritti, rischi, probabilità di successo), la strategia prevista (trattativa, procedura, mediazione?) e i costi (modalità di fatturazione, anticipo richiesto, stima del budget totale).",
                    "Chiedete anche se vi sono termini da rispettare: nel diritto svizzero molti diritti si estinguono o si prescrivono: termini per contestare una disdetta, per agire in giudizio, per fare opposizione a un decreto d'accusa, ecc. È spesso l'informazione più urgente del primo colloquio.",
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
                    "Before the meeting, collect every document related to your matter: contracts, letters and e-mails, decisions received, minutes, certificates, photos, including documents that seem unfavourable to you. A lawyer advises best with the full picture, and professional secrecy (art. 321 of the Criminal Code, art. 13 BGFA/LLCA) protects everything you disclose.",
                    "Also prepare a written timeline of events, ideally one page: dates, facts, people involved. No other document saves more time (and therefore fees) in a first meeting.",
                ]},
                {"heading": "Questions to ask upfront", "paragraphs": [
                    "Clarify three things at the first consultation: the assessment of your situation (rights, risks, prospects), the proposed strategy (negotiation, litigation, mediation?) and the cost (billing method, retainer requested, estimated total budget).",
                    "Also ask about deadlines: under Swiss law many rights lapse or become time-barred: deadlines to challenge a termination, to file suit, to oppose a summary penalty order, and so on. This is often the most urgent information of a first meeting.",
                ]},
                {"heading": "After the meeting", "paragraphs": [
                    "A serious lawyer will generally confirm the mandate, its scope and billing terms in writing. Read that document before signing and ask about anything unclear. You remain free not to proceed, or to consult another lawyer for a second opinion.",
                ]},
            ],
            "faq": [
                {"q": "Is the first consultation free?",
                 "a": "It depends on the firm: some offer a brief first meeting, others bill it at their hourly rate or an announced flat fee. Ask explicitly when booking the appointment. A serious firm will answer clearly."},
                {"q": "What should I bring to the first meeting?",
                 "a": "All documents related to the matter (contracts, correspondence, decisions, evidence), an identity document and, if possible, a written timeline of events. Bring unfavourable documents too: the lawyer needs the full picture to advise you properly."},
                {"q": "Is what I tell a lawyer confidential?",
                 "a": "Yes. A lawyer's professional secrecy is protected by art. 321 of the Criminal Code and art. 13 of the Federal Act on the Free Movement of Lawyers. It covers everything you disclose in the course of the lawyer's professional activity, even if you end up not instructing them."},
                {"q": "Can I change lawyers during proceedings?",
                 "a": "Yes, at any time. You will owe fees for work already done; the new lawyer takes over the file and the previous one must hand over the case documents."},
            ],
        },
    },
    "calcul-prescription": {
        "fr": {
            "slug": "calcul-delai-prescription",
            "title": "Calculateur de délai de prescription en Suisse",
            "meta": "Outil gratuit pour estimer un délai de prescription civile ou pénale en Suisse (art. 60, 127, 128 CO et art. 97 CP), avec les bases légales citées.",
            "sections": [
                {"heading": "À quoi sert ce calculateur", "paragraphs": [
                    "La prescription éteint le droit d'agir en justice une fois un certain délai écoulé depuis un événement déterminé. Ce délai varie fortement selon le type de créance ou d'infraction : 10 ans pour une créance contractuelle ordinaire, 5 ans pour des prestations périodiques comme un loyer ou un salaire, ou un régime à deux délais pour un dommage résultant d'un acte illicite.",
                    "En matière pénale, le délai dépend de la peine maximale encourue pour l'infraction, de 3 ans pour une contravention à 30 ans pour un crime passible d'une peine privative de liberté à vie.",
                ]},
                {"heading": "Ce que le calculateur ne couvre pas", "paragraphs": [
                    "Le résultat est une estimation à partir des délais de base. Il ne tient pas compte des causes de suspension (par exemple pendant une procédure en cours) ni d'interruption de la prescription civile (art. 134 à 138 CO), qui peuvent reporter l'échéance réelle.",
                    "Un délai de prescription qui approche est une situation où le temps compte : en cas de doute, mieux vaut consulter un avocat rapidement plutôt que de se fier uniquement à cette estimation.",
                ]},
            ],
            "faq": [
                {"q": "Que se passe-t-il si une créance est prescrite ?",
                 "a": "Le débiteur peut refuser de payer en invoquant la prescription, mais celle-ci doit être soulevée activement : un tribunal ne l'examine pas d'office. Une dette prescrite reste une obligation naturelle qui peut être payée volontairement."},
                {"q": "La prescription pénale peut-elle être interrompue ?",
                 "a": "Non, depuis la révision entrée en vigueur en 2014, les délais de l'art. 97 CP sont absolus : ils ne sont plus interrompus par des actes de procédure et continuent à courir jusqu'à leur terme."},
                {"q": "Quelle est la différence entre le délai relatif et le délai absolu pour un acte illicite ?",
                 "a": "Le délai relatif (3 ans) court dès que vous connaissez le dommage et son auteur. Le délai absolu (20 ans) court dès l'acte lui-même, indépendamment de la connaissance. La créance est prescrite dès que le premier des deux délais est atteint."},
            ],
        },
        "de": {
            "slug": "verjaehrung-berechnen",
            "title": "Verjährungsrechner für die Schweiz",
            "meta": "Kostenloses Tool zur Schätzung einer zivil- oder strafrechtlichen Verjährungsfrist in der Schweiz (Art. 60, 127, 128 OR und Art. 97 StGB), mit zitierten Rechtsgrundlagen.",
            "sections": [
                {"heading": "Wozu dieser Rechner dient", "paragraphs": [
                    "Die Verjährung lässt das Klagerecht nach Ablauf einer bestimmten Frist seit einem massgebenden Ereignis untergehen. Diese Frist unterscheidet sich stark je nach Art der Forderung oder Straftat: 10 Jahre für eine gewöhnliche vertragliche Forderung, 5 Jahre für periodische Leistungen wie Miete oder Lohn, oder eine Zweifristenregelung für einen Schaden aus unerlaubter Handlung.",
                    "Im Strafrecht hängt die Frist von der für die Straftat angedrohten Höchststrafe ab, von 3 Jahren für eine Übertretung bis 30 Jahre für ein mit lebenslänglicher Freiheitsstrafe bedrohtes Verbrechen.",
                ]},
                {"heading": "Was der Rechner nicht abdeckt", "paragraphs": [
                    "Das Ergebnis ist eine Schätzung anhand der Grundfristen. Hemmungsgründe (zum Beispiel während eines laufenden Verfahrens) und Unterbrechungsgründe der zivilrechtlichen Verjährung (Art. 134 bis 138 OR) werden nicht berücksichtigt und können den tatsächlichen Endtermin verschieben.",
                    "Bei einer nahenden Verjährungsfrist zählt jede Woche: im Zweifelsfall sollte rasch eine Anwältin oder ein Anwalt konsultiert werden, statt sich allein auf diese Schätzung zu verlassen.",
                ]},
            ],
            "faq": [
                {"q": "Was geschieht, wenn eine Forderung verjährt ist?",
                 "a": "Die Schuldnerin oder der Schuldner kann die Zahlung unter Berufung auf die Verjährung verweigern; diese muss aber aktiv geltend gemacht werden, ein Gericht prüft sie nicht von Amtes wegen. Eine verjährte Schuld bleibt eine natürliche Verbindlichkeit, die freiwillig beglichen werden kann."},
                {"q": "Kann die strafrechtliche Verjährung unterbrochen werden?",
                 "a": "Nein. Seit der 2014 in Kraft getretenen Revision sind die Fristen von Art. 97 StGB absolut: Sie werden durch Verfahrenshandlungen nicht mehr unterbrochen und laufen bis zu ihrem Ende weiter."},
                {"q": "Was unterscheidet die relative von der absoluten Frist bei unerlaubter Handlung?",
                 "a": "Die relative Frist (3 Jahre) beginnt mit der Kenntnis von Schaden und Schädiger. Die absolute Frist (20 Jahre) beginnt mit der Handlung selbst, unabhängig von der Kenntnis. Die Forderung verjährt, sobald die frühere der beiden Fristen erreicht ist."},
            ],
        },
        "it": {
            "slug": "calcolo-prescrizione",
            "title": "Calcolatore del termine di prescrizione in Svizzera",
            "meta": "Strumento gratuito per stimare un termine di prescrizione civile o penale in Svizzera (art. 60, 127, 128 CO e art. 97 CP), con le basi legali citate.",
            "sections": [
                {"heading": "A cosa serve questo calcolatore", "paragraphs": [
                    "La prescrizione estingue il diritto di agire in giudizio una volta trascorso un determinato termine da un evento specifico. Questo termine varia molto a seconda del tipo di credito o di reato: 10 anni per un credito contrattuale ordinario, 5 anni per prestazioni periodiche come una pigione o un salario, oppure un regime a due termini per un danno derivante da atto illecito.",
                    "In materia penale, il termine dipende dalla pena massima comminata per il reato, da 3 anni per una contravvenzione a 30 anni per un crimine punibile con la pena detentiva a vita.",
                ]},
                {"heading": "Cosa non copre questo calcolatore", "paragraphs": [
                    "Il risultato è una stima basata sui termini di base. Non tiene conto delle cause di sospensione (per esempio durante una procedura in corso) né di interruzione della prescrizione civile (art. 134 a 138 CO), che possono spostare la scadenza reale.",
                    "Un termine di prescrizione che si avvicina è una situazione in cui il tempo conta: in caso di dubbio, è meglio consultare rapidamente un avvocato piuttosto che affidarsi solo a questa stima.",
                ]},
            ],
            "faq": [
                {"q": "Cosa succede se un credito è prescritto?",
                 "a": "Il debitore può rifiutarsi di pagare invocando la prescrizione, ma questa deve essere sollevata attivamente: un tribunale non la esamina d'ufficio. Un debito prescritto rimane un'obbligazione naturale che può essere pagata volontariamente."},
                {"q": "La prescrizione penale può essere interrotta?",
                 "a": "No. Dalla revisione in vigore dal 2014, i termini dell'art. 97 CP sono assoluti: non sono più interrotti da atti procedurali e continuano a decorrere fino al loro termine."},
                {"q": "Qual è la differenza tra il termine relativo e quello assoluto per un atto illecito?",
                 "a": "Il termine relativo (3 anni) decorre dalla conoscenza del danno e del suo autore. Il termine assoluto (20 anni) decorre dall'atto stesso, indipendentemente dalla conoscenza. Il credito è prescritto non appena è raggiunto il primo dei due termini."},
            ],
        },
        "en": {
            "slug": "prescription-calculator",
            "title": "Statute of limitations calculator for Switzerland",
            "meta": "Free tool to estimate a civil or criminal limitation period in Switzerland (art. 60, 127, 128 CO and art. 97 Criminal Code), with the legal basis cited.",
            "sections": [
                {"heading": "What this calculator is for", "paragraphs": [
                    "Limitation extinguishes the right to sue once a set period has elapsed since a defining event. That period varies significantly depending on the type of claim or offence: 10 years for an ordinary contractual claim, 5 years for periodic performances such as rent or wages, or a two-tier regime for damage arising from an unlawful act.",
                    "In criminal matters, the period depends on the maximum penalty incurred for the offence, from 3 years for a minor offence up to 30 years for a crime punishable by life imprisonment.",
                ]},
                {"heading": "What this calculator does not cover", "paragraphs": [
                    "The result is an estimate based on the basic statutory periods. It does not account for causes of suspension (for example during ongoing proceedings) or interruption of civil limitation (art. 134 to 138 CO), which can push back the actual deadline.",
                    "An approaching limitation deadline is a situation where time matters: if in doubt, it is best to consult a lawyer promptly rather than relying solely on this estimate.",
                ]},
            ],
            "faq": [
                {"q": "What happens if a claim is time-barred?",
                 "a": "The debtor may refuse to pay by invoking limitation, but this must be actively raised; a court does not examine it on its own initiative. A time-barred debt remains a natural obligation that can still be paid voluntarily."},
                {"q": "Can criminal limitation be interrupted?",
                 "a": "No. Since the revision in force since 2014, the periods under art. 97 of the Criminal Code are absolute: they are no longer interrupted by procedural acts and keep running until they expire."},
                {"q": "What is the difference between the relative and absolute deadline for an unlawful act?",
                 "a": "The relative deadline (3 years) starts running once you know of the loss and the liable person. The absolute deadline (20 years) starts running from the act itself, regardless of knowledge. The claim becomes time-barred as soon as whichever deadline comes first is reached."},
            ],
        },
    },
    "calcul-delai-procedure": {
        "fr": {
            "slug": "calcul-delai-recours",
            "title": "Calculateur de délai de recours ou de procédure en Suisse",
            "meta": "Outil gratuit pour calculer l'échéance d'un délai de procédure civile en Suisse, en tenant compte des féries judiciaires (art. 142 et 145 CPC).",
            "sections": [
                {"heading": "Comment ce calculateur fonctionne", "paragraphs": [
                    "En procédure civile suisse, un délai fixé en jours commence à courir le lendemain de la communication qui le déclenche (art. 142 al. 1 CPC). Si son dernier jour tombe un samedi, un dimanche ou un jour férié reconnu, il est reporté au premier jour ouvrable suivant (art. 142 al. 3 CPC).",
                    "Trois périodes de féries judiciaires suspendent en plus le cours des délais en procédure ordinaire (art. 145 CPC) : la semaine avant et après Pâques, la mi-juillet à la mi-août, et les fêtes de fin d'année. Ce calculateur applique ces deux règles automatiquement.",
                ]},
                {"heading": "Limites à connaître", "paragraphs": [
                    "Seuls le week-end et le 1er août (seul jour férié reconnu au niveau fédéral) sont vérifiés automatiquement. Les jours fériés propres au canton ou à la commune du siège du tribunal ne sont pas inclus et doivent être vérifiés séparément auprès du tribunal concerné.",
                    "Ce calculateur ne remplace pas une vérification par un professionnel avant un acte de procédure important : manquer un délai de recours est en principe définitif.",
                ]},
            ],
            "faq": [
                {"q": "Les féries judiciaires s'appliquent-elles à toutes les procédures ?",
                 "a": "Non. L'art. 145 al. 2 CPC exclut la procédure de conciliation et la procédure sommaire, qui continuent pendant les féries. Sélectionnez le bon type de procédure dans le calculateur."},
                {"q": "Les féries judiciaires civiles sont-elles les mêmes que les féries des poursuites ?",
                 "a": "Non, ce sont deux régimes distincts avec des dates différentes : les féries de poursuite relèvent de l'art. 56 LP et ne sont pas couvertes par ce calculateur."},
                {"q": "Que se passe-t-il si je manque un délai de recours ?",
                 "a": "En principe, l'acte devient irrecevable et la décision entre en force. Une restitution de délai n'est possible que dans des cas exceptionnels (art. 148 CPC), en cas d'empêchement non fautif."},
            ],
        },
        "de": {
            "slug": "rechtsmittelfrist-berechnen",
            "title": "Rechtsmittel- und Verfahrensfristenrechner für die Schweiz",
            "meta": "Kostenloses Tool zur Berechnung des Endes einer zivilprozessualen Frist in der Schweiz unter Berücksichtigung der Gerichtsferien (Art. 142 und 145 ZPO).",
            "sections": [
                {"heading": "So funktioniert dieser Rechner", "paragraphs": [
                    "Im schweizerischen Zivilprozess beginnt eine in Tagen bemessene Frist am Tag nach der auslösenden Mitteilung zu laufen (Art. 142 Abs. 1 ZPO). Fällt der letzte Tag auf einen Samstag, Sonntag oder einen anerkannten Feiertag, wird die Frist auf den nächsten Werktag verschoben (Art. 142 Abs. 3 ZPO).",
                    "Zusätzlich unterbrechen drei Gerichtsferien-Perioden den Fristenlauf im ordentlichen Verfahren (Art. 145 ZPO): die Woche vor und nach Ostern, Mitte Juli bis Mitte August, und die Weihnachtszeit. Dieser Rechner wendet beide Regeln automatisch an.",
                ]},
                {"heading": "Grenzen, die Sie kennen sollten", "paragraphs": [
                    "Automatisch geprüft werden nur das Wochenende und der 1. August, der einzige eidgenössisch anerkannte Feiertag. Kantonale oder kommunale Feiertage am Gerichtssitz sind nicht enthalten und müssen separat beim betreffenden Gericht abgeklärt werden.",
                    "Dieser Rechner ersetzt keine fachliche Prüfung vor einer wichtigen Verfahrenshandlung: eine verpasste Rechtsmittelfrist ist grundsätzlich endgültig.",
                ]},
            ],
            "faq": [
                {"q": "Gelten die Gerichtsferien für alle Verfahren?",
                 "a": "Nein. Art. 145 Abs. 2 ZPO schliesst das Schlichtungsverfahren und das summarische Verfahren aus, die während der Gerichtsferien weiterlaufen. Wählen Sie die richtige Verfahrensart im Rechner."},
                {"q": "Sind die zivilrechtlichen Gerichtsferien dasselbe wie die Betreibungsferien?",
                 "a": "Nein, das sind zwei getrennte Regelungen mit unterschiedlichen Daten: Die Betreibungsferien richten sich nach Art. 56 SchKG und werden von diesem Rechner nicht abgedeckt."},
                {"q": "Was passiert, wenn ich eine Rechtsmittelfrist verpasse?",
                 "a": "Grundsätzlich wird die Eingabe unzulässig und der Entscheid erwächst in Rechtskraft. Eine Wiederherstellung der Frist ist nur in Ausnahmefällen möglich (Art. 148 ZPO), bei unverschuldeter Verhinderung."},
            ],
        },
        "it": {
            "slug": "calcolo-termine-ricorso",
            "title": "Calcolatore del termine di ricorso o procedurale per la Svizzera",
            "meta": "Strumento gratuito per calcolare la scadenza di un termine procedurale civile in Svizzera, tenendo conto della sospensione feriale (art. 142 e 145 CPC).",
            "sections": [
                {"heading": "Come funziona questo calcolatore", "paragraphs": [
                    "Nella procedura civile svizzera, un termine fissato in giorni decorre dal giorno successivo alla comunicazione che lo fa scattare (art. 142 cpv. 1 CPC). Se l'ultimo giorno cade di sabato, domenica o in un giorno festivo riconosciuto, il termine è prorogato al primo giorno feriale seguente (art. 142 cpv. 3 CPC).",
                    "Inoltre, tre periodi di sospensione feriale interrompono il decorso dei termini nella procedura ordinaria (art. 145 CPC): la settimana prima e dopo Pasqua, da metà luglio a metà agosto, e le festività di fine anno. Questo calcolatore applica automaticamente entrambe le regole.",
                ]},
                {"heading": "Limiti da conoscere", "paragraphs": [
                    "Vengono verificati automaticamente solo il fine settimana e il 1° agosto, unico giorno festivo riconosciuto a livello federale. I giorni festivi cantonali o comunali della sede del tribunale non sono inclusi e devono essere verificati separatamente presso il tribunale competente.",
                    "Questo calcolatore non sostituisce una verifica professionale prima di un atto procedurale importante: la perdita di un termine di ricorso è in linea di principio definitiva.",
                ]},
            ],
            "faq": [
                {"q": "La sospensione feriale si applica a tutte le procedure?",
                 "a": "No. L'art. 145 cpv. 2 CPC esclude la procedura di conciliazione e la procedura sommaria, che proseguono durante la sospensione feriale. Selezionate il tipo di procedura corretto nel calcolatore."},
                {"q": "La sospensione feriale civile coincide con quella dell'esecuzione?",
                 "a": "No, sono due regimi distinti con date diverse: la sospensione feriale dell'esecuzione è retta dall'art. 56 LEF e non è coperta da questo calcolatore."},
                {"q": "Cosa succede se perdo un termine di ricorso?",
                 "a": "In linea di principio l'atto diventa irricevibile e la decisione passa in giudicato. Una restituzione del termine è possibile solo in casi eccezionali (art. 148 CPC), in caso di impedimento senza colpa."},
            ],
        },
        "en": {
            "slug": "appeal-deadline-calculator",
            "title": "Appeal and procedural deadline calculator for Switzerland",
            "meta": "Free tool to calculate the deadline for a Swiss civil procedure time limit, accounting for court recess periods (art. 142 and 145 CPC).",
            "sections": [
                {"heading": "How this calculator works", "paragraphs": [
                    "Under Swiss civil procedure, a deadline set in days starts running the day after the notice that triggers it (art. 142 para. 1 CPC). If its last day falls on a Saturday, Sunday or a recognised public holiday, it is postponed to the next business day (art. 142 para. 3 CPC).",
                    "Three court recess periods additionally suspend deadlines in ordinary proceedings (art. 145 CPC): the week before and after Easter, mid-July to mid-August, and the year-end holidays. This calculator applies both rules automatically.",
                ]},
                {"heading": "Limits to be aware of", "paragraphs": [
                    "Only weekends and 1 August (the only public holiday recognised at federal level) are checked automatically. Public holidays specific to the canton or municipality where the court sits are not included and must be checked separately with the relevant court.",
                    "This calculator does not replace a professional check before any significant procedural step: missing an appeal deadline is generally final.",
                ]},
            ],
            "faq": [
                {"q": "Do court recess periods apply to every type of proceedings?",
                 "a": "No. Art. 145 para. 2 CPC excludes conciliation proceedings and summary proceedings, which continue during recess periods. Select the correct type of proceedings in the calculator."},
                {"q": "Are civil court recess periods the same as debt enforcement recess periods?",
                 "a": "No, these are two separate regimes with different dates: debt enforcement recess periods are governed by art. 56 DEBA and are not covered by this calculator."},
                {"q": "What happens if I miss an appeal deadline?",
                 "a": "As a rule, the submission becomes inadmissible and the decision becomes final. Restoring a deadline is only possible in exceptional cases (art. 148 CPC), where the failure was not the party's fault."},
            ],
        },
    },
    "calcul-interets-moratoires": {
        "fr": {
            "slug": "calcul-interets-moratoires",
            "title": "Calculateur d'intérêts moratoires en Suisse",
            "meta": "Outil gratuit pour calculer des intérêts moratoires au taux légal de 5% l'an ou à un taux conventionnel (art. 104 CO).",
            "sections": [
                {"heading": "Le principe de l'intérêt moratoire", "paragraphs": [
                    "Lorsqu'un débiteur est en retard dans le paiement d'une somme d'argent, le créancier a droit à un intérêt moratoire, même sans avoir subi de dommage. À défaut d'un taux convenu entre les parties, la loi fixe ce taux à 5% l'an (art. 104 al. 1 CO).",
                    "L'intérêt commence à courir dès que le débiteur est en demeure : soit le lendemain d'une échéance fixée au contrat, soit le lendemain d'une sommation (mise en demeure) si aucune échéance n'avait été convenue (art. 102 CO).",
                ]},
                {"heading": "Comment ce calculateur compte les jours", "paragraphs": [
                    "Le calcul se fait au prorata du nombre exact de jours entre la date de départ et la date de fin, sur une base de 365 jours par an. C'est une méthode indicative et courante ; un décompte définitif entre parties ou devant un tribunal peut retenir une convention légèrement différente.",
                    "Un taux conventionnel plus élevé que 5% est possible s'il a été convenu entre les parties, dans les limites de l'interdiction de l'usure. Vous pouvez le saisir directement dans le champ prévu.",
                ]},
            ],
            "faq": [
                {"q": "Le taux de 5% s'applique-t-il toujours ?",
                 "a": "C'est le taux légal supplétif, applicable sauf accord contraire entre les parties ou disposition légale spéciale prévoyant un autre taux."},
                {"q": "Faut-il un dommage pour réclamer des intérêts moratoires ?",
                 "a": "Non. L'intérêt moratoire est dû du seul fait du retard dans le paiement d'une somme d'argent, sans que le créancier ait à prouver un dommage."},
                {"q": "Comment fixer la date de départ des intérêts si le contrat ne prévoit pas d'échéance ?",
                 "a": "Il faut mettre le débiteur en demeure, généralement par une sommation écrite. Les intérêts courent en principe dès le lendemain de cette sommation (art. 102 CO)."},
            ],
        },
        "de": {
            "slug": "verzugszins-berechnen",
            "title": "Verzugszinsrechner für die Schweiz",
            "meta": "Kostenloses Tool zur Berechnung von Verzugszinsen zum gesetzlichen Satz von 5% pro Jahr oder zu einem vereinbarten Satz (Art. 104 OR).",
            "sections": [
                {"heading": "Das Prinzip des Verzugszinses", "paragraphs": [
                    "Gerät eine Schuldnerin oder ein Schuldner mit der Zahlung eines Geldbetrags in Verzug, hat die Gläubigerin oder der Gläubiger Anspruch auf Verzugszins, auch ohne einen Schaden nachzuweisen. Fehlt eine zwischen den Parteien vereinbarte Zinshöhe, setzt das Gesetz diesen Satz auf 5% pro Jahr fest (Art. 104 Abs. 1 OR).",
                    "Der Zins beginnt zu laufen, sobald sich die Schuldnerin oder der Schuldner in Verzug befindet: entweder am Tag nach einer vertraglich vereinbarten Fälligkeit, oder am Tag nach einer Mahnung, falls keine Fälligkeit vereinbart wurde (Art. 102 OR).",
                ]},
                {"heading": "Wie dieser Rechner die Tage zählt", "paragraphs": [
                    "Die Berechnung erfolgt taggenau zwischen Start- und Enddatum, auf Basis von 365 Tagen pro Jahr. Dies ist eine gängige, indikative Methode; eine endgültige Abrechnung zwischen Parteien oder vor Gericht kann eine leicht andere Konvention zugrunde legen.",
                    "Ein höherer vereinbarter Zinssatz als 5% ist möglich, sofern er zwischen den Parteien vereinbart wurde, innerhalb der Grenzen des Wuchers. Sie können ihn direkt im vorgesehenen Feld eingeben.",
                ]},
            ],
            "faq": [
                {"q": "Gilt der Satz von 5% immer?",
                 "a": "Es handelt sich um den gesetzlichen Auffangsatz, anwendbar sofern die Parteien nichts anderes vereinbart haben oder eine besondere gesetzliche Bestimmung einen anderen Satz vorsieht."},
                {"q": "Braucht es einen Schaden, um Verzugszinsen zu verlangen?",
                 "a": "Nein. Der Verzugszins ist allein wegen des Zahlungsverzugs geschuldet, ohne dass die Gläubigerin oder der Gläubiger einen Schaden nachweisen muss."},
                {"q": "Wie bestimme ich den Beginn des Zinslaufs, wenn der Vertrag keine Fälligkeit vorsieht?",
                 "a": "Die Schuldnerin oder der Schuldner muss gemahnt werden, in der Regel schriftlich. Die Zinsen laufen grundsätzlich ab dem Tag nach dieser Mahnung (Art. 102 OR)."},
            ],
        },
        "it": {
            "slug": "calcolo-interessi-moratori",
            "title": "Calcolatore degli interessi moratori per la Svizzera",
            "meta": "Strumento gratuito per calcolare gli interessi moratori al tasso legale del 5% annuo o a un tasso convenzionale (art. 104 CO).",
            "sections": [
                {"heading": "Il principio dell'interesse moratorio", "paragraphs": [
                    "Quando un debitore è in ritardo nel pagamento di una somma di denaro, il creditore ha diritto a un interesse moratorio, anche senza aver subito un danno. In mancanza di un tasso convenuto tra le parti, la legge fissa questo tasso al 5% annuo (art. 104 cpv. 1 CO).",
                    "L'interesse inizia a decorrere non appena il debitore è in mora: il giorno successivo a una scadenza fissata contrattualmente, oppure il giorno successivo a una diffida se non era stata convenuta alcuna scadenza (art. 102 CO).",
                ]},
                {"heading": "Come questo calcolatore conta i giorni", "paragraphs": [
                    "Il calcolo è effettuato in proporzione al numero esatto di giorni tra la data di inizio e la data di fine, su base di 365 giorni all'anno. È un metodo indicativo e comune; un conteggio definitivo tra le parti o davanti a un tribunale può adottare una convenzione leggermente diversa.",
                    "Un tasso convenzionale superiore al 5% è possibile se è stato concordato tra le parti, entro i limiti del divieto di usura. Potete inserirlo direttamente nel campo previsto.",
                ]},
            ],
            "faq": [
                {"q": "Il tasso del 5% si applica sempre?",
                 "a": "È il tasso legale suppletivo, applicabile salvo accordo contrario tra le parti o disposizione legale speciale che preveda un tasso diverso."},
                {"q": "Serve un danno per richiedere interessi moratori?",
                 "a": "No. L'interesse moratorio è dovuto per il solo fatto del ritardo nel pagamento di una somma di denaro, senza che il creditore debba provare un danno."},
                {"q": "Come si stabilisce la data di inizio degli interessi se il contratto non prevede una scadenza?",
                 "a": "Occorre costituire in mora il debitore, generalmente con una diffida scritta. Gli interessi decorrono in linea di principio dal giorno successivo a tale diffida (art. 102 CO)."},
            ],
        },
        "en": {
            "slug": "late-payment-interest-calculator",
            "title": "Late payment interest calculator for Switzerland",
            "meta": "Free tool to calculate late payment interest at the statutory rate of 5% per year or an agreed rate (art. 104 CO).",
            "sections": [
                {"heading": "The principle of late payment interest", "paragraphs": [
                    "When a debtor is late in paying a sum of money, the creditor is entitled to late payment interest, even without having suffered any loss. Absent a rate agreed between the parties, the law sets this rate at 5% per year (art. 104 para. 1 CO).",
                    "Interest starts accruing once the debtor is in default: either the day after a due date set in the contract, or the day after formal notice (mise en demeure) if no due date had been agreed (art. 102 CO).",
                ]},
                {"heading": "How this calculator counts days", "paragraphs": [
                    "The calculation is prorated to the exact number of days between the start and end dates, on a 365-day-per-year basis. This is a common, indicative method; a final settlement between parties or before a court may use a slightly different convention.",
                    "An agreed rate higher than 5% is possible if agreed between the parties, within the limits of the prohibition on usury. You can enter it directly in the field provided.",
                ]},
            ],
            "faq": [
                {"q": "Does the 5% rate always apply?",
                 "a": "It is the statutory default rate, applicable unless the parties have agreed otherwise or a special legal provision sets a different rate."},
                {"q": "Do I need to prove a loss to claim late payment interest?",
                 "a": "No. Late payment interest is owed simply because of the delay in paying a sum of money, without the creditor having to prove any loss."},
                {"q": "How do I determine the start date for interest if the contract sets no due date?",
                 "a": "The debtor must be put in default, usually via written formal notice. Interest generally starts running the day after that notice (art. 102 CO)."},
            ],
        },
    },
    "calcul-amende-vitesse": {
        "fr": {
            "slug": "calculateur-amende-exces-vitesse-gratuit",
            "title": "Calculateur gratuit d'amende excès de vitesse et retrait de permis",
            "meta": "Outil gratuit : calculez votre amende pour excès de vitesse en Suisse et le risque de retrait de permis selon le barème officiel (OAO, art. 16 LCR).",
            "sections": [
                {"heading": "Un barème fédéral fixe, jusqu'à un certain seuil", "paragraphs": [
                    "En Suisse, les excès de vitesse modérés sont sanctionnés par une amende d'ordre au montant fixe, prévu par le barème fédéral des amendes d'ordre (OAO). Ce barème varie selon que l'excès a lieu à l'intérieur d'une localité, hors localité, ou sur autoroute — les seuils de tolérance sont plus élevés hors agglomération.",
                    "Au-delà d'un certain dépassement, l'amende d'ordre ne s'applique plus : l'infraction fait l'objet d'une dénonciation pénale, et des mesures administratives (avertissement, retrait du permis de conduire) s'ajoutent à une amende dont le montant n'est plus fixé par un barème, mais par le Ministère public ou un tribunal.",
                ]},
            ],
            "faq": [
                {"q": "Ce calculateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Il applique le barème fédéral des amendes d'ordre (OAO) ainsi que les seuils de retrait de permis des art. 16a à 16c LCR."},
                {"q": "Le dépassement à saisir inclut-il la marge de tolérance du radar ?",
                 "a": "Non : indiquez le dépassement déjà net, tel qu'il figure sur l'amende ou le rapport de mesure reçu, tolérance déjà déduite."},
                {"q": "Que se passe-t-il si mon excès de vitesse dépasse le barème fixe ?",
                 "a": "L'amende n'est alors plus fixée par un tarif : l'infraction fait l'objet d'une dénonciation pénale et l'amende est déterminée par le Ministère public ou un tribunal, en fonction des circonstances. Le permis de conduire est en principe retiré, pour une durée qui dépend de la gravité de l'infraction (art. 16b et 16c LCR)."},
                {"q": "Ce résultat remplace-t-il une consultation d'avocat ?",
                 "a": "Non. Il s'agit d'un résultat indicatif basé sur le barème fédéral et les seuils légaux généraux. Les circonstances concrètes (antécédents, canton, mise en danger) peuvent faire varier la décision de l'autorité. Un avocat en droit de la circulation routière peut faire recours contre une mesure de retrait."},
            ],
        },
        "de": {
            "slug": "kostenloser-bussenrechner-geschwindigkeit",
            "title": "Kostenloser Bussenrechner für Geschwindigkeitsüberschreitungen und Führerausweisentzug",
            "meta": "Kostenloses Tool: Berechnen Sie Ihre Busse für eine Geschwindigkeitsüberschreitung in der Schweiz und das Risiko eines Führerausweisentzugs nach dem offiziellen Bussenkatalog (OBV, Art. 16 SVG).",
            "sections": [
                {"heading": "Ein fester eidgenössischer Tarif, bis zu einer bestimmten Schwelle", "paragraphs": [
                    "In der Schweiz werden moderate Geschwindigkeitsüberschreitungen mit einer betragsmässig festen Ordnungsbusse geahndet, die im eidgenössischen Ordnungsbussenkatalog (OBV) festgelegt ist. Dieser Katalog unterscheidet zwischen innerorts, ausserorts und Autobahn — ausserhalb von Ortschaften gelten höhere Toleranzschwellen.",
                    "Ab einer bestimmten Überschreitung gilt die Ordnungsbusse nicht mehr: Die Widerhandlung wird zur Anzeige gebracht, und zur Busse, die dann nicht mehr tarifmässig, sondern von der Staatsanwaltschaft oder einem Gericht festgelegt wird, kommen administrative Massnahmen (Verwarnung, Führerausweisentzug) hinzu.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Rechner kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Er wendet den eidgenössischen Ordnungsbussenkatalog (OBV) sowie die Ausweisentzugs-Schwellen der Art. 16a bis 16c SVG an."},
                {"q": "Ist die Messtoleranz des Radars in der einzugebenden Überschreitung enthalten?",
                 "a": "Nein: Geben Sie die bereits bereinigte Nettoüberschreitung an, wie sie auf der erhaltenen Busse oder dem Messbericht ausgewiesen ist."},
                {"q": "Was passiert, wenn meine Geschwindigkeitsüberschreitung den festen Tarif übersteigt?",
                 "a": "Die Busse wird dann nicht mehr tarifmässig festgelegt: Die Widerhandlung wird zur Anzeige gebracht, und die Busse wird von der Staatsanwaltschaft oder einem Gericht je nach Umständen bestimmt. Der Führerausweis wird in der Regel entzogen, für eine Dauer, die von der Schwere der Widerhandlung abhängt (Art. 16b und 16c SVG)."},
                {"q": "Ersetzt dieses Ergebnis eine anwaltliche Beratung?",
                 "a": "Nein. Es handelt sich um ein Orientierungsergebnis auf Grundlage des eidgenössischen Tarifs und der allgemeinen gesetzlichen Schwellen. Konkrete Umstände (Vorstrafen, Kanton, Gefährdung) können den Entscheid der Behörde beeinflussen. Eine auf Verkehrsrecht spezialisierte Anwältin bzw. ein Anwalt kann gegen einen Entzug Beschwerde führen."},
            ],
        },
        "it": {
            "slug": "calcolatore-multa-eccesso-velocita-gratuito",
            "title": "Calcolatore gratuito di multa per eccesso di velocità e ritiro della licenza",
            "meta": "Strumento gratuito: calcolate la vostra multa per eccesso di velocità in Svizzera e il rischio di ritiro della licenza secondo il tariffario ufficiale (OAO, art. 16 LCStr).",
            "sections": [
                {"heading": "Un tariffario federale fisso, fino a una certa soglia", "paragraphs": [
                    "In Svizzera, gli eccessi di velocità moderati sono sanzionati con una multa disciplinare di importo fisso, previsto dal tariffario federale delle multe disciplinari (OAO). Questo tariffario varia a seconda che il superamento avvenga all'interno di una località, fuori località o in autostrada — le soglie di tolleranza sono più elevate fuori dagli abitati.",
                    "Oltre un certo superamento, la multa disciplinare non si applica più: l'infrazione viene denunciata penalmente, e alla multa, il cui importo non è più fissato da un tariffario ma dal Ministero pubblico o da un tribunale, si aggiungono misure amministrative (ammonimento, ritiro della licenza di condurre).",
                ]},
            ],
            "faq": [
                {"q": "Questo calcolatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Applica il tariffario federale delle multe disciplinari (OAO) e le soglie di ritiro della licenza degli art. 16a-16c LCStr."},
                {"q": "Il superamento da inserire include la tolleranza di misurazione del radar?",
                 "a": "No: indicate il superamento già al netto, come riportato sulla multa o sul rapporto di misurazione ricevuto."},
                {"q": "Cosa succede se il mio eccesso di velocità supera il tariffario fisso?",
                 "a": "La multa non è più fissata da una tariffa: l'infrazione viene denunciata penalmente e la multa è determinata dal Ministero pubblico o da un tribunale, a seconda delle circostanze. La licenza di condurre viene di norma ritirata, per una durata che dipende dalla gravità dell'infrazione (art. 16b e 16c LCStr)."},
                {"q": "Questo risultato sostituisce una consulenza legale?",
                 "a": "No. Si tratta di un risultato indicativo basato sul tariffario federale e sulle soglie legali generali. Le circostanze concrete (precedenti, cantone, messa in pericolo) possono far variare la decisione dell'autorità. Un avvocato specializzato in diritto della circolazione può presentare ricorso contro un ritiro."},
            ],
        },
        "en": {
            "slug": "free-speeding-fine-calculator",
            "title": "Free speeding fine and licence withdrawal calculator",
            "meta": "Free tool: calculate your speeding fine in Switzerland and the risk of driving licence withdrawal under the official schedule (OAO, art. 16 LCR).",
            "sections": [
                {"heading": "A fixed federal schedule, up to a certain threshold", "paragraphs": [
                    "In Switzerland, moderate speeding is sanctioned with a fixed-amount fine set by the federal fixed-penalty fine schedule (OAO). This schedule differs depending on whether the overage occurs inside a built-up area, outside one, or on a motorway — tolerance thresholds are higher outside built-up areas.",
                    "Beyond a certain overage, the fixed-penalty fine no longer applies: the offence is referred for criminal prosecution, and administrative measures (warning, licence withdrawal) are added to a fine whose amount is then set by the public prosecutor or a court, not by a schedule.",
                ]},
            ],
            "faq": [
                {"q": "Is this calculator free?",
                 "a": "Yes, completely free and with no registration. It applies the federal fixed-penalty fine schedule (OAO) and the licence withdrawal thresholds of art. 16a to 16c LCR."},
                {"q": "Does the overage I enter already account for the radar's measurement tolerance?",
                 "a": "No: enter the net overage already adjusted, as shown on the fine or measurement report you received."},
                {"q": "What happens if my speeding overage exceeds the fixed schedule?",
                 "a": "The fine is then no longer set by a tariff: the offence is referred for criminal prosecution and the fine is determined by the public prosecutor or a court, depending on the circumstances. The driving licence is typically withdrawn, for a duration depending on the severity of the offence (art. 16b and 16c LCR)."},
                {"q": "Does this result replace a consultation with a lawyer?",
                 "a": "No. This is an indicative result based on the federal schedule and general legal thresholds. Concrete circumstances (prior record, canton, danger created) can affect the authority's decision. A lawyer specialising in road traffic law can appeal a withdrawal decision."},
            ],
        },
    },
    "resiliation-bail": {
        "fr": {
            "slug": "lettre-resiliation-bail-gratuite",
            "title": "Générateur gratuit de lettre de résiliation de bail",
            "meta": "Outil gratuit : générez votre lettre de résiliation de bail en Suisse (logement ou local commercial) avec vérification du délai légal (art. 266c/266d CO).",
            "sections": [
                {"heading": "Un délai minimal, mais un terme à respecter", "paragraphs": [
                    "En droit suisse, la résiliation d'un bail d'habitation doit respecter un préavis minimal de 3 mois ; pour un local commercial, le préavis minimal est de 6 mois (art. 266c et 266d CO). Ces délais sont des minimums : le contrat peut prévoir un préavis plus long, jamais plus court.",
                    "La résiliation doit en outre être donnée pour un « terme », c'est-à-dire une date de fin de bail prévue par le contrat ou par les usages locaux — le plus souvent la fin d'un trimestre. Ce générateur vérifie le respect du délai minimal jusqu'à la date que vous indiquez, mais ne devine pas si cette date correspond à un terme valable pour votre bail : vérifiez ce point dans votre contrat.",
                ]},
            ],
            "faq": [
                {"q": "Ce générateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Il génère une lettre de résiliation prête à relire, compléter et signer."},
                {"q": "Le délai de 3 mois s'applique-t-il à tous les logements ?",
                 "a": "C'est le délai minimal légal (art. 266c CO) pour un logement loué pour une durée indéterminée. Le contrat peut prévoir un délai plus long. Pour un local commercial, le délai minimal est de 6 mois (art. 266d CO)."},
                {"q": "Comment envoyer cette lettre ?",
                 "a": "Il est recommandé de l'envoyer par courrier recommandé, afin de disposer d'une preuve de la date d'envoi en cas de litige sur le respect du délai."},
                {"q": "Que faire si le bailleur conteste la date de résiliation ?",
                 "a": "Si le bailleur estime que la résiliation ne respecte pas un terme valable, la résiliation peut être reportée au terme suivant. En cas de désaccord, la commission de conciliation en matière de baux, puis un avocat spécialisé en droit du bail, peuvent vous conseiller."},
            ],
        },
        "de": {
            "slug": "kostenloses-mietkuendigungsschreiben",
            "title": "Kostenloser Generator für Mietkündigungsschreiben",
            "meta": "Kostenloses Tool: Erstellen Sie Ihr Mietkündigungsschreiben in der Schweiz (Wohnung oder Geschäftsräume) mit Prüfung der gesetzlichen Frist (Art. 266c/266d OR).",
            "sections": [
                {"heading": "Eine Mindestfrist, aber ein einzuhaltender Termin", "paragraphs": [
                    "Nach schweizerischem Recht muss die Kündigung eines Wohnungsmietvertrags eine Mindestfrist von 3 Monaten einhalten; für Geschäftsräume beträgt die Mindestfrist 6 Monate (Art. 266c und 266d OR). Diese Fristen sind Minimalfristen: Der Vertrag kann eine längere, nie eine kürzere Frist vorsehen.",
                    "Die Kündigung muss zudem auf einen «Termin» hin erfolgen, also ein im Vertrag oder durch örtliche Gepflogenheiten vorgesehenes Enddatum — meist das Quartalsende. Dieser Generator prüft die Einhaltung der Mindestfrist bis zum von Ihnen angegebenen Datum, errät aber nicht, ob dieses Datum einem für Ihren Mietvertrag gültigen Termin entspricht: Prüfen Sie dies in Ihrem Vertrag.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Generator kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Er erstellt ein kündigungsfertiges Schreiben zum Prüfen, Ergänzen und Unterschreiben."},
                {"q": "Gilt die 3-Monats-Frist für alle Wohnungen?",
                 "a": "Dies ist die gesetzliche Mindestfrist (Art. 266c OR) für eine unbefristet vermietete Wohnung. Der Vertrag kann eine längere Frist vorsehen. Für Geschäftsräume beträgt die Mindestfrist 6 Monate (Art. 266d OR)."},
                {"q": "Wie soll ich dieses Schreiben versenden?",
                 "a": "Es wird empfohlen, es per Einschreiben zu versenden, um im Streitfall über die Fristeinhaltung einen Nachweis des Versanddatums zu haben."},
                {"q": "Was, wenn die Vermieterschaft das Kündigungsdatum bestreitet?",
                 "a": "Ist die Vermieterschaft der Ansicht, die Kündigung entspreche keinem gültigen Termin, kann sie auf den nächstfolgenden Termin verschoben werden. Bei Uneinigkeit können die Schlichtungsbehörde für Mietsachen und anschliessend eine auf Mietrecht spezialisierte Anwältin bzw. ein Anwalt beraten."},
            ],
        },
        "it": {
            "slug": "lettera-disdetta-affitto-gratuita",
            "title": "Generatore gratuito di lettera di disdetta del contratto d'affitto",
            "meta": "Strumento gratuito: generate la vostra lettera di disdetta d'affitto in Svizzera (abitazione o locale commerciale) con verifica del termine legale (art. 266c/266d CO).",
            "sections": [
                {"heading": "Un termine minimo, ma una scadenza da rispettare", "paragraphs": [
                    "Secondo il diritto svizzero, la disdetta di un contratto di locazione abitativa deve rispettare un preavviso minimo di 3 mesi; per un locale commerciale, il preavviso minimo è di 6 mesi (art. 266c e 266d CO). Questi termini sono minimi: il contratto può prevedere un preavviso più lungo, mai più breve.",
                    "La disdetta deve inoltre essere data per una «scadenza», cioè una data di fine locazione prevista dal contratto o dagli usi locali — di norma la fine di un trimestre. Questo generatore verifica il rispetto del termine minimo fino alla data indicata, ma non stabilisce se tale data corrisponda a una scadenza valida per il vostro contratto: verificatelo nel vostro contratto.",
                ]},
            ],
            "faq": [
                {"q": "Questo generatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Genera una lettera di disdetta pronta da rileggere, completare e firmare."},
                {"q": "Il termine di 3 mesi si applica a tutte le abitazioni?",
                 "a": "È il termine legale minimo (art. 266c CO) per un'abitazione locata a tempo indeterminato. Il contratto può prevedere un termine più lungo. Per un locale commerciale, il termine minimo è di 6 mesi (art. 266d CO)."},
                {"q": "Come devo inviare questa lettera?",
                 "a": "Si consiglia di inviarla per raccomandata, per disporre di una prova della data di invio in caso di controversia sul rispetto del termine."},
                {"q": "Cosa fare se il locatore contesta la data di disdetta?",
                 "a": "Se il locatore ritiene che la disdetta non rispetti una scadenza valida, essa può essere rinviata alla scadenza successiva. In caso di disaccordo, l'autorità di conciliazione in materia di locazione e, successivamente, un avvocato specializzato in diritto della locazione possono fornire consulenza."},
            ],
        },
        "en": {
            "slug": "free-lease-termination-letter",
            "title": "Free lease termination letter generator",
            "meta": "Free tool: generate your lease termination letter in Switzerland (housing or commercial premises) with a check of the legal notice period (art. 266c/266d CO).",
            "sections": [
                {"heading": "A minimum notice period, but a valid date to respect", "paragraphs": [
                    "Under Swiss law, terminating a residential lease requires a minimum notice period of 3 months; for commercial premises, the minimum is 6 months (art. 266c and 266d CO). These are minimums: the lease may set a longer period, never a shorter one.",
                    "Notice must also be given for a valid termination date set by the lease or by local usage — usually the end of a quarter. This generator checks that the minimum notice period is respected up to the date you enter, but does not guess whether that date matches a valid term for your lease: check this in your contract.",
                ]},
            ],
            "faq": [
                {"q": "Is this generator free?",
                 "a": "Yes, completely free and with no registration. It produces a ready-to-review termination letter for you to complete and sign."},
                {"q": "Does the 3-month notice period apply to all housing leases?",
                 "a": "This is the minimum legal notice period (art. 266c CO) for an open-ended residential lease. The lease may set a longer period. For commercial premises, the minimum notice period is 6 months (art. 266d CO)."},
                {"q": "How should I send this letter?",
                 "a": "It is recommended to send it by registered mail, to have proof of the sending date in case of a dispute over the notice period."},
                {"q": "What if the landlord disputes the termination date?",
                 "a": "If the landlord considers the notice does not match a valid term, it may be postponed to the next available term. If there is disagreement, the rental conciliation authority, and then a lawyer specialising in tenancy law, can advise you."},
            ],
        },
    },
    "estimation-pension-alimentaire": {
        "fr": {
            "slug": "estimation-pension-alimentaire-gratuite",
            "title": "Estimateur gratuit de pension alimentaire pour enfant en Suisse",
            "meta": "Outil gratuit : estimez une pension alimentaire indicative pour votre enfant selon la méthode en deux étapes du Tribunal fédéral (ATF 147 III 265).",
            "sections": [
                {"heading": "Pas de formule légale fixe, mais une méthode en deux étapes", "paragraphs": [
                    "Contrairement à d'autres calculs juridiques, il n'existe en Suisse aucun barème légal fixe pour la pension alimentaire d'un enfant. Depuis l'arrêt de principe ATF 147 III 265 (2021), le Tribunal fédéral impose toutefois une méthode commune à tous les tribunaux : déterminer d'abord le minimum vital de chaque parent et de l'enfant, puis répartir l'éventuel excédent entre les membres de la famille.",
                    "Cet estimateur applique une version simplifiée et illustrative de cette méthode, avec les montants de base du minimum vital reconnus en matière de poursuite (art. 93 LP) et une répartition de l'excédent selon la convention dite \"grandes têtes / petites têtes\". Il ne remplace pas le pouvoir d'appréciation du juge, qui tient compte de bien d'autres éléments (garde alternée, revenu hypothétique, besoins particuliers de l'enfant, contribution de prise en charge).",
                ]},
            ],
            "faq": [
                {"q": "Cet estimateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Aucune donnée saisie n'est enregistrée."},
                {"q": "Le résultat est-il le montant que je devrai payer ou recevoir ?",
                 "a": "Non. C'est une estimation indicative basée sur une version simplifiée de la méthode du Tribunal fédéral. Le montant fixé par un juge ou une convention alimentaire peut différer sensiblement en fonction d'éléments non pris en compte ici (garde alternée, revenu hypothétique, besoins particuliers de l'enfant, contribution de prise en charge)."},
                {"q": "Pourquoi l'outil me demande-t-il mon loyer et mes assurances plutôt que de les estimer ?",
                 "a": "Ce site applique un principe de non-fabrication : aucun montant réel n'est deviné à votre place. Vous devez saisir vos propres charges effectives pour obtenir une estimation cohérente."},
                {"q": "Que se passe-t-il si le parent débiteur n'a pas assez de revenu ?",
                 "a": "Si son revenu ne dépasse pas son propre minimum vital, l'outil l'indique clairement : dans ce cas, le juge peut envisager de lui imputer un revenu hypothétique s'il estime qu'il pourrait raisonnablement gagner davantage. Cette question relève d'une analyse individuelle par un avocat en droit de la famille."},
            ],
        },
        "de": {
            "slug": "kostenlose-schaetzung-kinderunterhalt",
            "title": "Kostenloser Kinderunterhalt-Rechner für die Schweiz",
            "meta": "Kostenloses Tool: Schätzen Sie einen orientierenden Kinderunterhaltsbeitrag nach der zweistufigen Methode des Bundesgerichts (BGE 147 III 265).",
            "sections": [
                {"heading": "Keine feste gesetzliche Formel, aber eine zweistufige Methode", "paragraphs": [
                    "Anders als bei anderen juristischen Berechnungen gibt es in der Schweiz keinen festen gesetzlichen Tarif für den Kinderunterhalt. Seit dem Grundsatzentscheid BGE 147 III 265 (2021) schreibt das Bundesgericht jedoch allen Gerichten eine gemeinsame Methode vor: zuerst das Existenzminimum jedes Elternteils und des Kindes ermitteln, dann einen allfälligen Überschuss unter den Familienmitgliedern verteilen.",
                    "Dieser Rechner wendet eine vereinfachte, illustrative Version dieser Methode an, mit den im Betreibungsrecht anerkannten Grundbeträgen des Existenzminimums (Art. 93 SchKG) und einer Überschussverteilung nach der sogenannten Konvention \"grosse Köpfe / kleine Köpfe\". Er ersetzt nicht das richterliche Ermessen, das viele weitere Elemente berücksichtigt (alternierende Obhut, hypothetisches Einkommen, besondere Bedürfnisse des Kindes, Betreuungsunterhalt).",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Rechner kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Es werden keine eingegebenen Daten gespeichert."},
                {"q": "Ist das Ergebnis der Betrag, den ich zahlen oder erhalten werde?",
                 "a": "Nein. Es handelt sich um eine orientierende Schätzung auf Grundlage einer vereinfachten Version der bundesgerichtlichen Methode. Der von einem Gericht oder einer Unterhaltsvereinbarung festgelegte Betrag kann erheblich abweichen, abhängig von hier nicht berücksichtigten Elementen (alternierende Obhut, hypothetisches Einkommen, besondere Bedürfnisse des Kindes, Betreuungsunterhalt)."},
                {"q": "Warum fragt das Tool nach meiner Miete und meinen Versicherungen, statt sie zu schätzen?",
                 "a": "Diese Website folgt dem Grundsatz, nichts zu erfinden: Es wird kein tatsächlicher Betrag für Sie geraten. Sie müssen Ihre eigenen effektiven Auslagen eingeben, um eine stimmige Schätzung zu erhalten."},
                {"q": "Was passiert, wenn der unterhaltspflichtige Elternteil kein ausreichendes Einkommen hat?",
                 "a": "Übersteigt sein Einkommen sein eigenes Existenzminimum nicht, weist das Tool klar darauf hin: In diesem Fall kann das Gericht erwägen, ihm ein hypothetisches Einkommen anzurechnen, wenn es davon ausgeht, dass er vernünftigerweise mehr verdienen könnte. Diese Frage erfordert eine individuelle Analyse durch eine auf Familienrecht spezialisierte Anwältin bzw. einen Anwalt."},
            ],
        },
        "it": {
            "slug": "stima-gratuita-alimenti-figli",
            "title": "Calcolatore gratuito di alimenti per i figli in Svizzera",
            "meta": "Strumento gratuito: stimate un contributo alimentare indicativo per vostro figlio secondo il metodo in due fasi del Tribunale federale (DTF 147 III 265).",
            "sections": [
                {"heading": "Nessuna formula legale fissa, ma un metodo in due fasi", "paragraphs": [
                    "A differenza di altri calcoli giuridici, in Svizzera non esiste un tariffario legale fisso per gli alimenti dei figli. Dalla sentenza di principio DTF 147 III 265 (2021), il Tribunale federale impone tuttavia un metodo comune a tutti i tribunali: determinare anzitutto il minimo vitale di ciascun genitore e del figlio, poi ripartire l'eventuale eccedenza tra i membri della famiglia.",
                    "Questo calcolatore applica una versione semplificata e illustrativa di tale metodo, con gli importi base del minimo vitale riconosciuti in materia di esecuzione (art. 93 LEF) e una ripartizione dell'eccedenza secondo la cosiddetta convenzione delle \"teste grandi / teste piccole\". Non sostituisce il potere di apprezzamento del giudice, che tiene conto di molti altri elementi (custodia alternata, reddito ipotetico, bisogni particolari del figlio, contributo di presa a carico).",
                ]},
            ],
            "faq": [
                {"q": "Questo calcolatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Nessun dato inserito viene salvato."},
                {"q": "Il risultato è l'importo che dovrò pagare o ricevere?",
                 "a": "No. Si tratta di una stima indicativa basata su una versione semplificata del metodo del Tribunale federale. L'importo fissato da un giudice o da una convenzione alimentare può differire sensibilmente in base a elementi qui non considerati (custodia alternata, reddito ipotetico, bisogni particolari del figlio, contributo di presa a carico)."},
                {"q": "Perché lo strumento chiede il mio affitto e le mie assicurazioni invece di stimarli?",
                 "a": "Questo sito applica un principio di non invenzione: nessun importo reale viene ipotizzato al posto vostro. Dovete inserire le vostre spese effettive per ottenere una stima coerente."},
                {"q": "Cosa succede se il genitore debitore non ha un reddito sufficiente?",
                 "a": "Se il suo reddito non supera il proprio minimo vitale, lo strumento lo indica chiaramente: in tal caso, il giudice può valutare di imputargli un reddito ipotetico se ritiene che potrebbe ragionevolmente guadagnare di più. Questa questione richiede un'analisi individuale da parte di un avvocato specializzato in diritto di famiglia."},
            ],
        },
        "en": {
            "slug": "free-child-support-estimate",
            "title": "Free child support (pension alimentaire) estimator for Switzerland",
            "meta": "Free tool: estimate indicative child support for your child using the Federal Supreme Court's two-stage method (ATF 147 III 265).",
            "sections": [
                {"heading": "No fixed legal formula, but a two-stage method", "paragraphs": [
                    "Unlike other legal calculations, Switzerland has no fixed legal schedule for child support. Since the leading case ATF 147 III 265 (2021), however, the Federal Supreme Court requires all courts to follow a common method: first determine each parent's and the child's minimum subsistence level, then distribute any surplus among family members.",
                    "This estimator applies a simplified, illustrative version of that method, using the minimum-subsistence base amounts recognised in debt-enforcement law (art. 93 LP) and a surplus distribution under the so-called \"big heads / small heads\" convention. It does not replace the court's discretion, which considers many other factors (alternating custody, hypothetical income, the child's specific needs, care-related contribution).",
                ]},
            ],
            "faq": [
                {"q": "Is this estimator free?",
                 "a": "Yes, completely free and with no registration. No data you enter is saved."},
                {"q": "Is the result the amount I will have to pay or receive?",
                 "a": "No. It is an indicative estimate based on a simplified version of the Federal Supreme Court's method. The amount set by a court or a support agreement can differ significantly based on factors not covered here (alternating custody, hypothetical income, the child's specific needs, care-related contribution)."},
                {"q": "Why does the tool ask for my rent and insurance instead of estimating them?",
                 "a": "This site follows a never-fabricate principle: no real figure is guessed on your behalf. You must enter your own actual expenses to get a coherent estimate."},
                {"q": "What happens if the paying parent doesn't have enough income?",
                 "a": "If their income does not exceed their own minimum subsistence, the tool clearly states this: in that case, the court may consider imputing a hypothetical income if it judges the parent could reasonably earn more. This question requires an individual analysis by a lawyer specialising in family law."},
            ],
        },
    },
    "calcul-frais-poursuite": {
        "fr": {
            "slug": "calculateur-frais-poursuite-gratuit",
            "title": "Calculateur gratuit des frais de poursuite en Suisse",
            "meta": "Outil gratuit : calculez l'émolument du commandement de payer selon le barème officiel de l'OELP (art. 16), en vigueur depuis 2026.",
            "sections": [
                {"heading": "Un barème dégressif fixé par ordonnance fédérale", "paragraphs": [
                    "Lorsqu'un créancier engage une poursuite pour dettes en Suisse, l'office des poursuites perçoit un émolument pour la rédaction, l'établissement et la notification du commandement de payer. Ce montant est fixé par un barème fédéral dégressif : plus la créance est élevée, plus l'émolument, en proportion, diminue.",
                    "Ce barème a été révisé avec effet au 1er janvier 2026. Ce calculateur applique la version actuellement en vigueur, telle que publiée dans le Recueil officiel du droit fédéral. L'émolument est avancé par le créancier au dépôt de la réquisition de poursuite, puis mis à la charge finale du débiteur si la poursuite aboutit.",
                ]},
            ],
            "faq": [
                {"q": "Ce calculateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Il applique le barème officiel actuel de l'art. 16 al. 1 OELP."},
                {"q": "Ce montant couvre-t-il tous les frais d'une poursuite ?",
                 "a": "Non. Il ne couvre que l'émolument de base du commandement de payer. D'autres frais peuvent s'ajouter : tentative de notification supplémentaire, double exemplaire, procédure d'opposition, continuation de la poursuite, saisie ou faillite."},
                {"q": "Qui paie cet émolument au départ ?",
                 "a": "Le créancier l'avance lors du dépôt de sa réquisition de poursuite auprès de l'office des poursuites compétent. Si la poursuite aboutit, cet émolument est mis à la charge finale du débiteur (art. 68 LP)."},
                {"q": "Ce barème a-t-il changé récemment ?",
                 "a": "Oui, une révision est entrée en vigueur le 1er janvier 2026. Les montants affichés par cet outil correspondent au texte actuellement en vigueur ; vérifiez le Recueil officiel du droit fédéral en cas de doute sur une créance très ancienne."},
            ],
        },
        "de": {
            "slug": "kostenloser-betreibungskostenrechner",
            "title": "Kostenloser Betreibungskosten-Rechner für die Schweiz",
            "meta": "Kostenloses Tool: Berechnen Sie die Gebühr für den Zahlungsbefehl nach dem amtlichen Tarif der GebV SchKG (Art. 16), gültig seit 2026.",
            "sections": [
                {"heading": "Ein degressiver Tarif, festgelegt durch eidgenössische Verordnung", "paragraphs": [
                    "Leitet ein Gläubiger in der Schweiz eine Betreibung ein, erhebt das Betreibungsamt eine Gebühr für die Ausfertigung, Erstellung und Zustellung des Zahlungsbefehls. Dieser Betrag wird durch einen degressiven eidgenössischen Tarif festgelegt: Je höher die Forderung, desto geringer die Gebühr im Verhältnis dazu.",
                    "Dieser Tarif wurde mit Wirkung ab 1. Januar 2026 revidiert. Dieser Rechner wendet die aktuell gültige Fassung an, wie sie in der Amtlichen Sammlung des Bundesrechts veröffentlicht ist. Die Gebühr wird vom Gläubiger bei der Einreichung des Betreibungsbegehrens vorgeschossen und dem Schuldner endgültig auferlegt, wenn die Betreibung erfolgreich ist.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Rechner kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Er wendet den aktuellen amtlichen Tarif von Art. 16 Abs. 1 GebV SchKG an."},
                {"q": "Deckt dieser Betrag alle Kosten einer Betreibung ab?",
                 "a": "Nein. Er deckt nur die Grundgebühr des Zahlungsbefehls ab. Weitere Kosten können hinzukommen: zusätzlicher Zustellversuch, Doppel, Rechtsvorschlagsverfahren, Fortsetzung der Betreibung, Pfändung oder Konkurs."},
                {"q": "Wer zahlt diese Gebühr zunächst?",
                 "a": "Der Gläubiger schiesst sie bei der Einreichung seines Betreibungsbegehrens beim zuständigen Betreibungsamt vor. Ist die Betreibung erfolgreich, wird die Gebühr dem Schuldner endgültig auferlegt (Art. 68 SchKG)."},
                {"q": "Hat sich dieser Tarif kürzlich geändert?",
                 "a": "Ja, eine Revision trat am 1. Januar 2026 in Kraft. Die von diesem Tool angezeigten Beträge entsprechen der aktuell gültigen Fassung; prüfen Sie im Zweifelsfall bei einer sehr alten Forderung die Amtliche Sammlung des Bundesrechts."},
            ],
        },
        "it": {
            "slug": "calcolatore-spese-esecuzione-gratuito",
            "title": "Calcolatore gratuito delle spese di esecuzione in Svizzera",
            "meta": "Strumento gratuito: calcolate la tassa del precetto esecutivo secondo il tariffario ufficiale dell'OTLEF (art. 16), in vigore dal 2026.",
            "sections": [
                {"heading": "Un tariffario degressivo fissato da ordinanza federale", "paragraphs": [
                    "Quando un creditore avvia un'esecuzione per debiti in Svizzera, l'ufficio d'esecuzione riscuote una tassa per la redazione, l'allestimento e la notificazione del precetto esecutivo. Questo importo è fissato da un tariffario federale degressivo: più elevato è il credito, minore è la tassa in proporzione.",
                    "Questo tariffario è stato rivisto con effetto dal 1° gennaio 2026. Questo calcolatore applica la versione attualmente in vigore, come pubblicata nella Raccolta ufficiale del diritto federale. La tassa è anticipata dal creditore al momento del deposito della domanda d'esecuzione, poi posta definitivamente a carico del debitore se l'esecuzione va a buon fine.",
                ]},
            ],
            "faq": [
                {"q": "Questo calcolatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Applica il tariffario ufficiale attuale dell'art. 16 cpv. 1 OTLEF."},
                {"q": "Questo importo copre tutte le spese di un'esecuzione?",
                 "a": "No. Copre solo la tassa base del precetto esecutivo. Possono aggiungersi altre spese: ulteriore tentativo di notificazione, doppio esemplare, procedura di opposizione, continuazione dell'esecuzione, pignoramento o fallimento."},
                {"q": "Chi paga inizialmente questa tassa?",
                 "a": "Il creditore la anticipa al momento del deposito della domanda d'esecuzione presso l'ufficio d'esecuzione competente. Se l'esecuzione va a buon fine, questa tassa viene posta definitivamente a carico del debitore (art. 68 LEF)."},
                {"q": "Questo tariffario è cambiato di recente?",
                 "a": "Sì, una revisione è entrata in vigore il 1° gennaio 2026. Gli importi mostrati da questo strumento corrispondono al testo attualmente in vigore; in caso di dubbio su un credito molto vecchio, verificate la Raccolta ufficiale del diritto federale."},
            ],
        },
        "en": {
            "slug": "free-debt-collection-fee-calculator",
            "title": "Free debt-collection fee calculator for Switzerland",
            "meta": "Free tool: calculate the fee for the payment order under the official OELP fee schedule (art. 16), in force since 2026.",
            "sections": [
                {"heading": "A degressive schedule set by federal ordinance", "paragraphs": [
                    "When a creditor starts debt-collection proceedings in Switzerland, the debt-enforcement office charges a fee for drafting, preparing and serving the payment order. This amount is set by a degressive federal schedule: the higher the claim, the lower the fee proportionally.",
                    "This schedule was revised with effect from 1 January 2026. This calculator applies the version currently in force, as published in the Official Compilation of Federal Legislation. The fee is advanced by the creditor when filing the collection request, and is ultimately charged to the debtor if the collection proceeding succeeds.",
                ]},
            ],
            "faq": [
                {"q": "Is this calculator free?",
                 "a": "Yes, completely free and with no registration. It applies the current official schedule of art. 16 para. 1 OELP."},
                {"q": "Does this amount cover all costs of a debt-collection proceeding?",
                 "a": "No. It only covers the base fee for the payment order. Other costs may be added: an additional service attempt, an extra copy, opposition proceedings, continuation of the collection proceeding, seizure or bankruptcy."},
                {"q": "Who pays this fee initially?",
                 "a": "The creditor advances it when filing the collection request with the competent debt-enforcement office. If the collection proceeding succeeds, this fee is ultimately charged to the debtor (art. 68 LP)."},
                {"q": "Has this schedule changed recently?",
                 "a": "Yes, a revision came into force on 1 January 2026. The amounts shown by this tool match the currently applicable text; for a very old claim, check the Official Compilation of Federal Legislation if in doubt."},
            ],
        },
    },
    "demande-sous-location": {
        "fr": {
            "slug": "demande-sous-location-gratuite",
            "title": "Générateur gratuit de demande de sous-location",
            "meta": "Outil gratuit : générez votre demande de consentement à la sous-location (art. 262 CO), avec vérification du loyer selon la jurisprudence.",
            "sections": [
                {"heading": "Un accord écrit obligatoire du bailleur", "paragraphs": [
                    "En droit suisse, un locataire peut sous-louer tout ou partie de son logement, mais seulement avec le consentement écrit préalable du bailleur (art. 262 CO). Le bailleur ne peut refuser ce consentement que pour des motifs limitativement énumérés par la loi : refus de communiquer les conditions de la sous-location, conditions abusives par rapport au bail principal, ou inconvénients majeurs pour le bailleur.",
                    "Le loyer de sous-location fait l'objet d'une attention particulière : selon la jurisprudence du Tribunal fédéral (ATF 119 II 353), une majoration du loyer de sous-location par rapport au loyer principal n'est en principe admise, dans l'ordre de 20%, que si le logement est meublé ou accompagné de prestations supplémentaires (mobilier, ustensiles, charges incluses). Sans cela, un loyer de sous-location sensiblement supérieur au loyer principal peut être considéré comme abusif.",
                ]},
            ],
            "faq": [
                {"q": "Ce générateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Il génère une lettre de demande de consentement prête à relire, compléter et signer."},
                {"q": "Puis-je sous-louer sans l'accord du bailleur ?",
                 "a": "Non. Une sous-location sans le consentement écrit du bailleur constitue une violation du contrat de bail et peut justifier une résiliation anticipée par le bailleur (art. 262 al. 3 CO)."},
                {"q": "Le bailleur peut-il refuser sans raison ?",
                 "a": "Non. Les motifs de refus sont limitativement énumérés à l'art. 262 al. 2 CO : refus de communiquer les conditions de la sous-location, conditions abusives, ou inconvénients majeurs pour le bailleur. Un refus arbitraire peut être contesté."},
                {"q": "Que se passe-t-il si l'outil signale un loyer de sous-location abusif ?",
                 "a": "Cela signifie que la majoration dépasse le seuil généralement admis par la jurisprudence pour un logement non meublé. Ce n'est pas une interdiction automatique, mais un risque de contestation ; ajustez le loyer ou documentez les prestations supplémentaires justifiant la majoration, et consultez si besoin un avocat spécialisé en droit du bail."},
            ],
        },
        "de": {
            "slug": "kostenloses-untermietgesuch",
            "title": "Kostenloser Generator für Untermietgesuche",
            "meta": "Kostenloses Tool: Erstellen Sie Ihr Gesuch um Zustimmung zur Untervermietung (Art. 262 OR), mit Prüfung des Mietzinses nach der Rechtsprechung.",
            "sections": [
                {"heading": "Eine zwingend schriftliche Zustimmung der Vermieterschaft", "paragraphs": [
                    "Nach schweizerischem Recht darf ein Mieter seine Wohnung ganz oder teilweise untervermieten, jedoch nur mit der vorgängigen schriftlichen Zustimmung der Vermieterschaft (Art. 262 OR). Die Vermieterschaft darf diese Zustimmung nur aus abschliessend im Gesetz genannten Gründen verweigern: Weigerung, die Bedingungen der Untermiete mitzuteilen, missbräuchliche Bedingungen im Vergleich zum Hauptmietvertrag, oder wesentliche Nachteile für die Vermieterschaft.",
                    "Der Untermietzins wird besonders geprüft: Gemäss bundesgerichtlicher Rechtsprechung (BGE 119 II 353) ist ein Aufschlag des Untermietzinses gegenüber dem Hauptmietzins grundsätzlich nur in der Grössenordnung von 20% zulässig, wenn die Wohnung möbliert ist oder zusätzliche Leistungen umfasst (Mobiliar, Ausstattung, eingeschlossene Nebenkosten). Ohne dies kann ein deutlich höherer Untermietzins als missbräuchlich gelten.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Generator kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Er erstellt ein zustimmungsfertiges Gesuch zum Prüfen, Ergänzen und Unterschreiben."},
                {"q": "Darf ich ohne Zustimmung der Vermieterschaft untervermieten?",
                 "a": "Nein. Eine Untervermietung ohne schriftliche Zustimmung der Vermieterschaft verletzt den Mietvertrag und kann eine ausserordentliche Kündigung durch die Vermieterschaft rechtfertigen (Art. 262 Abs. 3 OR)."},
                {"q": "Kann die Vermieterschaft grundlos ablehnen?",
                 "a": "Nein. Die Ablehnungsgründe sind in Art. 262 Abs. 2 OR abschliessend aufgezählt: Weigerung, die Bedingungen mitzuteilen, missbräuchliche Bedingungen, oder wesentliche Nachteile für die Vermieterschaft. Eine willkürliche Ablehnung kann angefochten werden."},
                {"q": "Was bedeutet es, wenn das Tool einen missbräuchlichen Untermietzins meldet?",
                 "a": "Das bedeutet, dass der Aufschlag die von der Rechtsprechung für eine unmöblierte Wohnung allgemein akzeptierte Schwelle übersteigt. Das ist kein automatisches Verbot, aber ein Anfechtungsrisiko; passen Sie den Mietzins an oder dokumentieren Sie die zusätzlichen Leistungen, die den Aufschlag rechtfertigen, und konsultieren Sie bei Bedarf eine auf Mietrecht spezialisierte Anwältin bzw. einen Anwalt."},
            ],
        },
        "it": {
            "slug": "richiesta-sublocazione-gratuita",
            "title": "Generatore gratuito di richiesta di sublocazione",
            "meta": "Strumento gratuito: generate la vostra richiesta di consenso alla sublocazione (art. 262 CO), con verifica della pigione secondo la giurisprudenza.",
            "sections": [
                {"heading": "Un accordo scritto obbligatorio del locatore", "paragraphs": [
                    "Secondo il diritto svizzero, un conduttore può sublocare in tutto o in parte la propria abitazione, ma solo con il consenso scritto preventivo del locatore (art. 262 CO). Il locatore può rifiutare questo consenso solo per motivi tassativamente elencati dalla legge: rifiuto di comunicare le condizioni della sublocazione, condizioni abusive rispetto al contratto principale, o inconvenienti rilevanti per il locatore.",
                    "La pigione di sublocazione è oggetto di particolare attenzione: secondo la giurisprudenza del Tribunale federale (DTF 119 II 353), una maggiorazione della pigione di sublocazione rispetto alla pigione principale è di norma ammessa, nell'ordine del 20%, solo se l'abitazione è ammobiliata o accompagnata da prestazioni supplementari (mobilio, dotazioni, spese accessorie incluse). In caso contrario, una pigione di sublocazione sensibilmente superiore alla pigione principale può essere considerata abusiva.",
                ]},
            ],
            "faq": [
                {"q": "Questo generatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Genera una lettera di richiesta di consenso pronta da rileggere, completare e firmare."},
                {"q": "Posso sublocare senza il consenso del locatore?",
                 "a": "No. Una sublocazione senza il consenso scritto del locatore costituisce una violazione del contratto di locazione e può giustificare una disdetta anticipata da parte del locatore (art. 262 cpv. 3 CO)."},
                {"q": "Il locatore può rifiutare senza motivo?",
                 "a": "No. I motivi di rifiuto sono elencati tassativamente all'art. 262 cpv. 2 CO: rifiuto di comunicare le condizioni, condizioni abusive, o inconvenienti rilevanti per il locatore. Un rifiuto arbitrario può essere contestato."},
                {"q": "Cosa significa se lo strumento segnala una pigione di sublocazione abusiva?",
                 "a": "Significa che la maggiorazione supera la soglia generalmente ammessa dalla giurisprudenza per un'abitazione non ammobiliata. Non si tratta di un divieto automatico, ma di un rischio di contestazione; adeguate la pigione o documentate le prestazioni supplementari che giustificano la maggiorazione, e consultate se necessario un avvocato specializzato in diritto della locazione."},
            ],
        },
        "en": {
            "slug": "free-sublease-request",
            "title": "Free sublease consent-request generator",
            "meta": "Free tool: generate your sublease consent request (art. 262 CO), with a rent check based on case law.",
            "sections": [
                {"heading": "A mandatory written agreement from the landlord", "paragraphs": [
                    "Under Swiss law, a tenant may sublet all or part of their home, but only with the landlord's prior written consent (art. 262 CO). The landlord may only refuse consent for reasons exhaustively listed by law: refusal to disclose the sublease terms, terms that are abusive compared with the main lease, or major inconvenience to the landlord.",
                    "The sublease rent gets particular scrutiny: under Federal Supreme Court case law (ATF 119 II 353), a mark-up of the sublease rent over the main rent is generally only accepted, in the order of 20%, if the home is furnished or comes with extra services (furniture, fittings, charges included). Without that, a sublease rent significantly higher than the main rent can be considered abusive.",
                ]},
            ],
            "faq": [
                {"q": "Is this generator free?",
                 "a": "Yes, completely free and with no registration. It produces a ready-to-review consent-request letter for you to complete and sign."},
                {"q": "Can I sublet without the landlord's consent?",
                 "a": "No. Subletting without the landlord's written consent breaches the lease and can justify early termination by the landlord (art. 262 para. 3 CO)."},
                {"q": "Can the landlord refuse without a reason?",
                 "a": "No. The grounds for refusal are exhaustively listed in art. 262 para. 2 CO: refusal to disclose the terms, abusive terms, or major inconvenience to the landlord. An arbitrary refusal can be challenged."},
                {"q": "What does it mean if the tool flags an abusive sublease rent?",
                 "a": "It means the mark-up exceeds the threshold generally accepted by case law for unfurnished accommodation. This is not an automatic ban, but a risk of challenge; adjust the rent or document the extra services justifying the mark-up, and consult a lawyer specialising in tenancy law if needed."},
            ],
        },
    },
    "calcul-reserve-hereditaire": {
        "fr": {
            "slug": "calculateur-reserve-hereditaire-gratuit",
            "title": "Calculateur gratuit de la réserve héréditaire en Suisse",
            "meta": "Outil gratuit : calculez la réserve héréditaire de votre conjoint, de vos descendants et de vos parents selon la réforme entrée en vigueur en 2023 (art. 470/471 CC).",
            "sections": [
                {"heading": "Une réserve réduite depuis la révision de 2023", "paragraphs": [
                    "La révision du droit des successions entrée en vigueur le 1er janvier 2023 a sensiblement réduit la réserve héréditaire, c'est-à-dire la part minimale de la succession que la loi garantit à certains héritiers, même contre la volonté du défunt exprimée par testament. Depuis cette réforme, la réserve du conjoint (ou partenaire enregistré) survivant et celle des descendants sont réduites à la moitié de leur part légale, contre les trois quarts auparavant. La réserve des parents, elle, a été totalement supprimée : un testateur sans conjoint ni descendants peut désormais disposer de l'intégralité de sa succession librement, même en présence de parents survivants.",
                    "La quotité disponible — la part que le défunt peut librement attribuer par testament, y compris à des tiers — est ainsi passée d'un minimum d'un quart à un minimum de la moitié de la succession dans la configuration la plus courante (conjoint et descendants).",
                ]},
            ],
            "faq": [
                {"q": "Ce calculateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Il applique les fractions légales en vigueur depuis le 1er janvier 2023."},
                {"q": "Ce résultat s'applique-t-il si je suis déjà marié sous un régime matrimonial ?",
                 "a": "Ce calculateur porte uniquement sur la réserve héréditaire, calculée sur la masse successorale après liquidation du régime matrimonial (part du conjoint survivant au titre du régime matrimonial, distincte de sa part successorale). Cette liquidation préalable n'est pas prise en compte ici."},
                {"q": "Les parents n'ont-ils vraiment plus aucune protection ?",
                 "a": "Exact, depuis la révision de 2023, les parents du défunt n'ont plus de réserve héréditaire légale. Un testament peut donc les exclure entièrement de la succession, sous réserve d'autres mécanismes de protection (par exemple une donation antérieure sujette à réduction dans certains cas)."},
                {"q": "Que faire si je souhaite rédiger un testament tenant compte de ces règles ?",
                 "a": "Ce calculateur donne un ordre de grandeur indicatif. La rédaction d'un testament valable et adapté à votre situation (present d'éléments internationaux, entreprise à transmettre, pacte successoral) nécessite une consultation d'avocat ou de notaire spécialisé en droit des successions."},
            ],
        },
        "de": {
            "slug": "kostenloser-pflichtteilsrechner",
            "title": "Kostenloser Pflichtteilsrechner für die Schweiz",
            "meta": "Kostenloses Tool: Berechnen Sie den Pflichtteil Ihres Ehegatten, Ihrer Nachkommen und Ihrer Eltern nach der 2023 in Kraft getretenen Reform (Art. 470/471 ZGB).",
            "sections": [
                {"heading": "Ein reduzierter Pflichtteil seit der Revision von 2023", "paragraphs": [
                    "Die am 1. Januar 2023 in Kraft getretene Revision des Erbrechts hat den Pflichtteil deutlich reduziert — jenen Mindestanteil an der Erbschaft, den das Gesetz bestimmten Erben garantiert, selbst gegen den im Testament geäusserten Willen der verstorbenen Person. Seit dieser Reform ist der Pflichtteil des überlebenden Ehegatten (oder der eingetragenen Partnerin bzw. des Partners) sowie der Nachkommen auf die Hälfte ihres gesetzlichen Erbanspruchs reduziert, gegenüber zuvor drei Vierteln. Der Pflichtteil der Eltern wurde vollständig aufgehoben: Ein Erblasser ohne Ehegatten und ohne Nachkommen kann nun frei über seine gesamte Erbschaft verfügen, auch wenn Eltern noch leben.",
                    "Der frei verfügbare Teil — jener Anteil, den die verstorbene Person durch Testament frei zuweisen kann, auch an Dritte — ist damit in der häufigsten Konstellation (Ehegatte und Nachkommen) von einem Minimum von einem Viertel auf ein Minimum von der Hälfte der Erbschaft gestiegen.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Rechner kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Er wendet die seit dem 1. Januar 2023 geltenden gesetzlichen Quoten an."},
                {"q": "Gilt dieses Ergebnis, wenn ich bereits unter einem Güterstand verheiratet bin?",
                 "a": "Dieser Rechner betrifft ausschliesslich den Pflichtteil, berechnet auf der Erbmasse nach güterrechtlicher Auseinandersetzung (der Anteil des überlebenden Ehegatten aus dem Güterrecht ist von seinem erbrechtlichen Anteil zu unterscheiden). Diese vorgängige Auseinandersetzung wird hier nicht berücksichtigt."},
                {"q": "Haben die Eltern wirklich gar keinen Schutz mehr?",
                 "a": "Korrekt, seit der Revision von 2023 haben die Eltern der verstorbenen Person keinen gesetzlichen Pflichtteil mehr. Ein Testament kann sie somit vollständig von der Erbschaft ausschliessen, vorbehältlich anderer Schutzmechanismen (z. B. einer früheren Schenkung, die unter bestimmten Umständen der Herabsetzung unterliegt)."},
                {"q": "Was, wenn ich ein Testament nach diesen Regeln verfassen möchte?",
                 "a": "Dieser Rechner liefert eine orientierende Grössenordnung. Die Errichtung eines gültigen, auf Ihre Situation zugeschnittenen Testaments (internationale Bezüge, zu übertragendes Unternehmen, Erbvertrag) erfordert die Beratung durch eine auf Erbrecht spezialisierte Anwältin bzw. einen Anwalt oder eine Notarin bzw. einen Notar."},
            ],
        },
        "it": {
            "slug": "calcolatore-legittima-gratuito",
            "title": "Calcolatore gratuito della legittima ereditaria in Svizzera",
            "meta": "Strumento gratuito: calcolate la legittima del coniuge, dei discendenti e dei genitori secondo la riforma entrata in vigore nel 2023 (art. 470/471 CC).",
            "sections": [
                {"heading": "Una legittima ridotta dalla revisione del 2023", "paragraphs": [
                    "La revisione del diritto successorio entrata in vigore il 1° gennaio 2023 ha ridotto sensibilmente la legittima, ossia la quota minima della successione che la legge garantisce a determinati eredi, anche contro la volontà del defunto espressa per testamento. Da questa riforma, la legittima del coniuge (o partner registrato) superstite e quella dei discendenti sono ridotte alla metà della loro quota legale, contro i tre quarti precedenti. La legittima dei genitori è stata invece del tutto soppressa: un testatore senza coniuge né discendenti può ora disporre liberamente dell'intera successione, anche in presenza di genitori in vita.",
                    "La quota disponibile — la parte che il defunto può attribuire liberamente per testamento, anche a terzi — è così passata da un minimo di un quarto a un minimo della metà della successione nella configurazione più comune (coniuge e discendenti).",
                ]},
            ],
            "faq": [
                {"q": "Questo calcolatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Applica le quote legali in vigore dal 1° gennaio 2023."},
                {"q": "Questo risultato vale se sono già sposato sotto un regime dei beni?",
                 "a": "Questo calcolatore riguarda esclusivamente la legittima, calcolata sulla massa successoria dopo la liquidazione del regime dei beni (la quota del coniuge superstite a titolo di regime dei beni è distinta dalla sua quota successoria). Questa liquidazione preliminare non è considerata qui."},
                {"q": "I genitori non hanno davvero più alcuna protezione?",
                 "a": "Esatto, dalla revisione del 2023 i genitori del defunto non hanno più una legittima legale. Un testamento può quindi escluderli interamente dalla successione, fatti salvi altri meccanismi di protezione (ad esempio una donazione precedente soggetta a riduzione in determinati casi)."},
                {"q": "Cosa fare se desidero redigere un testamento conforme a queste regole?",
                 "a": "Questo calcolatore fornisce un ordine di grandezza indicativo. La redazione di un testamento valido e adeguato alla vostra situazione (elementi internazionali, impresa da trasmettere, patto successorio) richiede una consulenza presso un avvocato o un notaio specializzato in diritto successorio."},
            ],
        },
        "en": {
            "slug": "free-forced-heirship-calculator",
            "title": "Free forced-heirship (réserve héréditaire) calculator for Switzerland",
            "meta": "Free tool: calculate the forced share of your spouse, descendants and parents under the reform in force since 2023 (art. 470/471 CC).",
            "sections": [
                {"heading": "A reduced forced share since the 2023 revision", "paragraphs": [
                    "The succession-law revision that came into force on 1 January 2023 significantly reduced the forced share (réserve héréditaire) — the minimum portion of the estate the law guarantees to certain heirs, even against the deceased's wishes as expressed in a will. Since that reform, the forced share of the surviving spouse (or registered partner) and of descendants is reduced to half of their statutory share, down from three-quarters previously. The forced share of parents has been abolished entirely: a testator with no spouse and no descendants can now freely dispose of their entire estate, even with living parents.",
                    "The freely disposable portion — the share the deceased can freely assign by will, including to third parties — has thus risen from a minimum of one-quarter to a minimum of one-half of the estate in the most common configuration (spouse and descendants).",
                ]},
            ],
            "faq": [
                {"q": "Is this calculator free?",
                 "a": "Yes, completely free and with no registration. It applies the statutory fractions in force since 1 January 2023."},
                {"q": "Does this result apply if I am already married under a matrimonial-property regime?",
                 "a": "This calculator only covers the forced share, calculated on the estate after the matrimonial-property regime has been settled (the surviving spouse's share under the matrimonial regime is distinct from their inheritance share). That prior settlement is not accounted for here."},
                {"q": "Do parents really have no protection at all anymore?",
                 "a": "Correct — since the 2023 revision, the deceased's parents no longer have a statutory forced share. A will can therefore exclude them entirely from the estate, subject to other protective mechanisms (for example, an earlier gift subject to reduction in certain cases)."},
                {"q": "What if I want to draft a will that reflects these rules?",
                 "a": "This calculator gives an indicative order of magnitude. Drafting a valid will tailored to your situation (international elements, a business to be transferred, an inheritance contract) requires a consultation with a lawyer or notary specialising in inheritance law."},
            ],
        },
    },
    "calcul-delai-conge-bail": {
        "fr": {
            "slug": "calculateur-delai-conge-bail-gratuit",
            "title": "Calculateur gratuit du délai de congé de bail en Suisse",
            "meta": "Outil gratuit : calculez la date la plus proche possible pour résilier votre bail selon le délai légal minimal (art. 266c/266d CO).",
            "sections": [
                {"heading": "Un délai minimal légal, calculé rapidement", "paragraphs": [
                    "Avant d'envoyer un congé pour votre logement ou votre local commercial, il est utile de vérifier rapidement la date la plus proche possible compatible avec le délai légal minimal : 3 mois pour un logement, 6 mois pour un local commercial (art. 266c et 266d CO). Ce calculateur effectue ce calcul instantanément à partir de votre date d'envoi.",
                    "Attention : le délai minimal n'est qu'une première condition. La résiliation doit aussi être donnée pour un terme valable — une date de fin de bail prévue par le contrat ou les usages locaux, le plus souvent la fin d'un trimestre. Ce calculateur ne vérifie que le délai, pas le terme.",
                ]},
            ],
            "faq": [
                {"q": "Cet outil est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription."},
                {"q": "Quelle est la différence avec le générateur de lettre de résiliation de bail du site ?",
                 "a": "Cet outil calcule uniquement la date la plus proche possible à partir d'une date d'envoi. Le générateur de lettre de résiliation de bail, disponible séparément sur ce site, produit en plus un courrier prêt à envoyer avec vérification d'une date de fin que vous avez déjà choisie."},
                {"q": "La date obtenue est-elle automatiquement valable ?",
                 "a": "Non. Elle respecte le délai légal minimal, mais doit encore correspondre à un terme valable selon votre contrat de bail ou les usages locaux. Si ce n'est pas le cas, la résiliation est en principe reportée au terme suivant."},
                {"q": "Ce délai peut-il être plus long que 3 ou 6 mois ?",
                 "a": "Oui, le contrat de bail peut prévoir un délai de congé plus long que le minimum légal, mais jamais plus court. Vérifiez toujours votre contrat en complément de ce calculateur."},
            ],
        },
        "de": {
            "slug": "kostenloser-mietkuendigungsfristrechner",
            "title": "Kostenloser Rechner für die Mietkündigungsfrist in der Schweiz",
            "meta": "Kostenloses Tool: Berechnen Sie das frühestmögliche Datum für die Kündigung Ihres Mietvertrags nach der gesetzlichen Mindestfrist (Art. 266c/266d OR).",
            "sections": [
                {"heading": "Eine gesetzliche Mindestfrist, schnell berechnet", "paragraphs": [
                    "Bevor Sie eine Kündigung für Ihre Wohnung oder Ihre Geschäftsräume versenden, lohnt es sich, rasch das frühestmögliche Datum zu prüfen, das mit der gesetzlichen Mindestfrist vereinbar ist: 3 Monate für eine Wohnung, 6 Monate für Geschäftsräume (Art. 266c und 266d OR). Dieser Rechner führt diese Berechnung sofort anhand Ihres Versanddatums durch.",
                    "Achtung: Die Mindestfrist ist nur eine erste Voraussetzung. Die Kündigung muss zudem auf einen gültigen Termin hin erfolgen — ein im Vertrag oder durch örtliche Gepflogenheiten vorgesehenes Enddatum, meist das Quartalsende. Dieser Rechner prüft nur die Frist, nicht den Termin.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieses Tool kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung."},
                {"q": "Was ist der Unterschied zum Generator für Mietkündigungsschreiben dieser Website?",
                 "a": "Dieses Tool berechnet nur das frühestmögliche Datum ab einem Versanddatum. Der separat auf dieser Website verfügbare Generator für Mietkündigungsschreiben erstellt zusätzlich ein versandfertiges Schreiben mit Prüfung eines von Ihnen bereits gewählten Enddatums."},
                {"q": "Ist das errechnete Datum automatisch gültig?",
                 "a": "Nein. Es hält die gesetzliche Mindestfrist ein, muss aber noch einem gemäss Ihrem Mietvertrag oder den örtlichen Gepflogenheiten gültigen Termin entsprechen. Ist dies nicht der Fall, wird die Kündigung in der Regel auf den nächstfolgenden Termin verschoben."},
                {"q": "Kann diese Frist länger als 3 oder 6 Monate sein?",
                 "a": "Ja, der Mietvertrag kann eine längere Kündigungsfrist als das gesetzliche Minimum vorsehen, nie eine kürzere. Prüfen Sie ergänzend zu diesem Rechner stets Ihren Vertrag."},
            ],
        },
        "it": {
            "slug": "calcolatore-termine-disdetta-affitto-gratuito",
            "title": "Calcolatore gratuito del termine di disdetta dell'affitto in Svizzera",
            "meta": "Strumento gratuito: calcolate la data più vicina possibile per disdire il vostro contratto d'affitto secondo il termine legale minimo (art. 266c/266d CO).",
            "sections": [
                {"heading": "Un termine legale minimo, calcolato rapidamente", "paragraphs": [
                    "Prima di inviare una disdetta per la vostra abitazione o il vostro locale commerciale, è utile verificare rapidamente la data più vicina possibile compatibile con il termine legale minimo: 3 mesi per un'abitazione, 6 mesi per un locale commerciale (art. 266c e 266d CO). Questo calcolatore effettua tale calcolo istantaneamente a partire dalla vostra data di invio.",
                    "Attenzione: il termine minimo è solo una prima condizione. La disdetta deve inoltre essere data per una scadenza valida — una data di fine locazione prevista dal contratto o dagli usi locali, di norma la fine di un trimestre. Questo calcolatore verifica solo il termine, non la scadenza.",
                ]},
            ],
            "faq": [
                {"q": "Questo strumento è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione."},
                {"q": "Qual è la differenza con il generatore di lettera di disdetta del sito?",
                 "a": "Questo strumento calcola solo la data più vicina possibile a partire da una data di invio. Il generatore di lettera di disdetta, disponibile separatamente su questo sito, produce inoltre una lettera pronta da inviare con verifica di una data di fine già scelta da voi."},
                {"q": "La data ottenuta è automaticamente valida?",
                 "a": "No. Rispetta il termine legale minimo, ma deve ancora corrispondere a una scadenza valida secondo il vostro contratto di locazione o gli usi locali. In caso contrario, la disdetta è di norma rinviata alla scadenza successiva."},
                {"q": "Questo termine può essere più lungo di 3 o 6 mesi?",
                 "a": "Sì, il contratto di locazione può prevedere un termine di disdetta più lungo del minimo legale, mai più breve. Verificate sempre il vostro contratto in aggiunta a questo calcolatore."},
            ],
        },
        "en": {
            "slug": "free-lease-notice-period-calculator",
            "title": "Free lease notice-period calculator for Switzerland",
            "meta": "Free tool: calculate the earliest possible date to terminate your lease under the minimum legal notice period (art. 266c/266d CO).",
            "sections": [
                {"heading": "A minimum legal notice period, calculated instantly", "paragraphs": [
                    "Before sending notice for your home or commercial premises, it helps to quickly check the earliest possible date compatible with the minimum legal notice period: 3 months for housing, 6 months for commercial premises (art. 266c and 266d CO). This calculator does that instantly from your sending date.",
                    "Note: the minimum notice period is only a first condition. Notice must also be given for a valid term — an end date set by the lease or by local usage, usually the end of a quarter. This calculator only checks the notice period, not the term.",
                ]},
            ],
            "faq": [
                {"q": "Is this tool free?",
                 "a": "Yes, completely free and with no registration."},
                {"q": "What is the difference with the site's lease termination letter generator?",
                 "a": "This tool only calculates the earliest possible date from a sending date. The lease termination letter generator, available separately on this site, additionally produces a ready-to-send letter with a check of an end date you have already chosen."},
                {"q": "Is the resulting date automatically valid?",
                 "a": "No. It respects the minimum legal notice period, but still needs to match a valid term under your lease or local usage. If it does not, the notice is typically postponed to the next term."},
                {"q": "Can this notice period be longer than 3 or 6 months?",
                 "a": "Yes, the lease may set a longer notice period than the legal minimum, never a shorter one. Always check your contract in addition to this calculator."},
            ],
        },
    },
    "mise-en-demeure": {
        "fr": {
            "slug": "mise-en-demeure-gratuite",
            "title": "Générateur gratuit de mise en demeure",
            "meta": "Outil gratuit : générez votre lettre de mise en demeure pour réclamer un paiement, avec délai de grâce et rappel de l'intérêt moratoire légal (art. 102/104 CO).",
            "sections": [
                {"heading": "Une étape souvent nécessaire avant la poursuite", "paragraphs": [
                    "En droit suisse, un débiteur est mis en demeure par l'interpellation de son créancier (art. 102 CO), sauf si une date d'exécution a déjà été fixée d'un commun accord — dans ce cas, la demeure survient automatiquement à l'échéance. Une mise en demeure écrite, avec un délai de grâce raisonnable, constitue une étape simple mais souvent utile avant d'engager une procédure de poursuite : elle formalise la créance, fixe une échéance claire et prépare le dossier en cas de litige ultérieur.",
                    "Dès la mise en demeure, un intérêt moratoire légal de 5% l'an est dû sur le montant réclamé, sauf taux conventionnel différent (art. 104 CO). Ce générateur intègre ce rappel dans la lettre produite.",
                ]},
            ],
            "faq": [
                {"q": "Ce générateur est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription. Il génère une lettre prête à relire, compléter et signer."},
                {"q": "La mise en demeure est-elle obligatoire avant une poursuite ?",
                 "a": "Non, une poursuite peut en principe être engagée sans mise en demeure préalable. Mais cette lettre reste utile : elle formalise la créance, fixe un délai clair et peut faciliter un règlement amiable avant d'engager les frais et démarches d'une poursuite."},
                {"q": "Quel délai de grâce accorder ?",
                 "a": "La loi ne fixe pas de délai minimal ; un délai de 10 à 30 jours est courant en pratique. Adaptez-le à la nature de la créance et à votre relation avec le débiteur."},
                {"q": "Que faire si le débiteur ne paie pas dans le délai fixé ?",
                 "a": "Vous pouvez alors engager une poursuite pour dettes auprès de l'office des poursuites compétent, ou consulter un avocat si la créance est contestée ou complexe."},
            ],
        },
        "de": {
            "slug": "kostenlose-mahnung",
            "title": "Kostenloser Mahnungs-Generator (Inverzugsetzung)",
            "meta": "Kostenloses Tool: Erstellen Sie Ihre Mahnung zur Zahlungsforderung, mit Nachfrist und Hinweis auf den gesetzlichen Verzugszins (Art. 102/104 OR).",
            "sections": [
                {"heading": "Ein oft notwendiger Schritt vor der Betreibung", "paragraphs": [
                    "Nach schweizerischem Recht wird ein Schuldner durch die Mahnung seines Gläubigers in Verzug gesetzt (Art. 102 OR), es sei denn, ein Erfüllungstermin wurde bereits einvernehmlich festgelegt — in diesem Fall tritt der Verzug automatisch mit Ablauf dieses Termins ein. Eine schriftliche Mahnung mit angemessener Nachfrist ist ein einfacher, aber oft nützlicher Schritt vor Einleitung einer Betreibung: Sie formalisiert die Forderung, setzt eine klare Frist und bereitet die Akte für einen allfälligen späteren Streitfall vor.",
                    "Ab der Mahnung ist ein gesetzlicher Verzugszins von 5% pro Jahr auf den geforderten Betrag geschuldet, sofern kein abweichender vertraglicher Zinssatz vereinbart wurde (Art. 104 OR). Dieser Generator integriert diesen Hinweis in das erstellte Schreiben.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieser Generator kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung. Er erstellt ein unterschriftsfertiges Schreiben zum Prüfen und Ergänzen."},
                {"q": "Ist die Mahnung vor einer Betreibung obligatorisch?",
                 "a": "Nein, eine Betreibung kann grundsätzlich auch ohne vorgängige Mahnung eingeleitet werden. Dieses Schreiben ist dennoch nützlich: Es formalisiert die Forderung, setzt eine klare Frist und kann eine gütliche Einigung erleichtern, bevor Kosten und Aufwand einer Betreibung entstehen."},
                {"q": "Welche Nachfrist sollte ich gewähren?",
                 "a": "Das Gesetz sieht keine Mindestfrist vor; in der Praxis sind 10 bis 30 Tage üblich. Passen Sie die Frist an die Art der Forderung und Ihre Beziehung zum Schuldner an."},
                {"q": "Was, wenn der Schuldner nicht innert der gesetzten Frist zahlt?",
                 "a": "Sie können dann eine Betreibung beim zuständigen Betreibungsamt einleiten oder eine Anwältin bzw. einen Anwalt konsultieren, falls die Forderung bestritten oder komplex ist."},
            ],
        },
        "it": {
            "slug": "diffida-pagamento-gratuita",
            "title": "Generatore gratuito di diffida di pagamento",
            "meta": "Strumento gratuito: generate la vostra lettera di diffida per richiedere un pagamento, con termine di grazia e promemoria dell'interesse di mora legale (art. 102/104 CO).",
            "sections": [
                {"heading": "Una tappa spesso necessaria prima dell'esecuzione", "paragraphs": [
                    "Secondo il diritto svizzero, un debitore è costituito in mora dalla diffida del suo creditore (art. 102 CO), salvo che una data di adempimento sia già stata fissata di comune accordo — in tal caso la mora sopravviene automaticamente alla scadenza. Una diffida scritta, con un termine di grazia ragionevole, costituisce una tappa semplice ma spesso utile prima di avviare una procedura esecutiva: formalizza il credito, fissa una scadenza chiara e prepara il fascicolo in caso di controversia successiva.",
                    "Dalla diffida, è dovuto un interesse di mora legale del 5% annuo sull'importo richiesto, salvo un tasso convenzionale diverso (art. 104 CO). Questo generatore integra questo promemoria nella lettera prodotta.",
                ]},
            ],
            "faq": [
                {"q": "Questo generatore è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione. Genera una lettera pronta da rileggere, completare e firmare."},
                {"q": "La diffida è obbligatoria prima di un'esecuzione?",
                 "a": "No, un'esecuzione può in linea di principio essere avviata senza diffida preventiva. Questa lettera resta tuttavia utile: formalizza il credito, fissa un termine chiaro e può facilitare una composizione amichevole prima di sostenere le spese e le pratiche di un'esecuzione."},
                {"q": "Quale termine di grazia concedere?",
                 "a": "La legge non fissa un termine minimo; nella pratica è comune un termine da 10 a 30 giorni. Adattatelo alla natura del credito e al vostro rapporto con il debitore."},
                {"q": "Cosa fare se il debitore non paga entro il termine fissato?",
                 "a": "Potete allora avviare un'esecuzione presso l'ufficio d'esecuzione competente, oppure consultare un avvocato se il credito è contestato o complesso."},
            ],
        },
        "en": {
            "slug": "free-formal-notice-letter",
            "title": "Free formal-notice (mise en demeure) letter generator",
            "meta": "Free tool: generate your formal notice letter demanding payment, with a grace period and a reminder of the statutory default interest (art. 102/104 CO).",
            "sections": [
                {"heading": "An often-necessary step before debt collection", "paragraphs": [
                    "Under Swiss law, a debtor is put in default by the creditor's formal notice (art. 102 CO), unless a performance date has already been set by agreement — in which case default occurs automatically once that date passes. A written formal notice, with a reasonable grace period, is a simple but often useful step before starting a debt-collection proceeding: it formalises the claim, sets a clear deadline, and prepares the file in case of a later dispute.",
                    "From the formal notice onward, statutory default interest of 5% per year is owed on the amount claimed, unless a different contractual rate applies (art. 104 CO). This generator includes that reminder in the letter it produces.",
                ]},
            ],
            "faq": [
                {"q": "Is this generator free?",
                 "a": "Yes, completely free and with no registration. It produces a ready-to-review letter for you to complete and sign."},
                {"q": "Is a formal notice mandatory before debt collection?",
                 "a": "No, debt-collection proceedings can generally be started without a prior formal notice. This letter remains useful, though: it formalises the claim, sets a clear deadline, and can help reach an amicable settlement before the cost and effort of a collection proceeding."},
                {"q": "What grace period should I grant?",
                 "a": "The law sets no minimum period; 10 to 30 days is common in practice. Adjust it to the nature of the claim and your relationship with the debtor."},
                {"q": "What if the debtor doesn't pay within the set period?",
                 "a": "You can then start debt-collection proceedings with the competent debt-enforcement office, or consult a lawyer if the claim is disputed or complex."},
            ],
        },
    },
    "calcul-delai-licenciement": {
        "fr": {
            "slug": "calculateur-delai-licenciement-gratuit",
            "title": "Calculateur gratuit du délai de préavis de licenciement",
            "meta": "Outil gratuit : calculez le délai de préavis de licenciement selon votre ancienneté et la date de fin des rapports de travail (art. 335b/335c CO).",
            "sections": [
                {"heading": "Un délai qui dépend de l'ancienneté", "paragraphs": [
                    "En droit suisse, le délai de préavis pour résilier un contrat de travail dépend de l'ancienneté du travailleur. Durant le temps d'essai, le délai est de 7 jours et le congé peut prendre effet n'importe quel jour (art. 335b CO). Après le temps d'essai, le délai est en principe d'un mois durant la première année de service, de deux mois de la deuxième à la neuvième année, et de trois mois dès la dixième année — toujours pour la fin d'un mois, sauf accord contraire (art. 335c CO).",
                    "Ces délais sont des minimums légaux : un contrat individuel, un contrat-type de travail ou une convention collective peut prévoir des délais plus longs, jamais plus courts sauf exception prévue par la loi.",
                ]},
            ],
            "faq": [
                {"q": "Cet outil est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription."},
                {"q": "Comment savoir si je suis encore en temps d'essai ?",
                 "a": "Le temps d'essai est en principe le premier mois de service, mais peut être prolongé jusqu'à trois mois par accord écrit, contrat-type de travail ou convention collective. Vérifiez votre contrat de travail pour connaître sa durée exacte."},
                {"q": "Le congé doit-il toujours être donné pour la fin d'un mois ?",
                 "a": "Oui, après le temps d'essai, sauf accord contraire entre les parties (art. 335c al. 1 CO). Ce calculateur applique automatiquement cette règle en arrondissant à la fin du mois."},
                {"q": "Ce résultat s'applique-t-il en cas de licenciement immédiat pour justes motifs ?",
                 "a": "Non. Le licenciement immédiat pour justes motifs (art. 337 CO) ne suit pas ces délais et répond à des conditions strictes et exceptionnelles. Consultez un avocat en droit du travail dans ce cas."},
            ],
        },
        "de": {
            "slug": "kostenloser-kuendigungsfristrechner-arbeit",
            "title": "Kostenloser Rechner für die Kündigungsfrist im Arbeitsverhältnis",
            "meta": "Kostenloses Tool: Berechnen Sie die Kündigungsfrist nach Ihren Dienstjahren und dem Ende des Arbeitsverhältnisses (Art. 335b/335c OR).",
            "sections": [
                {"heading": "Eine von den Dienstjahren abhängige Frist", "paragraphs": [
                    "Nach schweizerischem Recht hängt die Kündigungsfrist für einen Arbeitsvertrag von den Dienstjahren der Arbeitnehmerin bzw. des Arbeitnehmers ab. Während der Probezeit beträgt die Frist 7 Tage, und die Kündigung kann auf jeden beliebigen Tag wirksam werden (Art. 335b OR). Nach der Probezeit beträgt die Frist grundsätzlich einen Monat im ersten Dienstjahr, zwei Monate vom zweiten bis zum neunten Dienstjahr und drei Monate ab dem zehnten Dienstjahr — stets auf ein Monatsende, sofern nichts anderes vereinbart ist (Art. 335c OR).",
                    "Diese Fristen sind gesetzliche Minima: Ein Einzelarbeitsvertrag, ein Normalarbeitsvertrag oder ein Gesamtarbeitsvertrag kann längere Fristen vorsehen, nie kürzere, ausser bei einer vom Gesetz vorgesehenen Ausnahme.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieses Tool kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung."},
                {"q": "Wie weiss ich, ob ich noch in der Probezeit bin?",
                 "a": "Die Probezeit ist grundsätzlich der erste Monat des Dienstverhältnisses, kann aber durch schriftliche Vereinbarung, Normalarbeitsvertrag oder Gesamtarbeitsvertrag auf bis zu drei Monate verlängert werden. Prüfen Sie Ihren Arbeitsvertrag, um die genaue Dauer zu erfahren."},
                {"q": "Muss die Kündigung immer auf ein Monatsende erfolgen?",
                 "a": "Ja, nach der Probezeit, sofern die Parteien nichts anderes vereinbart haben (Art. 335c Abs. 1 OR). Dieser Rechner wendet diese Regel automatisch an, indem er auf das Monatsende aufrundet."},
                {"q": "Gilt dieses Ergebnis auch bei einer fristlosen Kündigung aus wichtigem Grund?",
                 "a": "Nein. Die fristlose Kündigung aus wichtigem Grund (Art. 337 OR) folgt nicht diesen Fristen und unterliegt strengen, aussergewöhnlichen Voraussetzungen. Konsultieren Sie in diesem Fall eine auf Arbeitsrecht spezialisierte Anwältin bzw. einen Anwalt."},
            ],
        },
        "it": {
            "slug": "calcolatore-termine-disdetta-lavoro-gratuito",
            "title": "Calcolatore gratuito del termine di disdetta del rapporto di lavoro",
            "meta": "Strumento gratuito: calcolate il termine di disdetta secondo la vostra anzianità e la data di fine del rapporto di lavoro (art. 335b/335c CO).",
            "sections": [
                {"heading": "Un termine che dipende dall'anzianità", "paragraphs": [
                    "Secondo il diritto svizzero, il termine di disdetta di un contratto di lavoro dipende dall'anzianità del lavoratore. Durante il tempo di prova, il termine è di 7 giorni e la disdetta può avere effetto in qualsiasi giorno (art. 335b CO). Dopo il tempo di prova, il termine è di norma di un mese durante il primo anno di servizio, di due mesi dal secondo al nono anno, e di tre mesi dal decimo anno — sempre per la fine di un mese, salvo diverso accordo (art. 335c CO).",
                    "Questi termini sono minimi legali: un contratto individuale, un contratto normale di lavoro o un contratto collettivo può prevedere termini più lunghi, mai più brevi salvo eccezione prevista dalla legge.",
                ]},
            ],
            "faq": [
                {"q": "Questo strumento è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione."},
                {"q": "Come faccio a sapere se sono ancora in tempo di prova?",
                 "a": "Il tempo di prova è di norma il primo mese di servizio, ma può essere prolungato fino a tre mesi mediante accordo scritto, contratto normale di lavoro o contratto collettivo. Verificate il vostro contratto di lavoro per conoscerne la durata esatta."},
                {"q": "La disdetta deve sempre essere data per la fine di un mese?",
                 "a": "Sì, dopo il tempo di prova, salvo diverso accordo tra le parti (art. 335c cpv. 1 CO). Questo calcolatore applica automaticamente questa regola arrotondando alla fine del mese."},
                {"q": "Questo risultato si applica in caso di licenziamento immediato per gravi motivi?",
                 "a": "No. Il licenziamento immediato per gravi motivi (art. 337 CO) non segue questi termini e risponde a condizioni rigorose ed eccezionali. In questo caso consultate un avvocato specializzato in diritto del lavoro."},
            ],
        },
        "en": {
            "slug": "free-employment-notice-period-calculator",
            "title": "Free employment notice-period calculator",
            "meta": "Free tool: calculate the notice period for a dismissal based on seniority and the end date of employment (art. 335b/335c CO).",
            "sections": [
                {"heading": "A period that depends on seniority", "paragraphs": [
                    "Under Swiss law, the notice period for terminating an employment contract depends on the employee's seniority. During the trial period, the notice period is 7 days and notice can take effect on any day (art. 335b CO). After the trial period, the notice period is generally one month during the first year of service, two months from the second to the ninth year, and three months from the tenth year onward — always for the end of a month, unless otherwise agreed (art. 335c CO).",
                    "These are minimum legal periods: an individual contract, a standard employment contract, or a collective bargaining agreement may set longer periods, never shorter ones except for an exception the law allows.",
                ]},
            ],
            "faq": [
                {"q": "Is this tool free?",
                 "a": "Yes, completely free and with no registration."},
                {"q": "How do I know if I'm still within the trial period?",
                 "a": "The trial period is generally the first month of service, but can be extended up to three months by written agreement, standard employment contract, or collective bargaining agreement. Check your employment contract for its exact duration."},
                {"q": "Does notice always have to be given for the end of a month?",
                 "a": "Yes, after the trial period, unless the parties agree otherwise (art. 335c para. 1 CO). This calculator automatically applies this rule by rounding up to the end of the month."},
                {"q": "Does this result apply to an immediate dismissal for cause?",
                 "a": "No. Immediate dismissal for cause (art. 337 CO) does not follow these notice periods and is subject to strict, exceptional conditions. Consult a lawyer specialising in employment law in that case."},
            ],
        },
    },
    "calcul-delai-recours-administratif": {
        "fr": {
            "slug": "calculateur-delai-recours-administratif-gratuit",
            "title": "Calculateur gratuit du délai de recours administratif",
            "meta": "Outil gratuit : calculez l'échéance de votre délai de recours contre une décision administrative fédérale, féries incluses (art. 20/22a PA).",
            "sections": [
                {"heading": "Les mêmes féries que devant les tribunaux civils", "paragraphs": [
                    "Pour recourir contre une décision d'une autorité administrative fédérale, le délai indiqué dans la décision (souvent 30 jours) court dès le lendemain de la notification et peut être suspendu par les féries judiciaires. La loi fédérale sur la procédure administrative (PA) reprend exactement les mêmes trois périodes de féries que le Code de procédure civile : du 7e jour avant Pâques au 7e jour après Pâques, du 15 juillet au 15 août, et du 18 décembre au 2 janvier (art. 22a PA).",
                    "Ces féries ne s'appliquent toutefois pas aux procédures d'effet suspensif, de mesures provisionnelles ou de marchés publics, qui exigent une décision rapide (art. 22a al. 2 PA). Vérifiez si votre recours entre dans l'une de ces catégories avant d'utiliser ce calculateur.",
                ]},
            ],
            "faq": [
                {"q": "Cet outil est-il gratuit ?",
                 "a": "Oui, entièrement gratuit et sans inscription."},
                {"q": "Où trouver la durée exacte du délai de recours ?",
                 "a": "Elle est indiquée dans la décision elle-même, dans la rubrique des voies de droit (« indication des voies de recours »), ou dans la loi spéciale applicable à votre cas. Ce calculateur ne devine jamais cette durée : vous devez la saisir vous-même."},
                {"q": "Ce calculateur s'applique-t-il aux décisions cantonales ?",
                 "a": "Il applique les féries fédérales de la PA. Si l'autorité qui a rendu la décision est cantonale, des règles de procédure cantonales spécifiques peuvent s'appliquer : vérifiez-les séparément."},
                {"q": "Que se passe-t-il si mon recours porte sur l'effet suspensif ou des mesures provisionnelles ?",
                 "a": "Dans ce cas, les féries ne s'appliquent pas (art. 22a al. 2 PA) et le résultat de ce calculateur n'est pas fiable : consultez un avocat pour calculer précisément votre délai."},
            ],
        },
        "de": {
            "slug": "kostenloser-verwaltungsbeschwerdefristrechner",
            "title": "Kostenloser Rechner für die Verwaltungsbeschwerdefrist",
            "meta": "Kostenloses Tool: Berechnen Sie den Ablauf Ihrer Beschwerdefrist gegen eine eidgenössische Verwaltungsverfügung, Gerichtsferien inbegriffen (Art. 20/22a VwVG).",
            "sections": [
                {"heading": "Dieselben Gerichtsferien wie vor den Zivilgerichten", "paragraphs": [
                    "Um gegen eine Verfügung einer eidgenössischen Verwaltungsbehörde Beschwerde zu erheben, läuft die in der Verfügung angegebene Frist (oft 30 Tage) ab dem Tag nach der Eröffnung und kann durch Gerichtsferien unterbrochen werden. Das Bundesgesetz über das Verwaltungsverfahren (VwVG) übernimmt genau dieselben drei Gerichtsferien-Perioden wie die Zivilprozessordnung: vom 7. Tag vor Ostern bis zum 7. Tag nach Ostern, vom 15. Juli bis 15. August, und vom 18. Dezember bis 2. Januar (Art. 22a VwVG).",
                    "Diese Gerichtsferien gelten jedoch nicht für Verfahren betreffend aufschiebende Wirkung, vorsorgliche Massnahmen oder öffentliches Beschaffungswesen, die eine rasche Entscheidung erfordern (Art. 22a Abs. 2 VwVG). Prüfen Sie, ob Ihre Beschwerde in eine dieser Kategorien fällt, bevor Sie diesen Rechner verwenden.",
                ]},
            ],
            "faq": [
                {"q": "Ist dieses Tool kostenlos?",
                 "a": "Ja, vollständig kostenlos und ohne Anmeldung."},
                {"q": "Wo finde ich die genaue Dauer der Beschwerdefrist?",
                 "a": "Sie steht in der Verfügung selbst, in der Rechtsmittelbelehrung, oder im auf Ihren Fall anwendbaren Spezialgesetz. Dieser Rechner errät diese Dauer nie: Sie müssen sie selbst eingeben."},
                {"q": "Gilt dieser Rechner auch für kantonale Verfügungen?",
                 "a": "Er wendet die eidgenössischen Gerichtsferien des VwVG an. Wenn die verfügende Behörde kantonal ist, können besondere kantonale Verfahrensregeln gelten: Prüfen Sie diese separat."},
                {"q": "Was, wenn meine Beschwerde die aufschiebende Wirkung oder vorsorgliche Massnahmen betrifft?",
                 "a": "In diesem Fall gelten die Gerichtsferien nicht (Art. 22a Abs. 2 VwVG), und das Ergebnis dieses Rechners ist nicht zuverlässig: Konsultieren Sie eine Anwältin bzw. einen Anwalt, um Ihre Frist präzise zu berechnen."},
            ],
        },
        "it": {
            "slug": "calcolatore-termine-ricorso-amministrativo-gratuito",
            "title": "Calcolatore gratuito del termine di ricorso amministrativo",
            "meta": "Strumento gratuito: calcolate la scadenza del vostro termine di ricorso contro una decisione amministrativa federale, sospensione feriale inclusa (art. 20/22a PA).",
            "sections": [
                {"heading": "La stessa sospensione feriale dei tribunali civili", "paragraphs": [
                    "Per ricorrere contro una decisione di un'autorità amministrativa federale, il termine indicato nella decisione (spesso 30 giorni) decorre dal giorno successivo alla notifica e può essere sospeso dalla sospensione feriale. La legge federale sulla procedura amministrativa (PA) riprende esattamente gli stessi tre periodi di sospensione feriale del Codice di procedura civile: dal 7° giorno prima di Pasqua al 7° giorno dopo Pasqua, dal 15 luglio al 15 agosto, e dal 18 dicembre al 2 gennaio (art. 22a PA).",
                    "Questa sospensione feriale non si applica tuttavia alle procedure di effetto sospensivo, misure cautelari o appalti pubblici, che richiedono una decisione rapida (art. 22a cpv. 2 PA). Verificate se il vostro ricorso rientra in una di queste categorie prima di utilizzare questo calcolatore.",
                ]},
            ],
            "faq": [
                {"q": "Questo strumento è gratuito?",
                 "a": "Sì, completamente gratuito e senza registrazione."},
                {"q": "Dove trovo la durata esatta del termine di ricorso?",
                 "a": "È indicata nella decisione stessa, nella rubrica dei rimedi giuridici, oppure nella legge speciale applicabile al vostro caso. Questo calcolatore non ipotizza mai questa durata: dovete inserirla voi stessi."},
                {"q": "Questo calcolatore si applica anche alle decisioni cantonali?",
                 "a": "Applica la sospensione feriale federale della PA. Se l'autorità che ha emesso la decisione è cantonale, possono applicarsi regole procedurali cantonali specifiche: verificatele separatamente."},
                {"q": "Cosa succede se il mio ricorso riguarda l'effetto sospensivo o misure cautelari?",
                 "a": "In tal caso, la sospensione feriale non si applica (art. 22a cpv. 2 PA) e il risultato di questo calcolatore non è affidabile: consultate un avvocato per calcolare con precisione il vostro termine."},
            ],
        },
        "en": {
            "slug": "free-administrative-appeal-deadline-calculator",
            "title": "Free administrative-appeal deadline calculator",
            "meta": "Free tool: calculate the deadline for your appeal against a federal administrative decision, including court recess periods (art. 20/22a PA).",
            "sections": [
                {"heading": "The same court recess periods as before civil courts", "paragraphs": [
                    "To appeal a federal administrative authority's decision, the deadline stated in the decision (often 30 days) runs from the day after notification and can be suspended by court recess periods. The Federal Act on Administrative Procedure (PA) uses exactly the same three recess periods as the Code of Civil Procedure: from the 7th day before Easter to the 7th day after Easter, from 15 July to 15 August, and from 18 December to 2 January (art. 22a PA).",
                    "These recess periods do not apply, however, to proceedings on suspensive effect, provisional measures, or public procurement, which require a swift decision (art. 22a para. 2 PA). Check whether your appeal falls into one of these categories before using this calculator.",
                ]},
            ],
            "faq": [
                {"q": "Is this tool free?",
                 "a": "Yes, completely free and with no registration."},
                {"q": "Where can I find the exact length of the appeal deadline?",
                 "a": "It is stated in the decision itself, in the section on legal remedies, or in the special law applicable to your case. This calculator never guesses this length: you must enter it yourself."},
                {"q": "Does this calculator apply to cantonal decisions?",
                 "a": "It applies the federal court recess periods of the PA. If the authority that issued the decision is cantonal, specific cantonal procedural rules may apply: check those separately."},
                {"q": "What if my appeal concerns suspensive effect or provisional measures?",
                 "a": "In that case, the recess periods do not apply (art. 22a para. 2 PA) and the result of this calculator is not reliable: consult a lawyer to calculate your deadline precisely."},
            ],
        },
    },
}
