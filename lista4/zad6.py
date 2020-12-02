from scipy import optimize
import math
import numpy as np

def func(data):
    x, y = data
    f = math.tan(x) - y - 1
    g = math.cos(x) - 3 * math.sin(y)
    return [f, g]


wynik = []

for i in np.arange(0, 1.6, 0.01):
    for j in np.arange(0, 1.6, 0.01):
        x1 = optimize.root(func, [i, j])
        if(x1.success):
            if 0 <= round(x1.x[0], 3) <= 1.5:
                if [round(x1.x[0], 3), round(x1.x[1], 3)] not in wynik:
                    wynik.append([round(x1.x[0], 3), round(x1.x[1], 3)])

print(wynik)