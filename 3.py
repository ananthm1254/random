import numpy as np
import math
def poisson(r,n,t):
	P_N = (np.exp(-r*t))*(((r*t)**n)/np.math.factorial(n))
	return P_N
def expn(r,t):
	return np.exp(-r*t)

R = 2
T = 5
t = 1
sum = poisson(R,0,T)
for i in range(0,5):
	sum = sum + poisson(R,i+1,T)*(expn(R,t)**i)
	
print sum
print (poisson(R,5,T))*(expn(R,t))**4
