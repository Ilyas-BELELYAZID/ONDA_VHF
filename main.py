import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QIcon
from views.splash.splash import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Définit l'icône globale de l'application (utile pour la barre des tâches)
    app.setWindowIcon(QIcon(":/images/logo_onda.ico"))  
    window = MainWindow()
    window.show()
    sys.exit(app.exec())