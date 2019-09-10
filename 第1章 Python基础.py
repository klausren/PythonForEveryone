#!/usr/bin/env python
# coding: utf-8

# # <font size=10 >Python入门</font>

# # 1.1 第一个程序

# In[3]:


# This program says hello and asks for my name.

print('Hello World!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is : ')
print(len(myName))
print("What is your age ?") # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# # 1.2 简单程序剖析

# ## 1.2.1 注释

# In[4]:


#Python会互忽略注释。


# In[5]:


'''
我也是注释
你信不信
'''
print('人生苦短 我用Python')


# In[6]:


"""
我也是注释
你信不信

"""
print('人生苦短 我用Python')


# ## 1.2.2 print()函数

# In[7]:


print("我"+'用',"Python") #Python 3 必须加括号


# ## 1.2.3 input()函数

# In[8]:


myName = input()


# In[10]:


myName = input("你的名字是：")


# In[12]:


print('你的名字是：')
myName = input()


# ## 1.2.4 len()函数

# In[14]:


length = len("hello")
print(length)


# ## 1.2.5 str() int() float()函数

# In[16]:


myAge = 29
# print('I am '+ 29 + ' years old')
print("I am "+ str(myAge) +' years old')


# In[ ]:


spam = input()
print(spam)
print(type(spam))
print(float(spam))


# In[29]:


spam = 7.0

print(spam)
print(int(spam))
print(type(spam))
print(spam==str(spam))
print(spam==int(spam))


# In[34]:


number = 12/4
print(number==3)


# In[ ]:




