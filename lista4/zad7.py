from sympy import solveset
from sympy.abc import x
import sympy
x = solveset(x**4 + (5+sympy.I)*x**3 - (8 - 5*sympy.I)*x**2 + (30 - 14*sympy.I)*x - 84, x) # domain=S.Complexes is default
print(x)