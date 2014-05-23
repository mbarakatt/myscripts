#!/usr/bin/env python
#This class load a bed file parses it and then can tell you if a position is in one of the regions defined in the bed file.
import numpy
from bisect import bisect_right
import sys
import subprocess
import os

class bedfile:
	#this constructor takes a path to a bed file. The bed file will be smoothed
	def __init__(self,filepath,chrstarts={},chrends={},verbose=True,skipCreateDict=True):
		self.isInitialized= not skipCreateDict
		self.path=filepath
		self.verbose=True
		if not skipCreateDict:
			self.Initialize(self.path,verbose)
			
	def Initialize(self,filepath,verbose):
		if verbose:
			print "Creating Dictionnary for", filepath
		bedf=open(filepath,'r')
		self.chrstarts={}
		self.chrends={}
		for line in bedf:
			if line[0]=="#":
				continue
			lsp=line.split()
			chr=lsp[0].split("chr")[-1]
			start=int(lsp[1])
			end=int(lsp[2])
			#self.chrstarts["test"]=[3]
			#print self.chrstarts["test"]
			try:
				self.chrstarts[chr].append(start)
				self.chrends[chr].append(end)
			except KeyError:
				self.chrstarts[chr]=[start]
				self.chrends[chr]=[end]

		dictargsort={}
		for chr, lst in self.chrstarts.iteritems():
			dictargsort[chr]=numpy.argsort(lst)
			self.chrstarts[chr] = [ lst[i] for i in dictargsort[chr] ]
			self.chrends[chr] = [ self.chrends[chr][i] for i in dictargsort[chr] ]
		
		for chr, lst in self.chrstarts.iteritems():
			tempstarts=[]
			tempends=[]
			tempstarts.append(lst[0])
			tempends.append(self.chrends[chr][0])
			for i  in range(len(lst))[1:]:
				if tempends[-1] <= self.chrstarts[chr][i]: # Deals with the case were there is no intersection at all
					tempstarts.append(lst[i])
					tempends.append(self.chrends[chr][i])
				else:
					if self.chrends[chr][i] > tempends[-1]:#if the new CDS is not completely contained in the already present one
						tempends[-1]=self.chrends[chr][i]
			self.chrstarts[chr]=tempstarts
			self.chrends[chr]=tempends
		bedf.close()
		if verbose:
			print "Dictionnary Created"
	
	#WARNING: must use vcf position unless specified otherwise
	def isinregion(self,chr,pos,isvcf=True):
		if not self.isInitialized:
			self.Initialize(self.path, self.verbose)
			self.isInitialized=True
		if isvcf==True:
			pos=pos - 1 #adjusted bed position for vcf
		p=bisect_right(self.chrstarts[chr],pos)
		if p==0:
			return False
		elif self.chrends[chr][p-1]>pos:
			return True
		else:
			return False

	def bpinbed(self,autosomalonly=True):
		if not self.isInitialized:
			self.Initialize(self.path, self.verbose)
			self.isInitialized=True
		total=0
		for chr in self.chrstarts:
			if autosomalonly and (chr.split("chr")[-1] not in map(str,range(1,22+1)) ) :
				continue
			for i in range(len(self.chrstarts[chr])):
				total += self.chrends[chr][i] - self.chrstarts[chr][i]

		return total
	
	def intersection(self,other,tempdirectory,filename):
		subprocess.call(['mkdir' ,'-p', tempdirectory])
		subprocess.call('bedtools '+ 'intersect '+ ' -a '+ self.path + ' -b ' + other.path + ' > '  +  os.path.join(tempdirectory ,filename),shell=True)
		return bedfile(os.path.join(tempdirectory ,filename))












