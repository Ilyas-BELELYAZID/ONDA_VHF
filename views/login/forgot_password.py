from PySide6.QtCore import QCoreApplication, QTimer
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow
from views.login.ui_forgot_password import Ui_MainWindow
from controllers.auth_controller import AuthController

class Password_Reset_Screen(QMainWindow):
    def __init__(self, duration: int = 2500):
        super().__init__()

        # Create an instance of the controller
        self.controller = AuthController()

        self.user_id = None

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Définit l'icône spécifique de la fenêtre (affichée dans la barre de titre)
        self.setWindowIcon(QIcon(":/images/logo_onda.ico"))

        # --- Configuration initiale ---
        # On s'assure que la fenêtre démarre TOUJOURS sur la première page (index 0)
        # C'est la ligne la plus importante pour "verrouiller" le basculement.
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.newPasswordLineEdit.setEnabled(False)
        self.ui.confirmPasswordLineEdit.setEnabled(False)
        self.ui.resetButton.setEnabled(False)

        # Connect button click event
        self.ui.verifyButton.clicked.connect(self.on_verify)
        self.ui.backToLoginButton.clicked.connect(self.on_back_login_clicked)

        self.duration = duration

    def show_alert(self, text: str, level="error"):
        # Levels: error (red), warn (orange), info (blue)
        if level == "error":
            bg = "#d9534f"
            fg = "#FFFFFF"
            self.ui.label_2.setPixmap(QPixmap(u":/icons/icons/exclamation-circle.svg"))
        elif level == "warn":
            bg = "#f0ad4e"
            fg = "#FFFFFF"
            self.ui.label_2.setPixmap(QPixmap(u":/icons/icons/alert-triangle.svg"))
        else:
            bg = "#5bc0de"
            fg = "#FFFFFF"
            self.ui.label_2.setPixmap(QPixmap(u":/icons/icons/circle-check.svg"))
            
        self.ui.frame.setStyleSheet(f"width: 1120px; height: 74px; background-color: {bg}; border-radius: 10px;")
        self.ui.label.setStyleSheet(f"font-size: 16px; font-weight: 500; color: {fg};")

        self.ui.label.setText(QCoreApplication.translate("MainWindow", text, None))
        
        # self.ui.verticalLayout_5.addItem(self.ui.verticalSpacer_6)
        
        self.ui.verticalLayout_5.setContentsMargins(0, 10, 0, 40)
        self.ui.frame.setVisible(True)
        QTimer.singleShot(self.duration, self.clear_alert)

    def clear_alert(self):
        self.ui.frame.setVisible(False)
        
        # self.ui.verticalLayout_5.removeItem(self.ui.verticalSpacer_6)
        
        self.ui.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ui.label.setText("")

    def on_verify(self):
        username = self.ui.usernameLineEdit.text().strip()
        email = self.ui.emailLineEdit.text().strip()
        if not username or not email:
            self.show_alert("Veuillez remplir nom d'utilisateur et email.", "warn")
            return
        ok, msg, user_id = self.controller.forgot_start(username, email)
        if ok:
            self.clear_alert()
            self.user_id = user_id

            # hide verification inputs to avoid re-check
            self.ui.usernameLineEdit.setEnabled(False)
            self.ui.emailLineEdit.setEnabled(False)
            self.ui.verifyButton.setEnabled(False)

            # C'EST LA SEULE LIGNE QUI AUTORISE LE BASCULEMENT VERS LA PAGE 2 (index 1)
            self.ui.stackedWidget.setCurrentIndex(1)

            # show password fields
            self.ui.newPasswordLineEdit.setEnabled(True)
            self.ui.confirmPasswordLineEdit.setEnabled(True)
            self.ui.resetButton.setEnabled(True)

            self.ui.resetButton.clicked.connect(self.on_set_password)

        else:
            self.show_alert(msg, "error")

    def on_set_password(self):
        if not self.user_id:
            self.show_alert("Aucune opération de verification active.", "warn")
            return
        new_pw = self.ui.newPasswordLineEdit.text().strip()
        confirm = self.ui.confirmPasswordLineEdit.text().strip()
        ok, msg = self.controller.forgot_set_password(self.user_id, new_pw, confirm)
        if ok:
            self.clear_alert()
            self.show_alert(msg, "info")

            # emit success to return to login
            self.on_back_login_clicked()
        else:
            self.show_alert(msg, "error")

    def on_back_login_clicked(self):
        from views.login.login import Login_Screen
        self.Next_Screen = Login_Screen()
        self.Next_Screen.show()
        self.close()
