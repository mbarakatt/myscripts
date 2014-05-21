import sys
usage ="""
python physical_to_genetic.py physical_position_file map_file

DATA MUST BE SORTED

Output is in stdout
"""

fake_incr=0.000001

args=sys.argv

f_physical_pos = open(args[1],'r')
f_map_file = open(args[2],'r')

map_phys=[]
map_gen=[]

"""
line = f_physical_pos.readline()
while line[0:3] != "chr":
	line=f_map_file.readline()
	#print line
	"""
f_map_file.readline()#remove the header line

for line in f_map_file:
	linesp=line.split()
	map_phys.append(int(linesp[0]))#this is the column where to find the integer in the genetic map file
	if linesp[2] != "NA":#will sometimes be "NA" in this case we put -1
		map_gen.append(float(linesp[2]))
	else:
		map_gen.append(float(-1))

start_incr=0
cur_position=0
previous_pos=-1
for line in f_physical_pos:
	if int(line) < map_phys[0]:
		if previous_pos == -1:
			previous_pos=float(line)
		start_incr += (float(line)-previous_pos)/1000000.0
		print start_incr
		previous_pos=float(line)
	elif int(line) > map_phys[-1]:
		print latest_gen_pos_mapped + (int(line) - map_phys[-1])/1000000.0
	else:
		while int(line) > map_phys[cur_position]:
			cur_position+=1

                latest_gen_pos_mapped=map_gen[cur_position-1] + (map_gen[cur_position] - map_gen[cur_position -1])*(float((int(line)-map_phys[cur_position-1]))/(map_phys[cur_position]-map_phys[cur_position-1])) + start_incr
		
		print latest_gen_pos_mapped #cur_position -= 1 #just to make sure we don't have 2 snp really close to eachother

