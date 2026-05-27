# SAÉ 1.05 — Outil de reporting « gros fichiers »

Projet conforme au sujet : chaînage PowerShell + 3 scripts Python simples.

## Contenu

- `sujet/` : scripts fournis (NON MODIFIÉS) : `Creation_Onglets.py`, `Creation_Camembert.py`, `Creation_Legendes.py`, `Creation_Boutons.py`
- `script_1_selection_repertoire.py` : sélection du répertoire (QFileDialog.getExistingDirectory)
- `script_2_scan_et_json.py` : scan récursif + tri + filtre/limite + JSON
- `script_3_affichage_ihm.py` : IHM (onglets + camembert + légendes) + génération du script de suppression
- `analyse_gros_fichiers.ps1` : script PowerShell de chaînage (obligatoire)

## Installation

```powershell
cd C:\Users\louiserb\Desktop\super\main
python -m pip install -r requirements.txt
```

Alternative (recommandé) : lancez directement le script PowerShell, il crée un venv local `.venv` et installe automatiquement les dépendances si besoin.

## Exécution (Windows)

```powershell
cd C:\Users\louiserb\Desktop\super\main
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; .\analyse_gros_fichiers.ps1
```

## Notes

- Le script #2 produit `report.json` (liste de listes `[chemin, taille_en_octets]`).
- L'IHM (script #3) lit le JSON et génère `delete_selected.ps1` dans le dossier courant.
