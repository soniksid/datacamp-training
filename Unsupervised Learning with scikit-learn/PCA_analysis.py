# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr
from sklearn.decomposition import PCA


# reading csv file
df = pd.read_csv('iris_dataset.csv')
df1 = df[['SepalLengthCm', 'PetalLengthCm']]
df1 = np.array(df1)
width = df1[:, 0]
length = df1[:, 1]
# # plotting Scatter plot width vs length
# plt.scatter(width, length)
# plt.axis('equal')
# plt.show()

# # Calculating the Pearson correlation
# correlation, pvalue = pearsonr(width, length)
# print(correlation)


# # plotting scatter plot after PCA
# model = PCA()
# pca_features = model.fit_transform(df1)
# xs = pca_features[:,0]
# ys = pca_features[:,1]
# # Scatter plot xs vs ys
# plt.scatter(xs, ys)
# plt.axis('equal')
# plt.show()

# # Calculate the Pearson correlation of xs and ys
# correlation, pvalue = pearsonr(xs, ys)
# print(correlation)


# plotting bar plot of variance of PCA features
# creating array of Versicolor species
samples = df.loc[51:99, :]
samples = samples[['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm']]
print(samples.head())
pca = PCA()
pca.fit(samples)
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()
