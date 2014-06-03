import sys
fin=sys.stdin
fout=sys.stdout

#usage python vcf2haps.py file.vcf 
#Input in stdin output stdout 

while 1==1:
	if fin.readline()[0:6]== "#CHROM":
		break

for line in fin:
	sp=line.split()
	fout.write(str(sp[0]) + " " + str(sp[2])+ " " + str(sp[1]) + " " + str(sp[3]) + " " + str(sp[4]) + " " + (" ".join(sp[9:]).replace("\t"," ").replace("|"," ")) + "\n")
	
	
