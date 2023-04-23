from Database.Connection import connection
class GestoreAcquisti:
    table_acquisto = '''
        Acquisto(
            codice INTEGER NOT NULL PRIMARY KEY,
            data_acquisto date,
            importo_totale decimal(4,2),
            punti int
        )
    '''
    table_fumetti_acquistati = '''
        FumettiAcquistati(
            codice int not null references Acquisto(codice),
            barcode int not null references Fumetto(barcode)
            
        )
    '''
    def __init__(self):
        super(GestoreAcquisti).__init__()
        self.lista = []
        try:
            self.db = connection()
            self.cur = self.db.cursor()
            self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table_acquisto}')
            self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table_fumetti_acquistati}')
        except Exception as m:
            print(m)

    def nuovo_acquisto(self,codice,data_acquisto):
        with self.db.cursor() as cursor:
            query = '''
                INSERT INTO Acquisto(codice,data_acquisto,importo_totale,punti)
                VALUES (%s,%s,NULL,NULL)
            '''
            data = (codice,data_acquisto)
            cursor.execute(query,data)
            self.db.commit()

    def inserisci_fumetti_acquistati(self,codice,barcode):
        with self.db.cursor() as cursor:
            query = '''
                INSERT INTO FumettiAcquistati(codice,barcode)
                values (%s,%s)
            '''
            data = (codice,barcode)
            cursor.execute(query,data)
            self.db.commit()
    def set_importo(self,codice):
        with self.db.cursor() as cursor:
            query_prezzo = '''
                select sum(f.prezzo)
                from Acquisto as a join FumettiAcquistati as fa on a.codice = fa.codice
                join Fumetto as f on f.barcode = fa.barcode
                where a.codice = %s;
            '''
            cursor.execute(query_prezzo,codice)
            self.prezzo = cursor.fetchall()
            query_importo = '''
                update Acquisto 
                set importo_totale = %s
                where codice = %s
            '''
            data_importo = (self.prezzo,codice)
            cursor.execute(query_importo,data_importo)
            self.db.commit()
    def set_punti(self,codice):
        with self.db.cursor() as cursor:
            query_count = '''
                select count(fa.barcode)
                from Acquisto as a join FumettiAcquistati as fa on a.codice = fa.codice
                join Fumetto as f on f.barcode = fa.barcode
                where a.codice = %s;
            '''
            cursor.execute(query_count,codice)
            self.punti = cursor.fetchall()
            query_punti = '''
                update Acquisto 
                set punti = %s
                where codice = %s
            '''
            data_punti = (self.punti,codice)
            cursor.execute(query_punti,data_punti)
            self.db.commit()
    def ricerca_acquisto(self,codice):
        with self.db.cursor() as cursor:
            query = '''
                select *
                from Acquisto as a
                where a.codice = %s;
            '''
            cursor.execute(query,codice)
            self.acquisto = cursor.fetchall()
            if self.acquisto:
                return self.acquisto

    def ricerca_fumetti_acquistati(self,codice):
        with self.db.cursor() as cursor:
            query = '''
                select f.barcode,f.titolo,f.categoria,f.distributore,f.editore,f.prezzo
                from Acquisto as a join FumettiAcquistati as fa on a.codice = fa.codice
                join Fumetto as f on f.barcode = fa.barcode
                where a.codice = %s;
            '''
            cursor.execute(query,codice)
            self.fumetto_acquistato = cursor.fetchall()
            print(self.fumetto_acquistato)
            if self.fumetto_acquistato:
                return self.fumetto_acquistato
