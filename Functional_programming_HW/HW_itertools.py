import itertools


def combinations(n):
    comb_list = []
    for i in range(1, n + 1):
        comb_list += itertools.product("AGTC", repeat=i)
    for tuples in comb_list:
        yield ''.join(tuples)


print(list(combinations(3)))
