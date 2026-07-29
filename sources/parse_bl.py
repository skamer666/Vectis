# -*- coding: utf-8 -*-
"""Parse le registre des avocats de Bale-Campagne (nom + adresse combinee) en
CSV structure. Le champ adresse source est de la forme
"[Cabinet, ]Rue Numero[, Postfach ...], NPA Ville" -- on isole le cabinet (s'il
existe), la rue, le NPA et la ville. Rien n'est invente : si le format ne
correspond a aucun motif attendu, la ligne entiere est conservee telle quelle
dans le champ adresse plutot que force dans un champ qui ne convient pas."""
import csv
import re
import sys

from sources.bl_raw import BL_RAW

NPA_VILLE_RE = re.compile(r"^(\d{4})\s+(.+)$")


def parse_address(raw):
    parts = [p.strip() for p in raw.split(",")]
    if not parts:
        return "", "", "", raw
    m = NPA_VILLE_RE.match(parts[-1])
    if not m:
        # Pas de NPA+ville identifiable en fin de chaine -- on ne force rien.
        return "", raw, "", ""
    npa, ville = m.group(1), m.group(2)
    remaining = parts[:-1]
    # Cherche, en partant de la fin, le premier segment qui ressemble a une
    # rue+numero et qui n'est pas une case postale (Postfach).
    street_idx = None
    for i in range(len(remaining) - 1, -1, -1):
        seg = remaining[i]
        if re.match(r"(?i)^postfach\b", seg):
            continue
        if re.search(r"\d", seg):
            street_idx = i
            break
    if street_idx is None:
        # Aucune rue distincte trouvee (adresse tres courte) -- tout le reste
        # est traite comme "etude" absente, adresse vide plutot que devinee.
        etude = ", ".join(remaining).strip()
        return etude, "", npa, ville
    street = remaining[street_idx]
    firm_parts = [p for j, p in enumerate(remaining) if j != street_idx and not re.match(r"(?i)^postfach\b", p)]
    etude = ", ".join(firm_parts).strip()
    return etude, street, npa, ville


def split_name_title(raw_name):
    # "Nom Prenom, titre" -> on garde nom_complet=raw avant la virgule, titre=reste
    if "," in raw_name:
        nom, titre = raw_name.split(",", 1)
        return nom.strip(), titre.strip()
    return raw_name.strip(), ""


def main():
    rows = []
    for raw_name, raw_addr in BL_RAW:
        nom_complet, titre = split_name_title(raw_name)
        etude, adresse, npa, ville = parse_address(raw_addr)
        rows.append({
            "nom_complet": nom_complet,
            "titre": titre,
            "etude": etude,
            "adresse": adresse,
            "npa": npa,
            "ville": ville,
            "canton": "BL",
        })

    out_path = sys.argv[1] if len(sys.argv) > 1 else "avocats_bale_campagne.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["nom_complet", "titre", "etude", "adresse", "npa", "ville", "canton"])
        w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} lignes ecrites dans {out_path}")
    # Diagnostics : combien ont un npa/ville identifie, combien ont un cabinet
    n_npa = sum(1 for r in rows if r["npa"])
    n_etude = sum(1 for r in rows if r["etude"])
    print(f"{n_npa}/{len(rows)} avec npa/ville identifie")
    print(f"{n_etude}/{len(rows)} avec cabinet identifie")
    print()
    print("--- Echantillon (10 premiers) ---")
    for r in rows[:10]:
        print(r)
    print()
    print("--- Lignes sans npa/ville (a verifier) ---")
    for r in rows:
        if not r["npa"]:
            print(r)


if __name__ == "__main__":
    main()
