# --------------------------------------------------------
# Script : script_1_selection_repertoire.py
# SAÉ 1.05 - Script Python #1
# Rôle   : Laisser l'utilisateur choisir le répertoire_de_base
# Contraintes sujet : QFileDialog.getExistingDirectory(...)
# Sortie : imprime le chemin choisi (stdout) pour PowerShell
# --------------------------------------------------------

import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QFileDialog


def choisir_repertoire():
    dossier = QFileDialog.getExistingDirectory(None, "Sélectionnez le répertoire de base", "")
    if dossier:
        return str(Path(dossier).resolve())
    return ""


def main():
    app = QApplication(sys.argv)
    rep_base = choisir_repertoire()
    print(rep_base)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
