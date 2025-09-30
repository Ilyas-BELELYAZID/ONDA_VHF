# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'packagesexSlnP.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"/* --- Barre Lat\u00e9rale --- */\n"
"#sidebar {\n"
"	background: #F8F9FA; \n"
"  	border-radius: 0px; \n"
"  	border-width: 1px; \n"
"  	border-color: #DEE1E6; \n"
"  	border-style: solid;\n"
"}\n"
"\n"
"#logoLabel {\n"
"	text-align: left;\n"
"	font-size: 24px;\n"
"	font-weight: bold;\n"
"	color: #111827;\n"
"}\n"
"\n"
"#frame {\n"
"	Background: transparent;\n"
"	Border: None;\n"
"}\n"
"\n"
"#navButtonsContainer QPushButton {\n"
"	text-align: left;\n"
"	border: none;\n"
"	border-radius: 22px;\n"
"	color: #374151;\n"
"	background-color: transparent;\n"
"	padding: 12px 12px; \n"
"	font-family: Inter;\n"
"	font-size: 14px;\n"
"	font-weight: 400;\n"
"	opacity: 1;\n"
"}\n"
"\n"
"#navButtonsContainer QPushButton:hover {\n"
"	border-radius: 22px;\n"
"	background-color: #F3F4F6;\n"
"}\n"
"\n"
"#navButtonsContainer QPushButton:checked {\n"
"	font-weight: 700; \n"
"	background-color: #E5E7EB;\n"
"	color: #111827;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#logoutButton {\n"
"	text-align: left;\n"
"	width: 254px; \n"
"	heig"
                        "ht: 40px;\n"
