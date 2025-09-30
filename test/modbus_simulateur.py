"""
Simulateur d'équipements VHF pour l'ONDA.
Ce script lance un serveur Modbus TCP sur localhost:5020 avec 3 escalves :
1 = Émetteur, 2 = Récepteur, 3 = Basculeur
Il simule un émetteur, un récepteur et un basculeur en mettant à jour
périodiquement leurs registres respectifs.

Compatible avec Pymodbus 3.11.1.
"""
import random
import time
import threading
import logging
import asyncio

from pymodbus.server import ModbusTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# --- Création des trois esclaves ---
store_emetteur = ModbusSequentialDataBlock(0, [0]*100)
store_recepteur = ModbusSequentialDataBlock(0, [0]*100)
store_basculeur = ModbusSequentialDataBlock(0, [0]*100)

# Contexte serveur multi-esclaves
context = ModbusServerContext(
    devices={1: store_emetteur, 2: store_recepteur, 3: store_basculeur},
    single=False
)

# Pour accéder aux esclaves plus facilement, on garde un dictionnaire
slaves = {
    1: store_emetteur,
    2: store_recepteur,
    3: store_basculeur
}

def update_registers_loop():
    """
    Boucle infinie qui met à jour les valeurs des registres toutes les 3 secondes.
    Lancée dans un thread séparé.
    """
    log.info("Démarrage du thread de mise à jour des registres.")

    while True:
        try:
            # --- ESCLAVE 1 : ÉMETTEUR (adresses 0-5) ---
            hr = slaves[1].getValues(0, 30)
            hr[0] = int(11870) # fréquence (valeur * 100)
            hr[1] = int(random.uniform(49.5, 51.0) * 10)   # Puissance (W *10)
            hr[2] = int(random.uniform(35.0, 56.0) * 10)   # Température (°C *10)
            hr[3] = int(random.uniform(86.0, 98.0) * 10)   # Modulation (% *10)
            hr[4] = int(random.uniform(20.5, 31.5) * 10)   # Tension (V *10)
            hr[5] = 1 # ON/OFF
            slaves[1].setValues(0, hr)

            # --- ESCLAVE 2 : RÉCEPTEUR (adresses 10–13) ---
            hr = slaves[2].getValues(0, 30)
            hr[10] = int(11870) # 118.70 MHz (valeur * 100)
            rssi_val = int(random.uniform(-90.0, -35.0) * 10)
            hr[11] = rssi_val & 0xFFFF  # RSSI en 16-bit non signé
            hr[12] = int(random.uniform(25.0, 35.0) * 10)  # Bruit (dB *10)

            # Squelch (niveau de 0 à 50)
            # Ce registre peut être lu et écrit pour simuler la configuration
            hr[13] = 5 # Exemple de valeur fixe, modifiable par le client
            slaves[2].setValues(0, hr)

            # --- ESCLAVE 3 : BASCULEUR (adresses 20–22) ---
            hr = slaves[3].getValues(0, 30)
            # Voie active (0=Principal, 1=Secours)
            hr[20] = 0 # Valeur fixe, modifiable par le client
            
            # Mode auto (1=Auto, 0=Manuel)
            hr[21] = 1 # Valeur fixe, modifiable par le client

            hr[22] = int(time.time()) % 65535  # Timestamp modulo 16-bit

            slaves[3].setValues(0, hr)

            log.debug("Registres mis à jour avec de nouvelles valeurs simulées.")

        except Exception as e:
            log.error(f"Erreur dans la boucle de mise à jour: {e}")

        time.sleep(3)  # Pause avant prochaine mise à jour

async def run_server():
    """Fonction principale pour lancer le serveur et le thread de mise à jour."""
    # 3. Thread de mise à jour
    threading.Thread(
        target=update_registers_loop, daemon=True
    ).start()

    # 4. Démarrage du serveur Modbus TCP
    server = ModbusTcpServer(
        context=context, 
        address=("localhost", 5020)
    )
    log.info("🚀 Lancement du simulateur Modbus TCP multi-esclaves sur localhost:5020")
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(run_server())
