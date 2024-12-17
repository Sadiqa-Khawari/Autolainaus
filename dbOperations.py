# MODUULI POSTGRESQL TIETOKANTAPALVELIMEN KÄYTTÄMISEEN
# ====================================================

# KIRJASTOT JA MODUULIT
# ---------------------

# Ladattavat kirjastot
import psycopg2

# Sisäiset kirjastot
import json

# Omat moduulit
import cipher


# LUOKAT
# ------

class DbConnection():
    """A class to crate PostgreSQL Database connections and various data operations"""
    
    # Konstruktori
    def __init__(self, settings: dict):
        self.server = settings['server']
        self.port = settings['port']
        self.databaseName = settings['database']
        self.userName = settings['userName']
        self.password = settings['password']

        # Yhteysmerkkijono
        self.connectionString =f'dbname={self.databaseName} user={self.userName} password={self.password} host={self.server} port={self.port}'
        
    # Metodi tietojen lisäämiseen (INSERT)
    def addToTable(self, table: str, data: dict) -> None:
        """Inserts a record (row) to a table according to a dictionary
        containing field names (columns) as keys and values

        Args:
            table (str): Name of the table
            data (dict): Field names and values
        """

        # Muodostetaan lista sarakkeiden (kenttien) nimistä ja arvoista SQL laustetta varten
        keys = data.keys() # Luetaan sanakirjan avaimet
        columns = '' # SQL-lauseeseen tarvittava sarakemerkkijono
        values = '' # SQL-lauseen arvot merkkijonona

        # Luetaan kaikki avaimet sekä arvot ja lisätään ne listoihin
        for key in keys:
            columns += key + ', ' # Lisätään pilkku
            rawValue = data[key] # Luetaan sanakirjan arvo

            # Lisätään puolilainausmerkit, jos kyseessä on merkkijono
            if isinstance(rawValue, str):
                value = f'\'{rawValue}\'' # \' mahdollistaa puolilainausmerkin lisäämisen
            else:
                value = f'{rawValue}'
            values += value + ', ' # Lisätään arvo sekä pilkku ja välilyönti

        # Poistetaan sarakkeista ja arvoista viimeinen pilkku ja välilyönti
        columns = columns[:-2]
        values = values[:-2]

        # Määritellään tilaviestiksi tyhjä merkkijono
        message = ''

        # Yritetään avata yhteys tietokantaan ja lisätä tietue
        try:
            # Luodaan yhteys tietokantaan
            currentConnection = psycopg2.connect(self.connectionString)

            # Luodaan kursori suorittamaan tietokantoperaatiota
            cursor = currentConnection.cursor()

            # Määritellään lopullinen SQL-lause
            sqlClause = f'INSERT INTO {table} ({columns}) VALUES ({values})'
            
            # Suoritetaan SQL-lause
            cursor.execute(sqlClause)

            # Vahvistetaan tapahtuma (transaction)
            currentConnection.commit()

        # Jos tapahtuu virhe, välitetään se luokkaa käyttävälle ohjelmalle
        except (Exception, psycopg2.Error) as e:
            raise e 
        finally:

            # Selvitetään muodostuiko yhteysolio
            if currentConnection:
                cursor.close() # Tuhotaan kursori
                currentConnection.close() # Tuhotaan yhteys
                
    # TODO: Tee metodi tietojen lukemisen taulun kaiki sarakkeet
    def readAllColumnsFromTable(self, table: str) -> list | None:
        """Returns all columns and rows from a table

        Args:
            table (str): Name of the table

        Returns:
            list: List of tuples. One tuple contains a row 
        """
        records = []
        # Yritetään avata yhteys tietokantaan lisätä tietue
        try:
            # Luodaan yhteys tietokantaan
            currentConnection = psycopg2.connect(self.connectionString)

            # Luodaan kursori suorittamaan tietokantoperaatiota
            cursor = currentConnection.cursor()
           

            sqlClause = f"SELECT * FROM {table})"
                                   
            # Suoritetaan SQL-lause 
            cursor.execute(sqlClause)

            records = cursor.fetchall()

            return records

        # Jos tapahtuu virhe, välitetään
        except (Exception, psycopg2.Error) as e:
            raise e
        finally:
            
            # Selvitetään muodostuiko yhteysolio
            if currentConnection:
                cursor.close() # Tuhotaan kursori
                currentConnection.close() # Tuotaan yhteys
        
    #  Tee metodi tietojen lukemisen taulun valitut sarakkeet
    def readColumnsFromTable(self, table: str, columns: list) -> list:
        """Returns all rows from a table. Columns are defind for the result set 

        Args:
            table (str): Name of the table
            colums (list): Column names to include in the result set

        Returns:
            list: List of tuples. One tuple contains a row 
        """
        # Yritetään avata yhteys tietokantaan lisätä tietue
        try:
            # Luodaan yhteys tietokantaan
            currentConnection = psycopg2.connect(self.connectionString)

            # Luodaan kursori suorittamaan tietokantoperaatiota
            cursor = currentConnection.cursor()

            # Muodostetaan sarakelistasta merkkijono
            columnString = ""
            for column in columns:
                columnString = columnString + str(column) + ", "
                
            cleandedColumnString = columnString[:-2]
           

            sqlClause = f"SELECT {cleandedColumnString} FROM {table})"


         
            cursor.execute(sqlClause)
            records = cursor.fetchall()
            return records

        # Jos tapahtuu virhe, välitetään
        except (Exception, psycopg2.Error) as e:
            raise e
        
        finally:
            
            # Selvitetään muodostuiko yhteysolio
            if currentConnection:
                cursor.close() # Tuhotaan kursori
                currentConnection.close() # Tuotaan yhteys

    # TODO:Tee metodi tietojen muokkamiseen
    def mname(self, table, clumn, criteriaClumn, criteriaValue):
        pass

    # TODO:Tee metodi tietojen poisamisen
    def deleterRawsFromTable(self, table, criteriaCloumn, criteriavalue):
        pass
        
if __name__ == "__main__":
    
    testDictionary ={"server": "localhost",
                     "port": "5432",
                     "database": "autolainaus",
                     "userName": "autolainaus",
                     "password": "Q2werty"}
    
    tableDictionary = {"Etunimi": "Uolevi",
                       "Sukunimi": "Untamo"}
    
    
    dbConnection = DbConnection(testDictionary)

    print("Yhteysmerkkijono on:", dbConnection.connectionString)

    #dbConnection.addToTable("testitaulu", tableDictionary)
    recordSet = dbConnection.readAllColumnsFromTable("ryhma")
    print("Ryhmät ovat ", recordSet)

    recordSet2 = dbConnection.readColumnsFromTable("ryhmat", ["ryhma", "vastahenkilo"])
    print("Vastahenkilöt ovat ", )
    
    recordSet3 = dbConnection.readColumnsFromTable("ryhma", ["vastuuhenkilo"])
    print("Ryhmät ja vastuuhenkilöt ovat: ", recordSet3)
