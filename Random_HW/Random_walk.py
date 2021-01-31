import random

import matplotlib.pyplot as plt
import numpy as np

n = 10000
x = np.zeros(n)
y = np.zeros(n)

# Filling array with coordinates
for i in range(1, n):
    step = random.randint(1, 4)
    if step == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif step == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif step == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

# Visualization of random walk
plt.title("Random Walk ($n = " + str(n) + "$ steps)")
plt.plot(x, y)
plt.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)
