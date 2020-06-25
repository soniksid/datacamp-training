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


# Categorical plots using pointplot()
sns.pointplot(y='Max', x='State', data=jdh1, hue='Pollutants')
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()


# Categorical plots using countplot()
sns.countplot(y='State', data=jdh1, hue='Pollutants')
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()