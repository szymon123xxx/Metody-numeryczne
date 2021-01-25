import math as mp
from scipy import integrate


def function(y,x):
    return (mp.sin(mp.pi * x) * mp.sin(mp.pi*(y - x)))

#Compute a double integral./Return the double (definite) integral of func(y, x) from x = a..b and y = gfun(x)..hfun(x)
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.dblquad.html
w = integrate.dblquad(function, 0, 1, lambda x: 0, lambda x: x)

print(f"Wynik całkowania => {w}")