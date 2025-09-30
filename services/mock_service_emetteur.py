import time
import random

# =============================================================================
# CLASSES MOCK (SIMULATIONS DE SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """Simule un client Modbus avec des valeurs qui changent pour tester les alertes."""
    def __init__(self, device_id=1):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        # [Freq, Power, Temp, Mod, Volt, ROS, Enabled]
        # Les valeurs sont multipliées par 10 pour simuler une décimale
        self.regs = [11870, 500, 350, 850, 240, 11, 1]
        self.start_time = time.time()

    def connect(self):
        print("[MockModbus] Connexion (bloquante) simulée.")
        time.sleep(0.2) # Simule un appel réseau bloquant
        return True

    def read_holding(self, address, count):
        # Simule des conditions changeantes
        elapsed = time.time() - self.start_time
        cycle_time = 30

        if (elapsed % cycle_time) < 10: # Normal
            self.regs[2] = 350 # Temp = 35°C
            self.regs[1] = 500 # Power = 50W
            self.regs[4] = 240 # Volt = 24V
        elif (elapsed % cycle_time) < 20: # Température haute (Warning)
            self.regs[2] = 480 # Temp = 48°C
        elif (elapsed % cycle_time) < 30: # Température critique
            self.regs[2] = random.randint(560, 650) # Temp 
        else: # Puissance hors bornes
            self.regs[2] = random.randint(350, 450)
            self.regs[1] = 40 # Power = 4W
        
        # --- Cycle de simulation du ROS et de la Puissance ---
        if (elapsed % cycle_time) < 20: # 20s Normal
            self.regs[5] = random.randint(11, 13) # ROS = 1.1 - 1.3
            self.regs[1] = 500 # Puissance = 50.0W (pleine puissance)
        elif (elapsed % cycle_time) < 30: # 10s Alerte ROS (Warning)
            self.regs[5] = random.randint(21, 28) # ROS = 2.1 - 2.8
            self.regs[1] = 500 # La puissance n'est pas encore réduite
        else: # 10s ROS Critique -> Réduction de puissance
            self.regs[5] = random.randint(35, 50) # ROS = 3.5 - 5.0 (Critique)
            self.regs[1] = 250 # L'émetteur réduit la puissance à 25.0W

        print(f"[MockModbus] Lecture (bloquante)... retourne {self.regs}")
        time.sleep(0.3)
        return self.regs

    def write_register(self, address: int, value: int):
        print(f"[MockModbus] Écriture (bloquante)... reg[{address}] = {value}")
        if address < len(self.regs):
            self.regs[address] = value
            time.sleep(0.1)
            return True
        return False

    def close(self):
        print("[MockModbus] Connexion fermée.")