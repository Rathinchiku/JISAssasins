#!/usr/bin/env python
# coding: utf-8

# In[ ]:


salary=int(input("enter the salary"))
if salary>5000:
    hra=salary*0.15
    da=salary*1.5
    print("gross salary= ",salary+hra+da)
elif salary<5000:
    hra=salary*0.1
    da=salary*1.1
    print("gross salary= ",salary+hra+da)

