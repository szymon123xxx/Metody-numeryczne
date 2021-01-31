import numpy as np
from scipy.linalg import eig
a = [ [-1, -4, 1], [-1, -2, -5], [5, 4, 3]]

#Compute the eigenvalues and right eigenvectors of a square array.
x=np.linalg.eig(a)

print(f"Wartości oraz wektory własne macierzy -> {x}")
