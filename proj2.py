import os
import numpy as np
#import matplotlib as plt
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
	#print(line)
	raw = re.findall(r"[^\s\\]+",line)
	for i in range(0,len(raw)):
		raw[i] = float(raw[i])
		#print(raw[i])
	if float(raw[-1]) == 1.0:
		N1 += 1
		C1.append(raw[:-1])
		#print('In loop 1')
	if float(raw[-1]) == 2.0:
		N2 += 1
		C2.append(raw[:-1])
		#print('In loop 2')
	else:
		classError += 1

if sampleSize != N1+N2:
	print('Your data is whack')

PC1 = N1/sampleSize
PC2 = N2/sampleSize

#print(PC1,PC2)

C1 = np.array(C1).T
print("This is class 1")
print (C1)
C2 = np.array(C2).T
#print ("This is class 2 ")
#print(C2)

print(" ")
mu1 = average(C1,N1)
mu2 = average(C2,N2)

#print(mu1,len(mu2),'\n')
#print(mu2,len(mu2),'\n')


#some minor edits:
#book says:
#S1 = (1/(N1))*sum(Xn - mu1)(Xn - mu1).T
# let thing1 = (Xn - mu1)

#where Xn is an element in class1 from n = 0 to range of C1

print("This is C1[0 , 0]")
print(C1[0,0])

print("This is c1[0, 129]")
print(C1[0, 129])

print("This is C1 at position 0")
print (C1 [0][:])

print("This is C1 at position 1")
print(C1[1][:])

cuanto0 = 0

for item in C1[0]:
	cuanto0 = cuanto0 + 1 

print ("Cuanto in C1[0] is: ")
print (cuanto0)

cuanto1 = 0
for item in C1[1]:
	cuanto1 = cuanto1 + 1 

print ("Cuanto in C1[1] is: ")
print (cuanto1)


cuanto2 = 0
for item in C1[2]:
	cuanto2 = cuanto2 + 1 

print ("Cuanto in C1[2] is: ")
print (cuanto2)

cuanto3 = 0
for item in C1[3]:
	cuanto3 = cuanto3 + 1 

print ("Cuanto in C1[3] is: ")
print (cuanto3)

print("This mess is huge: ")
print(C1.shape)

newList = []
thing11 = []
thing1 = []


for item in range(0, 129):
	newList.append(C1[0][item])
	thing11.append(newList[item] - mu1)


print ("This is newList: ")
print(newList)

print("This is thing11: ")
#print(thing11)
	#sigh. fix this with psuedo code


# posible si usamos dos for loops....

for row in range(0,11):
	for column in range(0, 129):
		thing1.append((C1[row][column])-mu1[row])

thing1 = np.array(thing1)

print("this is shape of thing1 ")
print(thing1.shape)


