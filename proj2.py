import os
import numpy as np
import matplotlib as plt
import re
import sys

exec(open('patFunctions.py').read())	# Opens a file that contains created functions pertaining to this script

count = 0

while True:
	file = input('Enter filename:\n')+'.txt'
	count += 1
	if os.path.isfile(file) == True:
		del count
		break
	if count == 3:
		print("The filenames you have entered do not exist. Find the correct filename and try again later.")
		sys.exit()

percent = input('Enter the percent of the data which you would like to be set as training data:\n')

f = open(file,'r')

data = []
N1 = 0
N2 = 0
classError = 0
C1 = []
C2 = []
sampleSize = 0

# Goal is to solve for N1,N2,PC1,PC2,

for line in f.readlines():
	sampleSize +=1
	print(line)
	raw = re.findall(r"[^\s\\]+",line)
	for i in range(0,len(raw)):
		raw[i] = float(raw[i])
		print(raw[i])
	if float(raw[-1]) == 1.0:
		N1 += 1
		C1.append(raw[:-1])
		print('In loop 1')
	if float(raw[-1]) == 2.0:
		N2 += 1
		C2.append(raw[:-1])
		print('In loop 2')
	else:
		classError += 1

if sampleSize != N1+N2:
	print('Your data is whack')

PC1 = N1/sampleSize
PC2 = N2/sampleSize

print(PC1,PC2)

C1 = np.array(C1).T
C2 = np.array(C2).T

mu1 = average(C1,N1)
mu2 = average(C2,N2)

print(mu1,len(mu2),'\n')
print(mu2,len(mu2),'\n')