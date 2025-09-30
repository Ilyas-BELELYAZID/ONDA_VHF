import mysql.connector
from services.database_service import DatabaseService
from datetime import datetime


class AlerteModel:
    def __init__(self, db: DatabaseService = None):
        self.db = db or DatabaseService()

    def save(self, equipment_type, equipment_id, type, severity, timestamp, resolved=False):
        query = """
        INSERT INTO alertes (equipment_type, equipment_id, type, severity, timestamp, resolved)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (equipment_type, equipment_id, type, severity, timestamp, resolved)
        self.db.execute_query(query, params)

    def get(self, equipment_type=None, equipment_id=None, type=None, severity=None, limit=20):
        query = "SELECT * FROM alertes WHERE 1=1"
        params = []
        if equipment_type:
            query += " AND equipment_type=%s"
            params.append(equipment_type)
        if equipment_id:
            query += " AND equipment_id=%s"
            params.append(equipment_id)
        if type:
            query += " AND type=%s"
            params.append(type)
        if severity:
            query += " AND severity=%s"
            params.append(severity)
        query += " ORDER BY created_at DESC LIMIT %s"
        params.append(limit)
        return self.db.fetch_query(query, tuple(params))
