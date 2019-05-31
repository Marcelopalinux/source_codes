#!/usr/bin/env python
# coding: utf-8

# In[19]:


from PIL import Image


# In[20]:


blue = Image.open('blue_color.png')


# In[21]:


red = Image.open('red_color.jpg')


# In[22]:


blue


# In[23]:


blue.putalpha(50)


# In[24]:


blue


# In[27]:


red.putalpha(128)


# In[28]:


blue.paste(im=red,box=(0,0),mask=red)


# In[ ]:





# In[29]:


blue


# In[ ]:




