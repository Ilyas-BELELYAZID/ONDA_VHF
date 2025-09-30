# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgot_passwordebsnry.ui'
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
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(700, 625)
        MainWindow.setStyleSheet(u"/* --- Global Style --- */\n"
"QMainWindow {\n"
"	background-color: #f3f4f6; /* Light gray background */\n"
"	font-family: Inter, sans-serif;\n"
"}\n"
"\n"
"/* --- Main Frame Style --- */\n"
"QFrame#resetFrame {\n"
"	background-color: white;\n"
"	border: 1px solid #e5e7eb;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"/* --- Title and Labels Style --- */\n"
"QLabel#titleLabel {\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #1f2937;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	color: #1f2937;\n"
"}\n"
"\n"
"/* --- Input Field Style --- */\n"
"QLineEdit {\n"
"	padding: 12px;\n"
"	border: 1px solid #d1d5db;\n"
"	border-radius: 8px;\n"
"	font-size: 14px;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #2563eb; /* Blue border on focus */\n"
"}\n"
"\n"
"/* --- Button Style --- */\n"
"QPushButton {\n"
"	background-color: #2563eb; /* Blue */\n"
"	color: white;\n"
"	padding: 12px;\n"
"	borde"
                        "r: none;\n"
"	border-radius: 8px;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1d4ed8; /* Darker blue on hover */\n"
"}\n"
"\n"
"/* --- 'Back to Login' Button Style --- */\n"
"QPushButton#backToLoginButton {\n"
"	border: none;\n"
"	font-size: 13px;\n"
"	background-color: #FFFFFF;\n"
"	color: #6b7281; /* Gray */\n"
"    font-weight: normal; /* Override bold */\n"
"}\n"
"\n"
"QPushButton#backToLoginButton:hover {\n"
"	color: #1d4ed8; /* Blue on hover */\n"
"}\n"
"\n"
"/* --- 'ONDA' Logo Text Style --- */\n"
"QLabel#logoText {\n"
"	font-size: 28px;\n"
"	font-weight: 800; /* Extra bold */\n"
"	color: #1e3a8a; /* Dark blue */\n"
"}\n"
"\n"
"/* Make the stacked widget background transparent */\n"
"QStackedWidget, QStackedWidget > QWidget {\n"
"    background-color: transparent;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)



        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setVisible(False)
        self.frame.setMaximumWidth(580)
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


        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignCenter)

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

        self.resetFrame = QFrame(self.mainContent)
        self.resetFrame.setObjectName(u"resetFrame")
        self.resetFrame.setMinimumSize(QSize(400, 0))
        self.resetFrame.setMaximumSize(QSize(400, 16777215))
        self.resetFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.resetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.resetFrame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.logoLayout = QHBoxLayout()
        self.logoLayout.setSpacing(12)
        self.logoLayout.setObjectName(u"logoLayout")
        self.logoLayout.setContentsMargins(-1, 0, -1, 10)
        self.logoHorizontalSpacer_Left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logoLayout.addItem(self.logoHorizontalSpacer_Left)

        self.logoImage = QLabel(self.resetFrame)
        self.logoImage.setObjectName(u"logoImage")
        pixmap = QPixmap("assets/logo_onda.png")
        pixmap = pixmap.scaled(120, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logoImage.setPixmap(pixmap)
        self.logoImage.setStyleSheet(u"background-color: #DBEAFE; /* Placeholder color */\n"
"border: 1px solid #1E3A8A;\n"
"border-radius: 8px;")
        self.logoImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.logoLayout.addWidget(self.logoImage)

        self.logoText = QLabel(self.resetFrame)
        self.logoText.setObjectName(u"logoText")

        self.logoLayout.addWidget(self.logoText)

        self.logoHorizontalSpacer_Right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logoLayout.addItem(self.logoHorizontalSpacer_Right)


        self.verticalLayout.addLayout(self.logoLayout)

        self.titleLabel = QLabel(self.resetFrame)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.stackedWidget = QStackedWidget(self.resetFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_verification = QWidget()
        self.page_verification.setObjectName(u"page_verification")
        self.verticalLayout_3 = QVBoxLayout(self.page_verification)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_username = QLabel(self.page_verification)
        self.label_username.setObjectName(u"label_username")

        self.verticalLayout_3.addWidget(self.label_username)

        self.usernameLineEdit = QLineEdit(self.page_verification)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout_3.addWidget(self.usernameLineEdit)

        self.label_email = QLabel(self.page_verification)
        self.label_email.setObjectName(u"label_email")

        self.verticalLayout_3.addWidget(self.label_email)

        self.emailLineEdit = QLineEdit(self.page_verification)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.verticalLayout_3.addWidget(self.emailLineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verifyButton = QPushButton(self.page_verification)
        self.verifyButton.setObjectName(u"verifyButton")
        self.verifyButton.setMinimumSize(QSize(0, 45))
        self.verifyButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.verifyButton)

        self.stackedWidget.addWidget(self.page_verification)
        self.page_new_password = QWidget()
        self.page_new_password.setObjectName(u"page_new_password")
        self.verticalLayout_4 = QVBoxLayout(self.page_new_password)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_new_password = QLabel(self.page_new_password)
        self.label_new_password.setObjectName(u"label_new_password")

        self.verticalLayout_4.addWidget(self.label_new_password)

        self.newPasswordLineEdit = QLineEdit(self.page_new_password)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.newPasswordLineEdit)

        self.label_confirm_password = QLabel(self.page_new_password)
        self.label_confirm_password.setObjectName(u"label_confirm_password")

        self.verticalLayout_4.addWidget(self.label_confirm_password)

        self.confirmPasswordLineEdit = QLineEdit(self.page_new_password)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.confirmPasswordLineEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.resetButton = QPushButton(self.page_new_password)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(0, 45))
        self.resetButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.resetButton)

        self.stackedWidget.addWidget(self.page_new_password)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.backToLoginButton = QPushButton(self.resetFrame)
        self.backToLoginButton.setObjectName(u"backToLoginButton")
        self.backToLoginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.backToLoginButton)


        self.verticalLayout_2.addWidget(self.resetFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA | R\u00e9initialisation du mot de passe", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.logoImage.setText("")
        self.logoText.setText(QCoreApplication.translate("MainWindow", u"ONDA", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"R\u00e9initialiser le mot de passe", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre nom d'utilisateur", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Adresse e-mail", None))
        self.emailLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre adresse e-mail", None))
        self.verifyButton.setText(QCoreApplication.translate("MainWindow", u"Consulter", None))
        self.label_new_password.setText(QCoreApplication.translate("MainWindow", u"Nouveau mot de passe", None))
        self.newPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez le nouveau mot de passe", None))
        self.label_confirm_password.setText(QCoreApplication.translate("MainWindow", u"Confirmer le mot de passe", None))
        self.confirmPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmez le nouveau mot de passe", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"R\u00e9initialiser le mot de passe", None))
        self.backToLoginButton.setText(QCoreApplication.translate("MainWindow", u"Retour \u00e0 la connexion", None))
    # retranslateUi

