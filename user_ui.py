# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import userUiRescources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(754, 600)
        icon = QIcon(QIcon.fromTheme(u"emblem-shared"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(223, 32, 112);")
        self.actionLopeta = QAction(MainWindow)
        self.actionLopeta.setObjectName(u"actionLopeta")
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionLopeta.setIcon(icon1)
        self.actionKalle = QAction(MainWindow)
        self.actionKalle.setObjectName(u"actionKalle")
        self.actionVille = QAction(MainWindow)
        self.actionVille.setObjectName(u"actionVille")
        self.actionJaana = QAction(MainWindow)
        self.actionJaana.setObjectName(u"actionJaana")
        self.actionMikko = QAction(MainWindow)
        self.actionMikko.setObjectName(u"actionMikko")
        self.actionTallenna_nimell = QAction(MainWindow)
        self.actionTallenna_nimell.setObjectName(u"actionTallenna_nimell")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ssnLineEdit = QLineEdit(self.centralwidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setEnabled(True)
        self.ssnLineEdit.setGeometry(QRect(60, 330, 191, 31))
        font = QFont()
        font.setPointSize(18)
        self.ssnLineEdit.setFont(font)
        self.ssnLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(32, 75, 70);")
        self.ssnLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ssnLineEdit.setClearButtonEnabled(True)
        self.keyBarcodeLineEdit = QLineEdit(self.centralwidget)
        self.keyBarcodeLineEdit.setObjectName(u"keyBarcodeLineEdit")
        self.keyBarcodeLineEdit.setEnabled(True)
        self.keyBarcodeLineEdit.setGeometry(QRect(390, 330, 121, 31))
        self.keyBarcodeLineEdit.setFont(font)
        self.keyBarcodeLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.keyBarcodeLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keyBarcodeLineEdit.setClearButtonEnabled(True)
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(100, 0, 171, 101))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.takeCarPushButton.setFont(font1)
        self.takeCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeCarPushButton.setToolTipDuration(3000)
        self.takeCarPushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(140, 51, 85);")
        icon2 = QIcon()
        icon2.addFile(u":/pictures/uiPictures/ota.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.takeCarPushButton.setIcon(icon2)
        self.takeCarPushButton.setIconSize(QSize(42, 42))
        self.keyPictureLabel = QLabel(self.centralwidget)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setEnabled(True)
        self.keyPictureLabel.setGeometry(QRect(330, 160, 201, 141))
        self.keyPictureLabel.setPixmap(QPixmap(u":/pictures/uiPictures/keys.png"))
        self.keyPictureLabel.setScaledContents(True)
        self.lenderPictureLabel = QLabel(self.centralwidget)
        self.lenderPictureLabel.setObjectName(u"lenderPictureLabel")
        self.lenderPictureLabel.setEnabled(True)
        self.lenderPictureLabel.setGeometry(QRect(50, 100, 211, 231))
        self.lenderPictureLabel.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lenderPictureLabel.setPixmap(QPixmap(u":/pictures/uiPictures/Teacher.png"))
        self.lenderPictureLabel.setScaledContents(False)
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setEnabled(True)
        self.dateLabel.setGeometry(QRect(80, 400, 191, 41))
        font2 = QFont()
        font2.setPointSize(32)
        self.dateLabel.setFont(font2)
        self.dateLabel.setStyleSheet(u"color:  rgb(0, 33, 72);")
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(310, 0, 171, 101))
        self.returnCarPushButton.setFont(font1)
        self.returnCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnCarPushButton.setToolTipDuration(3000)
        self.returnCarPushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(140, 51, 85);")
        icon3 = QIcon()
        icon3.addFile(u":/pictures/uiPictures/palauta.drawio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.returnCarPushButton.setIcon(icon3)
        self.returnCarPushButton.setIconSize(QSize(42, 42))
        self.calendarLabel = QLabel(self.centralwidget)
        self.calendarLabel.setObjectName(u"calendarLabel")
        self.calendarLabel.setGeometry(QRect(40, 400, 31, 51))
        self.calendarLabel.setPixmap(QPixmap(u":/pictures/uiPictures/calendar.png"))
        self.calendarLabel.setScaledContents(True)
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setEnabled(True)
        self.timeLabel.setGeometry(QRect(440, 400, 111, 41))
        self.timeLabel.setFont(font2)
        self.timeLabel.setStyleSheet(u"color:  rgb(0, 33, 72);")
        self.clockLabel = QLabel(self.centralwidget)
        self.clockLabel.setObjectName(u"clockLabel")
        self.clockLabel.setGeometry(QRect(370, 400, 41, 41))
        self.clockLabel.setPixmap(QPixmap(u":/pictures/uiPictures/clock.png"))
        self.clockLabel.setScaledContents(True)
        self.goBackPushButton = QPushButton(self.centralwidget)
        self.goBackPushButton.setObjectName(u"goBackPushButton")
        self.goBackPushButton.setGeometry(QRect(570, 440, 171, 91))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.goBackPushButton.setFont(font3)
        self.goBackPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/pictures/uiPictures/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.goBackPushButton.setIcon(icon4)
        self.goBackPushButton.setIconSize(QSize(32, 32))
        self.soundOnPushButton = QPushButton(self.centralwidget)
        self.soundOnPushButton.setObjectName(u"soundOnPushButton")
        self.soundOnPushButton.setGeometry(QRect(520, 0, 101, 101))
        self.soundOnPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);")
        icon5 = QIcon()
        icon5.addFile(u":/pictures/uiPictures/soundOn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOnPushButton.setIcon(icon5)
        self.soundOnPushButton.setIconSize(QSize(48, 48))
        self.soundOffPushButton = QPushButton(self.centralwidget)
        self.soundOffPushButton.setObjectName(u"soundOffPushButton")
        self.soundOffPushButton.setGeometry(QRect(520, 0, 101, 101))
        self.soundOffPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);")
        icon6 = QIcon()
        icon6.addFile(u":/pictures/uiPictures/soundOff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOffPushButton.setIcon(icon6)
        self.soundOffPushButton.setIconSize(QSize(56, 56))
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(70, 10, 441, 91))
        font4 = QFont()
        font4.setPointSize(36)
        font4.setBold(True)
        self.statusLabel.setFont(font4)
        self.statusLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lenderNameLabel = QLabel(self.centralwidget)
        self.lenderNameLabel.setObjectName(u"lenderNameLabel")
        self.lenderNameLabel.setGeometry(QRect(70, 360, 181, 31))
        font5 = QFont()
        font5.setPointSize(16)
        self.lenderNameLabel.setFont(font5)
        self.lenderNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.carInfoLabel = QLabel(self.centralwidget)
        self.carInfoLabel.setObjectName(u"carInfoLabel")
        self.carInfoLabel.setGeometry(QRect(360, 360, 181, 31))
        self.carInfoLabel.setFont(font5)
        self.carInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.okPushButton = QPushButton(self.centralwidget)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setGeometry(QRect(570, 330, 171, 91))
        font6 = QFont()
        font6.setPointSize(24)
        font6.setBold(True)
        self.okPushButton.setFont(font6)
        self.okPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);\n"
"color: rgb(255, 255, 255);")
        self.okPushButton.setIconSize(QSize(32, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 754, 33))
        self.menubar.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        self.menuTiedosto = QMenu(self.menubar)
        self.menuTiedosto.setObjectName(u"menuTiedosto")
        self.menuEdelliset = QMenu(self.menuTiedosto)
        self.menuEdelliset.setObjectName(u"menuEdelliset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font7 = QFont()
        font7.setPointSize(9)
        self.statusbar.setFont(font7)
        self.statusbar.setToolTipDuration(-1)
        self.statusbar.setStyleSheet(u"background-color: rgb(243, 89, 148);")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTiedosto.menuAction())
        self.menuTiedosto.addAction(self.actionLopeta)
        self.menuTiedosto.addAction(self.menuEdelliset.menuAction())
        self.menuTiedosto.addAction(self.actionTallenna_nimell)
        self.menuEdelliset.addAction(self.actionKalle)
        self.menuEdelliset.addAction(self.actionVille)
        self.menuEdelliset.addAction(self.actionJaana)
        self.menuEdelliset.addAction(self.actionMikko)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLopeta.setText(QCoreApplication.translate("MainWindow", u"Lopeta", None))
