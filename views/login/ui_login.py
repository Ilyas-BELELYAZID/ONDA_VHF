# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginhxdCTa.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.setFixedSize(700, 625)
        MainWindow.setStyleSheet(u"/* --- Style Global --- */\n"
"QMainWindow {\n"
"	background-color: #f3f4f6; /* Arri\u00e8re-plan gris clair */\n"
"	font-family: Inter, sans-serif;\n"
"}\n"
"\n"
"/* --- Style du formulaire de connexion --- */\n"
"QFrame#loginFrame {\n"
"	background-color: white;\n"
"	border: 1px solid #e5e7eb;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"/* --- Style des labels --- */\n"
"QLabel#label_username, QLabel#label_password {\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	color: #1f2937;\n"
"}\n"
"\n"
"/* --- Style des champs de saisie --- */\n"
"QLineEdit {\n"
"	padding: 12px;\n"
"	border: 1px solid #d1d5db;\n"
"	border-radius: 8px;\n"
"	font-size: 14px;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #2563eb; /* Bordure bleue lors de la s\u00e9lection */\n"
"}\n"
"\n"
"/* --- Style du bouton de connexion --- */\n"
"QPushButton#loginButton {\n"
"	background-color: #2563eb; /* Bleu */\n"
"	color: white;\n"
"	padding: 12px;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-"
                        "size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#loginButton:hover {\n"
"	background-color: #1d4ed8; /* Bleu plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* --- Style du Button 'Mot de passe oubli\u00e9' --- */\n"
"QPushButton#forgotButton {\n"
"	font-size: 13px;\n"
"	color: #6b7281; /* Gris */\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#forgotButton:hover {\n"
"	color: #1d4ed8; /* Bleu au survol */\n"
"}\n"
"\n"
"/* --- Style du logo texte 'ONDA' --- */\n"
"QLabel#logoText {\n"
"	font-size: 28px;\n"
"	font-weight: 800; /* Extra bold */\n"
"	color: #1e3a8a; /* Bleu fonc\u00e9 */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setVisible(False)
        self.frame.setMaximumWidth(550)
        self.frame.setStyleSheet(u"width: 1120px; \n"
"height: 74px; \n"
"background-color: #991B1B;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFixedSize(24, 24)
        self.label_2.setPixmap(QPixmap(u":/icons/icons/exclamation-circle.svg"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 16px; \n"
"font-weight: 500; \n"
"color: #FFFFFF;")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignCenter)

        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.horizontalLayout = QHBoxLayout(self.mainContent)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.loginFrame = QFrame(self.mainContent)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setMinimumSize(QSize(400, 0))
        self.loginFrame.setMaximumSize(QSize(400, 16777215))
        self.loginFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.loginFrame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.logoLayout = QHBoxLayout()
        self.logoLayout.setSpacing(12)
        self.logoLayout.setObjectName(u"logoLayout")
        self.logoLayout.setContentsMargins(-1, 0, -1, 20)
        self.logoHorizontalSpacer_Left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logoLayout.addItem(self.logoHorizontalSpacer_Left)

        self.logoImage = QLabel(self.loginFrame)
        self.logoImage.setObjectName(u"logoImage")
        pixmap = QPixmap("assets/logo_onda.png")
        pixmap = pixmap.scaled(120, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logoImage.setPixmap(pixmap)
        self.logoImage.setStyleSheet(u"background-color: #DBEAFE; /* Placeholder color */\n"
"border: 1px solid #1E3A8A;\n"
"border-radius: 8px;")
        self.logoImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.logoLayout.addWidget(self.logoImage)

        self.logoText = QLabel(self.loginFrame)
        self.logoText.setObjectName(u"logoText")

        self.logoLayout.addWidget(self.logoText)

        self.logoHorizontalSpacer_Right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logoLayout.addItem(self.logoHorizontalSpacer_Right)


        self.verticalLayout.addLayout(self.logoLayout)

        self.label_username = QLabel(self.loginFrame)
        self.label_username.setObjectName(u"label_username")

        self.verticalLayout.addWidget(self.label_username)

        self.usernameLineEdit = QLineEdit(self.loginFrame)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.label_password = QLabel(self.loginFrame)
        self.label_password.setObjectName(u"label_password")

        self.verticalLayout.addWidget(self.label_password)

        self.passwordLineEdit = QLineEdit(self.loginFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passwordLineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.loginButton = QPushButton(self.loginFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 45))
        self.loginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.loginButton)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.forgotButton = QPushButton(self.loginFrame)
        self.forgotButton.setObjectName(u"forgotButton")
        self.forgotButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.forgotButton)


        self.verticalLayout_2.addWidget(self.loginFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA | Connexion \u00e0 la supervision VHF", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.logoImage.setText("")
        self.logoText.setText(QCoreApplication.translate("MainWindow", u"ONDA", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre nom d'utilisateur", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre mot de passe", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.forgotButton.setText(QCoreApplication.translate("MainWindow", u"Mot de passe oubli\u00e9 ?", None))
    # retranslateUi

