import numpy as np
import helperplot
from scipy.stats import binom
from scipy import spatial


NUMBER_TESTS = 10000
def test():
	return np.random.randint(0, 2, NUMBER_TESTS)


res = [ np.sum(test())  for i in range(10000) ]

cdf = [binom.cdf(r, NUMBER_TESTS, 0.5) for r in res ]
# print cdf
p_values = [ 2 * np.min([1 - c, c]) for c in cdf ]
# print p_values


#helperplot.histogram(res)
helperplot.qqplot(p_values)



