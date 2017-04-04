from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

continent_color = np.array([177,177,177]) / 255.


# setup Lambert Conformal basemap.
# m = Basemap(width=12000000,height=9000000,projection='lcc', resolution='l',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# m = Basemap(projection='cea',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='l')
# m = Basemap(projection='merc',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='l')
m = Basemap(projection='cyl',llcrnrlat=25,urcrnrlat=39,llcrnrlon=-95,urcrnrlon=-74,resolution='i')

# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(color='white', fill_color='white', linewidth=0)
m.drawcountries(linewidth=0.3,color='white')
m.drawstates(linewidth=0.2, color='white')
# fill continents, set lake color same as ocean color.
m.fillcontinents(color=continent_color, lake_color='white')
plt.subplots_adjust(left=0., right=1., top=1., bottom=0.)
plt.savefig('test.pdf',bbox_inches='tight')
