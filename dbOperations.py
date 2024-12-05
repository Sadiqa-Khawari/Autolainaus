# MODUULI POSTGRESQL TIETOKANTAPALVELIMEN KÄYTTÄMISEEN
# ====================================================

# kIRJASTOT JA MODUULIT
# ---------------------

import psycopg2

# LUOKAT
# ------

class DbConnection():
    """A class to create PostgreSQL bDatabase connection and various date operations"""

    # Konstruktori
    def __init__(self, settings: dict):
        self.settings = settings        
        self.server = self.settings["server"]
        self.part = settings["part"]
        self.databaseName = settings["datebase"]
        self.userName = settings["username"]
        self.password = settings["password"]
