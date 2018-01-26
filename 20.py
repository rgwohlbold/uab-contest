#!/usr/bin/python

def diamond(n):
    assert(n%2==1)
    result = ""
    center = n // 2 + 1
    for i in range(1, n+1, 2):
        space = (n-i) // 2
        for _ in range(space):
            result += " "
        for _ in range(i):
            result += "*"
        result += "\n"
    for i in range(n-2, 0, -2):
        space = (n-i) // 2
        for _ in range(space):
            result += " "
        for _ in range(i):
            result += "*"
        result += "\n"
    return result

print(diamond(31))
            

