import re
import datetime
from services.database_service import DatabaseService
from services.security_service import SecurityService

class UserModel:
    EMAIL_RE = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __init__(self, db : DatabaseService = None):
        self.db = db or DatabaseService()


    # --------- UTIL helpers ----------
    @staticmethod
    def valid_email(email: str) -> bool:
        return bool(UserModel.EMAIL_RE.match(email or ""))

    @staticmethod
    def valid_password_strength(pw: str) -> bool:
        return len(pw or "") >= 8

    # --------- DB operations ----------
    def create_user(self, username: str, email: str, password: str) -> int:
        if not self.valid_email(email):
            raise ValueError("Email invalide")
        if not self.valid_password_strength(password):
            raise ValueError("Mot de passe trop court (min 8)")
        if self.get_by_username(username):
            raise ValueError("Le nom d'utilisateur déjà existe!")
        pw_hash = SecurityService.hash_password(password)
        sql = "INSERT INTO users (username,email,password_hash,blocked,created_at) VALUES (%s,%s,%s,%s,%s)"
        now = datetime.datetime.now()
        return self.db.execute_query(sql, (username, email, pw_hash, False, now))

    def get_by_username(self, username: str):
        return self.db.fetch_one("SELECT * FROM users WHERE username=%s", (username,))

    def get_by_email(self, email: str):
        return self.db.fetch_one("SELECT * FROM users WHERE email=%s", (email,))

    def get_by_id(self, user_id: int):
        return self.db.fetch_one("SELECT * FROM users WHERE id=%s", (user_id,))

    def set_blocked(self, user_id: int, blocked: bool = True):
        return self.db.execute_query("UPDATE users SET blocked=%s WHERE id=%s", (1 if blocked else 0, user_id))

    def update_password(self, user_id: int, new_password: str):
        if not self.valid_password_strength(new_password):
            raise ValueError("Mot de passe trop court (min 8)")
        hashed = SecurityService.hash_password(new_password)
        return self.db.execute_query("UPDATE users SET password_hash=%s WHERE id=%s", (hashed, user_id))

    # For login flow: verify credentials and optionally return user row
    def verify_credentials(self, username: str, password: str):
        row = self.get_by_username(username)
        if not row:
            return False, None
        if row.get("blocked"):
            return False, row  # blocked account
        ok = SecurityService.verify_password(password, row["password_hash"])
        return (ok, row) if ok else (False, row)