#if QT_CONFIG(shortcut)
        self.actionLopeta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionKalle.setText(QCoreApplication.translate("MainWindow", u"Kalle", None))
        self.actionVille.setText(QCoreApplication.translate("MainWindow", u"Ville", None))
        self.actionJaana.setText(QCoreApplication.translate("MainWindow", u"Jaana", None))
        self.actionMikko.setText(QCoreApplication.translate("MainWindow", u"Mikko", None))
        self.actionTallenna_nimell.setText(QCoreApplication.translate("MainWindow", u"Tallenna nimell\u00e4...", None))
        self.ssnLineEdit.setText("")
        self.ssnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue ajokortti", None))
        self.keyBarcodeLineEdit.setText("")
        self.keyBarcodeLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avain", None))
#if QT_CONFIG(tooltip)
        self.takeCarPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tallentaa henkil\u00f6n tiedot tietokantaa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"LAINAA", None))
        self.keyPictureLabel.setText("")
        self.lenderPictureLabel.setText("")
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"15.3.2024", None))
#if QT_CONFIG(tooltip)
        self.returnCarPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tallentaa henkil\u00f6n tiedot tietokantaa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.returnCarPushButton.setText(QCoreApplication.translate("MainWindow", u"PALAUTA", None))
        self.calendarLabel.setText("")
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"10.05", None))
        self.clockLabel.setText("")
        self.goBackPushButton.setText(QCoreApplication.translate("MainWindow", u"Palaa takaisin", None))
        self.soundOnPushButton.setText("")
        self.soundOffPushButton.setText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Tila", None))
        self.lenderNameLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaajan nimi", None))
        self.carInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki ja malli", None))
        self.okPushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menuEdelliset.setTitle(QCoreApplication.translate("MainWindow", u"Edelliset", None))
    # retranslateUi
