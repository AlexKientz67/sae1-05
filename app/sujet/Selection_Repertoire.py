# --------------------------------------------------------
# Script : Selection_Repertoire.py
# Destiné à la SAE 1.05 : traitement des données
# Rôle   : Script #1 - Sélection du répertoire de base
# --------------------------------------------------------

from __future__ import annotations

import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QFileDialog


def selectionne_repertoire_base(repertoire_initial: str | None = None) -> str:
    """Ouvre un sélecteur de répertoire et retourne le chemin sélectionné.

    Retour:
        - Chemin absolu (str) du répertoire sélectionné
        - Chaîne vide si l'utilisateur annule

    Notes:
        - Utilise QFileDialog.getExistingDirectory(...) comme demandé.
        - Le retour est un *texte* pour pouvoir être récupéré facilement via PowerShell.
    """
    initial_dir = ""
    if repertoire_initial:
        try:
            initial_dir = str(Path(repertoire_initial).expanduser().resolve())
        except Exception:
            initial_dir = ""

    dossier = QFileDialog.getExistingDirectory(
        None,
        "Sélectionnez le répertoire de base",
        initial_dir,
    )

    if not dossier:
        return ""

    # Normalisation en chemin absolu
    try:
        return str(Path(dossier).expanduser().resolve())
    except Exception:
        return str(dossier)


def main(argv: list[str]) -> int:
    # Prépare l'environnement graphique Qt (obligatoire pour QFileDialog)
    app = QApplication(argv)

    repertoire_initial = argv[1] if len(argv) > 1 else None
    dossier = selectionne_repertoire_base(repertoire_initial)

    # IMPORTANT : renvoyer le résultat sur stdout pour PowerShell
    # - Si annulation: on imprime une ligne vide
    print(dossier)

    # Sur annulation on retourne un code non-zéro (pratique côté PowerShell)
    return 0 if dossier else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

