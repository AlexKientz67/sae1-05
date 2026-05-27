# ============================================================
# Script PowerShell pour supprimer des fichiers avec confirmation
# ============================================================

# Affiche un message d'avertissement initial à l'utilisateur
Write-Output "Script PowerShell pour supprimer des fichiers sans confirmation"

# Affiche un avertissement que la suppression est irréversible
Write-Output "Attention : cette suppression est definitivement ..."

# Demande la première confirmation à l'utilisateur via un dialogue
# L'utilisateur doit taper "OUI" exactement pour continuer
$reponse = Read-Host "Veuillez confirmer la suppression de tous ces fichiers : (OUI)"

# Vérifie si l'utilisateur a tapé "OUI" (comparaison exacte avec -eq)
if ($reponse -eq "OUI") {
  # Affiche un second dialogue de confirmation pour s'assurer de l'intention
  # Cette double confirmation évite les suppressions accidentelles
  $confirmation = Read-Host "Etes-vous bien certain(e) ? (OUI)"
  
  # Vérifie la réponse au second dialogue
  if ($confirmation -eq "OUI") {
    # Si l'utilisateur a confirmé deux fois, supprime le fichier spécifié
    # -Path: chemin exact du fichier à supprimer
    # -Force: force la suppression sans invite supplémentaire
    Remove-Item -Path "C:\Users\Alex\Desktop\FileZilla_3.69.5_win64_sponsored2-setup.exe" -Force
  } else {
    # Si la deuxième confirmation n'est pas "OUI", annule l'opération
    Write-Output "Operation annulee..."
  }
} else {
  # Si la première confirmation n'est pas "OUI", annule l'opération
  Write-Output "Operation annulee..."
}
