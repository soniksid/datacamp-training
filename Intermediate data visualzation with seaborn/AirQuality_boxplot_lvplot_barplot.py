#importing packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading files
jdh = pd.read_csv("AirQuality.csv")
jdh1 = jdh.loc[1:287]
fig, ax = plt.subplots()
sns.set_style('darkgrid')


# Categorical plots using boxplot()
sns.boxplot(x='Min', y='State', data=jdh)
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()


# Categorical plots using lvplot(), also called as boxenplot()
sns.boxenplot(x='Max', y='State', data=jdh, hue='Pollutants')
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()


# Categorical plots using barplot()
sns.barplot(x='Max', y='State', data=jdh1, hue='Pollutants')
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()