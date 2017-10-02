
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np

df = pd.read_csv("Nashville_housing_data_2013_2016.csv.zip")
df.head()


# In[5]:

def getMonth(x):
    vals = x.split("-")
    return vals[1]

def getSeason(x):
    if x=="12":
        return "Winter"
    if x=="01":
        return "Winter"
    if x=="02":
        return "Winter"
    if x=="03":
        return "Spring"
    if x=="04":
        return "Spring"
    if x=="05":
        return "Spring"
    if x=="06":
        return "Summer"
    if x=="07":
        return "Summer"
    if x=="08":
        return "Summer"
    if x=="09":
        return "Fall"
    if x=="10":
        return "Fall"
    if x=="11":
        return "Fall"


# In[8]:

df['Month'] = df["Sale Date"].apply(getMonth)

df.head()


# In[10]:

df['Season'] = df["Month"].apply(getSeason)
df.tail()


# In[27]:

df_winter = df[df['Season'] == 'Winter']
    
df_winter['Sale Price'].mean()


# In[29]:

df_spring = df[df['Season'] == 'Spring']
df_summer = df[df['Season'] == 'Summer']
df_fall = df[df['Season'] == 'Fall']


# In[32]:


df_spring['Sale Price'].mean()


# In[33]:

df_summer['Sale Price'].mean()


# In[34]:

df_fall['Sale Price'].mean()


# In[35]:

df_winter['Sale Price'].mean()


# In[36]:

print "the mean values for Sale Prices for Winter months are higher so the best period to sell homes in Nashville is during the winter months"


# In[ ]:



