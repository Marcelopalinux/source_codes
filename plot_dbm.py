import matplotlib.pyplot as plt
import pyodbc

try:
    cnxn = pyodbc.connect("DSN=BANCOFORUM")
    cursor = cnxn.cursor()
    cursor.execute("select id_estado as 'UF',count(id_estado) from loja.cep group by id_estado order by 2 desc")
    rows = cursor.fetchall()
except:
    print('error')

x = []
y = []

for i in range(len(rows)):
    x.append(rows[i][0])
    y.append(rows[i][1])
plt.rcParams.update({'font.size':5})
plt.bar(x,y,align="center",color="r",width=0.9)
#plt.scatter(x,y,color="y",linewidths=0.1)
plt.title("Ceps por Estado")
#capturar valor largura e altura da saida
fig_size = plt.rcParams["figure.figsize"]

# aumentar o valor
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size

#plt.show()
plt.savefig('c:/tb/ceps_por_estado.pdf', format='pdf',orientation='landscape')

