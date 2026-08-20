# -*- coding: utf-8 -*-
"""Contenu de l'offre "site web gratuit" et du contrat associe, presentes a
l'avocat juste apres la creation de son compte (voir
templates/verification_demande.html), avant que son identite ne soit
validee. Meme principe que verification_content.py : contenu statique
versionne dans le depot, traduit en 4 langues, consomme par build.py.

IMPORTANT (non-juridique) : ce contrat est un premier jet redige par une IA,
pas par un avocat. Il couvre les points demandes par Gregoire Giuliano
(gratuite, controle total du site par Legatis, modifications payantes, nom
de domaine a la charge de l'avocat, backlinks, transmission de leads a
d'autres entites) mais DOIT etre relu par un avocat suisse specialise avant
toute utilisation reelle, en particulier parce que le public cible (des
avocats) est particulierement susceptible d'en contester les clauses les
plus favorables au prestataire (controle unilateral, suppression du site,
revente/partage de leads). Les traductions DE/IT/EN sont des traductions
non-juridiques du texte francais, fournies pour permettre le deploiement
multilingue du site ; en cas de divergence, la version francaise fait foi
jusqu'a validation juridique formelle -- voir le champ contract_version
utilise pour horodater/tracer la version acceptee (api/verification-request.js,
supabase_schema.sql)."""

CONTRACT_VERSION = "2026-08-20-v1"

# -- Ecran d'offre (avant le contrat) --------------------------------------

OFFER = {
    "fr": {
        "eyebrow": "Offre exclusive Legatis",
        "title": "Et si Legatis vous offrait votre site internet ?",
        "hook": "Avant de finaliser votre demande, une dernière chose : nous aimerions vous offrir la création complète de votre site internet professionnel — entièrement, totalement gratuitement.",
        "why_title": "Pourquoi gratuitement ?",
        "why_text": "Legatis veut moderniser la profession d'avocat en Suisse. Trop d'avocats compétents n'ont aujourd'hui aucune présence en ligne digne de ce nom, faute de temps ou de budget. En créant votre site sans frais, nous vous offrons cette vitrine professionnelle — et en retour, cela nous permet de faire connaître Legatis. C'est un échange gagnant-gagnant, pas un cadeau sans contrepartie : les conditions précises figurent dans le contrat que nous vous présenterons si vous êtes intéressé(e).",
        "points_title": "Ce que ça change concrètement",
        "point_1_title": "Un site clé en main",
        "point_1_text": "Nous concevons, mettons en ligne et hébergeons votre site professionnel, sans que vous n'ayez rien à gérer techniquement.",
        "point_2_title": "Zéro coût de création",
        "point_2_text": "La conception initiale est entièrement gratuite. Seul le nom de domaine (si vous en souhaitez un dédié) reste à votre charge.",
        "point_3_title": "Des règles claires et transparentes",
        "point_3_text": "Un contrat complet précise qui fait quoi : Legatis garde la main sur le site et peut le faire évoluer, les modifications spécifiques que vous demandez sont facturées, et Legatis peut valoriser le site (liens, mise en relation avec des clients).",
        "decline_note": "Aucune obligation : vous pouvez continuer votre demande de vérification sans donner suite à cette offre, à tout moment.",
        "cta_accept": "Je veux un site GRATUIT",
        "cta_decline": "Je ne veux pas, merci",
        "contract_title": "Contrat de création de site internet gratuit",
        "contract_intro": "Merci de lire ce contrat dans son intégralité. Vous devez faire défiler le texte jusqu'en bas pour pouvoir l'accepter.",
        "contract_scroll_hint": "Continuez à faire défiler pour lire l'intégralité du contrat...",
        "contract_reached_end": "Vous avez atteint la fin du contrat. Vous pouvez maintenant l'accepter ou le refuser.",
        "contract_checkbox": "J'ai lu et j'accepte l'intégralité des termes de ce contrat de création de site internet gratuit.",
        "contract_accept": "J'accepte et je continue ma demande",
        "contract_decline": "Refuser et continuer sans le site gratuit",
        "contract_error_not_scrolled": "Merci de faire défiler l'intégralité du contrat avant de l'accepter.",
        "contract_error_not_checked": "Merci de cocher la case de confirmation.",
        "recorded_accept_note": "Votre acceptation est enregistrée avec votre demande, horodatée, avec la version du contrat concernée.",
        "recorded_decline_note": "Votre choix (sans le site gratuit) est enregistré avec votre demande.",
        "back_to_form": "Retour",
    },
    "de": {
        "eyebrow": "Exklusives Legatis-Angebot",
        "title": "Was, wenn Legatis Ihnen Ihre Website schenkt?",
        "hook": "Bevor Sie Ihre Anfrage abschliessen, noch etwas: Wir möchten Ihnen die vollständige Erstellung Ihrer professionellen Website anbieten — vollständig, komplett kostenlos.",
        "why_title": "Warum kostenlos?",
        "why_text": "Legatis möchte den Anwaltsberuf in der Schweiz modernisieren. Zu viele kompetente Anwältinnen und Anwälte haben heute keine würdige Online-Präsenz, aus Zeit- oder Budgetmangel. Indem wir Ihre Website kostenlos erstellen, bieten wir Ihnen dieses professionelle Schaufenster — und im Gegenzug ermöglicht uns das, Legatis bekannt zu machen. Es ist ein Win-win-Austausch, kein Geschenk ohne Gegenleistung: Die genauen Bedingungen finden Sie im Vertrag, den wir Ihnen vorlegen, falls Sie interessiert sind.",
        "points_title": "Was sich konkret ändert",
        "point_1_title": "Eine schlüsselfertige Website",
        "point_1_text": "Wir gestalten, veröffentlichen und hosten Ihre professionelle Website, ohne dass Sie technisch etwas verwalten müssen.",
        "point_2_title": "Null Erstellungskosten",
        "point_2_text": "Die Erstgestaltung ist vollständig kostenlos. Nur die Domain (falls Sie eine dedizierte wünschen) bleibt zu Ihren Lasten.",
        "point_3_title": "Klare und transparente Regeln",
        "point_3_text": "Ein vollständiger Vertrag legt fest, wer was tut: Legatis behält die Kontrolle über die Website und kann sie weiterentwickeln, spezifische von Ihnen gewünschte Änderungen werden verrechnet, und Legatis kann die Website wirtschaftlich nutzen (Links, Vermittlung von Kunden).",
        "decline_note": "Keine Verpflichtung: Sie können Ihre Verifizierungsanfrage jederzeit fortsetzen, ohne auf dieses Angebot einzugehen.",
        "cta_accept": "Ich möchte eine KOSTENLOSE Website",
        "cta_decline": "Nein danke",
        "contract_title": "Vertrag über die kostenlose Erstellung einer Website",
        "contract_intro": "Bitte lesen Sie diesen Vertrag vollständig. Sie müssen den Text bis zum Ende durchscrollen, um ihn akzeptieren zu können.",
        "contract_scroll_hint": "Scrollen Sie weiter, um den gesamten Vertrag zu lesen...",
        "contract_reached_end": "Sie haben das Ende des Vertrags erreicht. Sie können ihn nun annehmen oder ablehnen.",
        "contract_checkbox": "Ich habe den vollständigen Vertrag über die kostenlose Website-Erstellung gelesen und akzeptiere ihn.",
        "contract_accept": "Ich akzeptiere und setze meine Anfrage fort",
        "contract_decline": "Ablehnen und ohne die kostenlose Website fortfahren",
        "contract_error_not_scrolled": "Bitte scrollen Sie den gesamten Vertrag durch, bevor Sie ihn akzeptieren.",
        "contract_error_not_checked": "Bitte kreuzen Sie das Bestätigungsfeld an.",
        "recorded_accept_note": "Ihre Zustimmung wird mit Ihrer Anfrage, zeitgestempelt und mit der betreffenden Vertragsversion, gespeichert.",
        "recorded_decline_note": "Ihre Wahl (ohne die kostenlose Website) wird mit Ihrer Anfrage gespeichert.",
        "back_to_form": "Zurück",
    },
    "it": {
        "eyebrow": "Offerta esclusiva Legatis",
        "title": "E se Legatis vi offrisse il vostro sito internet?",
        "hook": "Prima di completare la vostra richiesta, un'ultima cosa: vorremmo offrirvi la creazione completa del vostro sito internet professionale — interamente, del tutto gratuitamente.",
        "why_title": "Perché gratuitamente?",
        "why_text": "Legatis vuole modernizzare la professione forense in Svizzera. Troppi avvocati competenti non hanno oggi una presenza online degna di questo nome, per mancanza di tempo o di budget. Creando il vostro sito senza costi, vi offriamo questa vetrina professionale — e in cambio, ciò ci permette di far conoscere Legatis. È uno scambio vantaggioso per entrambi, non un regalo senza contropartita: le condizioni precise figurano nel contratto che vi presenteremo se siete interessati.",
        "points_title": "Cosa cambia concretamente",
        "point_1_title": "Un sito chiavi in mano",
        "point_1_text": "Progettiamo, pubblichiamo e ospitiamo il vostro sito professionale, senza che dobbiate gestire nulla dal punto di vista tecnico.",
        "point_2_title": "Zero costi di creazione",
        "point_2_text": "La progettazione iniziale è interamente gratuita. Solo il nome di dominio (se ne desiderate uno dedicato) resta a vostro carico.",
        "point_3_title": "Regole chiare e trasparenti",
        "point_3_text": "Un contratto completo precisa chi fa cosa: Legatis mantiene il controllo del sito e può farlo evolvere, le modifiche specifiche che richiedete sono fatturate, e Legatis può valorizzare il sito (link, messa in contatto con clienti).",
        "decline_note": "Nessun obbligo: potete continuare la vostra richiesta di verifica senza aderire a questa offerta, in qualsiasi momento.",
        "cta_accept": "Voglio un sito GRATUITO",
        "cta_decline": "Non lo voglio, grazie",
        "contract_title": "Contratto di creazione di un sito internet gratuito",
        "contract_intro": "Vi preghiamo di leggere questo contratto nella sua integralità. Dovete scorrere il testo fino in fondo per poterlo accettare.",
        "contract_scroll_hint": "Continuate a scorrere per leggere l'intero contratto...",
        "contract_reached_end": "Avete raggiunto la fine del contratto. Ora potete accettarlo o rifiutarlo.",
        "contract_checkbox": "Ho letto e accetto integralmente i termini di questo contratto di creazione di un sito internet gratuito.",
        "contract_accept": "Accetto e continuo la mia richiesta",
        "contract_decline": "Rifiutare e continuare senza il sito gratuito",
        "contract_error_not_scrolled": "Vi preghiamo di scorrere l'intero contratto prima di accettarlo.",
        "contract_error_not_checked": "Vi preghiamo di spuntare la casella di conferma.",
        "recorded_accept_note": "La vostra accettazione viene registrata con la vostra richiesta, con data e ora, e con la versione del contratto interessata.",
        "recorded_decline_note": "La vostra scelta (senza il sito gratuito) viene registrata con la vostra richiesta.",
        "back_to_form": "Indietro",
    },
    "en": {
        "eyebrow": "Exclusive Legatis offer",
        "title": "What if Legatis built your website for you?",
        "hook": "Before you finalize your request, one more thing: we'd like to offer you the complete creation of your professional website — entirely, completely free of charge.",
        "why_title": "Why free?",
        "why_text": "Legatis wants to modernize the legal profession in Switzerland. Too many competent lawyers today have no proper online presence, for lack of time or budget. By building your website at no cost, we give you this professional showcase — and in return, this lets us make Legatis known. It's a win-win exchange, not a gift with no return: the precise terms are set out in the contract we'll present to you if you're interested.",
        "points_title": "What this means concretely",
        "point_1_title": "A turnkey website",
        "point_1_text": "We design, publish, and host your professional website, with nothing for you to manage technically.",
        "point_2_title": "Zero creation cost",
        "point_2_text": "The initial design is entirely free. Only the domain name (if you want a dedicated one) remains your responsibility.",
        "point_3_title": "Clear, transparent rules",
        "point_3_text": "A complete contract sets out who does what: Legatis keeps control of the site and can develop it further, specific changes you request are billed, and Legatis may derive value from the site (links, referring clients to you).",
        "decline_note": "No obligation: you can continue your verification request without taking up this offer, at any time.",
        "cta_accept": "I want a FREE website",
        "cta_decline": "No thanks",
        "contract_title": "Free website creation contract",
        "contract_intro": "Please read this contract in full. You must scroll through the entire text to be able to accept it.",
        "contract_scroll_hint": "Keep scrolling to read the full contract...",
        "contract_reached_end": "You have reached the end of the contract. You can now accept or decline it.",
        "contract_checkbox": "I have read and accept the entirety of the terms of this free website creation contract.",
        "contract_accept": "I accept and continue my request",
        "contract_decline": "Decline and continue without the free website",
        "contract_error_not_scrolled": "Please scroll through the entire contract before accepting it.",
        "contract_error_not_checked": "Please check the confirmation box.",
        "recorded_accept_note": "Your acceptance is recorded with your request, timestamped, along with the relevant contract version.",
        "recorded_decline_note": "Your choice (without the free website) is recorded with your request.",
        "back_to_form": "Back",
    },
}

# -- Contrat complet --------------------------------------------------------
#
# Structure : chaque langue a "title", "preamble" (liste de paragraphes) et
# "articles" (liste de {"heading": ..., "paragraphs": [...]}). Rendu tel
# quel par templates/website_offer_contract.html (partial inclus dans
# verification_demande.html), qui gere le defilement obligatoire avant
# activation de la case a cocher + bouton d'acceptation.

