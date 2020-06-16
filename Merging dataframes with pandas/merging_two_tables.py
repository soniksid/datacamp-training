# importing pandas
import pandas as pd


# merging dataframes using .merge()
table1 = pd.DataFrame(
   {'id':[1,2,3,4,5],
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