from PySide6.QtWidgets import QMainWindow
from views.erreur.ui_erreur import Ui_MainWindow

class Erreur_Screen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
