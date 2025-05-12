"""
Interface web Streamlit pour le Réseau Neuronal Gravitationnel Quantique
"""

import streamlit as st
import numpy as np
import logging
import asyncio
import threading
import time
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
import sys

# Ajout du répertoire racine au path pour les imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.quantum_sim.simulator import QuantumGravitySimulator
from core.neuron.quantum_neuron import QuantumGravitationalNeuron
from core.utils.config import Config

# Configuration du logger
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Chargement de la configuration
config = Config()

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Réseau Neuronal Gravitationnel Quantique",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem !important;
        color: #7792E3;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.5rem !important;
        margin-bottom: 2rem;
    }
    .neuron-metrics {
        background-color: #1E2639;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .network-status {
        background-color: #1E2639;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .activation-high {
        color: #4CAF50;
        font-weight: bold;
    }
    .activation-medium {
        color: #FFC107;
        font-weight: bold;
    }
    .activation-low {
        color: #9E9E9E;
        font-weight: normal;
    }
</style>
""", unsafe_allow_html=True)

# Titre et description
st.markdown('<h1 class="main-title">🌌 Réseau Neuronal Gravitationnel Quantique</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Exploration collective des fluctuations quantiques d\'espace-temps</p>', unsafe_allow_html=True)

# Fonction pour initialiser l'état de session
def init_session_state():
    if 'neuron' not in st.session_state:
        st.session_state.neuron = None
    if 'last_update' not in st.session_state:
        st.session_state.last_update = None
    if 'simulation_running' not in st.session_state:
        st.session_state.simulation_running = False
    if 'peer_count' not in st.session_state:
        st.session_state.peer_count = 0
    if 'activation_history' not in st.session_state:
        st.session_state.activation_history = []
    if 'creativity_history' not in st.session_state:
        st.session_state.creativity_history = []
    if 'decision_history' not in st.session_state:
        st.session_state.decision_history = []
    if 'network_history' not in st.session_state:
        st.session_state.network_history = []
    if 'timestamps' not in st.session_state:
        st.session_state.timestamps = []

# Initialiser l'état de session
init_session_state()

# Layout principal
sidebar = st.sidebar
col1, col2 = st.columns([3, 2])

# Sidebar: Paramètres et contrôles
with sidebar:
    st.header("Configuration")
    
    # Paramètres du simulateur
    st.subheader("Paramètres de Simulation")
    
    grid_size = st.slider(
        "Taille de Grille",
        min_value=20,
        max_value=100,
        value=config.get("quantum.grid_size", 50),
        step=10,
        help="Taille de la grille d'espace-temps 3D"
    )
    
    time_steps = st.slider(
        "Étapes Temporelles",
        min_value=2,
        max_value=16,
        value=config.get("quantum.time_steps", 8),
        step=2,
        help="Nombre d'étapes temporelles dans la simulation"
    )
    
    intensity = st.slider(
        "Intensité des Fluctuations",
        min_value=1e-7,
        max_value=1e-5,
        value=config.get("quantum.default_intensity", 1e-6),
        step=1e-7,
        format="%.7f",
        help="Intensité des fluctuations quantiques"
    )
    
    # Paramètres neuronaux
    st.subheader("Paramètres Neuronaux")
    
    p_0 = st.slider(
        "Probabilité de Base (p₀)",
        min_value=0.0,
        max_value=1.0,
        value=config.get("neuron.p_0", 0.5),
        step=0.01,
        help="Probabilité de base pour l'équation d'activation"
    )
    
    beta_1 = st.slider(
        "Coefficient de Créativité (β₁)",
        min_value=0.0,
        max_value=1.0,
        value=config.get("neuron.beta_1", 0.3),
        step=0.01,
        help="Influence de l'indice de créativité"
    )
    
    beta_2 = st.slider(
        "Coefficient de Décision (β₂)",
        min_value=0.0,
        max_value=1.0,
        value=config.get("neuron.beta_2", 0.3),
        step=0.01,
        help="Influence de l'indice de décision"
    )
    
    beta_3 = st.slider(
        "Coefficient de Consensus (β₃)",
        min_value=0.0,
        max_value=1.0,
        value=config.get("neuron.beta_3", 0.2),
        step=0.01,
        help="Influence du consensus réseau"
    )
    
    # Paramètres réseau
    st.subheader("Paramètres Réseau")
    
    local_port = st.number_input(
        "Port Local",
        min_value=1000,
        max_value=65535,
        value=config.get("network.local_port", 5000),
        help="Port d'écoute pour les connexions P2P"
    )
    
    bootstrap_node = st.text_input(
        "Nœud Bootstrap",
        value="",
        help="Adresse du nœud bootstrap (format: host:port)"
    )
    
    # Boutons de contrôle
    st.header("Contrôles")
    
    if st.button("Initialiser Neurone"):
        with st.spinner("Initialisation du neurone..."):
            try:
                # Créer le neurone
                st.session_state.neuron = QuantumGravitationalNeuron(
                    grid_size=grid_size,
                    time_steps=time_steps,
                    p_0=p_0,
                    beta_1=beta_1,
                    beta_2=beta_2,
                    beta_3=beta_3
                )
                
                # Réinitialiser les historiques
                st.session_state.activation_history = []
                st.session_state.creativity_history = []
                st.session_state.decision_history = []
                st.session_state.network_history = []
                st.session_state.timestamps = []
                
                st.success("Neurone initialisé avec succès")
                st.session_state.last_update = datetime.now()
            except Exception as e:
                st.error(f"Erreur lors de l'initialisation: {str(e)}")
                logger.error(f"Initialization error: {e}", exc_info=True)
    
    col_sim1, col_sim2 = st.columns(2)
    
    with col_sim1:
        start_button = st.button(
            "Démarrer Simulation",
            disabled=st.session_state.neuron is None or st.session_state.simulation_running
        )
    
    with col_sim2:
        stop_button = st.button(
            "Arrêter Simulation",
            disabled=not st.session_state.simulation_running
        )
    
    if start_button:
        st.session_state.simulation_running = True
    
    if stop_button:
        st.session_state.simulation_running = False

# Colonne 1: Visualisations et simulation
with col1:
    st.header("Simulation d'Espace-Temps")
    
    # Onglets pour différentes visualisations
    viz_tabs = st.tabs(["Visualisation 3D", "Coupe 2D"])
    
    # Tab 1: Visualisation 3D
    with viz_tabs[0]:
        viz_3d_placeholder = st.empty()
    
    # Tab 2: Coupe 2D
    with viz_tabs[1]:
        viz_2d_placeholder = st.empty()
    
    # Section métriques
    st.subheader("Métriques de Simulation")
    metrics_container = st.container()

# Colonne 2: État neuronal et réseau
with col2:
    st.header("État du Neurone")
    
    # Onglets pour différentes informations
    info_tabs = st.tabs(["Activation", "Réseau", "Journal"])
    
    # Tab 1: Activation neuronale
    with info_tabs[0]:
        # ID du neurone et activation
        neuron_info = st.empty()
        
        # Graphique d'activation
        activation_chart = st.empty()
    
    # Tab 2: État du réseau
    with info_tabs[1]:
        network_status = st.empty()
        peers_list = st.empty()
    
    # Tab 3: Journal
    with info_tabs[2]:
        log_container = st.empty()

# Fonction pour mettre à jour les visualisations
def update_visualizations():
    if st.session_state.neuron is None:
        return
    
    try:
        # Obtenir l'état actuel
        current_state = st.session_state.neuron.simulator.get_current_state()
        
        # Visualisation 3D
        with viz_3d_placeholder.container():
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Trouver les points significatifs (au-dessus du 99e percentile)
            threshold = np.percentile(current_state, 99)
            mask = current_state > threshold
            x, y, z = np.nonzero(mask)
            values = current_state[mask]
            
            # Créer scatter plot
            scatter = ax.scatter(x, y, z,
                              c=values,
                              cmap='viridis',
                              alpha=0.6,
                              marker='o',
                              s=30)
            
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Fluctuations Quantiques Significatives')
            
            plt.colorbar(scatter, ax=ax, label='Intensité')
            st.pyplot(fig)
            plt.close(fig)
        
        # Visualisation 2D (coupe)
        with viz_2d_placeholder.container():
            fig, ax = plt.subplots(figsize=(8, 8))
            
            # Prendre une coupe au milieu
            slice_idx = current_state.shape[0] // 2
            slice_data = current_state[slice_idx, :, :]
            
            im = ax.imshow(slice_data, cmap='viridis', interpolation='nearest')
            ax.set_title(f'Coupe à z={slice_idx}')
            plt.colorbar(im, ax=ax, label='Intensité')
            
            st.pyplot(fig)
            plt.close(fig)
        
        # Métriques
        with metrics_container:
            metrics = st.session_state.neuron.simulator.get_metrics()
            
            col1_m, col2_m, col3_m = st.columns(3)
            
            with col1_m:
                st.metric("Courbure Moyenne", f"{metrics.get('mean_curvature', 0):.2e}")
                st.metric("Courbure Min", f"{metrics.get('min_curvature', 0):.2e}")
            
            with col2_m:
                st.metric("Courbure Max", f"{metrics.get('max_curvature', 0):.2e}")
                st.metric("Écart Type", f"{metrics.get('std_deviation', 0):.2e}")
            
            with col3_m:
                st.metric("Énergie Totale", f"{metrics.get('total_energy', 0):.2e}")
                st.metric("Densité Quantique", f"{metrics.get('quantum_density', 0):.2e}")
    
    except Exception as e:
        st.error(f"Erreur de visualisation: {str(e)}")
        logger.error(f"Visualization error: {e}", exc_info=True)

# Fonction pour mettre à jour l'état neuronal
def update_neuron_state():
    if st.session_state.neuron is None:
        return
    
    try:
        # Info neuronale
        with neuron_info:
            neuron_data = st.session_state.neuron.get_neuron_state()
            
            # Afficher l'ID et l'activation avec style conditionnel
            activation = neuron_data.get('activation', 0)
            
            if activation >= 0.7:
                activation_class = "activation-high"
            elif activation >= 0.3:
                activation_class = "activation-medium"
            else:
                activation_class = "activation-low"
            
            st.markdown(f"""
            <div class="neuron-metrics">
                <p><b>ID du Neurone:</b> {neuron_data.get('node_id', 'Non initialisé')}</p>
                <p><b>Activation:</b> <span class="{activation_class}">{activation:.4f}</span></p>
                <p><b>Créativité:</b> {neuron_data.get('creativity', 0):.4f}</p>
                <p><b>Décision:</b> {neuron_data.get('decision', 0):.4f}</p>
                <p><b>Consensus Réseau:</b> {neuron_data.get('network_consensus', 0):.4f}</p>
                <p><b>Itérations:</b> {neuron_data.get('iterations', 0)}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Graphiques d'activation
        with activation_chart:
            # Mettre à jour les historiques
            if st.session_state.neuron.activation_history:
                st.session_state.activation_history.append(st.session_state.neuron.activation_history[-1])
            else:
                st.session_state.activation_history.append(0)
                
            if st.session_state.neuron.creativity_history:
                st.session_state.creativity_history.append(st.session_state.neuron.creativity_history[-1])
            else:
                st.session_state.creativity_history.append(0)
                
            if st.session_state.neuron.decision_history:
                st.session_state.decision_history.append(st.session_state.neuron.decision_history[-1])
            else:
                st.session_state.decision_history.append(0)
                
            if st.session_state.neuron.network_consensus_history:
                st.session_state.network_history.append(st.session_state.neuron.network_consensus_history[-1])
            else:
                st.session_state.network_history.append(0)
                
            st.session_state.timestamps.append(len(st.session_state.timestamps))
            
            # Limiter la taille des historiques
            max_history = 100
            if len(st.session_state.activation_history) > max_history:
                st.session_state.activation_history = st.session_state.activation_history[-max_history:]
                st.session_state.creativity_history = st.session_state.creativity_history[-max_history:]
                st.session_state.decision_history = st.session_state.decision_history[-max_history:]
                st.session_state.network_history = st.session_state.network_history[-max_history:]
                st.session_state.timestamps = st.session_state.timestamps[-max_history:]
            
            # Créer le graphique
            fig, ax = plt.subplots(figsize=(8, 5))
            
            ax.plot(st.session_state.timestamps, st.session_state.activation_history, 
                   label="Activation", color='#7792E3', linewidth=2)
            ax.plot(st.session_state.timestamps, st.session_state.creativity_history, 
                   label="Créativité", color='#FFA500', linewidth=1.5)
            ax.plot(st.session_state.timestamps, st.session_state.decision_history, 
                   label="Décision", color='#4CAF50', linewidth=1.5)
            ax.plot(st.session_state.timestamps, st.session_state.network_history, 
                   label="Consensus", color='#E91E63', linewidth=1.5)
            
            ax.set_xlabel('Itérations')
            ax.set_ylabel('Valeur')
            ax.set_ylim(0, 1)
            ax.grid(True, alpha=0.3)
            ax.legend(loc='upper left')
            
            ax.set_title('Évolution Neuronale au Cours du Temps')
            
            st.pyplot(fig)
            plt.close(fig)
    
    except Exception as e:
        st.error(f"Erreur de mise à jour neuronale: {str(e)}")
        logger.error(f"Neuron update error: {e}", exc_info=True)

