#!/usr/bin/env python
import math
import sys
from Tkinter import *
import copy
import gzip

CHR_HEIGHT=4 #the height of the rectangle for the colored chromosome
CHR_WIDTH=187 #the width of the rectangle for the colored chromosome
DISTANCE_BETWEEN_CHR=0 #the distance between chromosome in the same box!
DISTANCE_FROM_LEFT=5 # distance of the colored rectangle for each chromosome form the left in its box.
DISTANCE_FROM_TOP=3
DIMENSION_BOXES=[190,CHR_HEIGHT*2 + DISTANCE_BETWEEN_CHR + 4]
CONTENT_POSITION=[10,50]

OFFSET_BOXE=1
CHR_NB_PER_BOX=2 #individual are diploid

color=["no_ancestry","red","blue","orange","gray"]
#LOADING FILES
args=sys.argv

if args[1][-3:]=='.gz':
	f_viterbi=gzip.open(args[1],'r')
else:
	f_viterbi=open(args[1],'r')


#f_indiv=open(args[2],'r')
f_marker_location=open(args[2],'r')
viterbi_data=[]
for line in f_viterbi:
	viterbi_data.append(line.replace(" ", "").replace('\n',""))

#indiv_data=f_indiv.readlines()
marker_location_data=f_marker_location.readlines()
#---------------------
figure_title=args[3]

marker_location_data= [float(item)- float(marker_location_data[0]) for item in marker_location_data]

length_chr = float(marker_location_data[-1])#the position (must be in physical distance) of the last SNPs is interpreted as the length of the chromosome.
number_individual=min(2500,len(viterbi_data[0]))
NUMBER_BOXES=[13,math.ceil(float(number_individual)/13.0)]
#math.ceil(math.sqrt(float(number_individual)))

CANVAS_SIZE=[NUMBER_BOXES[0]*DIMENSION_BOXES[0]+CONTENT_POSITION[0],math.ceil((NUMBER_BOXES[1]+1)*DIMENSION_BOXES[1])/2+CONTENT_POSITION[1]]
master = Tk()
w = Canvas(master, width=CANVAS_SIZE[0], height=CANVAS_SIZE[1],background="black")
w.pack()

w.create_text(CANVAS_SIZE[0]/2,0,text=figure_title,anchor="n",font=("Helvectica", "25"))

def my_draw_rectangle(global_position, left, right,ancestry):
	w.create_rectangle(global_position[0]+DISTANCE_FROM_LEFT +left,global_position[1]+ DISTANCE_FROM_TOP, global_position[0]+DISTANCE_FROM_LEFT+right,global_position[1] +DISTANCE_FROM_TOP + CHR_HEIGHT,fill=color[ancestry],width=0)

def draw_box(position,individual,chr_number):
	if chr_number==0:
		#w.create_rectangle(position[0]+OFFSET_BOXE,position[1]+OFFSET_BOXE,position[0]+DIMENSION_BOXES[0]-OFFSET_BOXE,position[1]+DIMENSION_BOXES[1]-OFFSET_BOXE,fill="")
		w.create_text(position[0] + (DIMENSION_BOXES[0]/2),position[1]+ DISTANCE_BETWEEN_CHR,anchor="n")#,text=indiv_data[individual][:-2])
	position[1]+=chr_number*(CHR_HEIGHT+DISTANCE_BETWEEN_CHR)

	cur_marker=0
	while cur_marker < len(marker_location_data):
		ancestry=int(viterbi_data[cur_marker][individual])
		left_marker=cur_marker
		cur_marker+=1 ####CASE THAT IT DOES NOT ENTER ONCE
		while ancestry == int(viterbi_data[cur_marker][individual]):
			cur_marker +=1
			if cur_marker >= len(marker_location_data):
				break;
		
		my_draw_rectangle(position,(float(marker_location_data[left_marker])/length_chr)*CHR_WIDTH,(float(marker_location_data[cur_marker-1])/length_chr)*CHR_WIDTH ,ancestry)

#print range(len(viterbi_data[0].replace(" ","")) )
box_position = copy.deepcopy(CONTENT_POSITION)
chr_number=0
for individual in range(number_individual):
	print individual
	draw_box(copy.deepcopy(box_position),individual,chr_number)
	if individual % CHR_NB_PER_BOX == 1:
		chr_number=0
		if ((individual +1)/CHR_NB_PER_BOX) % NUMBER_BOXES[0] == 0 and individual > CHR_NB_PER_BOX:
			box_position = [CONTENT_POSITION[0],box_position[1]+DIMENSION_BOXES[1]]
		else:
			box_position[0]+=DIMENSION_BOXES[0]
	else:
		chr_number+=1


#w.create_rectangle(0, 25, 150, 75, fill="blue",width=0)
w.update()
w.postscript(file= figure_title + ".ps", colormode='color')
mainloop()
