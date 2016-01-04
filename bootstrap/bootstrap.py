import numpy as np


data = np.random.normal(0,1,600)
def bootstrap(data, number_bs=10000, confidence=0.95):
	"""if confidence is 0.95 returns the 2.5% and 97.5% quantiles"""
	means = []
	for i in range(number_bs):
		means.append(np.mean(np.random.choice(data,size=len(data))))
	sorted_means =  np.sort(means)
	low_quantile = (1 - confidence) / 2
	high_quantile =  confidence + low_quantile
	return sorted_means[int(number_bs*low_quantile)], sorted_means[int(number_bs*high_quantile)]

bs_result = bootstrap(data)
mean = np.mean(data)
std_error = np.std(data)/np.sqrt(len(data))

print 'one sigma(bootstrap), one sigma(SEM), difference between the two'
print mean - bs_result[0], 2*std_error, (mean - bs_result[0] ) - 2* std_error

