
import os.path
import pymysql
from Model.Tessera import Tessera


class GestoreTessera(Tessera):

    table = [
        """Cliente( 
        idCliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome char[20] not null,
        cognome char[20] not null,
        dataNascita """
    ]

    def __init__(self,path):
        if not os.path.exists(path):
            self.dbb = pymysql.connect(path)
            self.cur = self.dbb.cursor()
            self.cur.execute(f"CREATE TABLE {self.table}")
