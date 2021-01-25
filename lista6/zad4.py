import math as ma
from scipy.integrate import simps
import numpy as np

def function(x):
    return ma.cos(2 * ma.cos(x)**-1)

y1 = []
y2 = []
y3 = []
x1 = np.linspace(-1, 1, 3)
x2 = np.linspace(-1, 1, 5)
x3 = np.linspace(-1, 1, 7)
for i in x1:
    y1.append(function(i))
for i in x2:
    y2.append(function(i))
for i in x3:
    y3.append(function(i))

#Integrate y(x) using samples along the given axis and the composite Simpson’s rule
print(f"Metoda Simpsona dla 3 węzłów => {simps(y1,x1)}" )
print(f"Metoda Simpsona dla 5 węzłów => {simps(y2,x2)}" )
print(f"Metoda Simpsona dla 7 węzłów => {simps(y3,x3)}" )
#Przy zwiększaniu ilości węzłów zwiększamy dokładność wyniku ponieważ zwiększamy ilość próbek po której wykonywana jest metoda simpson