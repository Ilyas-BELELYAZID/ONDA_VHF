import datetime
from models.user_model import UserModel
from services.database_service import DatabaseService

class AuthController:
    """
    AuthController:
      - login(username, password) -> (ok:bool, msg:str, user_row)
      - forgot_start(username, email) -> (ok,msg,user_id)
      - forgot_set_password(user_id, new_password, confirm) -> (ok,msg)
    """

    def __init__(self, db : DatabaseService = None, max_attempts=3):
        self.db = db or DatabaseService()
        self.user_model = UserModel(self.db)
        self.max_attempts = max_attempts
        # stockage des tentatives en mémoire (simple). Tu peux persister si besoin.
        # structure: { user_id_or_username: { "count": int, "last_try": datetime } }
        self._attempts = {}

    def _inc_attempt(self, user_key):
        rec = self._attempts.get(user_key, {"count": 0})
        rec["count"] = rec.get("count", 0) + 1
        rec["last_try"] = datetime.datetime.now()
        self._attempts[user_key] = rec
        return rec["count"]

    def _reset_attempts(self, user_key):
        if user_key in self._attempts:
            del self._attempts[user_key]

    def login(self, username: str, password: str):
        # Step 1: get user
        row = self.user_model.get_by_username(username)
        if not row:
            # To avoid username probing, return generic message
            return False, "Identifiants invalides.", None

        user_key = row["id"]
        if row.get("blocked"):
            return False, "Compte bloqué. Veuillez réinitialiser le mot de passe.", row

        ok, _ = self.user_model.verify_credentials(username, password)
        if ok:
            # successful login -> reset attempts and return user id as session key
            self._reset_attempts(user_key)
            # return user id to be used by other views as 'session id'
            return True, "Connexion réussie.", row
        else:
            # increase attempts
            cnt = self._inc_attempt(user_key)
            remaining = max(0, self.max_attempts - cnt)
            # block if reached
            if cnt >= self.max_attempts:
                self.user_model.set_blocked(row["id"], True)
                return False, "Compte bloqué après 3 tentatives. Veuillez réinitialiser le mot de passe.", row
            else:
                return False, f"Identifiants invalides. Tentatives restantes: {remaining}.", row

    def forgot_start(self, username: str, email: str):
        # verify username/email match
        row = self.user_model.get_by_username(username)
        if not row:
            return False, "Nom d'utilisateur introuvable.", None
        if row.get("email") != email:
            return False, "L'email ne correspond pas.", None
        # allow password reset -> return user id for next step
        return True, "Vérification réussie. Vous pouvez maintenant saisir un nouveau mot de passe.", row["id"]

    def forgot_set_password(self, user_id: int, new_password: str, confirm: str):
        if new_password != confirm:
            return False, "Les mots de passe ne correspondent pas."
        if not self.user_model.valid_password_strength(new_password):
            return False, "Mot de passe trop court (min 8)."
        # update password and clear blocked
        self.user_model.update_password(user_id, new_password)
        self.user_model.set_blocked(user_id, False)
        # clear attempts if any
        try:
            del self._attempts[user_id]
        except KeyError:
            pass
        return True, "Mot de passe réinitialisé avec succès. Vous pouvez vous connecter."
