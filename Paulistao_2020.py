from selenium import webdriver
import time
import pandas as pd
import matplotlib.pyplot as plt

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.srgoool.com.br/classificacao/Paulistao/Serie-A1/2020#geral')

html_list = driver.find_element_by_id("table_classificacao_geral")
items = html_list.find_elements_by_tag_name("tr")
tabela = []
for item in items:
    colunas = []
    for i in item.find_elements_by_tag_name("td"):
        text = i.text
        colunas.append(text)
    tabela.append(colunas)
driver.close()
driver.quit()
df = pd.DataFrame(tabela[1:17],columns=['Colocação','Time','PG','J','V','E','D','GP','GC','SG','%A','PP','I','%V','RL','RB'])
df.set_index("Colocação",inplace=True)

def moeda_converte(valor):
    valor = float(valor.replace('R$','').replace('.','').replace(',','.'))
    return  valor
df['RL'] = df['RL'].apply(moeda_converte)
df['RB'] = df['RB'].apply(moeda_converte)



plt.figure(figsize=(100,50))
plt.rcParams.update({'font.size': 50})
plt.bar(df['Time'],df['RL'])
plt.ylabel('Valores em R$')
plt.xlabel('Times do Paulistão 2020')
plt.title('Renda Liquida de cada Time do Paulistao 2020')


plt.figure(figsize=(100,50))
plt.rcParams.update({'font.size': 50})
plt.bar(df['Time'],df['PG'].astype('int64'))
plt.ylabel('PONTUAÇÃO')
plt.xlabel('Times do Paulistão 2020')
plt.ylim(0,25)
plt.title('PONTOS GERAIS NO CAMPEONATO')



plt.figure(figsize=(100,50))
plt.rcParams.update({'font.size': 50})
plt.bar(df['Time'],df['GP'].astype('float')/df['J'].astype('int64'))
plt.ylabel('Média de Gols por partida')
plt.xlabel('Times do Paulistão 2020')
plt.ylim(0,5)
plt.title('MEDIAS')

