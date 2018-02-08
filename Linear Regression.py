from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

x = np.array([], dtype=np.float64)      #Put your input value in the x array i.e inside []
y = np.array([], dtype=np.float64) 		#Put the labels inside y array i.e inside [] 
#Data can also be fetched from some file or can be randomize with the function in comment below named createDataset

##def createDataset(total, variance, step=2, correlation=False):
##	val = 1
##	y = []
##	for i in range(hm):
##		temp = val + random.randrange(-variance, variance)
##		y.append(temp)
##		if correlation and correlation == 'pos':
##			val+=step
##		elif correlation and correlation =='neg':
##			val-=step
##	x = [i for i in range(len(y))]
##	return np.array(x, dtype = np.float64), np.array(y, dtype = np.float64)

def bestFitLineAndIntercept(x, y):
	m = (((mean(x)*mean(y)) - mean(x*y))/ ((mean(x))**2 - mean(x**2)) )
	b = mean(y) - m*mean(x)
	return m, b

def squaredError(yOriginal, yLine):
	return sum((yLine - yOriginal)**2)

def coefficientOfDetermination(yOriginal, yLine):
	yMeanLine = [mean(yOriginal) for a in yOriginal]
	squaredErrorRegression = squaredError(yOriginal, yLine)
	squaredErrorYMean = squaredError(yOriginal, yMeanLine)
	return 1-(squaredErrorRegression/squaredErrorYMean)

#Please uncomment the below command when you need to create random data and the arguments are 1.total=number of data points, 2.variance=possible variety in the data points
#3.step=This detemines the increment/decrement in consecutive data 4.correlation=It is True/'pos' for increment in data and Flase/'neg' for decrement 

##x, y = createDataset(20, 20, 1, correlation='pos')

m,b = bestFitLineAndIntercept(x, y)

regressionLine = [(m*a)+b for a in x]

predictX = []                   #Data to be predicted goes here
for i in range(len(predictX)):
	predictY[i] = (m*predictX[i])+b  #predicted value

rSquared = coefficientOfDetermination(y, regressionLine)
print(rSquared)

plt.scatter(x, y)
plt.scatter(predictX, predictY) 	#Plots the predicted value
plt.plot(x, regressionLine)
plt.show()
