
# coding: utf-8

# In[4]:


text=input("please type anything:\n")
counter = set()

    
for ch in set(text):
    print("'"+ch+"':",text.count(ch))

