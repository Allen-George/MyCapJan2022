#!/usr/bin/env python
# coding: utf-8

# In[15]:


x = input('Please enter a string : ')
def most_frequent(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(most_frequent(x))


# In[ ]:




