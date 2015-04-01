#!/usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import seaborn

from sklearn import decomposition
from sklearn import datasets

np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target
f = open(sys.argv[1], 'r')
X = np.array(map(lambda l: [int(c) for c in l[:-1]], f))
y = np.array([0]*int(len(X)/2.) + [1]*int(len(X)/2.) )

fig = plt.figure(1, figsize=(8, 6))
# plt.clf()
ax = fig.add_subplot(111)  # Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

# plt.cla()
pca = decomposition.PCA(n_components=2)
pca.fit(X)
X = pca.transform(X)

# for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
#     ax.text3D(X[y == label, 0].mean(),
#               X[y == label, 1].mean() + 1.5,
#               X[y == label, 2].mean(), name,
#               horizontalalignment='center',
#               bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.spectral)

# x_surf = [X[:, 0].min(), X[:, 0].max(),
#           X[:, 0].min(), X[:, 0].max()]
# y_surf = [X[:, 0].max(), X[:, 0].max(),
#           X[:, 0].min(), X[:, 0].min()]
# x_surf = np.array(x_surf)
# y_surf = np.array(y_surf)
# v0 = pca.transform(pca.components_[0])
# v0 /= v0[-1]
# v1 = pca.transform(pca.components_[1])
# v1 /= v1[-1]

# ax.w_xaxis.set_ticklabels([])
# ax.w_yaxis.set_ticklabels([])
# ax.w_zaxis.set_ticklabels([])

ax.set_title(sys.argv[1])
ax.set_xlabel(pca.explained_variance_ratio_[0])
ax.set_ylabel(pca.explained_variance_ratio_[1])

plt.savefig('%s.jpg' % sys.argv[1])



exit(1)

# import numpy as np
# from sklearn.decomposition import PCA

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 20)
# pca = PCA(n_components=2)
# pca.fit(X)

# print(pca.explained_variance_ratio_)



