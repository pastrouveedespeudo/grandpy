# -*- coding: utf-8 -*-

"""Here we create database, tables and we inserting products"""

from tables import *            # We importing modules necessary to Mysql data

from Connexion import *

from config import *

class Lunching:
    """This is the first program to lunch for create our database"""

    def __init__(self):

 

        Mysql_connexion.database(self)

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 database=DATABASE)
        self.cursor = self.connexion.cursor()

        user = "root"

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)

        print("Database crée")


    def tables(self):
        """We creating Mysql tables"""

        table.create_table_message(self)


        print("Tables crées")





if __name__ == "__main__":

    lunch = Lunching()
    lunch.tables()
 
