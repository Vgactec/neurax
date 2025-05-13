import numpy as np
from scipy.constants import hbar, c, G
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumGravitySimulator:
    def __init__(self, size=50, time_steps=10, grid_size=None):
        """
        Initialise le simulateur de gravité quantique
        
        Args:
            size (int): Taille de la grille 3D (utilisé si grid_size est None)
            time_steps (int): Nombre de pas temporels
            grid_size (int): Alternative à size, pour compatibilité avec les interfaces
        """
        # Pour assurer la compatibilité avec différentes interfaces
        if grid_size is not None:
            size = grid_size
            
        self.PLANCK_LENGTH = np.sqrt(hbar * G / c**3)
        self.size = size
        self.time_steps = time_steps
        self.space_time = np.zeros((time_steps, size, size, size))
        
        logging.info(f"Initialized simulator with grid size {size}³ and {time_steps} time steps")
        logging.info(f"Planck Length: {self.PLANCK_LENGTH}")
        logging.info(f"Initial space-time grid shape: {self.space_time.shape}")

    def quantum_fluctuations(self, intensity=2.0, time_slice=None):
        """
        Applique des fluctuations quantiques à l'espace-temps
        
        Args:
            intensity (float): Intensité des fluctuations (>0)
            time_slice (int, optional): Pas de temps spécifique à modifier (None = tous)
        
        Returns:
            ndarray: Référence à l'espace-temps modifié
        """
        # Vectorisation SIMD - Utilisation optimisée de numpy pour les calculs intensifs
        if time_slice is not None:
            # Appliquer les fluctuations à un pas de temps spécifique
            slice_shape = self.space_time[time_slice].shape
            noise = np.random.normal(0, intensity, slice_shape)
            exponential_factor = np.random.exponential(15.0, slice_shape)
            self.space_time[time_slice] += noise * exponential_factor  # Effets quantiques non-linéaires
        else:
            # Appliquer les fluctuations à tous les pas de temps
            noise = np.random.normal(0, intensity, self.space_time.shape)
            exponential_factor = np.random.exponential(15.0, self.space_time.shape)
            self.space_time += noise * exponential_factor  # Effets quantiques non-linéaires
        
        logging.debug(f"Applied quantum fluctuations with intensity {intensity}")
        logging.debug(f"Fluctuation range: [{np.min(noise):.2e}, {np.max(noise):.2e}]")
        return self.space_time

    def calculate_curvature(self, time_slice=None):
        """
        Calcule la courbure de l'espace-temps basée sur les fluctuations d'énergie-impulsion
        
        Args:
            time_slice (int, optional): Pas de temps spécifique à calculer (None = tous)
            
        Returns:
            ndarray: Courbure calculée
        """
        # Optimisation par vectorisation SIMD (Single Instruction, Multiple Data)
        if time_slice is not None:
            # Calculer la courbure pour un pas de temps spécifique
            data = self.space_time[time_slice]
            # Opérateur laplacien 3D (calculé en une seule opération vectorisée)
            laplacian = (
                np.roll(data, 1, axis=0) + 
                np.roll(data, -1, axis=0) +
                np.roll(data, 1, axis=1) + 
                np.roll(data, -1, axis=1) +
                np.roll(data, 1, axis=2) + 
                np.roll(data, -1, axis=2) - 
                6 * data
            )
            # Effet gravitationnel non-linéaire
            curvature = laplacian * self.PLANCK_LENGTH
            logging.debug(f"Calculated curvature for time slice {time_slice}, range: [{np.min(curvature):.2e}, {np.max(curvature):.2e}]")
            return curvature
        else:
            # Calculer la courbure pour tous les pas de temps
            # Optimisation : préallocation du tableau pour éviter les allocations répétées
            curvature = np.zeros_like(self.space_time)
            
            # Parallélisation possible ici pour les grands espaces-temps
            for t in range(self.time_steps):
                curvature[t] = self.calculate_curvature(time_slice=t)
                
            logging.debug(f"Calculated curvature for all time slices, range: [{np.min(curvature):.2e}, {np.max(curvature):.2e}]")
            return curvature

    def simulate_step(self, intensity=1e-6, time_slice=None, evolve_time=True):
        """
        Exécute une étape de simulation de l'espace-temps
        
        Args:
            intensity (float): Intensité des fluctuations quantiques
            time_slice (int, optional): Pas de temps spécifique à simuler (None = tous)
            evolve_time (bool): Si True, fait évoluer les pas de temps (t->t+1)
            
        Returns:
            ndarray: État actuel de l'espace-temps
        """
        # Optimisation SIMD: les opérations vectorisées sont utilisées dans les fonctions appelées
        if time_slice is not None:
            # Simuler un pas de temps spécifique
            self.quantum_fluctuations(intensity, time_slice=time_slice)
            curvature = self.calculate_curvature(time_slice=time_slice)
            self.space_time[time_slice] += curvature
            logging.debug(f"Space-time state after step (time slice {time_slice}): mean={np.mean(self.space_time[time_slice]):.2e}, std={np.std(self.space_time[time_slice]):.2e}")
        else:
            # Simuler tous les pas de temps
            self.quantum_fluctuations(intensity)
            curvature = self.calculate_curvature()
            self.space_time += curvature
            logging.debug(f"Space-time state after step (all slices): mean={np.mean(self.space_time):.2e}, std={np.std(self.space_time):.2e}")
        
        # Évolution temporelle
        if evolve_time:
            # Décaler tous les pas de temps (t -> t+1) et initialiser le nouveau t=0
            self.space_time = np.roll(self.space_time, 1, axis=0)
            self.space_time[0] = np.zeros((self.size, self.size, self.size))
            logging.debug("Time evolution performed: t -> t+1")
            
        return self.space_time

    def get_metrics(self, time_slice=None):
        """
        Calcule les métriques de la simulation pour l'analyse
        
        Args:
            time_slice (int, optional): Pas de temps spécifique à analyser (None = tous)
            
        Returns:
            dict: Métriques calculées
        """
        # Optimisation: utilisation de la vectorisation SIMD via numpy pour les calculs
        if time_slice is not None:
            # Métriques pour un pas de temps spécifique
            data = self.space_time[time_slice]
            
            # Calcul vectorisé de toutes les métriques en une seule passe sur les données
            abs_data = np.abs(data)  # Calculé une seule fois et réutilisé
            
            metrics = {
                'time_slice': time_slice,
                'mean_curvature': np.mean(data),
                'max_curvature': np.max(data),
                'min_curvature': np.min(data),
                'std_deviation': np.std(data),
                'total_energy': np.sum(abs_data),
                'quantum_density': np.mean(abs_data) / self.PLANCK_LENGTH,
                'spatial_entropy': -np.sum(abs_data * np.log(abs_data + 1e-10)) / data.size,
                'non_zero_ratio': np.count_nonzero(data) / data.size
            }
        else:
            # Métriques pour tous les pas de temps (agrégées)
            # Astuce d'optimisation: calculer abs_data une seule fois
            abs_data = np.abs(self.space_time)
            
            # Préallouer des tableaux pour stocker les métriques par pas de temps
            metrics_by_time = np.zeros((self.time_steps, 5))  # [mean, max, min, std, energy]
            
            # Calculer les métriques pour chaque pas de temps en utilisant la vectorisation
            for t in range(self.time_steps):
                slice_data = self.space_time[t]
                slice_abs = abs_data[t]
                metrics_by_time[t, 0] = np.mean(slice_data)
                metrics_by_time[t, 1] = np.max(slice_data)
                metrics_by_time[t, 2] = np.min(slice_data)
                metrics_by_time[t, 3] = np.std(slice_data)
                metrics_by_time[t, 4] = np.sum(slice_abs)
            
            # Calculer les métriques agrégées
            metrics = {
                'mean_curvature': np.mean(self.space_time),
                'max_curvature': np.max(self.space_time),
                'min_curvature': np.min(self.space_time),
                'std_deviation': np.std(self.space_time),
                'total_energy': np.sum(abs_data),
                'quantum_density': np.mean(abs_data) / self.PLANCK_LENGTH,
                'spatial_entropy': -np.sum(abs_data * np.log(abs_data + 1e-10)) / self.space_time.size,
                'non_zero_ratio': np.count_nonzero(self.space_time) / self.space_time.size,
                # Métriques temporelles
                'temporal_variance': np.var(metrics_by_time[:, 0]),  # Variance des moyennes
                'temporal_energy_gradient': np.gradient(metrics_by_time[:, 4]).mean(),  # Gradient d'énergie
                'time_steps': self.time_steps
            }
            
        logging.info(f"Calculated metrics: {metrics}")
        return metrics
        
    def set_grid_value(self, x, y, z, value, time_slice=0):
        """
        Définit une valeur spécifique dans la grille d'espace-temps
        Utile pour encoder des données externes comme les puzzles ARC
        
        Args:
            x (int): Coordonnée x
            y (int): Coordonnée y
            z (int): Coordonnée z
            value (float): Valeur à définir
            time_slice (int): Pas de temps (défaut: 0 = présent)
            
        Returns:
            bool: Succès de l'opération
        """
        if 0 <= x < self.size and 0 <= y < self.size and 0 <= z < self.size and 0 <= time_slice < self.time_steps:
            self.space_time[time_slice, x, y, z] = float(value)
            return True
        return False
        
    def get_grid_value(self, x, y, z, time_slice=0):
        """
        Récupère une valeur spécifique de la grille d'espace-temps
        
        Args:
            x (int): Coordonnée x
            y (int): Coordonnée y
            z (int): Coordonnée z
            time_slice (int): Pas de temps (défaut: 0 = présent)
            
        Returns:
            float: Valeur à la position indiquée
        """
        if 0 <= x < self.size and 0 <= y < self.size and 0 <= z < self.size and 0 <= time_slice < self.time_steps:
            return float(self.space_time[time_slice, x, y, z])
        return 0.0
    
    def extract_grid_slice(self, axes='xy', position=0, time_slice=0):
        """
        Extrait une tranche 2D de l'espace-temps
        Utile pour visualiser ou décoder des données comme les puzzles ARC
        
        Args:
            axes (str): Axes à extraire ('xy', 'xz', ou 'yz')
            position (int): Position sur le troisième axe
            time_slice (int): Pas de temps (défaut: 0 = présent)
            
        Returns:
            ndarray: Tranche 2D extraite
        """
        if 0 <= time_slice < self.time_steps:
            if axes == 'xy' and 0 <= position < self.size:
                return self.space_time[time_slice, :, :, position].copy()
            elif axes == 'xz' and 0 <= position < self.size:
                return self.space_time[time_slice, :, position, :].copy()
            elif axes == 'yz' and 0 <= position < self.size:
                return self.space_time[time_slice, position, :, :].copy()
        
        # En cas d'erreur, retourner une grille vide
        return np.zeros((self.size, self.size))