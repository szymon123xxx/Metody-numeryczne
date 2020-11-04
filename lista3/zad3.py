
import numpy as np
A = [[0, 0, 2, 1, 2], [0, 1, 0, 2, -1], [1, 2, 0, -2, 0], [0, 0, 0, -1, 1], [0, 1, -1, 1, -1]]
b = [[1], [1], [-4], [-2], [-1]]

x = np.linalg.solve(A, b)
y = np.allclose(np.dot(A, x), b) #sprawdzanie poprawnosci
print(x)
print(y)
