import math as ma
import numpy as np
import scipy.misc as sp
import matplotlib.pyplot as plt

def funkcja(x):
    return ma.log(np.tanh(x /( x**2 + 1 )))

p1 = sp.derivative(funkcja, 0.2, 0.00001)
p2 = sp.derivative(funkcja, 0.2, 0.00001, 2)
p3 = sp.derivative(funkcja, 0.2, 0.00001, 3, order=7)

print(f"Pierwsza pochodna w x = 0.2 => {p1}" )
print(f"Druga pochodna w x = 0.2 => {p2}" )
print(f"Trzecia pochodna w x = 0.2 => {p3}" )
