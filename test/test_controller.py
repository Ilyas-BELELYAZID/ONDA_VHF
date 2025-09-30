# test_controller.py
import asyncio
import logging
import signal
import sys

from controllers.recepteur_controller import RecepteurController
from PySide6.QtCore import QCoreApplication
app = QCoreApplication.instance() or QCoreApplication([])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pymodbus")
logger.setLevel(logging.ERROR) # ou ERROR


async def data_callback(data):
    """Callback appelé à chaque cycle de lecture du controller."""
    print("\n--- Lecture reçu ---")
    print(f"Fréquence : {data['frequency_mhz']} MHz")
    print(f"RSSI      : {data['rssi_dbm']} dBm")
    print(f"SNR       : {data['snr_db']} dB")
    print(f"Squelch   : {data['squelch']}")


async def main():
    # configuration
    DEVICE_ID = 2
    POLL_INTERVAL = 3.0
    MODBUS_PORT = "COM2"     # adapte si nécessaire
    BAUDRATE = 9600

    controller = RecepteurController(device_id=DEVICE_ID,
                                     poll_interval=POLL_INTERVAL)

    controller.sound.play = lambda level=None: print("[SOUND]", level)

    # 1) Connexion unique initiale (pour pouvoir appeler setters de façon fiable)
    print("-> Connexion Modbus initiale...")
    connected = await controller.modbus.connect()
    print("   connecté:" if connected else "   échec de connexion")
    if not connected:
        print("Impossible de se connecter au port série — vérifie le câble / simulateur.")
        return

    # IMPORTANT: empêcher start_polling() de recréer un nouveau client lors du test.
    # On remplace temporairement `controller.modbus.connect` par une petite coroutine qui renvoie True.
    async def _dummy_connect():
        return True

    controller.modbus.connect = _dummy_connect

    # 2) Tester set_frequency (async maintenant)
    print("\n--- TEST : set_frequency(125.5) ---")
    ok, err = await controller.set_frequency(125.5)
    print("Résultat:", "OK" if ok else f"Erreur: {err}")

    # 3) Tester set_squelch (async)
    print("\n--- TEST : set_squelch(20) ---")
    ok, err = await controller.set_squelch(20)
    print("Résultat:", "OK" if ok else f"Erreur: {err}")

    # 4) Optionnel : scanner les devices présents sur le bus (rapide scan 1..50)
    print("\n--- TEST : scan/count devices (1..50) ---")
    try:
        # connect_if_needed=False car on est déjà connecté
        count, ids = await controller.modbus.count_devices(start=1, end=50,
                                                           address=0, count=1,
                                                           delay=0.01,
                                                           connect_if_needed=False)
        print(f"Résultat: {count} device(s) trouvés -> {ids}")
    except Exception as e:
        print("Erreur lors du scan:", e)

    # 5) Lancer le polling (en tâche séparée)
    print("\n--- Lancement du polling (Ctrl+C pour arrêter) ---")
    polling_task = asyncio.create_task(controller.start_polling(callback=data_callback))

    # Gestion d'arrêt propre cross-platform :
    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    def _signal_handler():
        logger.info("Signal d'arrêt reçu.")
        stop_event.set()

    # try to register signal handlers (may fail on Windows when not main thread)
    try:
        loop.add_signal_handler(signal.SIGINT, _signal_handler)
        loop.add_signal_handler(signal.SIGTERM, _signal_handler)
    except NotImplementedError:
        # fallback: we'll catch KeyboardInterrupt below
        pass

    try:
        # attente jusqu'à réception du signal / Ctrl+C
        await stop_event.wait()
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt capturé.")
    finally:
        print("\nArrêt demandé : shutting down...")
        # 6) Arrêt du polling et fermeture propre
        controller.running = False
        polling_task.cancel()
        try:
            await polling_task
        except asyncio.CancelledError:
            pass
        # fermer proprement le controller/modbus
        try:
            await controller.close()
        except Exception as e:
            logger.exception("Erreur lors de controller.close(): %s", e)

        print("Terminé. Sortie.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nArrêt par l'utilisateur (KeyboardInterrupt).")
        try:
            sys.exit(0)
        except SystemExit:
            pass
