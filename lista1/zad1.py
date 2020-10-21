import math
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 1.5, 0.001)
list1 = []
list2 = []
for i in x:
    y = math.cos(i) - 3*math.sin(math.tan(i) - 1)
    list1.append(y)
    list2.append(0)
plt.plot(list1)
plt.plot(list2)
plt.show()
