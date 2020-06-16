import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# reading csv file
jdh= pd.read_csv("AirQuality.csv")
jdh.fillna(0)


# setting styles to plot
sns.set_style("darkgrid")
abcd= sns.catplot(x="city", y="Min", data=jdh, kind="point")
abcd.fig.suptitle("Pollution in different cities", y=1)
abcd.set(xlabel="CITIES", ylabel="PLLUTANTS")
plt.xticks(rotation=90)
plt.show()