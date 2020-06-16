# importing matplotlib and pandas
import matplotlib.pyplot as plt 
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


# making table from dataframe
electric_usage = pd.DataFrame(elec_dict)
electric_usage.index = row_labels
print(electric_usage)


# making histogram of the above dataframe
electric_usage["Energy_Usage(MegaWatt)"].hist(alpha=0.5)
electric_usage["Population(Billions)"].hist(alpha=0.2)
plt.legend("Type_of_phase")
plt.show()