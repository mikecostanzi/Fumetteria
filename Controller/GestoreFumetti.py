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
        self.lista = []
        try:

            self.db = connection()
            self.cur = self.db.cursor()
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}")

        except Exception as m:
            print("Database non connesso")
            print(m)

    def inserisci_fumetto(self,barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita):
        try:
            with self.db.cursor() as cursor:

                query = """
                    INSERT INTO Fumetto(barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                data = (barcode,titolo,categoria,distributore,editore,collana,sottocollana,prezzo,quantita)
                cursor.execute(query,data)
                self.db.commit()
        except Exception as m:
            print("Query fumetto non andato a buon fine")
            print(m)
    def ricerca(self,barcode):
        print('---Inizio ricerca su database---')
        try:
            with self.db.cursor() as cursor:
                query = """
                    select * 
                    from Fumetto as f
                    where f.barcode = %s
                """
                data = barcode
                cursor.execute(query,data)
                self.fumetto = cursor.fetchall()
                print(self.fumetto)
                if self.fumetto:
                    return self.fumetto

        except Exception as m:
            print("Query ricerca non andato a buon fine")
            print(m)

    def elimina_fumetto(self,barcode):
        print('--- Inizio eliminazione su database ---')
        try:
            with self.db.cursor() as cursor:
                query= '''
                        delete 
                        from Fumetto as t
                        where t.barcode = %s
                '''
                data = barcode
                cursor.execute(query,data)
                self.db.commit()
                print('--- Fine eliminazione su database ---')
        except Exception as m:
            print("Query ricerca non andato a buon fine")
            print(m)

    def modifica_quantita(self,barcode,quantita):
        print('--- Inizio modifica quantità ---')
        try:
            with self.db.cursor() as cursor:
                query = '''
                        update Fumetto
                        set quantita = %s
                        where barcode = %s
                '''
                data = (quantita,barcode)
                cursor.execute(query,(data))
                self.db.commit()
            print('Fumetto modificato')
        except pymysql.err.ProgrammingError as m:
            print('Query modifica quantita non andato a buon fine')
            print(m)
            print(type(m))