#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script d'exécution d'un échantillon de puzzles ARC avec le système Neurax
Ce script exécute l'apprentissage et l'évaluation sur un échantillon de puzzles pour
tester le système et produire des résultats rapidement.
"""

import os
import sys
import time
import json
import logging
import numpy as np
from datetime import datetime
from arc_learning_system import ARCPuzzleProcessor

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("arc_sample.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ARCSample")

def run_arc_sample_learning(training_limit=5, evaluation_limit=3, test_limit=2):
    """
    Exécute l'apprentissage et l'évaluation sur un échantillon de puzzles ARC
    
    Args:
        training_limit: Nombre de puzzles d'entraînement à traiter
        evaluation_limit: Nombre de puzzles d'évaluation à traiter
        test_limit: Nombre de puzzles de test à traiter
        
    Returns:
        dict: Résultats
    """
    logger.info(f"Démarrage de l'apprentissage et de l'évaluation sur un échantillon de puzzles ARC")
    logger.info(f"Limites: {training_limit} puzzles d'entraînement, {evaluation_limit} puzzles d'évaluation, {test_limit} puzzles de test")
    
    # Initialiser le processeur de puzzles
    processor = ARCPuzzleProcessor()
    
    # Créer le répertoire de sortie
    output_dir = "arc_sample_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Étape 1: Apprentissage sur un échantillon de puzzles d'entraînement
    logger.info("ÉTAPE 1: Apprentissage sur un échantillon de puzzles d'entraînement")
    training_results = processor.train_on_all_training_puzzles(limit=training_limit)
    
    # Étape 2: Évaluation sur un échantillon de puzzles d'évaluation
    logger.info("ÉTAPE 2: Évaluation sur un échantillon de puzzles d'évaluation")
    evaluation_results = processor.evaluate_on_evaluation_puzzles(limit=evaluation_limit)
    
    # Étape 3: Génération des prédictions pour un échantillon de puzzles de test
    logger.info("ÉTAPE 3: Génération des prédictions pour un échantillon de puzzles de test")
    test_results = processor.generate_test_predictions(limit=test_limit)
    
    # Étape 4: Sauvegarde des résultats
    logger.info("ÉTAPE 4: Sauvegarde des résultats")
    processor.save_results(output_dir)
    
    # Étape 5: Génération du rapport de synthèse
    logger.info("ÉTAPE 5: Génération du rapport de synthèse")
    report_path = os.path.join(output_dir, "summary_report.md")
    processor.generate_summary_report(output_file=report_path)
    
    logger.info(f"Apprentissage et évaluation terminés. Résultats dans {output_dir}")
    
    return {
        "training_results": training_results,
        "evaluation_results": evaluation_results,
        "test_results": test_results,
        "output_dir": output_dir
    }

if __name__ == "__main__":
    run_arc_sample_learning()