from subprocess import call
import os
import argparse
import shutil

# Parsing arguments
# =================

def to_str_or_quotes(o):
          """Converts a value to string or add quotes"""
          if isinstance(o, basestring):
               return '"' + o + '"'
          else:
               return str(o)

parser = argparse.ArgumentParser(
	description='Change the number of individual in the population and recompile the main directory of the application as well as the utility subdirectory'
)
parser.add_argument(
	'pop_size',
	metavar='the size of the population to compile the program for',
	type=int
)
parser.add_argument(
	'path_pedhunter',
	metavar='The path to the pedhunter main folder',
	type=str
)


dic = vars(parser.parse_args())
pop_size = dic['pop_size']
path_pedhunter = dic['path_pedhunter']



# This is the string to search for that is unique for the line were there is the population size defined.
POPSIZE_LINE = "#define POPULATION "
f_outtemp = open(os.path.join(path_pedhunter, 'temp'), 'w')

# Quick and dirty way to change a line
for line in open(os.path.join(path_pedhunter, 'search.h'), 'r'):
	if POPSIZE_LINE in line:
		f_outtemp.write("%s%d\n" % (POPSIZE_LINE, pop_size))
		print "ADSF"
	else:
		f_outtemp.write(line)

f_outtemp.close()

# Create a backup of the search.h file in search.h.bak
shutil.copyfile(os.path.join(path_pedhunter, 'search.h'), os.path.join(path_pedhunter, 'search.h.bak'))

# Overwrite the search.h file
shutil.copyfile(os.path.join(path_pedhunter, 'temp'), os.path.join(path_pedhunter, 'search.h'))

# Move to the pedhunter directory
os.chdir(path_pedhunter)

call(['make'])

# Move into utility subfolder
os.chdir('./utility')

call(['make'])

