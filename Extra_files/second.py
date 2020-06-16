# plotting graphs using matplotlib package
import matplotlib.pyplot as plt


# population in billions
year = [1990, 2000, 2001, 2002, 2003, 2004]
pop = [1, 2, 3.1, 3.5, 6, 6.8]

plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('population')
plt.show()
plt.clf()

# to plot graphs using scatter() and xscale('log') 
plt.scatter(year, pop)
plt.xscale('log')
plt.show()
plt.clf()

