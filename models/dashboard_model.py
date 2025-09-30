import asyncio
from datetime import datetime, date
from services.database_service import DatabaseService
from services.modbus_service import ModbusService
import typing

class DashboardModel:
    def __init__(self, db : DatabaseService = None):
        self.db = db or DatabaseService()
        self.count = 0

    async def progress_cb(device_id, ok):
        status = "OK" if ok else "no"
        print(f"ID {device_id:3d} -> {status}")
    """
    async def get_equipment_count(self): # Run it as: asyncio.run(get_equipment_count())
        service = ModbusService(timeout=0.3)

        try:
            print("Connexion au port...", end=" ")
            connected = await service.connect()
            print("OK" if connected else "ÉCHEC")
            if not connected:
                return

            # Scanner la plage 1..50 (adapte selon ton besoin)
            print("Lancement du scan (1..50) — ça peut prendre quelques secondes...")
            self.count, ids = await service.count_devices(start=1, end=50, address=0, count=1, delay=0.02,
                                                    connect_if_needed=False, progress_callback=self.progress_cb)
            print(f"\nRésultat: {self.count} device(s) trouvés -> {ids}")

        except Exception as e:
            print("Erreur durant le scan:", e)
        finally:
            # fermer proprement
            await service.close()
            print("Connexion Modbus fermée.")
            return self.count
    """

    def get_recent_alerts(self, limit=6):
        # Certains connecteurs MySQL n'autorise pas les placeholders pour LIMIT.
        # On force un int puis on injecte proprement la valeur (sécurisé car c'est un entier).
        try:
            limit = int(limit)
        except Exception:
            limit = 6
        return self.db.fetch_query(f"SELECT * FROM alertes ORDER BY timestamp DESC LIMIT {limit}")

    def get_last_update_time(self):
        row = self.db.fetch_one("SELECT MAX(timestamp) as last FROM alertes")
        return row.get("last") if row else None

    def get_current_system_state(self, limit: int = 6):
        try:
            limit = int(limit)
        except Exception:
            limit = 10

        # On sélectionne les 'limit' dernières alertes dans une sous-requête puis on agrège.
        query = f"""
        SELECT
        SUM(CASE WHEN severity='CRITICAL' AND resolved=0 THEN 1 ELSE 0 END) AS cnt_critical,
        SUM(CASE WHEN severity='WARNING'  AND resolved=0 THEN 1 ELSE 0 END) AS cnt_warning
        FROM (
        SELECT severity, resolved
        FROM alertes
        ORDER BY timestamp DESC
        LIMIT {limit}
        ) AS recent
        """

        row = self.db.fetch_one(query)
        if row and row.get("cnt_critical", 0) > 0:
            return "Erreur"
        if row and row.get("cnt_warning", 0) > 0:
            return "Dégradé"
        return "OK"
