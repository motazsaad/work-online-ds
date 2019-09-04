import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score # suitable for nominal class
# load data
iris_data = pd.read_csv('iris.csv')

print('data\n', iris_data.head())


# prepare data
y = iris_data.Species
print('y\n', y.tail())

X = iris_data.drop(['Species'], axis=1)
print('X\n', X.head())


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


# define model
max_depths = np.linspace(1, 32, 32, endpoint=True)
train_results = []
test_results = []
for max_depth in max_depths:
    model = DecisionTreeClassifier(max_depth=max_depth,random_state=1)
    # model = GaussianNB()
    #print(model)
    # train model
    model.fit(X_train, y_train)
    # predict
    preds = model.predict(X_test)
    # print(preds)
    # evaluate
    score = accuracy_score(y_true=y_test, y_pred=preds)
    print('accuracy=', score)
    if score != 1 :
        print('max_depth =', max_depth)