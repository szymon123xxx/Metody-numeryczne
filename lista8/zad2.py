from scipy.linalg import hilbert
from scipy.linalg import eigh


a = hilbert(6)

# Solve a standard or generalized eigenvalue problem for a complex Hermitian or real symmetric matrix and find eigenvalues array w and optionally eigenvectors array v of array a
x = eigh(a)

print(f"Macierz hilberta 6x6 -> {a}")
print(f"Wartości oraz wektory własne macierzy hilberta -> {x}")
