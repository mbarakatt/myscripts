#!/usr/bin/env python2
from bisect import bisect_right
import numpy as np
import sys
import os

list_indiv = []
list_indiv_diploid = []
for ind in open(sys.argv[1], 'r'):
    ind = ind[:-1]
    list_indiv.append(ind + "_A")
    list_indiv.append(ind + "_B")
    list_indiv_diploid.append(ind)


print("Loading bed files (%d to load) " % len(list_indiv))

class outbed:
    def __init__(self, ind):
        self.ind = ind
        self.outbed = open(os.path.join('outbed','T' + ind + '_cM.bed'), 'r')
        self.startbp = {}
        self.endbp = {}
        self.startcm = {}
        self.endcm = {}
        self.ancestry = {}
        self.order_chr = []
        for line in self.outbed:
            sp = line.split()
            if sp[0] not in self.order_chr:
                self.order_chr.append(sp[0])
            self.addtodict(self.startbp, sp[0], int(sp[1]))
            self.addtodict(self.endbp, sp[0], int(sp[2]))
            self.addtodict(self.ancestry, sp[0], sp[3])
            self.addtodict(self.startcm, sp[0], float(sp[4]))
            self.addtodict(self.endcm, sp[0], float(sp[5]))

        # Converting regular arrays to numpy arrays
        for d in [self.startbp, self.endbp, self.ancestry, self.startcm, self.endcm]:
            d = {k: np.array(v) for k, v in d.iteritems()}

        self.outbed.close()

    def addtodict(self, d, k, v):
        try:
            d[k].append(v)
        except:
            d[k] = [v]
        return d

    def get_ancestry(self, chro, pos):
        # print  bisect_right(self.startbp[chro], pos) - 1, self.startbp[chro], pos
        # print  self.ancestry[chro][bisect_right(self.startbp[chro], pos) - 1 ]
        return self.ancestry[chro][bisect_right(self.startbp[chro], pos) - 1]



# Parsing bed files in objects
outbeds = []
for i, ind in enumerate(list_indiv):
    outbeds.append(outbed(ind))
    # continue
    # if i > 300:
    #     break  # breaking for testing purposes

def list_to_list2tuple(l):
    """generator to convert a list into a list of 2-tuples"""
    for i in range(0,len(l),2):
        yield (l[i], l[i+1])

def AFR_proportion(tuple_bed, chro, pos):
    """Given a tuple of outbed object and a genomic position this method returns 0, 0.5 or 1 depending on the AFR ancestry"""
    # print tuple_bed[0].ancestry[chro], tuple_bed[1].ancestry[chro]
    return ((tuple_bed[0].get_ancestry(chro, pos) == 'AFR') + (tuple_bed[1].get_ancestry(chro, pos) =='AFR') ) / 2.


print("Computing global ancestry switch")
switch_positions = {}
for chro in outbeds[0].order_chr:
    print("Chr%s" % chro)
    switch_positions[chro] = np.unique((np.concatenate([i.startbp[chro] for i in outbeds])))

f_out = open('globed.txt', 'w')
f_out.write('chr' + 'pos' + ','.join(list_indiv_diploid) + '\n')
for chro in outbeds[0].order_chr:
    for pos in switch_positions[chro]:
        f_out.write(chro + pos + ','.join(map(str,[ AFR_proportion(o, chro, pos) for o in list_to_list2tuple(outbeds)])) + '\n')



exit(1)

# print outbeds[50].ind
# print [outbeds[50].startbp[str(i)] for i in range(1,23)]
print switch_positions['1']
