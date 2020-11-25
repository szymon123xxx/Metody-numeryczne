from scipy.optimize import newton
from numpy import arange
from numpy import random

f = lambda x, a: x**5 - a
y = lambda x, a: 5*x**4
a = arange(0, 10)
x = random.randn(10)
print(newton(f, x, fprime=y, args = (a,)))