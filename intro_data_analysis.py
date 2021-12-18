#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:



dict1 = {
    'Name':['Lanre','Biola','Shola','Seun','Femi','Lola','Chidi'],
    'Marks':[98,89,99,87,90,83,99],
    'Gender':['Male','Female','Male','Male','Male','Female','Male']
}

df1 = pd.DataFrame(dict1)
df1


# ### 1. Display 3 row from the dataframe

# In[5]:


df1.head(3)


# ### 2. Check the last 3 rows of the dataframe

# In[6]:


df1.tail(3)


# ### 3.Find the shape of the dataframe

# In[10]:


df1.shape


# In[11]:


print('Numbers of rows:',df1.shape[0])
print('Numbers of columns:', df1.shape[1])


# ### 4. Get info about the total number of rows,columns,datatypes,memory requirement

# In[14]:


df1.info()


# ### 5.To check non-value in the dataset

# In[21]:


# note: when you put axis=0 or axis=1 as argument in the sum method, 
# it gives the numbers of null values in the rows or columns

df1.isnull().sum()


# ### 6. Get Overall statistics about the dataframes

# In[23]:


df1.describe(include='all')


# ### 7. Find unique values from Gendar column

# In[28]:


df1['Gender'].unique()


# ### 8.Find number of unique values from Gendar column

# In[32]:


num_of_unique_value = df1['Gender'].nunique()
print('The number of unique value(s) is/are: ',num_of_unique_value)


# ### 9. Count the number of unique value in gendet column

# In[34]:


df1['Gender'].value_counts()


# ### 10.Find the total number of students btw 90 amd 100

# In[51]:


#sdt_above_90 = len(df1[df1['Marks'] >= 90])
sdt_above_90 = sum(df1['Marks'].between(90,100))

print(f"There are {sdt_above_90} students with marks with 90 and above")


# ### 11.Find average marks

# In[52]:


df1['Marks'].mean()


# ### 12a.Using apply method

# In[54]:


def marks(x):
    return x/2


# In[55]:


df1['Half_marks'] = df1['Marks'].apply(marks)


# In[56]:


df1


# ### 12b. Using lambda method

# In[58]:


df1['Marks'].apply(lambda x: x/2)


# In[59]:


df1


# ### 13. To find length of the string in Name column

# In[60]:


df1['Name'].apply(len)


# ### 14. Using map function

# In[64]:


# creating a gender code using map function
df1['gender_code'] = df1['Gender'].map({'Male':1,'Female':0})


# In[65]:


df1


# ### 15. Drop columns

# In[69]:


# Note: when dropping multiple list,put the columns in a list
df1.drop('gender_code', axis=1)


# ### 16. To modify existing dataframe

# In[72]:


df1.drop(['Half_marks','gender_code'],axis=1,inplace=True)


# In[73]:


df1


# ### 17. Print names of columns

# In[74]:


df1.columns


# ### 18. Sort the Marks columns

# In[77]:


df1.sort_values(by='Marks',ascending=False)


# ### 19. Display names and marks of female student only

# In[86]:


#df1[df1['Gender'] == 'Female'][['Name','Marks']]
df1[df1['Gender'].isin(['Female'])][['Name','Marks']]


# In[ ]:




