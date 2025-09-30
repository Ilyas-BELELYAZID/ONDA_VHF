import mysql.connector
from mysql.connector import Error

class DatabaseService:
    def __init__(self, host="localhost", user="supervision_user", password="Onda@123", database="supervision_vhf"):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                autocommit = True
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("✅ Connexion MySQL établie.")
        except Error as e:
            print(f"❌ Erreur MySQL: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
            return True
        except Error as e:
            print(f"❌ Erreur SQL: {e}")
            return False

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def close(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("🔒 Connexion MySQL fermée.")
