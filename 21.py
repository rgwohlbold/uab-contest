#!/usr/bin/python3

def pushup(score):
    assert(score%11==0)
    td = score // 11
    total = 0
    for i in range(1, td+1):
        total += i
    return total

print(pushup(33))
