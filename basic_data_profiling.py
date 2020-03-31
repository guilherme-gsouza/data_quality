#objective: get the amount of null values, data type of the colunms and the amount of lines

## importing packages
import pandas as pd


# In[4]:


## reading the data, could be a table from a database or a csv/excel file
df = pd.read_csv("base_teste_2.csv", delimiter = ';', index_col=False)


# In[5]:


print(df.head())


# In[6]:


## get the datatype of each column in the dataframe
df_types = df.dtypes


# In[9]:


## convert the df_types variable to reset the index
df_type_rind = df_types.reset_index()

## rename the columns of the variable df_type_rind
df_type_rind.columns = ['col_name','data_type']


# In[13]:


for index, row in df_type_rind.iterrows():
    
    ## print the name of the colunm and the data type
    print(row['col_name'] + ' | ' + str(row['data_type']))


# In[14]:


## get the amount of null values in each colunm of the dataframe
df_nulos = df.isnull().sum()

## convert the df_nulos variable to reset the index
df_nulos_rind = df_nulos.reset_index()

## rename the columns of the variable df_nulos_rind
df_nulos_rind.columns = ['col_name','qtd_nulos']


# In[16]:


for index, row in df_nulos_rind.iterrows():
    
    ## print the amount of null values in each colunm
    print (str(row['qtd_nulos']) + ' | ' + row['col_name'] )


# In[19]:


## get the amount of lines in the whole dataframe
df_lin = df.count().sum()

## print amount of lines in the whole dataframe
print(df_lin)
