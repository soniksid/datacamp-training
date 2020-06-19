import re
import pandas as pd
from numpy import NaN


df = pd.read_csv('AirQuality.csv')
pattern = re.compile('[Delhi]')

def func(column):
	state = column['State']
	if bool(pattern.match(state)):
		state = state.replace("Delhi" , "DELHI")
		return state
	else:
		return (NaN)
# printing only 40 values of the state column 
df = df.apply(func, axis = 1,).loc[40:80]
print(df)



