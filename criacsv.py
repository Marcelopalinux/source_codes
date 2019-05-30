import pyodbc,csv
'''
este simples programa faz leitura de um banco de dados e cria um arquivo CSV
com resultado da query 
delimitador utilizado = ','
os passos para criar o arquivo estão abaixo
'''

cnxn = pyodbc.connect("DSN=BANCOFORUM")
cursor = cnxn.cursor()
cursor.execute("select * from loja.cep limit 1000")
rows = cursor.fetchall()
arquivo_novo = open("arquivo_novo.csv",'w',newline='')
new_file = csv.writer(arquivo_novo,delimiter=',')
for i in rows:
    new_file.writerow(i)
arquivo_novo.close()
