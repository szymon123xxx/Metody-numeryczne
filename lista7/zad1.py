import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def function(t, y):
    return np.sin(t * y)

y_p = 0
y_k = 6
y_a = [2, 2.5, 3, 3.5]
t = np.arange(0, 6, 0.001) #Ilość punktów na wykresie
for i in y_a:
    result = solve_ivp(function, [y_p, y_k], [i], t_eval=t, atol=1e-12, rtol=1e-9, method="LSODA")
    plt.plot(result.t, result.y[0], '-')
    print("Wynik:")
    print(result)

plt.xlabel('t')
plt.ylabel('y')
plt.legend(["2", "2.5", "3", "3.5"])

plt.show()