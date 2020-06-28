# importing packeges
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



# reading csv files
census = pd.read_csv('India_census_2011.csv')
census.drop(census.iloc[:, 6:118], axis='columns', inplace=True)
df = census.groupby('State name').mean().reset_index()
df1 = df.loc[1:10]
print(df)


# plotting boxplot using seaborn
sns.set()
census1 = sns.boxplot(x = 'State name', y = 'Male', data = census)
census1.set_xticklabels(census1.get_xticklabels(), rotation = 75)
plt.xlabel('States')
plt.ylabel('Population')
plt.show()