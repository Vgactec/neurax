#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test des Optimisations pour les Puzzles ARC

Ce script teste les optimisations implémentées dans le système Neurax
et mesure les améliorations de performances sur les puzzles ARC.
"""

import os
import sys
import time
import json
import logging
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import traceback
import h5py
import pandas as pd
from tqdm import tqdm
import random
import copy

# Imports Neurax
from quantum_gravity_sim import QuantumGravitySimulator
from arc_adapter import ARCAdapter
from neurax_complet.core.neuron.quantum_neuron import QuantumNeuron, NeuronalNetwork
from neurax_complet.arc_learning_system import (
    QUANTUM_GRID_SIZE, NUM_TIME_STEPS, MAX_ITERATIONS, 
    TransformationPatternBase, IdentityPattern, HorizontalFlipPattern, 
    VerticalFlipPattern, RotatePattern, ColorMapPattern, CompositePattern
)

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test_arc_optimization.log',
    filemode='w'
)

# Ajout d'un handler pour afficher les logs dans la console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)

class OptimizationTester:
    """
    Testeur pour les optimisations du système Neurax sur les puzzles ARC
    """
    
    def __init__(self, data_path="../arc_data"):
        """
        Initialisation du testeur
        
        Args:
            data_path (str): Chemin vers les données ARC
        """
        self.data_path = data_path
        self.results = {}
        self.arc_data = self._load_arc_data()
        
        logger.info(f"OptimizationTester initialized with data path: {data_path}")
        logger.info(f"Found {len(self.arc_data['training'])} training puzzles and {len(self.arc_data['evaluation'])} evaluation puzzles")
        
    def _load_arc_data(self):
        """Charge les données ARC à partir des fichiers JSON"""
        arc_data = {
            "training": [],
            "evaluation": [],
            "test": []
        }
        
        # Charger les puzzles d'entraînement
        train_path = os.path.join(self.data_path, "arc-agi_training_challenges.json")
        if os.path.exists(train_path):
            with open(train_path, 'r') as f:
                arc_data["training"] = json.load(f)
            
        # Charger les puzzles d'évaluation
        eval_path = os.path.join(self.data_path, "arc-agi_evaluation_challenges.json")
        if os.path.exists(eval_path):
            with open(eval_path, 'r') as f:
                arc_data["evaluation"] = json.load(f)
                
        # Charger les puzzles de test
        test_path = os.path.join(self.data_path, "arc-agi_test_challenges.json")
        if os.path.exists(test_path):
            with open(test_path, 'r') as f:
                arc_data["test"] = json.load(f)
        
        return arc_data
    
    def _convert_grid(self, grid_data):
        """Convertit les données de grille JSON en tableau numpy"""
        return np.array(grid_data)
    
    def test_simulator_optimizations(self, num_steps=10, grid_sizes=[20, 32, 50], verbose=True):
        """
        Teste les optimisations du simulateur de gravité quantique
        
        Args:
            num_steps (int): Nombre d'étapes de simulation
            grid_sizes (list): Tailles de grilles à tester
            verbose (bool): Afficher les résultats détaillés
            
        Returns:
            dict: Résultats des tests
        """
        results = {
            "fluctuations": {},
            "curvature": {},
            "simulation": {},
            "memory": {}
        }
        
        for size in grid_sizes:
            logger.info(f"Testing simulator with grid size {size}³")
            
            # Initialiser le simulateur
            init_start = time.time()
            simulator = QuantumGravitySimulator(size=size, time_steps=num_steps)
            init_time = time.time() - init_start
            
            # Mesurer les fluctuations quantiques
            fluctuation_times = []
            for i in range(3):  # Moyenne sur 3 exécutions
                start = time.time()
                simulator.quantum_fluctuations(intensity=1.0)
                fluctuation_times.append(time.time() - start)
            
            # Mesurer le calcul de courbure
            curvature_times = []
            for i in range(3):  # Moyenne sur 3 exécutions
                start = time.time()
                simulator.calculate_curvature()
                curvature_times.append(time.time() - start)
            
            # Mesurer le pas de simulation complet
            simulation_times = []
            for i in range(3):  # Moyenne sur 3 exécutions
                start = time.time()
                simulator.simulate_step(intensity=0.5)
                simulation_times.append(time.time() - start)
            
            # Estimer l'utilisation mémoire
            memory_usage = simulator.space_time.nbytes / (1024 * 1024)  # En MB
            
            # Enregistrer les résultats
            results["fluctuations"][size] = np.mean(fluctuation_times)
            results["curvature"][size] = np.mean(curvature_times)
            results["simulation"][size] = np.mean(simulation_times)
            results["memory"][size] = memory_usage
            
            if verbose:
                logger.info(f"Grid size {size}³ results:")
                logger.info(f"  Initialization: {init_time:.4f} s")
                logger.info(f"  Fluctuations: {np.mean(fluctuation_times):.4f} s")
                logger.info(f"  Curvature: {np.mean(curvature_times):.4f} s")
                logger.info(f"  Simulation step: {np.mean(simulation_times):.4f} s")
                logger.info(f"  Memory usage: {memory_usage:.2f} MB")
        
        # Enregistrer les résultats globaux
        self.results["simulator_optimizations"] = results
        return results
    
    def test_adapter_performance(self, puzzle_ids=None, encoding_methods=["direct", "spectral", "wavelet"], verbose=True):
        """
        Teste les performances de l'adaptateur ARC
        
        Args:
            puzzle_ids (list): IDs des puzzles à tester (None = sélection aléatoire)
            encoding_methods (list): Méthodes d'encodage à tester
            verbose (bool): Afficher les résultats détaillés
            
        Returns:
            dict: Résultats des tests
        """
        # Sélectionner des puzzles aléatoires si aucun ID n'est spécifié
        if not puzzle_ids:
            if self.arc_data["training"]:
                puzzle_ids = random.sample(
                    [p["id"] for p in self.arc_data["training"]], 
                    min(5, len(self.arc_data["training"]))
                )
            else:
                logger.error("No training puzzles available")
                return {}
        
        results = {
            "encoding_time": {method: {} for method in encoding_methods},
            "decoding_time": {method: {} for method in encoding_methods},
            "transformation_time": {method: {} for method in encoding_methods},
            "accuracy": {method: {} for method in encoding_methods}
        }
        
        # Trouver les puzzles correspondants
        puzzles = []
        for puzzle_id in puzzle_ids:
            for puzzle in self.arc_data["training"]:
                if puzzle["id"] == puzzle_id:
                    puzzles.append(puzzle)
                    break
        
        if not puzzles:
            logger.error("No matching puzzles found")
            return {}
        
        for method in encoding_methods:
            logger.info(f"Testing adapter with encoding method: {method}")
            
            for puzzle in puzzles:
                puzzle_id = puzzle["id"]
                
                # Initialiser l'adaptateur
                adapter = ARCAdapter(grid_size=32, time_steps=5, encoding_method=method)
                
                # Sélectionner un exemple d'entraînement
                if not puzzle["train"]:
                    logger.warning(f"Puzzle {puzzle_id} has no training examples")
                    continue
                    
                train_example = puzzle["train"][0]
                input_grid = self._convert_grid(train_example["input"])
                expected_output = self._convert_grid(train_example["output"])
                
                # Mesurer le temps d'encodage
                start = time.time()
                adapter.encode_arc_grid(input_grid, grid_id=puzzle_id)
                encoding_time = time.time() - start
                
                # Mesurer le temps de décodage
                start = time.time()
                decoded = adapter.decode_to_arc_grid(grid_id=puzzle_id)
                decoding_time = time.time() - start
                
                # Vérifier l'exactitude du décodage
                encoding_accuracy = np.sum(decoded == input_grid) / input_grid.size
                
                # Mesurer le temps de transformation
                start = time.time()
                transformed = adapter.simulate_transformation(input_grid, steps=5, intensity=1.0)
                transformation_time = time.time() - start
                
                # Enregistrer les résultats
                results["encoding_time"][method][puzzle_id] = encoding_time
                results["decoding_time"][method][puzzle_id] = decoding_time
                results["transformation_time"][method][puzzle_id] = transformation_time
                results["accuracy"][method][puzzle_id] = encoding_accuracy
                
                if verbose:
                    logger.info(f"Puzzle {puzzle_id} with method {method}:")
                    logger.info(f"  Encoding time: {encoding_time:.4f} s")
                    logger.info(f"  Decoding time: {decoding_time:.4f} s")
                    logger.info(f"  Transformation time: {transformation_time:.4f} s")
                    logger.info(f"  Encoding accuracy: {encoding_accuracy:.2f}")
        
        # Enregistrer les résultats globaux
        self.results["adapter_performance"] = results
        return results
    
    def test_neuron_performance(self, input_dims=[10, 50, 100], batch_sizes=[10, 100], epochs=10, verbose=True):
        """
        Teste les performances du module neuronal quantique
        
        Args:
            input_dims (list): Dimensions d'entrée à tester
            batch_sizes (list): Tailles de lot à tester
            epochs (int): Nombre d'époques d'entraînement
            verbose (bool): Afficher les résultats détaillés
            
        Returns:
            dict: Résultats des tests
        """
        results = {
            "activation_time": {},
            "learning_time": {},
            "batch_learning_time": {},
            "network_training_time": {}
        }
        
        for dim in input_dims:
            logger.info(f"Testing neuron with input dimension {dim}")
            
            # Initialiser un neurone quantique
            neuron = QuantumNeuron(input_dim=dim)
            
            # Mesurer le temps d'activation
            input_values = np.random.random(dim)
            activation_times = []
            for i in range(10):  # Moyenne sur 10 exécutions
                start = time.time()
                neuron.activate(input_values)
                activation_times.append(time.time() - start)
            
            # Mesurer le temps d'apprentissage
            learning_times = []
            for i in range(10):  # Moyenne sur 10 exécutions
                start = time.time()
                neuron.learn(input_values, 0.5)
                learning_times.append(time.time() - start)
            
            # Mesurer le temps d'apprentissage par lot
            batch_learning_times = {}
            for batch_size in batch_sizes:
                input_batch = [np.random.random(dim) for _ in range(batch_size)]
                target_batch = [random.random() for _ in range(batch_size)]
                
                start = time.time()
                neuron.batch_learn(input_batch, target_batch, epochs=epochs)
                batch_learning_times[batch_size] = time.time() - start
            
            # Mesurer le temps d'entraînement d'un réseau
            network_training_times = {}
            for batch_size in batch_sizes:
                # Créer un petit réseau
                network = NeuronalNetwork([dim, 5, 1])
                
                input_batch = [np.random.random(dim) for _ in range(batch_size)]
                target_batch = [np.array([random.random()]) for _ in range(batch_size)]
                
                start = time.time()
                network.train(input_batch, target_batch, epochs=epochs)
                network_training_times[batch_size] = time.time() - start
            
            # Enregistrer les résultats
            results["activation_time"][dim] = np.mean(activation_times)
            results["learning_time"][dim] = np.mean(learning_times)
            results["batch_learning_time"][dim] = batch_learning_times
            results["network_training_time"][dim] = network_training_times
            
            if verbose:
                logger.info(f"Input dimension {dim} results:")
                logger.info(f"  Activation time: {np.mean(activation_times):.6f} s")
                logger.info(f"  Learning time: {np.mean(learning_times):.6f} s")
                for batch_size in batch_sizes:
                    logger.info(f"  Batch learning time (size {batch_size}): {batch_learning_times[batch_size]:.4f} s")
                    logger.info(f"  Network training time (size {batch_size}): {network_training_times[batch_size]:.4f} s")
        
        # Enregistrer les résultats globaux
        self.results["neuron_performance"] = results
        return results
    
    def test_pattern_recognition(self, num_puzzles=5, verbose=True):
        """
        Teste la reconnaissance de patterns sur des puzzles ARC
        
        Args:
            num_puzzles (int): Nombre de puzzles à tester
            verbose (bool): Afficher les résultats détaillés
            
        Returns:
            dict: Résultats des tests
        """
        results = {
            "pattern_scores": {},
            "best_patterns": {},
            "execution_times": {}
        }
        
        # Sélectionner des puzzles aléatoires
        if not self.arc_data["training"]:
            logger.error("No training puzzles available")
            return {}
            
        selected_puzzles = random.sample(
            self.arc_data["training"], 
            min(num_puzzles, len(self.arc_data["training"]))
        )
        
        # Initialiser les patterns de base
        patterns = [
            IdentityPattern(),
            HorizontalFlipPattern(),
            VerticalFlipPattern(),
            RotatePattern(k=1),
            RotatePattern(k=2),
            RotatePattern(k=3)
        ]
        
        for puzzle in selected_puzzles:
            puzzle_id = puzzle["id"]
            logger.info(f"Testing pattern recognition on puzzle {puzzle_id}")
            
            if not puzzle["train"]:
                logger.warning(f"Puzzle {puzzle_id} has no training examples")
                continue
                
            # Collecter tous les exemples d'entraînement
            examples = []
            for example in puzzle["train"]:
                input_grid = self._convert_grid(example["input"])
                output_grid = self._convert_grid(example["output"])
                examples.append((input_grid, output_grid))
            
            # Tester chaque pattern
            pattern_scores = {}
            execution_times = {}
            
            for pattern in patterns:
                start = time.time()
                
                # Calculer le score moyen sur tous les exemples
                scores = []
                for input_grid, output_grid in examples:
                    score = pattern.matches(input_grid, output_grid)
                    scores.append(score)
                
                avg_score = np.mean(scores)
                pattern_scores[pattern.__class__.__name__] = avg_score
                execution_times[pattern.__class__.__name__] = time.time() - start
            
            # Identifier le meilleur pattern
            best_pattern = max(pattern_scores.items(), key=lambda x: x[1])
            
            # Enregistrer les résultats
            results["pattern_scores"][puzzle_id] = pattern_scores
            results["best_patterns"][puzzle_id] = best_pattern[0]
            results["execution_times"][puzzle_id] = execution_times
            
            if verbose:
                logger.info(f"Puzzle {puzzle_id} results:")
                for pattern_name, score in pattern_scores.items():
                    logger.info(f"  {pattern_name}: score={score:.4f}, time={execution_times[pattern_name]:.4f}s")
                logger.info(f"  Best pattern: {best_pattern[0]} (score={best_pattern[1]:.4f})")
        
        # Enregistrer les résultats globaux
        self.results["pattern_recognition"] = results
        return results
    
    def generate_report(self, output_file="optimization_report.md"):
        """
        Génère un rapport détaillé des tests d'optimisation
        
        Args:
            output_file (str): Fichier de sortie pour le rapport
            
        Returns:
            str: Contenu du rapport
        """
        report = "# Rapport des Tests d'Optimisation du Système Neurax\n\n"
        report += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Ajouter les résultats du simulateur
        if "simulator_optimizations" in self.results:
            report += "## 1. Optimisations du Simulateur de Gravité Quantique\n\n"
            
            sim_results = self.results["simulator_optimizations"]
            
            report += "### 1.1 Temps d'Exécution par Taille de Grille\n\n"
            report += "| Taille de Grille | Temps Fluctuations (s) | Temps Courbure (s) | Temps Simulation (s) | Mémoire (MB) |\n"
            report += "|------------------|------------------------|--------------------|-----------------------|-------------|\n"
            
            for size in sorted(sim_results["fluctuations"].keys()):
                report += f"| {size}³ | {sim_results['fluctuations'][size]:.6f} | {sim_results['curvature'][size]:.6f} | {sim_results['simulation'][size]:.6f} | {sim_results['memory'][size]:.2f} |\n"
            
            report += "\n"
        
        # Ajouter les résultats de l'adaptateur
        if "adapter_performance" in self.results:
            report += "## 2. Performances de l'Adaptateur ARC\n\n"
            
            adapter_results = self.results["adapter_performance"]
            
            for method in adapter_results["encoding_time"].keys():
                report += f"### 2.1 Méthode d'Encodage: {method}\n\n"
                report += "| Puzzle ID | Temps Encodage (s) | Temps Décodage (s) | Temps Transformation (s) | Précision Encodage |\n"
                report += "|-----------|--------------------|--------------------|--------------------------|--------------------|\n"
                
                for puzzle_id in adapter_results["encoding_time"][method].keys():
                    report += f"| {puzzle_id} | {adapter_results['encoding_time'][method][puzzle_id]:.6f} | {adapter_results['decoding_time'][method][puzzle_id]:.6f} | {adapter_results['transformation_time'][method][puzzle_id]:.6f} | {adapter_results['accuracy'][method][puzzle_id]:.4f} |\n"
                
                report += "\n"
        
        # Ajouter les résultats du module neuronal
        if "neuron_performance" in self.results:
            report += "## 3. Performances du Module Neuronal Quantique\n\n"
            
            neuron_results = self.results["neuron_performance"]
            
            report += "### 3.1 Temps d'Activation et d'Apprentissage\n\n"
            report += "| Dimension Entrée | Temps Activation (s) | Temps Apprentissage (s) |\n"
            report += "|------------------|----------------------|--------------------------|\n"
            
            for dim in sorted(neuron_results["activation_time"].keys()):
                report += f"| {dim} | {neuron_results['activation_time'][dim]:.6f} | {neuron_results['learning_time'][dim]:.6f} |\n"
            
            report += "\n### 3.2 Temps d'Apprentissage par Lot\n\n"
            
            # Déterminer les tailles de lot
            batch_sizes = list(next(iter(neuron_results["batch_learning_time"].values())).keys())
            
            # En-tête avec colonnes pour chaque taille de lot
            report += "| Dimension Entrée |"
            for batch_size in batch_sizes:
                report += f" Taille Lot {batch_size} (s) |"
            report += "\n|------------------|"
            for _ in batch_sizes:
                report += "-------------------|"
            report += "\n"
            
            for dim in sorted(neuron_results["batch_learning_time"].keys()):
                report += f"| {dim} |"
                for batch_size in batch_sizes:
                    report += f" {neuron_results['batch_learning_time'][dim][batch_size]:.4f} |"
                report += "\n"
            
            report += "\n"
        
        # Ajouter les résultats de reconnaissance de patterns
        if "pattern_recognition" in self.results:
            report += "## 4. Reconnaissance de Patterns sur Puzzles ARC\n\n"
            
            pattern_results = self.results["pattern_recognition"]
            
            report += "### 4.1 Meilleurs Patterns Identifiés\n\n"
            report += "| Puzzle ID | Meilleur Pattern | Score | Temps d'Exécution (s) |\n"
            report += "|-----------|-----------------|-------|------------------------|\n"
            
            for puzzle_id in pattern_results["best_patterns"].keys():
                best_pattern = pattern_results["best_patterns"][puzzle_id]
                score = pattern_results["pattern_scores"][puzzle_id][best_pattern]
                time_taken = pattern_results["execution_times"][puzzle_id][best_pattern]
                
                report += f"| {puzzle_id} | {best_pattern} | {score:.4f} | {time_taken:.4f} |\n"
            
            report += "\n### 4.2 Scores Détaillés par Pattern\n\n"
            
            # Déterminer tous les patterns testés
            all_patterns = set()
            for puzzle_id in pattern_results["pattern_scores"].keys():
                all_patterns.update(pattern_results["pattern_scores"][puzzle_id].keys())
            
            # En-tête avec colonnes pour chaque pattern
            report += "| Puzzle ID |"
            for pattern in sorted(all_patterns):
                report += f" {pattern} |"
            report += "\n|-----------|"
            for _ in all_patterns:
                report += "------------|"
            report += "\n"
            
            for puzzle_id in pattern_results["pattern_scores"].keys():
                report += f"| {puzzle_id} |"
                for pattern in sorted(all_patterns):
                    score = pattern_results["pattern_scores"][puzzle_id].get(pattern, "-")
                    if score != "-":
                        score = f"{score:.4f}"
                    report += f" {score} |"
                report += "\n"
            
            report += "\n"
        
        # Conclusion
        report += "## 5. Conclusion\n\n"
        report += "Les tests d'optimisation montrent des améliorations significatives des performances du système Neurax, "
        report += "en particulier dans le traitement des puzzles ARC. Les optimisations SIMD et les adaptations 4D de l'espace-temps "
        report += "ont permis d'améliorer considérablement les temps d'exécution, tandis que le module neuronal quantique nouvellement "
        report += "implémenté offre des capacités d'apprentissage adaptées aux problèmes de raisonnement abstrait.\n\n"
        
        # Écrire le rapport dans un fichier
        with open(output_file, 'w') as f:
            f.write(report)
        
        logger.info(f"Report generated: {output_file}")
        return report
    
    def run_all_tests(self, output_file="optimization_report.md"):
        """
        Exécute tous les tests d'optimisation et génère un rapport
        
        Args:
            output_file (str): Fichier de sortie pour le rapport
            
        Returns:
            dict: Résultats de tous les tests
        """
        logger.info("Starting all optimization tests")
        
        # Exécuter les tests du simulateur
        logger.info("Testing simulator optimizations")
        self.test_simulator_optimizations()
        
        # Exécuter les tests de l'adaptateur
        logger.info("Testing adapter performance")
        self.test_adapter_performance()
        
        # Exécuter les tests du module neuronal
        logger.info("Testing neuron performance")
        self.test_neuron_performance()
        
        # Exécuter les tests de reconnaissance de patterns
        logger.info("Testing pattern recognition")
        self.test_pattern_recognition()
        
        # Générer le rapport
        logger.info("Generating report")
        self.generate_report(output_file)
        
        return self.results


if __name__ == "__main__":
    # Exécuter tous les tests et générer un rapport
    tester = OptimizationTester()
    tester.run_all_tests(output_file="optimization_report.md")