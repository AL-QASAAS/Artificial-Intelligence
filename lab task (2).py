#!/usr/bin/env python
# coding: utf-8

# #### myList1=[]
# print("Enter objects of first list...")
# for i in range(5):
#     val=input("Enter a value:")
#     n=int(val)
#     myList1.append(n)
#     
#     myList2=[]
#     print("Enter objects of second list...")
#     for i in range(5):
#         val=input("Enter a value:")
#         n=int(val)
#         myList2.append(n)
#         
#         list3=myList1+myList2;
#         print(list3)

# In[4]:


def isPalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
     return True
    else:
     return False
print(isPalindrome("deed"))


# In[16]:


a=[[1,0,0],[0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[],[],[]]

for indrow in range (3):
    c.append([])
    print(c)
    for indcol in range(3):
        c[indrow].append (0)
        for indaux in range (3):
            c[indrow][indcol] += a[indrow][indaux] * b[indcol][indrow]
print(c)


# In[ ]:




