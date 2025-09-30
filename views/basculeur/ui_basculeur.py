# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basculeur_vhfyCkkzH.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
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
"#mainContentFrame {\n"
"	background-color: #FFFFFF;\n"
"	border: None;\n"
"	border-radius: 0px;\n"
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
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContentFrame = QFrame(self.centralwidget)
        self.mainContentFrame.setObjectName(u"mainContentFrame")
        self.mainContentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainContentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.mainContentFrame)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(32, 24, 32, 24)
        self.headerFrame = QFrame(self.mainContentFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"border: none;")
        self.headerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.headerFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Source Sans Pro"])
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.headerFrame)

        self.alertRed = QFrame(self.mainContentFrame)
        self.alertRed.setObjectName(u"alertRed")
        self.alertRed.setVisible(False)
        self.alertRed.setStyleSheet(u"#alertRed {\n"
"	width: 1120px; \n"
"	height: 74px; \n"
"	background-color: #991B1B;\n"
"	border-radius: 10px;\n"
"	border-width: 1px; \n"
"	border-color: #991B1B; \n"
"	border-style: solid; \n"
"}")
        self.alertRed.setFrameShape(QFrame.Shape.NoFrame)
        self.alertRed.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.alertRed)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.iconAlertRed = QLabel(self.alertRed)
        self.iconAlertRed.setObjectName(u"iconAlertRed")
        self.iconAlertRed.setMinimumSize(QSize(24, 24))
        self.iconAlertRed.setMaximumSize(QSize(24, 24))
        self.iconAlertRed.setPixmap(QPixmap(u":/icons/icons/exclamation-circle.svg"))
        self.iconAlertRed.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_5.addWidget(self.iconAlertRed)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.alertRedTitle = QLabel(self.alertRed)
        self.alertRedTitle.setObjectName(u"alertRedTitle")
        self.alertRedTitle.setStyleSheet(u"background-color: #991B1B;\n"
"font-family: Open Sans; \n"
"font-size: 16px; \n"
"line-height: 16px; \n"
"font-weight: 500; \n"
"color: #FFFFFF;")

        self.verticalLayout_5.addWidget(self.alertRedTitle)

        self.alertRedBody = QLabel(self.alertRed)
        self.alertRedBody.setObjectName(u"alertRedBody")
        self.alertRedBody.setStyleSheet(u"background-color: #991B1B;\n"
"color: #FFFFFF;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"font-family: Roboto; ")
        self.alertRedBody.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.alertRedBody)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.alertRed)

        self.statusFrame = QFrame(self.mainContentFrame)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setStyleSheet(u"border-radius: 12px;")
        self.statusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.statusFrame)
        self.verticalLayout_3.setSpacing(13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.statusTitleLabel = QLabel(self.statusFrame)
        self.statusTitleLabel.setObjectName(u"statusTitleLabel")
        self.statusTitleLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.statusTitleLabel)

        self.frame_2 = QFrame(self.statusFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"	font-family: Open Sans; \n"
"	font-size: 20px; \n"
"	line-height: 28px; \n"
"	font-weight: 700; \n"
"	color: #1570D1; ")
        self.label.setIndent(5)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"	font-family: Open Sans; \n"
