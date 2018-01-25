#!/usr/bin/python

def missing(list):
    for i in range(1, len(list) + 2):
        if i not in list:
            return i

print(missing([1, 2, 3, 5]))
