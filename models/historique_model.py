import datetime
from typing import Optional, Dict, List
from services.database_service import DatabaseService

class HistoriqueModel:
    def __init__(self, db : DatabaseService = None):
        self.db = db or DatabaseService()

    def save_event(self, event: Dict):
        """
        event: { event_type, description, equipment_type, timestamp(optional) }
        """
        data = {
                "event_type": event.get("event_type"),
                "description": event.get("description"),
                "equipment_type": event.get("equipment_type"),
                "timestamp": event.get("timestamp") or datetime.datetime.now()
            }

        # Sauvegarde MySQL
        self.db.execute_query(
            """
            INSERT INTO historique (event_type, description, equipment_type, timestamp)
            VALUES (%s,%s,%s,%s)
            """,
            (data["event_type"], data["description"], data["equipment_type"], data["timestamp"])
        ) 
        return True

    def get_events(self, start_date: Optional[datetime.date] = None,
                   end_date: Optional[datetime.date] = None,
                   event_type: Optional[str] = None,
                   equipment_type: Optional[str] = None,
                   limit: int = 500,
                   auto_severity: bool = True) -> List[Dict]:
        """
        Fetch events with optional filters and automatically add a 'severity' field
        when it is not stored in the DB.

        Parameters
        ----------
        start_date, end_date : datetime.date or 'YYYY-MM-DD' string or None
        event_type, equipment_type : optional filter strings
        limit : max rows to return
        auto_severity : if True, compute severity when not present in DB

        Returns
        -------
        List[Dict] : each dict contains at least the DB columns plus:
            - 'severity' : one of 'CRITIQUE', 'HAUTE', 'FAIBLE'
            - 'created_at' : datetime.datetime object (parsed from timestamp column)
        """
        sql = "SELECT * FROM historique WHERE 1=1"
        params = []
        if start_date:
            sql += " AND timestamp >= %s"
            if isinstance(start_date, str):
                params.append(start_date + " 00:00:00")
            else:
                params.append(str(start_date) + " 00:00:00")
        if end_date:
            sql += " AND timestamp <= %s"
            if isinstance(end_date, str):
                params.append(end_date + " 23:59:59")
            else:
                params.append(str(end_date) + " 23:59:59")
        if event_type and event_type.lower() != "toutes":
            sql += " AND event_type=%s"
            params.append(event_type)
        if equipment_type and equipment_type.lower() != "tous":
            sql += " AND equipment_type=%s"
            params.append(equipment_type)
        sql += " ORDER BY timestamp DESC LIMIT %s"
        params.append(limit)

        rows = self.db.fetch_query(sql, tuple(params))  # on suppose une liste de dicts

        # helper pour parser timestamp en datetime
        def _parse_ts(val):
            if val is None:
                return None
            if isinstance(val, datetime.datetime):
                return val
            if isinstance(val, str):
                # essaie ISO puis format commun
                try:
                    return datetime.datetime.fromisoformat(val)
                except Exception:
                    try:
                        return datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
                    except Exception:
                        return None
            # si int/float -> timestamp unix
            if isinstance(val, (int, float)):
                try:
                    return datetime.datetime.fromtimestamp(int(val))
                except Exception:
                    return None
            return None

        # règles simples pour déduire la gravité si elle n'existe pas
        critical_kw = {"défaillance", "panne", "critical", "critique", "perte de signal", "perte", "échec", "failure", "overheat", "surchauffe", "incendie", "alimentation"}
        warning_kw = {"interférence", "interference", "warning", "alerte", "élevé", "élevée", "température élevée", "basculement non prévu", "basculement innatendu", "dégradation", "latence"}
        moyenne_kw = {"moyenne", "proche du seuil", "configuration bascule automatique"}
        info_kw = {"maintenance", "mise à jour", "info", "résolu", "connexion", "log", "en cours", "ok", "test", "basculement manuel"}

        def _infer_severity(event_type_str, description_str):
            """
            renvoie 'CRITIQUE'|'HAUTE'|'MOYENNE'|'FAIBLE'
            priorité : CRITIQUE > HAUTE > MOYENNE > FAIBLE
            """
            s = ""
            if event_type_str:
                s += str(event_type_str).lower() + " "
            if description_str:
                s += str(description_str).lower() + " "
            text = s

            # check critical keywords
            for kw in critical_kw:
                if kw in text:
                    return "Critique"
            for kw in warning_kw:
                if kw in text:
                    return "Haute"
            for kw in moyenne_kw:
                if kw in text:
                    return "Moyenne"
            # fallback check info keywords
            for kw in info_kw:
                if kw in text:
                    return "Faible"
            # si rien trouvé, considérer FAIBLE par défaut
            return "Faible"

        # Normalisation/ajout du champ severity et parsing timestamp
        normalized = []
        for row in rows:
            # on suppose row est un dict (si ce n'est pas le cas, adapter suivant ta db.fetch_query)
            r = dict(row)  # clone pour ne pas muter l'original
            # gère timestamp / created_at
            ts_val = None
            if "timestamp" in r:
                ts_val = r.get("timestamp")
            elif "created_at" in r:
                ts_val = r.get("created_at")
            parsed_ts = _parse_ts(ts_val)
            # expose created_at toujours comme datetime (compatibilité)
            r["timestamp"] = parsed_ts or r.get("timestamp") or r.get("created_at")

            # si la table contient déjà 'severity' on garde / normalise sinon on génère
            if "severity" in r and r.get("severity"):
                # normaliser valeurs existantes vers les trois catégories
                sev = str(r.get("severity")).upper()
                if sev in ("CRITIQUE", "CRITICAL", "HIGH", "HAUT"):
                    r["severity"] = "Critique"
                elif sev in ("WARNING", "MAJOR"):
                    r["severity"] = "Haute"
                elif sev in ("MIDDLE", "MOYENNE", "MIDDLE"):
                    r["severity"] = "Moyenne"
                else:
                    r["severity"] = "Faible"
            else:
                if auto_severity:
                    infer = _infer_severity(r.get("event_type"), r.get("description"))
                    r["severity"] = infer
                else:
                    r["severity"] = "Faible"

            normalized.append(r)

        return normalized

    def count_by_month(self, year: int) -> List[Dict]:
        """
        Return counts per month for given year:
        [{month:1, count: 12}, ...]
        """
        return self.db.fetch_query(
            """
            SELECT MONTH(timestamp) AS month, COUNT(*) AS count
            FROM historique
            WHERE YEAR(timestamp) = %s
            GROUP BY MONTH(timestamp)
            ORDER BY month;
            """, 
            (year,)
        )
