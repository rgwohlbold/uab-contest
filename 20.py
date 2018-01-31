#!/usr/bin/python3

def diamond(n):
    assert(n%2==1)
    result = ""
    for i in range(1, n+1, 2):
        space = (n-i) // 2
        result += " " * space
        result += "*" * i
        result += "\n"
    for i in range(n-2, 0, -2):
        space = (n-i) // 2
        result += " " * space
        result += "*" * i
        result += "\n"
    return result

print(diamond(31))
            

