class table:

    def create_table_message(self):
        """This is category table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS message (

            id_message INT UNSIGNED NOT NULL AUTO_INCREMENT,
            message TEXT NOT NULL,
            dateHeure DATETIME NOT NULL,
            utilisateur VARCHAR(50),
    
            PRIMARY KEY(id_message) )

            ENGINE=InnoDB;

            """)

        #ajouter utilisateur
