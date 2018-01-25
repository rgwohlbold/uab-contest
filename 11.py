#!/usr/bin/python

def peaks(floats):
    res = []
    for i in range(len(floats)-1):
        if floats[i] > max(floats[i+1::]):
            res.append(floats[i])
    res.append(floats[-1])
    return res

print(peaks([4.0, 6.0, 4.0, 2.0]))

