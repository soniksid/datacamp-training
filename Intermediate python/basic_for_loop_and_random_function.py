# if statement for area
area = 18
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

# importing random
import random  


# iteration over a list using shuffle
li = [1, 4, 5, 10, 2] 
random.shuffle(li)
for i in range(0, 5):
    print(li[i])