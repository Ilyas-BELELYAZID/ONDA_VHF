# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_vhfmYMMFJ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QScrollArea, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1323, 880)
        MainWindow.setStyleSheet(u"#scrollArea {\n"
"background-color: #FFFFFF;\n"
"}\n"
"\n"
"/* --- Contenu Principal --- */\n"
"#mainContent {\n"
"	background-color: #FFFFFF;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"#titleLabel {\n"
"	font-family: Source Sans Pro; \n"
"	font-size: 24px;\n"
"	font-weight: 700;\n"
"	color: #171A1F;\n"
"}\n"
"\n"
"/* --- Cartes --- */\n"
".QFrame {\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 12px;\n"
"	border: 1px solid #E5E7EB;\n"
"}\n"
"\n"
".cardTitleLabel {\n"
"	font-family: Roboto; \n"
"	font-size: 20px; \n"
"	font-weight: 700; \n"
"	color: #171A1F;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
".dataLabel {\n"
"	font-family: Roboto; \n"
"	font-size: 20px; \n"
"	font-weight: 600; \n"
"	color: #171A1F; \n"
"}\n"
"\n"
".dataValue {\n"
"	font-family: Open Sans; \n"
"	font-size: 12px; \n"
"	font-weight: 600; \n"
"	color: #565D6D; \n"
"}\n"
"\n"
"/* --- Graphes --- */\n"
"#chartPlaceholder {\n"
"	background-color: #F9FAFB;\n"
"	border-radius: 8px;\n"
"	border: 1px dashed #D1D5DB;\n"
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
        self.verticalLayout_3 = QVBoxLayout(self.mainContent)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 5, 20)
        self.headerFrame = QFrame(self.mainContent)
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
        self.titleLabel.setStyleSheet(u"color: #11182B;")

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.headerFrame)

        self.scrollArea = QScrollArea(self.mainContent)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* Optional: Pour un look plus propre, on enl\u00e8ve la bordure du ScrollArea */\n"
"QScrollArea {\n"
"	border: none;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1298, 801))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"background-color: #FFFFFF;")
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.scrollAreaWidgetContents_5)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 15, 0)
        self.statusCard = QFrame(self.widget)
        self.statusCard.setObjectName(u"statusCard")
        self.statusCard.setStyleSheet(u"")
        self.statusCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.statusCard)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 15, 20, 30)
        self.frame_3 = QFrame(self.statusCard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setWeight(QFont.DemiBold)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #6B7280;")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"padding-top: 5px;")
        self.label_19.setPixmap(QPixmap(u":/icons/icons/shield-check.svg"))

        self.horizontalLayout_6.addWidget(self.label_19)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.label_3 = QLabel(self.statusCard)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font-family: Roboto; \n"
"font-size: 36px; \n"
"font-weight: 700; \n"
"color: #171A1F;")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.statusCard)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Open Sans"])
        font3.setWeight(QFont.ExtraLight)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"width: 216px; \n"
"font-family: Open Sans; \n"
"font-size: 12px; \n"
"line-height: 20px; \n"
"font-weight: 200; \n"
"color: #565D6D;")

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout_4.addWidget(self.statusCard)

        self.equipmentsCard = QFrame(self.widget)
        self.equipmentsCard.setObjectName(u"equipmentsCard")
        self.equipmentsCard.setStyleSheet(u"")
        self.equipmentsCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.equipmentsCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.equipmentsCard)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 15, 20, 30)
        self.frame_4 = QFrame(self.equipmentsCard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #6B7280;")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"padding-top: 5px;")
        self.label_20.setPixmap(QPixmap(u":/icons/icons/list-check.svg"))

        self.horizontalLayout_7.addWidget(self.label_20)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.label_6 = QLabel(self.equipmentsCard)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font-family: Roboto; \n"
"font-size: 36px; \n"
"font-weight: 700; \n"
"color: #171A1F;")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.equipmentsCard)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"width: 216px; \n"
"font-family: Open Sans; \n"
"font-size: 12px; \n"
"line-height: 20px; \n"
"font-weight: 200; \n"
"color: #565D6D;")

        self.verticalLayout_5.addWidget(self.label_7)


        self.horizontalLayout_4.addWidget(self.equipmentsCard)

        self.alertsCard = QFrame(self.widget)
        self.alertsCard.setObjectName(u"alertsCard")
        self.alertsCard.setStyleSheet(u"")
        self.alertsCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.alertsCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.alertsCard)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 15, 20, 30)
        self.frame_5 = QFrame(self.alertsCard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: none;")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: #6B7280;")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"padding-top: 5px;")
        self.label_21.setPixmap(QPixmap(u":/icons/icons/alert-triangle_1.svg"))

        self.horizontalLayout_8.addWidget(self.label_21)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.label_9 = QLabel(self.alertsCard)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"font-family: Roboto; \n"
"font-size: 36px; \n"
"font-weight: 700; \n"
"color: #171A1F;")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.alertsCard)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"width: 216px; \n"
"font-family: Open Sans; \n"
"font-size: 12px; \n"
"font-weight: 200; \n"
"color: #565D6D;")

        self.verticalLayout_6.addWidget(self.label_10)


        self.horizontalLayout_4.addWidget(self.alertsCard)

        self.lastUpdateCard = QFrame(self.widget)
        self.lastUpdateCard.setObjectName(u"lastUpdateCard")
        self.lastUpdateCard.setStyleSheet(u"")
        self.lastUpdateCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.lastUpdateCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.lastUpdateCard)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.frame_2 = QFrame(self.lastUpdateCard)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: #6B7280;")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"padding-top: 5px;")
        self.label_18.setPixmap(QPixmap(u":/icons/icons/history_1.svg"))

        self.horizontalLayout_5.addWidget(self.label_18)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.label_12 = QLabel(self.lastUpdateCard)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"font-family: Roboto; \n"
