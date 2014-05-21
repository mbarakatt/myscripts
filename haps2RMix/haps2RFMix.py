#!/usr/bin/env python
import sys
arg=sys.argv
import os


#usage python haps2RFMix.py Admixed_pop.haps refpop1.haps refpop2.haps ... out_folder out_name
#outputs the allele.txt and classes.txt file in folders in the directory 



def complement(char):
	if char == 'A':
		return 'T'
	elif char == 'T':
		return 'A'
	elif char == 'G':
		return 'C'
	else :
		return 'G'

#identify .haps files in the arguements
hapfiles=[]
for input in arg:
	if ".haps" ==  input[-5:]:
		hapfiles.append(input)

#open the haps file
fhaps=[]
for f in hapfiles:
	fhaps.append(open(f,'r'))

if "haps"not in arg[-1]:
	out_folder=arg[-2]
else:
	out_folder=""

os.system("mkdir -p " + out_folder)
os.system("mkdir -p " + os.path.join(out_folder,"alleles" ))
os.system("mkdir -p " + os.path.join(out_folder,"classes"))
os.system("mkdir -p " + os.path.join(out_folder,"markerlocations"))


if "haps"not in arg[-1]:
	out_name=arg[-1]
else:
	out_name="" 

if "chr" in hapfiles[0]:
	chr=(hapfiles[0].split("chr")[-1]).split(".")[0]
else:
	chr=(hapfiles[0].split("Chr")[-1]).split(".")[0]

#creating the pointer for output files
OUTPUTALLELES= os.path.join(out_folder,"alleles" ) + "/alleles." + out_name + ".chr" + chr + ".txt"
falleles=open(OUTPUTALLELES,'w')
OUTPUTCLASSES=os.path.join(out_folder,"classes" ) + "/classes." + out_name + ".chr" + chr + ".txt"
fclasses=open(OUTPUTCLASSES,'w')

#flip=0
#total=0
count=0
cont=True
while cont:
	alllines=[]
	for file in fhaps:
		alllines.append(file.readline().split())
	if len(alllines[0]) < 2 :
		break
	geno1=alllines[0][3:5]
	geno2=alllines[1][3:5]
	#total+=1
	#check if flipped
	if (geno1[0] == geno2[1] and geno1[1] == geno2[0] ):# or (geno1[0] == complement(geno2[1]) and  geno1[1] == complement(geno2[0]) ):
		#flip+=1
		#print flip, total
		alllines[0]= alllines[0][:5] + [str((int(b) + 1) % 2) for b in alllines[0][5:]]
	outputline=[]
	for line in alllines:
		outputline= outputline + line[5:]

	falleles.write("".join(outputline)+ "\n") 
	#print "".join(outputline) + "\n"


#open the haps file again
fhaps=[]
for f in hapfiles:
        fhaps.append(open(f,'r'))

popcounter=0
clas=[]
for eachfile in fhaps:
	clas= clas + [str(popcounter)]*(len(eachfile.readline().split()) - 5 )
	popcounter = popcounter + 1

fclasses.write(" ".join(clas))



