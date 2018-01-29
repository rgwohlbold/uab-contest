#!/usr/bin/python3

def missing(lst):
    for x,y in enumerate(lst):
        if (x + 1 != y):
            return x + 1
    return x + 1

print(missing([1, 2, 3, 5]))
