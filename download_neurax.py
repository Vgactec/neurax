#!/usr/bin/env python3
"""
Script pour télécharger fichier par fichier le contenu du dépôt neurax
sans avoir besoin de cloner l'ensemble du dépôt.
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
LOCAL_DIR = "neurax_files"
API_RATE_LIMIT_WAIT = 2  # secondes entre les requêtes pour éviter les limites d'API

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
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Assurez-vous que le répertoire parent existe
        parent_dir = os.path.dirname(local_path)
        if parent_dir:
            create_directory(parent_dir)
        
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        return True
    except Exception as e:
        print_colored(f"Erreur lors du téléchargement de {url}: {e}", Colors.RED)
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

def download_directory_contents(repo_path="", local_base_path=LOCAL_DIR):
    """Télécharge récursivement tous les fichiers d'un dossier du dépôt"""
    print_colored(f"Exploration du dossier: {repo_path if repo_path else 'racine'}", Colors.BLUE)
    
    contents = get_repo_contents(repo_path)
    if not contents:
        return 0
    
    # Si c'est un seul fichier (pas une liste)
    if not isinstance(contents, list):
        if contents.get("type") == "file":
            contents = [contents]
        else:
            print_colored(f"Erreur: Contenu inattendu pour {repo_path}", Colors.RED)
            return 0
    
    files_downloaded = 0
    
    for item in contents:
        item_name = item["name"]
        item_path = f"{repo_path}/{item_name}" if repo_path else item_name
        local_path = os.path.join(local_base_path, item_path)
        
        if item["type"] == "dir":
            # C'est un dossier, on appelle récursivement
            create_directory(local_path)
            time.sleep(API_RATE_LIMIT_WAIT)  # Éviter d'être limité par l'API
            files_downloaded += download_directory_contents(item_path, local_base_path)
        
        elif item["type"] == "file":
            # C'est un fichier, on le télécharge
            download_url = item["download_url"]
            print(f"Téléchargement de {item_path}...")
            if download_file(download_url, local_path):
                files_downloaded += 1
                print_colored(f"✓ Téléchargé: {item_path}", Colors.GREEN)
            time.sleep(API_RATE_LIMIT_WAIT)  # Éviter d'être limité par l'API
    
    return files_downloaded

def download_repo_via_direct_urls():
    """Télécharge les fichiers en utilisant les URLs directes GitHub"""
    print_colored(f"Début du téléchargement du dépôt {REPO_OWNER}/{REPO_NAME} fichier par fichier", Colors.BOLD)
    
    # Créer le dossier principal pour stocker les fichiers
    create_directory(LOCAL_DIR)
    
    # Commencer le téléchargement récursif depuis la racine
    total_files = download_directory_contents()
    
    print_colored(f"\nTéléchargement terminé! {total_files} fichiers téléchargés dans le dossier '{LOCAL_DIR}'", Colors.BOLD + Colors.GREEN)
    print(f"Vous pouvez maintenant explorer le contenu complet du dépôt.")

def main():
    print_colored("TÉLÉCHARGEMENT DES FICHIERS NEURAX", Colors.BOLD + Colors.BLUE)
    print(f"Ce script va télécharger tous les fichiers du dépôt {REPO_OWNER}/{REPO_NAME}")
    print(f"Les fichiers seront sauvegardés dans le dossier: {LOCAL_DIR}")
    print()
    
    download_repo_via_direct_urls()

if __name__ == "__main__":
    main()