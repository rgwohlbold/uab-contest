#!/usr/bin/python3

def collatz(seed):
    length = 1
    while seed != 1:
        length += 1
        seed = seed // 2 if seed % 2 == 0 else 3 * seed + 1
    return length

print(collatz(22))

