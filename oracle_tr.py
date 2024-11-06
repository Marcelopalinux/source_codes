#!/usr/bin/env python
# coding: utf-8

# In[12]:


import sys
cont=0
print(sys.argv[1])
with open("t.txt") as file:
    for i in file:
        cont+=1
        if cont%int(sys.argv[2])==0:
            print("'"+i.strip()+"')")
            print(sys.argv[1])
        else:
            print("'"+i.strip()+"',")
          


# In[ ]:




