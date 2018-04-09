import numpy as np
import matplotlib.pyplot as plt
t = 54.83
lamda_i = 12.
N = 1000
E = 1.
lambda_BR = 4.
print lambda_BR

q = np.linspace(-1.,1.,N)
e_pp = lambda_BR + np.sqrt((54.83*abs(q))**2 + (lambda_BR - lamda_i)**2)
e_np = -lambda_BR + np.sqrt((54.83*abs(q))**2 + (lambda_BR + lamda_i)**2)
e_pn = lambda_BR - np.sqrt((54.83*abs(q))**2 + (lambda_BR - lamda_i)**2)
e_nn = -lambda_BR - np.sqrt((54.83*abs(q))**2 + (lambda_BR + lamda_i)**2)

plt.plot(q,e_pp)
plt.plot(q,e_np)
plt.plot(q,e_pn)
plt.plot(q,e_nn)
plt.show()