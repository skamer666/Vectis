# -*- coding: utf-8 -*-
"""Regenere data/avocats_tessin.csv a partir de TOUS les fichiers
sources/ti_raw/batchNN.txt (un fichier par lot de pages scrapees depuis le
registre cantonal tessinois -- www4.ti.ch/poteri/giudiziario/avvocatura-e-
notariato/registro-cantonale-avvocati). Format d'une ligne source :
"Avv. NOM|adresse combinee|date_iscrizione". Ne fabrique rien : si npa/ville
ou etude ne sont pas identifiables dans l'adresse, les champs restent vides
plutot que devines (voir registry_parse_common.parse_address).

Usage : python3 sources/build_ti_csv.py
Combine tous les sources/ti_raw/batch*.txt (tries par nom de fichier =
ordre de scraping = ordre des pages), deduplique par nom+adresse (au cas ou
un lot chevaucherait un precedent), ecrit data/avocats_tessin.csv."""
import csv
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sources.registry_parse_common import parse_address

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def split_name(raw_name):
    # "Avv. NOM Prenom" ou "Avv. dr. NOM Prenom" -> on retire le prefixe "Avv."
    name = raw_name.strip()
    name = re.sub(r"(?i)^avv\.\s*", "", name).strip()
    return name


def main():
    batch_files = sorted(glob.glob(os.path.join(ROOT, "sources", "ti_raw", "batch*.txt")))
    if not batch_files:
        print("Aucun fichier sources/ti_raw/batch*.txt trouve.")
        return

    seen = set()
    rows = []
    for bf in batch_files:
        with open(bf, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line.strip():
                    continue
                parts = line.split("|")
                if len(parts) != 3:
                    print(f"Ligne ignoree (format inattendu) dans {bf}: {line!r}")
                    continue
                raw_name, raw_addr, date_iscrizione = parts
                nom_complet = split_name(raw_name)
                key = (nom_complet, raw_addr)
                if key in seen:
                    continue
                seen.add(key)
                etude, adresse, npa, ville = parse_address(raw_addr)
                rows.append({
                    "nom_complet": nom_complet,
                    "etude": etude,
                    "adresse": adresse,
                    "npa": npa,
                    "ville": ville,
                    "date_inscription": date_iscrizione.strip(),
                    "canton": "TI",
                })

    out_path = os.path.join(ROOT, "data", "avocats_tessin.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["nom_complet", "etude", "adresse", "npa", "ville", "date_inscription", "canton"])
        w.writeheader()
        w.writerows(rows)

    n_npa = sum(1 for r in rows if r["npa"])
    n_etude = sum(1 for r in rows if r["etude"])
    print(f"{len(rows)} avocats ecrits dans {out_path} (depuis {len(batch_files)} lot(s))")
    print(f"{n_npa}/{len(rows)} avec npa/ville identifie")
    print(f"{n_etude}/{len(rows)} avec cabinet identifie")


if __name__ == "__main__":
    main()
