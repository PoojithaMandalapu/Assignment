#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report, confusion_matrix
warnings.filterwarnings("ignore")


# # Question
# 
# 
# 1.Read the provided CSV file ‘data.csv’.
# https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing
# 2. Show the basic statistical description about the data.
# 3. Check if the data has null values.
# a. Replace the null values with the mean
# 4. Select at least two columns and aggregate the data using: min, max, count, mean.
# 5. Filter the dataframe to select the rows with calories values between 500 and 1000.
# 6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
# 7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
# 8. Delete the “Maxpulse” column from the main df dataframe
# 9. Convert the datatype of Calories column to int datatype.
# 10. Using pandas create a scatter plot for the two columns (Duration and Calories).
# 

# In[2]:


#1. Read the provided CSV file ‘data.csv’. https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing


df = pd.read_csv("data.csv")
df.head()


# In[3]:


#2. Show the basic statistical description about the data.

df.describe()


# In[4]:


#3. Check if the data has null values.

df.isnull().any()


# In[5]:


#Replace the null values with the mean

df.fillna(df.mean(), inplace=True)
df.isnull().any()


# In[6]:


#4. Select at least two columns and aggregate the data using: min, max, count, mean.

df.agg({'Maxpulse':['min','max','count','mean'],'Calories':['min','max','count','mean']})


# In[7]:


#5. Filter the dataframe to select the rows with calories values between 500 and 1000.

df.loc[(df['Calories']>500)&(df['Calories']<1000)]


# In[8]:


#6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.

df.loc[(df['Calories']>500)&(df['Pulse']<100)]


# In[9]:


#7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.

df_modified = df[['Duration','Pulse','Calories']]
df_modified.head()


# In[10]:


#8. Delete the “Maxpulse” column from the main df dataframe

del df['Maxpulse']


# In[11]:


df.head()


# In[12]:


df.dtypes


# In[13]:


#9. Convert the datatype of Calories column to int datatype.

df['Calories'] = df['Calories'].astype(np.int64)
df.dtypes

