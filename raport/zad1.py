from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

def function(t, x):
    return [ x[1], 10*x[0] -3*x[1] ]

y_a = 4 # Miejsce zerowe w punkcie y(0) = 4
dy = -2 # Miejssce zerowe w punkcie y'(0) = -2
t_p = 0 # Początek przedziału
t_k = 1 # Koniec przedziału

y0 = [y_a, dy]
t = np.arange(0, t_k, 0.001)

result = solve_ivp(function, [t_p, t_k], y0, t_eval=t ,atol=1e-10, rtol=13-8,method="LSODA")

plt.plot(result.t, result.y[0])
plt.plot(result.t, result.y[1])

plt.grid(color='darkgrey', linestyle='-', linewidth=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(["LSODA","dy/dt(LSODA)" ])
plt.show()

extremum = argrelextrema(result.y[0], np.less)[0]
print("Ekstremum" ,result.t[extremum]) #extremum funkcji






