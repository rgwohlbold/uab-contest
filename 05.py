#!/usr/bin/python3

def area(diags):
    x = abs(diags[0] - diags[2])
    y = abs(diags[1] - diags[3])
    return x*y


print(area([2, 5, 5, 2]))
