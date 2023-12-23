import psycopg2 as y

conn_params = {
    'dbname': 'maram',
    'user': 'postgres',
    'password': 'fatma95356658',
    'host': '127.0.0.1',
    'port': '5432'
}

conn = y.connect(**conn_params)
cursor = conn.cursor()

sql = 'SELECT * FROM personne'
cursor.execute(sql)

for row in cursor:
    print('=================')
    for value in row:
        print(value)


