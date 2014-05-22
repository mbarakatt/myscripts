#!/usr/bin/env python
import sys
import os

args=sys.argv
folder=args[1]#eg HRS_EU
name=args[2]#eg HRS_EU
chr=args[3]#eg 3




REF_START=21603
REF_END=22078
NB_INDIV=(REF_START-1)/2
NB_PART=8
starts=[ (mult*NB_INDIV)/NB_PART*2+1 for mult in range(0,NB_PART)]
ends=[ (mult*NB_INDIV)/NB_PART*2 for mult in range(1,NB_PART+1)]


for i in range(NB_PART):
	field_part= str(starts[i]) + "-" + str(ends[i]) + "," + str(REF_START) +"-" + str(REF_END)+ " "
	print "Iteration", str(i), 'cut -d " " ' + field_part  + os.path.join(folder,"alleles","alleles."+name+ ".chr"+ str(chr) + ".txt" ) + " > " + os.path.join(folder,"alleles","alleles."+name+ ".chr" + str(chr) + "." + str(i)+".txt  " )
	os.system('cut -c' + field_part  + os.path.join(folder,"alleles","alleles."+name+ ".chr"+ str(chr) + ".txt" ) + " > " + os.path.join(folder,"alleles","alleles."+name+ ".chr" + str(chr) + "." + str(i)+".txt &" ))
	os.system('cut -d " " -f' + field_part  + os.path.join(folder,"classes","classes."+name+ ".chr"+ str(chr) + ".txt" ) + " > " + os.path.join(folder,"classes","classes."+name+ ".chr" + str(chr) + "." + str(i)+".txt" ))
