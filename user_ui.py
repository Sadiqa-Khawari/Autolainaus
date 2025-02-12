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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import pictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(781, 885)
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
        self.ssnLineEdit.setGeometry(QRect(50, 350, 191, 31))
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
        self.keyBarcodeLineEdit.setGeometry(QRect(430, 350, 121, 31))
        self.keyBarcodeLineEdit.setFont(font)
        self.keyBarcodeLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.keyBarcodeLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(70, 0, 201, 111))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.takeCarPushButton.setFont(font1)
        self.takeCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeCarPushButton.setToolTipDuration(3000)
        self.takeCarPushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(140, 51, 85);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/picture/uiPictures/ota.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.takeCarPushButton.setIcon(icon2)
        self.takeCarPushButton.setIconSize(QSize(42, 42))
        self.keyPictureLabel = QLabel(self.centralwidget)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setEnabled(True)
        self.keyPictureLabel.setGeometry(QRect(450, 170, 201, 141))
        self.keyPictureLabel.setPixmap(QPixmap(u":/picture/uiPictures/keys.png"))
        self.keyPictureLabel.setScaledContents(True)
        self.lenderPictureLabel = QLabel(self.centralwidget)
        self.lenderPictureLabel.setObjectName(u"lenderPictureLabel")
        self.lenderPictureLabel.setEnabled(True)
        self.lenderPictureLabel.setGeometry(QRect(10, 100, 211, 231))
        self.lenderPictureLabel.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lenderPictureLabel.setPixmap(QPixmap(u":/picture/uiPictures/Teacher.png"))
        self.lenderPictureLabel.setScaledContents(False)
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setEnabled(True)
        self.dateLabel.setGeometry(QRect(70, 450, 191, 41))
        font2 = QFont()
        font2.setPointSize(32)
        self.dateLabel.setFont(font2)
        self.dateLabel.setStyleSheet(u"color:  rgb(0, 33, 72);")
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(290, 0, 191, 111))
        self.returnCarPushButton.setFont(font1)
        self.returnCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnCarPushButton.setToolTipDuration(3000)
        self.returnCarPushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(140, 51, 85);")
        icon3 = QIcon()
        icon3.addFile(u":/picture/uiPictures/palauta.drawio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.returnCarPushButton.setIcon(icon3)
        self.returnCarPushButton.setIconSize(QSize(42, 42))
        self.calendarLabel = QLabel(self.centralwidget)
        self.calendarLabel.setObjectName(u"calendarLabel")
        self.calendarLabel.setGeometry(QRect(30, 440, 31, 51))
        self.calendarLabel.setPixmap(QPixmap(u":/picture/uiPictures/calendar.png"))
        self.calendarLabel.setScaledContents(True)
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setEnabled(True)
        self.timeLabel.setGeometry(QRect(440, 440, 111, 41))
        self.timeLabel.setFont(font2)
        self.timeLabel.setStyleSheet(u"color:  rgb(0, 33, 72);")
        self.clockLabel = QLabel(self.centralwidget)
        self.clockLabel.setObjectName(u"clockLabel")
        self.clockLabel.setGeometry(QRect(400, 450, 41, 41))
        self.clockLabel.setPixmap(QPixmap(u":/picture/uiPictures/clock.png"))
        self.clockLabel.setScaledContents(True)
        self.goBackPushButton = QPushButton(self.centralwidget)
        self.goBackPushButton.setObjectName(u"goBackPushButton")
        self.goBackPushButton.setGeometry(QRect(610, 450, 151, 101))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.goBackPushButton.setFont(font3)
        self.goBackPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/picture/uiPictures/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.goBackPushButton.setIcon(icon4)
        self.goBackPushButton.setIconSize(QSize(32, 32))
        self.soundOnPushButton = QPushButton(self.centralwidget)
        self.soundOnPushButton.setObjectName(u"soundOnPushButton")
        self.soundOnPushButton.setGeometry(QRect(520, 0, 101, 101))
        self.soundOnPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);")
        icon5 = QIcon()
        icon5.addFile(u":/picture/uiPictures/soundOn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOnPushButton.setIcon(icon5)
        self.soundOnPushButton.setIconSize(QSize(48, 48))
        self.soundOffPushButton = QPushButton(self.centralwidget)
        self.soundOffPushButton.setObjectName(u"soundOffPushButton")
        self.soundOffPushButton.setGeometry(QRect(520, 0, 101, 101))
        self.soundOffPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);")
        icon6 = QIcon()
        icon6.addFile(u":/picture/uiPictures/soundOff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOffPushButton.setIcon(icon6)
        self.soundOffPushButton.setIconSize(QSize(56, 56))
        self.lenderNameLabel = QLabel(self.centralwidget)
        self.lenderNameLabel.setObjectName(u"lenderNameLabel")
        self.lenderNameLabel.setGeometry(QRect(70, 400, 151, 31))
        font4 = QFont()
        font4.setPointSize(16)
        self.lenderNameLabel.setFont(font4)
        self.lenderNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.carInfoLabel = QLabel(self.centralwidget)
        self.carInfoLabel.setObjectName(u"carInfoLabel")
        self.carInfoLabel.setGeometry(QRect(420, 400, 171, 31))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.carInfoLabel.setFont(font5)
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(220, 110, 291, 91))
        font6 = QFont()
        font6.setFamilies([u"Segoe Print"])
        font6.setPointSize(28)
        font6.setBold(False)
        font6.setItalic(False)
        self.statusLabel.setFont(font6)
        self.statusLabel.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"font: 28pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.okPushButton = QPushButton(self.centralwidget)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setGeometry(QRect(600, 350, 171, 91))
        self.okPushButton.setFont(font3)
        self.okPushButton.setStyleSheet(u"background-color: rgb(140, 51, 85);\n"
"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/pictures/uiPictures/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.okPushButton.setIcon(icon7)
        self.okPushButton.setIconSize(QSize(32, 32))
        self.keyReturnBarcodeLineEdit = QLineEdit(self.centralwidget)
        self.keyReturnBarcodeLineEdit.setObjectName(u"keyReturnBarcodeLineEdit")
        self.keyReturnBarcodeLineEdit.setEnabled(True)
        self.keyReturnBarcodeLineEdit.setGeometry(QRect(430, 350, 121, 31))
        self.keyReturnBarcodeLineEdit.setFont(font)
        self.keyReturnBarcodeLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.keyReturnBarcodeLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 510, 191, 121))
        font7 = QFont()
        font7.setPointSize(20)
        self.label.setFont(font7)
        self.label.setPixmap(QPixmap(u"uiPictures/auto.png"))
        self.statusFrame = QFrame(self.centralwidget)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setGeometry(QRect(40, 130, 531, 401))
        self.statusFrame.setFrameShape(QFrame.Shape.Box)
        self.statusFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.statusFrame.setLineWidth(4)
        self.avalablePlainTextEdite = QPlainTextEdit(self.statusFrame)
        self.avalablePlainTextEdite.setObjectName(u"avalablePlainTextEdite")
        self.avalablePlainTextEdite.setGeometry(QRect(20, 60, 221, 321))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        self.avalablePlainTextEdite.setFont(font8)
        self.avalablePlainTextEdite.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.avalablePlainTextEdite.setFrameShape(QFrame.Shape.NoFrame)
        self.avalablePlainTextEdite.setFrameShadow(QFrame.Shadow.Plain)
        self.avalablePlainTextEdite.setLineWidth(8)
        self.plainTextEdit_2 = QPlainTextEdit(self.statusFrame)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(300, 60, 201, 261))
        self.plainTextEdit_2.setFont(font8)
        self.plainTextEdit_2.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.plainTextEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.plainTextEdit_2.setLineWidth(8)
        self.line = QFrame(self.statusFrame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(250, 0, 20, 401))
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.availableLabel = QLabel(self.statusFrame)
        self.availableLabel.setObjectName(u"availableLabel")
        self.availableLabel.setGeometry(QRect(50, 10, 101, 31))
        self.availableLabel.setFont(font3)
        self.inUseLabel = QLabel(self.statusFrame)
        self.inUseLabel.setObjectName(u"inUseLabel")
        self.inUseLabel.setGeometry(QRect(340, 10, 101, 31))
        self.inUseLabel.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 781, 33))
        self.menubar.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        self.menuTiedosto = QMenu(self.menubar)
        self.menuTiedosto.setObjectName(u"menuTiedosto")
        self.menuEdelliset = QMenu(self.menuTiedosto)
        self.menuEdelliset.setObjectName(u"menuEdelliset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font9 = QFont()
        font9.setPointSize(9)
        self.statusbar.setFont(font9)
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
        self.goBackPushButton.setText(QCoreApplication.translate("MainWindow", u"KUMOA", None))
        self.soundOnPushButton.setText("")
        self.soundOffPushButton.setText("")
        self.lenderNameLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaajan nimi", None))
        self.carInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki ja malli", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Auton Lainaus", None))
        self.okPushButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.keyReturnBarcodeLineEdit.setText("")
        self.keyReturnBarcodeLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avain", None))
        self.label.setText("")
        self.avalablePlainTextEdite.setPlainText(QCoreApplication.translate("MainWindow", u"Vapaat ajaneuvot\n"
"XSE-778 Toyota BZ4X 5 henkill\u00f6\u00e4\n"
"XYZ-123 VW Transtporter 3 henkil\u00f6\u00e4", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Ajossa:\n"
"XAm-15 Renault Megane 5 henkil\u00f6\u00e4", None))
        self.availableLabel.setText(QCoreApplication.translate("MainWindow", u"VAPAANA", None))
        self.inUseLabel.setText(QCoreApplication.translate("MainWindow", u"AJOSSA", None))
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menuEdelliset.setTitle(QCoreApplication.translate("MainWindow", u"Edelliset", None))
    # retranslateUi

