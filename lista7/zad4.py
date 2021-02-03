from scipy.integrate import solve_ivp
import numpy as np
import math as ma
import matplotlib.pyplot as plt

def function(t, y):
    return [y[1], - ma.sin(y[0]) - 1]


utest = [0.5, 1, 1.5] # przedział w jakim strzelamy
y_a = 0 #Warunek brzegowy
t_k = 2
y_b = 0 #Warunek brzegowy
t = np.arange(0, t_k, 0.001) #Ilość punktów na wykresie
for u in utest:
    y0 = [y_a, u]
    wu = solve_ivp(function, [0, t_k], y0, t_eval=t , atol=1e-10, rtol=13-8, method="RK45")
    plt.plot(wu.t, wu.y[0])

plt.plot([0, t_k], [y_a, y_b], 'o', label="war. brzeg")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(["0.5", "1", "1.5"])
plt.show()