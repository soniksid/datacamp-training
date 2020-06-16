# importing pandas
import pandas as pd


# making dataframes from lists using pandas
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# making dictionary from above lists
my_dict= {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# making dataframe using pandas
cars = pd.DataFrame(my_dict)
cars.index= row_labels
print(cars)