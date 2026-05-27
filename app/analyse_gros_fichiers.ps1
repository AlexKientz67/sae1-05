<#
  Script : analyse_gros_fichiers.ps1
  Objectif minimal: enchaîner les 3 scripts Python avec une seule vérification:
  - ne continuer que si le dossier sélectionné existe
#>

# Paramètres de base
$MIN_SIZE_MIB = 1
$MAX_FILES = 100

# Se placer dans le dossier du script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$jsonOut = Join-Path $scriptDir "report.json"

# 1) Sélection du répertoire
$rep_base = & py (Join-Path $scriptDir "script_1_selection_repertoire.py")

# le dossier doit exister
if (-not (Test-Path -LiteralPath $rep_base)) {
  Write-Output "Repertoire invalide ou non selectionne: $rep_base"
  exit 1
}

# 2) Scan + JSON
& py (Join-Path $scriptDir "script_2_scan_et_json.py") "$rep_base" $MIN_SIZE_MIB $MAX_FILES "$jsonOut"

# 3) IHM depuis JSON
& py (Join-Path $scriptDir "script_3_affichage_ihm.py") "$jsonOut" "$rep_base"
