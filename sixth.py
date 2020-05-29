import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


jdh= pd.read_csv("AirQuality.csv")
jdh.fillna(0)
# abcd= sns.relplot(x="city", y= "Avg", data= jdh, kind= "line", hue="Pollutants", size="Pollutants")
# abcd.set_xticklabels(rotation=90)

# plt.show()

# sns.catplot(x="city", y="Min", data=jdh, kind="box")
# abcd.set_xticklabels(rotation=90)
# plt.show()

sns.set_style("darkgrid")
abcd= sns.catplot(x="city", y="Min", data=jdh, kind="point")
abcd.fig.suptitle("Pollution in different cities", y=1)
abcd.set(xlabel="CITIES", ylabel="PLLUTANTS")
plt.xticks(rotation=90)
plt.show()