"font-size: 36px; \n"
"font-weight: 700; \n"
"color: #171A1F;")

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.lastUpdateCard)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"width: 216px; \n"
"font-family: Open Sans; \n"
"font-size: 12px; \n"
"line-height: 20px; \n"
"font-weight: 200; \n"
"color: #565D6D;")

        self.verticalLayout_7.addWidget(self.label_13)


        self.horizontalLayout_4.addWidget(self.lastUpdateCard)


        self.verticalLayout_10.addWidget(self.widget)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(8)
        self.gridLayout_2.setContentsMargins(0, 5, 15, 0)
        self.temperatureChartFrame = QFrame(self.widget_2)
        self.temperatureChartFrame.setObjectName(u"temperatureChartFrame")
        self.temperatureChartFrame.setStyleSheet(u"")
        self.temperatureChartFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.temperatureChartFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.temperatureChartFrame)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 8)
        self.label_14 = QLabel(self.temperatureChartFrame)
        self.label_14.setObjectName(u"label_14")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setWeight(QFont.DemiBold)
        self.label_14.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_14)

        self.widget_4 = QWidget(self.temperatureChartFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.widget_4)

        self.verticalLayout_8.setStretch(1, 1)

        self.gridLayout_2.addWidget(self.temperatureChartFrame, 1, 0, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.powerGaugeFrame = QFrame(self.widget_2)
        self.powerGaugeFrame.setObjectName(u"powerGaugeFrame")
        self.powerGaugeFrame.setStyleSheet(u"")
        self.powerGaugeFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.powerGaugeFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.powerGaugeFrame)
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 10, 15, 20)
        self.label_15 = QLabel(self.powerGaugeFrame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.verticalLayout_9.addWidget(self.label_15)

        self.frame_6 = QFrame(self.powerGaugeFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(245, 120))
        self.frame_6.setMaximumSize(QSize(245, 120))
        self.frame_6.setStyleSheet(u"background-image: url(:/images/images/gauge.png);\n"
"border: none;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 66, 0, 0)
        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(48, 48))
        self.label_22.setMaximumSize(QSize(48, 48))
        self.label_22.setPixmap(QPixmap(u":/icons/icons/gauge.svg"))
        self.label_22.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frame_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gaugeLabel = QLabel(self.powerGaugeFrame)
        self.gaugeLabel.setObjectName(u"gaugeLabel")
        self.gaugeLabel.setFont(font2)
        self.gaugeLabel.setStyleSheet(u"font-family: Roboto; \n"
"font-size: 36px; \n"
"font-weight: 700; \n"
"color: #171A1F;")
        self.gaugeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.gaugeLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_16 = QLabel(self.powerGaugeFrame)
        self.label_16.setObjectName(u"label_16")
        font5 = QFont()
        font5.setFamilies([u"Open Sans"])
        font5.setBold(False)
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"font-family: Open Sans; \n"
"font-size: 12px; \n"
"font-weight: 400; \n"
"color: #565D6D;")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_2.addWidget(self.powerGaugeFrame, 1, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(0, 5, 15, 0)
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setMinimumHeight(300)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	width: 1058px; \n"
"	height: 329.5px; \n"
"	border: none;\n"
"	gridline-color: #E5E7EB;\n"
"	font-family: Inter;\n"
"	font-size: 10pt;\n"
"	border-radius: 6px;\n"
"	opacity: 1;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 500; \n"
"	color: #565D6D; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	padding: 10px;\n"
"	font-weight: bold;\n"
"	color: #6B7280;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	padding: 15px 10px;\n"
"	font-family: Open Sans; \n"
"	font-size: 14px; \n"
"	font-weight: 400; \n"
"	color: #171A1F; \n"
"}\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA - Supervision VHF", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Vue d'ensemble du syst\u00e8me", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00c9TAT G\u00c9N\u00c9RAL DU SYST\u00c8ME", None))
        self.label_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_19.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tous les syst\u00e8mes fonctionnent\n"
"normalement.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00c9QUIPEMENTS CONNECT\u00c9S", None))
        self.label_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_20.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre total d'appareils actifs.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ALERTES EN COURS", None))
        self.label_8.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_21.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Alertes critiques et moyennes.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"DERNI\u00c8RE MISE \u00c0 JOUR", None))
        self.label_11.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataValue", None))
        self.label_18.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"2025-08-15\n"
"14:30", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Donn\u00e9es accumul\u00e9es en temps\n"
"r\u00e9el.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Courbe de Temp\u00e9rature (24h)", None))
        self.label_14.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Donn\u00e9es en temps r\u00e9el", None))
        self.label.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Puissance d'\u00c9mission Actuelle", None))
        self.label_15.setProperty(u"class", QCoreApplication.translate("MainWindow", u"dataLabel", None))
        self.label_22.setText("")
        self.gaugeLabel.setText(QCoreApplication.translate("MainWindow", u"75%", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"de la capacit\u00e9 maximale", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Statut", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gravit\u00e9", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Journal des alertes r\u00e9centes", None))
        self.label_17.setProperty(u"class", QCoreApplication.translate("MainWindow", u"cardTitleLabel", None))
    # retranslateUi

