import asyncio
from services.modbus_service import ModbusService

async def progress_cb(device_id, ok):
    status = "OK" if ok else "no"
    print(f"ID {device_id:3d} -> {status}")

async def main():
    # Réglage: timeout court pour accélérer le scan si tu le souhaites
    service = ModbusService(timeout=0.3)

    try:
        print("Connexion au port...", end=" ")
        connected = await service.connect()
        print("OK" if connected else "ÉCHEC")
        if not connected:
            return

        # Scanner la plage 1..50 (adapte selon ton besoin)
        print("Lancement du scan (1..50) — ça peut prendre quelques secondes...")
        count, ids = await service.count_devices(start=1, end=50, address=0, count=1, delay=0.02,
                                                 connect_if_needed=False, progress_callback=progress_cb)
        print(f"\nRésultat: {count} device(s) trouvés -> {ids}")

    except Exception as e:
        print("Erreur durant le scan:", e)
    finally:
        # fermer proprement
        await service.close()
        print("Connexion Modbus fermée.")

if __name__ == "__main__":
    asyncio.run(main())
