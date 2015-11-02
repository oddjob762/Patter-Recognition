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



tempArray = C1[0][:]
print("This is temp array: ")
print(tempArray)

print("This is mu1[0]:")
print(mu1[0])

#hold on
tempArray = tempArray - mu1[0]
print("This is tempArray after subtraction: ")
print(tempArray)


#matrixProduct = tempArray*tempArray.T
#print("This is the matix product  ")
#print(matrixProduct)
#^^this no good

#since we are actually taking the dot product with ourselves...
#let us use numpy.dot
#mucho mas facil creo

matrixProduct = np.dot(tempArray, tempArray)
print("This is matrix product: ")
print(matrixProduct)

#yaaaaa!!!


#ok now to build the loop for all of class1:

counter = 0
S1 = 0

while counter < 12:
	tempArray = C1[counter][:]
	tempArray = tempArray - mu1[counter]
	matrixProduct = np.dot(tempArray, tempArray)
	S1 = S1 + matrixProduct
	counter = counter + 1 

print("This is S1: ")	
print(S1)

#does happy dance for 5 seconds


#ok now to rebuild for all of C2

print("This is the size of class 2: ")
print(C2.shape)

#okay

print("This is the size of mu2: ")
print(mu2)

#looks like same code will work
#derpity derp. 

counter = 0
S2 = 0

while counter < 12:
	tempArray = C2[counter][:]
	tempArray = tempArray - mu2[counter]
	matrixProduct = np.dot(tempArray, tempArray)
	S2 = S2 + matrixProduct
	counter = counter + 1 

print("This is S2: ")	
print(S2)


#now to finish the hard coded bit...robinson suggests to divide by respective N1 and N2
#okey doke

S1 = S1/N1
S2 = S2/N2

print("This is S1: ")
print(S1)

print("This is S2: ")
print(S2)



# kewwwl, so this should match with the results from std in the numpy routines

#final bit is to build the giant S equation as mentioned in the book:

#S = N1/#pat * S1  + N2/#pat* S2

#kk

numPatterns = N1+N2

bigS = ((N1/numPatterns)*S1) + ((N2/numPatterns)*S2)

print("This is bigS: ")
print(bigS)


















#print(thing11) 
	#sigh. fix this with psuedo code


# posible si usamos dos for loops....
#don't do this, creates giant mess:
#for row in range(0,11):
	#for column in range(0, 129):
		#thing1.append((C1[row][column])-mu1[row])

#thing1 = np.array(thing1)

#print("this is shape of thing1 ")
#print(thing1.shape)


