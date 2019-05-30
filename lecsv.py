import csv
'''
leitura do CSV fazendo um loop 
encoding = UTF-8 ( importante para algumas regioes e tipos de caracter ) 
alimentando uma lista e capturando nome + sobrenome + email 
'''

#data = open('c:/tb/download_link.csv', encoding='utf-8')
data = open('c:/tb/example.csv', encoding='utf-8')
csvdata = csv.reader(data)
datalines = list(csvdata)
dados_user = []
for i in datalines[1:]:
  #  print(i)
    email = i[3]
    nome = i[1]
    sobrenome = i[2]
    dados_user.append(nome + ' ' + sobrenome + ' ' + email)
print(dados_user)
