import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0,5000,10000)
n = 4999
F = (n-s) + (np.log(n*(s-1)+1)) - n*np.log(n)
print F
X = np.exp(F/100)
plt.plot(s,X)
plt.show()
