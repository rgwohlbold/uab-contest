#!/usr/bin/python3

def nums(s):
    numbers = [0,0,0]
    for c in s:
        if c.isupper():
            numbers[0] += 1
        elif c.islower():
            numbers[1] += 1
        else:
            numbers[2] += 1
    return numbers

print(nums("MySecurePwd123!"))

