import pandas as x
import psycopg2 as y
def Extract(type,path):
  if type == 'csv':
    data = x.read_csv(path)
  elif type == 'xlsx':
        data = x.read_excel(path)
  else:
     conn = y.connect(path)
     cursor = conn.cursor()
     sql = 'SELECT * FROM personne'
     cursor.execute(sql)
     data=cursor.fetchall()
     conn.close()
  return data
print (Extract('csv','C:/monprojet/bi/data/iris.csv'))
print (Extract('xlsx','C:/monprojet/bi/data//test.xlsx'))
print (Extract('bd','dbname=maram user=postgres password=fatma95356658 host=127.0.0.1 port=5432'))


