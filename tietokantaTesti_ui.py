# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tietokantaTesti.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import testPictures_rc
import autoPicture_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1063, 767)
        icon = QIcon()
        iconThemeName = u"emblem-shared"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(223, 32, 112);")
        self.actionLopeta = QAction(MainWindow)
        self.actionLopeta.setObjectName(u"actionLopeta")
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

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
        self.ssnLineEdit.setGeometry(QRect(90, 430, 161, 31))
        font = QFont()
        font.setPointSize(15)
        self.ssnLineEdit.setFont(font)
        self.ssnLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(32, 75, 70);")
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(20, 0, 91, 16))
        self.firstNameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.keyBarcodeLineEdit = QLineEdit(self.centralwidget)
        self.keyBarcodeLineEdit.setObjectName(u"keyBarcodeLineEdit")
        self.keyBarcodeLineEdit.setGeometry(QRect(380, 430, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Serif"])
        font1.setPointSize(15)
        self.keyBarcodeLineEdit.setFont(font1)
        self.keyBarcodeLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.keyBarcodeLineEdit.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.lastNameLabel = QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(150, 0, 49, 16))
        self.lastNameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(480, 50, 221, 101))
        self.returnCarPushButton.setFont(font)
        self.returnCarPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnCarPushButton.setToolTipDuration(3000)
        self.returnCarPushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.returnCarPushButton.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.studentPictureLabel = QLabel(self.centralwidget)
        self.studentPictureLabel.setObjectName(u"studentPictureLabel")
        self.studentPictureLabel.setGeometry(QRect(730, 50, 211, 231))
        self.studentPictureLabel.setPixmap(QPixmap(u":/png/student.png"))
        self.studentPictureLabel.setScaledContents(False)
        self.keyPictureLabel = QLabel(self.centralwidget)
        self.keyPictureLabel.setObjectName(u"keyPictureLabel")
        self.keyPictureLabel.setGeometry(QRect(370, 230, 201, 141))
        self.keyPictureLabel.setPixmap(QPixmap(u":/png/keys.png"))
        self.teacherPictureLabel = QLabel(self.centralwidget)
        self.teacherPictureLabel.setObjectName(u"teacherPictureLabel")
        self.teacherPictureLabel.setGeometry(QRect(40, 160, 211, 231))
        self.teacherPictureLabel.setPixmap(QPixmap(u"Teacher.png"))
        self.teacherPictureLabel.setScaledContents(False)
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(120, 470, 131, 31))
        font2 = QFont()
        font2.setPointSize(17)
        self.dateLabel.setFont(font2)
        self.Number = QLabel(self.centralwidget)
        self.Number.setObjectName(u"Number")
        self.Number.setGeometry(QRect(730, 350, 171, 121))
        self.Number.setPixmap(QPixmap(u":/auto/auto.png"))
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(80, 70, 221, 101))
        self.takeCarPushButton.setFont(font)
        self.takeCarPushButton.setStyleSheet(u"color: rgb(255, 255, 255); \n"
"color: rgb(0, 0, 0);\n"
"\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 570, 111, 41))
        self.minuteLCDNumber = QLCDNumber(self.centralwidget)
        self.minuteLCDNumber.setObjectName(u"minuteLCDNumber")
        self.minuteLCDNumber.setGeometry(QRect(420, 470, 65, 51))
        self.minuteLCDNumber.setLineWidth(1)
        self.minuteLCDNumber.setMidLineWidth(0)
        self.minuteLCDNumber.setDigitCount(2)
        self.minuteLCDNumber.setProperty(u"intValue", 24)
        self.hourLCDNumber = QLCDNumber(self.centralwidget)
        self.hourLCDNumber.setObjectName(u"hourLCDNumber")
        self.hourLCDNumber.setGeometry(QRect(360, 470, 61, 51))
        self.hourLCDNumber.setDigitCount(2)
        self.hourLCDNumber.setProperty(u"intValue", 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1063, 21))
        self.menubar.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        self.menuTiedosto = QMenu(self.menubar)
        self.menuTiedosto.setObjectName(u"menuTiedosto")
        self.menuEdelliset = QMenu(self.menuTiedosto)
        self.menuEdelliset.setObjectName(u"menuEdelliset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font3 = QFont()
        font3.setPointSize(20)
        self.statusbar.setFont(font3)
        self.statusbar.setToolTipDuration(3000)
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
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Puhuttelunimi", None))
        self.keyBarcodeLineEdit.setText("")
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
#if QT_CONFIG(tooltip)
        self.returnCarPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Tallentaa henkil\u00f6n tiedot tietokantaa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.returnCarPushButton.setText(QCoreApplication.translate("MainWindow", u"palauta", None))
        self.studentPictureLabel.setText("")
        self.keyPictureLabel.setText("")
        self.teacherPictureLabel.setText("")
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"15.3.2024", None))
        self.Number.setText("")
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"LAINAA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menuEdelliset.setTitle(QCoreApplication.translate("MainWindow", u"Edelliset", None))
    # retranslateUi