# Fonction pour mettre à jour l'état du réseau
def update_network_state():
    if st.session_state.neuron is None:
        return
    
    try:
        # État du réseau
        with network_status:
            st.markdown(f"""
            <div class="network-status">
                <p><b>État du Réseau:</b> {'En ligne' if st.session_state.peer_count > 0 else 'Hors ligne'}</p>
                <p><b>Pairs Connectés:</b> {st.session_state.peer_count}</p>
                <p><b>Dernière Mise à Jour:</b> {st.session_state.last_update.strftime('%H:%M:%S') if st.session_state.last_update else 'Jamais'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Liste des pairs
        with peers_list:
            if not st.session_state.neuron.neighbors:
                st.info("Aucun pair connecté")
            else:
                st.write("Pairs connectés:")
                for peer_id, weight in st.session_state.neuron.neighbors.items():
                    st.progress(weight, text=f"{peer_id[:8]}... ({weight:.2f})")
    
    except Exception as e:
        st.error(f"Erreur de mise à jour réseau: {str(e)}")
        logger.error(f"Network update error: {e}", exc_info=True)

# Fonction pour mettre à jour le journal
def update_log():
    with log_container:
        # Pour l'instant, utiliser des entrées fictives
        if st.session_state.neuron is not None:
            st.write(f"Session active, {st.session_state.neuron.iterations} itérations effectuées")
            
            # Si des itérations ont été effectuées, afficher des infos
            if st.session_state.neuron.iterations > 0:
                metrics = st.session_state.neuron.simulator.get_metrics()
                
                # Créer un journal avec les dernières activités
                log_entries = []
                log_entries.append(f"[{datetime.now().strftime('%H:%M:%S')}] Itération {st.session_state.neuron.iterations} complétée")
                
                if st.session_state.neuron.activation_history:
                    activation = st.session_state.neuron.activation_history[-1]
                    log_entries.append(f"[{datetime.now().strftime('%H:%M:%S')}] Activation neuronale: {activation:.4f}")
                
                log_entries.append(f"[{datetime.now().strftime('%H:%M:%S')}] Énergie totale: {metrics.get('total_energy', 0):.2e}")
                
                st.text_area("Journal d'activité", "\n".join(log_entries), height=300)
        else:
            st.info("Neurone non initialisé")

# Fonction principale de simulation
def simulation_loop():
    while True:
        try:
            # Si la simulation est en cours et le neurone est initialisé
            if st.session_state.simulation_running and st.session_state.neuron is not None:
                # Effectuer une étape de simulation
                peer_states = {}  # À remplacer par les vrais états des pairs quand le réseau est implémenté
                st.session_state.neuron.neuron_step(intensity, peer_states)
                
                # Mettre à jour le timestamp
                st.session_state.last_update = datetime.now()
            
            # Pause pour éviter de surcharger le CPU
            time.sleep(0.1)
        
        except Exception as e:
            logger.error(f"Simulation error: {e}", exc_info=True)
            time.sleep(1)  # Pause plus longue en cas d'erreur

# Démarrer la boucle de simulation dans un thread séparé
def start_simulation_thread():
    simulation_thread = threading.Thread(target=simulation_loop, daemon=True)
    simulation_thread.start()

# Démarrer le thread de simulation
start_simulation_thread()

# Boucle principale Streamlit
while True:
    # Mettre à jour les visualisations et informations
    if st.session_state.neuron is not None:
        update_visualizations()
        update_neuron_state()
        update_network_state()
        update_log()
    
    # Attendre avant la prochaine mise à jour
    time.sleep(0.5)
    
    # Rafraîchir l'interface (via rerun)
    st.experimental_rerun()