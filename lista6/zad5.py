import math as ma
from scipy import integrate

def function(phi,phi2):
    return (1 / ma.sqrt(1 - (ma.sin(phi2/2)**2 * (ma.sin(phi))**2)))

h15 = ma.pi/12
h30 = ma.pi/6
h45 = ma.pi/4
h0 = ma.pi/2

wynik15 = integrate.quad(function, 0, ma.pi/2, h15)
wynik30 = integrate.quad(function, 0, ma.pi/2, h30)
wynik45 = integrate.quad(function, 0, ma.pi/2, h45)
wynik0 = integrate.quad(function, 0, ma.pi/2, h0)

print(f"Wynik dla 15 stopni = {wynik15[0]}")
print(f"Wynik dla 30 stopni = {wynik30[0]}")
print(f"Wynik dla 45 stopni = {wynik45[0]}")
print(f"Porównanie dla h(0) = pi/2 => {h0}")

