import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading files
jdh = pd.read_csv("AirQuality.csv")
fig, ax = plt.subplots()
sns.set_style('darkgrid')

# Categorical plots using stripplot()
sns.stripplot(x='Min', y='State', data=jdh, jitter=True)
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()


# Categorical plots using swarmplot()
sns.swarmplot(x='Min', y='State', data=jdh)
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()


# Categorical plots using violinplot()
sns.violinplot(x='Min', y='State', data=jdh)
ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
plt.show()