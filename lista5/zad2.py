import numpy as np
from scipy.optimize import fsolve
from scipy import interpolate
from scipy import misc
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline


x = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
y = [-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334]

# Dopasowywanie funkcji do punktów
f = interpolate.interp1d(x, y, kind="cubic")

xnew = np.arange(1, 3, 0.001)
ynew = f(xnew)

tab = []
for i in range(4):
    tab.append(0)
i = 1

plt.plot(tab) # rysowanie OX
plt.plot(x, y, "o", xnew, ynew, '-')
plt.show()

#Wyliczanie miejsc zerowych funkcji
x0 = fsolve(f, [1.15])
x1 = fsolve(f, [2.2])
x2 = fsolve(f, [2.7])
print("x0 =" + str(x0))
print("x1 =" + str(x1))
print("x2 =" + str(x2))

spl = UnivariateSpline(xnew, ynew, k=1, s =2)
# Ponizszy kod wyrysowuje nam ta sama funckje "plt.plot(x, y, "o", xnew, ynew, '-')"
# spl.set_smoothing_factor(0.1)
# plt.plot(xnew, spl(xnew), 'g', lw=2)
# plt.show()

#zgadywanie pochodnej w punkcie 2.1
print(spl.derivatives(2.1))