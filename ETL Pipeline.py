#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd #for data extract/transformation/manipulation or analysis etc.
import psycopg2 #for connecting Python to PostgreSQl
from sqlalchemy import create_engine #to efficiently manage and reuse the database connections


# In[12]:


#Extract data from a csv file into a Pandas DataFrame and get the file path for the document/data
data = pd.read_csv(r"C:\Users\dell\Downloads\Softwork Technologies - Sheet1.csv")


# In[13]:


#view the top five rows
data.head()


# In[14]:


#view the bottom five rows
data.tail()


# In[15]:


#Tranform the data(i.e., clean the data)-Deal with missing and duplicate data
data.duplicated().sum()


# In[16]:


#Explore missing data
data.isnull().sum()


# In[17]:


#Let's take a look at the missing data-EDUCATION column
data[data['education'].isnull()].head() #top 5 rows


# In[18]:


data[data['previous_year_rating'].isnull()].head() #top 5 rows


# In[19]:


#Deal with missing data
data['education']=data['education'].fillna('unknown') #for the education column
data['previous_year_rating']=data['previous_year_rating'].fillna(0)#for previous_year_rating column


# In[20]:


data.isnull().sum()


# In[21]:


#Create a Database
#Go to pdAdmin4 and create a database table


# In[13]:


from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine

# Load CSV data
data = pd.read_csv(r"C:\Users\dell\Downloads\Softwork Technologies - Sheet1.csv")

# Credentials
username = 'postgres'
password = quote_plus('Postgre@123')  # Use your real password
host = 'localhost'
port = 5432
db_name = 'softwork'  # Make sure this DB is already created in PostgreSQL

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')

# Load data into PostgreSQL table
data.to_sql('employee_table', engine, if_exists='replace', index=False)

# Close connection
engine.dispose()



# In[ ]:





# In[ ]:




