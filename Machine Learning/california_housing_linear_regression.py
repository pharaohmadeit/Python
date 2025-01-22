# coding: utf-8
get_ipython().run_line_magic('matplotlib', '')
from sklearn.datasets import fetch_california_housing
california = fetch_california_housing()
print(california.DESCR)
california.data.shape
california.target.shape
california.feature_names
import pandas as pd
pd.set_option('display.precision', 4)
pd.set_option('display.max_columns', 9)
pd.set_option('display.width', None)
california_df = pd.DataFrame(california.data, columns=california.feature_names)
california_df['MedHouseValue'] = pd.Series(california.target)
california_df.head()
california_df.describe()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(california.data, california.target, random_state=11)
X_train.shape
X_test.shape
from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)
for i, name in enumerate(california.feature_names):
    print(f'{name:>10}: {linear_regression.coef_[i]}')
    
predicted = linear_regression.predict(X_test)
expected = y_test
predicted[:5]
expected[:5]
df = pd.DataFrame()
df['Expected'] = pd.Series(expected)
df['Predicted'] = pd.Series(predicted)
import matplotlib.pyplot as plt
import seaborn as sns
figure = plt.figure(figsize=(5, 5))
axes = sns.scatterplot(data=df, x='Expected', y='Predicted', hue='Predicted', palette='cool', legend=False)
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
axes.set_xlim(start, end)
axes.set_ylim(start, end)
line = plt.plot([start, end], [start, end], 'k--')
plt.tight_layout()
from sklearn import metrics
metrics.r2_score(expected, predicted)
metrics.mean_squared_error(expected, predicted)
from sklearn.linear_model import ElasticNet, Lasso, Ridge
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
from sklearn.model_selection import KFold, cross_val_score
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=california.data, y=california.target, cv=kfold, scoring='r2')
    print(f'{estimator_name:>16}: ' + f'mean of r2 scores={scores.mean():.3f}')
    
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=california.data, y=california.target, cv=kfold, scoring='neg_mean_squared_error')
    print(f'{estimator_name:>16}: ' + f'mean of mean squared error values={scores.mean():.3f}')
    
