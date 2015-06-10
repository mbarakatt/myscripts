#!/usr/bin/env python
import sys
fin=sys.stdin
fout=sys.stdout
args = sys.argv

#usage= python selectsnp.py file_with_snps

fsnp=open(args[1]) 

snps=[]

for line in fsnp:
	snps.append(int(line[0:-1]))

index=0
for line in fin:
	sp=line.split()
	if int(sp[2]) ==  snps[index]:
		fout.write(line)
		index = index + 1
		if index >= len(snps):
			break
