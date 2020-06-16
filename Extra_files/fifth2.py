import pandas as pd
import matplotlib.pyplot as plt


Family_2015 = pd.DataFrame(
   {
      'Height': [130, 120, 104, 160, 168],
      'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung']
   }
)

Family_2020 = pd.DataFrame(
   {
      'Height': [150, 160, 120, 165, 170],
      'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung']
   }
)


print(Family_2015, "\n")

print(Family_2020, "\n\n\n")

fig, ax = plt.subplots()


# Making bar plot and customizing it
ax.bar(Family_2015["Name"], Family_2015["Height"], label= "Family in 2015", color= "red")
ax.bar(Family_2020["Name"], Family_2020["Height"], bottom=Family_2015["Height"], label= "Family in 2020", color= "grey")

# Giving titles to both axes
ax.set_xlabel("Family Members")
ax.set_ylabel("Height(cm)")
ax.set_title("Height vs Name")
ax.legend()
plt.show()