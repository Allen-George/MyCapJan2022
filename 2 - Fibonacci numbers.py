#!/usr/bin/env python
# coding: utf-8

# In[1]:


Fn = 0
c = 1
x = int(input('Enter the number : '))
for i in range(x):
    print(Fn)
    Fn += c
    if (i>1):
        c = Fn - c

