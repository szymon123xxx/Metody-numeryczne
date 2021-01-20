import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import lagrange

x = [0.0, 0.1, 0.2, 0.3, 0.4]
y = [0.0, 0.078348, 0.13891, 0.192916, 0.244981]

f = interpolate.interp1d(x, y, kind="quadratic")
xnew = np.arange(0, 0.4, 0.001)
ynew = f(xnew)

plt.plot(x, y, "o", xnew, ynew, '-')
plt.show()

p1 = lagrange(x, y)
pochodna = np.polyder(p1)

print(f"Pochodna w punkcie x = 0.2 => {pochodna(0.2)}")