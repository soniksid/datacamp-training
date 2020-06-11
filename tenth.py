# reading txt files

import numpy as np
import pandas as pd
from sqlalchemy import create_engine 


# file = open('datacamp_sample_file.txt', mode='r') # opening the file
# print(file.read())

# checking whether the file closed or not
# print(file.closed)

# with open('datacamp_sample_file.txt') as file:
#     print(file.readline(5))
#     print(file.readline(5))


# imoprtimg particular columns using numpy
# filename1='AirQuality.csv'
# data = np.loadtxt(filename1, delimiter=',', skiprows=1, usecols = [7, 8], dtype=str)
# print(data)


# loading excel file using pandas
# file = 'AirQuality.xlsx'
# data = pd.ExcelFile(file)
# print(data.sheet_names)
# df = data.parse('Sheet1')
# print(df)


# extracting data from database
# engine = create_engine('sqlite:///database.sqlite')
# names = engine.table_names()
# print(names)


# making sqlite file into dataframe
# engine1 = create_engine('sqlite:///database.sqlite')
# con = engine1.connect()
# rs = con.execute("SELECT * FROM Match")
# df = pd.DataFrame(rs.fetchall())
# df.columns = rs.keys() #making columns names 
# con.close()
# print(df.head())


#simple code to make sql file into a dataframe
engine1 = create_engine('sqlite:///database.sqlite')
df = pd.read_sql_query("SELECT * FROM Match", engine1)
print(df.head())

