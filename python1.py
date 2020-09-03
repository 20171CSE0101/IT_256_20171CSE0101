#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fact(n):
    if n==0 or n==1:
        return(1)
    else:
        return(n*fact(n-1))
n=int(input('enter n'))
r=int(input('enter r'))
ncr=fact(n)/(fact(r)*fact(n-r))
print('binomial coefficient of {0} and {1} is {2}'.format(n,r,ncr))


# In[4]:


def power(x,y):
    if y==0:
        return(1)
    else:
        return(x*power(x,y-1))
x=int(input('enter x'))
y=int(input('enter y'))
print('{0} to the power of {1} is {2}'.format(x,y,power(x,y)))


# In[5]:


print('hello world')


# In[6]:


a=4
print(a*5)


# In[ ]:




