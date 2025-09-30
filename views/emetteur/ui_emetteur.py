# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emetteur_vhfemSnEr.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"/* --- Contenu Principal --- */\n"
"#mainContent {\n"
"	background-color: #FFFFFF;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"#titleLabel {\n"
"	font-family: Source Sans Pro; \n"
"	font-size: 30px;\n"
"	font-weight: 700;\n"
"	color: #171A1F;\n"
"}\n"
"\n"
"/* --- Cartes --- */\n"
".QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 24px;\n"
"	border: 1px solid #E5E7EB;\n"
"}\n"
"\n"
".cardTitleLabel {\n"
"	font-family: Source Sans Pro;\n"
"	font-size: 20px;\n"
"	font-weight: 700;\n"
"	color: #171A1F;\n"
"	padding-bottom: 10px;\n"
"}\n"
"\n"
".dataLabel {\n"
"	font-size: 14px;\n"
"	width: 114px;\n"
"	font-family: Source Sans Pro;\n"
"	color: #565D6D;\n"
"	font-weight: 400; \n"
"}\n"
"\n"
".dataValue {\n"
"	font-family: Source Sans Pro; \n"
"	font-size: 18px; \n"
"	line-height: 28px; \n"
"	font-weight: 600; \n"
"	color: #171A1F; \n"
"}\n"
"\n"
"/* --- Graphes --- */\n"
"#graphPlaceholder1, #graphPlaceholder2 {\n"
"	border-radius: 8px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.verticalLayout_4 = QVBoxLayout(self.mainContent)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.header = QWidget(self.mainContent)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.titleLabel = QLabel(self.header)
        self.titleLabel.setObjectName(u"titleLabel")

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.headerIcons = QWidget(self.header)
        self.headerIcons.setObjectName(u"headerIcons")
        self.horizontalLayout_3 = QHBoxLayout(self.headerIcons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_2.addWidget(self.headerIcons)


        self.verticalLayout_4.addWidget(self.header)

        self.scrollArea = QScrollArea(self.mainContent)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* Optional: Pour un look plus propre, on enl\u00e8ve la bordure du ScrollArea */\n"
"QScrollArea {\n"
"	background-color: #FFFFFF;\n"
"	border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1148, 827))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setVisible(False)
        self.frame_5.setFixedHeight(40)
        self.frame_5.setStyleSheet(u"\n"
"                        QFrame {\n"
"                            background-color: #f0ad4e;\n"
"                            border: 1px solid #f0ad4e;\n"
"                            border-radius: 8px;\n"
"                            color: #856404;\n"
"                        }\n"
"                    ")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(24, 24))
        self.label_16.setMaximumSize(QSize(24, 24))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/alert-triangle.svg"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_16)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"font-size: 14px;\n"
"font-weight: 600;")
        self.label_15.setIndent(10)

        self.horizontalLayout_4.addWidget(self.label_15)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.cardsContainer = QWidget(self.scrollAreaWidgetContents_2)
        self.cardsContainer.setObjectName(u"cardsContainer")
        self.gridLayout = QGridLayout(self.cardsContainer)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.cardsContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 20, 30, 20)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 4, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 6, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 7, 0, 1, 1)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 5, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout_5.addWidget(self.widget)

        self.verticalLayout_5.setStretch(2, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.cardsContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 30, 30, 30)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_12)

        self.actionsContainer = QWidget(self.frame_2)
        self.actionsContainer.setObjectName(u"actionsContainer")
        self.actionsContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.actionsContainer)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_4 = QPushButton(self.actionsContainer)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 45))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"/* --- Boutons d'Action --- */\n"
