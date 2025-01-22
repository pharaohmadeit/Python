# coding: utf-8
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.DESCR)
iris.data.shape
iris.target.shape
iris.target_names
iris.feature_names
import pandas as pd
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', None)
iris.target
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = [iris.target_names[i] for i in iris.target]
iris_df.head()
pd.set_option('display.precision', 2)
iris_df.describe()
iris_df['species'].describe()
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=11)
kmeans.fit(iris.data)
print(kmeans.labels_[0:49])
print(kmeans.labels_[50:100])
print(kmeans.labels_[100:150])
from sklearn.decomposition import PCA
pca = PCA(n_components=2, random_state=11)
pca.fit(iris.data)
iris_pca = pca.transform(iris.data)
iris_pca.shape
iris_pca_df = pd.DataFrame(iris_pca, columns=['Component1', 'Component2'])
iris_pca_df['species'] = iris_df.species
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.1)
sns.set_style('whitegrid')
kmeans.cluster_centers_
iris_centers = pca.transform(kmeans.cluster_centers_)
axes = sns.scatterplot(data=iris_pca_df, x='Component1', y='Component2', hue='species', legend='brief', palette='cool')
dots = plt.scatter(iris_centers[:,0], iris_centers[:,1], s=100, c='k')
from sklearn.cluster import DBSCAN, MeanShift, SpectralClustering, AgglomerativeClustering
estimators = {
    'KMeans': kmeans,
    'DBSCAN': DBSCAN(),
    'MeanShift': MeanShift(),
    'SpectralClustering': SpectralClustering(n_clusters=3),
    'AgglomerativeClustering': AgglomerativeClustering(n_clusters=3)
}
import numpy as np
for estimator_name, estimator_object in estimators.items():
    estimator_object.fit(iris.data)
    print(f'\n{estimator_name}:')
    for i in range(0, 101, 50):
        labels, counts = np.unique(estimator_object.labels_[i:i+50], return_counts=True)
        print(f'{i}-{i+50}:')
        for label, count in zip(labels, counts):
            print(f'    {label=}, {count=}')
            
plt.show()
