import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# reading population dataset
census = pd.read_csv('India_census_2011.csv')
census.drop(census.iloc[:, 6:118], axis='columns', inplace=True)
df = census.groupby('State name').mean().reset_index()
print(df)


# plotting scatter plot
plt.plot(df['Female'], df['Male'], marker='.', linestyle= 'none')
plt.xlabel('Female')
plt.ylabel('Male')

# finding slope(a) and intercept(b) using np.polyfit()
a, b = np.polyfit(df['Female'], df['Male'], 1)

# making theoretical line to plot (f = a * i + b)
x = np.array([0, 5899900])
y = a * x + b
plt.plot(x, y)
plt.show()


# plotting ECDF plots using bootstrap methods
# making ecdf function
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

for _ in range(100):
	df_sample = np.random.choice(df['Male'], size=len(df['Male']))

x, y = ecdf(df_sample)
plt.plot(x, y, marker= '.', linestyle= 'none', alpha=0.1, color = 'gray')

# making another ecdf plot without bootstrap method
x, y = ecdf(df['Male'])
plt.plot(x, y, marker='.')
plt.margins(0.02)
plt.xlabel('Male population')
plt.ylabel('ECDF')
plt.show()


# defining a bootstrap function with
def bootstrap(data, func):
	df_sample = np.random.choice(data, len(data))
	return func(df_sample)


#making bootstrap replicates using for loops
df_replicas = np.empty(10000) # making empty array to create 10,000 replicates  
for i in range(10000):
	df_replicas[i] = bootstrap(df['Male'], np.mean)

# potting histogram of bootstrap replicates
plt.hist(df_replicas, bins = 50)
plt.show()


# making a function for bootstrap pair returning slope and intercept
def bs_pairs(x, y, size=1):
    inds = np.arange(len(x))
    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope = np.empty(size)
    bs_intercept = np.empty(size)
    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope[i], bs_intercept[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope, bs_intercept

# plotting histogram for male and females
bs_slope, bs_intercept = bs_pairs(df['Male'], df['Female'], size=1)
plt.hist(bs_slope, bins=50)
plt.xlabel('Male')
plt.ylabel('Female')
plt.show()











