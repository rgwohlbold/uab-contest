#!/usr/bin/python3

def pushup(score):
    points = score // 11
    return points * (points + 1) // 2 * 11

print(pushup(33))
