# 
# CS 224 Spring 2019 
# Programming Assignment 1 
# 
# This program performs simple analysis of a data element across a 
# large number of data files representing runs of a traveling salesman 
# algorithm. 
# 
# Author: Zachary Baklund 
# Date: February 18, 2019 
#

from os import listdir
import re

path = './datafiles'
files = listdir(path)
all_min_dist = []
print "\n...Collecting All Minimum Distances\n"
for f in files:
    lookup = f + '.runbest'
    if lookup[0] == 'r':
        fn = open(path + '/' + f + '/' + lookup, 'r')
        lines = fn.readlines()
        fn.close()
        for line in lines:
            m = re.search(r"F\s(\d*.\d*)", line)
            print("{:<7s} > {:<15s} F {:<9s}".format(f, lookup, m.group(1)))
            all_min_dist.append(float(m.group(1)))
print "\n...Compiling Statistics\n"
max_val = max(all_min_dist)
min_val = min(all_min_dist)
avg_val = sum(all_min_dist)/len(all_min_dist)

print 'Run Count: ' + str(len(all_min_dist))
print 'Max Value: ' + str(max_val)
print 'Min Value: ' + str(min_val)
print 'Avg Value: ' + str(avg_val)