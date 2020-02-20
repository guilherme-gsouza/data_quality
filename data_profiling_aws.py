### developed by Guilherme Garcia
### objective: connect to Athena, and for each database list the table, the colunms and the data type and store this in anothe table.

import pyathena
from pandas_profiling import ProfileReport
from pyathena import connect
from pyathena.pandas_cursor import PandasCursor

#%%

cursor_pandas = connect(
				 aws_access_key_id='####',
                 aws_secret_access_key='####',
                 s3_staging_dir='####',
                 region_name='us-west-1',
				 cursor_class=PandasCursor).cursor()	
				 
#cursor = connect(
#				 aws_access_key_id='####',
#                 aws_secret_access_key='####',
#                 s3_staging_dir='####',
#                 region_name='us-west-1',
#				 cursor_class=PandasCursor).cursor()

#%%

def insere_banco(banco,tabela,coluna,data_type):
    
    sql = """INSERT INTO teste.metadados VALUES ('%s','%s','%s','%s',CURRENT_DATE)"""%(banco,tabela,coluna,data_type)
    print(sql)
    cursor_pandas.execute(sql)


#%%

sql = "show databases"

df = cursor_pandas.execute(sql).as_pandas()

for index, row in df.iterrows():
    
    banco = row['database_name']
    
    sql = """show tables in %s"""%(banco)
    
    df1 = cursor_pandas.execute(sql).as_pandas()
    
    for index, row in df1.iterrows():
        
        tabela = row['tab_name']
        
        sql = """describe %s.%s"""%(banco,row['tab_name'])		
        
        df2 = cursor_pandas.execute(sql).as_pandas()
        
        for index, row in df2.iterrows():
            
            print(banco + ' | ' + tabela + ' | ' + row['col_name'] + ' | ' + row['data_type'])
            
            insere_banco(banco,tabela,row['col_name'],row['data_type'])
            
#%%
            
sql = """select * from teste.dados"""

df3 = cursor_pandas.execute(sql).as_pandas()

profile = ProfileReport(df3, minimal=True)

profile.to_file(output_file="output.html")

df3_describe = df3.describe()

print(df3_describe.head())
