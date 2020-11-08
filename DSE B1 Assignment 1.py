#!/usr/bin/env python
# coding: utf-8
Question 1:
# In[6]:


import enchant
a = enchant.Dict("en_US")
choices=['RAINBOW',"RANIBOW","BOWRANI","ROBWANI"]

for i in range(len(choices)):
    if a.check(choices[i]) == True:
        print(choices[i])    

Question 2:
# In[5]:


tobeprinted=input().upper()
print(tobeprinted)

Question 3:
# In[5]:


costPrice = int(input())
sellingPrice = int(input())
profit="Profit"
loss="Loss"
neither="Neither"

if (costPrice > 0) & (sellingPrice > 0):
    if costPrice == sellingPrice:
        print(neither)
    elif costPrice > sellingPrice:
        print(loss)
    else:
        print(profit)

Question 4:
# In[4]:


userInput=int(input())
amount=0
if userInput > 0:
    amount = userInput*80
    print(amount)
else:
    print(amount)

