import numpy as np

A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
B = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
w = np.array([[1], [-2], [3]])

print("Wynik mnożenia A*B =", A.dot(B))
print("Wynik mnożenia A*w =", A.dot(w))
print("Wynik mnożenia B*(A*w) =", B.dot(A.dot(w)))
print("Wyznacznik macierzy A = ", np.linalg.det(A))
print("Wyznacznik macierzy B = ", np.linalg.det(B))
print("Macierz odwrotna A = ", np.linalg.inv(A))
print("Macierz odwrotna A = ", np.linalg.inv(B))
