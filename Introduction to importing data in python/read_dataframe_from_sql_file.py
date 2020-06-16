# importing packages
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


# making sqlite file into dataframe
engine1 = create_engine('sqlite:///database.sqlite')
con = engine1.connect()
rs = con.execute("SELECT * FROM Match") # (*)means to select all columns
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys() #making columns names 
con.close()
print(df.head())


#simple code to make sql file into a dataframe
engine1 = create_engine('sqlite:///database.sqlite')
df = pd.read_sql_query("SELECT * FROM Match", engine1)
print(df.head())