"/* Button */\n"
"#actionsContainer QPushButton {\n"
"  width: 250.671875px; \n"
"  height: 48px; \n"
"  padding: 0 12px; \n"
"  font-family: Source Sans Pro; \n"
"  font-size: 14px; \n"
"  font-weight: 500; \n"
"  color: #FFFFFF; \n"
"  background: #3B5EB0; \n"
"  opacity: 1; \n"
"  border: none; \n"
"  border-radius: 16px; \n"
"}\n"
"/* Hover */\n"
"#actionsContainer QPushButton:hover {\n"
"  background: #284079; \n"
"}\n"
"/* Pressed */\n"
"#actionsContainer QPushButton:hover:active {\n"
"  background: #1A2A4F; \n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.actionsContainer)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 45))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"/* --- Boutons d'Action --- */\n"
"/* Button */\n"
"#actionsContainer QPushButton {\n"
"  width: 250.671875px; \n"
"  height: 48px; \n"
"  padding: 0 12px; \n"
"  font-family: Source Sans Pro; \n"
"  font-size: 14px; \n"
"  font-weight: 500; \n"
"  color: #FFFFFF; \n"
"  background: #3B5EB0; \n"
"  opacity: 1; \n"
"  border: none; \n"
"  border-radius: 16px; \n"
"}\n"
"/* Hover */\n"
"#actionsContainer QPushButton:hover {\n"
"  background: #284079; \n"
"}\n"
"/* Pressed */\n"
"#actionsContainer QPushButton:hover:active {\n"
"  background: #1A2A4F; \n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.pushButton = QPushButton(self.actionsContainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"/* --- Boutons d'Action --- */\n"
"/* Button */\n"
"#actionsContainer QPushButton {\n"
"  width: 250.671875px; \n"
"  height: 48px; \n"
"  padding: 0 12px; \n"
"  font-family: Source Sans Pro; \n"
"  font-size: 14px; \n"
"  font-weight: 500; \n"
"  color: #FFFFFF; \n"
"  background: #3B5EB0; \n"
"  opacity: 1; \n"
"  border: none; \n"
"  border-radius: 16px; \n"
"}\n"
"/* Hover */\n"
"#actionsContainer QPushButton:hover {\n"
"  background: #284079; \n"
"}\n"
"/* Pressed */\n"
"#actionsContainer QPushButton:hover:active {\n"
"  background: #1A2A4F; \n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.actionsContainer)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 45))
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"/* --- Boutons d'Action --- */\n"
"/* Button */\n"
"#actionsContainer QPushButton {\n"
"  width: 250.671875px; \n"
"  height: 48px; \n"
"  padding: 0 12px; \n"
"  font-family: Source Sans Pro; \n"
"  font-size: 14px; \n"
"  font-weight: 500; \n"
"  color: #FFFFFF; \n"
"  background: #3B5EB0; \n"
"  opacity: 1; \n"
"  border: none; \n"
"  border-radius: 16px; \n"
"}\n"
"/* Hover */\n"
"#actionsContainer QPushButton:hover {\n"
"  background: #284079; \n"
"}\n"
"/* Pressed */\n"
"#actionsContainer QPushButton:hover:active {\n"
"  background: #1A2A4F; \n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.actionsContainer)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.cardsContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 400))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 5, 5, 5)
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_13)

        self.graphPlaceholder1 = QWidget(self.frame_3)
        self.graphPlaceholder1.setObjectName(u"graphPlaceholder1")
        self.verticalLayout = QVBoxLayout(self.graphPlaceholder1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.graphPlaceholder1)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.cardsContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 400))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(8, 5, 5, 5)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.label_14)

        self.graphPlaceholder2 = QWidget(self.frame_4)
        self.graphPlaceholder2.setObjectName(u"graphPlaceholder2")
        self.verticalLayout_2 = QVBoxLayout(self.graphPlaceholder2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.graphPlaceholder2)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_3.addWidget(self.cardsContainer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.mainContent)

        self.horizontalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA - Emetteur", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u00c9metteur VHF", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Informations Techniques", None))
        self.label.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Temp\u00e9rature interne", None))
        self.label_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Taux de modulation", None))
        self.label_7.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"95.2 %", None))
        self.label_9.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fr\u00e9quence configur\u00e9e", None))
        self.label_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"ROS", None))
        self.label_19.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"24.1 V", None))
        self.label_11.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"118.7 MHz", None))
        self.label_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u00c9tat", None))
        self.label_17.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"26.9 W", None))
        self.label_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Puissance d'\u00e9mission", None))
        self.label_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tension d'alimentation", None))
        self.label_10.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"39.9 \u00b0C", None))
        self.label_8.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"ACTIF", None))
        self.label_18.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_20.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.label_12.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Modifier fr\u00e9quence", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"R\u00e9gler puissance", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Modifier TDM", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Activer/d\u00e9sactiver", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Puissance d'\u00c9mission (W)", None))
        self.label_13.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Temp\u00e9rature Interne (\u00b0C)", None))
        self.label_14.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
    # retranslateUi