CONTRACT = {
    "fr": {
        "title": "Contrat de création et de gestion gratuite d'un site internet professionnel",
        "parties_label": "Entre Legatis, plateforme suisse de référencement d'avocats exploitée à titre individuel par Monsieur Grégoire Giuliano (ci-après « Legatis » ou le « Prestataire »), et l'avocat ou l'avocate identifié(e) par la demande de vérification à laquelle ce contrat est joint (ci-après l'« Avocat » ou le « Client »), ci-après ensemble les « Parties ».",
        "preamble": [
            "Legatis exploite un annuaire en ligne d'avocats en Suisse ainsi que, pour les avocats qui le souhaitent, un service de création et d'hébergement de site internet professionnel individuel. Le présent contrat (ci-après le « Contrat ») a pour objet de définir les conditions dans lesquelles Legatis fournit gratuitement ce service au Client, ainsi que les droits que le Client concède à Legatis en contrepartie.",
            "Legatis poursuit un objectif de modernisation de la profession d'avocat en Suisse : de nombreux avocats compétents, en particulier dans des études de taille modeste ou exerçant seuls, ne disposent aujourd'hui d'aucune présence en ligne professionnelle satisfaisante, faute de temps, de compétences techniques ou de budget dédié. En mettant à disposition gratuitement la conception, la mise en ligne et l'hébergement technique d'un site internet, Legatis entend combler ce manque et contribuer à une meilleure visibilité numérique de la profession.",
            "Cette prestation gratuite n'est pas dénuée de contrepartie pour Legatis : elle lui permet de faire connaître sa marque, d'élargir son audience, de démontrer son savoir-faire technique auprès de la profession, et de développer son activité de mise en relation entre avocats et justiciables. Le Client reconnaît et accepte expressément que cette contrepartie, décrite en détail aux articles suivants, constitue la cause économique du caractère gratuit de la prestation initiale.",
            "Le Client déclare avoir pris connaissance de l'intégralité du présent Contrat avant de l'accepter, avoir eu la possibilité de poser toute question à Legatis avant son acceptation, et accepter le Contrat en toute connaissance de cause, sans y être contraint par ailleurs : l'acceptation du présent Contrat est entièrement facultative et son refus n'a aucune incidence sur la poursuite de la demande de vérification d'identité et de création de compte sur Legatis, ni sur la présence du Client dans l'annuaire Legatis.",
        ],
        "articles": [
            {
                "heading": "Article 1 — Définitions",
                "paragraphs": [
                    "« Site » désigne le site internet individuel conçu, développé et mis en ligne par Legatis pour le compte du Client dans le cadre du présent Contrat, comprenant sa structure, son design, son code, ainsi que son contenu tel que fourni ou approuvé par le Client.",
                    "« Prestation initiale » désigne la conception graphique, le développement technique et la mise en ligne initiale du Site, fournis gratuitement par Legatis conformément à l'article 3.",
                    "« Modifications » désigne toute intervention sur le Site postérieure à sa mise en ligne initiale, qu'elle soit demandée par le Client ou décidée par Legatis de sa propre initiative.",
                    "« Nom de domaine » désigne l'adresse internet (par exemple « www.nom-du-cabinet.ch ») sous laquelle le Site est accessible au public.",
                    "« Lead » désigne toute demande de contact, message, prise de rendez-vous ou coordonnées transmises par un visiteur du Site ou de l'annuaire Legatis, susceptible de constituer une opportunité commerciale pour le Client ou pour un tiers.",
                    "« Entités tierces » ou « partenaires » désigne toute personne physique ou morale, autre que le Client et Legatis, avec laquelle Legatis entretient une relation commerciale ou de partenariat, y compris d'autres avocats, études, ou services juridiques ou non juridiques.",
                ],
            },
            {
                "heading": "Article 2 — Objet du Contrat",
                "paragraphs": [
                    "Le présent Contrat a pour objet de définir les conditions dans lesquelles Legatis fournit au Client la Prestation initiale décrite à l'article 4, ainsi que les droits d'exploitation, de gestion, de modification et de valorisation que le Client concède à Legatis sur le Site en contrepartie de cette gratuité.",
                    "Le présent Contrat est distinct et indépendant de l'inscription du Client à l'annuaire Legatis et de la procédure de vérification d'identité qui l'accompagne. Le refus du présent Contrat n'affecte en rien l'inscription du Client à l'annuaire Legatis ni son compte de connexion.",
                ],
            },
            {
                "heading": "Article 3 — Gratuité de la Prestation initiale",
                "paragraphs": [
                    "La Prestation initiale, telle que décrite à l'article 4, est fournie par Legatis au Client sans contrepartie financière directe. Aucun montant n'est facturé au Client pour la conception, le développement et la mise en ligne initiale du Site.",
                    "Cette gratuité ne s'étend pas aux éléments expressément exclus par le présent Contrat, notamment le Nom de domaine (article 8) et les Modifications demandées par le Client postérieurement à la mise en ligne initiale (article 7), qui font l'objet d'une facturation distincte selon les modalités décrites ci-après.",
                    "Legatis se réserve le droit de mettre fin à la gratuité de tout ou partie de ses services pour les nouveaux clients à tout moment, sans que cela n'affecte les conditions applicables aux Sites déjà mis en ligne au moment de ce changement, sauf accord contraire des Parties.",
                ],
            },
            {
                "heading": "Article 4 — Description de la Prestation initiale",
                "paragraphs": [
                    "La Prestation initiale comprend : (i) un entretien ou échange préalable avec le Client afin de recueillir ses informations professionnelles, son contenu textuel, ses éventuelles photographies et ses préférences esthétiques dans la mesure compatible avec les gabarits proposés par Legatis ; (ii) la conception graphique du Site à partir de gabarits et composants développés par Legatis ; (iii) l'intégration du contenu fourni ou validé par le Client ; (iv) la mise en ligne technique du Site sur l'infrastructure d'hébergement choisie par Legatis ; et (v) une configuration de référencement de base.",
                    "Legatis s'efforce de livrer la Prestation initiale dans un délai raisonnable après acceptation du présent Contrat, sans toutefois s'engager sur un délai précis, la Prestation initiale étant fournie à titre gratuit et n'étant, à ce titre, soumise à aucune obligation de résultat quant aux délais.",
                    "Le Client s'engage à fournir à Legatis, dans un délai raisonnable après en avoir été sollicité, l'ensemble des informations, textes, images et autorisations nécessaires à la réalisation du Site, notamment concernant le droit d'utiliser toute photographie ou tout texte qu'il transmet à Legatis.",
                ],
            },
            {
                "heading": "Article 5 — Contrôle éditorial et technique du Site",
                "paragraphs": [
                    "Le Client reconnaît et accepte que Legatis conserve, pendant toute la durée du présent Contrat, un contrôle éditorial et technique total sur le Site. À ce titre, Legatis a le droit, à sa seule discrétion et sans avoir à requérir l'accord préalable du Client, d'ajouter, de modifier, de réorganiser ou de supprimer tout ou partie du contenu, du design, de la structure ou des fonctionnalités du Site.",
                    "Ce contrôle inclut notamment le droit pour Legatis d'apporter des corrections, des mises à jour techniques ou de sécurité, des évolutions esthétiques globales appliquées à l'ensemble des sites qu'il gère pour ses clients, ainsi que toute modification que Legatis estime nécessaire à la bonne tenue, à la conformité légale ou à l'image de la plateforme Legatis dans son ensemble.",
                    "Legatis s'efforce, dans la mesure du raisonnable, d'informer le Client des modifications substantielles apportées au Site de sa propre initiative, sans toutefois que cette information constitue une condition de validité de ces modifications.",
                    "Legatis se réserve également le droit de suspendre l'accès au Site ou de le retirer intégralement de la publication, notamment en cas de manquement du Client au présent Contrat, de cessation de l'activité d'avocat du Client, de radiation du Client du barreau, de contenu illicite ou contraire à la déontologie professionnelle, de non-paiement de frais dus au titre du présent Contrat, ou de résiliation du Contrat dans les conditions de l'article 15.",
                ],
            },
            {
                "heading": "Article 6 — Ajout, modification et suppression du Site par Legatis",
                "paragraphs": [
                    "Sans préjudice de l'article 5, Legatis peut, à tout moment et à sa seule discrétion, décider de supprimer purement et simplement le Site, notamment pour des raisons techniques, commerciales, économiques ou stratégiques propres à Legatis, moyennant un préavis raisonnable adressé au Client par tout moyen utile, sauf en cas d'urgence ou de motif grave où la suppression peut être immédiate.",
                    "En cas de suppression du Site à l'initiative de Legatis pour des raisons autres qu'un manquement du Client, Legatis s'efforce, dans la mesure du possible et sans y être tenu, de fournir au Client une exportation raisonnable du contenu textuel du Site tel qu'il existait au moment de la suppression.",
                    "Le Client ne peut prétendre à aucune indemnité, de quelque nature que ce soit, du fait de l'exercice par Legatis des droits de contrôle, de modification ou de suppression décrits au présent article et à l'article 5, sous réserve des dispositions impératives du droit suisse qui ne peuvent être exclues contractuellement.",
                ],
            },
            {
                "heading": "Article 7 — Modifications demandées par le Client (prestations payantes)",
                "paragraphs": [
                    "Toute Modification du Site demandée par le Client après la mise en ligne initiale, qu'il s'agisse d'une modification de contenu, de design, de structure ou de fonctionnalité, constitue une prestation distincte de la Prestation initiale et fait l'objet d'une facturation par Legatis, sauf accord exprès contraire.",
                    "Legatis communique au Client, sur demande, un tarif ou un devis pour toute Modification sollicitée avant de procéder à sa réalisation. Aucune Modification payante n'est effectuée sans l'accord préalable du Client sur le principe et le montant de la facturation, étant précisé que cet accord préalable ne s'applique pas aux modifications que Legatis effectue de sa propre initiative en vertu de l'article 5 ou 6, lesquelles demeurent gratuites pour le Client.",
                    "Les tarifs applicables aux Modifications sont ceux communiqués par Legatis au moment de la demande, Legatis se réservant le droit de faire évoluer sa grille tarifaire à tout moment pour les demandes futures.",
                    "À défaut de paiement des sommes dues au titre des Modifications facturées, Legatis peut suspendre la réalisation de nouvelles Modifications jusqu'à régularisation, sans que cela n'affecte le maintien en ligne du Site tel qu'existant.",
                ],
            },
            {
                "heading": "Article 8 — Nom de domaine",
                "paragraphs": [
                    "Si le Client souhaite que le Site soit accessible sous un Nom de domaine dédié (par exemple le nom de son étude), l'enregistrement et le renouvellement périodique de ce Nom de domaine sont à la charge financière exclusive du Client, y compris lorsque Legatis procède techniquement à cet enregistrement pour le compte du Client par souci de simplicité.",
                    "À défaut de Nom de domaine dédié ou en cas de non-renouvellement par le Client, le Site reste ou redevient accessible sous une adresse générique fournie par Legatis (par exemple un sous-domaine du site legatis.ch), sans frais supplémentaires pour le Client.",
                    "En cas de résiliation du présent Contrat ou de suppression du Site à l'initiative de l'une ou l'autre des Parties, la titularité du Nom de domaine, s'il a été enregistré au nom du Client et payé par celui-ci, demeure acquise au Client, sous réserve du règlement de tout solde éventuellement dû.",
                ],
            },
            {
                "heading": "Article 9 — Hébergement et disponibilité",
                "paragraphs": [
                    "Legatis héberge le Site sur une infrastructure technique de son choix, qu'il peut faire évoluer ou modifier à tout moment sans que cela ne nécessite l'accord du Client, dans la mesure où le Site demeure accessible au public dans des conditions équivalentes.",
                    "Legatis met en œuvre des moyens raisonnables pour assurer une disponibilité satisfaisante du Site, sans toutefois garantir une disponibilité ininterrompue, le Site pouvant faire l'objet d'interruptions temporaires pour maintenance, mise à jour, ou pour des raisons échappant au contrôle raisonnable de Legatis (panne d'un prestataire tiers, incident de sécurité, cas de force majeure au sens de l'article 17).",
                ],
            },
            {
                "heading": "Article 10 — Référencement, liens retour et visibilité de Legatis",
                "paragraphs": [
                    "En contrepartie de la gratuité de la Prestation initiale, le Client concède à Legatis le droit d'inclure sur le Site, de manière visible, un ou plusieurs liens hypertextes (« backlinks ») renvoyant vers le site legatis.ch, vers la fiche du Client sur l'annuaire Legatis, ou vers d'autres pages ou services exploités par Legatis, ainsi qu'une mention du type « site réalisé par Legatis » ou équivalent.",
                    "Le Client autorise Legatis à mentionner et, le cas échéant, à présenter le Site (captures d'écran, extraits, lien) à titre de référence commerciale ou de démonstration de son savoir-faire, notamment auprès d'autres avocats susceptibles d'être intéressés par une prestation similaire, sous réserve du respect de la confidentialité prévue à l'article 14 pour les informations non publiques.",
                    "Le Client reconnaît que ces liens et mentions participent de la contrepartie économique justifiant la gratuité de la Prestation initiale et ne peut en demander la suppression que dans le cadre d'une résiliation du présent Contrat, laquelle emporte alors les conséquences décrites à l'article 15.",
                ],
            },
            {
                "heading": "Article 11 — Génération, gestion et transmission de leads",
                "paragraphs": [
                    "Le Site et, plus largement, l'annuaire Legatis sur lequel figure le Client sont susceptibles de générer des Leads, notamment via des formulaires de contact, des demandes de mise en relation ou des outils de comparaison mis à disposition sur le site legatis.ch.",
                    "Le Client autorise Legatis à collecter, gérer et transmettre au Client les Leads le concernant directement, dans le respect de la législation applicable en matière de protection des données (article 13).",
                    "Le Client reconnaît en outre que Legatis, dans le cadre de son activité de plateforme de mise en relation, peut orienter, partager ou transmettre à des Entités tierces des demandes, informations ou Leads qui ne concernent pas spécifiquement et exclusivement le Client — notamment lorsqu'un visiteur formule une demande générale susceptible d'intéresser plusieurs avocats, lorsque le Client n'est pas en mesure de répondre à une demande, ou dans le cadre de services complémentaires proposés par Legatis ou ses partenaires. Cette faculté ne confère au Client aucune exclusivité sur les Leads générés via l'annuaire Legatis ou le Site.",
                    "Legatis ne garantit aucun volume, aucune fréquence ni aucune qualité minimale de Leads transmis au Client, la Prestation initiale et le présent Contrat ne constituant en aucun cas un engagement de résultat commercial en faveur du Client.",
                ],
            },
            {
                "heading": "Article 12 — Propriété intellectuelle",
                "paragraphs": [
                    "Le code source, les gabarits, les composants graphiques, les fonctionnalités techniques et, plus généralement, tout élément du Site conçu ou développé par Legatis indépendamment du contenu spécifique fourni par le Client, demeurent la propriété exclusive de Legatis, y compris après la mise en ligne du Site.",
                    "Le contenu spécifique au Client (son nom, sa présentation personnelle, ses coordonnées, les textes et photographies qu'il fournit personnellement et dont il est l'auteur ou l'ayant droit) demeure la propriété du Client, sous réserve du droit d'utilisation concédé à Legatis pour les besoins de l'exécution du présent Contrat, notamment son affichage sur le Site et sur l'annuaire Legatis.",
                    "Le Client garantit à Legatis qu'il détient tous les droits nécessaires sur le contenu qu'il fournit (textes, photographies, logos) et garantit Legatis contre tout recours de tiers relatif à une atteinte à des droits de propriété intellectuelle ou de la personnalité résultant de ce contenu.",
                    "En cas de résiliation du présent Contrat, Legatis conserve le droit d'utiliser les gabarits, composants et savoir-faire techniques développés dans le cadre de la réalisation du Site pour d'autres clients, à l'exclusion du contenu spécifique et des informations personnelles propres au Client.",
                ],
            },
            {
                "heading": "Article 13 — Protection des données",
                "paragraphs": [
                    "Legatis traite les données personnelles du Client et des visiteurs du Site conformément à la loi fédérale sur la protection des données (LPD) et à sa révision (nLPD), ainsi qu'aux dispositions de la politique de confidentialité de Legatis, consultable sur le site legatis.ch.",
                    "Les données des Leads transmises au Client dans le cadre de l'article 11 ne peuvent être utilisées par celui-ci que pour les besoins de sa propre activité professionnelle, dans le respect des règles déontologiques applicables aux avocats et de la législation sur la protection des données.",
                    "Le Client demeure seul responsable, en sa qualité d'avocat, du respect du secret professionnel et des règles de protection des données applicables à sa propre activité, indépendamment des obligations de Legatis au titre du présent article.",
                ],
            },
            {
                "heading": "Article 14 — Confidentialité",
                "paragraphs": [
                    "Chaque Partie s'engage à garder confidentielles les informations non publiques dont elle aurait connaissance dans le cadre de l'exécution du présent Contrat et à ne les utiliser qu'aux fins de cette exécution, sauf accord écrit contraire ou obligation légale de divulgation.",
                    "Cette obligation de confidentialité ne fait pas obstacle à l'exercice par Legatis des droits de communication et de mise en avant du Site prévus à l'article 10, ces derniers portant par nature sur des informations rendues publiques par la mise en ligne du Site lui-même.",
                ],
            },
            {
                "heading": "Article 15 — Durée et résiliation",
                "paragraphs": [
                    "Le présent Contrat est conclu pour une durée indéterminée à compter de son acceptation par le Client, et reste en vigueur tant que le Site demeure hébergé par Legatis.",
                    "Chaque Partie peut résilier le présent Contrat à tout moment, moyennant un préavis raisonnable adressé à l'autre Partie par écrit (y compris par courrier électronique), sans avoir à justifier de motif particulier.",
                    "En cas de résiliation à l'initiative du Client, celui-ci reconnaît que le Site, en tant que réalisation technique et graphique de Legatis, cesse d'être hébergé et accessible au public par l'intermédiaire de Legatis, sans préjudice de la titularité du contenu spécifique du Client tel que défini à l'article 12.",
                    "La résiliation du présent Contrat est sans effet sur l'inscription du Client à l'annuaire Legatis et sur son compte de connexion, lesquels demeurent régis par les conditions générales d'utilisation de Legatis.",
                ],
            },
            {
                "heading": "Article 16 — Responsabilité et garanties",
                "paragraphs": [
                    "La Prestation initiale étant fournie à titre gratuit, Legatis n'est tenu, dans les limites autorisées par le droit suisse, qu'à une obligation de moyens et non de résultat, et sa responsabilité ne peut être engagée qu'en cas de faute intentionnelle ou de négligence grave.",
                    "Legatis ne garantit ni l'absence totale d'erreur, de panne ou d'indisponibilité du Site, ni un quelconque résultat commercial (nombre de visiteurs, de Leads, de nouveaux clients) découlant de la mise en ligne du Site.",
                    "En tout état de cause, la responsabilité de Legatis, si elle devait être engagée, est limitée aux dommages directs et prévisibles, à l'exclusion de tout dommage indirect (perte de clientèle, perte de chance, atteinte à l'image), et ce dans les limites autorisées par les dispositions impératives du droit suisse, notamment l'article 100 du Code des obligations relatif à la responsabilité pour dol ou faute grave qui ne peut être exclue par convention.",
                    "Le Client demeure seul responsable du contenu qu'il fournit ou approuve pour publication sur le Site, notamment de sa conformité aux règles déontologiques de la profession d'avocat et aux dispositions légales relatives à la publicité des avocats.",
                ],
            },
            {
                "heading": "Article 17 — Force majeure",
                "paragraphs": [
                    "Aucune des Parties ne peut être tenue responsable d'un manquement à ses obligations au titre du présent Contrat lorsque ce manquement résulte d'un cas de force majeure, entendu comme tout événement extérieur, imprévisible et irrésistible au sens de la jurisprudence suisse, notamment une catastrophe naturelle, une panne majeure et généralisée d'infrastructure internet, une cyberattaque de grande ampleur, ou une décision d'une autorité publique.",
                ],
            },
            {
                "heading": "Article 18 — Cession du Contrat",
                "paragraphs": [
                    "Legatis peut céder le présent Contrat, ainsi que l'ensemble des droits et obligations qui en découlent, à toute entité qui reprendrait tout ou partie de son activité, moyennant une information préalable du Client.",
                    "Le Client ne peut céder le présent Contrat à un tiers sans l'accord préalable et écrit de Legatis, le Contrat étant conclu en considération de la personne du Client en sa qualité d'avocat inscrit à l'annuaire Legatis.",
                ],
            },
            {
                "heading": "Article 19 — Modification du présent Contrat",
                "paragraphs": [
                    "Legatis peut modifier les termes du présent Contrat pour l'avenir, notamment pour tenir compte d'évolutions légales, techniques ou commerciales. Les modifications substantielles sont communiquées au Client par tout moyen utile et sont réputées acceptées si le Client ne s'y oppose pas dans un délai raisonnable ou s'il continue à bénéficier des services de Legatis après leur entrée en vigueur.",
                    "Le Client peut, s'il n'accepte pas une modification substantielle, résilier le présent Contrat dans les conditions de l'article 15.",
                ],
            },
            {
                "heading": "Article 20 — Nullité partielle",
                "paragraphs": [
                    "Si l'une des clauses du présent Contrat devait être jugée nulle, illicite ou inapplicable par une autorité compétente, les autres clauses du Contrat demeurent pleinement en vigueur. Les Parties s'efforcent alors de remplacer la clause invalidée par une clause valide dont l'effet économique se rapproche le plus possible de celui de la clause invalidée.",
                ],
            },
            {
                "heading": "Article 21 — Acceptation électronique et preuve",
                "paragraphs": [
                    "Le Client accepte le présent Contrat en faisant défiler l'intégralité de son texte, en cochant la case de confirmation prévue à cet effet, puis en cliquant sur le bouton d'acceptation prévu sur l'interface de Legatis.",
                    "Le Client reconnaît que cette acceptation électronique constitue une manifestation de volonté valable et l'engage juridiquement au même titre qu'une signature manuscrite, conformément aux principes généraux du droit suisse des contrats relatifs à la liberté de la forme (article 10 du Code des obligations), sous réserve des dispositions légales imposant une forme particulière pour certains actes.",
                    "Legatis conserve un enregistrement horodaté de l'acceptation du Client, incluant la version du Contrat acceptée, à titre de preuve.",
                ],
            },
            {
                "heading": "Article 22 — Droit applicable et for juridique",
                "paragraphs": [
                    "Le présent Contrat est soumis au droit suisse, à l'exclusion de ses règles de conflit de lois et de la Convention des Nations Unies sur les contrats de vente internationale de marchandises.",
                    "Tout litige découlant du présent Contrat ou en relation avec celui-ci relève de la compétence exclusive des tribunaux ordinaires du domicile ou du siège de Legatis, sous réserve des dispositions impératives du droit suisse prévoyant un for différent, notamment en matière de protection des consommateurs si celles-ci devaient s'appliquer.",
                ],
            },
            {
                "heading": "Article 23 — Dispositions finales",
                "paragraphs": [
                    "Le présent Contrat constitue l'intégralité de l'accord des Parties relatif à la création et à la gestion gratuite du Site, et prévaut sur tout accord ou échange antérieur portant sur le même objet, sous réserve des conditions générales d'utilisation de Legatis applicables par ailleurs à l'inscription du Client à l'annuaire.",
                    "Le fait pour l'une des Parties de ne pas se prévaloir, à un moment donné, d'un manquement de l'autre Partie à l'une des clauses du présent Contrat ne saurait être interprété comme une renonciation à se prévaloir, dans l'avenir, dudit manquement ou de toute autre clause du Contrat.",
                    "En acceptant le présent Contrat, le Client confirme avoir la capacité juridique de contracter et agir en son nom propre ou dûment habilité à engager l'entité pour le compte de laquelle il contracte, le cas échéant.",
                ],
            },
        ],
    },
    "de": {
    "title": "Vertrag über die kostenlose Erstellung und Verwaltung einer beruflichen Internetseite",
    "parties_label": "Zwischen Legatis, einer Schweizer Plattform zur Vermittlung von Anwältinnen und Anwälten, die von Herrn Grégoire Giuliano als Einzelunternehmen betrieben wird (nachfolgend „Legatis“ oder der „Dienstleister“), und der Anwältin oder dem Anwalt, die bzw. der durch den Verifizierungsantrag identifiziert wird, dem dieser Vertrag beigefügt ist (nachfolgend die „Anwältin“ bzw. der „Anwalt“ oder die „Kundin“ bzw. der „Kunde“), nachfolgend gemeinsam die „Parteien“.",
    "preamble": [
        "Legatis betreibt ein Online-Verzeichnis von Anwältinnen und Anwälten in der Schweiz sowie, für diejenigen Anwältinnen und Anwälte, die dies wünschen, einen Dienst zur Erstellung und zum Hosting einer individuellen beruflichen Internetseite. Der vorliegende Vertrag (nachfolgend der „Vertrag“) bezweckt die Festlegung der Bedingungen, unter denen Legatis dem Kunden diesen Dienst kostenlos erbringt, sowie der Rechte, die der Kunde Legatis im Gegenzug einräumt.",
        "Legatis verfolgt das Ziel, den Anwaltsberuf in der Schweiz zu modernisieren: Zahlreiche kompetente Anwältinnen und Anwälte, insbesondere in kleineren Kanzleien oder als Einzelpraktizierende, verfügen heute mangels Zeit, technischer Kompetenzen oder eines dafür vorgesehenen Budgets über keine zufriedenstellende berufliche Online-Präsenz. Indem Legatis die Konzeption, die Veröffentlichung und das technische Hosting einer Internetseite kostenlos zur Verfügung stellt, will es diese Lücke schliessen und zu einer besseren digitalen Sichtbarkeit des Berufsstands beitragen.",
        "Diese kostenlose Leistung ist für Legatis nicht ohne Gegenleistung: Sie ermöglicht es Legatis, seine Marke bekannt zu machen, sein Publikum zu erweitern, sein technisches Know-how gegenüber dem Berufsstand zu demonstrieren und seine Tätigkeit der Vermittlung zwischen Anwältinnen und Anwälten sowie Rechtsuchenden weiterzuentwickeln. Der Kunde anerkennt und akzeptiert ausdrücklich, dass diese in den nachfolgenden Artikeln im Einzelnen beschriebene Gegenleistung den wirtschaftlichen Grund für die Unentgeltlichkeit der ursprünglichen Leistung bildet.",
        "Der Kunde erklärt, den vorliegenden Vertrag vor dessen Annahme vollständig zur Kenntnis genommen zu haben, vor der Annahme die Möglichkeit gehabt zu haben, Legatis jegliche Frage zu stellen, und den Vertrag in voller Kenntnis der Sachlage anzunehmen, ohne im Übrigen dazu gezwungen zu sein: Die Annahme des vorliegenden Vertrags ist vollständig freiwillig, und ihre Ablehnung hat keinerlei Auswirkung auf die Fortsetzung des Antrags auf Identitätsverifizierung und Kontoerstellung bei Legatis noch auf die Präsenz des Kunden im Verzeichnis von Legatis."
    ],
    "articles": [
        {"heading": "Artikel 1 — Begriffsbestimmungen", "paragraphs": [
            "„Internetseite“ bezeichnet die individuelle Internetseite, die von Legatis im Rahmen des vorliegenden Vertrags im Auftrag des Kunden konzipiert, entwickelt und veröffentlicht wird, einschliesslich ihrer Struktur, ihres Designs, ihres Codes sowie ihres Inhalts, wie er vom Kunden bereitgestellt oder genehmigt wurde.",
            "„Ursprüngliche Leistung“ bezeichnet die grafische Gestaltung, die technische Entwicklung und die erstmalige Veröffentlichung der Internetseite, die von Legatis gemäss Artikel 3 kostenlos erbracht werden.",
            "„Änderungen“ bezeichnet jeden Eingriff in die Internetseite nach deren erstmaliger Veröffentlichung, unabhängig davon, ob dieser vom Kunden verlangt oder von Legatis aus eigener Initiative beschlossen wird.",
            "„Domainname“ bezeichnet die Internetadresse (zum Beispiel „www.name-der-kanzlei.ch“), unter welcher die Internetseite der Öffentlichkeit zugänglich ist.",
            "„Lead“ bezeichnet jede Kontaktanfrage, Nachricht, Terminvereinbarung oder Kontaktangabe, die von einem Besucher der Internetseite oder des Verzeichnisses von Legatis übermittelt wird und geeignet ist, eine geschäftliche Gelegenheit für den Kunden oder für einen Dritten darzustellen.",
            "„Dritte Einrichtungen“ oder „Partner“ bezeichnet jede natürliche oder juristische Person ausser dem Kunden und Legatis, mit der Legatis eine Geschäfts- oder Partnerschaftsbeziehung unterhält, einschliesslich anderer Anwältinnen und Anwälte, Kanzleien oder juristischer bzw. nichtjuristischer Dienstleistungen."
        ]},
        {"heading": "Artikel 2 — Vertragsgegenstand", "paragraphs": [
            "Der vorliegende Vertrag bezweckt die Festlegung der Bedingungen, unter denen Legatis dem Kunden die in Artikel 4 beschriebene ursprüngliche Leistung erbringt, sowie der Nutzungs-, Verwaltungs-, Änderungs- und Verwertungsrechte, die der Kunde Legatis an der Internetseite als Gegenleistung für diese Unentgeltlichkeit einräumt.",
            "Der vorliegende Vertrag ist eigenständig und unabhängig von der Registrierung des Kunden im Verzeichnis von Legatis und dem damit einhergehenden Verfahren zur Identitätsverifizierung. Die Ablehnung des vorliegenden Vertrags berührt weder die Registrierung des Kunden im Verzeichnis von Legatis noch sein Benutzerkonto."
        ]},
        {"heading": "Artikel 3 — Unentgeltlichkeit der ursprünglichen Leistung", "paragraphs": [
            "Die in Artikel 4 beschriebene ursprüngliche Leistung wird dem Kunden von Legatis ohne direkte finanzielle Gegenleistung erbracht. Dem Kunden wird für die Konzeption, die Entwicklung und die erstmalige Veröffentlichung der Internetseite kein Betrag in Rechnung gestellt.",
            "Diese Unentgeltlichkeit erstreckt sich nicht auf die vom vorliegenden Vertrag ausdrücklich ausgenommenen Elemente, namentlich den Domainnamen (Artikel 8) und die vom Kunden nach der erstmaligen Veröffentlichung verlangten Änderungen (Artikel 7), welche gemäss den nachfolgend beschriebenen Modalitäten gesondert in Rechnung gestellt werden.",
            "Legatis behält sich das Recht vor, die Unentgeltlichkeit sämtlicher oder eines Teils seiner Dienstleistungen für neue Kunden jederzeit zu beenden, ohne dass dies die auf die zum Zeitpunkt dieser Änderung bereits veröffentlichten Internetseiten anwendbaren Bedingungen berührt, sofern die Parteien nichts anderes vereinbaren."
        ]},
        {"heading": "Artikel 4 — Beschreibung der ursprünglichen Leistung", "paragraphs": [
            "Die ursprüngliche Leistung umfasst: (i) ein vorbereitendes Gespräch oder einen vorbereitenden Austausch mit dem Kunden zur Erhebung seiner beruflichen Angaben, seines Textinhalts, allfälliger Fotografien und seiner ästhetischen Präferenzen, soweit dies mit den von Legatis angebotenen Vorlagen vereinbar ist; (ii) die grafische Gestaltung der Internetseite anhand von durch Legatis entwickelten Vorlagen und Komponenten; (iii) die Einbindung des vom Kunden bereitgestellten oder genehmigten Inhalts; (iv) die technische Veröffentlichung der Internetseite auf der von Legatis gewählten Hosting-Infrastruktur; und (v) eine grundlegende Suchmaschinenoptimierung.",
            "Legatis bemüht sich, die ursprüngliche Leistung innerhalb einer angemessenen Frist nach Annahme des vorliegenden Vertrags zu erbringen, ohne sich jedoch auf eine bestimmte Frist zu verpflichten, da die ursprüngliche Leistung unentgeltlich erbracht wird und insofern keiner Erfolgspflicht hinsichtlich der Fristen unterliegt.",
            "Der Kunde verpflichtet sich, Legatis innerhalb einer angemessenen Frist, nachdem er darum ersucht wurde, sämtliche für die Realisierung der Internetseite erforderlichen Informationen, Texte, Bilder und Genehmigungen zur Verfügung zu stellen, insbesondere hinsichtlich des Rechts zur Nutzung jeder Fotografie oder jedes Textes, den er Legatis übermittelt."
        ]},
        {"heading": "Artikel 5 — Redaktionelle und technische Kontrolle der Internetseite", "paragraphs": [
            "Der Kunde anerkennt und akzeptiert, dass Legatis während der gesamten Dauer des vorliegenden Vertrags die uneingeschränkte redaktionelle und technische Kontrolle über die Internetseite behält. Legatis hat in diesem Zusammenhang das Recht, nach eigenem Ermessen und ohne die vorherige Zustimmung des Kunden einholen zu müssen, den Inhalt, das Design, die Struktur oder die Funktionen der Internetseite ganz oder teilweise hinzuzufügen, zu ändern, neu zu ordnen oder zu entfernen.",
            "Diese Kontrolle umfasst insbesondere das Recht von Legatis, Korrekturen, technische oder sicherheitsbezogene Aktualisierungen sowie globale gestalterische Weiterentwicklungen vorzunehmen, die auf sämtliche von Legatis für seine Kunden verwalteten Internetseiten angewendet werden, sowie jede Änderung, die Legatis für die ordnungsgemässe Führung, die rechtliche Konformität oder das Erscheinungsbild der Plattform Legatis als Ganzes für erforderlich hält.",
            "Legatis bemüht sich im Rahmen des Zumutbaren, den Kunden über wesentliche Änderungen zu informieren, die es aus eigener Initiative an der Internetseite vornimmt, ohne dass diese Information jedoch eine Gültigkeitsvoraussetzung für diese Änderungen darstellt.",
            "Legatis behält sich zudem das Recht vor, den Zugang zur Internetseite auszusetzen oder sie vollständig aus der Veröffentlichung zu nehmen, insbesondere bei einem Verstoss des Kunden gegen den vorliegenden Vertrag, bei Einstellung der Anwaltstätigkeit des Kunden, bei dessen Streichung aus dem Anwaltsregister, bei rechtswidrigen oder standeswidrigen Inhalten, bei Nichtzahlung von aufgrund des vorliegenden Vertrags geschuldeten Gebühren oder bei Kündigung des Vertrags gemäss den Bedingungen von Artikel 15."
        ]},
        {"heading": "Artikel 6 — Hinzufügung, Änderung und Löschung der Internetseite durch Legatis", "paragraphs": [
            "Unbeschadet von Artikel 5 kann Legatis jederzeit und nach eigenem Ermessen beschliessen, die Internetseite schlicht und einfach zu löschen, insbesondere aus technischen, geschäftlichen, wirtschaftlichen oder strategischen Gründen, die Legatis selbst betreffen, unter Einhaltung einer dem Kunden auf geeignetem Weg mitgeteilten angemessenen Vorankündigungsfrist, ausser in dringenden Fällen oder bei schwerwiegenden Gründen, in denen die Löschung sofort erfolgen kann.",
            "Im Fall einer Löschung der Internetseite auf Initiative von Legatis aus anderen Gründen als einem Verstoss des Kunden bemüht sich Legatis, soweit möglich und ohne dazu verpflichtet zu sein, dem Kunden einen angemessenen Export des Textinhalts der Internetseite zur Verfügung zu stellen, wie er zum Zeitpunkt der Löschung bestand.",
            "Der Kunde kann keinerlei Entschädigung, gleich welcher Art, aufgrund der Ausübung der in diesem Artikel und in Artikel 5 beschriebenen Kontroll-, Änderungs- oder Löschungsrechte durch Legatis geltend machen, vorbehaltlich der zwingenden Bestimmungen des schweizerischen Rechts, die vertraglich nicht ausgeschlossen werden können."
        ]},
        {"heading": "Artikel 7 — Vom Kunden verlangte Änderungen (kostenpflichtige Leistungen)", "paragraphs": [
            "Jede vom Kunden nach der erstmaligen Veröffentlichung verlangte Änderung der Internetseite, sei es eine Änderung des Inhalts, des Designs, der Struktur oder der Funktionalität, stellt eine von der ursprünglichen Leistung eigenständige Leistung dar und wird von Legatis in Rechnung gestellt, sofern nichts ausdrücklich anderes vereinbart wird.",
            "Legatis teilt dem Kunden auf Anfrage einen Tarif oder einen Kostenvoranschlag für jede beantragte Änderung mit, bevor deren Umsetzung erfolgt. Keine kostenpflichtige Änderung wird ohne vorherige Zustimmung des Kunden zum Grundsatz und zum Betrag der Rechnungsstellung vorgenommen, wobei klargestellt wird, dass diese vorherige Zustimmung nicht für Änderungen gilt, die Legatis aus eigener Initiative gemäss Artikel 5 oder 6 vornimmt und die für den Kunden weiterhin kostenlos bleiben.",
            "Die für Änderungen anwendbaren Tarife sind diejenigen, die Legatis zum Zeitpunkt der Anfrage mitteilt, wobei sich Legatis das Recht vorbehält, seine Preisliste für künftige Anfragen jederzeit anzupassen.",
            "Bei Nichtzahlung der für in Rechnung gestellte Änderungen geschuldeten Beträge kann Legatis die Durchführung neuer Änderungen bis zur Regularisierung aussetzen, ohne dass dies den Fortbestand der Internetseite in ihrem bestehenden Zustand beeinträchtigt."
        ]},
        {"heading": "Artikel 8 — Domainname", "paragraphs": [
            "Wünscht der Kunde, dass die Internetseite unter einem eigenen Domainnamen (zum Beispiel dem Namen seiner Kanzlei) zugänglich ist, gehen die Registrierung und die regelmässige Erneuerung dieses Domainnamens ausschliesslich zulasten des Kunden, auch wenn Legatis diese Registrierung aus Gründen der Einfachheit technisch im Auftrag des Kunden vornimmt.",
            "Mangels eines eigenen Domainnamens oder bei Nichterneuerung durch den Kunden bleibt die Internetseite unter einer von Legatis bereitgestellten generischen Adresse zugänglich oder wird wieder unter einer solchen zugänglich (zum Beispiel eine Subdomain der Seite legatis.ch), ohne zusätzliche Kosten für den Kunden.",
            "Bei Kündigung des vorliegenden Vertrags oder Löschung der Internetseite auf Initiative der einen oder anderen Partei bleibt die Inhaberschaft des Domainnamens, sofern dieser auf den Namen des Kunden registriert und von ihm bezahlt wurde, beim Kunden, vorbehaltlich der Begleichung eines allfälligen ausstehenden Saldos."
        ]},
        {"heading": "Artikel 9 — Hosting und Verfügbarkeit", "paragraphs": [
            "Legatis hostet die Internetseite auf einer technischen Infrastruktur seiner Wahl, die es jederzeit weiterentwickeln oder ändern kann, ohne dass hierfür die Zustimmung des Kunden erforderlich ist, sofern die Internetseite unter gleichwertigen Bedingungen öffentlich zugänglich bleibt.",
            "Legatis setzt angemessene Mittel ein, um eine zufriedenstellende Verfügbarkeit der Internetseite sicherzustellen, ohne jedoch eine unterbrechungsfreie Verfügbarkeit zu garantieren, da die Internetseite vorübergehenden Unterbrechungen für Wartungsarbeiten, Aktualisierungen oder aus Gründen unterliegen kann, die der angemessenen Kontrolle von Legatis entzogen sind (Ausfall eines Drittanbieters, Sicherheitsvorfall, höhere Gewalt im Sinne von Artikel 17)."
        ]},
        {"heading": "Artikel 10 — Suchmaschinenoptimierung, Backlinks und Sichtbarkeit von Legatis", "paragraphs": [
            "Als Gegenleistung für die Unentgeltlichkeit der ursprünglichen Leistung räumt der Kunde Legatis das Recht ein, auf der Internetseite sichtbar einen oder mehrere Hyperlinks („Backlinks“) einzubinden, die auf die Seite legatis.ch, auf das Profil des Kunden im Verzeichnis von Legatis oder auf andere von Legatis betriebene Seiten oder Dienste verweisen, sowie einen Hinweis wie „Website erstellt von Legatis“ oder Gleichwertiges.",
            "Der Kunde ermächtigt Legatis, die Internetseite als geschäftliche Referenz oder zum Nachweis seines Know-hows zu erwähnen und gegebenenfalls darzustellen (Bildschirmaufnahmen, Auszüge, Link), insbesondere gegenüber anderen Anwältinnen und Anwälten, die an einer ähnlichen Leistung interessiert sein könnten, unter Vorbehalt der Wahrung der in Artikel 14 vorgesehenen Vertraulichkeit für nicht öffentliche Informationen.",
            "Der Kunde anerkennt, dass diese Links und Hinweise Bestandteil der wirtschaftlichen Gegenleistung sind, welche die Unentgeltlichkeit der ursprünglichen Leistung rechtfertigt, und kann deren Entfernung nur im Rahmen einer Kündigung des vorliegenden Vertrags verlangen, welche sodann die in Artikel 15 beschriebenen Folgen nach sich zieht."
        ]},
        {"heading": "Artikel 11 — Generierung, Verwaltung und Übermittlung von Leads", "paragraphs": [
            "Die Internetseite und, allgemeiner, das Verzeichnis von Legatis, in dem der Kunde erscheint, können Leads generieren, insbesondere über Kontaktformulare, Vermittlungsanfragen oder Vergleichswerkzeuge, die auf der Seite legatis.ch zur Verfügung gestellt werden.",
            "Der Kunde ermächtigt Legatis, die ihn betreffenden Leads unter Einhaltung der geltenden Datenschutzgesetzgebung (Artikel 13) zu erheben, zu verwalten und direkt an den Kunden zu übermitteln.",
            "Der Kunde anerkennt darüber hinaus, dass Legatis im Rahmen seiner Tätigkeit als Vermittlungsplattform Anfragen, Informationen oder Leads, die den Kunden nicht spezifisch und ausschliesslich betreffen, an Dritte Einrichtungen weiterleiten, mit diesen teilen oder ihnen übermitteln kann — insbesondere wenn ein Besucher eine allgemeine Anfrage stellt, die für mehrere Anwältinnen und Anwälte von Interesse sein könnte, wenn der Kunde nicht in der Lage ist, auf eine Anfrage zu antworten, oder im Rahmen ergänzender Dienstleistungen, die von Legatis oder seinen Partnern angeboten werden. Diese Befugnis verleiht dem Kunden keinerlei Exklusivität an den über das Verzeichnis von Legatis oder die Internetseite generierten Leads.",
            "Legatis garantiert weder ein bestimmtes Volumen noch eine bestimmte Häufigkeit noch eine bestimmte Mindestqualität der dem Kunden übermittelten Leads, da die ursprüngliche Leistung und der vorliegende Vertrag in keinem Fall eine Verpflichtung zu einem geschäftlichen Erfolg zugunsten des Kunden darstellen."
        ]},
        {"heading": "Artikel 12 — Geistiges Eigentum", "paragraphs": [
            "Der Quellcode, die Vorlagen, die grafischen Komponenten, die technischen Funktionen und, allgemeiner, jedes von Legatis unabhängig vom vom Kunden bereitgestellten spezifischen Inhalt konzipierte oder entwickelte Element der Internetseite bleiben ausschliessliches Eigentum von Legatis, auch nach der Veröffentlichung der Internetseite.",
            "Der kundenspezifische Inhalt (sein Name, seine persönliche Präsentation, seine Kontaktdaten, die von ihm persönlich bereitgestellten Texte und Fotografien, deren Urheber oder Rechtsinhaber er ist) bleibt Eigentum des Kunden, vorbehaltlich des Legatis für die Zwecke der Erfüllung des vorliegenden Vertrags eingeräumten Nutzungsrechts, insbesondere für dessen Anzeige auf der Internetseite und im Verzeichnis von Legatis.",
            "Der Kunde garantiert Legatis, dass er über sämtliche erforderlichen Rechte an dem von ihm bereitgestellten Inhalt (Texte, Fotografien, Logos) verfügt, und stellt Legatis von jedem Anspruch Dritter frei, der sich aus einer Verletzung von Rechten des geistigen Eigentums oder von Persönlichkeitsrechten infolge dieses Inhalts ergibt.",
            "Bei Kündigung des vorliegenden Vertrags behält Legatis das Recht, die im Rahmen der Realisierung der Internetseite entwickelten Vorlagen, Komponenten und technischen Kenntnisse für andere Kunden zu verwenden, unter Ausschluss des spezifischen Inhalts und der persönlichen Informationen des Kunden."
        ]},
        {"heading": "Artikel 13 — Datenschutz", "paragraphs": [
            "Legatis bearbeitet die Personendaten des Kunden und der Besucher der Internetseite gemäss dem Bundesgesetz über den Datenschutz (DSG) und seiner Revision (revDSG) sowie den Bestimmungen der Datenschutzerklärung von Legatis, die auf der Seite legatis.ch einsehbar ist.",
            "Die dem Kunden im Rahmen von Artikel 11 übermittelten Lead-Daten dürfen von ihm nur für die Zwecke seiner eigenen beruflichen Tätigkeit verwendet werden, unter Einhaltung der für Anwältinnen und Anwälte geltenden Standesregeln sowie der Datenschutzgesetzgebung.",
            "Der Kunde bleibt als Anwältin bzw. Anwalt allein verantwortlich für die Einhaltung des Berufsgeheimnisses und der für seine eigene Tätigkeit geltenden Datenschutzvorschriften, unabhängig von den Pflichten von Legatis gemäss dem vorliegenden Artikel."
        ]},
        {"heading": "Artikel 14 — Vertraulichkeit", "paragraphs": [
            "Jede Partei verpflichtet sich, die nicht öffentlichen Informationen, von denen sie im Rahmen der Erfüllung des vorliegenden Vertrags Kenntnis erlangt, vertraulich zu behandeln und sie nur für die Zwecke dieser Erfüllung zu verwenden, sofern nichts anderes schriftlich vereinbart wurde oder eine gesetzliche Offenlegungspflicht besteht.",
            "Diese Vertraulichkeitspflicht steht der Ausübung der in Artikel 10 vorgesehenen Kommunikations- und Präsentationsrechte von Legatis bezüglich der Internetseite nicht entgegen, da diese sich naturgemäss auf Informationen beziehen, die durch die Veröffentlichung der Internetseite selbst öffentlich gemacht wurden."
        ]},
        {"heading": "Artikel 15 — Dauer und Kündigung", "paragraphs": [
            "Der vorliegende Vertrag wird auf unbestimmte Zeit ab seiner Annahme durch den Kunden geschlossen und bleibt in Kraft, solange die Internetseite von Legatis gehostet wird.",
            "Jede Partei kann den vorliegenden Vertrag jederzeit unter Einhaltung einer der anderen Partei schriftlich (auch per E-Mail) mitgeteilten angemessenen Vorankündigungsfrist kündigen, ohne einen besonderen Grund angeben zu müssen.",
            "Im Fall einer Kündigung auf Initiative des Kunden anerkennt dieser, dass die Internetseite als technische und grafische Umsetzung von Legatis nicht mehr über Legatis gehostet und der Öffentlichkeit zugänglich gemacht wird, unbeschadet der Inhaberschaft des spezifischen Inhalts des Kunden gemäss Artikel 12.",
            "Die Kündigung des vorliegenden Vertrags hat keine Auswirkung auf die Registrierung des Kunden im Verzeichnis von Legatis und auf sein Benutzerkonto, welche weiterhin den allgemeinen Nutzungsbedingungen von Legatis unterliegen."
        ]},
        {"heading": "Artikel 16 — Haftung und Gewährleistung", "paragraphs": [
            "Da die ursprüngliche Leistung unentgeltlich erbracht wird, unterliegt Legatis im nach schweizerischem Recht zulässigen Rahmen nur einer Sorgfalts- und nicht einer Erfolgspflicht, und seine Haftung kann nur bei Vorsatz oder grober Fahrlässigkeit begründet werden.",
            "Legatis garantiert weder das vollständige Fehlen von Fehlern, Ausfällen oder Nichtverfügbarkeit der Internetseite noch irgendein geschäftliches Ergebnis (Anzahl Besucher, Leads, Neukunden), das sich aus der Veröffentlichung der Internetseite ergibt.",
            "In jedem Fall ist die Haftung von Legatis, sollte sie begründet sein, auf direkte und vorhersehbare Schäden beschränkt, unter Ausschluss jeglichen indirekten Schadens (Verlust von Kundschaft, entgangener Gewinn, Rufschädigung), und dies im Rahmen der zwingenden Bestimmungen des schweizerischen Rechts, insbesondere Artikel 100 des Obligationenrechts betreffend die Haftung für Vorsatz oder grobe Fahrlässigkeit, die vertraglich nicht ausgeschlossen werden kann.",
            "Der Kunde bleibt allein verantwortlich für den von ihm bereitgestellten oder zur Veröffentlichung auf der Internetseite genehmigten Inhalt, insbesondere für dessen Übereinstimmung mit den Standesregeln des Anwaltsberufs und den gesetzlichen Bestimmungen über die Anwaltswerbung."
        ]},
        {"heading": "Artikel 17 — Höhere Gewalt", "paragraphs": [
            "Keine der Parteien kann für eine Verletzung ihrer Pflichten aus dem vorliegenden Vertrag verantwortlich gemacht werden, wenn diese Verletzung auf einem Fall höherer Gewalt beruht, verstanden als jedes im Sinne der schweizerischen Rechtsprechung äussere, unvorhersehbare und unabwendbare Ereignis, insbesondere eine Naturkatastrophe, ein grösserer und weitreichender Ausfall der Internetinfrastruktur, ein umfangreicher Cyberangriff oder eine Entscheidung einer Behörde."
        ]},
        {"heading": "Artikel 18 — Abtretung des Vertrags", "paragraphs": [
            "Legatis kann den vorliegenden Vertrag sowie sämtliche sich daraus ergebenden Rechte und Pflichten an jede Einrichtung abtreten, die seine Tätigkeit ganz oder teilweise übernimmt, unter vorheriger Information des Kunden.",
            "Der Kunde kann den vorliegenden Vertrag ohne vorherige schriftliche Zustimmung von Legatis nicht an einen Dritten abtreten, da der Vertrag im Hinblick auf die Person des Kunden in seiner Eigenschaft als im Verzeichnis von Legatis eingetragener Anwalt geschlossen wurde."
        ]},
        {"heading": "Artikel 19 — Änderung des vorliegenden Vertrags", "paragraphs": [
            "Legatis kann die Bedingungen des vorliegenden Vertrags für die Zukunft ändern, insbesondere um rechtlichen, technischen oder geschäftlichen Entwicklungen Rechnung zu tragen. Wesentliche Änderungen werden dem Kunden auf geeignetem Weg mitgeteilt und gelten als angenommen, wenn der Kunde ihnen nicht innerhalb einer angemessenen Frist widerspricht oder wenn er die Dienste von Legatis nach deren Inkrafttreten weiterhin in Anspruch nimmt.",
            "Nimmt der Kunde eine wesentliche Änderung nicht an, kann er den vorliegenden Vertrag gemäss den Bedingungen von Artikel 15 kündigen."
        ]},
        {"heading": "Artikel 20 — Teilnichtigkeit", "paragraphs": [
            "Sollte eine der Klauseln des vorliegenden Vertrags von einer zuständigen Behörde für nichtig, rechtswidrig oder unanwendbar erklärt werden, bleiben die übrigen Klauseln des Vertrags vollumfänglich in Kraft. Die Parteien bemühen sich in diesem Fall, die ungültige Klausel durch eine gültige Klausel zu ersetzen, deren wirtschaftliche Wirkung derjenigen der ungültigen Klausel möglichst nahekommt."
        ]},
        {"heading": "Artikel 21 — Elektronische Annahme und Beweis", "paragraphs": [
            "Der Kunde nimmt den vorliegenden Vertrag an, indem er dessen gesamten Text durchscrollt, das dafür vorgesehene Bestätigungskästchen ankreuzt und anschliessend auf die auf der Benutzeroberfläche von Legatis vorgesehene Annahmeschaltfläche klickt.",
            "Der Kunde anerkennt, dass diese elektronische Annahme eine gültige Willensäusserung darstellt und ihn im gleichen Masse rechtlich verpflichtet wie eine handschriftliche Unterschrift, gemäss den allgemeinen Grundsätzen des schweizerischen Vertragsrechts betreffend die Formfreiheit (Artikel 10 des Obligationenrechts), vorbehaltlich gesetzlicher Bestimmungen, die für bestimmte Rechtsgeschäfte eine besondere Form vorschreiben.",
            "Legatis bewahrt zu Beweiszwecken eine zeitlich gestempelte Aufzeichnung der Annahme durch den Kunden auf, einschliesslich der angenommenen Vertragsversion."
        ]},
        {"heading": "Artikel 22 — Anwendbares Recht und Gerichtsstand", "paragraphs": [
            "Der vorliegende Vertrag unterliegt schweizerischem Recht, unter Ausschluss seiner Kollisionsnormen und des Übereinkommens der Vereinten Nationen über Verträge über den internationalen Warenkauf.",
            "Für jede Streitigkeit, die sich aus dem vorliegenden Vertrag ergibt oder damit im Zusammenhang steht, sind ausschliesslich die ordentlichen Gerichte am Wohnsitz oder Sitz von Legatis zuständig, vorbehaltlich zwingender Bestimmungen des schweizerischen Rechts, die einen anderen Gerichtsstand vorsehen, insbesondere im Bereich des Konsumentenschutzes, sofern diese anwendbar sein sollten."
        ]},
        {"heading": "Artikel 23 — Schlussbestimmungen", "paragraphs": [
            "Der vorliegende Vertrag stellt die gesamte Vereinbarung der Parteien betreffend die kostenlose Erstellung und Verwaltung der Internetseite dar und geht jeder früheren Vereinbarung oder jedem früheren Austausch zum selben Gegenstand vor, vorbehaltlich der allgemeinen Nutzungsbedingungen von Legatis, die im Übrigen auf die Registrierung des Kunden im Verzeichnis anwendbar sind.",
            "Die Tatsache, dass eine der Parteien zu einem bestimmten Zeitpunkt einen Verstoss der anderen Partei gegen eine der Klauseln des vorliegenden Vertrags nicht geltend macht, darf nicht als Verzicht darauf ausgelegt werden, sich künftig auf diesen Verstoss oder auf eine andere Klausel des Vertrags zu berufen.",
            "Mit der Annahme des vorliegenden Vertrags bestätigt der Kunde, dass er die Rechts- und Handlungsfähigkeit besitzt, um Verträge einzugehen, und dass er im eigenen Namen handelt oder gegebenenfalls ordnungsgemäss bevollmächtigt ist, die Einrichtung zu verpflichten, in deren Namen er den Vertrag abschliesst."
        ]}
    ],
},
    "it": {
    "title": "Contratto di creazione e gestione gratuita di un sito internet professionale",
    "parties_label": "Tra Legatis, piattaforma svizzera di referenziazione di avvocati gestita a titolo individuale dal Signor Grégoire Giuliano (di seguito « Legatis » o il « Prestatore »), e l'avvocato o l'avvocatessa identificato/a dalla richiesta di verifica a cui il presente contratto è allegato (di seguito l'« Avvocato » o il « Cliente »), di seguito congiuntamente le « Parti ».",
    "preamble": [
        "Legatis gestisce un elenco online di avvocati in Svizzera nonché, per gli avvocati che lo desiderano, un servizio di creazione e ospitalità (hosting) di sito internet professionale individuale. Il presente contratto (di seguito il « Contratto ») ha per oggetto di definire le condizioni alle quali Legatis fornisce gratuitamente tale servizio al Cliente, nonché i diritti che il Cliente concede a Legatis in contropartita.",
        "Legatis persegue un obiettivo di modernizzazione della professione forense in Svizzera: numerosi avvocati competenti, in particolare presso studi di dimensioni modeste o che esercitano in proprio, non dispongono oggi di alcuna presenza online professionale soddisfacente, per mancanza di tempo, di competenze tecniche o di budget dedicato. Mettendo a disposizione gratuitamente la progettazione, la pubblicazione e l'ospitalità tecnica di un sito internet, Legatis intende colmare tale lacuna e contribuire a una migliore visibilità digitale della professione.",
        "Questa prestazione gratuita non è priva di contropartita per Legatis: essa le consente di far conoscere il proprio marchio, di ampliare il proprio pubblico, di dimostrare il proprio know-how tecnico presso la professione forense, e di sviluppare la propria attività di messa in relazione tra avvocati e giustiziabili. Il Cliente riconosce e accetta espressamente che tale contropartita, descritta in dettaglio negli articoli seguenti, costituisce la causa economica della gratuità della prestazione iniziale.",
        "Il Cliente dichiara di aver preso conoscenza dell'integralità del presente Contratto prima di accettarlo, di aver avuto la possibilità di porre qualsiasi domanda a Legatis prima della sua accettazione, e di accettare il Contratto con piena cognizione di causa, senza esservi altrimenti costretto: l'accettazione del presente Contratto è interamente facoltativa e il suo rifiuto non ha alcuna incidenza sulla prosecuzione della richiesta di verifica d'identità e di creazione dell'account su Legatis, né sulla presenza del Cliente nell'elenco Legatis."
    ],
    "articles": [
        {"heading": "Articolo 1 — Definizioni", "paragraphs": [
            "« Sito » indica il sito internet individuale progettato, sviluppato e pubblicato online da Legatis per conto del Cliente nell'ambito del presente Contratto, comprendente la sua struttura, il suo design, il suo codice, nonché il suo contenuto quale fornito o approvato dal Cliente.",
            "« Prestazione iniziale » indica la progettazione grafica, lo sviluppo tecnico e la pubblicazione online iniziale del Sito, forniti gratuitamente da Legatis conformemente all'articolo 3.",
            "« Modifiche » indica qualsiasi intervento sul Sito successivo alla sua pubblicazione online iniziale, sia esso richiesto dal Cliente o deciso da Legatis di propria iniziativa.",
            "« Nome di dominio » indica l'indirizzo internet (ad esempio « www.nome-dello-studio.ch ») sotto il quale il Sito è accessibile al pubblico.",
            "« Lead » indica qualsiasi richiesta di contatto, messaggio, presa di appuntamento o dati di contatto trasmessi da un visitatore del Sito o dell'elenco Legatis, suscettibile di costituire un'opportunità commerciale per il Cliente o per un terzo.",
            "« Entità terze » o « partner » indica qualsiasi persona fisica o giuridica, diversa dal Cliente e da Legatis, con la quale Legatis intrattiene un rapporto commerciale o di partenariato, compresi altri avvocati, studi, o servizi giuridici o non giuridici."
        ]},
        {"heading": "Articolo 2 — Oggetto del Contratto", "paragraphs": [
            "Il presente Contratto ha per oggetto di definire le condizioni alle quali Legatis fornisce al Cliente la Prestazione iniziale descritta all'articolo 4, nonché i diritti di sfruttamento, gestione, modifica e valorizzazione che il Cliente concede a Legatis sul Sito in contropartita di tale gratuità.",
            "Il presente Contratto è distinto e indipendente dall'iscrizione del Cliente all'elenco Legatis e dalla procedura di verifica d'identità che l'accompagna. Il rifiuto del presente Contratto non incide in alcun modo sull'iscrizione del Cliente all'elenco Legatis né sul suo account di accesso."
        ]},
        {"heading": "Articolo 3 — Gratuità della Prestazione iniziale", "paragraphs": [
            "La Prestazione iniziale, come descritta all'articolo 4, è fornita da Legatis al Cliente senza contropartita finanziaria diretta. Nessun importo è fatturato al Cliente per la progettazione, lo sviluppo e la pubblicazione online iniziale del Sito.",
            "Tale gratuità non si estende agli elementi espressamente esclusi dal presente Contratto, in particolare il Nome di dominio (articolo 8) e le Modifiche richieste dal Cliente successivamente alla pubblicazione online iniziale (articolo 7), che sono oggetto di fatturazione distinta secondo le modalità descritte in seguito.",
            "Legatis si riserva il diritto di porre fine alla gratuità della totalità o di parte dei propri servizi per i nuovi clienti in qualsiasi momento, senza che ciò incida sulle condizioni applicabili ai Siti già pubblicati al momento di tale cambiamento, salvo accordo contrario delle Parti."
        ]},
        {"heading": "Articolo 4 — Descrizione della Prestazione iniziale", "paragraphs": [
            "La Prestazione iniziale comprende: (i) un colloquio o scambio preliminare con il Cliente al fine di raccogliere le sue informazioni professionali, il suo contenuto testuale, le sue eventuali fotografie e le sue preferenze estetiche nella misura compatibile con i modelli proposti da Legatis; (ii) la progettazione grafica del Sito a partire da modelli e componenti sviluppati da Legatis; (iii) l'integrazione del contenuto fornito o convalidato dal Cliente; (iv) la pubblicazione tecnica del Sito sull'infrastruttura di hosting scelta da Legatis; e (v) una configurazione di referenziazione di base (SEO).",
            "Legatis si adopera per consegnare la Prestazione iniziale entro un termine ragionevole dopo l'accettazione del presente Contratto, senza tuttavia impegnarsi su un termine preciso, essendo la Prestazione iniziale fornita a titolo gratuito e non essendo, a tale titolo, soggetta ad alcun obbligo di risultato quanto ai tempi.",
            "Il Cliente si impegna a fornire a Legatis, entro un termine ragionevole dopo esserne stato richiesto, l'insieme delle informazioni, dei testi, delle immagini e delle autorizzazioni necessarie alla realizzazione del Sito, in particolare relativamente al diritto di utilizzare qualsiasi fotografia o testo che egli trasmette a Legatis."
        ]},
        {"heading": "Articolo 5 — Controllo editoriale e tecnico del Sito", "paragraphs": [
            "Il Cliente riconosce e accetta che Legatis conservi, per tutta la durata del presente Contratto, un controllo editoriale e tecnico totale sul Sito. A tale titolo, Legatis ha il diritto, a sua esclusiva discrezione e senza dover richiedere il consenso preventivo del Cliente, di aggiungere, modificare, riorganizzare o sopprimere la totalità o parte del contenuto, del design, della struttura o delle funzionalità del Sito.",
            "Tale controllo include in particolare il diritto per Legatis di apportare correzioni, aggiornamenti tecnici o di sicurezza, evoluzioni estetiche complessive applicate all'insieme dei siti che gestisce per i propri clienti, nonché qualsiasi modifica che Legatis ritenga necessaria alla buona tenuta, alla conformità legale o all'immagine della piattaforma Legatis nel suo complesso.",
            "Legatis si adopera, nella misura del ragionevole, per informare il Cliente delle modifiche sostanziali apportate al Sito di propria iniziativa, senza tuttavia che tale informazione costituisca una condizione di validità di tali modifiche.",
            "Legatis si riserva altresì il diritto di sospendere l'accesso al Sito o di ritirarlo integralmente dalla pubblicazione, in particolare in caso di inadempimento del Cliente al presente Contratto, di cessazione dell'attività di avvocato del Cliente, di radiazione del Cliente dall'albo, di contenuto illecito o contrario alla deontologia professionale, di mancato pagamento di importi dovuti a titolo del presente Contratto, o di risoluzione del Contratto alle condizioni dell'articolo 15."
        ]},
        {"heading": "Articolo 6 — Aggiunta, modifica e soppressione del Sito da parte di Legatis", "paragraphs": [
            "Fatto salvo l'articolo 5, Legatis può, in qualsiasi momento e a sua esclusiva discrezione, decidere di sopprimere puramente e semplicemente il Sito, in particolare per ragioni tecniche, commerciali, economiche o strategiche proprie di Legatis, mediante un preavviso ragionevole indirizzato al Cliente con qualsiasi mezzo utile, salvo in caso di urgenza o di motivo grave, nel qual caso la soppressione può essere immediata.",
            "In caso di soppressione del Sito su iniziativa di Legatis per ragioni diverse da un inadempimento del Cliente, Legatis si adopera, nella misura del possibile e senza esservi tenuto, per fornire al Cliente un'esportazione ragionevole del contenuto testuale del Sito quale esistente al momento della soppressione.",
            "Il Cliente non può pretendere alcuna indennità, di qualsivoglia natura, a causa dell'esercizio da parte di Legatis dei diritti di controllo, modifica o soppressione descritti nel presente articolo e all'articolo 5, fatte salve le disposizioni imperative del diritto svizzero che non possono essere escluse contrattualmente."
        ]},
        {"heading": "Articolo 7 — Modifiche richieste dal Cliente (prestazioni a pagamento)", "paragraphs": [
            "Qualsiasi Modifica del Sito richiesta dal Cliente dopo la pubblicazione online iniziale, che si tratti di una modifica di contenuto, di design, di struttura o di funzionalità, costituisce una prestazione distinta dalla Prestazione iniziale ed è oggetto di fatturazione da parte di Legatis, salvo espresso accordo contrario.",
            "Legatis comunica al Cliente, su richiesta, una tariffa o un preventivo per qualsiasi Modifica sollecitata prima di procedere alla sua realizzazione. Nessuna Modifica a pagamento viene effettuata senza il previo accordo del Cliente sul principio e sull'importo della fatturazione, precisandosi che tale previo accordo non si applica alle modifiche che Legatis effettua di propria iniziativa in virtù dell'articolo 5 o 6, le quali rimangono gratuite per il Cliente.",
            "Le tariffe applicabili alle Modifiche sono quelle comunicate da Legatis al momento della richiesta, riservandosi Legatis il diritto di far evolvere il proprio listino tariffario in qualsiasi momento per le richieste future.",
            "In mancanza del pagamento degli importi dovuti a titolo delle Modifiche fatturate, Legatis può sospendere la realizzazione di nuove Modifiche fino a regolarizzazione, senza che ciò incida sul mantenimento online del Sito quale esistente."
        ]},
        {"heading": "Articolo 8 — Nome di dominio", "paragraphs": [
            "Qualora il Cliente desideri che il Sito sia accessibile sotto un Nome di dominio dedicato (ad esempio il nome del proprio studio), la registrazione e il rinnovo periodico di tale Nome di dominio sono a carico finanziario esclusivo del Cliente, anche quando Legatis proceda tecnicamente a tale registrazione per conto del Cliente per motivi di semplicità.",
            "In mancanza di un Nome di dominio dedicato o in caso di mancato rinnovo da parte del Cliente, il Sito rimane o ridiventa accessibile sotto un indirizzo generico fornito da Legatis (ad esempio un sottodominio del sito legatis.ch), senza costi aggiuntivi per il Cliente.",
            "In caso di risoluzione del presente Contratto o di soppressione del Sito su iniziativa dell'una o dell'altra Parte, la titolarità del Nome di dominio, qualora sia stato registrato a nome del Cliente e pagato da quest'ultimo, rimane acquisita al Cliente, fatto salvo il pagamento di eventuali importi ancora dovuti."
        ]},
        {"heading": "Articolo 9 — Hosting e disponibilità", "paragraphs": [
            "Legatis ospita il Sito su un'infrastruttura tecnica di propria scelta, che può far evolvere o modificare in qualsiasi momento senza che ciò richieda il consenso del Cliente, nella misura in cui il Sito rimanga accessibile al pubblico a condizioni equivalenti.",
            "Legatis mette in atto mezzi ragionevoli per garantire una disponibilità soddisfacente del Sito, senza tuttavia garantire una disponibilità ininterrotta, potendo il Sito essere oggetto di interruzioni temporanee per manutenzione, aggiornamento, o per ragioni che sfuggono al controllo ragionevole di Legatis (guasto di un fornitore terzo, incidente di sicurezza, caso di forza maggiore ai sensi dell'articolo 17)."
        ]},
        {"heading": "Articolo 10 — Referenziazione, link di ritorno e visibilità di Legatis", "paragraphs": [
            "In contropartita della gratuità della Prestazione iniziale, il Cliente concede a Legatis il diritto di includere sul Sito, in modo visibile, uno o più collegamenti ipertestuali (« backlink ») che rinviano al sito legatis.ch, alla scheda del Cliente sull'elenco Legatis, o ad altre pagine o servizi gestiti da Legatis, nonché una dicitura del tipo « sito realizzato da Legatis » o equivalente.",
            "Il Cliente autorizza Legatis a menzionare e, se del caso, a presentare il Sito (schermate, estratti, link) a titolo di referenza commerciale o di dimostrazione del proprio know-how, in particolare presso altri avvocati suscettibili di essere interessati a una prestazione analoga, fatto salvo il rispetto della riservatezza prevista all'articolo 14 per le informazioni non pubbliche.",
            "Il Cliente riconosce che tali link e menzioni concorrono alla contropartita economica che giustifica la gratuità della Prestazione iniziale e non può richiederne la soppressione se non nell'ambito di una risoluzione del presente Contratto, la quale comporta allora le conseguenze descritte all'articolo 15."
        ]},
        {"heading": "Articolo 11 — Generazione, gestione e trasmissione dei lead", "paragraphs": [
            "Il Sito e, più in generale, l'elenco Legatis in cui figura il Cliente sono suscettibili di generare Lead, in particolare tramite moduli di contatto, richieste di messa in relazione o strumenti di comparazione messi a disposizione sul sito legatis.ch.",
            "Il Cliente autorizza Legatis a raccogliere, gestire e trasmettere al Cliente i Lead che lo riguardano direttamente, nel rispetto della legislazione applicabile in materia di protezione dei dati (articolo 13).",
            "Il Cliente riconosce inoltre che Legatis, nell'ambito della propria attività di piattaforma di messa in relazione, può indirizzare, condividere o trasmettere a Entità terze richieste, informazioni o Lead che non riguardano specificamente ed esclusivamente il Cliente — in particolare quando un visitatore formula una richiesta generale suscettibile di interessare più avvocati, quando il Cliente non è in grado di rispondere a una richiesta, o nell'ambito di servizi complementari proposti da Legatis o dai suoi partner. Tale facoltà non conferisce al Cliente alcuna esclusiva sui Lead generati tramite l'elenco Legatis o il Sito.",
            "Legatis non garantisce alcun volume, alcuna frequenza né alcuna qualità minima di Lead trasmessi al Cliente, non costituendo la Prestazione iniziale e il presente Contratto in alcun caso un impegno di risultato commerciale a favore del Cliente."
        ]},
        {"heading": "Articolo 12 — Proprietà intellettuale", "paragraphs": [
            "Il codice sorgente, i modelli, i componenti grafici, le funzionalità tecniche e, più in generale, qualsiasi elemento del Sito progettato o sviluppato da Legatis indipendentemente dal contenuto specifico fornito dal Cliente, rimangono di proprietà esclusiva di Legatis, anche dopo la pubblicazione online del Sito.",
            "Il contenuto specifico del Cliente (il suo nome, la sua presentazione personale, i suoi dati di contatto, i testi e le fotografie che fornisce personalmente e di cui è autore o avente diritto) rimane di proprietà del Cliente, fatto salvo il diritto di utilizzo concesso a Legatis per le esigenze dell'esecuzione del presente Contratto, in particolare la sua pubblicazione sul Sito e sull'elenco Legatis.",
            "Il Cliente garantisce a Legatis di detenere tutti i diritti necessari sul contenuto che fornisce (testi, fotografie, loghi) e manleva Legatis da qualsiasi azione di terzi relativa a una violazione di diritti di proprietà intellettuale o della personalità derivante da tale contenuto.",
            "In caso di risoluzione del presente Contratto, Legatis conserva il diritto di utilizzare i modelli, i componenti e il know-how tecnico sviluppati nell'ambito della realizzazione del Sito per altri clienti, ad esclusione del contenuto specifico e delle informazioni personali proprie del Cliente."
        ]},
        {"heading": "Articolo 13 — Protezione dei dati", "paragraphs": [
            "Legatis tratta i dati personali del Cliente e dei visitatori del Sito conformemente alla legge federale sulla protezione dei dati (LPD) e alla sua revisione (nLPD), nonché alle disposizioni della politica sulla privacy di Legatis, consultabile sul sito legatis.ch.",
            "I dati dei Lead trasmessi al Cliente nell'ambito dell'articolo 11 possono essere utilizzati da quest'ultimo solo per le esigenze della propria attività professionale, nel rispetto delle regole deontologiche applicabili agli avvocati e della legislazione sulla protezione dei dati.",
            "Il Cliente rimane il solo responsabile, nella sua qualità di avvocato, del rispetto del segreto professionale e delle regole di protezione dei dati applicabili alla propria attività, indipendentemente dagli obblighi di Legatis a titolo del presente articolo."
        ]},
        {"heading": "Articolo 14 — Riservatezza", "paragraphs": [
            "Ciascuna Parte si impegna a mantenere riservate le informazioni non pubbliche di cui venisse a conoscenza nell'ambito dell'esecuzione del presente Contratto e a utilizzarle esclusivamente ai fini di tale esecuzione, salvo diverso accordo scritto o obbligo legale di divulgazione.",
            "Tale obbligo di riservatezza non osta all'esercizio da parte di Legatis dei diritti di comunicazione e di valorizzazione del Sito previsti all'articolo 10, i quali riguardano per loro natura informazioni rese pubbliche dalla pubblicazione online del Sito stesso."
        ]},
        {"heading": "Articolo 15 — Durata e risoluzione", "paragraphs": [
            "Il presente Contratto è concluso a tempo indeterminato a decorrere dalla sua accettazione da parte del Cliente, e rimane in vigore finché il Sito rimane ospitato da Legatis.",
            "Ciascuna Parte può risolvere il presente Contratto in qualsiasi momento, mediante un preavviso ragionevole indirizzato per iscritto all'altra Parte (anche per posta elettronica), senza dover giustificare un motivo particolare.",
            "In caso di risoluzione su iniziativa del Cliente, quest'ultimo riconosce che il Sito, in quanto realizzazione tecnica e grafica di Legatis, cessa di essere ospitato e accessibile al pubblico tramite Legatis, fatta salva la titolarità del contenuto specifico del Cliente quale definito all'articolo 12.",
            "La risoluzione del presente Contratto non ha alcun effetto sull'iscrizione del Cliente all'elenco Legatis né sul suo account di accesso, i quali rimangono disciplinati dalle condizioni generali di utilizzo di Legatis."
        ]},
        {"heading": "Articolo 16 — Responsabilità e garanzie", "paragraphs": [
            "Essendo la Prestazione iniziale fornita a titolo gratuito, Legatis è tenuta, nei limiti consentiti dal diritto svizzero, solo a un'obbligazione di mezzi e non di risultato, e la sua responsabilità può essere chiamata in causa solo in caso di dolo o negligenza grave.",
            "Legatis non garantisce né l'assenza totale di errori, guasti o indisponibilità del Sito, né alcun risultato commerciale (numero di visitatori, di Lead, di nuovi clienti) derivante dalla pubblicazione online del Sito.",
            "In ogni caso, la responsabilità di Legatis, qualora dovesse essere chiamata in causa, è limitata ai danni diretti e prevedibili, ad esclusione di qualsiasi danno indiretto (perdita di clientela, perdita di chance, pregiudizio all'immagine), e ciò nei limiti consentiti dalle disposizioni imperative del diritto svizzero, in particolare l'articolo 100 del Codice delle obbligazioni relativo alla responsabilità per dolo o colpa grave che non può essere esclusa per convenzione.",
            "Il Cliente rimane il solo responsabile del contenuto che fornisce o approva per la pubblicazione sul Sito, in particolare della sua conformità alle regole deontologiche della professione forense e alle disposizioni legali relative alla pubblicità degli avvocati."
        ]},
        {"heading": "Articolo 17 — Forza maggiore", "paragraphs": [
            "Nessuna delle Parti può essere ritenuta responsabile di un inadempimento dei propri obblighi a titolo del presente Contratto qualora tale inadempimento derivi da un caso di forza maggiore, inteso come qualsiasi evento esterno, imprevedibile e irresistibile ai sensi della giurisprudenza svizzera, in particolare una catastrofe naturale, un guasto grave e generalizzato dell'infrastruttura internet, un attacco informatico di grande portata, o una decisione di un'autorità pubblica."
        ]},
        {"heading": "Articolo 18 — Cessione del Contratto", "paragraphs": [
            "Legatis può cedere il presente Contratto, nonché l'insieme dei diritti e degli obblighi che ne derivano, a qualsiasi entità che rilevasse la totalità o parte della propria attività, previa informazione del Cliente.",
            "Il Cliente non può cedere il presente Contratto a un terzo senza il previo consenso scritto di Legatis, essendo il Contratto concluso in considerazione della persona del Cliente nella sua qualità di avvocato iscritto all'elenco Legatis."
        ]},
        {"heading": "Articolo 19 — Modifica del presente Contratto", "paragraphs": [
            "Legatis può modificare i termini del presente Contratto per il futuro, in particolare per tener conto di evoluzioni legali, tecniche o commerciali. Le modifiche sostanziali sono comunicate al Cliente con qualsiasi mezzo utile e si considerano accettate se il Cliente non vi si oppone entro un termine ragionevole o se continua a beneficiare dei servizi di Legatis dopo la loro entrata in vigore.",
            "Il Cliente può, qualora non accetti una modifica sostanziale, risolvere il presente Contratto alle condizioni dell'articolo 15."
        ]},
        {"heading": "Articolo 20 — Nullità parziale", "paragraphs": [
            "Qualora una delle clausole del presente Contratto dovesse essere ritenuta nulla, illecita o inapplicabile da un'autorità competente, le altre clausole del Contratto rimangono pienamente in vigore. Le Parti si adoperano allora per sostituire la clausola invalidata con una clausola valida il cui effetto economico si avvicini il più possibile a quello della clausola invalidata."
        ]},
        {"heading": "Articolo 21 — Accettazione elettronica e prova", "paragraphs": [
            "Il Cliente accetta il presente Contratto scorrendo l'integralità del suo testo, spuntando la casella di conferma prevista a tale scopo, e quindi cliccando sul pulsante di accettazione previsto sull'interfaccia di Legatis.",
            "Il Cliente riconosce che tale accettazione elettronica costituisce una manifestazione di volontà valida e lo vincola giuridicamente al pari di una firma autografa, conformemente ai principi generali del diritto svizzero dei contratti relativi alla libertà di forma (articolo 10 del Codice delle obbligazioni), fatte salve le disposizioni legali che impongono una forma particolare per determinati atti.",
            "Legatis conserva una registrazione con marca temporale dell'accettazione del Cliente, comprendente la versione del Contratto accettata, a titolo di prova."
        ]},
        {"heading": "Articolo 22 — Diritto applicabile e foro competente", "paragraphs": [
            "Il presente Contratto è disciplinato dal diritto svizzero, ad esclusione delle sue norme di conflitto di leggi e della Convenzione delle Nazioni Unite sui contratti di vendita internazionale di merci.",
            "Qualsiasi controversia derivante dal presente Contratto o in relazione con esso è di competenza esclusiva dei tribunali ordinari del domicilio o della sede di Legatis, fatte salve le disposizioni imperative del diritto svizzero che prevedono un foro diverso, in particolare in materia di protezione dei consumatori qualora queste dovessero applicarsi."
        ]},
        {"heading": "Articolo 23 — Disposizioni finali", "paragraphs": [
            "Il presente Contratto costituisce l'integralità dell'accordo delle Parti relativo alla creazione e alla gestione gratuita del Sito, e prevale su qualsiasi accordo o scambio precedente avente il medesimo oggetto, fatte salve le condizioni generali di utilizzo di Legatis applicabili peraltro all'iscrizione del Cliente all'elenco.",
            "Il fatto che una delle Parti non si avvalga, in un dato momento, di un inadempimento dell'altra Parte a una delle clausole del presente Contratto non può essere interpretato come una rinuncia ad avvalersi, in futuro, di detto inadempimento o di qualsiasi altra clausola del Contratto.",
            "Accettando il presente Contratto, il Cliente conferma di avere la capacità giuridica di contrarre e di agire in nome proprio oppure di essere debitamente autorizzato a impegnare l'entità per conto della quale contrae, se del caso."
        ]}
    ],
},
    "en": {
    "title": "Agreement for the Free Creation and Management of a Professional Website",
    "parties_label": "Between Legatis, a Swiss lawyer-referencing platform operated as a sole proprietorship by Mr. Grégoire Giuliano (hereinafter \"Legatis\" or the \"Provider\"), and the lawyer identified by the identity-verification request to which this agreement is attached (hereinafter the \"Lawyer\" or the \"Client\"), hereinafter jointly the \"Parties\".",
    "preamble": [
        "Legatis operates an online directory of lawyers in Switzerland as well as, for those lawyers who wish to use it, a service for the creation and hosting of an individual professional website. This agreement (hereinafter the \"Agreement\") is intended to define the conditions under which Legatis provides this service to the Client free of charge, as well as the rights that the Client grants to Legatis in return.",
        "Legatis pursues an objective of modernizing the legal profession in Switzerland: many competent lawyers, in particular those in small firms or practising alone, currently have no satisfactory professional online presence, for lack of time, technical skills or a dedicated budget. By making available, free of charge, the design, publication and technical hosting of a website, Legatis intends to fill this gap and to contribute to a better digital visibility of the profession.",
        "This free-of-charge service is not devoid of consideration for Legatis: it enables Legatis to promote its brand, expand its audience, demonstrate its technical know-how to the profession, and develop its activity of connecting lawyers with members of the public. The Client expressly acknowledges and accepts that this consideration, described in detail in the following articles, constitutes the economic cause of the gratuitous nature of the initial service.",
        "The Client declares having read the entirety of this Agreement before accepting it, having had the opportunity to ask Legatis any questions prior to acceptance, and accepting the Agreement in full knowledge of the facts, without being otherwise compelled to do so: acceptance of this Agreement is entirely optional and its refusal has no bearing on the continuation of the identity-verification request and account-creation process on Legatis, nor on the Client's presence in the Legatis directory."
    ],
    "articles": [
        {"heading": "Article 1 — Definitions", "paragraphs": [
            "\"Site\" means the individual website designed, developed and published by Legatis on behalf of the Client within the framework of this Agreement, comprising its structure, design and code, as well as its content as provided or approved by the Client.",
            "\"Initial Service\" means the graphic design, technical development and initial publication of the Site, provided free of charge by Legatis in accordance with Article 3.",
            "\"Modifications\" means any intervention on the Site subsequent to its initial publication, whether requested by the Client or decided upon by Legatis on its own initiative.",
            "\"Domain Name\" means the internet address (for example \"www.name-of-the-firm.ch\") under which the Site is accessible to the public.",
            "\"Lead\" means any contact request, message, appointment request or contact details transmitted by a visitor to the Site or to the Legatis directory, which may constitute a business opportunity for the Client or for a third party.",
            "\"Third Parties\" or \"partners\" means any natural or legal person, other than the Client and Legatis, with whom Legatis maintains a business or partnership relationship, including other lawyers, law firms, or legal or non-legal services."
        ]},
        {"heading": "Article 2 — Purpose of the Agreement", "paragraphs": [
            "This Agreement is intended to define the conditions under which Legatis provides the Client with the Initial Service described in Article 4, as well as the rights of exploitation, management, modification and enhancement that the Client grants to Legatis over the Site in consideration for this gratuitousness.",
            "This Agreement is distinct and independent from the Client's registration in the Legatis directory and from the accompanying identity-verification procedure. Refusal of this Agreement in no way affects the Client's registration in the Legatis directory or the Client's login account."
        ]},
        {"heading": "Article 3 — Gratuitousness of the Initial Service", "paragraphs": [
            "The Initial Service, as described in Article 4, is provided by Legatis to the Client without direct financial consideration. No amount is invoiced to the Client for the design, development and initial publication of the Site.",
            "This gratuitousness does not extend to elements expressly excluded by this Agreement, in particular the Domain Name (Article 8) and Modifications requested by the Client after the initial publication (Article 7), which are subject to separate invoicing in accordance with the terms described below.",
            "Legatis reserves the right to end the gratuitousness of all or part of its services for new clients at any time, without this affecting the conditions applicable to Sites already published at the time of such change, unless otherwise agreed by the Parties."
        ]},
        {"heading": "Article 4 — Description of the Initial Service", "paragraphs": [
            "The Initial Service includes: (i) a prior interview or exchange with the Client in order to gather the Client's professional information, textual content, any photographs, and aesthetic preferences to the extent compatible with the templates offered by Legatis; (ii) the graphic design of the Site based on templates and components developed by Legatis; (iii) the integration of content provided or approved by the Client; (iv) the technical publication of the Site on the hosting infrastructure chosen by Legatis; and (v) a basic search-engine-optimization configuration.",
            "Legatis endeavours to deliver the Initial Service within a reasonable time after acceptance of this Agreement, without however committing to any specific deadline, the Initial Service being provided free of charge and, as such, not subject to any obligation of result as to timing.",
            "The Client undertakes to provide Legatis, within a reasonable time after being requested to do so, with all information, texts, images and authorizations necessary for the creation of the Site, in particular regarding the right to use any photograph or text transmitted to Legatis."
        ]},
        {"heading": "Article 5 — Editorial and technical control of the Site", "paragraphs": [
            "The Client acknowledges and accepts that Legatis retains, throughout the term of this Agreement, full editorial and technical control over the Site. Accordingly, Legatis has the right, in its sole discretion and without having to obtain the Client's prior consent, to add, modify, reorganize or delete all or part of the content, design, structure or functionality of the Site.",
            "This control includes, in particular, Legatis's right to make corrections, technical or security updates, overall aesthetic changes applied to all of the sites it manages for its clients, as well as any modification that Legatis deems necessary for the proper maintenance, legal compliance or image of the Legatis platform as a whole.",
            "Legatis endeavours, to the extent reasonable, to inform the Client of substantial modifications made to the Site on its own initiative, without however such notice constituting a condition of the validity of such modifications.",
            "Legatis also reserves the right to suspend access to the Site or to withdraw it entirely from publication, in particular in the event of the Client's breach of this Agreement, cessation of the Client's activity as a lawyer, the Client's disbarment, unlawful content or content contrary to professional ethics, non-payment of fees owed under this Agreement, or termination of the Agreement under the conditions of Article 15."
        ]},
        {"heading": "Article 6 — Addition, modification and deletion of the Site by Legatis", "paragraphs": [
            "Without prejudice to Article 5, Legatis may, at any time and in its sole discretion, decide to remove the Site altogether, in particular for technical, commercial, economic or strategic reasons of its own, subject to reasonable notice given to the Client by any suitable means, except in cases of urgency or serious cause, where removal may be immediate.",
            "In the event that Legatis removes the Site on its own initiative for reasons other than a breach by the Client, Legatis endeavours, to the extent possible and without being obliged to do so, to provide the Client with a reasonable export of the Site's textual content as it existed at the time of removal.",
            "The Client may not claim any compensation whatsoever on account of Legatis's exercise of the rights of control, modification or deletion described in this Article and in Article 5, subject to the mandatory provisions of Swiss law that cannot be contractually excluded."
        ]},
        {"heading": "Article 7 — Modifications requested by the Client (paid services)", "paragraphs": [
            "Any Modification of the Site requested by the Client after its initial publication, whether relating to content, design, structure or functionality, constitutes a service distinct from the Initial Service and is invoiced by Legatis, unless expressly agreed otherwise.",
            "Legatis provides the Client, upon request, with a price or quote for any requested Modification before carrying it out. No paid Modification is carried out without the Client's prior agreement as to the principle and amount of the invoicing, it being specified that this prior agreement does not apply to modifications that Legatis carries out on its own initiative pursuant to Article 5 or 6, which remain free of charge for the Client.",
            "The rates applicable to Modifications are those communicated by Legatis at the time of the request, Legatis reserving the right to change its pricing schedule at any time for future requests.",
            "In the absence of payment of amounts due for invoiced Modifications, Legatis may suspend the carrying out of new Modifications until the situation is regularized, without this affecting the continued publication of the Site as it exists."
        ]},
        {"heading": "Article 8 — Domain Name", "paragraphs": [
            "If the Client wishes the Site to be accessible under a dedicated Domain Name (for example, the name of the Client's firm), the registration and periodic renewal of that Domain Name are the exclusive financial responsibility of the Client, including where Legatis technically carries out such registration on the Client's behalf for the sake of simplicity.",
            "In the absence of a dedicated Domain Name, or in the event of non-renewal by the Client, the Site remains or again becomes accessible under a generic address provided by Legatis (for example, a subdomain of the legatis.ch website), at no additional cost to the Client.",
            "In the event of termination of this Agreement or removal of the Site at the initiative of either Party, ownership of the Domain Name, where it has been registered in the Client's name and paid for by the Client, remains vested in the Client, subject to settlement of any outstanding balance."
        ]},
        {"heading": "Article 9 — Hosting and availability", "paragraphs": [
            "Legatis hosts the Site on a technical infrastructure of its choosing, which it may change or modify at any time without requiring the Client's agreement, provided that the Site remains accessible to the public under equivalent conditions.",
            "Legatis implements reasonable means to ensure satisfactory availability of the Site, without however guaranteeing uninterrupted availability, the Site being liable to temporary interruptions for maintenance, updates, or for reasons beyond Legatis's reasonable control (failure of a third-party provider, security incident, force majeure within the meaning of Article 17)."
        ]},
        {"heading": "Article 10 — Search engine ranking, backlinks and visibility of Legatis", "paragraphs": [
            "In consideration for the gratuitousness of the Initial Service, the Client grants Legatis the right to include on the Site, in a visible manner, one or more hyperlinks (\"backlinks\") pointing to the legatis.ch website, to the Client's profile on the Legatis directory, or to other pages or services operated by Legatis, as well as a mention such as \"site created by Legatis\" or equivalent.",
            "The Client authorizes Legatis to mention and, where applicable, to present the Site (screenshots, excerpts, link) as a commercial reference or a demonstration of its know-how, in particular to other lawyers who may be interested in a similar service, subject to compliance with the confidentiality obligations set out in Article 14 with respect to non-public information.",
            "The Client acknowledges that these links and mentions form part of the economic consideration justifying the gratuitousness of the Initial Service and may request their removal only in connection with a termination of this Agreement, which then entails the consequences described in Article 15."
        ]},
        {"heading": "Article 11 — Generation, management and transmission of leads", "paragraphs": [
            "The Site and, more broadly, the Legatis directory in which the Client appears, are liable to generate Leads, in particular via contact forms, requests for referral, or comparison tools made available on the legatis.ch website.",
            "The Client authorizes Legatis to collect, manage and transmit to the Client Leads that directly concern the Client, in compliance with the applicable data-protection legislation (Article 13).",
            "The Client further acknowledges that Legatis, within the framework of its activity as a matchmaking platform, may direct, share or transmit to Third Parties requests, information or Leads that do not specifically and exclusively concern the Client — in particular where a visitor makes a general request that may be of interest to several lawyers, where the Client is unable to respond to a request, or in connection with ancillary services offered by Legatis or its partners. This ability confers on the Client no exclusivity over Leads generated via the Legatis directory or the Site.",
            "Legatis does not guarantee any volume, frequency or minimum quality of Leads transmitted to the Client, the Initial Service and this Agreement in no way constituting a commitment of commercial results in favour of the Client."
        ]},
        {"heading": "Article 12 — Intellectual property", "paragraphs": [
            "The source code, templates, graphic components, technical functionalities and, more generally, any element of the Site designed or developed by Legatis independently of the Client's specific content, remain the exclusive property of Legatis, including after the Site is published.",
            "Content specific to the Client (the Client's name, personal presentation, contact details, texts and photographs personally provided by the Client and of which the Client is the author or rights holder) remains the property of the Client, subject to the right of use granted to Legatis for the purposes of performing this Agreement, in particular its display on the Site and on the Legatis directory.",
            "The Client warrants to Legatis that the Client holds all rights necessary in respect of the content it provides (texts, photographs, logos) and indemnifies Legatis against any third-party claim relating to an infringement of intellectual property or personality rights arising from such content.",
            "In the event of termination of this Agreement, Legatis retains the right to use the templates, components and technical know-how developed in connection with the creation of the Site for other clients, excluding the Client's specific content and personal information."
        ]},
        {"heading": "Article 13 — Data protection", "paragraphs": [
            "Legatis processes the personal data of the Client and of the Site's visitors in accordance with the Federal Act on Data Protection (FADP) and its revision (revFADP), as well as the provisions of Legatis's privacy policy, available on the legatis.ch website.",
            "Lead data transmitted to the Client under Article 11 may only be used by the Client for the purposes of the Client's own professional activity, in compliance with the professional-conduct rules applicable to lawyers and with data-protection legislation.",
            "The Client remains solely responsible, in its capacity as a lawyer, for compliance with professional secrecy and with the data-protection rules applicable to its own activity, independently of Legatis's obligations under this Article."
        ]},
        {"heading": "Article 14 — Confidentiality", "paragraphs": [
            "Each Party undertakes to keep confidential any non-public information of which it becomes aware in connection with the performance of this Agreement, and to use it only for the purposes of such performance, unless otherwise agreed in writing or required by law.",
            "This confidentiality obligation does not preclude Legatis from exercising the rights of communication and promotion of the Site set out in Article 10, such rights by nature relating to information made public through the publication of the Site itself."
        ]},
        {"heading": "Article 15 — Term and termination", "paragraphs": [
            "This Agreement is entered into for an indefinite term as from its acceptance by the Client, and remains in force for as long as the Site continues to be hosted by Legatis.",
            "Either Party may terminate this Agreement at any time, subject to reasonable notice given to the other Party in writing (including by email), without having to state any particular reason.",
            "In the event of termination at the initiative of the Client, the Client acknowledges that the Site, as a technical and graphic work of Legatis, ceases to be hosted and made accessible to the public through Legatis, without prejudice to the ownership of the Client's specific content as defined in Article 12.",
            "Termination of this Agreement has no effect on the Client's registration in the Legatis directory or on the Client's login account, which remain governed by Legatis's general terms of use."
        ]},
        {"heading": "Article 16 — Liability and warranties", "paragraphs": [
            "As the Initial Service is provided free of charge, Legatis is, to the extent permitted by Swiss law, subject only to a best-efforts obligation and not an obligation of result, and its liability may only be engaged in the event of intentional misconduct or gross negligence.",
            "Legatis does not guarantee either the total absence of errors, failures or unavailability of the Site, or any commercial outcome (number of visitors, Leads, new clients) resulting from the publication of the Site.",
            "In any event, Legatis's liability, should it be engaged, is limited to direct and foreseeable damages, excluding any indirect damage (loss of clientele, loss of a chance, harm to reputation), and this within the limits permitted by the mandatory provisions of Swiss law, in particular Article 100 of the Swiss Code of Obligations relating to liability for wilful misconduct or gross negligence, which cannot be excluded by agreement.",
            "The Client remains solely responsible for the content it provides or approves for publication on the Site, in particular its compliance with the professional-conduct rules of the legal profession and the legal provisions relating to lawyer advertising."
        ]},
        {"heading": "Article 17 — Force majeure", "paragraphs": [
            "Neither Party may be held liable for a failure to perform its obligations under this Agreement where such failure results from a case of force majeure, understood as any external, unforeseeable and irresistible event within the meaning of Swiss case law, in particular a natural disaster, a major and widespread failure of internet infrastructure, a large-scale cyberattack, or a decision of a public authority."
        ]},
        {"heading": "Article 18 — Assignment of the Agreement", "paragraphs": [
            "Legatis may assign this Agreement, together with all rights and obligations arising therefrom, to any entity that takes over all or part of its business, subject to prior notice to the Client.",
            "The Client may not assign this Agreement to a third party without the prior written consent of Legatis, the Agreement having been entered into in consideration of the Client's identity as a lawyer registered in the Legatis directory."
        ]},
        {"heading": "Article 19 — Amendment of this Agreement", "paragraphs": [
            "Legatis may amend the terms of this Agreement for the future, in particular to take account of legal, technical or commercial developments. Substantial amendments are communicated to the Client by any suitable means and are deemed accepted if the Client does not object within a reasonable time or continues to benefit from Legatis's services after they take effect.",
            "If the Client does not accept a substantial amendment, the Client may terminate this Agreement under the conditions of Article 15."
        ]},
        {"heading": "Article 20 — Partial invalidity", "paragraphs": [
            "Should any clause of this Agreement be held void, unlawful or unenforceable by a competent authority, the other clauses of the Agreement remain in full force and effect. The Parties shall then endeavour to replace the invalidated clause with a valid clause whose economic effect comes as close as possible to that of the invalidated clause."
        ]},
        {"heading": "Article 21 — Electronic acceptance and evidence", "paragraphs": [
            "The Client accepts this Agreement by scrolling through its entire text, ticking the confirmation box provided for that purpose, and then clicking the acceptance button provided on the Legatis interface.",
            "The Client acknowledges that this electronic acceptance constitutes a valid expression of intent and binds the Client legally in the same manner as a handwritten signature, in accordance with the general principles of Swiss contract law relating to freedom of form (Article 10 of the Swiss Code of Obligations), subject to legal provisions requiring a particular form for certain acts.",
            "Legatis retains a time-stamped record of the Client's acceptance, including the version of the Agreement accepted, as evidence."
        ]},
        {"heading": "Article 22 — Governing law and jurisdiction", "paragraphs": [
            "This Agreement is governed by Swiss law, to the exclusion of its conflict-of-laws rules and of the United Nations Convention on Contracts for the International Sale of Goods.",
            "Any dispute arising out of or in connection with this Agreement falls within the exclusive jurisdiction of the ordinary courts of Legatis's domicile or registered office, subject to the mandatory provisions of Swiss law providing for a different forum, in particular in matters of consumer protection should such provisions apply."
        ]},
        {"heading": "Article 23 — Final provisions", "paragraphs": [
            "This Agreement constitutes the entire agreement of the Parties regarding the free creation and management of the Site, and prevails over any prior agreement or exchange relating to the same subject matter, subject to Legatis's general terms of use otherwise applicable to the Client's registration in the directory.",
            "The fact that either Party does not, at a given point in time, invoke a breach by the other Party of any clause of this Agreement may not be construed as a waiver of the right to invoke, in the future, that breach or any other clause of the Agreement.",
            "By accepting this Agreement, the Client confirms having the legal capacity to contract and acting in the Client's own name, or duly authorized to bind the entity on whose behalf the Client is contracting, as the case may be."
        ]}
    ],
},
}
