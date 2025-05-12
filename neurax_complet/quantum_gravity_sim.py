import numpy as np
from scipy.constants import hbar, c, G
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumGravitySimulator:
    def __init__(self, size=50):
        self.PLANCK_LENGTH = np.sqrt(hbar * G / c**3)
        self.size = size
        self.space_time = np.zeros((size, size, size))
        logging.info(f"Initialized simulator with grid size {size}³")
        logging.info(f"Planck Length: {self.PLANCK_LENGTH}")
        logging.info(f"Initial space-time grid shape: {self.space_time.shape}")

    def quantum_fluctuations(self, intensity=2.0):  # Maximum fluctuations
        noise = np.random.normal(0, intensity, self.space_time.shape, dtype=np.float128)
        exponential_factor = np.random.exponential(15.0, self.space_time.shape)
        self.space_time += noise * exponential_factor  # Non-linear quantum effects
        logging.debug(f"Applied quantum fluctuations with intensity {intensity}")
        logging.debug(f"Fluctuation range: [{np.min(noise):.2e}, {np.max(noise):.2e}]")
        return self.space_time

    def calculate_curvature(self):
        """Calculate space-time curvature based on energy-momentum fluctuations"""
        laplacian = (
            np.roll(self.space_time, 1, axis=0) + 
            np.roll(self.space_time, -1, axis=0) +
            np.roll(self.space_time, 1, axis=1) + 
            np.roll(self.space_time, -1, axis=1) +
            np.roll(self.space_time, 1, axis=2) + 
            np.roll(self.space_time, -1, axis=2) - 
            6 * self.space_time
        )
        curvature = laplacian * self.PLANCK_LENGTH
        logging.debug(f"Calculated curvature range: [{np.min(curvature):.2e}, {np.max(curvature):.2e}]")
        return curvature

    def simulate_step(self, intensity=1e-6):
        """Perform one simulation step"""
        self.quantum_fluctuations(intensity)
        curvature = self.calculate_curvature()
        self.space_time += curvature
        logging.debug(f"Space-time state after step: mean={np.mean(self.space_time):.2e}, std={np.std(self.space_time):.2e}")
        return self.space_time

    def get_metrics(self):
        """Calculate simulation metrics"""
        metrics = {
            'mean_curvature': np.mean(self.space_time),
            'max_curvature': np.max(self.space_time),
            'min_curvature': np.min(self.space_time),
            'std_deviation': np.std(self.space_time),
            'total_energy': np.sum(np.abs(self.space_time)),
            'quantum_density': np.mean(np.abs(self.space_time)) / self.PLANCK_LENGTH
        }
        logging.info(f"Calculated metrics: {metrics}")
        return metrics