# reading txt files

import numpy as np
import pandas as pd


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
file = 'AirQuality.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
df = data.parse('Sheet1')
print(df)

