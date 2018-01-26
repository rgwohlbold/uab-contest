#!/usr/bin/python3


def decompose(frac):
    n = frac[0] / frac[1]
    units = []
    i = 7
    while round(n, 9) > 0:
        if 1/i <= n:
            n -= 1/i
            units.append((1, i))
        i += 1
    return units

print(decompose((6,7)))

