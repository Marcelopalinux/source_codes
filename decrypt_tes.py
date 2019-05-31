#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib


# In[2]:


hashlib.algorithms_available


# In[3]:


hash_obj = hashlib.sha3_256()


# In[4]:


hash_obj.update(b'Hello')


# In[5]:


hash_obj.hexdigest()


# In[7]:


from cryptography.fernet import Fernet 


# In[8]:


key = Fernet.generate_key()


# In[9]:


key


# In[10]:


key


# In[11]:


cipher = Fernet(key)


# In[13]:


cipher.encrypt(b'Hello are you there?')


# In[14]:


other_cipher= Fernet(b'ezwfa6V2D6NuT-qhY1Xr2YwQdeMXnSv62VCbgSjw1FY=')


# In[15]:


other_cipher.decrypt(b'gAAAAABc8WQ9OlFCerKNLH93HlYxOu1EpvAXUpCd1-O7ha779mqEM8lh0Jvq3g4X5VTBS8962Y4KvQ2nM2EDkHyqG10t9J6mAjPPCu8stVbj0r6FLuLCKwk=')


# In[17]:


keywork = b'123'


# In[18]:


key = hashlib.sha3_256(keywork)


# In[19]:


key


# In[21]:


key.digest()


# In[22]:


import base64


# In[23]:


key_bytes = key.digest()


# In[24]:


fernet_key = base64.urlsafe_b64encode(key_bytes)


# In[25]:


fernet_key


# In[26]:


custom_cipher = Fernet(fernet_key)


# In[27]:


custom_cipher.encrypt(b'Hello')


# In[28]:


custom_cipher.decrypt(b'gAAAAABc8WaOoop15kIg2xNfAjgMHJp9VKiCZu1RdP_XnWRSB0cmsy1c0Fu6js2YhEqE87OpDWinCqnVqZ7u4FpPKIf75DuJwQ==')


# In[60]:


fernet_prime = b'65537'


# In[ ]:





# In[61]:


key_hash = hashlib.sha3_256(fernet_prime)


# In[62]:


key_bytes2 = key_hash.digest()


# In[63]:


key_fernet = base64.urlsafe_b64encode(key_bytes2)


# In[64]:


key_fernet


# In[65]:


customFernet = Fernet(key_fernet)


# In[66]:


customFernet.decrypt(b'gAAAAABaSsmdCFRxbqA6n-L0CMIMuhn26uGiIk5Wtx-V7wEPLBZYA67nGbNWyZziGyorwIlHqp3M5xrtzQj5tCab8XfBRCmdJXZYD1Fwp68AtD8WEMhblQ4I2DKDNFzqULH1DDETry3ptZnGZUgVo5gdDlnihqu1_oX-KboNpyRQ6J0DmeWTsm3L31btF_O6sX81rj3rBVI0qVuT7QdRT2burisQRnw5htA05llYgc1_fMkN_PSxCwY=')


# In[ ]:




