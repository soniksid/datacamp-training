# importing packages
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


# imoprtimg particular columns using numpy
filename1='AirQuality.csv'
data = np.loadtxt(filename1, delimiter=',', skiprows=1, usecols = [7, 8], dtype=str)
print(data)


# loading excel file using pandas
file = 'AirQuality.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
df = data.parse('Sheet1')
print(df)


# extracting data from database
engine = create_engine('sqlite:///database.sqlite')
names = engine.table_names()
print(names)