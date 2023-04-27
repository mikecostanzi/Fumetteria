from Database.Connection import connection

class GestoreStatistiche:
    def __init__(self):
        self.db = connection()
        print(f'Il numero di tesserati totali è: {self.prima_statistica}\n')
        print()
    def prima_statistica(self):
        with self.db.cursor() as cursor:
            query = '''
                select count(t.codice) as numero_tesserati
                from Tessera as t
            '''
            cursor.execute(query)
            numero_tesserati = cursor.fetchone()

            return numero_tesserati[0]
    def seconda_statistica(self,data):
        with self.db.cursor() as cursor:
            stringa = f'{data}%'
            query = '''
                select sum(a.importo_totale) as totale
                from Acquisto as a
                where a.data_acquisto like %s;
            '''
            cursor.execute(query,stringa)
            totale = cursor.fetchall()
            return totale
    def terza_statistica(self):
        with self.db.cursor() as cursor:
            query = '''
            select count(f.barcode) as numero_dc_acquistati
            from Fumetto as f join FumettiAcquistati as fa on f.barcode = fa.barcode
            where f.editore = 'Dc';
            '''
            cursor.execute(query)
            numero = cursor.fetchone()

            return numero[0]
    def quarta_statistica(self):
        with self.db.cursor() as cursor:
            query = '''
            select count(f.barcode) as numero_dc_acquistati
            from Fumetto as f join FumettiAcquistati as fa on f.barcode = fa.barcode
            where f.editore = 'Marvel';
            '''
            cursor.execute(query)
            numero = cursor.fetchone()

            return numero[0]
