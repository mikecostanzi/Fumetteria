from Database.Connection import Connection
from Model.Fumetto import Fumetto
import os.path
import pymysql

class GestoreFumetti():
    table = [
        """
        Fumetto(
        barcode INTEGER NOT NULL PRIMARY KEY,
        categoria char[20],
        distributore char[20],
        editore char[20],
        collana int,
        sottocollana int,
        prezzo decimal(4,2) not null,
        quantita int)
        """
    ]
    def __init__(self):
        super(GestoreFumetti).__init__()
        connessione = Connection()

        try:
            db = pymysql.connect(connessione.connection())
            self.cur = db.cursor()
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}")
        except Exception as m:
            print("Database non connesso")
            print(m)
    def inserisci_fumetto(self,barcode,categoria,distributore,editore,collana,sottocollana,prezzo,quantita):
        try:
            with self.db.cursor() as cursor:
                query = f"""
                    INSERT INTO Fumetto(barcode,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
                    VALUES ({barcode},{categoria},{distributore},{editore},{collana},{sottocollana},{prezzo},{quantita})
                """
                cursor.execute(query)
                self.db.commit()
        except Exception as m:
            print("Query fumetto non andato a buon fine")
            print(m)