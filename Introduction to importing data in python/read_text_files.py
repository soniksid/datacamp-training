# importing packages
import numpy as np
import pandas as pd
from sqlalchemy import create_engine 

# opening the file
file = open('datacamp_sample_file.txt', mode='r') 
print(file.read())

# checking whether the file closed or not
print(file.closed)

# with open('datacamp_sample_file.txt') as file:
print(file.readline(5))
print(file.readline(5))