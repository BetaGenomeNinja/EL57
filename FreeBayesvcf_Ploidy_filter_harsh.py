#FreeBayesvcf_Ploidy_filter_harsh.py

import sys
import os
import time
import subprocess
import fileinput
dir = os.getcwd()

File1 = sys.argv[1]
for k in fileinput.input(File1):
	if '#' in k:
		print(k[0:-1])
	if '#' not in k:
		j=k.split('\t')
		DP=j[7].replace(';',' ').split(' ')
		DP1=DP[7].split('=')[1]
		DP2=DP[15].split('=')[1]
		DP22=DP2.split(',')[0]
		#print(DP2)
		#print(DP1)
		#print(k)
		if float(j[5]) >= float(30) and float(DP1) > float(25) and float(DP1) < float(300) and float(DP22) >= float(60):
			print(k[0:-1])
