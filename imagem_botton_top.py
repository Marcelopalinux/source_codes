#!/usr/bin/env python
# coding: utf-8

# # capturar pedaços de imagens, inicio e fim 

# In[1]:


from PIL import Image


# In[2]:


img = Image.open('pencils.jpg')


# In[3]:


img


# In[5]:


img.size


# In[6]:


x = 0 
y = 0 

w = 1950 / 3
h = 1300 / 10


# In[7]:


img2 = img.crop((x,y,w,h))


# In[8]:


img2


# In[9]:


x = 0
y = 1100

w = 1950 / 3
h = 1300


# In[10]:


img3 = img.crop((x,y,w,h))


# In[11]:


img3


# In[ ]:




