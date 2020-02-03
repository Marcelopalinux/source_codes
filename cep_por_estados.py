#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pyodbc
import matplotlib.pyplot as plt


# In[2]:


con = pyodbc.connect("DSN=BANCOFORUM")


# In[3]:


cur = con.cursor()


# In[41]:


stmt = cur.execute("select  count(c.CEP) as 'num_cep',c.id_estado"+ " from loja.cep  c"+ " join loja.bairro b on c.id_bairro=b.id_bairro"+ " join loja.cidade cid on b.id_cidade=cid.id_cidade"+" group by c.id_estado order by 1 desc")


# In[42]:


rows = stmt.fetchall()


# In[43]:


n_ceps = []
estado = []


# In[44]:


for i in rows:
   # if i[3] == 'SP':
   #     estado_sp.append(i[3])
   #     n_ceps_sp.append(i[2])
   # else:
   #     estado_rj.append(i[3])
   #     n_ceps_rj.append(i[2])
    n_ceps.append(i[0])
    estado.append(i[1])

    


# In[53]:


# figsize redimenciona tamanho da plotagem em tela, ajudando na demonstração ao cliente
plt.figure(figsize=(16,10))
plt.bar(estado,n_ceps,color='red')


# In[ ]:





# In[ ]:




