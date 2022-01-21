#!/usr/bin/env python
# coding: utf-8

# In[18]:


x = int(input("Enter number of terms : "))

n1, n2 = 0, 1
count = 0

while count < x:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1


# In[ ]:




