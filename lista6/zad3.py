import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import scipy.misc as sp

x = [-2.2, -0.3, 0.8, 1.9]
y = [-15.18, 10.962, 1.92, -2.04]

#Dopasowywanie wielomianu do punktów poprzez interpolacje wielomianową
f2 = interpolate.lagrange(x,y)

xnew = np.arange(-2.2, 1.9, 0.1)
ynew = f2(xnew)

plt.plot(x, y, "o", xnew, ynew, '-')
plt.show()

#Obliczanie pochodnych wielomianu w punkcie 0
p1 = sp.derivative(f2, 0.0, 0.00001)
p2 = sp.derivative(f2, 0.0, 0.00001, 2)
print(f"Pierwsza pochodna w punkcie x = 0.0 => {p1}" )
print(f"Druga pochodna w punkcie x = 0.0 => {p2}" )
