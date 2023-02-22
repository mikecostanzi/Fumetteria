from Database.Connection import connection
from Model.Fumetto import Fumetto
import os.path
import pymysql

class GestoreFumetti():
    table = [
        """
        Fumetto(barcode INTEGER NOT NULL PRIMARY KEY,
        categoria varchar[20],
        distributore varchar[20],
        editore varchar[20],
        collana int,
        sottocollana int,
        prezzo decimal(4,2) not null,
        quantita int)
        """
    ]
    def __init__(self):
        super(GestoreFumetti).__init__()
        try:
            db = pymysql.connect(connection())
            self.cur = db.cursor()
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}")

        except Exception as m:
            print("Database non connesso")
            print(m)

    def inserisci_fumetto(self,barcode,categoria,distributore,editore,collana,sottocollana,prezzo,quantita):
        try:
            with self.db.cursor() as cursor:

                query = """
                    INSERT INTO Fumetto(barcode,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """
                data = (barcode,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
                cursor.execute(query,data)
                self.db.commit()

        except Exception as m:
            print("Query fumetto non andato a buon fine")
            print(m)