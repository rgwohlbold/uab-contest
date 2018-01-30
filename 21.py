#!/usr/bin/python3

def pushup(score):
    assert(score % 11 is 0)
    return score * 2 - 11

print(pushup(33))
