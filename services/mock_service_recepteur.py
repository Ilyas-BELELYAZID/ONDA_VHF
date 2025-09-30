import asyncio
import time
from PySide6.QtCore import Signal

# =============================================================================
# CLASSES MOCK (SIMULATIONS DE SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """
    Simule un client Modbus avec des valeurs qui changent pour tester les alertes.
    """
    def __init__(self, device_id=2):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        # [Freq*100, RSSI, SNR*10, Squelch, Temp*10, Volt*10]
        self.regs = [12550, 65486, 250, 10, 350, 240] # Freq=125.5, RSSI=-50, SNR=25.0
        self.start_time = time.time()

    async def connect(self):
        print("[MockModbus] Connexion simulée réussie.")
        await asyncio.sleep(0.1)
        return True

    async def read_holding(self, address, count):
        # Simule des conditions changeantes toutes les ~10 secondes
        elapsed = time.time() - self.start_time
        cycle_time = 30 # Durée d'un cycle complet de simulation

        if (elapsed % cycle_time) < 10: # 0-10s: Signal Normal
            self.regs[1] = 65486 # RSSI = -50 dBm (signed: -50 + 65536)
            self.regs[2] = 250   # SNR = 25.0 dB
            self.regs[4] = 350 # Temp = 35°C
            self.regs[5] = 240 # Volt = 24V
        elif (elapsed % cycle_time) < 20: # 10-20s: Signal Faible (Warning/Critical)
            self.regs[1] = 65436 # RSSI = -100 dBm
            self.regs[4] = 480 # Temp = 48°C
        else: # 20-30s: Interférences (SNR bas)
            self.regs[1] = 65486 # Retour à RSSI normal
            self.regs[2] = 50    # SNR = 5.0 dB
            self.regs[4] = 600 # Temp = 60°C

        print(f"[MockModbus] Lecture... retourne {self.regs}")
        await asyncio.sleep(0.2)
        return self.regs

    def write_register(self, address: int, value: int):
        print(f"[MockModbus] Écriture... reg[{address}] = {value}")
        if address < len(self.regs):
            self.regs[address] = value
            asyncio.sleep(0.1)
            return True
        return False

    async def close(self):
        print("[MockModbus] Connexion fermée.")