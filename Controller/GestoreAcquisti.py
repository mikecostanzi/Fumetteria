from Database.Connection import connection
class GestoreAcquisti:
    table = '''
        Acquisto()
    '''
    def __init__(self):
        super(GestoreAcquisti).__init__()
        self.lista = []
        try:
            self.db = connection()
            self.cur = self.db.cursor()
            self.cur.execute(f'CREATE TABLE IF NON EXISTS {self.table}')
        except Exception as m:
            print(m)

    def nuovo_acquisto(self):
        pass
    def ricerca_acquisti(self):
        pass