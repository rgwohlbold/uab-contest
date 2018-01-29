#!/usr/bin/python3

import math

def expand(frac, n):
    lcm = frac[1] * n // math.gcd(frac[1], n)
    frac[0] *= lcm
    frac[1] *= lcm


def reduce(frac):
    gcd = math.gcd(frac[0], frac[1])
    frac[0] //= gcd
    frac[1] //= gcd
    

def decompose(frac):
    f = list(frac)
    n = f[0] / f[1]
    units = []
    while f[0] > 0:
        units.append((1, math.ceil(f[1] / f[0])))
        f[0], f[1] = -f[1] % f[0], f[1] * math.ceil(f[1] / f[0])
        reduce(f)
    return units

print(decompose((6,7)))

