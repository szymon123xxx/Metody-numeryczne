import copy

def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b

a = [[-1, 1, -4], [2, 2, 0], [3, 3, 2]]
b = [[0], [1], [0.5]]
det, c = gauss(a, b)

A = [[0, 0, 2, 1, 2], [0, 1, 0, 2, -1], [1, 2, 0, -2, 0], [0, 0, 0, -1, 1], [0, 1, -1, 1, -1]]
B = [[1], [1], [-4], [-2], [-1]]
det, d = gauss(A, B)

L = [[1, 0, 0], [3/2, 1, 0], [1/2, 11/13, 1]]
bb = [[1], [-1], [2]]
det, e = gauss(L, bb)

U = [[2, -3, -1], [0, 13/2, -7/2], [0, 0, 32/13]]
det, e2 = gauss(U,e)

print("Macierz zadanie 1", c)
print("Macierz zadanie 3", d)
print("Macierz zadanie 2", e2)