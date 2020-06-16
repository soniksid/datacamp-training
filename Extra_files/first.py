print("\nOUTPUT BEGINS")

#  addition
a = "Addition of 4 and 5 is "
b = 4 + 5
print(a + str(b))

# exponentiation
a = "exponentiation of 4 and 2 is "
b = 4 ** 2
print(a + str(b))

# modulo
a = "modulo of 18 and 7 is "
b = 18%7
print(a + str(b))


# assigning variables
height = 1.79
weight = 68.7
print(type(height))

# calculation of BMI
a = "BMI is "
bmi = weight / height**2
print(a + str(bmi))

# to see the type of a variable
print(type(bmi))

# to calculate the amount of money after 7 years investing $100
savings = "amount of money after 7 years investing in $100 is "
growth_multiplier = (100)*(1.1)**(7)
print(savings + str(growth_multiplier))


# to create list of age
mom = 42
dad = 45
sid = 20
daadi = 56.1
family = [mom, dad, sid, daadi]
print(max(family))


# to print area and circumference by importing math package
r = 0.43
import math
circum = 2* math.pi*r
area = math.pi*r*r
print(circum)
print(area)

# to calculate distance using radians() from math package
r = 192500
from math import radians
dist = r*radians(12)
print(dist)


# addition of lists and array
import numpy as np
python_list= [1, 2, 3]
np_array=np.array([1, 2, 3])
plc = python_list + python_list
print(plc)




