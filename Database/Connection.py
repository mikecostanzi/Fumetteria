import pymysql
'''''''''
class Connection:
    def __init__(self):
        super(Connection).__init__()
        self.connection()
'''
def connection():
    try:
        conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="NicolA380!",
                    database="GestioneFumetteria"
            )
        print('Database is Connected!')
        return conn
    except Exception as m:
        print(m)
