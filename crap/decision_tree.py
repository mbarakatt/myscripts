import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns


grid = np.array([(i,j) for i in range(-5,5) for j in range(-5,5)]) + (0.2,0.2)
data = np.array(zip(np.random.random(10000) - 0.5, np.random.random(10000) - 0.5)) *2 *6
# print 'data ', grid


# def get_labels(data):
#	 """Using the 4 quadrants"""
# 	labels = []
# 	for d in data:
# 		if d[0] >= 0 and d[1] >= 0:
# 			labels.append(1)
# 		if d[0] < 0 and d[1] >= 0:
# 			labels.append(2)
# 		if d[0] < 0 and d[1] < 0:
# 			labels.append(3)
# 		if d[0] >= 0 and d[1] < 0:
# 			labels.append(4)

# 	labels = np.array(labels)
# 	return labels

def get_labels(data):
	a = 2
	b = 0
	labels = []
	for d in data:
		if d[1] - d[0]*a - b  >= 0:
			labels.append(0)
		else:
			labels.append(1)
	return np.array(labels)

labels = get_labels(data)
labels_grid = get_labels(grid)

# print 'labels', labels

# rfc = RandomForestClassifier(n_estimators=10)
rfc = DecisionTreeClassifier(min_samples_split=2)
rfc.fit(data, labels)

# transformed_x = rfc.fit_transform(data, labels)

# pred = rfc.predict(data)
pred = rfc.predict(grid)
# print zip(data, transformed_x, pred)[0:10]
print 'Accuracy', list(pred - labels_grid).count(0)/float(len(labels_grid))
# print 'trees', rfc.estimators_

xs = np.linspace(-3,3,50)
ys = xs*2 + 0

plt.plot(xs, ys)
plt.scatter(grid[:,0],grid[:,1], color=[sns.color_palette()[n] for n in pred])
plt.scatter(data[:,0],data[:,1], s=2, color='black', alpha=0.2)
plt.show()
