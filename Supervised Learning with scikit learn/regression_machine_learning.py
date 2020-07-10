# importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# reading dataset into df 
df = pd.read_csv('height_and_weight.csv')
print(df.head())


# plotting scatter plot for height vs weight
plt.scatter(df.Height, df.Weight)
plt.xlabel('Height (M)')
plt.ylabel('Weight (KG)')
plt.show()


# predicting values in regression model
reg = LinearRegression()
reg.fit(df['Height'], df['Weight'])
new_values = np.array([2.2],
						[5.7],
						[4.7])

prediction = reg.predict(new_values)
print(prediction)
