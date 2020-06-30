import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# reading population dataset
census = pd.read_csv('India_census_2011.csv')
census.drop(census.iloc[:, 6:118], axis='columns', inplace=True)
df = census.groupby('State name').mean().reset_index()
print(df)


# plotting scatter plot
plt.plot(df['Female'], df['Male'], marker='.', linestyle= 'none')
plt.xlabel('Female')
plt.ylabel('Male')

# finding slope(a) and intercept(b) using np.polyfit()
a, b = np.polyfit(df['Female'], df['Male'], 1)

# making theoretical line to plot (f = a * i + b)
x = np.array([0, 5899900])
y = a * x + b
plt.plot(x, y)
plt.show()