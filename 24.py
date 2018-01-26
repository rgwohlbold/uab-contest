#!/usr/bin/python

def greatest(l):
    max = 0
    i = 0
    for n in l:
        sum = 0
        for m in l[i::]:
            sum += m
            if sum > max:
                max = sum
        i += 1
    return max




print(greatest([2, -5000]))


