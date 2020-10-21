import numpy as np

i = 1
for n in range(2, 20):
    i = np.e - ((n+1)*i)
    print('x' + str(n) + '=' + str(i))
