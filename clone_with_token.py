#!/usr/bin/env python3
"""
Script pour cloner le dépôt neurax en utilisant un token d'authentification
"""

import os
import subprocess
import sys

# Configuration
REPO_OWNER = "Vgactec"
REPO_NAME = "neurax"
TOKEN = "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"
CLONE_DIR = "neurax_complet"

# URL avec le token d'authentification
GIT_URL = f"https://{TOKEN}@github.com/{REPO_OWNER}/{REPO_NAME}.git"

# Couleurs pour l'affichage
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_colored(text, color):
    """Affiche du texte coloré dans le terminal"""
    print(f"{color}{text}{Colors.ENDC}")

def run_command(command):
    """Exécute une commande shell et retourne le résultat"""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print_colored(f"Erreur lors de l'exécution de la commande: {e}", Colors.RED)
        if e.stderr:
            print_colored(f"Erreur: {e.stderr}", Colors.RED)
        return None

def main():
    print_colored("CLONAGE DU DÉPÔT NEURAX AVEC AUTHENTIFICATION", Colors.BOLD + Colors.BLUE)
    print(f"Ce script va cloner le dépôt {REPO_OWNER}/{REPO_NAME}")
    print(f"Destination: {CLONE_DIR}")
    print()
    
    # Nettoyer le dossier s'il existe déjà
    if os.path.exists(CLONE_DIR):
        print_colored(f"Suppression du dossier existant {CLONE_DIR}...", Colors.YELLOW)
        run_command(f"rm -rf {CLONE_DIR}")
    
    # Cloner le dépôt avec le token
    print_colored("Démarrage du clonage (cela peut prendre quelques minutes)...", Colors.BLUE)
    result = run_command(f"git clone {GIT_URL} {CLONE_DIR}")
    
    if result is not None:
        print_colored("Le dépôt a été cloné avec succès!", Colors.GREEN + Colors.BOLD)
        
        # Afficher les informations sur le dépôt cloné
        file_count = run_command(f"find {CLONE_DIR} -type f | wc -l")
        dir_count = run_command(f"find {CLONE_DIR} -type d | wc -l")
        
        print_colored("\nInformations sur le dépôt cloné:", Colors.BOLD)
        print(f"Nombre de fichiers: {file_count}")
        print(f"Nombre de dossiers: {dir_count}")
        print(f"Emplacement: {os.path.abspath(CLONE_DIR)}")
    else:
        print_colored("Le clonage a échoué!", Colors.RED + Colors.BOLD)
        sys.exit(1)

if __name__ == "__main__":
    main()