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


# Regression plots using regplot()
jdh = pd.read_csv("jdh_temp.csv")
sns.regplot(x='jdh_avg_temp(in_celcius)', y='pollution', data=jdh, x_estimator=np.mean, order=2)
ax.set(xlabel='Avg Temp', ylabel='Pollution(ppm)', title="Pollution in each state")
plt.show()


# Regression plots using lmplot()
jdh = pd.read_csv("jdh_temp.csv")
sns.lmplot(x='jdh_avg_temp(in_celcius)', y='pollution', data=jdh, hue='rain', col='month')
ax.set(xlabel='Avg Temp', ylabel='Pollution(ppm)', title="Pollution in each state")
plt.show()

# Regression plots using residplot()
jdh = pd.read_csv("jdh_temp.csv")
sns.residplot(x='jdh_avg_temp(in_celcius)', y='pollution', data=jdh)
plt.show()