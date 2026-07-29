# -*- coding: utf-8 -*-
"""Utilitaires de parsing partages pour les registres cantonaux scrapes
manuellement (BL, AR) ou avec pagination (TI). Meme principe que dans
build.py : on separe cabinet / rue / NPA / ville a partir d'un champ adresse
combine, sans jamais inventer une donnee absente."""
import re

NPA_VILLE_RE = re.compile(r"^(\d{4})\s+(.+)$")


def parse_address(raw):
    parts = [p.strip() for p in raw.split(",")]
    if not parts:
        return "", "", "", raw
    m = NPA_VILLE_RE.match(parts[-1])
    if not m:
        return "", raw, "", ""
    npa, ville = m.group(1), m.group(2)
    remaining = parts[:-1]
    street_idx = None
    for i in range(len(remaining) - 1, -1, -1):
        seg = remaining[i]
        if re.match(r"(?i)^(postfach|casella postale|cp)\b", seg):
            continue
        if re.search(r"\d", seg):
            street_idx = i
            break
    if street_idx is None:
        etude = ", ".join(remaining).strip()
        return etude, "", npa, ville
    street = remaining[street_idx]
    firm_parts = [p for j, p in enumerate(remaining) if j != street_idx and not re.match(r"(?i)^(postfach|casella postale|cp)\b", p)]
    etude = ", ".join(firm_parts).strip()
    # "c/o Nom du cabinet" -- convention d'adresse (chez/aux bons soins de),
    # pas une partie du nom lui-meme : on la retire pour un affichage propre,
    # sans changer le nom reel du cabinet.
    etude = re.sub(r"(?i)^c/o\s+", "", etude).strip()
    return etude, street, npa, ville


def split_name_title(raw_name):
    if "," in raw_name:
        nom, titre = raw_name.split(",", 1)
        return nom.strip(), titre.strip()
    return raw_name.strip(), ""
