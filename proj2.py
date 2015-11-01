import os
import numpy as np
import matplotlib as plt
import re
import sys

exec(open('patFunctions.py').read())	# Opens a file that contains created functions pertaining to this script

count = 0
while True:
	file = input('Enter filename:\n')+'.txt'
	# file = 'plrx.txt'
	count += 1
	if os.path.isfile(file) == True:
		del count
		break
	if count == 3:
		print("The filenames you have entered do not exist. Find the correct filename and try again later.")
		sys.exit()

percent = float(round(float(input('Enter the percent of the data which you would like to be set as training data:\n')))/100)

f = open(file,'r')

data,C1,C2 = [],[],[]
classError, sampleSize, N1, N2 = 0,0,0,0

# Goal is to solve for N1,N2,PC1,PC2,Sigma1,Sigma2

all_data = []

for line in f.readlines():
	raw = re.findall(r"[^\s\\]+",line)
	for i in range(0,len(raw)):
		raw[i] = float(raw[i])
	all_data.append(raw)

data_len = len(all_data)

training_data = []
test_data = []

train_num = round(len(all_data)*percent)
test_num = len(all_data)-train_num

for i in range(train_num): 
	sampleSize +=1
	data_len -= 1
	k = all_data.pop(round(np.random.uniform(low=0,high=data_len)))
	if k[-1] == 1.0:
		N1 += 1
		C1.append(k[:-1])
	if k[-1] == 2.0:
		N2 += 1
		C2.append(k[:-1])
	else:
		classError += 1

training_data.append(C1+C2)

if len(all_data) != test_num:
	print('Your data is whack. Check 1')
	print(len(all_data),test_num)


if len(all_data) != data_len:
	print('Your data is whack. Check 2')
	print(len(all_data),data_len)

if sampleSize != N1+N2:
	print('Your data is whack.')
	print(sampleSize,N1,N2)


PC1 = N1/sampleSize
PC2 = N2/sampleSize

# print(PC1,PC2)

C1 = np.array(C1).T
C2 = np.array(C2).T

print('This is C1\n',C1.shape,C1)
print('This is C2\n',C2.shape,C2)

mu1 = average(C1,N1)
mu2 = average(C2,N2)

A = np.empty([12,12])

for x in C1:
	p = x-mu1
	pT = p.T
	p = np.multiply(p,pT)
	A = p + A
A = A*(1/N1)
print(A)


# print(mu1,len(mu2),'\n')
# print(mu2,len(mu2),'\n')

sigma1 = np.std(C1,axis=1)
sigma2 = np.std(C2,axis=1)

Sigma = ((PC1*sigma1) + (PC2*sigma2))*np.identity(12)

# print(Sigma)
# print(Sigma.shape)

print(sigma1)
# print(sigma2)
# print(Sigma)