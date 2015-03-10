#!/usr/bin/bash
#This script expects a single integer.

i=$1
echo "Argument given:"$i  ; 
geodesic -c 2 -f ${i} -M s ico | python OFFtopts.py > searchspheres/searchspace${i}.txt 


