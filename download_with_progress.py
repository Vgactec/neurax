#!/usr/bin/env python3
"""
Script amélioré pour télécharger fichier par fichier le contenu du dépôt neurax
avec affichage de la progression globale en pourcentage.
"""

import os
import requests
from bs4 import BeautifulSoup
import json
import time
import sys

# Configuration
REPO_OWNER = "Vgactec"
REPO_NAME = "neurax"
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
RAW_CONTENT_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/main"
LOCAL_DIR = "neurax_project"
API_RATE_LIMIT_WAIT = 0.5  # réduit pour accélérer le téléchargement
EXCLUDED_DIRS = [".cache", ".git", "__pycache__", ".upm"]  # dossiers à ignorer

# Variables pour le suivi de la progression
total_files = 0
downloaded_files = 0
file_list = []

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

def create_directory(path):
    """Crée un répertoire s'il n'existe pas déjà"""
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False

def download_file(url, local_path):
    """Télécharge un fichier depuis l'URL vers le chemin local"""
    global downloaded_files
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Assurez-vous que le répertoire parent existe
        parent_dir = os.path.dirname(local_path)
        if parent_dir:
            create_directory(parent_dir)
        
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        downloaded_files += 1
        progress = (downloaded_files / total_files) * 100 if total_files > 0 else 0
        print(f"Progression: {progress:.2f}% ({downloaded_files}/{total_files}) - Fichier: {local_path}")
        
        return True
    except Exception as e:
        print_colored(f"Erreur lors du téléchargement de {url}: {e}", Colors.RED)
        return False

def check_excluded(path):
    """Vérifie si le chemin doit être exclu du téléchargement"""
    for excluded in EXCLUDED_DIRS:
        if excluded in path.split('/'):
            return True
    return False

def get_repo_contents(path=""):
    """Récupère la liste des fichiers et dossiers dans le chemin spécifié du dépôt"""
    url = f"{BASE_URL}/contents/{path}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print_colored(f"Erreur lors de la récupération du contenu de {path}: {e}", Colors.RED)
        return []

def collect_all_files(repo_path=""):
    """Collecte récursivement tous les fichiers du dépôt pour calculer le total"""
    global file_list
    
    if check_excluded(repo_path):
        return
    
    contents = get_repo_contents(repo_path)
    if not contents:
        return
    
    # Si c'est un seul fichier (pas une liste)
    if not isinstance(contents, list):
        if contents.get("type") == "file":
            contents = [contents]
        else:
            return
    
    for item in contents:
        item_name = item["name"]
        item_path = f"{repo_path}/{item_name}" if repo_path else item_name
        
        if check_excluded(item_path):
            continue
        
        if item["type"] == "dir":
            time.sleep(API_RATE_LIMIT_WAIT)
            collect_all_files(item_path)
        
        elif item["type"] == "file":
            file_list.append((item_path, item.get("download_url")))
    
    time.sleep(API_RATE_LIMIT_WAIT)

def download_all_files():
    """Télécharge tous les fichiers collectés"""
    global total_files, downloaded_files
    
    total_files = len(file_list)
    downloaded_files = 0
    
    print_colored(f"Nombre total de fichiers à télécharger: {total_files}", Colors.BOLD + Colors.BLUE)
    
    for file_path, download_url in file_list:
        local_path = os.path.join(LOCAL_DIR, file_path)
        
        # Affichage court pour ne pas surcharger la console
        short_path = file_path
        if len(short_path) > 50:
            short_path = "..." + short_path[-47:]
        
        print(f"Téléchargement de {short_path}")
        
        if download_file(download_url, local_path):
            # Mise à jour de la progression globale
            progress = (downloaded_files / total_files) * 100
            if downloaded_files % 10 == 0 or downloaded_files == total_files:
                print_colored(f"PROGRESSION GLOBALE: {progress:.2f}% ({downloaded_files}/{total_files})", 
                             Colors.BOLD + Colors.GREEN)
        
        time.sleep(API_RATE_LIMIT_WAIT)

def main():
    print_colored("TÉLÉCHARGEMENT DES FICHIERS NEURAX AVEC PROGRESSION", Colors.BOLD + Colors.BLUE)
    print(f"Ce script va télécharger tous les fichiers du dépôt {REPO_OWNER}/{REPO_NAME}")
    print(f"Les fichiers seront sauvegardés dans le dossier: {LOCAL_DIR}")
    print(f"Dossiers ignorés: {', '.join(EXCLUDED_DIRS)}")
    print()
    
    # Créer le dossier principal pour stocker les fichiers
    create_directory(LOCAL_DIR)
    
    # Phase 1: Collecter tous les fichiers pour calculer le total
    print_colored("Phase 1: Recensement des fichiers du dépôt...", Colors.BOLD)
    collect_all_files()
    
    # Phase 2: Télécharger les fichiers
    print_colored("\nPhase 2: Téléchargement des fichiers...", Colors.BOLD)
    download_all_files()
    
    print_colored(f"\nTéléchargement terminé! {downloaded_files} fichiers téléchargés dans le dossier '{LOCAL_DIR}'", 
                 Colors.BOLD + Colors.GREEN)
    print(f"Progression finale: 100%")

if __name__ == "__main__":
    main()