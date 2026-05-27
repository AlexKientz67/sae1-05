# --------------------------------------------------------
# Script : script_3_affichage_ihm.py
# SAÉ 1.05 - Script Python #3
# Rôle   : lire report.json et afficher l'IHM (onglets + camembert + légendes)
#          + générer un script PowerShell de suppression (cases cochées)
# --------------------------------------------------------

import json
import random
import sys
from pathlib import Path

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication

# Les 4 fichiers fournis par le sujet sont dans ./sujet/
SUJET_DIR = Path(__file__).resolve().parent / "sujet"
if str(SUJET_DIR) not in sys.path:
    sys.path.insert(0, str(SUJET_DIR))

from Creation_Onglets import Onglets
from Creation_Camembert import Camembert
from Creation_Legendes import Legendes
from Creation_Boutons import Boutons

NB_LEGENDES_PAR_PAGE = 25


def lit_json(chemin_json):
    path = Path(chemin_json).expanduser().resolve()
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def genere_couleurs(nb):
    return [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(nb)]


def ecrit_script_suppression(liste_fichiers_a_supprimer, chemin_ps1):
    lignes = [
        'Write-Output "Script PowerShell pour supprimer des fichiers sans confirmation"',
        'Write-Output "Attention : cette suppression est definitivement ..."',
        '$reponse = Read-Host "Veuillez confirmer la suppression de tous ces fichiers : (OUI)"',
        'if ($reponse -eq "OUI") {',
        '  $confirmation = Read-Host "Etes-vous bien certain(e) ? (OUI)"',
        '  if ($confirmation -eq "OUI") {'
    ]
    for path_str in liste_fichiers_a_supprimer:
        lignes.append(f'    Remove-Item -Path "{path_str}" -Force')
    lignes += [
        '  } else {',
        '    Write-Output "Operation annulee..."',
        '  }',
        '} else {',
        '  Write-Output "Operation annulee..."',
        '}'
    ]
    open(chemin_ps1, "w", encoding="utf-8").write("\n".join(lignes) + "\n")


def main():
    app = QApplication(sys.argv)
    liste_fichiers = lit_json(sys.argv[1])
    couleurs = genere_couleurs(len(liste_fichiers))

    fenetre = Onglets()

    # Onglet camembert
    fromage = Camembert(liste_fichiers, couleurs)
    layout_fromage = fromage.dessine_camembert()
    fenetre.add_onglet("Camembert", layout_fromage)

    # Onglets légendes (25 par page)
    pages_legendes = []
    nb_pages = (len(liste_fichiers) + NB_LEGENDES_PAR_PAGE - 1) // NB_LEGENDES_PAR_PAGE
    for page in range(nb_pages):
        start = page * NB_LEGENDES_PAR_PAGE
        obj = Legendes(liste_fichiers, couleurs, start, NB_LEGENDES_PAR_PAGE)
        pages_legendes.append(obj)
        layout_leg = obj.dessine_legendes()
        fenetre.add_onglet(f"Legende {page + 1}", layout_leg)

    # Onglet IHM (bouton)
    def on_click():
        fichiers_a_supprimer = []
        for page_idx, page_obj in enumerate(pages_legendes):
            etats = page_obj.recupere_etats_cases_a_cocher()
            start_idx = page_idx * NB_LEGENDES_PAR_PAGE
            for offset, checked in enumerate(etats):
                if checked:
                    fichiers_a_supprimer.append(liste_fichiers[start_idx + offset][0])
        ecrit_script_suppression(fichiers_a_supprimer, "delete_selected.ps1")

    ihm = Boutons(sys.argv[2], on_click)
    layout_ihm = ihm.dessine_boutons()
    fenetre.add_onglet("IHM", layout_ihm)

    fenetre.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
