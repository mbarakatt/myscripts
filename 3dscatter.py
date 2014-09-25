from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random
import sys

fig = pylab.figure()
ax = Axes3D(fig)

OFFfile=sys.stdin.read().split('\n')
nblines=int(OFFfile[1].split()[0])
print "Nblines", nblines

data=OFFfile[2:nblines+2]


points=zip(*map(lambda x : map(float,x.split()) , data))

ax.scatter(*points)
pyplot.show()
