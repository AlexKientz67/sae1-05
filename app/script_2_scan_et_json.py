# --------------------------------------------------------
# Script : script_2_scan_et_json.py
# SAÉ 1.05 - Script Python #2
# Rôle   : scanner récursivement un répertoire_de_base
#          -> liste [[chemin_absolu, taille_octets], ...]
#          -> tri décroissant
#          -> filtre (taille mini) + limite (max 100)
#          -> écriture dans un fichier JSON
# --------------------------------------------------------

import json
import sys
from pathlib import Path


def inventorie_fichiers(repertoire_de_base):
    base = Path(repertoire_de_base).resolve()
    liste = []
    for p in base.rglob("*"):
        if p.is_file():
            liste.append([str(p.resolve()), p.stat().st_size])
    return liste


def tri_decroissant_par_taille(liste_fichiers):
    return sorted(liste_fichiers, key=lambda x: x[1], reverse=True)


def filtre_et_limite(liste_fichiers, taille_mini_mib, nb_maxi_fichiers):
    seuil_octets = taille_mini_mib * 1048576
    liste_filtre = [x for x in liste_fichiers if x[1] >= seuil_octets]
    return liste_filtre[:nb_maxi_fichiers]


def ecrit_json(liste_fichiers,chemin_json):
    with open(chemin_json, "w", encoding="utf-8") as f:
        json.dump(liste_fichiers, f, ensure_ascii=False, indent=2)


def main():
    liste = inventorie_fichiers(sys.argv[1])
    liste = tri_decroissant_par_taille(liste)
    liste = filtre_et_limite(liste, int(sys.argv[2]), int(sys.argv[3]))
    ecrit_json(liste, sys.argv[4])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
