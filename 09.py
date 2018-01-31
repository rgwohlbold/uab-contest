#!/usr/bin/python3

def merge(l1, l2):
    l1 += l2
    return sorted(l1)


print(merge([1,2,5,6], [2,2,4,5]))
