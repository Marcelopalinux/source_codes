#!/usr/bin/env python
# coding: utf-8

# # capturar trecho da imagem
# 
# # dividir a imagem em 2 para pegar o meio utilizando o size
# # colocar X como essa metade menos um valor para capturar a imagem
# # como no exemplo - 200
# # colocar W como o valor + 200 
# 

# In[1]:


from PIL import Image


# In[2]:


img1 = Image.open('example.jpg')


# In[3]:


img1


# In[4]:


img1.size


# In[90]:


# start e finish  y = start h = finish
# start = x finish = w 
halfway = 1993/2
x = halfway - 160 
w = halfway + 160 

y = 850
h = 1257


# In[91]:


img2 = img1.crop((x,y,w,h))


# In[92]:


img2


# In[ ]:





# In[ ]:




