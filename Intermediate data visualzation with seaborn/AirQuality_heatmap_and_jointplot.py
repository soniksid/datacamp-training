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


# matrix plots using heatmap(). crosstab() is used to change numerical values in matrix which will be readable by heatmap()
sns.heatmap(pd.crosstab(jdh['State'], jdh['Min'], values=jdh['Max'], aggfunc='mean').round(0), cmap="coolwarm")
plt.show()


# plots using jointplot()
sns.jointplot(x="Avg", y="Min", kind='reg', data=jdh1)
plt.show()