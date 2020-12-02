from scipy import optimize
import numpy as np

def f(x):
    return [x[0] + np.exp(-1*x[0]) + x[1]**3, x[0]**2 + 2*x[0]*x[1] - x[1]**2 + np.tan(x[0])]


a = [np.array([-1.270, -1.260]), np.array([-0.720, -0.700]), np.array([1.200, 1.210])]

b = []

for i in a:
    x = optimize.root(f, i)
    if(x.success):
        if( x.x[0]**2 + x.x[1]**2 <=4 ):
            b.append(x.x)
print(b)



