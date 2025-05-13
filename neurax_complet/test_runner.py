#!/usr/bin/env python3
"""
Script de test pour le projet Neurax
Exécute tous les tests et compare les résultats avec les attentes documentées
"""

import os
import sys
import time
import logging
import json
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('neurax_tests')

# Assurez-vous que les chemins d'import sont corrects
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports des modules à tester
try:
    from core.quantum_sim.simulator import QuantumGravitySimulator
    MODULE_IMPORT_SUCCESS = True
except ImportError as e:
    logger.error(f"Erreur d'importation des modules: {str(e)}")
    try:
        # Alternative: essayer d'importer depuis le fichier principal
        from quantum_gravity_sim import QuantumGravitySimulator
        logger.info("QuantumGravitySimulator importé avec succès depuis quantum_gravity_sim.py")
        MODULE_IMPORT_SUCCESS = True
    except ImportError as e2:
        logger.error(f"Erreur d'importation alternative: {str(e2)}")
        MODULE_IMPORT_SUCCESS = False

class TestResults:
    """Classe pour stocker et formater les résultats des tests"""
    def __init__(self):
        self.test_results = {}
        self.start_time = time.time()
        
    def add_result(self, test_name, status, execution_time, details=None):
        self.test_results[test_name] = {
            "status": status,
            "execution_time": execution_time,
            "details": details or {}
        }
    
    def get_summary(self):
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results.values() if result["status"] == "PASS")
        failed_tests = total_tests - passed_tests
        
        return {
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "failed_tests": failed_tests,
            "success_rate": (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            "total_execution_time": round(time.time() - self.start_time, 2)
        }
    
    def generate_markdown_report(self, file_path):
        """Génère un rapport au format Markdown"""
        summary = self.get_summary()
        
        with open(file_path, 'w') as f:
            f.write("# Rapport d'Exécution des Tests Neurax\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Résumé\n\n")
            f.write(f"- **Total des tests**: {summary['total_tests']}\n")
            f.write(f"- **Tests réussis**: {summary['passed_tests']}\n")
            f.write(f"- **Tests échoués**: {summary['failed_tests']}\n")
            f.write(f"- **Taux de réussite**: {summary['success_rate']:.2f}%\n")
            f.write(f"- **Temps d'exécution total**: {summary['total_execution_time']} secondes\n\n")
            
            f.write("## Détails des Tests\n\n")
            
            for test_name, result in self.test_results.items():
                status_icon = "✅" if result["status"] == "PASS" else "❌"
                f.write(f"### {status_icon} {test_name}\n\n")
                f.write(f"- **Statut**: {result['status']}\n")
                f.write(f"- **Temps d'exécution**: {result['execution_time']:.4f} secondes\n")
                
                if result["details"]:
                    f.write("- **Détails**:\n")
                    for key, value in result["details"].items():
                        f.write(f"  - {key}: {value}\n")
                
                f.write("\n")
            
            logger.info(f"Rapport généré avec succès dans {file_path}")


def run_quantum_simulator_test():
    """Teste le simulateur de gravité quantique"""
    logger.info("Test du simulateur de gravité quantique")
    start_time = time.time()
    
    try:
        # Créer une instance du simulateur (avec les bons paramètres)
        sim = QuantumGravitySimulator(grid_size=20)
        
        # Vérifier que l'instance a été créée correctement
        if not hasattr(sim, 'grid_size'):
            return "FAIL", time.time() - start_time, {"erreur": "L'attribut grid_size n'existe pas"}
            
        # Vérifier que la taille de la grille est correcte
        grid_size_correct = sim.grid_size == 20
        
        # Tester si l'attribut space_time existe
        has_space_time = hasattr(sim, 'space_time')
        
        # Vérifier si la méthode quantum_fluctuations existe
        has_quantum_fluctuations = hasattr(sim, 'quantum_fluctuations') and callable(getattr(sim, 'quantum_fluctuations'))
        
        # Essayer d'appeler les méthodes du simulateur si elles existent
        if has_quantum_fluctuations:
            try:
                # Essayer avec différentes signatures possibles
                try:
                    sim.quantum_fluctuations(intensity=1.5)
                except TypeError:
                    try:
                        sim.quantum_fluctuations(1.5)
                    except TypeError:
                        sim.quantum_fluctuations()
                
                fluctuations_called = True
            except Exception as e:
                fluctuations_called = False
                logger.warning(f"Impossible d'appeler quantum_fluctuations: {str(e)}")
        else:
            fluctuations_called = False
        
        # Collecter tous les résultats des tests
        status = "PASS" if grid_size_correct and has_space_time else "FAIL"
        details = {
            "grid_size_correct": str(grid_size_correct),
            "has_space_time": str(has_space_time),
            "has_quantum_fluctuations": str(has_quantum_fluctuations),
            "fluctuations_called": str(fluctuations_called)
        }
        
        # Ajouter des détails sur l'état de l'espace-temps si disponible
        if has_space_time and hasattr(sim.space_time, 'shape'):
            details["space_time_shape"] = str(sim.space_time.shape)
            
            # Calculer des statistiques sur l'espace-temps
            try:
                min_val = np.min(sim.space_time)
                max_val = np.max(sim.space_time)
                mean_val = np.mean(sim.space_time)
                details["min_value"] = f"{min_val:.6f}"
                details["max_value"] = f"{max_val:.6f}"
                details["mean_value"] = f"{mean_val:.6f}"
                details["has_fluctuations"] = str(not np.all(sim.space_time == 0))
            except Exception as e:
                details["stats_error"] = str(e)
        
        execution_time = time.time() - start_time
        return status, execution_time, details
        
    except Exception as e:
        logger.error(f"Erreur lors du test du simulateur: {str(e)}")
        return "FAIL", time.time() - start_time, {"erreur": str(e)}


def run_all_tests():
    """Exécute tous les tests disponibles"""
    results = TestResults()
    
    if not MODULE_IMPORT_SUCCESS:
        logger.error("Impossible d'exécuter les tests en raison d'erreurs d'importation des modules")
        return results
    
    # Test du simulateur quantique
    status, exec_time, details = run_quantum_simulator_test()
    results.add_result("Simulateur de Gravité Quantique", status, exec_time, details)
    
    # Ajouter d'autres tests ici
    
    return results


if __name__ == "__main__":
    logger.info("Démarrage des tests pour le projet Neurax")
    
    # Exécuter tous les tests
    test_results = run_all_tests()
    
    # Générer un rapport
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "current_test_results.md")
    test_results.generate_markdown_report(report_path)
    
    # Afficher le résumé
    summary = test_results.get_summary()
    logger.info(f"Tests terminés. Taux de réussite: {summary['success_rate']:.2f}%")
    logger.info(f"Rapport détaillé disponible dans {report_path}")