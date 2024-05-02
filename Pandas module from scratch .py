#!/usr/bin/env python
# coding: utf-8

# # *pandas from scratch*

# In[1]:


import pandas as pd
import numpy as np


# ## *Series*

# In[2]:


my_series=pd.Series([1,24,32]) #it can be created from list or array
my_series


# In[3]:


my_series.index


# In[5]:


my_series.values


# In[4]:


my_series[1]


# In[58]:


my_series.get(1)


# In[5]:


my_series[0:]


# In[6]:


my_series=pd.Series([1,22,33],index=['a','b','c'])
my_series


# In[11]:


my_series['a']


# In[7]:


my_series[0]


# In[8]:


my_series[2]


# In[9]:


my_series[0:]


# In[10]:


my_series=pd.Series({'a':[1,2,3],'b':[33,53,5]})
my_series


# In[11]:


my_series.index


# In[12]:


my_series.values


# In[13]:


my_series['a']


# In[14]:


my_series['b']


# In[15]:


my_series=pd.Series({'a':2,'b':8},index=['b','a']) #can be used for resort
my_series


# In[16]:


type (my_series.index)


# In[17]:


type(my_series.values)


# In[18]:


my_series.values


# In[19]:


list(my_series.values)


# In[20]:


for i in my_series.values: #for making iteration
    print(i)


# ## *Data Frame*

# In[22]:


data_frame=pd.DataFrame({'a':[1,2,3],'b':[4,67,9]}) #it can be created from dictionary or 2D list or Series
data_frame


# In[23]:


data_frame.index


# In[24]:


data_frame.columns


# In[25]:


type(data_frame.columns)


# In[26]:


type(data_frame.index)


# In[27]:


data_frame.values


# In[40]:


for i in (data_frame.columns):
    print(i)


# In[41]:


for i in data_frame.index:
    print(i)


# In[42]:


data_frame['a'] #return series object


# In[43]:


data_frame['a'][0]


# In[48]:


data_frame=pd.DataFrame(my_series,index=[0,1])
data_frame


# In[49]:


data_frame=pd.DataFrame(my_series)
data_frame


# In[51]:


data_frame=pd.DataFrame([[1,3,5],[5674,76,87]],index=[1,2],columns=['a','b','c'])
data_frame


# In[52]:


data_frame.index,data_frame.columns,data_frame['a']


# In[53]:


data_frame['a'].get(1) #as dictionary


# ## *Data selection and indexing in Series*

# In[60]:


my_series


# In[61]:


'a' in my_series #'a' in my_series.index


# In[62]:


my_series.keys()


# In[65]:


list(my_series.items())


# In[66]:


for i , j in my_series.items():
    print(i,j)


# In[67]:


my_series['d']=2.3
my_series


# In[68]:


my_series[[0,'d']]


# In[69]:


my_series[my_series>3]


# In[70]:


my_series[(my_series>3) & (my_series<30)]


# In[71]:


my_series[my_series.isnull()]


# ## *Data selection and indexing in Data Frame*

# In[29]:


data_frame


# In[30]:


data_frame['a']


# In[31]:


data_frame['b']


# In[32]:


data_frame.a


# In[33]:


data_frame.b #is available when column name is str or not method 


# In[34]:


data_frame['den']=data_frame['a']/data_frame['b']
data_frame


# In[35]:


data_frame['mult']=data_frame['a']*data_frame['b']
data_frame


# In[36]:


data_frame.values[0]


# In[37]:


data_frame.T


# In[38]:


data_frame.loc[:,'a']


# In[39]:


data_frame.loc[1,'b']


# In[40]:


data_frame.loc[[1,2],'a']


# In[41]:


data_frame.iloc[:,1]


# In[42]:


data_frame[data_frame['a']>12]


# In[43]:


data_frame[data_frame['a'].notnull()]['den']


# In[44]:


data_frame=data_frame[data_frame['a']>12]


# In[45]:


data_frame


# In[46]:


data_frame.reset_index(inplace=True)


# In[47]:


data_frame


# In[48]:


data_frame.drop('index',axis=1,inplace=True)
data_frame


# In[49]:


data_frame.loc[0,'c']=10
data_frame


# ## *Dealing with null values*

# In[50]:


data_frame.isnull()


# In[51]:


data_frame


# In[52]:


data_frame.notnull()


# In[53]:


data_frame.isnull().sum()


# In[54]:


data_frame.notnull().sum()


# In[55]:


