from scipy.linalg import hilbert
import numpy as np

def Norm_Wska(n):
    c = hilbert(n)

    norm = np.linalg.norm(c)
    wska = np.linalg.cond(c)

    print("Wskażnik uwarunkowania = ", wska)
    print("Norma = ", norm)

Norm_Wska(3)
Norm_Wska(10)
Norm_Wska(20)
