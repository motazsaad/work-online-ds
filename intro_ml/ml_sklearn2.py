import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
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

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    train_size=0.8,
                                                    test_size=0.2)

print('train:')
print('X', X_train.head())
print('y', y_train.head())

print('test')
print('X', X_test.head())
print('y', y_test.head())

# input()

# define model
# model = DecisionTreeClassifier(random_state=1)
model = GaussianNB()
print(model)

# train model
model.fit(X_train, y_train)


# predict
preds = model.predict(X_test)

# print(preds)

# evaluate

score = accuracy_score(y_true=y_test, y_pred=preds)
print('accuracy=', score)