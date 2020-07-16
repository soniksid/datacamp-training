import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.manifold import TSNE

# reading csv file
df = pd.read_csv('jdh_temp.csv')
print(df)


# # Hierarchial clustering
# mergings = linkage(df['pollution'], method='complete')
# # Plotting the dendrogram
# dendrogram(mergings,
# 			labels=df[['jdh_avg_temp(in_celcius)', 'pollution']],
#            leaf_rotation=90,
#            leaf_font_size=6,
# )
# plt.show()


# t-SNE clustering
# reading csv file into samples
samples = pd.read_csv('iris_dataset.csv')
samples = samples[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
samples = np.array(samples)
print(samples)
species = samples['ID']


# Creating a TSNE instance: model
model = TSNE(learning_rate=100)
tsne_features = model.fit_transform(samples)
xs = tsne_features[:,0]
ys = tsne_features[:,1]
# plotting scatter plot
plt.scatter(xs, ys)
plt.show()
