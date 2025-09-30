from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6.QtGui import QIcon
from views.packages.ui_packages import Ui_MainWindow

class Packages_Screen(QMainWindow):
    def __init__(self, user_id: int = None):
        super().__init__()

        self.user_id = user_id

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Définit l'icône spécifique de la fenêtre (affichée dans la barre de titre)
        self.setWindowIcon(QIcon(":/images/logo_onda.ico"))

        if not self.user_id == None:
            #loading
            self.show_view_packages()

            #button
            self.connect_signals()
        else:
            # Clear the current contents of the frame
            frame_layout5 = self.ui.frame_7.layout()
            if frame_layout5:
                while frame_layout5.count() > 0:
                    widget = frame_layout5.takeAt(0).widget()
                    if widget:
                        widget.deleteLater()

            # Create layout for frame_7 if it doesn't exist
            frame_layout5 = self.ui.frame_7.layout()
            if frame_layout5 is None:
                frame_layout5 = QtWidgets.QVBoxLayout()
                self.ui.frame_7.setLayout(frame_layout5)

            # Instantiate and add the Historique widget to the frame
            from views.erreur.erreur import Erreur_Screen
            self.view_erreur = Erreur_Screen()
            frame_layout5.addWidget(self.view_erreur)

        

    def connect_signals(self):
        self.ui.dashboardButton.clicked.connect(self.show_view_packages)
        self.ui.emetteurButton.clicked.connect(self.show_emetteur)
        self.ui.receiverButton.clicked.connect(self.show_receiver)
        self.ui.switchButton.clicked.connect(self.show_switch)
        self.ui.historyButton.clicked.connect(self.show_history)
        self.ui.logoutButton.clicked.connect(self.show_logout)

    def update_navigation_styles(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.dashboardButton, self.ui.emetteurButton, self.ui.receiverButton, self.ui.switchButton, self.ui.historyButton]

        for button in buttons:
            if button == selected_button:
                button.setCheckable(True)
                button.setChecked(True)
            else:
                button.setChecked(False)
        
    def show_view_packages(self):
        self.ui.package_screens.setCurrentWidget(self.ui.dashboard)
        self.update_navigation_styles(self.ui.dashboardButton)

        # Clear the current contents of the frame
        frame_layout = self.ui.frame_2.layout()
        if frame_layout:
            while frame_layout.count() > 0:
                widget = frame_layout.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_2 if it doesn't exist
        frame_layout = self.ui.frame_2.layout()
        if frame_layout is None:
            frame_layout = QtWidgets.QVBoxLayout()
            self.ui.frame_2.setLayout(frame_layout)

        # Instantiate and add the Dashboard widget to the frame
        from views.dashboard.dashboard import Dashboard_Screen
        self.view_pack = Dashboard_Screen(self.user_id)
        frame_layout.addWidget(self.view_pack)

    def show_emetteur(self):
        self.ui.package_screens.setCurrentWidget(self.ui.emetteur)
        self.update_navigation_styles(self.ui.emetteurButton)

        # Clear the current contents of the frame
        frame_layout1 = self.ui.frame_3.layout()
        if frame_layout1:
            while frame_layout1.count() > 0:
                widget = frame_layout1.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_3 if it doesn't exist
        frame_layout1 = self.ui.frame_3.layout()
        if frame_layout1 is None:
            frame_layout1 = QtWidgets.QVBoxLayout()
            self.ui.frame_3.setLayout(frame_layout1)

        # Instantiate and add the Emetteur widget to the frame
        from views.emetteur.emetteur import Emetteur_Screen
        self.view_emetteur = Emetteur_Screen(self.user_id)
        frame_layout1.addWidget(self.view_emetteur)

    def show_receiver(self):
        self.ui.package_screens.setCurrentWidget(self.ui.recepteur)
        self.update_navigation_styles(self.ui.receiverButton)

        # Clear the current contents of the frame
        frame_layout2 = self.ui.frame_4.layout()
        if frame_layout2:
            while frame_layout2.count() > 0:
                widget = frame_layout2.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_4 if it doesn't exist
        frame_layout2 = self.ui.frame_4.layout()
        if frame_layout2 is None:
            frame_layout2 = QtWidgets.QVBoxLayout()
            self.ui.frame_4.setLayout(frame_layout2)

        # Instantiate and add the Receiver widget to the frame
        from views.recepteur.recepteur import Recepteur_Screen
        self.view_recepteur = Recepteur_Screen(self.user_id)
        frame_layout2.addWidget(self.view_recepteur)

    def show_switch(self):
        self.ui.package_screens.setCurrentWidget(self.ui.basculeur)
        self.update_navigation_styles(self.ui.switchButton)

        # Clear the current contents of the frame
        frame_layout3 = self.ui.frame_5.layout()
        if frame_layout3:
            while frame_layout3.count() > 0:
                widget = frame_layout3.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_5 if it doesn't exist
        frame_layout3 = self.ui.frame_5.layout()
        if frame_layout3 is None:
            frame_layout3 = QtWidgets.QVBoxLayout()
            self.ui.frame_5.setLayout(frame_layout3)

        # Instantiate and add the Switch widget to the frame
        from views.basculeur.basculeur import Basculeur_Screen
        self.view_basculeur = Basculeur_Screen(self.user_id)
        frame_layout3.addWidget(self.view_basculeur)

    def show_history(self):
        self.ui.package_screens.setCurrentWidget(self.ui.historique)
        self.update_navigation_styles(self.ui.historyButton)

        # Clear the current contents of the frame
        frame_layout4 = self.ui.frame_6.layout()
        if frame_layout4:
            while frame_layout4.count() > 0:
                widget = frame_layout4.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_6 if it doesn't exist
        frame_layout4 = self.ui.frame_6.layout()
        if frame_layout4 is None:
            frame_layout4 = QtWidgets.QVBoxLayout()
            self.ui.frame_6.setLayout(frame_layout4)

        # Instantiate and add the Historique widget to the frame
        from views.historique.historique import historique_Screen
        self.view_historique = historique_Screen(self.user_id)
        frame_layout4.addWidget(self.view_historique)

    def show_logout(self):
        # Close the current window
        self.close()
