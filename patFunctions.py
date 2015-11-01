

def average(data,num):

	empty = []
	for i in data:
		avg = sum(i)/num
		empty.append([avg])
	return(np.array(empty))

def execute(lists,fname):
	
	access_mode = "w"

	with open(fname, access_mode) as out:
		for i in range(0,len(lists[0])):
			out.write(str(lists[0][i])+"\t"+str(lists[1][i])+"\n")

def npMatrix(data):
	
	lst = []

	for i in range(0,N):
		lst.append(([data[0][i],data[1][i]]))

	return(np.matrix(lst))

ast = sorted

def npArray(data):
	
	lst = []

	for i in range(0,N):
		lst.append(([data[0][i],data[1][i]]))

	return(np.array(lst))

def normList(mu,sigmaSquared,length):
	
	empty = []

	for l in mu:
		X = random(l,sigmaSquared,length)
		empty.append(list(X))

	return(empty)

def diff(mtrx,mu):

	lst = []

	for i in mtrx:
		dif = i-np.matrix(mu)
		lst.append(dif)

	return(lst)

def functionLoop(varableMu,variableSigma,accuracyList):
		
	N = 500

	mean1 = [-3+variableMu,4+variableMu]
	mean2 = [3+variableMu,-2+variableMu]

	mu1 = [[mean1[0]],[mean1[1]]]						# This is the mean for the first class of random values
	mu2 = [[mean2[0]],[mean2[1]]]						# This is the mean for the second class of random values

	stDev1 = 1+variableSigma								# This sets the variance to 1 for the first class of random values
	stDev2 = 2+variableSigma								# This sets the variance to 2 for the second class of random values

	Class1List = normList(mu1,stDev1,N)							# Generates a list from a function using a mu, variance, and N number or samples
	Class2List = normList(mu2,stDev2,N)		

	muClass1 = np.matrix(average(Class1List,N))					# Finds the new mu for the lists and places them into a list.
	muClass2 = np.matrix(average(Class2List,N))

	Class1Matrix = np.matrix(Class1List)						# Casts the list into a Numpy matrix for calculations while still allowing
	Class2Matrix = np.matrix(Class2List)						# to keep the list for easily sending to a .txt file for later

	dif1 = Class1Matrix-muClass1								# Subracts the means from the matrices for ease of getting the scatter matrices
	dif2 = Class2Matrix-muClass2

	S1 = dif1*np.matrix.transpose(dif1)*(1/N)					# Computes the scatter matrix for each class
	S2 = dif2*np.matrix.transpose(dif2)*(1/N)
	Sw = (S1+S2)												# Adds both scatter matrices to get the within class scatter matrix

	mnDif = np.array(muClass1-muClass2)							# Subtracts the means of both classes for ease of getting the between class scatter matrix
	Sb = mnDif*np.matrix.transpose(mnDif)						# Calculates the between scatter matrix

	scatter = (S1*S1)+(S2*S2)

	JofW = (np.array(mnDif.T*np.linalg.inv(scatter)))
	print(JofW)

	Jw = np.linalg.inv(Sw)*Sb 									# Calculates the matrix (Sw^-1*Sb)
	print(Jw)


	eigenDecomp = np.linalg.eig(Jw)								# Performs the eigen value decomposition

	eigenVal = max(np.array(eigenDecomp[0]))					# Gets the eigen value from the calculation

	eigenVectors = np.array(eigenDecomp[1])						# Gets the eigen vectors from the valculation

	eigenMatrix = np.matrix(eigenVectors)

	eigenVec1 = eigenVectors[0][0]								# Extracts the solution for w by extracting from the eigen Vectors
	eigenVec2 = eigenVectors[1][0]

	eigenVector = np.matrix([[eigenVec1],[eigenVec2]])			# Extracts the eigen vector from the decomposition
																# and creates an Numpy matrix

	multC1 = eigenVector.T*Class1Matrix							# Multiplies the w matrix with the classes to check for correctness
	multC2 = eigenVector.T*Class2Matrix

	JwFunct = np.array(eigenMatrix.T*Sb*eigenMatrix)*np.linalg.inv(eigenMatrix.T*Sw*eigenMatrix)

	someVal = eigenVal/(stDev1**2+stDev2**2)

	print(eigenVal)
	print(eigenVec1)
	print(eigenVec2)
	print(someVal)

	multC1 = np.array(multC1)
	multC2 = np.array(multC2)

	accuracyClass1 = 0
	accuracyClass2 = 0

	for i in multC1[0]:
		if i < 0:
			accuracyClass1 += 1

	for i in multC2[0]:
		if i < 0:
			accuracyClass2 += 1	

	accuracyClass1 = (accuracyClass1/len(multC1[0]))			# Calculates the accuracy of each class
	accuracyClass2 = (accuracyClass2/len(multC2[0]))

	if accuracyClass1 < 0.5:
		accuracyClass1 = 1-accuracyClass1

	if accuracyClass2 < 0.5:
		accuracyClass2 = 1-accuracyClass2

	accuracyClass1 = accuracyClass1*100
	accuracyClass2 = accuracyClass2*100

	totalAccuracy = (accuracyClass1+accuracyClass2)/2			# Calculates the average of the accuracy

	accuracyList.append(totalAccuracy)

	# print('This is the accuracy for Class 1 : '+str(accuracyClass1)+'%\n')
	# print('This is the accuracy for Class 2 : '+str(accuracyClass2)+'%\n')
	# print('The average accuracy is : '+str(totalAccuracy)+'%\n')

	# R = max([variableMu,variableSigma])

	# fname1 = 'Xdata'+str(int(R*100))+'.txt'
	# fname2 = 'Ydata'+str(R*100)+'.txt'

	x = range(-20,20,1)
	y = ((-(JofW[0][0]/JofW[0][1]))*x)+someVal

	graph(y,x,Class1List,Class2List)
	
	return(0)

def fileIO(flocation):
	if os.path.isdir(path+flocation):
		os.chdir(path+flocation)
	else:
		os.mkdir(path+flocation)	


def graph(formula, x_range,Class1List,Class2List):
	x = np.array(x_range)
	y = formula

	fig = plt.figure(figsize=(10,10), facecolor = 'k')
	ax = plt.subplot(frameon = True)
	v = [-15,15,-15,15]
	plt.plot(x,y) 
	ax.axis(v)
	ax.set_aspect('equal')
	ax.grid(True, which='both')

	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')

	line1 = ax.plot(Class1List[0], Class1List[1], color = "g", marker = ".") 
	line2 = ax.plot(Class2List[0], Class2List[1], color = "r",  marker = ".")

	plt.show()


# accuracyClass1 = (np.array(multC1)).count(Negativenum)

# print(accuracyClass1)

################
################

# The values for W are the first two elements of the matrices that # printed. Something like 0.92 and 0.39

###############
###############
