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


# plotting a distribution plot
sns.set_style('darkgrid')   # setting background style
sns.distplot(jdh['Max'], hist= True, kde= True, ax = ax)
ax.set(xlabel='Max Pollution curve', ylabel='Distribution', xlim=(-20, 600), title="Pollution Graph of India")
plt.show()