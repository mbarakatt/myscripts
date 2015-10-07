import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn
import itertools





if False:
	diff = []
	for i in range(10, 100):
		np.random.seed(int(time.time()))
		a = np.random.random(i)
		print a
		subsets = np.array([np.delete(a,j) for j in range(i)])

		thetas = np.mean(subsets, axis=1)
		print np.mean(thetas), np.mean(a)
		n = float(i)
		t1 = (n-1)/n * np.sum(np.power(thetas - np.mean(thetas),2))
		t2 = np.var(a)*n/(n-1)/(n)
		print t1 > t2, (t1 - t2)/t2
		diff.append((t1 - t2)/t2)

	plt.plot(range(len(diff)), diff)
	plt.show()

# Testing with block size of 2
if True:
	diff = []
	block_size = 2
	for i in range(10, 1000, block_size):
		np.random.seed(int(time.time()))
		a = np.random.random(i)
		# print a
		# subsets = np.array([j for j in itertools.combinations(a, i - block_size)])  # this is with all subsets of the right size
		subsets = np.array([np.delete(a,[j, j+1]) for j in range(0, i, block_size)])
		# print subsets
		# print subsets
		thetas = np.mean(subsets, axis=1)
		# print np.mean(thetas), np.mean(a)
		# print len(subsets)
		n = float(i)
		t1 = (n-block_size)/(float(block_size)*len(subsets)) * np.sum(np.power(thetas - np.mean(thetas),2))
		t2 = np.var(a)*n/(n-1)/(n)
		print t1 > t2, (t1 - t2)/t2, t1, t2
		diff.append((t1 - t2)/t2)

	plt.plot(range(len(diff)), diff)
	plt.show()










if False:
	diff = []
	for i in range(40, 200, 10):
		block_size = 10
		np.random.seed(int(time.time()))
		a = np.random.random(i)

		subsets = np.array([np.random.choice(a,i - block_size,replace=False) for j in range(len(a)*100)])

		thetas = np.mean(subsets, axis=1)
		n = float(len(a))
		t1 = (n - block_size)/float(block_size*len(subsets)) * np.sum(np.power(thetas - np.mean(thetas),2))
		t2 = np.var(a)/(n)
		print t1 > t2, (t1 - t2)/t2
		diff.append((t1 - t2)/t2)

	plt.plot(range(len(diff)), diff)
	plt.show()

