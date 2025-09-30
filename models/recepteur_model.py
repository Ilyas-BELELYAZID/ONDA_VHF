from typing import Optional, Dict
import datetime
from services.database_service import DatabaseService


class RecepteurModel:
    def __init__(self, db : DatabaseService = None):
        self.db = db or DatabaseService()

    def save_recepteur(self, data: Dict, id_recepteur: int = 1):
        """
        Insert or update the latest snapshot of the receiver.
        data keys: frequency_mhz, rssi_dbm, noise_db, squelch, last_update
        """
        data = {
                "id": id_recepteur,
                "frequency_mhz": float(data.get("frequency_mhz", 0.0)),
                "rssi_dbm": float(data.get("rssi_dbm", 0.0)),
                "noise_db": float(data.get("snr_db", 0.0)),
                "squelch": int(data.get("squelch", 0)),
                "last_update": datetime.datetime.now()
            }

        # Sauvegarde MySQL
        self.db.execute_query(
            """
            INSERT INTO recepteurs (id, frequency_mhz, rssi_dbm, noise_db, squelch, last_update)
            VALUES (%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
                frequency_mhz=VALUES(frequency_mhz),
                rssi_dbm=VALUES(rssi_dbm),
                noise_db=VALUES(noise_db),
                squelch=VALUES(squelch),
                last_update=VALUES(last_update)
            """,
            (data["id"], data["frequency_mhz"], data["rssi_dbm"], data["noise_db"], data["squelch"], data["last_update"])
        ) 
        return True

    def get_latest(self, id_recepteur: int = 1) -> Optional[Dict]:
        return self.db.fetch_one("SELECT * FROM recepteurs WHERE id=%s", (id_recepteur,))
