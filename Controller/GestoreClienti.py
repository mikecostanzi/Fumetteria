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
                if codice == '':
                    codice = None

                query = '''
                    INSERT INTO Cliente(id,nome,cognome,indirizzo,telefono,email,codice)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                '''
                data = (id,nome,cognome,indirizzo,telefono,email,codice)
                cursor.execute(query,data)
                self.db.commit()
        except Exception as m:
            print('Query non andata a buon fine ' + m)
    def ricerca_cliente(self,id):
        try:
            with self.db.cursor() as cursor:
                query = '''
                    select *
                    from Cliente as c
                    where c.id = %s
                '''
                cursor.execute(query,id)
                self.cliente = cursor.fetchall()
                print(self.cliente)
                if self.cliente:
                    return self.cliente
        except Exception as m:
            print('Query non andata a buon fine' + m)

    def elimina_cliente(self,id):
        with self.db.cursor() as cursor:
            query = '''
                delete from Cliente as c
                where c.id = %s
            '''
            cursor.execute(query,id)
            self.db.commit()
    def modifica_codice(self,id,codice):
        with self.db.cursor() as cursor:
            query = '''
                update Cliente 
                set codice = %s
                where id = %s
            '''
            data = (codice,id)
            cursor.execute(query,data)
            self.db.commit()

    def modifica_nome(self, id, nome):
        with self.db.cursor() as cursor:
            query = '''
                update Cliente 
                set nome = %s
                where id = %s
            '''
            data = (nome, id)
            cursor.execute(query, data)
            self.db.commit()

    def modifica_cognome(self, id, cognome):
        with self.db.cursor() as cursor:
            query = '''
                update Cliente 
                set cognome = %s
                where id = %s
            '''
            data = (cognome, id)
            cursor.execute(query, data)
            self.db.commit()

    def modifica_indirizzo(self, id, indirizzo):
        with self.db.cursor() as cursor:
            query = '''
                update Cliente 
                set indirizzo = %s
                where id = %s
            '''
            data = (indirizzo, id)
            cursor.execute(query, data)
            self.db.commit()

    def modifica_telefono(self, id, telefono):
        with self.db.cursor() as cursor:
            query = '''
                update Cliente 
                set telefono = %s
                where id = %s
            '''
            data = (telefono, id)
            cursor.execute(query, data)
            self.db.commit()

    def modifica_email(self, id, email):
        with self.db.cursor() as cursor:
            query = '''
                update Cliente 
                set email = %s
                where id = %s
            '''
            data = (email, id)
            cursor.execute(query, data)
            self.db.commit()


