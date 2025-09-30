import time
import random
from pymodbus.client import ModbusTcpClient

# Connexion au serveur
client = ModbusTcpClient("localhost", port=5020)

# ======================
# ÉMETTEUR
# ======================
def read_emetteur():
    rr = client.read_holding_registers(0, 6, slave=1)  # lecture 6 registres à partir de 0
    if rr.isError():
        return None
    return rr.registers

def write_emetteur():
    freq = random.randint(118000, 121000)  # 118.000 à 121.000 MHz *1000
    onoff = random.choice([0, 1])
    client.write_registers(0, [freq], slave=1)   # écriture fréquence
    client.write_registers(5, [onoff], slave=1)  # écriture ON/OFF
    return freq, onoff

# ======================
# RÉCEPTEUR
# ======================
def read_recepteur():
    rr = client.read_holding_registers(10, 4, slave=2)  # lecture 4 registres à partir de 10
    if rr.isError():
        return None
    return rr.registers

def write_recepteur():
    squelch = random.randint(0, 50)
    client.write_registers(13, [squelch], slave=2)
    return squelch

# ======================
# BASCULEUR
# ======================
def read_basculeur():
    rr = client.read_holding_registers(20, 3, slave=3)  # lecture 3 registres à partir de 20
    if rr.isError():
        return None
    return rr.registers

def write_basculeur():
    active = random.choice([0, 1])
    mode_auto = random.choice([0, 1])
    client.write_registers(20, [active], slave=3)
    client.write_registers(21, [mode_auto], slave=3)
    return active, mode_auto

# ======================
# BOUCLE PRINCIPALE
# ======================
try:
    while True:
        # Écriture aléatoire
        freq, onoff = write_emetteur()
        squelch = write_recepteur()
        active, mode_auto = write_basculeur()

        # Lecture des registres
        e = read_emetteur()
        r = read_recepteur()
        b = read_basculeur()

        print("=== Émetteur ===")
        print(f"Registres: {e}, Fréquence écrite: {freq}, ON/OFF: {onoff}")
        print("=== Récepteur ===")
        print(f"Registres: {r}, Squelch écrit: {squelch}")
        print("=== Basculeur ===")
        print(f"Registres: {b}, Active: {active}, Mode Auto: {mode_auto}")
        print("-" * 60)

        time.sleep(3)

except KeyboardInterrupt:
    print("Fermeture du client...")
finally:
    client.close()
