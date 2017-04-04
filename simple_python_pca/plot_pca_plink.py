import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# white backgroup with no grid
sns.set_style("white")

# Loading ancestry
# fglobal = open("../../results/PC_20150617/global_ancestry_prop.txt", 'r')
# ancestries = fglobal.readline()[:-1].split()[1:]
# indiv_ancestry_dict = dict()

# for line in fglobal:
# 	sp = line.split()
# 	ID = sp[0]
# 	indiv_ancestry_dict[ID] = map(float, sp[1:])


# loading individual positions in eigenspace
f = open('plink.eigenvec', 'r')


IDs = []
dims = []
colors = []
for line in f:
	sp = line.split()
	# if sp[1] in indiv_ancestry_dict.keys():
	IDs.append(sp[1])
	colors.append(sns.color_palette()[int(sp[1][0:3] == 'twa')])
	# colors.append(sns.color_palette()[0])
	dims.append(map(float, sp[2:3+1]))


# We plot the Bakigas first and then the Batwas to outline the Batwas with high
# proprotion of Bakiga ancestry

xs , ys = zip(*dims)
plt.scatter([x for (x,c) in zip(xs,colors) if c == sns.color_palette()[0]], [y  for (y,c) in zip(ys,colors) if c == sns.color_palette()[0]], c=sns.color_palette()[0], alpha=0.6, edgecolor='none',s=60)
plt.scatter([x for (x,c) in zip(xs,colors) if c == sns.color_palette()[1]], [y  for (y,c) in zip(ys,colors) if c == sns.color_palette()[1]], c=sns.color_palette()[1], alpha=0.6, edgecolor='none',s=60)
plt.tick_params(axis='both', which='major', labelsize=12)

# circles = [ mpatches.Circle((0.5, 0.5), 0.02, facecolor=sns.color_palette()[i], edgecolor='none') for i in range(3) ]
legend_items = [ Line2D(range(1), range(1), color="white", marker='o', markerfacecolor=sns.color_palette()[i], markeredgecolor='none') for i in range(2) ]
plt.legend(legend_items, ['Bakiga', 'Batwa'], fontsize=17, loc=2)

# tighter limits
plt.gca().set_ylim(np.min(ys) - 0.1*(np.max(ys)-np.min(ys)), np.max(ys) + 0.1*(np.max(ys)-np.min(ys)))
plt.gca().set_xlim(np.min(xs) - 0.1*(np.max(xs)-np.min(xs)), np.max(xs) + 0.1*(np.max(xs)-np.min(xs)))


eigenvalues = np.loadtxt('./plink.eigenval')

# plt.title('PCA')
plt.xlabel('PC1 (%.1f%%)' % (eigenvalues[0]/ np.sum(eigenvalues)*100 ), fontsize=17)
plt.ylabel('PC2 (%.1f%%)' % (eigenvalues[1]/ np.sum(eigenvalues)*100 ), fontsize=17)

plt.savefig('pca_fig.pdf')

