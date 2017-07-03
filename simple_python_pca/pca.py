#!/usr/bin/env python
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# import seaborn

from sklearn import decomposition


# Try to use content in argv[1] o/w uses stdin
try:
	input_name = sys.argv[1]
	f = open(input_name, 'r')
except:
	input_name = 'stdin'
	f = sys.stdin

# Trying to load the markers
try:
	markers = map(int, np.loadtxt('markers.txt'))
	HAS_MARKER = True
except:
	HAS_MARKER = False

print "loading data"
X = np.genfromtxt(sys.stdin, dtype=np.int, delimiter=1)
# X = np.array(map(lambda l: [int(c) for c in l[:-1]], f))
y = np.array([0]*int(len(X)/2.) + [1]*int(len(X)/2.) )


def thinning_genotypes(X, skip=10):
    return X[:,::skip]

# X = thinning_genotypes(X)

fig = plt.figure(1, figsize=(16, 12))
# plt.clf()
ax = fig.add_subplot(111)  # Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

print 'Starting decomposition'
# plt.cla()
pca = decomposition.PCA(n_components=2)
pca.fit(X)
X = pca.transform(X)

if not HAS_MARKER:
	for p in range(len(X)):
		ax.scatter(X[p, 0], X[p, 1], marker=r"$%d$" % markers[p], c=markers[p])#, cmap=plt.cm.spectral)
else:
	ax.scatter(X[:, 0], X[:, 1], marker='o', c=markers)


plt.xlabel('PC1 (%.1f%%)' % pca.explained_variance_ratio_[0]*100, fontsize=17)
plt.xlabel('PC2 (%.1f%%)' % pca.explained_variance_ratio_[1]*100, fontsize=17)
plt.savefig('%s.pdf' % 'pca')


