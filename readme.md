# SAÉ 1.05 – Outil de Reporting pour les Gros Fichiers

Projet réalisé par **Kientz Alexandre**, **Erb Louis** et **Legoll Benjamin**.

---

## 📌 Présentation

L’objectif du projet est de créer un outil permettant d’identifier les fichiers les plus volumineux présents sur un disque afin d’aider à libérer de l’espace de stockage.

Le programme :

- analyse un répertoire choisi par l’utilisateur,
- détecte les fichiers dépassant une taille minimale,
- trie les fichiers par taille décroissante,
- affiche les résultats graphiquement,
- permet de sélectionner des fichiers,
- génère un script PowerShell de suppression.

---

# ⚙️ Technologies utilisées

- **PowerShell**
- **Python 3**
- **PyQt5** (interface graphique)
- **JSON** (échange de données)

---

# 🧩 Structure du projet

## 1. Script PowerShell

Le script principal :

- initialise les paramètres,
- lance les scripts Python,
- récupère les données,
- coordonne l’ensemble du programme.

### Fonctionnalités principales

```powershell
# Sélection du répertoire
# Scan des fichiers
# Génération du JSON
# Affichage de l’interface graphique
```

---

## 2. Premier script Python

Ce script permet à l’utilisateur de choisir le répertoire à analyser grâce à une fenêtre graphique PyQt5.

### Fonctionnement

- ouverture d’une boîte de dialogue,
- récupération du chemin absolu,
- transmission au script principal.

---

## 3. Deuxième script Python

Ce script réalise l’inventaire des fichiers :

- parcours récursif du dossier,
- récupération des tailles,
- tri des fichiers,
- filtrage selon une taille minimale,
- export des données au format JSON.

### Fonctionnalités

```python
def inventaire_fichiers():
    pass

def tri_decroissant_par_taille():
    pass

def filtre_taille():
    pass

def ecrit_json():
    pass
```

---

## 4. Troisième script Python

Ce script gère l’interface graphique principale.

### Fonctionnalités

- affichage des fichiers,
- génération d’un diagramme circulaire,
- pagination des résultats,
- sélection des fichiers,
- génération d’un script `.ps1` de suppression.

Le script PowerShell généré demande une confirmation avant suppression définitive des fichiers.

---

# 📊 Fonctionnement global

1. L’utilisateur choisit un dossier.
2. Les fichiers sont analysés.
3. Les 100 plus gros fichiers sont récupérés.
4. Les données sont triées et affichées.
5. L’utilisateur peut sélectionner des fichiers.
6. Un script PowerShell de suppression est généré.

---

# 🖥️ Interface graphique

Le programme contient :

- un graphique camembert des tailles de fichiers,
- une liste détaillée des fichiers détectés,
- une interface de sélection,
- un système de suppression sécurisé.

---

# ⚠️ Avertissement

Ce logiciel est destiné à des utilisateurs avertis.

La suppression de fichiers système peut provoquer des dysfonctionnements importants du système d’exploitation.

---

# 🚀 Lancement du projet

## Prérequis

- Python 3
- PyQt5
- Windows PowerShell

## Installation

```bash
pip install pyqt5
```

## Exécution

Lancer le script PowerShell principal :

```powershell
powershell -ExecutionPolicy Bypass -File analyse_gros_fichiers.ps1
```

---

# 📁 Exemple d’arborescence

```text
project/
│
├── analyse_gros_fichiers.ps1
├── script_1_selection_repertoire.py
├── script_2_scan_et_json.py
├── script_3_affichage_ihm.py
├── report.json
└── delete_selected.ps1
```

---

# ✅ Conclusion

Ce projet permet d’automatiser la recherche des fichiers volumineux et facilite le nettoyage d’un disque grâce à une interface graphique intuitive et un système de suppression contrôlé.
