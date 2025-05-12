"""
Implémentation du neurone quantique gravitationnel
Ce module implémente la couche neuronale basée sur l'équation L(t) = 1 - e^{-t\,\phi(t)}
"""

import numpy as np
import logging
import time
from datetime import datetime
import json
import hashlib
from ..quantum_sim.simulator import QuantumGravitySimulator
from ..quantum_sim.constants import *

class QuantumGravitationalNeuron:
    """
    Neurone quantique gravitationnel qui étend le simulateur avec des capacités d'apprentissage
    et d'adaptation basées sur l'équation L(t) = 1 - e^{-t\,\phi(t)}
    """
    
    def __init__(self, grid_size=DEFAULT_GRID_SIZE, time_steps=DEFAULT_TIME_STEPS,
                 p_0=0.5, beta_1=0.3, beta_2=0.3, beta_3=0.2):
        """
        Initialise un neurone quantique gravitationnel.
        
        Args:
            grid_size (int): Taille de la grille spatiale 3D
            time_steps (int): Nombre d'étapes temporelles
            p_0 (float): Probabilité de base
            beta_1 (float): Coefficient d'influence créative
            beta_2 (float): Coefficient d'influence décisionnelle
            beta_3 (float): Coefficient d'influence du réseau
        """
        self.logger = logging.getLogger(__name__)
        
        # Initialiser le simulateur quantique sous-jacent
        self.simulator = QuantumGravitySimulator(grid_size, time_steps)
        
        # Paramètres neuronaux
        self.p_0 = p_0
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.beta_3 = beta_3
        
        # État neuronal
        self.iterations = 0
        self.activation_history = []
        self.creativity_history = []
        self.decision_history = []
        self.network_consensus_history = []
        self.p_effective_history = []
        
        # État du réseau
        self.neighbors = {}  # {node_id: connection_weight}
        self.shared_knowledge = []
        self.received_knowledge = []
        
        # Identificateur unique du neurone
        self.node_id = self._generate_node_id()
        
        self.logger.info(f"Quantum gravitational neuron initialized with ID: {self.node_id}")
        self.logger.debug(f"Neural parameters: p_0={p_0}, beta_1={beta_1}, beta_2={beta_2}, beta_3={beta_3}")
        
    def _generate_node_id(self):
        """
        Génère un identifiant unique pour ce neurone.
        
        Returns:
            str: Identifiant unique
        """
        # Combiner plusieurs sources d'entropie pour l'unicité
        unique_data = {
            'timestamp': time.time(),
            'random': np.random.random(),
            'grid_size': self.simulator.grid_size,
            'machine_info': {
                'time_steps': self.simulator.time_steps
            }
        }
        
        # Créer un hash unique
        serialized = json.dumps(unique_data, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()[:16]
        
    def calculate_creativity_index(self):
        """
        Calcule l'indice de créativité I_crea basé sur l'état de l'espace-temps.
        Mesure la diversité et l'originalité des structures d'espace-temps.
        
        Returns:
            float: Indice de créativité entre 0 et 1
        """
        # Obtenir l'état courant
        current_state = self.simulator.get_current_state()
        
        # Mesurer la diversité (variabilité des structures)
        diversity = np.std(current_state) / (np.mean(np.abs(current_state)) + EPSILON)
        
        # Mesurer l'originalité (formations non-uniformes, pics, motifs)
        gradient = np.gradient(current_state)
        gradient_magnitude = np.sqrt(np.sum([g**2 for g in gradient], axis=0))
        peak_ratio = np.sum(gradient_magnitude > np.mean(gradient_magnitude) + np.std(gradient_magnitude)) / gradient_magnitude.size
        
        # Mesurer la complexité des structures
        fft_spectrum = np.abs(np.fft.fftn(current_state))
        spectral_complexity = np.std(fft_spectrum) / (np.mean(fft_spectrum) + EPSILON)
        
        # Combiner les mesures et normaliser
        creativity = (0.4 * diversity + 0.3 * peak_ratio + 0.3 * spectral_complexity)
        normalized_creativity = np.tanh(creativity)
        
        self.logger.debug(f"Creativity index: {normalized_creativity:.4f} (diversity: {diversity:.4f}, peaks: {peak_ratio:.4f}, complexity: {spectral_complexity:.4f})")
        
        return normalized_creativity
        
    def calculate_decision_index(self):
        """
        Calcule l'indice de décision I_decis basé sur la cohérence des structures d'espace-temps.
        Mesure la qualité "décisionnelle" du neurone par la cohérence de ses configurations.
        
        Returns:
            float: Indice de décision entre 0 et 1
        """
        # Obtenir l'état courant et la courbure
        current_state = self.simulator.get_current_state()
        curvature = self.simulator.calculate_curvature()
        
        # Calculer le gradient de l'état courant
        gradient = np.gradient(current_state)
        gradient_magnitude = np.sqrt(np.sum([g**2 for g in gradient], axis=0))
        
        # Mesurer la cohérence entre la courbure et le gradient
        # Une forte corrélation indique des structures cohérentes
        flattened_curvature = curvature.flatten()
        flattened_gradient = gradient_magnitude.flatten()
        
        # Calcul de la corrélation (éviter les erreurs numériques)
        if np.std(flattened_curvature) > EPSILON and np.std(flattened_gradient) > EPSILON:
            coherence = np.corrcoef(flattened_curvature, flattened_gradient)[0,1]
            coherence = 0 if np.isnan(coherence) else coherence
        else:
            coherence = 0
            
        # Mesurer la stabilité temporelle si on a un historique
        stability = 0.0
        if self.iterations > 1 and len(self.activation_history) > 0:
            prev_activation = self.activation_history[-1]
            stability = 1.0 - np.min([abs(prev_activation - 0.5) * 2, 1.0])
        
        # Mesurer l'efficacité énergétique
        metrics = self.simulator.get_metrics()
        energy_ratio = np.exp(-abs(metrics['total_energy'] / (metrics['mean_curvature'] + EPSILON)))
        energy_efficiency = np.clip(energy_ratio, 0, 1)
        
        # Combiner les mesures et normaliser
        decision_quality = (0.5 * abs(coherence) + 0.3 * stability + 0.2 * energy_efficiency)
        normalized_decision = 0.5 * (np.tanh(decision_quality) + 1)  # Normaliser entre 0 et 1
        
        self.logger.debug(f"Decision index: {normalized_decision:.4f} (coherence: {coherence:.4f}, stability: {stability:.4f}, efficiency: {energy_efficiency:.4f})")
        
        return normalized_decision
        
    def calculate_network_consensus(self, peer_states=None):
        """
        Calcule l'indice de consensus réseau C_reseau basé sur l'alignement avec les pairs.
        Mesure la cohérence du neurone avec les connaissances partagées par ses voisins.
        
        Args:
            peer_states (dict): Dict de {peer_id: state_dict} ou None
            
        Returns:
            float: Indice de consensus entre 0 et 1
        """
        # Si pas de pairs connectés ou pas d'états reçus, retourner une valeur par défaut
        if not peer_states or not self.neighbors:
            return 0.0
            
        consensus_score = 0.0
        weight_sum = 0.0
        
        for peer_id, state in peer_states.items():
            if peer_id in self.neighbors:
                # Calculer la similarité avec l'état du pair
                similarity = self._calculate_state_similarity(state)
                
                # Pondérer par la force de la connexion
                weight = self.neighbors[peer_id]
                consensus_score += similarity * weight
                weight_sum += weight
        
        # Normalisation
        if weight_sum > EPSILON:
            normalized_consensus = consensus_score / weight_sum
        else:
            normalized_consensus = 0
            
        self.logger.debug(f"Network consensus: {normalized_consensus:.4f} (based on {len(peer_states)} peers)")
        
        return np.tanh(normalized_consensus)
        
    def _calculate_state_similarity(self, peer_state):
        """
        Calcule la similarité entre l'état local du neurone et l'état d'un pair.
        
        Args:
            peer_state (dict): État du pair
            
        Returns:
            float: Score de similarité entre 0 et 1
        """
        # Extraire les métriques comparables
        local_metrics = self.simulator.get_metrics()
        
        # Si le pair n'a pas de métriques ou des métriques incompatibles, retourner similitude faible
        if not peer_state or 'metrics' not in peer_state:
            return 0.1
            
        peer_metrics = peer_state['metrics']
        
        # Calculer la similarité des métriques clés
        similarity_scores = []
        
        for key in ['mean_curvature', 'std_deviation', 'quantum_density']:
            if key in local_metrics and key in peer_metrics:
                # Normaliser la différence
                diff = abs(local_metrics[key] - peer_metrics[key])
                max_val = max(abs(local_metrics[key]), abs(peer_metrics[key]))
                
                if max_val > EPSILON:  # Éviter division par zéro
                    similarity = 1.0 - min(diff / max_val, 1.0)
                else:
                    similarity = 1.0 if diff < EPSILON else 0.0
                
                similarity_scores.append(similarity)
        
        # Moyenne des similarités si on a des scores
        if similarity_scores:
            return np.mean(similarity_scores)
        else:
            return 0.1  # Valeur par défaut en cas d'incompatibilité
        
    def calculate_effective_probability(self, peer_states=None):
        """
        Calcule p_eff selon la formule adaptée pour environnement décentralisé.
        p_eff = p_0 + beta_1*I_crea + beta_2*I_decis + beta_3*C_reseau
        
        Args:
            peer_states (dict): Dict de {peer_id: state_dict} ou None
            
        Returns:
            float: Probabilité effective entre 0.01 et 0.99
        """
        I_crea = self.calculate_creativity_index()
        I_decis = self.calculate_decision_index()
        C_reseau = self.calculate_network_consensus(peer_states)
        
        # Calculer la probabilité effective
        p_eff = self.p_0 + self.beta_1 * I_crea + self.beta_2 * I_decis + self.beta_3 * C_reseau
        
        # Contrainte aux limites pour éviter instabilités numériques
        p_eff = np.clip(p_eff, 0.01, 0.99)
        
        # Sauvegarder l'historique
        self.creativity_history.append(I_crea)
        self.decision_history.append(I_decis)
        self.network_consensus_history.append(C_reseau)
        self.p_effective_history.append(p_eff)
        
        self.logger.debug(f"Effective probability: {p_eff:.4f}")
        
        return p_eff
        
    def calculate_activation(self, peer_states=None):
        """
        Calcule l'activation neuronale L(t) incorporant les effets des pairs.
        L(t) = 1 - e^{-t\,\phi(t)}
        
        Args:
            peer_states (dict): Dict de {peer_id: state_dict} ou None
            
        Returns:
            float: Niveau d'activation entre 0 et 1
        """
        # Si aucun pair connecté, utiliser formule simplifiée
        if not peer_states or not self.neighbors:
            p_eff = self.calculate_effective_probability({})
            phi = 1 - (1 - p_eff) ** 1  # N=1 en mode autonome
        else:
            # Calcul du produit des (1-p_eff)^w pour tous les pairs
            product_term = 1.0
            for peer_id, state in peer_states.items():
                if peer_id in self.neighbors:
                    peer_p_eff = state.get('p_effective', 0.5)
                    weight = self.neighbors[peer_id]
                    product_term *= (1 - peer_p_eff) ** weight
            
            phi = 1 - product_term
        
        # L(t) avec t normalisé
        t_norm = self.iterations / 1000.0  # Échelle arbitraire
        L = 1 - np.exp(-t_norm * phi)
        
        # Stockage pour analyse
        self.activation_history.append(L)
        
        self.logger.debug(f"Activation L(t): {L:.4f} (phi: {phi:.4f}, t_norm: {t_norm:.4f})")
        
        return L
        
    def neuron_step(self, intensity=DEFAULT_INTENSITY, peer_states=None):
        """
        Effectue une étape de simulation neuronale, intégrant la gravité quantique
        et les mécanismes neuronaux.
        
        Args:
            intensity (float): Intensité des fluctuations quantiques
            peer_states (dict): Dict de {peer_id: state_dict} ou None
            
        Returns:
            dict: Résultats de l'étape
        """
        # Exécuter une étape de simulation quantique
        self.simulator.simulate_step(intensity)
        
        # Incrémenter le compteur d'itérations
        self.iterations += 1
        
        # Calculer l'activation neuronale
        activation = self.calculate_activation(peer_states)
        
        # Moduler l'espace-temps en fonction de l'activation
        current_state = self.simulator.get_current_state()
        modulation = np.random.normal(0, activation, current_state.shape)
        
        # L'amplitude de modulation est proportionnelle à l'activation et à l'intensité
        modulation_scale = intensity * 10
        self.simulator.space_time[self.simulator.current_step % self.simulator.time_steps] += modulation * modulation_scale
        
        # Adapter les poids de connexion en fonction des interactions
        if peer_states:
            self._update_connection_weights(peer_states)
        
        # Préparer le résultat
        result = {
            'node_id': self.node_id,
            'iteration': self.iterations,
            'timestamp': datetime.now().isoformat(),
            'activation': float(activation),
            'creativity': float(self.creativity_history[-1]),
            'decision': float(self.decision_history[-1]),
            'network_consensus': float(self.network_consensus_history[-1]),
            'p_effective': float(self.p_effective_history[-1]),
            'metrics': self.simulator.get_metrics(),
            'space_time_hash': self._compute_state_hash()
        }
        
        self.logger.info(f"Neuron step {self.iterations} completed with activation {activation:.4f}")
        
        return result
        
    def _update_connection_weights(self, peer_states):
        """
        Met à jour les poids de connexion en fonction des interactions.
        Renforce les connexions utiles et affaiblit les connexions non productives.
        
        Args:
            peer_states (dict): Dict de {peer_id: state_dict}
        """
        for peer_id, state in peer_states.items():
            if peer_id in self.neighbors:
                # Calculer la similarité avec ce pair
                similarity = self._calculate_state_similarity(state)
                
                # Calculer l'utilité de cette connexion
                peer_creativity = state.get('creativity', 0.5)
                
                # L'utilité est haute si le pair est soit très similaire (consolidation)
                # soit très créatif (exploration)
                utility = 0.5 * similarity + 0.5 * peer_creativity
                
                # Ajuster le poids de la connexion
                current_weight = self.neighbors[peer_id]
                learning_rate = 0.01  # Taux d'apprentissage lent pour stabilité
                
                # Renforcement hebbian: "neurons that fire together, wire together"
                new_weight = current_weight + learning_rate * (utility - current_weight)
                
                # Contrainte aux limites
                self.neighbors[peer_id] = np.clip(new_weight, 0.01, 1.0)
                
                self.logger.debug(f"Updated connection to {peer_id}: {current_weight:.3f} -> {self.neighbors[peer_id]:.3f}")
        
    def _compute_state_hash(self):
        """
        Calcule un hash représentant l'état actuel de l'espace-temps.
        Utile pour partager un résumé de l'état sans transférer toutes les données.
        
        Returns:
            str: Hash SHA-256 de l'état
        """
        # Prendre un sous-échantillon de l'état pour réduire la taille
        current_state = self.simulator.get_current_state()
        
        # Réduction de dimensionnalité (sous-échantillonnage)
        subsample = current_state[::2, ::2, ::2]
        
        # Calcul du hash
        return hashlib.sha256(subsample.tobytes()).hexdigest()
        
    def connect_to_peer(self, peer_id, initial_weight=0.1):
        """
        Établit une connexion avec un pair.
        
        Args:
            peer_id (str): Identifiant du pair
            initial_weight (float): Poids initial de la connexion
            
        Returns:
            bool: True si la connexion est établie, False sinon
        """
        if peer_id == self.node_id:
            self.logger.warning(f"Cannot connect to self")
            return False
            
        if peer_id in self.neighbors:
            self.logger.debug(f"Already connected to {peer_id}")
            return True
            
        self.neighbors[peer_id] = initial_weight
        self.logger.info(f"Connected to peer {peer_id} with initial weight {initial_weight}")
        
        return True
        
    def disconnect_from_peer(self, peer_id):
        """
        Supprime la connexion avec un pair.
        
        Args:
            peer_id (str): Identifiant du pair
            
        Returns:
            bool: True si la déconnexion est réussie, False sinon
        """
        if peer_id in self.neighbors:
            del self.neighbors[peer_id]
            self.logger.info(f"Disconnected from peer {peer_id}")
            return True
        else:
            self.logger.debug(f"Not connected to {peer_id}")
            return False
            
    def share_knowledge(self):
        """
        Prépare les connaissances à partager avec les pairs.
        
        Returns:
            dict: Package de connaissances à partager
        """
        # Créer un package de connaissances
        knowledge_package = {
            'node_id': self.node_id,
            'timestamp': datetime.now().isoformat(),
            'iteration': self.iterations,
            'activation': float(self.activation_history[-1]) if self.activation_history else 0.0,
            'creativity': float(self.creativity_history[-1]) if self.creativity_history else 0.0,
            'decision': float(self.decision_history[-1]) if self.decision_history else 0.0,
            'p_effective': float(self.p_effective_history[-1]) if self.p_effective_history else 0.0,
            'metrics': self.simulator.get_metrics(),
            'space_time_hash': self._compute_state_hash()
        }
        
        # Ajouter à l'historique des connaissances partagées
        self.shared_knowledge.append(knowledge_package)
        
        self.logger.debug(f"Prepared knowledge package for sharing")
        
        return knowledge_package
        
    def receive_knowledge(self, knowledge_package):
        """
        Reçoit et traite les connaissances partagées par un pair.
        
        Args:
            knowledge_package (dict): Package de connaissances reçu
            
        Returns:
            bool: True si les connaissances sont valides et traitées, False sinon
        """
        # Vérifier si le package est valide
        if not knowledge_package or 'node_id' not in knowledge_package:
            self.logger.warning("Received invalid knowledge package")
            return False
            
        # Vérifier que ce n'est pas notre propre connaissance qui revient
        if knowledge_package['node_id'] == self.node_id:
            self.logger.debug("Ignoring our own knowledge package")
            return False
            
        # Ajouter à la liste des connaissances reçues
        self.received_knowledge.append(knowledge_package)
        
        # Établir une connexion si ce pair n'est pas déjà connu
        peer_id = knowledge_package['node_id']
        if peer_id not in self.neighbors:
            self.connect_to_peer(peer_id)
            
        self.logger.info(f"Received knowledge from peer {peer_id}")
        
        return True
        
    def get_neuron_state(self):
        """
        Renvoie l'état complet du neurone pour diagnostic ou partage.
        
        Returns:
            dict: État complet du neurone
        """
        return {
            'node_id': self.node_id,
            'iterations': self.iterations,
            'timestamp': datetime.now().isoformat(),
            'activation': float(self.activation_history[-1]) if self.activation_history else 0.0,
            'creativity': float(self.creativity_history[-1]) if self.creativity_history else 0.0,
            'decision': float(self.decision_history[-1]) if self.decision_history else 0.0,
            'network_consensus': float(self.network_consensus_history[-1]) if self.network_consensus_history else 0.0,
            'p_effective': float(self.p_effective_history[-1]) if self.p_effective_history else 0.0,
            'connected_peers': len(self.neighbors),
            'peer_list': list(self.neighbors.keys()),
            'metrics': self.simulator.get_metrics(),
            'space_time_hash': self._compute_state_hash()
        }
        
    def save_state(self, filepath):
        """
        Sauvegarde l'état complet du neurone.
        
        Args:
            filepath (str): Chemin du fichier de sauvegarde
            
        Returns:
            bool: True si la sauvegarde a réussi, False sinon
        """
        try:
            # Sauvegarder l'état du simulateur sous-jacent
            sim_filepath = filepath + '.sim.npz'
            self.simulator.save_state(sim_filepath)
            
            # Préparer l'état du neurone
            neuron_state = {
                'node_id': self.node_id,
                'p_0': self.p_0,
                'beta_1': self.beta_1,
                'beta_2': self.beta_2,
                'beta_3': self.beta_3,
                'iterations': self.iterations,
                'activation_history': self.activation_history,
                'creativity_history': self.creativity_history,
                'decision_history': self.decision_history,
                'network_consensus_history': self.network_consensus_history,
                'p_effective_history': self.p_effective_history,
                'neighbors': self.neighbors,
                'simulator_file': sim_filepath
            }
            
            # Sauvegarder l'état du neurone
            with open(filepath, 'w') as f:
                json.dump(neuron_state, f, indent=2)
                
            self.logger.info(f"Neuron state saved to {filepath}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to save neuron state: {str(e)}")
            return False
            
    def load_state(self, filepath):
        """
        Charge l'état du neurone depuis un fichier.
        
        Args:
            filepath (str): Chemin du fichier à charger
            
        Returns:
            bool: True si le chargement a réussi, False sinon
        """
        try:
            # Charger l'état du neurone
            with open(filepath, 'r') as f:
                neuron_state = json.load(f)
                
            # Charger l'état du simulateur
            sim_filepath = neuron_state.get('simulator_file')
            if sim_filepath and os.path.exists(sim_filepath):
                self.simulator.load_state(sim_filepath)
                
            # Restaurer les paramètres du neurone
            self.node_id = neuron_state.get('node_id', self._generate_node_id())
            self.p_0 = neuron_state.get('p_0', 0.5)
            self.beta_1 = neuron_state.get('beta_1', 0.3)
            self.beta_2 = neuron_state.get('beta_2', 0.3)
            self.beta_3 = neuron_state.get('beta_3', 0.2)
            
            # Restaurer l'état du neurone
            self.iterations = neuron_state.get('iterations', 0)
            self.activation_history = neuron_state.get('activation_history', [])
            self.creativity_history = neuron_state.get('creativity_history', [])
            self.decision_history = neuron_state.get('decision_history', [])
            self.network_consensus_history = neuron_state.get('network_consensus_history', [])
            self.p_effective_history = neuron_state.get('p_effective_history', [])
            self.neighbors = neuron_state.get('neighbors', {})
            
            self.logger.info(f"Neuron state loaded from {filepath}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load neuron state: {str(e)}")
            return False