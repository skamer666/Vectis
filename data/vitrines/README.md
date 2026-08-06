# Vitrines avocat -- schema de donnees

Chaque soumission est un fichier JSON `{slug}.json`, ou `{slug}` est un
identifiant unique (nom-prenom-canton, genere par le formulaire).

## Cycle de vie

1. L'avocat remplit le formulaire sur /vitrine-avocat/ (ou equivalent par
   langue). La fonction serverless (api/vitrine-submit.js) ecrit le fichier
   dans `pending/{slug}.json` via l'API GitHub, et enregistre la photo dans
   `static/vitrines/photos/{slug}.jpg`.
2. Greg (ou Claude) revoit la demande sur la page interne de revision
   (noindex), en regardant l'apercu rendu avec le template choisi.
3. Une fois valide (et apres le rdv Google My Business le cas echeant), le
   fichier est deplace de `pending/` vers `approved/` (manuellement, via un
   commit -- aucune automatisation de la validation elle-meme).
4. Au build suivant, `gen_vitrines()` dans build.py lit tous les fichiers de
   `approved/` et genere une page publique par avocat, dans les 4 langues.

## Schema JSON

```json
{
  "slug": "prenom-nom-canton",
  "submitted_at": "2026-08-06T14:32:00Z",
  "status": "pending",

  "registry_match": {
    "nom_complet": "Prenom Nom",
    "canton": "GE",
    "source_avocat_slug": "prenom-nom",
    "verified": false
  },

  "template": "prestige",

  "locked": {
    "nom_complet": "Prenom Nom",
    "canton": "GE",
    "canton_name": "Geneve",
    "ville": "Geneve",
    "annee_inscription": null,
    "langues": ["fr", "en"]
  },

  "free": {
    "photo_filename": "prenom-nom-geneve.jpg",
    "accroche": "Une phrase d'accroche courte, choisie par l'avocat.",
    "bio": "Texte de presentation libre, redige par l'avocat lui-meme.",
    "citation": "Une citation ou philosophie professionnelle (optionnel).",
    "specialites": ["droit-famille", "droit-travail"],
    "site_web": "https://exemple-cabinet.ch",
    "linkedin": "https://www.linkedin.com/in/...",
    "accent_color": "bordeaux",
    "sections_actives": ["citation", "distinctions"],
    "distinctions": ["Mention Meilleurs Avocats 2025"]
  },

  "contact_email": "avocat@exemple-cabinet.ch",
  "contact_phone": "+41 22 000 00 00"
}
```

Champs `locked.*` : jamais modifiables par le formulaire, toujours tires du
registre cantonal deja scrape (`registry_match.source_avocat_slug` pointe
vers l'entree existante). Champs `free.*` : remplis librement par l'avocat,
mais `specialites` reste une liste fermee (memes IDs que `i18n.DOMAINES`),
pas de texte libre, pour rester coherent avec le reste du site.
