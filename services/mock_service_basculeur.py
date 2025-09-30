import asyncio
import time

# =============================================================================
# CLASSES MOCK (SIMULATIONS DE SERVICES ET MODÈLES)
# =============================================================================

class MockModbusService:
    """Simule un client Modbus. Change d'état toutes les 15 secondes."""
    def __init__(self, device_id=3):
        print(f"[MockModbus] Initialisé pour l'appareil {device_id}.")
        self.regs = [0, 1, 1]  # [active_path, auto_enabled, cause_code]
        self.last_change_time = time.time()
        self.state_cycle = [
            # Normal -> Défaillance -> Manuel -> Retour Normal
            {'regs': [0, 1, 1], 'duration': 15},  # Principal, Auto, Cause: Auto
            {'regs': [1, 1, 2], 'duration': 10},  # Secours, Auto, Cause: Défaillance
            {'regs': [1, 0, 0], 'duration': 12},  # Secours, Manuel, Cause: Manuel
            {'regs': [0, 1, 1], 'duration': 15},  # Retour Principal
        ]
        self.current_state_index = 0

    async def connect(self):
        print("[MockModbus] Connexion simulée réussie.")
        await asyncio.sleep(0.1)
        return True

    async def read_holding(self, address, count):
        # Simule un changement d'état après une certaine durée
        current_state = self.state_cycle[self.current_state_index]
        if time.time() - self.last_change_time > current_state['duration']:
            self.current_state_index = (self.current_state_index + 1) % len(self.state_cycle)
            self.regs = self.state_cycle[self.current_state_index]['regs']
            self.last_change_time = time.time()
            print(f"[MockModbus] CHANGEMENT D'ÉTAT SIMULÉ -> {self.regs}")

        print(f"[MockModbus] Lecture... retourne {self.regs}")
        await asyncio.sleep(0.2)
        return self.regs

    async def write_register(self, address: int, value: int):
        print(f"[MockModbus] Écriture... reg[{address}] = {value}")
        if address < len(self.regs):
            self.regs[address] = value
            await asyncio.sleep(0.1)
            return True
        return False

    async def close(self):
        print("[MockModbus] Connexion fermée.")