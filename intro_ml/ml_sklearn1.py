import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score # suitable for nominal class
# load data
iris_data = pd.read_csv('my_iris.csv')

print('data\n', iris_data.head())

# prepare data
y = iris_data.species
print('y\n', y.tail())


X = iris_data.drop(['species'], axis=1)
print('X\n', X.head())

# define model
# model = DecisionTreeClassifier(random_state=1)
model = GaussianNB()
print(model)

# train model
model.fit(X, y)


# predict
preds = model.predict(X)

# print(preds)

# evaluate

score = accuracy_score(y_true=y, y_pred=preds)
print('accuracy=', score)