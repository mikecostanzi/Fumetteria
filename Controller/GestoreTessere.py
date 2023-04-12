import pymysql

from Database.Connection import connection


class GestoreTessere():
    table = """
        Tessera(
        codice INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        data_inizio date, 
        punti int)
    """

    def __init__(self):
        super(GestoreTessere).__init__()
        self.lista = []
        try:
            self.db = connection()
            self.cur = self.db.cursor()
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}")
        except Exception as m:
            print("Database non connesso, " + m)


    def inserisciTessera(self,codice, data_inizio, punti):
        try:
            with self.db.cursor() as cursor:
                query = """
                    INSERT INTO Tessera(codice,data_inizio, punti)
                    values (%s, %s, %s, %s)
                """
                data = (codice, data_inizio, punti)
                cursor.execute(query, data)
                self.db.commit()
        except Exception as m:
            print("Query tessera non andata a buon fine")
            print(m)

    def ricercaTessera(self, codice):
        print('---Inizio ricerca su database---')
        try:
            with self.db.cursor as cursor:
                query = """
                    select *
                    from Tessera as t
                    where t.codice = %s
                """
                data = codice
                cursor.execute(query, data)
                self.tessera = cursor.fetchall()
                print(self.tessera)
                if self.tessera:
                    return self.tessera

        except Exception as m:
            print("Query ricerca non andata a buon fine")
            print(m)

    def eliminaFumetto(self, codice):
        print('--- Inizio eliminazione su database ---')
        try:
            with self.db.cursor() as cursor:
                query = '''
                                delete 
                                from Tessera as t
                                where t.codice = %s
                        '''
                data = codice
                cursor.execute(query, data)
                self.db.commit()
                print('--- Fine eliminazione su database ---')
        except Exception as m:
            print("Query ricerca non andato a buon fine")
            print(m)

    def modifica_punti(self, codice, punti):
        print('--- Inizio modifica punti ---')
        try:
            with self.db.cursor() as cursor:
                query = '''
                        update Tessera
                        set punti = %s
                        where codice = %s
                '''
                data = (punti, codice)
                cursor.execute(query,(data))
                self.db.commit()
            print('Tessera modificata')
        except pymysql.err.ProgrammingError as m:
            print('Query modifica punti non andata a buon fine')
            print(m)