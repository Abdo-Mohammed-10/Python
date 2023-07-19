#!/usr/bin/env python
# coding: utf-8

# # modules

# # TIME

# In[17]:


import time  as t
t.localtime()


# In[18]:


time=t.localtime()
print("transactions completed at", str(time.tm_hour) + " h " + str(time.tm_min)+" m")


# In[19]:


t.time()


# In[20]:


t.time()


# In[21]:


t_now=t.time()


# In[24]:


delivery_time= t_now + (86400 * 7)  # 86400 seconds of day 
t.localtime(delivery_time)


# In[26]:


t.sleep(5) # make this cell sleep 5 seconds after that the line will run .


# # Good lUCK
# Abdulrahaman Mohammed
