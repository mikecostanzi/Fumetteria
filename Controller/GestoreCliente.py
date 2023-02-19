
import os.path
import pymysql

from Model.Cliente import Cliente
from Model.Tessera import Tessera
from Database.Connection import connection

class GestoreCliente(Cliente):

    table = [
        """Cliente( 
        idCliente INTEGER NOT NULL PRIMARY KEY,
        nome char[20] not null,
        cognome char[20] not null,
        dataNascita date not null,
        indirizzo char[20] not null,
        telefono char[10] not null,
        email char[20] not null
        )"""
    ]

    def __init__(self,path):
        if not os.path.exists(connection()):
            self.dbb = pymysql.connect(connection())
            self.cur = self.dbb.cursor()
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table}")
        else:
            self.dbb = pymysql.connect(connection())
            self.cur = self.dbb.cursor()

    def inserisci_Cliente(self,idCliente,nome,cognome,dataNascita,indirizzo,telefono,email):
        try:
            with self.dbb.cursor() as cursor:
                query = """INSERT INTO Cliente(idCliente,nome,cognome,dataNascita,indirizzo,telefono,email)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(query,(idCliente,nome,cognome,dataNascita,indirizzo,telefono,email))
                self.dbb.commit()
        except Exception as m:
            print(type(m))
            print(m)


