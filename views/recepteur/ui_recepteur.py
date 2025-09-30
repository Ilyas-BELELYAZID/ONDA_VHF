# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recepteur_vhfdLYiqF.ui'
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
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
"	padding-bottom: 5px;\n"
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
"/* --- Graphes --- */\n"
"#graphPlaceholder1, #graphPlaceholder2 {\n"
"	border-radius: 8px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.verticalLayout_3 = QVBoxLayout(self.mainContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 10, 20, 10)
        self.header = QWidget(self.mainContent)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 67))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.titleLabel = QLabel(self.header)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Source Sans Pro"])
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.header)

        self.scrollArea = QScrollArea(self.mainContent)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* Optional: Pour un look plus propre, on enl\u00e8ve la bordure du ScrollArea */\n"
"QScrollArea {\n"
"	background-color: #FFFFFF;\n"
"	border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1160, 726))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.alertFrame = QFrame(self.scrollAreaWidgetContents)
        self.alertFrame.setObjectName(u"alertFrame")
        self.alertFrame.setVisible(False)
        self.alertFrame.setFixedHeight(40)
        self.alertFrame.setStyleSheet(u"\n"
"                        QFrame {\n"
"                            background-color: #f0ad4e;\n"
"                            border: 1px solid #f0ad4e;\n"
"                            border-radius: 8px;\n"
"                            color: #856404;\n"
"                        }\n"
"                    ")
        self.alertFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.alertFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.alertFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_2 = QLabel(self.alertFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(24, 24))
        self.label_2.setMaximumSize(QSize(24, 24))
        self.label_2.setStyleSheet(u"border: none;")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/alert-triangle.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.alertLabel = QLabel(self.alertFrame)
        self.alertLabel.setObjectName(u"alertLabel")
        self.alertLabel.setMinimumSize(QSize(0, 36))
        self.alertLabel.setMaximumSize(QSize(16777215, 36))
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.alertLabel.setFont(font1)
        self.alertLabel.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"font-size: 14px;\n"
