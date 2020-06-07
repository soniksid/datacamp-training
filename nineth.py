# Intermediate data visualization with seaborn
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

jdh = pd.read_csv("AirQuality.csv")
jdh1 = jdh.loc[1:287]
fig, ax = plt.subplots()
sns.set_style('darkgrid')


# plotting a distribution plot
# sns.set_style('darkgrid')   # setting background style
# sns.distplot(jdh['Max'], hist= True, kde= True, ax = ax)
# ax.set(xlabel='Max Pollution curve', ylabel='Distribution', xlim=(-20, 600), title="Pollution Graph of India")
# plt.show()


# Categorical plots using stripplot()
# sns.stripplot(x='Min', y='State', data=jdh, jitter=True)
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()


# Categorical plots using swarmplot()
# sns.swarmplot(x='Min', y='State', data=jdh)
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()


# Categorical plots using violinplot()
# sns.violinplot(x='Min', y='State', data=jdh)
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()

# Categorical plots using boxplot()
# sns.boxplot(x='Min', y='State', data=jdh)
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()


# Categorical plots using lvplot(), also called as boxenplot()
# sns.boxenplot(x='Max', y='State', data=jdh, hue='Pollutants')
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()


# Categorical plots using barplot()
# sns.barplot(x='Max', y='State', data=jdh1, hue='Pollutants')
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()


# Categorical plots using pointplot()
# sns.pointplot(y='Max', x='State', data=jdh1, hue='Pollutants')
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()


# Categorical plots using countplot()
# sns.countplot(y='State', data=jdh1, hue='Pollutants')
# ax.set(xlabel='Min Pollution', ylabel='States', title="Pollution in each state")
# plt.show()

# Regression plots using regplot()
# jdh = pd.read_csv("jdh_temp.csv")
# sns.regplot(x='jdh_avg_temp(in_celcius)', y='pollution', data=jdh, x_estimator=np.mean, order=2)
# ax.set(xlabel='Avg Temp', ylabel='Pollution(ppm)', title="Pollution in each state")
# plt.show()


# Regression plots using lmplot()
# jdh = pd.read_csv("jdh_temp.csv")
# sns.lmplot(x='jdh_avg_temp(in_celcius)', y='pollution', data=jdh, hue='rain', col='month')
# ax.set(xlabel='Avg Temp', ylabel='Pollution(ppm)', title="Pollution in each state")
# plt.show()

# Regression plots using residplot()
# jdh = pd.read_csv("jdh_temp.csv")
# sns.residplot(x='jdh_avg_temp(in_celcius)', y='pollution', data=jdh)
# plt.show()


# matrix plots using heatmap(). crosstab() is used to change numerical values in matrix which will be readable by heatmap()
# sns.heatmap(pd.crosstab(jdh['State'], jdh['Min'], values=jdh['Max'], aggfunc='mean').round(0), cmap="coolwarm")
# plt.show()


# plots using jointplot()
sns.jointplot(x="Avg", y="Min", kind='reg', data=jdh1)
plt.show()