import random
import numpy
import matplotlib.pyplot as plt

# Three corners of an equilateral triangle
corner = [(0, 0), (0.5, 0.5), (1, 0)]

n = 100000
x = numpy.zeros(n)
y = numpy.zeros(n)


# Estimation of half of the distance
def middle(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


# Choice of random vertex and coordinate movement
for i in range(1, n):
    rand_vertex = random.randint(0, 2)
    x[i], y[i] = middle(corner[rand_vertex], (x[i - 1], y[i - 1]))

# Visualization of Sierpinski triangle
plt.title("Sierpinski triangle ($n = " + str(n) + "$ steps)")
plt.scatter(x, y, s=1)
plt.savefig("Sierpinski_triangle.png")
