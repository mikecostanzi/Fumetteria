import pymysql

def connection():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="NicolA380!",
        database="GestioneFumetteria"
    )
    print('Database is Connected!')
    return conn