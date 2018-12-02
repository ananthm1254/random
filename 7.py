import numpy as np
import matplotlib.pyplot as plt
	
f = np.linspace(-5,5,100)
H_f = (np.sin(np.pi*f)/(np.pi*f))**2
plt.plot(f,H_f)
plt.grid()
plt.show()