"	padding: 0 12px;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	font-family: Open Sans; \n"
"	font-size: 14px;\n"
"	color: #004480;\n"
"	background-color: transparent;\n"
"	opacity: 1; \n"
"	line-height: 22px; \n"
"	font-weight: 500; \n"
"}\n"
"\n"
"#logoutButton:hover {\n"
"	color: #004480;\n"
"	background-color: #F9FAFB;\n"
"}\n"
"\n"
"#logoutButton:hover:active {\n"
"	color: #004480; \n"
"	background-color: #F9FAFB;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(220, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.sidebar.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 15, 10, 20)
        self.frame = QFrame(self.sidebar)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.frame)
        self.logoLabel.setObjectName(u"logoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy)
        self.logoLabel.setMinimumSize(QSize(5, 0))
        palette = QPalette()
        brush = QBrush(QColor(17, 24, 39, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush1 = QBrush(QColor(17, 24, 39, 128))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush1)
#endif
        self.logoLabel.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setBold(True)
        self.logoLabel.setFont(font1)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.logoLabel, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(115, 66))
        self.label.setPixmap(QPixmap(u":/images/logo_onda.png"))
        self.label.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.navButtonsContainer = QWidget(self.sidebar)
        self.navButtonsContainer.setObjectName(u"navButtonsContainer")
        self.navButtonsContainer.setEnabled(True)
        font2 = QFont()
        self.navButtonsContainer.setFont(font2)
        self.verticalLayout_7 = QVBoxLayout(self.navButtonsContainer)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dashboardButton = QPushButton(self.navButtonsContainer)
        self.dashboardButton.setObjectName(u"dashboardButton")
        palette1 = QPalette()
        brush2 = QBrush(QColor(55, 65, 81, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 0))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        brush4 = QBrush(QColor(55, 65, 81, 128))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.dashboardButton.setPalette(palette1)
        self.dashboardButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboardButton.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u":/icons/icons/layout-dashboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboardButton.setIcon(icon)
        self.dashboardButton.setIconSize(QSize(24, 24))
        self.dashboardButton.setCheckable(True)
        self.dashboardButton.setChecked(True)

        self.verticalLayout_7.addWidget(self.dashboardButton)

        self.emetteurButton = QPushButton(self.navButtonsContainer)
        self.emetteurButton.setObjectName(u"emetteurButton")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.emetteurButton.setPalette(palette2)
        self.emetteurButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.emetteurButton.setMouseTracking(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/ripple.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.emetteurButton.setIcon(icon1)
        self.emetteurButton.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.emetteurButton)

        self.receiverButton = QPushButton(self.navButtonsContainer)
        self.receiverButton.setObjectName(u"receiverButton")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.receiverButton.setPalette(palette3)
        self.receiverButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.receiverButton.setMouseTracking(True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/microwave.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.receiverButton.setIcon(icon2)
        self.receiverButton.setIconSize(QSize(24, 24))
        self.receiverButton.setCheckable(False)
        self.receiverButton.setChecked(False)

        self.verticalLayout_7.addWidget(self.receiverButton)

        self.switchButton = QPushButton(self.navButtonsContainer)
        self.switchButton.setObjectName(u"switchButton")
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.switchButton.setPalette(palette4)
        self.switchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.switchButton.setMouseTracking(True)
        self.switchButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/git-fork.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.switchButton.setIcon(icon3)
        self.switchButton.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.switchButton)

        self.historyButton = QPushButton(self.navButtonsContainer)
        self.historyButton.setObjectName(u"historyButton")
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.historyButton.setPalette(palette5)
        self.historyButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyButton.setMouseTracking(True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/history.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.historyButton.setIcon(icon4)
        self.historyButton.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.historyButton)


        self.verticalLayout_2.addWidget(self.navButtonsContainer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.logoutButton = QPushButton(self.sidebar)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush3)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush3)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush3)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.logoutButton.setPalette(palette6)
        font3 = QFont()
        font3.setFamilies([u"Open Sans"])
        font3.setWeight(QFont.Medium)
        self.logoutButton.setFont(font3)
        self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutButton.setMouseTracking(True)
        self.logoutButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/logout.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutButton.setIcon(icon5)
        self.logoutButton.setIconSize(QSize(20, 20))
        self.logoutButton.setAutoRepeat(False)

        self.verticalLayout_2.addWidget(self.logoutButton)


        self.horizontalLayout.addWidget(self.sidebar)

        self.mainContent = QWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setStyleSheet(u"background-color: #FFFFFF;\n"
"border: none;")
        self.verticalLayout_3 = QVBoxLayout(self.mainContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.package_screens = QStackedWidget(self.mainContent)
        self.package_screens.setObjectName(u"package_screens")
        self.package_screens.setStyleSheet(u"")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout = QVBoxLayout(self.dashboard)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.dashboard)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.package_screens.addWidget(self.dashboard)
        self.emetteur = QWidget()
        self.emetteur.setObjectName(u"emetteur")
        self.verticalLayout_4 = QVBoxLayout(self.emetteur)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.emetteur)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.frame_3)

        self.package_screens.addWidget(self.emetteur)
        self.recepteur = QWidget()
        self.recepteur.setObjectName(u"recepteur")
        self.verticalLayout_5 = QVBoxLayout(self.recepteur)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.recepteur)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_4)

        self.package_screens.addWidget(self.recepteur)
        self.basculeur = QWidget()
        self.basculeur.setObjectName(u"basculeur")
        self.verticalLayout_6 = QVBoxLayout(self.basculeur)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.basculeur)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.package_screens.addWidget(self.basculeur)
        self.historique = QWidget()
        self.historique.setObjectName(u"historique")
        self.verticalLayout_8 = QVBoxLayout(self.historique)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.historique)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_8.addWidget(self.frame_6)

        self.package_screens.addWidget(self.historique)
        self.erreur = QWidget()
        self.erreur.setObjectName(u"erreur")
        self.verticalLayout_10 = QVBoxLayout(self.erreur)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.erreur)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_10.addWidget(self.frame_7)

        self.package_screens.addWidget(self.erreur)

        self.verticalLayout_3.addWidget(self.package_screens)


        self.horizontalLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.package_screens.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ONDA - Supervision VHF", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"ONDA", None))
        self.label.setText("")
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.emetteurButton.setText(QCoreApplication.translate("MainWindow", u"\u00c9metteur", None))
        self.receiverButton.setText(QCoreApplication.translate("MainWindow", u"R\u00e9cepteur", None))
        self.switchButton.setText(QCoreApplication.translate("MainWindow", u"Basculeur", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"Historique", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Signout", None))
    # retranslateUi

