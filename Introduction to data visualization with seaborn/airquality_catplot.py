import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading csv file
jdh= pd.read_csv("AirQuality.csv")
jdh.fillna(0)

#making categorical plot 
abcd = sns.catplot(x="city", y="Min", data=jdh, kind="box")
abcd.set_xticklabels(rotation=90)
plt.show()