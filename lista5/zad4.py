import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import lagrange

Re = [0.2, 2, 20, 200, 2000, 20000]
Cd = [103, 13.9, 2.72, 0.8, 0.401, 0.433]

#Nakładanie podwójnej logarytmicznej skali
cs = lagrange(np.log(Re), np.log(Cd))
xs = np.arange(0.2, 20000, 0.1)
y2 = np.exp(cs(np.log(xs)))

fig, ax = plt.subplots(figsize=(6.5, 4))

ax.plot(Re, Cd, 'o', label='data')
ax.plot(xs, y2)

plt.xscale('log')
plt.yscale('log')
plt.show()
# Rozwiązania Cd
print(f"Cd dla Re -> 5.5 = {cs(5.5)}" )
print(f"Cd dla Re -> 5000 = {cs(5000)}")