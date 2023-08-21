#!/usr/bin/env python
# coding: utf-8

# # NETFLIX STOCK ANALYSIS PROJECT

# In[35]:


'''Objective
1) Volume of stock Traded
2) Netflix Stock Price - High, Open ,Close
3) Netflix Stock Price - Day, Month, Year Wise
4) Top-5 Dates with Highest Stock Price
5) Top-5 Dates with Lowest Stock Price '''


# In[36]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from datetime import datetime


# In[37]:


df= pd.read_csv("netflix.csv")


# In[38]:


df.head()


# In[39]:


sns.set(rc={'figure.figsize':(10,5)})


# In[40]:


df['Date']= pd.to_datetime(df['Date'])
df =df.set_index('Date')
df.head()


# In[41]:


sns.lineplot(x=df.index,y=df['Volume'],label= 'volume')
plt.title('Volume of stock vs time')


# In[42]:


df.plot(y=["High","Close","Open"],title="Netflix stock price")


# In[43]:


fig,(ax1,ax2,ax3)=plt.subplots(3,figsize=(15,10))
df.groupby(df.index.day).mean().plot(y='Volume',ax=ax1,xlabel="Day")
df.groupby(df.index.month).mean().plot(y='Volume',ax=ax2,xlabel="Month")
df.groupby(df.index.year).mean().plot(y='Volume',ax=ax3,xlabel="Year")


# # Dates with highest price

# In[44]:


a= df.sort_values(by = 'High',ascending = False).head(5)
a['High']


# In[45]:


b = df.sort_values(by = "Low",ascending = True).head(5)
b['Low']


# In[46]:


fig,axes = plt.subplots(nrows=1,ncols=2,sharex = True,figsize=(12,5))
fig.suptitle('High and Low Values stock per period of time',fontsize = 18)
sns.lineplot(ax = axes[0],y = df["High"],x = df.index,color = "green")
sns.lineplot(ax = axes[1],y = df["Low"],x = df.index,color = "red")


# In[ ]:




