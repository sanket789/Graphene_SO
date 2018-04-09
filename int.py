import numpy as np
import matplotlib.pyplot as plt
t = 54.83
lamda_i = 12.
N = 1000.
q = np.linspace(-2,2,N)
q_mod = abs(q)
en_p = np.sqrt(t**2*q_mod**2+lamda_i**2)
en_n = -1*np.sqrt(t**2*q_mod**2+lamda_i**2) 
plt.plot(q,en_p)
plt.plot(q,en_n)
plt.show()
plt.title('Intrinsic splitting')

