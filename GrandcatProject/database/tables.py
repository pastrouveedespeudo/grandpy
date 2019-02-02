class table:

    def create_table_category(self):
        """This is category table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS echange (

            id_categorie INT UNSIGNED NOT NULL AUTO_INCREMENT,
            echange TEXT NOT NULL,
            dateHeure DATETIME NOT NULL,
    
            PRIMARY KEY(id_categorie) )

            ENGINE=InnoDB;

            """)
