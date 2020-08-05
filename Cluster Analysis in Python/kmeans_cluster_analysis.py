from scipy.cluster.vq import kmeans, vq
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
random.seed((1000, 2000))
# making list  of data points 
x_data = [12.0, 10.0, 11.0, 13.0, 15.0, 42.0, 52.0, 58.0, 49.0, 52.0, 83.0, 78.0, 92.0, 88.0, 70.0]
y_data = [14.0, 12.0, 12.0, 10.0, 11.0, 44.0, 45.0, 66.0, 57.0, 58.0, 85.0, 82.0, 93.0, 85.0, 89.0]

# making dataframe
df = pd.DataFrame({'x': x_data,
					'y': y_data})

# Compute cluster centers
centroids,_ = kmeans(df, 3)

# Assign cluster labels
df['cluster_labels'], _ = vq(df, centroids)

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()