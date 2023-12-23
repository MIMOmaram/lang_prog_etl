import pandas as pd
data = pd.read_excel('C:/monprojet/bi/data//test.xlsx')
print(data)
for i in data:
   print(i)
   print(data['Commande'])
