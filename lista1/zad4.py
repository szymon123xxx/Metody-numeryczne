import numpy as np
listn4 = []
listn5 = []
for i in range(4):
    listn4.append([])
    for j in range(4):
        listn4[i].append(1 / (i + j + 1))
for i in range(8):
    listn5.append([])
    for j in range(8):
        listn5[i].append(1 / (i + j + 1))


print("Macierz wygenerowana n4: \n", listn4)
print("Macierz odwrotna n4: \n", np.linalg.inv(listn4))
print("Macierz wygenerowana: n5 \n", listn5)
print("Macierz odwrotna n5: \n", np.linalg.inv(listn5))
print("Wyznacznik macierzy n4: \n", np.linalg.det(listn4))
print("Wyznacznik macierzy n5: \n", np.linalg.det(listn5))
