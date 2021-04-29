import itertools


def combinations(n):
    for i in range(1, n + 1):
        for seq in itertools.product("AGTC", repeat=i):
            yield ''.join(seq)


print(list(combinations(3)))
