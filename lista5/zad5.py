from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
x = [1, 2.5, 3.5, 4, 1.1, 1.8, 2.2, 3.7]
y = [6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828]

#Dopasowywanie f. kwadratowej
f = interpolate.interp1d(x, y, kind="quadratic")

xnew = np.arange(1, 4, 0.001)
ynew = f(xnew)

#Dopasowywanie prostej do punktow
linear = np.polyfit(x, y, 1)
linear_y = np.poly1d(linear)(x)

plt.plot(x, y, "o", xnew, ynew, '-')
plt.plot(x, linear_y)
plt.grid()
plt.show()

