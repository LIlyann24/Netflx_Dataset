#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd
data = pd.read_excel('D:\\Python\\Side Project\\Netflix Dataset\\8. Netflix Dataset.xlsx')
data


# In[126]:


data.head()


# In[127]:


data.tail()


# In[128]:


data.shape


# In[129]:


data.size


# In[130]:


data.columns


# In[131]:


data.dtypes


# In[132]:


data.info()


# In[133]:


data[data.duplicated()]


# In[134]:


##Remove duplicates
data.drop_duplicates(inplace = True)


# In[135]:


data[data.duplicated()]


# In[136]:


data.shape


# In[137]:


data.isnull()


# In[138]:


##Show the count of Null in each column
data.isnull().sum()


# In[139]:


##seaborn為視覺化模組
import seaborn as sns
sns.heatmap(data.isnull())


# In[140]:


##isin()函式找出示否存在該資料
data[data['Title'].isin(['House of Cards'])]


# In[141]:


data.dtypes


# In[142]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])
data


# In[143]:


data.dtypes


# In[144]:


##counts the occurance of all individual Yerars in Date column.
data['Date_N'].dt.year.value_counts()


# In[145]:


data['Date_N'].dt.year.value_counts().plot(kind = 'bar')


# In[146]:


data.groupby('Category').Category.count()


# In[147]:


##method 1
data.groupby('Category').Category.count().plot(kind = 'bar')


# In[148]:


data.head()


# In[ ]:





# In[151]:


#create a new column only consider year
data['Year'] = data['Date_N'].dt.year
data.head(2)


# In[157]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]


# In[159]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2020)]


# In[170]:


data[(data['Category'] == 'TV Show') & (data['Country'] == 'India')] ['Title']


# In[172]:


data['Director'].value_counts().head(10)


# In[178]:


##condition1: movies and comedies, condition2: united kingdom
data[(data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom') ]


# In[182]:


data[data['Cast'] == 'Tom Cruise']


# In[185]:


data[data['Cast'].str.contains('Tom Cruise')]


# In[188]:


##Drops the rolls that contains all or any missing values
data_new = data.dropna()
data_new.head(2)


# In[192]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[195]:


##Count number of distinct elements in specified axis.
data['Rating'].nunique()


# In[197]:


##show the values
data['Rating'].unique()


# In[202]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')]


# In[211]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')].shape


# In[219]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] >= 2018)]


# In[223]:


##=data['Duration'].unique()
data.Duration.unique()


# In[225]:


data.Duration.dtypes


# In[227]:


##str.split(): https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html
data[['Miniutes','Unit']] = data['Duration'].str.split(' ', expand=True)
data.head(2)


# In[232]:


data.Miniutes.max()


# In[234]:


data.Miniutes.min()


# In[236]:


data_tvshow = data[data['Category'] == 'TV Show']
data_tvshow.head(2)


# In[241]:


data_tvshow.Country.value_counts().head(1)


# In[246]:


data.sort_values(by='Year', ascending=False).head(2)


# In[275]:


mask1 = (data['Category']=='Movie') & (data['Type']=='Dramas')
data[mask1]


# In[276]:


mask2 = (data["Category"]=="TV Show") & (data["Type"]=="Kids' TV")
data[mask2]


# In[277]:


data[mask1 | mask2]

