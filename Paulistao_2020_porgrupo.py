from selenium import webdriver
import time
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import plotly.graph_objects as go


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.srgoool.com.br/classificacao/Paulistao/Serie-A1/2020#classificacao')
html_list = driver.find_element_by_id("table_classificacao")
items = html_list.find_elements_by_xpath("//tr[@class='linha-class']")

tabela = []
colunas = []
for i in items:
    colunas = []
    for grup in i.find_elements_by_tag_name('td')[1:]:
        if len(grup.text) > 0 :
            colunas.append(str(grup.text).strip())
    if len(colunas) > 0:
        tabela.append(colunas)
driver.close()
driver.quit()

# crindo um grupo para criar um MultiIndex, o exemplo abaixo, cria-se um indice 16 x 16
# 4 itens da lista b em cada elemento da lista A
grupos_colocacao = [['Grupo A','Grupo B','Grupo C', 'Grupo D'],['1º','2º','3º','4º']]
indice = pd.MultiIndex.from_product(grupos_colocacao,names=['Grupos', 'Colocação'])


# criar um data frame utilizando o multiindex criado e colocando todas as colunas 
df = pd.DataFrame(tabela,index=indice,columns=['Time','PG','J','V','E','D','GP','GC','SG','%A','PP','I','%V','RL','RB'])


# alterando alguns tipos de colunas para int ou float, passando um dict contendo nome da coluna e o tipo referente, esses tipos podem s
# ser convertidos diretamente sem a necessidade de tratar os dados
df = df.astype({'PG':'int64','J':'int64','V':'int64','E':'int64','D':'int64','GP':'int64','GC':'int64','SG':'int64','PP':'float','I':'float'})

fig, axes = plt.subplots(2, 2,figsize=(30,30))
axes[0,0].tick_params(labelsize=25) 
axes[0,1].tick_params(labelsize=25) 
axes[1,0].tick_params(labelsize=25) 
axes[1,1].tick_params(labelsize=25) 

sns.barplot(df.loc['Grupo A']['Time'], df.loc['Grupo A']['PG'],ax=axes[0,0],palette="Blues")
sns.barplot(df.loc['Grupo B']['Time'], df.loc['Grupo B']['PG'],ax=axes[0,1],palette="RdBu_r")
sns.barplot(df.loc['Grupo C']['Time'], df.loc['Grupo C']['PG'],ax=axes[1,0],palette="coolwarm")
sns.barplot(df.loc['Grupo D']['Time'], df.loc['Grupo D']['PG'],ax=axes[1,1],palette="cubehelix")




#teste com ploty
fig = go.Figure(data=go.Bar(x=df.loc['Grupo A']['Time'],y=df.loc['Grupo A']['PG']))
fig.write_html('first_figure.html', auto_open=True)





