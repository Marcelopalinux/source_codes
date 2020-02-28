#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
import time
import pandas as pd

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
    


# In[3]:


df = pd.DataFrame(tabela[1:17],columns=['Colocação','Time','PG','J','V','E','D','GP','GC','SG','%A','PP','I','%V','RL','RB'])


# In[4]:


df.set_index("Colocação",inplace=True)


# In[5]:


df


# In[6]:


def moeda_converte(valor):
    valor = float(valor.replace('R$','').replace('.','').replace(',','.'))
    return  valor


# In[7]:


df['RL'] = df['RL'].apply(moeda_converte)
df['RB'] = df['RB'].apply(moeda_converte)


# In[8]:


df


# In[9]:


import matplotlib.pyplot as plt


# In[11]:


plt.figure(figsize=(100,50))
plt.rcParams.update({'font.size': 50})
plt.bar(df['Time'],df['RL'])
plt.ylabel('Valores em R$')
plt.xlabel('Times do Paulistão 2020')
plt.title('Renda Liquida de cada Time do Paulistao 2020')


# In[17]:


plt.figure(figsize=(100,50))
plt.rcParams.update({'font.size': 50})
plt.bar(df['Time'],df['PG'].astype('int64'))
plt.ylabel('PONTUAÇÃO')
plt.xlabel('Times do Paulistão 2020')
plt.ylim(0,25)
plt.title('PONTOS GERAIS NO CAMPEONATO')


# In[21]:


plt.figure(figsize=(100,50))
plt.rcParams.update({'font.size': 50})
plt.bar(df['Time'],df['GP'].astype('float')/df['J'].astype('int64'))
plt.ylabel('Média de Gols por partida')
plt.xlabel('Times do Paulistão 2020')
plt.ylim(0,5)
plt.title('MEDIAS')


# In[ ]:




