import matplotlib.pyplot as plt
import pyodbc

cnxn = pyodbc.connect("DSN=DBINTERON")
cursor = cnxn.cursor()

cursor.execute("select id_estado as 'UF',count(id_estado) from cep group by id_estado order by 2 desc")
rows = cursor.fetchall()
x = []
y = []

for i in range(len(rows)):
    x.append(rows[i][0])
    y.append(rows[i][1])

plt.bar(x,y,align="center",color="r",width=0.9)
#plt.scatter(x,y,color="y",linewidths=0.1)
plt.title("Ceps por Estado")
plt.show()

