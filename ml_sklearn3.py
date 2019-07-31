import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

house_data = pd.read_csv('melbourne-housing-market/Melbourne_housing_FULL.csv')

# explore data
print(house_data.describe())
print(house_data.head())

print(house_data.columns)

# handle missing
print('# of missings')
print(house_data.columns)
print(house_data.isna().sum())

house_data = house_data.dropna(axis=0)
print(house_data.describe())

print(house_data.info())

obj_col = ['Suburb', 'Address', 'Type',
           'Method', 'SellerG', 'Date',
           'CouncilArea', 'Regionname',
           ]
# remove obj attributes
house_data = house_data.drop(obj_col, axis=1)
print(house_data.info())

y = house_data['Price']
X = house_data.drop(['Price'], axis=1)
print('y', y.head())
print('X columns', X.columns)

# split into 3 parts (train, val, test)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    train_size=0.8)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,
                                                  train_size=0.8)
# parameter tuning
results = {}
for i in range(100, 301, 100):
    model = RandomForestRegressor(n_estimators=i)
    model.fit(X_train, y_train)
    y_preds = model.predict(X_val)
    result = mean_absolute_error(y_true=y_val, y_pred=y_preds)
    print('mae for n_estimators={} is {}'.format(i, result))
    results[i] = result

print('best mae', min(results.values()))
best_est = sorted([(v, k) for k, v in results.items()])[0][1]
print('best estimator num', best_est)

print('evaluation ')
model = RandomForestRegressor(n_estimators=best_est)
model.fit(X_train, y_train)
y_preds = model.predict(X_test)
result = mean_absolute_error(y_true=y_test, y_pred=y_preds)
print('result ', result)
