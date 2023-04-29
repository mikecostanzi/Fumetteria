from Database.Connection import connection
from Model.Fumetto import Fumetto
import os.path
import pymysql

class GestoreFumetti():
    table =  """
        Fumetto(barcode INTEGER NOT NULL PRIMARY KEY,
        titolo varchar(40),
        categoria varchar(20),
        distributore varchar(20),
        editore varchar(20),
        collana int,
        sottocollana int,
        prezzo decimal(4,2) not null,
        quantita int)
        """
    def __init__(self):
        super(GestoreFumetti).__init__()
        try:

            self.db = connection()
            self.cur = self.db.cursor()
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}")

        except Exception as m:
            print("Errore nella connessione del database")
            print(m)

    def inserisci_fumetto(self,barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita):
        with self.db.cursor() as cursor:
            query = """
                    INSERT INTO Fumetto(barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            data = (barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
            cursor.execute(query,data)
            self.db.commit()
    def ricerca(self,barcode):
        with self.db.cursor() as cursor:
            query = """
                select * 
                from Fumetto as f
                where f.barcode = %s
            """
            data = barcode
            cursor.execute(query,data)
            self.fumetto = cursor.fetchall()
            if self.fumetto:
                return self.fumetto

    def elimina_fumetto(self,barcode):
        with self.db.cursor() as cursor:
            query= '''
                delete 
                from Fumetto as t
                where t.barcode = %s
            '''
            data = barcode
            cursor.execute(query,data)
            self.db.commit()


    def modifica_quantita(self,barcode,quantita):
        with self.db.cursor() as cursor:
            query = '''
                update Fumetto
                set quantita = %s
                where barcode = %s
            '''
            data = (quantita,barcode)
            cursor.execute(query,data)
            self.db.commit()

