import random

import matplotlib.pyplot as plt
import numpy

# 8 points of square
corner = [(0, 0), (0.5, 0), (1, 0), (0, 0.5),
          (0, 1), (1, 0.5), (1, 1), (0.5, 1)]

n = 100000
x = numpy.zeros(n)
y = numpy.zeros(n)

# Estimation of one third of the distance


def middle(p, q):
    return ((p[0] + q[0]) / 3, (p[1] + q[1]) / 3)


# Choice of random vertex and coordinate movement
for i in range(1, n):
    rand_vertex = random.randint(0, 7)
    x[i], y[i] = middle(corner[rand_vertex], (x[i - 1], y[i - 1]))

# Visualization of Sierpinski carpet
plt.title("Sierpinski carpet ($n = " + str(n) + "$ steps)")
plt.scatter(x, y, s=1)
plt.savefig("Sierpinski_carpet.png")
