#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4


# In[2]:


res = requests.get('https://pt.wikipedia.org/wiki/Ronaldinho_Ga%C3%BAcho')


# In[3]:


soap = bs4.BeautifulSoup(res.text,'lxml')


# In[29]:


img1 = soap.select('.image')[0]


# In[30]:


img2 = img1.find_all('img')


# ## 

# In[31]:


imagem_ronaldinho = 'http:'+img2[0]['src']


# In[32]:


imagem_ronaldinho


# In[20]:


resronaldo = requests.get(imagem_ronaldinho)


# In[23]:


file_gaucho = open('gaucho3.png','wb')


# In[24]:


file_gaucho.write(resronaldo.content)


# In[25]:


file_gaucho.close()


# <img src="gaucho3.png">

# In[ ]:




