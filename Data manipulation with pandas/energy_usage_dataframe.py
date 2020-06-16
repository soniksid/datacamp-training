# importing pandas as pd
import pandas as pd


# making lists using Pandas
phase = ['single', 'single', 'three', 'single', 'three', 'three']
usage_people = [20, 30, 50.5, 60, 68, 80]
countries = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco']
energy_usage = [18.2, 10, 15, 20, 16, 2.5]


# making dictionariy from above list
elec_dict = {"Type_of_phase": phase, "Population(Billions)": usage_people, "Countries": countries, "Energy_Usage(MegaWatt)": energy_usage}
# giving labels to each row
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR']


# importing pandas as pd
import pandas as pd

# making table from dataframe
electric_usage= pd.DataFrame(elec_dict)
electric_usage.index = row_labels
print(electric_usage)

# head of the table data
print(electric_usage.head())

#  information about table
print(electric_usage.info())

# the shape of table
print(electric_usage.shape)

# description of table
print(electric_usage.describe())

# calculating mean of the population
print(electric_usage["Population(Billions)"].mean())

# to calculate mean over rows
print(electric_usage.mean(axis="index"))

# to calculate mean over columns
print(electric_usage.mean(axis="columns"))