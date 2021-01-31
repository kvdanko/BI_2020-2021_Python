import random
import time

import matplotlib.pyplot as plt
import numpy as np

n = 10
y_numpy = np.zeros(n)
y_random = np.zeros(n)
x = np.arange(0, 10000, 1000, dtype=int)

# Random vs Numpy time comparison
for idx, val in enumerate(x):
    start_random = time.time()
    random_list = [random.random() for i in range(val)]
    finish_random = time.time() - start_random
    start_numpy = time.time()
    numpy_list = np.random.uniform(size=val)
    finish_numpy = time.time() - start_numpy
    y_numpy[idx] = finish_numpy
    y_random[idx] = finish_random

plt.title("Numpy/Random comparison")
plt.scatter(x, y_numpy, label="numpy")
plt.scatter(x, y_random, label="random")
plt.legend()
plt.xlabel("Array Length")
plt.ylabel("Time")
plt.savefig("Numpy_Random_comparison")
