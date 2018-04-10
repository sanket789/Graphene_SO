import numpy as np
import matplotlib.pyplot as plt
t = 54.83
lamda_i = 12.
N = 1000
E = 4.0
lambda_BR = 5.0*E
print lambda_BR

q = np.linspace(-1.8,1.8,N)
e_pp = lambda_BR + np.sqrt((54.83*abs(q))**2 + (lambda_BR - lamda_i)**2)
e_np = -lambda_BR + np.sqrt((54.83*abs(q))**2 + (lambda_BR + lamda_i)**2)
e_pn = lambda_BR - np.sqrt((54.83*abs(q))**2 + (lambda_BR - lamda_i)**2)
e_nn = -lambda_BR - np.sqrt((54.83*abs(q))**2 + (lambda_BR + lamda_i)**2)


fig, ax = plt.subplots()
ax.plot(q, e_pp, 'r--', label='Positive spin branch')
ax.plot(q, e_pn, 'r--', label='Positive spin branch')
ax.plot(q, e_nn, 'b', label='Negative spin branch')
ax.plot(q, e_np, 'b', label='Negative spin branch')
plt.xlabel(r'$\vec{q}$',fontsize='x-large')
plt.ylabel(r'$\epsilon \ in (\mu eV)$',fontsize = 'x-large')
plt.title('Extrinsic splitting')
legend = ax.legend(loc='upper center', shadow=True)
plt.show()