import datetime
from typing import Optional, Dict
from services.database_service import DatabaseService

class BasculeurModel:
    def __init__(self, db : DatabaseService = None):
        self.db = db or DatabaseService()

    def save_basculeur(self, data: Dict, id_basculeur: int = 1):
        """
        Insert or update current state of basculeur.
        data keys: active_path ('PRINCIPAL'|'SECOURS'), auto_enabled (bool), last_update (datetime)
        """
        data = {
                "id": id_basculeur,
                "active_path": data.get("active_path", "PRINCIPAL"),
                "auto_enabled": 1 if data.get("auto_enabled", True) else 0,
                "cause_code": data.get("cause_code", None),
                "cause_basculement": data.get("cause_basculement", None),
                "last_switch": data.get("last_switch") or datetime.datetime.now()
            }

        # Sauvegarde MySQL
        self.db.execute_query(
            """
            INSERT INTO basculeurs (id, active_path, auto_enabled, cause_code, cause_basculement, last_switch)
            VALUES (%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
                active_path=VALUES(active_path),
                auto_enabled=VALUES(auto_enabled),
                cause_code=VALUES(cause_code),
                cause_basculement=VALUES(cause_basculement),
                last_switch=VALUES(last_switch)
            """,
            (data["id"], data["active_path"], data["auto_enabled"], data["cause_code"], data["cause_basculement"], data["last_switch"])
        ) 
        return True

    def get_latest(self, id_basculeur: int = 1) -> Optional[Dict]:
        return self.db.fetch_one("SELECT * FROM basculeurs WHERE id=%s", (id_basculeur,))
