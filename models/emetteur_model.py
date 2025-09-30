from typing import Optional, Dict
import datetime
from services.database_service import DatabaseService

class EmetteurModel:
    def __init__(self, db : DatabaseService = None):
        self.db = db or DatabaseService()

    def save_emetteur(self, data: Dict, id_emetteur: int = 1):
        """
        Insert or update the latest snapshot of the transmitter.
        data keys: frequency_mhz, power_pct, temperature_c, modulation_rate, tension_alim, enabled, created_at
        """
        data = {
                "id": id_emetteur,
                "frequency_mhz": float(data.get("frequency_mhz", 0.0)),
                "power_pct": float(data.get("power_pct", 0.0)),
                "temperature_c": float(data.get("temperature_c", 0.0)),
                "modulation_rate": float(data.get("modulation_rate", 0.0)),
                "tension_alim": float(data.get("tension_alim", 0.0)),
                "enabled": 1 if data.get("enabled", True) else 0,
                "created_at": datetime.datetime.now(),
            }

        # Sauvegarde MySQL
        self.db.execute_query(
            """
            INSERT INTO emetteurs(id, frequency_mhz, power_pct, temperature_c, modulation_rate, tension_alim, enabled, created_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
                frequency_mhz=VALUES(frequency_mhz),
                power_pct=VALUES(power_pct),
                temperature_c=VALUES(temperature_c),
                modulation_rate=VALUES(modulation_rate),
                tension_alim=VALUES(tension_alim),
                enabled=VALUES(enabled),
                created_at=VALUES(created_at)
            """,
            (data["id"], data["frequency_mhz"], data["power_pct"], data["temperature_c"], data["modulation_rate"], data["tension_alim"], data["enabled"], data["created_at"])
        )
        return True

    def get_latest(self, id_emetteur: int = 1) -> Optional[Dict]:
        return self.db.fetch_one("SELECT * FROM emetteurs WHERE id=%s", (id_emetteur,))
