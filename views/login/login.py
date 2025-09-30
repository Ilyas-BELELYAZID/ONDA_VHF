from PySide6.QtCore import QCoreApplication, QTimer
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow
from views.login.ui_login import Ui_MainWindow
from controllers.auth_controller import AuthController

class Login_Screen(QMainWindow):
    def __init__(self, duration: int = 2500):
        super().__init__()

        # Create an instance of the controller
        self.controller = AuthController()

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Définit l'icône spécifique de la fenêtre (affichée dans la barre de titre)
        self.setWindowIcon(QIcon(":/images/logo_onda.ico"))

        # Connect button click event
        self.ui.loginButton.clicked.connect(self.on_login_clicked)
        self.ui.forgotButton.clicked.connect(self.on_forgot_pass_clicked)

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
        
        # self.ui.verticalLayout_3.addItem(self.ui.verticalSpacer_5)
        
        self.ui.verticalLayout_3.setContentsMargins(0, 30, 0, 70)
        self.ui.frame.setVisible(True)
        QTimer.singleShot(self.duration, self.clear_alert)

    def clear_alert(self):
        self.ui.frame.setVisible(False)
        
        # self.ui.verticalLayout_3.removeItem(self.ui.verticalSpacer_5)
        
        self.ui.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ui.label.setText("")

    def on_login_clicked(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        if not username or not password:
            self.show_alert("Veuillez saisir nom d'utilisateur et mot de passe.", "warn")
            return
        ok, msg, user_row = self.controller.login(username, password)
        if ok:
            print("Credentials are valid")

            self.clear_alert()
            # emit login success with user id and username (use id for session)
            from views.packages.packages import Packages_Screen
            self.pack_screen = Packages_Screen(user_row)
            self.pack_screen.show()
            self.close()
        else:
            # show inline alert
            self.show_alert(msg, "error")

    def on_forgot_pass_clicked(self):
        from views.login.forgot_password import Password_Reset_Screen
        self.Next_Screen = Password_Reset_Screen()
        self.Next_Screen.show()
        self.close()
