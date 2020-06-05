import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

jdh= pd.read_csv("AirQuality.csv")
jdh.fillna(0)

sns.distplot(jdh['Min'], hist= True, rug= True)
plt.show()

