# importing matplotlib
import matplotlib.pyplot as plt


# population in billions
year = [1990, 2000, 2001, 2002, 2003, 2004]
pop = [1, 2, 3.1, 3.5, 6, 6.8]

# simple plot between year and pop
plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('population')
plt.show()
plt.clf()