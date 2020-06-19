# importing packages
import pandas as pd
import glob


# printing all information about the dataframe
df1 = pd.read_csv('jdh_temp.csv')
df2 = pd.read_csv('AirQuality.csv')
print(df1.describe())


# concatenating two dataframes
df3 = pd.concat([df2, df1], ignore_index= True, join = 'outer')
print(df3)


# finding files and concatenating it
match = '*.csv'
csv_files = glob.glob(match)
csv_data = []    #creating empty lists
for files in csv_files:
	data = pd.read_csv(files)
	csv_data.append(data)
df = pd.concat(csv_data)
print(df)