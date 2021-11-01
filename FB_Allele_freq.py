from __future__ import division
import sys
import os
import time
import subprocess
import fileinput

dir = os.getcwd()

File1 = sys.argv[1]
for k in fileinput.input(File1):
	#if '#' in k:
		#print(k[0:-1])
	if '#' not in k:
		j=k.split('\t')
		#print(j[0],j[1],j[3],j[4],j[9],j[10][0:-1])
		J9=j[9].split(':')[0]
		J10=j[10].split(':')[0]
		J91=J9.split('/')
		J101=J10.split('/')
		J11=j[11].split(':')[0]
		J111=J11.split('/')
		alt=0
		ref=0
		#print(J91)
		for i in J91:
			#print(i)
			if i == '1':
				alt=alt+1
		if alt == 0:
			AF1 = 0
		if alt > 0:
			AF1=alt/25	
		alt1=0
		alt2=0
		for i in J111:
			#print(i)
			if i == '1':
				alt2=alt2+1
		if alt2 == 0:
			AF3 = 0
		if alt2 > 0:
			AF3=alt2/25
		alt1=0

		for i in J101:
			#print(i)
			if i == '1':
				alt1=alt1+1
		if alt1 == 0:
			AF2 = 0
		if alt1 > 0:
			AF2=alt1/25
		
		#print(alt)
		print(j[0],j[1],j[3],j[4],round(AF1,2),round(AF2,2),round(AF3,2))


