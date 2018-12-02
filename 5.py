import numpy as np
import matplotlib.pyplot as plt

p = 0.3
M = 500
P = np.zeros((M,M))
P[0][0] = 1-p
P[0][1] = p
P[M-1][M-2] = 1-p
P[M-1][M-1] = p
for i in range(1,M-2):
	P[i][i-1] = 1-p
	P[i][i+1] = p
P_n00 = []
Q = P
for i in range(0,10000):
	P_n00.append(Q[0][0])
	Q = np.dot(Q,P)
	
print Q

x = np.linspace(0,10000,10000)
plt.plot(x,P_n00)
plt.grid()
plt.show()
