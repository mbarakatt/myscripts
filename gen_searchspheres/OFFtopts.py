import sys


OFFfile=sys.stdin.read().split('\n')
nblines=int(OFFfile[1].split()[0])

data=OFFfile[2:nblines+2]

sys.stdout.write("\n".join(data))
sys.stdout.write('\n')

