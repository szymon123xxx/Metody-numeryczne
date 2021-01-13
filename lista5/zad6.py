from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
x = [0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150]
y = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]

z = np.polyfit(x, y, 2)
p = np.poly1d(z)

xnew = np.arange(-1, 10.5, 0.01)

plt.plot(x, y, '.', xnew, p(xnew))
plt.show()

print("Współrzędne 'y' w punkcie x = 10.5 -> y = " + str(p(10.5)))