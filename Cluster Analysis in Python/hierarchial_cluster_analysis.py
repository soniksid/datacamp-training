from scipy.cluster.hierarchy import linkage, fcluster
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# making list  of data points 
x_data = [12, 10, 11, 13, 15, 42, 52, 58, 49, 52, 83, 78, 92, 88, 70]
y_data = [14, 12, 12, 10, 11, 44, 45, 66, 57, 58, 85, 82, 93, 85, 89]

# making dataframe
df = pd.DataFrame({'x': x_data,
					'y': y_data})

# computing distances
Z = linkage(df, 'ward')
df['cluster_labels'] = fcluster(Z, 2, criterion='maxclust')

# plotting points
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()