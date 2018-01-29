#!/usr/bin/python3

def concat(ints):
    with_a = sorted(list(map(lambda x: str(x) + "a", ints)))[::-1]
    return int(''.join(list(map(lambda x: x[:-1:], with_a))))


print(concat([3,30,43,1]))
