# CLeaning data in python
import pandas as pd


# printing all information about the dataframe
df = pd.read_csv('AirQuality.csv')
print(df.describe())


