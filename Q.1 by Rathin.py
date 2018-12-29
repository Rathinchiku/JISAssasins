#!/usr/bin/env python
# coding: utf-8

# In[7]:


#q.1
x=input("Enter a four digit number:")
p=0
q=0
r=0
for z in x:
    if int(z)==0:
        p+=1
    elif int(z)%2==0:
        q+=1
    elif int(z)%2!=0:
        r+=1
    else:
        pass
print("Number of zeros= ",p)
print("Number of even number= ",q)
print("Number of odd number= ",r)


# In[ ]:





# In[ ]:





# In[ ]:




