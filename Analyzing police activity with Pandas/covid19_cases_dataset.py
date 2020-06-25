import pandas as pd
import matplotlib.pyplot as plt

# reading csv file
df = pd.read_csv('covid19_countrywise.csv')
print(df)


# # finding any NaN value
# print(df.isnull())


# # droping missing values
# print(df.dropna())


# # printing datatype of each column
# print(df.dtypes)


# # removing unwanted columns
# df.drop(["1 week change", "1 week % increase"], axis = 'columns', inplace = True)
# print(df.dtypes)


# plotting the countrywise no. of cases and deaths
df1 = df[['Country', 'Deaths']].loc[10:90]
df1.plot(x='Country', y='Deaths', rot =90, kind='bar')
plt.show()
