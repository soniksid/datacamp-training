#Reading Multiple Data Files 


import pandas as pd

phase = ['single', 'single', 'three', 'single', 'three', 'three']
usage_people = [20, 30, 50.5, 60, 68, 80]
countries = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco']
energy_usage = [18.2, 10, 15, 20, 16, 2.5]

# making dictionariy from above list
elec_dict = {"Type_of_phase": phase, "Population(Billions)": usage_people, "Countries": countries, "Energy_Usage(MegaWatt)": energy_usage}
# giving labels to each row
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR']

# making table from dataframe
electric_usage= pd.DataFrame(elec_dict)
electric_usage.index = row_labels
print(electric_usage)

# head of the table data
print(electric_usage.head(), "\n\n\n\n")


# merging dataframes using .merge()

table1 = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})

table2 = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(table1, "\n")
print(table2, "\n\n\n")

# merging dataframes on two keys
print(pd.merge(table1, table2, on=["id", "subject_id"]))