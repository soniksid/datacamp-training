# importing libraries
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 

# reading csv file
df = pd.read_csv('iris_dataset.csv')
data = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# splitting data for train and testing
X_train, X_test, y_train, y_test = train_test_split(data, df['ID'], test_size = 0.2,
												 random_state = 1, stratify = df['ID'])
dt = DecisionTreeClassifier(max_depth=4, criterion='entropy', random_state=1)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
print(accuracy_score(y_test, y_pred))