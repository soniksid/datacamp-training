# importing libraries 
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# reading dataset into df 
df = pd.read_csv('iris_dataset.csv')
data = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
print(df.head())
print(df.shape)


# storing data using .fit() fn.
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(data, df['ID'])

# predicting unlabelled values using .predict() fn.
new_values = np.array([[2.2, 5.2, 3.6, 4.2],
						[5.7, 2.6, 3.8, 1.2],
						[4.7, 3.2, 1.3, 1.9]])

prediction = knn.predict(new_values)
print("Predictions are : {}".format(prediction))


# Finding the accuracy of our model with knn=8
X_train, X_test, y_train, y_test = train_test_split(data, df['ID'], test_size = 0.2, random_state = 30, stratify = df['ID'])
knn = KNeighborsClassifier(n_neighbors = 8)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(y_pred)
print(knn.score(X_test, y_test))


# printing confusion matrix
X_train, X_test, y_train, y_test = train_test_split(data, df['ID'], test_size = 0.4, random_state=42)
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
