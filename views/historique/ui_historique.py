# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historique_vhfsYtSfy.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet(u"/* --- Contenu Principal --- */\n"
"#mainContentWidget {\n"
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
"	font-family: Open Sans;\n"
"	font-size: 18px;\n"
"	font-weight: 600;\n"
"	color: #171A1F;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
".dataLabel {\n"
"	font-size: 14px;\n"
"	font-family: Open Sans;\n"
"	color: #565D6D;\n"
"	font-weight: 500; \n"
"}\n"
"\n"
".dataValue {\n"
"	font-family: Open Sans;\n"
"	font-size: 12px;\n"
"	font-weight: 600;\n"
"	color: #171A1F;\n"
"}\n"
"\n"
"/* --- Graphes --- */\n"
"#graphPlaceholder {\n"
"	width: 1080px; \n"
"	height: 350px; \n"
"	background-color: #F9FAFB;\n"
"	border-radius: 8px;\n"
"	border: 1px dashed #D1D5DB;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContentWidget = QWidget(self.centralwidget)
        self.mainContentWidget.setObjectName(u"mainContentWidget")
        self.verticalLayout_3 = QVBoxLayout(self.mainContentWidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 20, 5, 20)
        self.headerFrame = QFrame(self.mainContentWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"border: none;")
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.headerFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Source Sans Pro"])
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnExportPDF = QPushButton(self.headerFrame)
        self.btnExportPDF.setObjectName(u"btnExportPDF")
        self.btnExportPDF.setMinimumSize(QSize(120, 40))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setWeight(QFont.Medium)
        self.btnExportPDF.setFont(font1)
        self.btnExportPDF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportPDF.setStyleSheet(u"/* Button */\n"
"\n"
"QPushButton {\n"
"	height: 40px; \n"
"	padding: 0 12px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 500; \n"
"	color: #007BFF; \n"
"	background: #FFFFFF; \n"
"	opacity: 1; \n"
"	border: 1px solid #007BFF; \n"
"	border-radius: 8px; \n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"	background: #0050A6; \n"
"	border: 1px solid #0050A6; \n"
"}\n"
"/* Pressed */\n"
"QPushButton:hover:active {\n"
"	background: #004084; \n"
"	border: 1px solid #004084; \n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportPDF.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btnExportPDF)

        self.btnExportExcel = QPushButton(self.headerFrame)
        self.btnExportExcel.setObjectName(u"btnExportExcel")
        self.btnExportExcel.setMinimumSize(QSize(120, 40))
        self.btnExportExcel.setFont(font1)
        self.btnExportExcel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExportExcel.setStyleSheet(u"/* Button */\n"
"QPushButton {\n"
"	height: 40px; \n"
"	padding: 0 12px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 500; \n"
"	color: #FFFFFF; \n"
"	background: #007BFF; \n"
"	opacity: 1; \n"
"	border: none; \n"
"	border-radius: 8px; \n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"	background-color: #0050A6;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:hover:active {\n"
"  background: #004084; \n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-spreadsheet.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExportExcel.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnExportExcel)


        self.verticalLayout_3.addWidget(self.headerFrame)

        self.scrollArea = QScrollArea(self.mainContentWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* Optional: Pour un look plus propre, on enl\u00e8ve la bordure du ScrollArea */\n"
"QScrollArea {\n"
"	border: none;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1168, 901))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.scrollAreaWidgetContents_6)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 15, 5)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #495057;")

        self.verticalLayout_12.addWidget(self.label_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(200, 35))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"	padding-left: 12px; \n"
"	padding-right: 34px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	background: #FFFFFF; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"	outline: none; \n"
"}\n"
"\n"
"/* hover */\n"
"QDateEdit:hover {\n"
"  color: #171A1F; \n"
"}\n"
"/* focused */\n"
"QDateEdit:focused {\n"
"  color: #171A1F; \n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"	width: 16px; \n"
"	height: 16px; \n"
"    image: url(:/icons/icons/calendar-week.svg); /* Chemin vers l'ic\u00f4ne */\n"
"}\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CED4DA;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"")
        self.dateEdit.setProperty(u"showGroupSeparator", False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate().addMonths(-1))

        self.horizontalLayout_3.addWidget(self.dateEdit)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.dateEdit_2 = QDateEdit(self.frame_4)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(200, 35))
        self.dateEdit_2.setStyleSheet(u"QDateEdit {\n"
"	padding-left: 12px; \n"
"	padding-right: 34px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	background: #FFFFFF; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"	outline: none; \n"
"}\n"
"\n"
"/* hover */\n"
"QDateEdit:hover {\n"
"  color: #171A1F; \n"
"}\n"
"/* focused */\n"
"QDateEdit:focused {\n"
"  color: #171A1F; \n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"	width: 16px; \n"
"	height: 16px; \n"
"    image: url(:/icons/icons/calendar-week.svg); /* Chemin vers l'ic\u00f4ne */\n"
"}\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CED4DA;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"")
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dateEdit_2)


        self.verticalLayout_12.addWidget(self.frame_4)


        self.gridLayout.addLayout(self.verticalLayout_12, 1, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #495057;")

        self.verticalLayout_13.addWidget(self.label_5)

        self.comboEquipement = QComboBox(self.frame)
        self.comboEquipement.addItem("")
        self.comboEquipement.addItem("")
        self.comboEquipement.addItem("")
        self.comboEquipement.addItem("")
        self.comboEquipement.setObjectName(u"comboEquipement")
        self.comboEquipement.setMinimumSize(QSize(200, 35))
        self.comboEquipement.setStyleSheet(u"QComboBox {\n"
"	padding-left: 12px; \n"
"	padding-right: 34px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	background: #FFFFFF; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"	outline: none; \n"
"}\n"
"\n"
"/* hover */\n"
"QComboBox:hover {\n"
"	color: #171A1F; \n"
"}\n"
"\n"
"/* focused */\n"
"QComboBox:focused {\n"
"	color: #171A1F; \n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	width: 16px; \n"
"	height: 16px; \n"
"	image: url(:/icons/icons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CED4DA;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.comboEquipement)


        self.gridLayout.addLayout(self.verticalLayout_13, 1, 2, 1, 1)

        self.btnAppliquer = QPushButton(self.frame)
        self.btnAppliquer.setObjectName(u"btnAppliquer")
        self.btnAppliquer.setMinimumSize(QSize(120, 40))
        self.btnAppliquer.setFont(font1)
        self.btnAppliquer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAppliquer.setStyleSheet(u"/* Button */\n"
"QPushButton {\n"
"	height: 40px; \n"
"	padding: 0 12px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 500; \n"
"	color: #171A1F; \n"
"	background: #FFFFFF; \n"
"	opacity: 1; \n"
"	border-radius: 8px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"	color: #FFFFFF;\n"
"	background-color: #171A1F;\n"
"	border-color: #FFFFFF;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:hover:active {\n"
"	color: #FFFFFF;\n"
"	background-color: #171A1F;\n"
"	border-color: #FFFFFF;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnAppliquer, 1, 4, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #495057;")

        self.verticalLayout_10.addWidget(self.label_4)

        self.comboTypeEvent = QComboBox(self.frame)
        self.comboTypeEvent.addItem("")
        self.comboTypeEvent.addItem("")
        self.comboTypeEvent.addItem("")
        self.comboTypeEvent.addItem("")
        self.comboTypeEvent.addItem("")
        self.comboTypeEvent.addItem("")
        self.comboTypeEvent.setObjectName(u"comboTypeEvent")
        self.comboTypeEvent.setMinimumSize(QSize(200, 35))
        self.comboTypeEvent.setStyleSheet(u"QComboBox {\n"
"	padding-left: 12px; \n"
"	padding-right: 34px; \n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	background: #FFFFFF; \n"
"	border-radius: 6px; \n"
"	border-width: 1px; \n"
"	border-color: #DEE1E6; \n"
"	border-style: solid; \n"
"	outline: none; \n"
"}\n"
"\n"
"/* hover */\n"
"QComboBox:hover {\n"
"	color: #171A1F; \n"
"}\n"
"\n"
"/* focused */\n"
"QComboBox:focused {\n"
"	color: #171A1F; \n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	width: 16px; \n"
"	height: 16px; \n"
"	image: url(:/icons/icons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CED4DA;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.comboTypeEvent)


        self.gridLayout.addLayout(self.verticalLayout_10, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 300))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.graphPlaceholder = QWidget(self.frame_2)
        self.graphPlaceholder.setObjectName(u"graphPlaceholder")
        self.verticalLayout_6 = QVBoxLayout(self.graphPlaceholder)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.graphPlaceholder)

        self.verticalLayout_4.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 400))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.tableEvents = QTableWidget(self.frame_3)
        if (self.tableEvents.columnCount() < 5):
            self.tableEvents.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableEvents.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEvents.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEvents.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEvents.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableEvents.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableEvents.rowCount() < 1):
            self.tableEvents.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableEvents.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableEvents.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableEvents.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableEvents.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableEvents.setItem(0, 4, __qtablewidgetitem9)
        self.tableEvents.setObjectName(u"tableEvents")
        self.tableEvents.setStyleSheet(u"QTableWidget {\n"
"	width: 1083px; \n"
"	height: 329.5px; \n"
"    border: none;\n"
"    gridline-color: #E9ECEF;\n"
"	border-radius: 6px;\n"
"}\n"
"QHeaderView::section {\n"
"	font-family: Open Sans; \n"
"	font-size: 14px;  \n"
"	font-weight: 500; \n"
"	color: #565D6D;\n"
"    background-color: #F8F9FA;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #DEE2E6;\n"
"}\n"
"QTableWidget::item {\n"
"	font-family: Open Sans; \n"
"	font-size: 14px;  \n"
"	font-weight: 400; \n"
"	color: #171A1F;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.tableEvents.setAlternatingRowColors(True)
        self.tableEvents.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableEvents.setShowGrid(True)
        self.tableEvents.setSortingEnabled(True)
        self.tableEvents.horizontalHeader().setStretchLastSection(True)
        self.tableEvents.verticalHeader().setVisible(True)
        self.tableEvents.verticalHeader().setCascadingSectionResizes(False)
        self.tableEvents.verticalHeader().setDefaultSectionSize(40)
        self.tableEvents.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tableEvents)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.mainContentWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA - Historique et Rapports", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Historique et Rapports", None))
        self.btnExportPDF.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.btnExportExcel.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"P\u00e9riode", None))
        self.label_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.label.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u00e0", None))
        self.label_11.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00c9quipement", None))
        self.label_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.comboEquipement.setItemText(0, QCoreApplication.translate("MainWindow", u"Tous", None))
        self.comboEquipement.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c9metteur", None))
        self.comboEquipement.setItemText(2, QCoreApplication.translate("MainWindow", u"R\u00e9cepteur", None))
        self.comboEquipement.setItemText(3, QCoreApplication.translate("MainWindow", u"Basculeur", None))

        self.btnAppliquer.setText(QCoreApplication.translate("MainWindow", u"Appliquer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Type d'\u00e9v\u00e9nement", None))
        self.label_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.comboTypeEvent.setItemText(0, QCoreApplication.translate("MainWindow", u"Toutes", None))
        self.comboTypeEvent.setItemText(1, QCoreApplication.translate("MainWindow", u"D\u00e9faillance", None))
        self.comboTypeEvent.setItemText(2, QCoreApplication.translate("MainWindow", u"Anomalie", None))
        self.comboTypeEvent.setItemText(3, QCoreApplication.translate("MainWindow", u"Retour service", None))
        self.comboTypeEvent.setItemText(4, QCoreApplication.translate("MainWindow", u"Basculement manuel", None))
        self.comboTypeEvent.setItemText(5, QCoreApplication.translate("MainWindow", u"Configuration bascule automatique", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filtres", None))
        self.label_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u00c9volution Historique des \u00c9v\u00e9nements", None))
        self.label_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nombre d'\u00e9v\u00e9nements par mois", None))
        self.label_9.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"D\u00e9tail des \u00c9v\u00e9nements", None))
        self.label_10.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        ___qtablewidgetitem = self.tableEvents.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableEvents.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Heure", None));
        ___qtablewidgetitem2 = self.tableEvents.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u00c9quipement", None));
        ___qtablewidgetitem3 = self.tableEvents.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem4 = self.tableEvents.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gravit\u00e9", None));

        __sortingEnabled = self.tableEvents.isSortingEnabled()
        self.tableEvents.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableEvents.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2024-07-20", None));
        ___qtablewidgetitem6 = self.tableEvents.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"14:30", None));
        ___qtablewidgetitem7 = self.tableEvents.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Capteur #001", None));
        ___qtablewidgetitem8 = self.tableEvents.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Panne Syst\u00e8me", None));
        ___qtablewidgetitem9 = self.tableEvents.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Critique", None));
        self.tableEvents.setSortingEnabled(__sortingEnabled)

    # retranslateUi

