#!/usr/bin/env python
# coding: utf-8

# **Vedant Modak**
#   | BE(IT) undergrad @ PES Modern College of Engineering,Pune.

# ****Exploratory Data Analysis****

# **Importing the necessary libraries**

# In[125]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **Importing the dataset**

# In[126]:


df=pd.read_csv('F:\Data Analytics\Portfolio\Projects\Project - 1 (Exploratory data analysis)\exploratory_data.csv')


# **Having  an overview of the dataset**

# In[127]:


df.head()


# In[128]:


df.tail()


# In[129]:


df.shape


# **Cleaning the dataset**

# **Looking for Null values**

# In[130]:


df.info()


# In[131]:


df.columns


# **Dropping unnecessary columns**

# In[132]:


df=df.drop(['Employer provided', 'seniority_by_title', 'Competitors', 'Degree', 'Hourly'], axis=1)


# In[133]:


df.columns


# In[134]:


print(df['Avg Salary(K)'])


# **Changing Data type of Average Salary to integer**

# In[135]:


df["Avg Salary(K)"] = df["Avg Salary(K)"].astype("int64")


# In[136]:


print(df['Avg Salary(K)'])


# In[137]:


df.fillna(-1)


# In[138]:


df.isnull().sum()


# In[139]:


df.describe()


# **Dropping duplicates and null values**

# In[140]:


df = df.drop_duplicates()


# In[141]:


df.dropna()


# **Removing Outliers**

# In[142]:


def remove_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    threshold = 1.5 * IQR
    outlier_mask = (column < Q1 - threshold) | (column > Q3 + threshold)
    return column[~outlier_mask]


# In[143]:


df.columns


# In[153]:


col_name = ['Rating', 'Founded']
for col in col_name:
    df[col] = remove_outliers(df[col])


# In[154]:


plt.figure(figsize=(10, 6)) 

for col in col_name:
    sns.boxplot(data=df[col])
    plt.title(col)
    plt.show()


# **Data Visualization**

# In[155]:


df.corr()


# In[158]:


plt.figure(figsize=(18, 12))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# Above heatmap shows a good correlation between Python, aws and the Salary
# This data can be used for feature selection

# In[159]:


sns.distplot(df['Avg Salary(K)'])


# In[161]:


x=df['Rating']
plt.hist(x)


# In[163]:


b=df['Avg Salary(K)']
sns.lineplot(x,b)


# In[164]:


d=df['Python']
sns.lineplot(d,b)


# Your Rating Increases if you know Python !

# In[168]:


sns.boxplot(x)

