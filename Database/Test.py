import pymysql

# Connessione al database
conn = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='nome_database')

# Creazione di un nuovo record
def create_record(table, data):
    with conn.cursor() as cursor:
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(query, tuple(data.values()))
    conn.commit()

# Lettura dei record
def read_records(table, condition=None):
    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

# Aggiornamento di un record esistente
def update_record(table, data, condition):
    with conn.cursor() as cursor:
        update_columns = ', '.join([f"{k}=%s" for k in data.keys()])
        query = f"UPDATE {table} SET {update_columns} WHERE {condition}"
        cursor.execute(query, tuple(data.values()))
    conn.commit()

# Cancellazione di un record esistente
def delete_record(table, condition):
    with conn.cursor() as cursor:
        query = f"DELETE FROM {table} WHERE {condition}"
        cursor.execute(query)
    conn.commit()

# Chiusura della connessione al database
conn.close()
