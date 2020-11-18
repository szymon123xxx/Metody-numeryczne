import math

u = 2510
M0 = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81

for i in range(10, 90):
    v = u * math.log(M0 / (M0 - m * i)) - g * i
    if v >= 335:
        print(i)
        break
