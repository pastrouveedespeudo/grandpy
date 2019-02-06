# -*- coding: utf-8 -*-

import mysql.connector
from config import *

class Mysql_connexion:
    """Here we make data Mysql"""


    def database(self):
        """We creating database pur_beurre"""

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER)
                                                 

        self.cursor = self.connexion.cursor()

        user = USER

        self.cursor.execute("""
        CREATE DATABASE grandpy""")
 
    def connexion(self):
        """We establish connexion with database with jbaw users"""

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 database=DATABASE)
        self.cursor = self.connexion.cursor()

        user = USER
        self.cursor.execute("""
        USE grandpy""")
