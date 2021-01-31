import random
import time

import matplotlib.pyplot as plt
import numpy as np


# Generate random list
def random_list(max_int, length):
    return [random.randint(0, max_int) for _ in range(length)]


# Check if the list is sorted
def sort_check(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True


# Monkey sort realisation
def monkey_sort(lst):
    while not sort_check(lst):
        random.shuffle(lst)
    else:
        return lst


n = 10
x = np.zeros(n - 1)
y = np.zeros(n - 1)

# Time of monkey sort vs Length of random list
for i in range(2, n + 1):
    duration = np.zeros(100)
    for rep in range(100):
        rd_list = random_list(i, i)
        start_time = time.time()
        sorted_list = monkey_sort(rd_list)
        finish_time = time.time() - start_time
        duration[rep] = finish_time
    x[i - 2] = i
    y[i - 2] = np.mean(duration)
    yerr = np.var(duration)
    plt.errorbar(i, np.mean(duration), yerr=yerr, capsize=3, ecolor='green')
plt.scatter(x, y)
plt.xlabel("Array Length")
plt.ylabel("Time")
plt.title("Time of monkey sort vs Length of random list")
plt.savefig("Monkey_sort.png")
