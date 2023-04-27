from Database.Connection import connection
class GestoreBackup:
    def __init__(self):
        self.db = connection()


    def b_fumetti(self):
        with self.db.cursor() as cursor:
            query = '''
                select *
                from Fumetto;
            '''
            cursor.execute(query)
            fumetti = cursor.fetchall()
            try:
                file = open('../Sistema/fumetti.txt','a')
                file.write(f'{fumetti}')
                file.close()
                print(str(fumetti))
            except Exception as m:
                print(type(m))
    def b_clienti(self):
        with self.db.cursor() as cursor:
            query = '''
                select *
                from Cliente;
            '''
            cursor.execute(query)
            clienti = cursor.fetchall()
            try:
                file = open('../Sistema/clienti.txt','a')
                file.write(f'{clienti}')
                file.close()
                print(str(clienti))
            except Exception as m:
                print(m)

    def b_tessere(self):
        with self.db.cursor() as cursor:
            query = '''
                select *
                from Tessera;
            '''
            cursor.execute(query)
            tessere = cursor.fetchall()
            try:
                file = open('../Sistema/tessere.txt', 'a')
                file.write(f'{tessere}')
                file.close()
                print(str(tessere))
            except Exception as m:
                print(m)

    def b_acquisti(self):
        with self.db.cursor() as cursor:
            query = '''
                select *
                from Acquisto;
            '''
            query2 = '''
                select *
                from FumettiAcquistati;
            '''
            cursor.execute(query)
            acquisti = cursor.fetchall()
            cursor.execute(query2)
            fumetti_acquistati = cursor.fetchall()
            try:
                file = open('../Sistema/acquisti.txt', 'a')
                file.write(f'{acquisti}')
                file.close()
                file2 = open('../Sistema/fumetti-acquistati.txt','a')
                file2.write(f'{fumetti_acquistati}')
                file2.close()
                print(str(acquisti)+'\n'+str(fumetti_acquistati))
            except Exception as m:
                print(type(m))

