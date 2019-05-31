#!/usr/bin/env python
# coding: utf-8

# # Necessario colocar imagem sobre a outra para capturar o link do exercicio
# #precisou deixar as imagens do mesmo tamanho e fazer o paste

# In[259]:


from PIL import Image


# In[260]:


imagem = Image.open('image_link.PNG')


# In[261]:


imagem


# In[262]:


capa = Image.open('cover_image.PNG')


# In[263]:


capa


# In[264]:


imagem


# In[265]:


#imagem.paste(im=capa,box=(0,0),mask=capa)
#capa.paste(im=imagem,box=(0,0),mask=imagem)


# In[ ]:





# In[266]:


capa.size


# In[279]:


img_new = imagem.resize((1093,693))


# In[280]:


capa.size


# In[281]:


img_new.size


# In[282]:


#img_new.paste(im=img_new,box=(0,0),mask=capa.putalpha(10))


# 

# In[283]:


capa.putalpha(50)


# In[284]:


capa


# In[285]:


img_new.paste(im=capa,box=(0,0),mask=capa)


# In[286]:


img_new


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




