"""Point d'entrée simple.

Pour la SAÉ 1.05, on lance normalement le projet via le script PowerShell:
  analyse_gros_fichiers.ps1

Ce fichier reste juste comme point d'entrée Python minimal.
"""

import sys

from script_3_affichage_ihm import main


if __name__ == "__main__":
    raise SystemExit(main())

