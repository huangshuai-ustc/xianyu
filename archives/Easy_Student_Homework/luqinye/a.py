import numpy as np
from sklearn.cluster import KMeans

x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
cluster = KMeans(n_clusters=2)
cluster.fit(x)
labels = cluster.labels_
print("labels:\n", labels)
# 新数据点
x_new = np.array([[2, 1], [6, 9]])
labels_new = cluster.predict(x_new)
print("labels_new:\n", labels_new)
