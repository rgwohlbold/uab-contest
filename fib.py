#!/usr/bin/python
import sys

def fib(n):
    fibs = [0, 1]
    for _ in range(2, n+1):
        fibs[0], fibs[1] = fibs[1], fibs[0] + fibs[1]
    return fibs[1]


print(fib(100000))