"font-weight: 600;")
        self.alertLabel.setIndent(10)

        self.horizontalLayout_3.addWidget(self.alertLabel)


        self.verticalLayout_8.addWidget(self.alertFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.dataGrid = QWidget(self.scrollAreaWidgetContents)
        self.dataGrid.setObjectName(u"dataGrid")
        self.gridLayout = QGridLayout(self.dataGrid)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, -1, -1, -1)
        self.infoFrame = QFrame(self.dataGrid)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setSizeIncrement(QSize(1, 0))
        self.infoFrame.setStyleSheet(u"")
        self.infoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 13, 20, 20)
        self.infoTitleLabel = QLabel(self.infoFrame)
        self.infoTitleLabel.setObjectName(u"infoTitleLabel")
        self.infoTitleLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.infoTitleLabel)

        self.infoSubtitleLabel = QLabel(self.infoFrame)
        self.infoSubtitleLabel.setObjectName(u"infoSubtitleLabel")
        self.infoSubtitleLabel.setStyleSheet(u"font-family: Roboto; \n"
"color: #565D6D;\n"
"font-weight: 400;  \n"
" ")

        self.verticalLayout_4.addWidget(self.infoSubtitleLabel)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.powerLabel = QLabel(self.infoFrame)
        self.powerLabel.setObjectName(u"powerLabel")

        self.gridLayout_2.addWidget(self.powerLabel, 0, 1, 1, 1)

        self.squelchValueLabel = QLabel(self.infoFrame)
        self.squelchValueLabel.setObjectName(u"squelchValueLabel")
        font2 = QFont()
        font2.setFamilies([u"Source Sans Pro"])
        font2.setWeight(QFont.DemiBold)
        self.squelchValueLabel.setFont(font2)
        self.squelchValueLabel.setStyleSheet(u"font-family: Source Sans Pro; \n"
"font-size: 18px; \n"
"font-weight: 600; \n"
"color: #171A1F; ")

        self.gridLayout_2.addWidget(self.squelchValueLabel, 3, 1, 1, 1)

        self.alimLabel = QLabel(self.infoFrame)
        self.alimLabel.setObjectName(u"alimLabel")

        self.gridLayout_2.addWidget(self.alimLabel, 4, 1, 1, 1)

        self.tmpLabel = QLabel(self.infoFrame)
        self.tmpLabel.setObjectName(u"tmpLabel")

        self.gridLayout_2.addWidget(self.tmpLabel, 4, 0, 1, 1)

        self.freqLabel = QLabel(self.infoFrame)
        self.freqLabel.setObjectName(u"freqLabel")

        self.gridLayout_2.addWidget(self.freqLabel, 0, 0, 1, 1)

        self.powerValueLabel = QLabel(self.infoFrame)
        self.powerValueLabel.setObjectName(u"powerValueLabel")
        self.powerValueLabel.setFont(font2)
        self.powerValueLabel.setStyleSheet(u"font-family: Source Sans Pro; \n"
"font-size: 18px; \n"
"font-weight: 600; \n"
"color: #171A1F; ")

        self.gridLayout_2.addWidget(self.powerValueLabel, 1, 1, 1, 1)

        self.freqValueLabel = QLabel(self.infoFrame)
        self.freqValueLabel.setObjectName(u"freqValueLabel")
        self.freqValueLabel.setFont(font2)
        self.freqValueLabel.setStyleSheet(u"font-family: Source Sans Pro; \n"
"font-size: 18px; \n"
"font-weight: 600; \n"
"color: #171A1F; ")

        self.gridLayout_2.addWidget(self.freqValueLabel, 1, 0, 1, 1)

        self.tmpValueLabel = QLabel(self.infoFrame)
        self.tmpValueLabel.setObjectName(u"tmpValueLabel")
        self.tmpValueLabel.setStyleSheet(u"font-family: Source Sans Pro; \n"
"font-size: 18px; \n"
"font-weight: 600; \n"
"color: #171A1F; ")

        self.gridLayout_2.addWidget(self.tmpValueLabel, 5, 0, 1, 1)

        self.alimValueLabel = QLabel(self.infoFrame)
        self.alimValueLabel.setObjectName(u"alimValueLabel")
        self.alimValueLabel.setStyleSheet(u"font-family: Source Sans Pro; \n"
"font-size: 18px; \n"
"font-weight: 600; \n"
"color: #171A1F; ")

        self.gridLayout_2.addWidget(self.alimValueLabel, 5, 1, 1, 1)

        self.noiseLabel = QLabel(self.infoFrame)
        self.noiseLabel.setObjectName(u"noiseLabel")

        self.gridLayout_2.addWidget(self.noiseLabel, 2, 0, 1, 1)

        self.noiseValueLabel = QLabel(self.infoFrame)
        self.noiseValueLabel.setObjectName(u"noiseValueLabel")
        self.noiseValueLabel.setFont(font2)
        self.noiseValueLabel.setStyleSheet(u"font-family: Source Sans Pro; \n"
"font-size: 18px; \n"
"font-weight: 600; \n"
"color: #171A1F; ")

        self.gridLayout_2.addWidget(self.noiseValueLabel, 3, 0, 1, 1)

        self.squelchLabel = QLabel(self.infoFrame)
        self.squelchLabel.setObjectName(u"squelchLabel")

        self.gridLayout_2.addWidget(self.squelchLabel, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.infoFrame, 0, 0, 1, 1)

        self.snrFrame = QFrame(self.dataGrid)
        self.snrFrame.setObjectName(u"snrFrame")
        self.snrFrame.setMinimumHeight(377)
        self.snrFrame.setStyleSheet(u"")
        self.snrFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.snrFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.snrFrame)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(8, 5, 5, 5)
        self.snrTitleLabel = QLabel(self.snrFrame)
        self.snrTitleLabel.setObjectName(u"snrTitleLabel")
        self.snrTitleLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.snrTitleLabel)

        self.snrSubtitleLabel = QLabel(self.snrFrame)
        self.snrSubtitleLabel.setObjectName(u"snrSubtitleLabel")
        self.snrSubtitleLabel.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.snrSubtitleLabel)

        self.graphPlaceholder1 = QWidget(self.snrFrame)
        self.graphPlaceholder1.setObjectName(u"graphPlaceholder1")
        self.graphPlaceholder1.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.graphPlaceholder1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.graphPlaceholder1)

        self.verticalLayout_5.setStretch(2, 1)

        self.gridLayout.addWidget(self.snrFrame, 0, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.dataGrid)

        self.dataGrid_1 = QWidget(self.scrollAreaWidgetContents)
        self.dataGrid_1.setObjectName(u"dataGrid_1")
        self.gridLayout_3 = QGridLayout(self.dataGrid_1)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(8, -1, -1, -1)
        self.actionsFrame = QFrame(self.dataGrid_1)
        self.actionsFrame.setObjectName(u"actionsFrame")
        self.actionsFrame.setMinimumSize(QSize(0, 0))
        self.actionsFrame.setMaximumSize(QSize(16777215, 16777215))
        self.actionsFrame.setStyleSheet(u"")
        self.actionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.actionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.actionsFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 13, 20, 20)
        self.actionsTitleLabel = QLabel(self.actionsFrame)
        self.actionsTitleLabel.setObjectName(u"actionsTitleLabel")
        self.actionsTitleLabel.setFont(font)
        self.actionsTitleLabel.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.actionsTitleLabel)

        self.actionsSubtitleLabel = QLabel(self.actionsFrame)
        self.actionsSubtitleLabel.setObjectName(u"actionsSubtitleLabel")
        self.actionsSubtitleLabel.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.actionsSubtitleLabel)

        self.changeFreqLabel = QLabel(self.actionsFrame)
        self.changeFreqLabel.setObjectName(u"changeFreqLabel")
        font3 = QFont()
        font3.setBold(True)
        self.changeFreqLabel.setFont(font3)

        self.verticalLayout_6.addWidget(self.changeFreqLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.freqLineEdit = QLineEdit(self.actionsFrame)
        self.freqLineEdit.setObjectName(u"freqLineEdit")
        self.freqLineEdit.setStyleSheet(u"\n"
"#freqLineEdit { \n"
"	padding: 7px; \n"
"	font-family: Roboto; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	background: #DEE1E6; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"	outline: none; \n"
"	border: none;\n"
"}\n"
"\n"
"#freqLineEdit:hover {\n"
"	color: #171A1F; \n"
"	background: #DEE1E6; \n"
"	border-color: #DEE1E6; \n"
"}\n"
"\n"
"#freqLineEdit:focused {\n"
"	color: #171A1F; \n"
"	background: #DEE1E6; \n"
"	border-color: #DEE1E6; \n"
"}")

        self.horizontalLayout_4.addWidget(self.freqLineEdit)

        self.changeFreqButton = QPushButton(self.actionsFrame)
        self.changeFreqButton.setObjectName(u"changeFreqButton")
        self.changeFreqButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.changeFreqButton.setStyleSheet(u"                                        QPushButton {\n"
"                                            background-color: #2577B1;\n"
"                                            color: white;\n"
"                                            border: none;\n"
"                                            padding: 8px 16px;\n"
"                                            border-radius: 6px;\n"
"                                            font-weight: bold;\n"
"  											font-family: Roboto; \n"
"  											font-size: 12px; \n"
"  											width: 115.203125px; \n"
"  											height: 18px; \n"
"											opacity: 1;\n"
"                                        }\n"
"                                        QPushButton:hover {\n"
"											color: #FFFFFF;\n"
"                                            background-color: #194F75;\n"
"                                        }\n"
"										QPushButton:hover:active {\n"
"											color: #FFFFFF;\n"
"                                            background-color"
                        ": #10324B;\n"
"                                        }\n"
"                                    ")

        self.horizontalLayout_4.addWidget(self.changeFreqButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.squelchLevelLabel = QLabel(self.actionsFrame)
        self.squelchLevelLabel.setObjectName(u"squelchLevelLabel")
        self.squelchLevelLabel.setFont(font3)

        self.verticalLayout_6.addWidget(self.squelchLevelLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.squelchLineEdit = QLineEdit(self.actionsFrame)
        self.squelchLineEdit.setObjectName(u"squelchLineEdit")
        self.squelchLineEdit.setStyleSheet(u"#squelchLineEdit {\n"
"	padding: 7px; \n"
"	font-family: Roboto; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	background: #DEE1E6; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"	outline: none; \n"
"	border: none;\n"
"}\n"
"\n"
"#squelchLineEdit:hover {\n"
"	color: #171A1F; \n"
"	background: #DEE1E6; \n"
"	border-color: #DEE1E6; \n"
"}\n"
"\n"
"#squelchLineEdit:focused {\n"
"	color: #171A1F; \n"
"	background: #DEE1E6; \n"
"	border-color: #DEE1E6; \n"
"}")

        self.horizontalLayout_5.addWidget(self.squelchLineEdit)

        self.adjustSquelchButton = QPushButton(self.actionsFrame)
        self.adjustSquelchButton.setObjectName(u"adjustSquelchButton")
        self.adjustSquelchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.adjustSquelchButton.setStyleSheet(u"                                        QPushButton {\n"
"                                            background-color: #2577B1;\n"
"                                            color: white;\n"
"                                            border: none;\n"
"                                            padding: 8px 16px;\n"
"                                            border-radius: 6px;\n"
"                                            font-weight: bold;\n"
"  											font-family: Roboto; \n"
"  											font-size: 12px; \n"
"  											width: 95.203125px; \n"
"  											height: 18px; \n"
"											opacity: 1;\n"
"                                        }\n"
"                                        QPushButton:hover {\n"
"											color: #FFFFFF;\n"
"                                            background-color: #194F75;\n"
"                                        }\n"
"										QPushButton:hover:active {\n"
"											color: #FFFFFF;\n"
"                                            background-color:"
                        " #10324B;\n"
"                                        }\n"
"                                    ")

        self.horizontalLayout_5.addWidget(self.adjustSquelchButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout_3.addWidget(self.actionsFrame, 0, 0, 1, 1)

        self.tmpFrame = QFrame(self.dataGrid_1)
        self.tmpFrame.setObjectName(u"tmpFrame")
        self.tmpFrame.setMinimumHeight(377)
        self.tmpFrame.setMinimumWidth(566)
        self.tmpFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tmpFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.tmpFrame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 5, 5, 5)
        self.tmpTitleLabel = QLabel(self.tmpFrame)
        self.tmpTitleLabel.setObjectName(u"tmpTitleLabel")

        self.verticalLayout_2.addWidget(self.tmpTitleLabel)

        self.tmpSubtitleLabel = QLabel(self.tmpFrame)
        self.tmpSubtitleLabel.setObjectName(u"tmpSubtitleLabel")

        self.verticalLayout_2.addWidget(self.tmpSubtitleLabel)

        self.graphPlaceholder2 = QWidget(self.tmpFrame)
        self.graphPlaceholder2.setObjectName(u"graphPlaceholder2")
        self.verticalLayout_7 = QVBoxLayout(self.graphPlaceholder2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.graphPlaceholder2)

        self.verticalLayout_2.setStretch(2, 1)

        self.gridLayout_3.addWidget(self.tmpFrame, 0, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.dataGrid_1)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R\u00e9cepteur VHF", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"R\u00e9cepteur VHF", None))
        self.label_2.setText("")
        self.alertLabel.setText(QCoreApplication.translate("MainWindow", u"Signal faible d\u00e9tect\u00e9 sur la fr\u00e9quence actuelle.", None))
        self.infoTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Informations Techniques", None))
        self.infoTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.infoSubtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Statut actuel du r\u00e9cepteur VHF", None))
        self.infoSubtitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.powerLabel.setText(QCoreApplication.translate("MainWindow", u"Puissance du signal re\u00e7u", None))
        self.squelchValueLabel.setText(QCoreApplication.translate("MainWindow", u"Ouvert", None))
        self.alimLabel.setText(QCoreApplication.translate("MainWindow", u"Tension d'alimentation", None))
        self.tmpLabel.setText(QCoreApplication.translate("MainWindow", u"Temp\u00e9rature interne", None))
        self.freqLabel.setText(QCoreApplication.translate("MainWindow", u"Fr\u00e9quence de r\u00e9ception", None))
        self.powerValueLabel.setText(QCoreApplication.translate("MainWindow", u"-85 dBm", None))
        self.freqValueLabel.setText(QCoreApplication.translate("MainWindow", u"146.520 MHz", None))
        self.tmpValueLabel.setText(QCoreApplication.translate("MainWindow", u"39.9 \u00b0C", None))
        self.alimValueLabel.setText(QCoreApplication.translate("MainWindow", u"24. 1 V", None))
        self.noiseLabel.setText(QCoreApplication.translate("MainWindow", u"Taux de bruit", None))
        self.noiseValueLabel.setText(QCoreApplication.translate("MainWindow", u"2.3 %", None))
        self.squelchLabel.setText(QCoreApplication.translate("MainWindow", u"\u00c9tat du Squelch", None))
        self.snrTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Rapport Signal/Bruit (SNR)", None))
        self.snrTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.snrSubtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Visualisation en temps r\u00e9el du SNR", None))
        self.snrSubtitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.actionsTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.actionsTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.actionsSubtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Contr\u00f4lez les param\u00e8tres du r\u00e9cepteur", None))
        self.actionsSubtitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.changeFreqLabel.setText(QCoreApplication.translate("MainWindow", u"Fr\u00e9quence (MHz)", None))
        self.freqLineEdit.setText(QCoreApplication.translate("MainWindow", u"146.520", None))
        self.changeFreqButton.setText(QCoreApplication.translate("MainWindow", u"Changer fr\u00e9quence", None))
        self.squelchLevelLabel.setText(QCoreApplication.translate("MainWindow", u"Niveau Squelch", None))
        self.squelchLineEdit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.adjustSquelchButton.setText(QCoreApplication.translate("MainWindow", u"Ajuster squelch", None))
        self.tmpTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Rapport Temp\u00e9rature Interne", None))
        self.tmpTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.tmpSubtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Visualisation en temps r\u00e9el de Temp\u00e9rature", None))
        self.tmpSubtitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
    # retranslateUi

