# dictionaries

fam = {'mom': 45, 'dad': 45, 'max': 23, 'sid': 20}
print(fam)

# to add or any data in dictionary:- use fam['key']: 'values'
fam['daadi']= '68'
print(fam)

# making dataframes from lists using pandas

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd

my_dict= {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars = pd.DataFrame(my_dict)
cars.index= row_labels

print(cars)

# learning conditional statements (for)
area = 18

# if statement for area
if area>15 :
    print("big place!")

# code for "for" loop
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         

for room, area in house:
    print("the " + str(room ) +  " is " +  str(area)+ " sqm")

# random number generator
import random  

   


li = [1, 4, 5, 10, 2] 
random.shuffle(li)
for i in range(0, 5):
    print(li[i])