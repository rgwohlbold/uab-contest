#!/usr/bin/python3

import math

def split(s, n):
    blocks = []
    for i in range(math.ceil(len(s) / n)):
        blocks.append(s[i*5:(i+1)*5:])
    blocks[-1] += " " * (n - len(blocks[-1]))
    return blocks

def swap_rows(b, r1, r2):
    b[r1-1], b[r2-1] = b[r2-1], b[r1-1]

def swap_columns(b, c1, c2):
    c1 -= 1
    c2 -= 1
    for i in range(len(b)):
        new = list(b[i])
        new[c1], new[c2] = new[c2], new[c1]
        b[i] = "".join(new)


b = split("bob is your uncle", 5)
print(b)
swap_rows(b, 1, 2)
print(b)
swap_columns(b, 2, 5)
print("".join(b))
