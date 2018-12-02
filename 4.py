import numpy as np
import matplotlib.pyplot as plt
X = np.matrix([[0],[0]])
x = []
y = []
for i in range(0,100000):
	theta = np.random.choice([1,2,3,4], p = [0.01,0.07,0.07,0.85])
	if theta==1:
		A = np.matrix([[0,0],[0,0.16]])
		b = np.matrix([[0],[0]])
	elif theta==2:
		A = np.matrix([[0.2,-0.26],[0.23,0.22]])
		b = np.matrix([[0],[1.6]])
	elif theta==3:
		A = np.matrix([[-0.15,0.28],[0.26,0.24]])
		b = np.matrix([[0],[0.44]])
	elif theta==4:
		A = np.matrix([[0.85,0.04],[-0.04,0.85]])
		b = np.matrix([[0],[1.6]])
	x.append(X[0][0])
	y.append(X[1][0])
	X = np.dot(A,X) + b
plt.scatter(x,y)
plt.show()
