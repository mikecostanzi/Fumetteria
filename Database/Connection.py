import pymysql

def connection():
    try:
        conn = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="admin",
                    database="GestioneFumetteria"
            )
        print('Database is Connected!')
        return conn
    except Exception as m:
        print(m)