data_frame=pd.DataFrame([[1,3,5],[5674,76,87]],index=[1,2],columns=['a','b','c'])
data_frame


# In[56]:


data_frame[data_frame['a'].notnull()]


# In[57]:


data_frame[data_frame['a'].isnull()]


# In[58]:


data_frame.a[1]=np.nan
data_frame.c[2]=np.nan
data_frame


# In[59]:


data_frame['a'].isnull().sum()


# In[60]:


data_frame.dropna() #remove null values by rows at least one nan


# In[61]:


data_frame = pd.DataFrame([[1, np.nan, 2],
 [2, 3, 5],
 [np.nan, 4, 6]])
data_frame


# In[62]:


data_frame.dropna(how='all') #drop rows only if all values is nan


# In[63]:


data_frame.dropna(how='all',axis=1)


# In[64]:


data_frame.dropna(thresh=3) #mini number of non null is 3 


# In[65]:


data_frame


# In[66]:


data_frame.dropna(thresh=3,inplace=True)


# In[67]:


data_frame


# In[68]:


data_frame = pd.DataFrame([[1, np.nan, 2],
 [2, 3, 5],
 [np.nan, 4, 6]])
data_frame


# ## *filling null values*

# In[69]:


data_frame.fillna(0)


# In[70]:


data_frame[0].fillna(12)


# In[71]:


data_frame


# In[72]:


data_frame[0].fillna(12,inplace=True)


# In[73]:


data_frame


# In[76]:


data_frame[1].fillna(data_frame[0].mean(),inplace=True)


# In[77]:


data_frame


# ## *concatenation of arrays*

# In[78]:


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])


# In[79]:


np.concatenate([x, y, z],axis=0)


# In[80]:


np.concatenate([x, y, z],axis=1)


# In[81]:


x = [[1, 2],
[3, 4]]
np.concatenate([x, x], axis=1) #axis=1 columns will change


# In[82]:


np.concatenate([x,x],axis=0)


# In[83]:


ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])


# In[86]:


data_frame1=pd.DataFrame({'A':[1,2],'B':[33,45]})
data_frame2=pd.DataFrame({'c':[13,22],'n':[99,76]})
pd.concat([data_frame1,data_frame2],axis=1)


# In[87]:


pd.concat([data_frame1,data_frame2],axis=0)


# In[88]:


data_frame1


# In[89]:


data_frame2


# In[90]:


pd.concat([data_frame1,data_frame2],axis=0)


# In[91]:


pd.concat([data_frame1,data_frame2],axis=1)


# In[92]:


data_frame1=pd.concat([data_frame1,data_frame2],axis=1)
data_frame1


# In[98]:


data_frame2=pd.DataFrame({'c':[13,22],'n':[99,76]},index=[3,4])
data_frame1


# In[99]:


data_frame2


# In[101]:


pd.concat([data_frame1,data_frame2],axis=0)


# In[102]:


pd.concat([data_frame1,data_frame2],axis=0,ignore_index=True)


# In[103]:


data_frame2.rename(columns={'c':'A','n':'B'},inplace=True)
pd.concat([data_frame1,data_frame2],axis=0)


# ## *ggregation*

# In[104]:


data_frame


# In[114]:


data_frame.rename(columns={0:'A',1:'B',2:'C'},inplace=True)


# In[115]:


my_series


# In[116]:


my_series.mean()


# In[117]:


my_series.sum()


# In[118]:


data_frame.mean()


# In[119]:


data_frame.mean(axis=1)


# In[120]:


data_frame.describe()


# In[122]:


data_frame.agg(['min'])


# In[123]:


data_frame.agg(['max'])


# In[124]:


data_frame.agg([lambda x : x**2])


# In[126]:


data_frame.agg(['min','max'
               ])


# In[127]:


data_frame['A'].agg(['min','max','sum'])


# In[128]:


data_frame.groupby('A')


# In[129]:


data_frame.groupby(by='A')


# In[130]:


d=data_frame.groupby(by='A')
d


# In[131]:


d.first


# In[132]:


d.first()


# In[133]:


data_frame.groupby('B').first()


# In[137]:


s=data_frame.groupby(['B','A'])
s.first()


# In[139]:


data_frame.apply(lambda x : x**0.5)


# In[140]:


data_frame['A'].apply(np.sum)


# In[141]:


data_frame['A'].apply(np.sqrt,axis=1)


# In[143]:


data_frame['sum_A']=data_frame['A'].apply(np.sqrt)
data_frame


# In[ ]:




