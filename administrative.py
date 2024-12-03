# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json 

from PySide6 import QtWidgets # Qt-vimpaimet
from administrative_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka
from settingsDialog_ui import Ui_Dialog # Asetukset-dialogin luokka

#
import cipher

# LUOKKA

#
# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
     # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        #Asetukset-valikon muokkaa toiminto avaa Asetukset-dialogi-ikkunan
        self.ui.actionMuokkaa.triggered.connect(self.openSettingsDialog)
        

        
   
   
    # OHJELMOIDUT SLOTIT
    # ------------------
    def openSettingsDialog(self):
        self.saveSettingsDialog = saveSettingsDialog()
        self.saveSettingsDialog.setWindowTitle("Palvelinasetukset")
        self.saveSettingsDialog.exec()
       



    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()



class saveSettingsDialog(QtWidgets.QDialog, Ui_Dialog):
    """A class to open settings dialog window"""
    def __init__(self):
        super().__init__


        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

                # Avain on luotu cipher.py 
        self.secretKey = b'CFACIiGZo4qEYYuSvS4a4T--PgWTzBRl4aYjqrnxZj8='
        self.cryptoEngine = cipher.createChipher(self.secretKey)

        # Luetaan asetustiedosto Python-sanakirjaksi
        self.currentSettings = {}

        # Tarkistetaan ensin, että asetustiedosto on olemassa
        try: 
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.serverLineEdit.setText(self.currentSettings['server'])
            self.ui.portLineEdit.setText(self.currentSettings['port'])
            self.ui.databaseLineEdit.setText(self.currentSettings['database'])
            self.ui.userLineEdit.setText(self.currentSettings['userName'])
            self.ui.paswordLineEdit.setText(self.currentSettings['password'])
        except Exception as e:
            self.openInfo()

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        # Kun Tallenna-painiketta on klikattu, kutsutaan saveToJsonFile-metodia
        self.ui.saveSettingspushButton.clicked.connect(self.saveToJsonFile)



    # Tallennetaan käyttöliittymään syötetyt asetukset tiedostoon
    def saveToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.serverLineEdit.text()
        port = self.ui.portLineEdit.text()
        database = self.ui.databaseLineEdit.text()
        userName = self.ui.userLineEdit.text()

        # Muutetaan merkkijono tavumuotoon (byte, merkistä UTF-8)
        plainTextPassword = bytes(self.ui.paswordLineEdit.text(), "utf-8")

        # Salataan ja muunetaan tavalliseksi merkijonoksi, jotta JSON-tallennus onnisto
        encryptedPassword = str(cipher.encrypt(self.cryptoEngine, plainTextPassword))

        
        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName,
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)
        
        # Avataan asetustiedosto ja kirjoitetaan asetukset
        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)


    # Avataan MessageBox
    def openInfo(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Luodaaan uusi asetustiedosto')
        msgBox.setText('Syötä kaikkien kenttien tiedot')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
       



if __name__ == "__main__":
    
    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()

    