import pymysql
from Database.Connection import connection

class GestoreClienti():
    table= '''
    Cliente(
    id integer not null primary key ,
    nome varchar(40),
    cognome varchar(40),
    indirizzo varchar(40),
    telefono varchar(20),
    email varchar(40),
    codice integer,
    foreign key (codice) references Tessera(codice)
    )
    '''

    def __init__(self):
        super(GestoreClienti).__init__()
        self.lista = []
        try:
            self.db = connection()
            self.cur = self.db.cursor()
            self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table}')
        except Exception as m:
            print('Database non connesso' + m)

    def inserisci_cliente(self,id,nome,cognome,indirizzo,telefono,email,codice):
        try:
            with self.db.cursor() as cursor:
                query = '''
                    INSERT INTO Cliente(id,nome,cognome,indirizzo,telefono,email,codice)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                '''
                data = (id,nome,cognome,indirizzo,telefono,email,codice)
                cursor.execute(query,data)
                self.db.commit()
        except Exception as m:
            print('Query non andata a buon fine ' + m)