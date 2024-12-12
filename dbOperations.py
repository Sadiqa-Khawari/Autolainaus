# MODUULI POSTGRESQL TIETOKANTAPALVELIMEN KÄYTTÄMISEEN
# ====================================================

# kIRJASTOT JA MODUULIT
# ---------------------

# Ladattavat kirjostot
import psycopg2

# Sisäiset kirjastot
import json

# Omat moduulit
import cipher


# LUOKAT
# ------

class DbConnection():
    """A class to create PostgreSQL bDatabase connection and various date operations"""

    # Konstruktori
    def __init__(self, settings: dict):      
        self.server = settings["server"]
        self.port = settings["port"]
        self.databaseName = settings["database"]
        self.userName = settings["userName"]
        self.password = settings["password"]

        # Yhteysmerkkijono
        self.connectionString = f'dbname={self.databaseName}, user={self.userName}, password={self.password}, server={self.server}, port={self.port}'
        

        print("Yhteysmerkkijono on :", self.connectionString)
    # Metodi tietojen lisäämiseen (INSERT)
    def addToTable(self, table: str, data: dict) -> str:
        """Inserts a record (row) tothe a table according to a dictionary
        containing field names (columns) as keys and values

        Args:
            table (str): Name of the table
            data (dict): Field names and values

        Returns:
            str: Information about successfull operation or an error massage
        """

        # Muodostetaan lista sarakkeiden (kenttien) nimistä ja arvoista SQL laustetta varten
        keys = data.keys() # Luoetaan sanakirjan avaimet
        columns = "" # SQL- lauseseen tarvittava sarakemerkkijono
        values = "" # SQL-lauseen arvot merkkijono

        # Luotaan kaikki avaimet sekä arvo ja lisätään 
        for key in keys:
            columns += key + ", " # Lisätään pilkku
            rawValue = data[key] # Luetaan sanakirja

            # Lisätään puolilainausmerkit, jos kyseessä on merkkijono
            if isinstance(rawValue, str):
                value = f"\"{rawValue}\"" # \" mahdollistaa puolilainausmerkkin lisäämisen
            else:
                value = rawValue
            values += value + ", " # Lisätään arvo sekä pilkku ja välily

        # Poistetaan sarakkeista ja arvoista viimeinen pilkko ja välilyönti
        columns = columns[:-2]
        values = values[:-2]

        # Määritrllään tilavie
        message = ""

        # Yritetään avata yhteys tietokantaan lisätä tietue
        try:
            # Luodaan yhteys tietokantaan
            currentConnection = psycopg2.connect(self.connectionString)

            # Luodaan kursori suorittamaan tietokantoperaatiota
            cursor = currentConnection.cursor()
           

            sqlClause = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            print("SQL-lause on: ", sqlClause)
                        
            # Suoritetaan SQL-lause 
            cursor.execute(sqlClause)

            # Vahvistetaan tapahtuma (transaction)
            currentConnection.commit()

        except (Exception, psycopg2.Error) as e:
            message = "Tietokantayhteyden muodostamisessa tapahtui virhe: " + str(e)
            
        finally:
            if message == "":
                message = f"Tietua lisättiin tauluun {table}"

            # Selvitetään muodostuiko yhteysolio
            if currentConnection:
                cursor.close() # Tuhotaan kursori
                currentConnection.close() # Tuotaan yhteys

            return message
        
if __name__ == "__main__":
    
    testDictionary ={"server": "127.0.0.1",
                     "port": "5432",
                     "database": "testi",
                     "userName": "user",
                     "password": "salasana"}
    
    tableDictionary = {"Etunimi": "Uolevi",
                       "Sukunimi": "Untamo"}
    
    
    dbConnection = DbConnection(testDictionary)

    print("Yhteysmerkkijono on:", dbConnection.connectionString)

    dbConnection.addToTable("testitaulu", tableDictionary)
    