"	font-size: 20px; \n"
"	line-height: 28px; \n"
"	font-weight: 700; \n"
"	color: #1570D1; ")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.statusBadge = QLabel(self.frame_2)
        self.statusBadge.setObjectName(u"statusBadge")
        self.statusBadge.setStyleSheet(u"background-color: #DCFCE7;\n"
"color: #166534;\n"
"border-radius: 8px;\n"
"padding: 2px 8px;\n"
"font-weight: 500;")

        self.horizontalLayout_3.addWidget(self.statusBadge)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.statusFrame)

        self.frame_3 = QFrame(self.mainContentFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnManuel = QPushButton(self.frame_3)
        self.btnManuel.setObjectName(u"btnManuel")
        self.btnManuel.setMinimumSize(QSize(0, 40))
        self.btnManuel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnManuel.setStyleSheet(u"/* Button */\n"
"QPushButton {\n"
"	width: 130.78125px; \n"
"	height: 40px; \n"
"	padding: 0 12px; \n"
"	font-family: Roboto; \n"
"	font-size: 14px; \n"
"	line-height: 22px; \n"
"	font-weight: 500; \n"
"	color: #FFFFFF; \n"
"	background: #1570D1; \n"
"	opacity: 1; \n"
"	border: none; \n"
"	border-radius: 6px; \n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"	background-color: #0E4A8A;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:hover:active {\n"
"  background: #09305A; \n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnManuel)

        self.btnConfigurer = QPushButton(self.frame_3)
        self.btnConfigurer.setObjectName(u"btnConfigurer")
        self.btnConfigurer.setMinimumSize(QSize(0, 40))
        self.btnConfigurer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConfigurer.setStyleSheet(u"/* Button */\n"
"QPushButton {\n"
"	width: 220.75px; \n"
"	height: 38.45px; \n"
"	padding: 0 12px; \n"
"	font-family: Roboto; \n"
"	font-size: 14px; \n"
"	line-height: 22px; \n"
"	font-weight: 500; \n"
"	color: #1570D1; \n"
"	background: #FFFFFF; \n"
"	opacity: 1; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #1570D1; \n"
"	border-style: solid; \n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"	background-color: #374151; \n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:hover:active {\n"
"	background-color: #F9FAFB;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnConfigurer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_3)

        self.historyFrame = QFrame(self.mainContentFrame)
        self.historyFrame.setObjectName(u"historyFrame")
        self.historyFrame.setStyleSheet(u"border: none;")
        self.historyFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.historyFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.historyFrame)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.historyTitleLabel = QLabel(self.historyFrame)
        self.historyTitleLabel.setObjectName(u"historyTitleLabel")
        self.historyTitleLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.historyTitleLabel)

        self.tableWidget = QTableWidget(self.historyFrame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(1000, 0))
        self.tableWidget.setStyleSheet(u"/* Table */\n"
"QTableWidget {\n"
"	border: 1px solid #E5E7EB;\n"
"	border-radius: 6px;\n"
"	width: 1123px; \n"
"	height: 242.5px;\n"
"	gridline-color: #E5E7EB;\n"
"	opacity: 1; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	font-family: Roboto; \n"
"	background-color: #F9FAFB;\n"
"	color: #565D6D;\n"
"	font-size: 14px;\n"
"	padding: 8px;\n"
"	border: none;\n"
"	border-bottom: 1px solid #E5E7EB;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	font-family: Roboto; \n"
"	font-size: 14px; \n"
"	padding-left: 8px;\n"
"	font-weight: 400;\n"
"	color: #171A1F;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableWidget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.historyFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout.setStretch(5, 1)

        self.horizontalLayout.addWidget(self.mainContentFrame)

        self.horizontalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA - Basculeur", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Basculeur", None))
        self.iconAlertRed.setText("")
        self.alertRedTitle.setText(QCoreApplication.translate("MainWindow", u"D\u00e9faillance canal principal", None))
        self.alertRedBody.setText(QCoreApplication.translate("MainWindow", u"Une d\u00e9faillance a \u00e9t\u00e9 d\u00e9tect\u00e9e sur le canal principal. Le basculement automatique est recommand\u00e9.", None))
        self.statusTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\u00c9tat de l'\u00e9quipement", None))
        self.statusTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00c9quipement actif :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.statusBadge.setText(QCoreApplication.translate("MainWindow", u"Actif", None))
        self.btnManuel.setText(QCoreApplication.translate("MainWindow", u"Basculement manuel", None))
        self.btnConfigurer.setText(QCoreApplication.translate("MainWindow", u"Configurer bascule automatique", None))
        self.historyTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Historique des basculements", None))
        self.historyTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date/Heure", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type d'\u00e9v\u00e9nement", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2023-10-26 14:30", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Manuel", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Principal", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2023-10-25 09:15", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"D\u00e9faillance", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Principal", None));
        ___qtablewidgetitem9 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2023-10-24 18:00", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Automatique", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Secours", None));
        ___qtablewidgetitem12 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2023-10-23 11:45", None));
        ___qtablewidgetitem13 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Manuel", None));
        ___qtablewidgetitem14 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Principal", None));
        ___qtablewidgetitem15 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2023-10-22 07:00", None));
        ___qtablewidgetitem16 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"D\u00e9faillance", None));
        ___qtablewidgetitem17 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Secours", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

