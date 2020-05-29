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


# Making Line plot and customizing it
ax.plot(Family_2015["Name"], Family_2015["Height"], linestyle = ':', marker='o')
ax.plot(Family_2020["Name"], Family_2020["Height"], linestyle = 'dashdot', marker='o')
# Giving titles to both axes
ax.set_xlabel("Family Members")
ax.set_ylabel("Height")
ax.set_title("Height vs Name")

plt.show()


