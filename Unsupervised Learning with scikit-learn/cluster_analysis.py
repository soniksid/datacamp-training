import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# reading csv file
samples = pd.read_csv('iris_dataset.csv')
samples = samples[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
samples = np.array(samples)
print(samples)


# Creating a KMeans with 3 clusters
model = KMeans(n_clusters=3)
# Fitting model to points
model.fit(samples)
# Determine the cluster labels of new_points: labels
labels = model.predict(samples)
# Print cluster labels of new_points
print(labels)


# plottng scatter plot of clusters
xs = samples[:,0]
ys = samples[:,2]
plt.scatter(xs, ys, c=labels, alpha=0.5)
centroids = model.cluster_centers_  
#plotting central point of clusters
centroids_x = centroids[:,0]
centroids_y = centroids[:,2]
plt.scatter(centroids_x, centroids_y, marker='D', s=50)
plt.show()