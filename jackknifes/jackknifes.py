import numpy as np
import matplotlib.pyplot as plt

import time
# Source principale: http://www.stat.berkeley.edu/~hhuang/STAT152/Jackknife-Bootstrap.pdf



def single_jk(data):
    means = []
    for i in range(len(data)):
        means.append(np.mean(np.delete(data,i)))

    means = np.array(means)
    mean_means = np.mean(means)
    # print 'm0', mean_means
    return (len(data) - 1) / float(len(data)) * np.sum(np.power(mean_means - means ,2))


def get_subsets_indices(mypoints, jackknife_size, total_number_of_jackknife=1):

	subsets_indices = []
	for jackknife_number in range(1, total_number_of_jackknife + 1):
		# same as np function but returns the array
		shuffle_returns = lambda x: (np.random.shuffle(x), x)[1]

		# print jackknife_number, int(np.ceil(jackknife_number*jackknife_size/float(mypoints.number_of_points))),((jackknife_number - 1) % (mypoints.number_of_points / jackknife_size ) * jackknife_size )

		np.random.seed(seed=int(np.ceil(jackknife_number*jackknife_size/float(len(mypoints)))))
                # print int(np.ceil(jackknife_number*jackknife_size/float(len(mypoints))))

		shuffled_list_indices = shuffle_returns(np.arange(len(mypoints)))
		# Jackknife number of 0 means we are not removing anyone.
		if jackknife_number > 0:
			index = ((jackknife_number - 1) % (len(mypoints) / jackknife_size ) * jackknife_size)
			subset_to_append = np.sort(
				np.delete(
					shuffled_list_indices,
					np.arange(
						index,
						np.min([index + jackknife_size, len(mypoints)]))))
                        # print np.arange( index, np.min([index + jackknife_size, len(mypoints)]))
			subsets_indices.append(subset_to_append)
		else:
			raise("Shouldn't be there")

	return np.array(subsets_indices)

def block_jk(data):
    NB_BLOCK = 1000
    SIZE_BLOCK = 1
    subs = get_subsets_indices(data, SIZE_BLOCK, NB_BLOCK * SIZE_BLOCK)

    means = []
    for s in subs:
        means.append(np.mean(data[s]))

    means = np.array(means)
    mean_means = np.mean(means)
    prop_data = (len(data) - SIZE_BLOCK) / float(SIZE_BLOCK)
    # # print 'm0', mean_means
    # return (99 ) / (float(100)) * np.sum(np.power(np.mean(data) - means, 2))
    return (prop_data  / len(means)) * np.sum(np.power(mean_means - means, 2))


# real_variance = np.power(np.std(data)/np.sqrt(float(len(data))),2)
# single_jk_variance = single_jk(data)
# block_jk_variance = block_jk(data)
# print 'Real Variance', real_variance
# print 'single_jk    ', single_jk_variance
# print 'block_jk     ', block_jk_variance
# print 'error single_jk', np.absolute(real_variance - single_jk_variance)
# print 'error block_jk', np.absolute(real_variance - block_jk_variance)



dist = []
inside = 0
inside_truth = 0
NB_LOOPS = 300
NB_DATA_POINTS = 1000
datas = []
for i in range(NB_LOOPS):
    datas.append(np.random.normal(0, 1, NB_DATA_POINTS))

time0 = time.time()
for i, data in zip(list(range(NB_LOOPS)), datas):
    real_variance = np.power(1./np.sqrt(float(NB_DATA_POINTS)), 2)
    # real_variance = float(len(data))/(len(data) - 1)*np.var(data)/np.power(np.sqrt(float(NB_DATA_POINTS)), 2)

    block_jk_variance = block_jk(data)
    if np.sqrt(real_variance) >= np.abs(np.mean(data)):
        inside_truth += 1
    if np.sqrt(block_jk_variance) >= np.abs(np.mean(data)):
        inside += 1
    # print block_jk_variance, real_variance
    print 'Proportion of error: %f%%' % (100*(block_jk_variance - real_variance) / real_variance)
    dist.append((100*(block_jk_variance - real_variance) / real_variance))


print 'Prop inside one sigma truth', inside_truth/float(NB_LOOPS)
print 'Prop inside one sigma jk', inside/float(NB_LOOPS)
print np.mean(np.abs(dist)), '%'
print 'Time', time.time() - time0
plt.hist(dist)
plt.show()
