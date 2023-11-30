from psycopg2 import connect, extras


host = 'localhost'
port = 5432
dbname = 'MaratonesUD'
user = 'postgres'
password = 'Lau.cubillos1234'

def get_connection():
    conn= connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn