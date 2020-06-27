# importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# reading population dataset
census = pd.read_csv('India_census_2011.csv')
census.drop(census.iloc[:, 6:118], axis='columns', inplace=True)
df = census.groupby('State name').mean().reset_index()
print(df)


# # plotting histogram of male polpulatin statewise wise
# sns.set()
# plt.hist(df['Male'], bins=24)
# plt.show()


# plotting swarm plot of district wise population in each state using seaborn
# df1 = sns.swarmplot(x='State name', y='Male', data=census)
# df1.set_xticklabels(df1.get_xticklabels(), rotation = 90) #setting xlabel to 90 deg
# plt.show()



# plotting ECDF plots
x = np.sort(df['Male'])
y = np.arange(1, len(x)+1)/ len(x)
plt.plot(x, y, marker = '.', linestyle = 'none')
plt.show()


