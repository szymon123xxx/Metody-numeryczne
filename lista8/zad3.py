from scipy.linalg import toeplitz
from scipy.linalg import eigh_tridiagonal
import numpy as np

#Tworzenie macierzy 10x10 oraz 100x100
n10 = 10
n100 = 100

listx10 = []
listy10 = []
listx100 = []
listy100 = []

for i in range(0, n10):
    listx10.append(0)
    listy10.append(0)

for i in range(0, n100):
    listx100.append(0)
    listy100.append(0)

listx10[0] = 2
listx10[1] = -1
listy10[1] = -1

listx100[0] = 2
listx100[1] = -1
listy100[1] = -1

macierz10 = toeplitz(listx10, listy10)
macierz100 = toeplitz(listx100, listy100)

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh_tridiagonal.html
#liczenie wartości własnych oraz wektorów własnych macierzy
offdiagonal = -1 * np.ones(9)
diagonal = 2 * np.ones(10)

offdiagonal2 = -1 * np.ones(9)
diagonal2 = 2 * np.ones(10)

x, y = eigh_tridiagonal(diagonal, offdiagonal)
x2, y2 = eigh_tridiagonal(diagonal2, offdiagonal2)

print(f"Macierz 10x10 = {macierz10}")
print(f"Wartości własne: {x[:3]}")
print(f"Wektory własne: {y[:, :3]}")

print(f"Macierz 100x100 = {macierz100}")
print(f"Wartości własne: {x2[:3]}")
print(f"Wektory własne: {y2[:, :3]}")