#!/usr/bin/env python
# coding: utf-8

# In[1]:


radius = float(input('Enter the radius of the circle: '))
area = 3.14159 * radius ** 2
print('The area of the circle with radius 1.1 is:',area)


# In[3]:


x = input("Input the Filename: ")
ext = x.split(".")
print ("The extension of the file is :" + repr(ext[-1]))

