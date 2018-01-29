#!/usr/bin/python3

def check(number):
    digits = list(map(int, str(number)))
    odds = digits[0::2]
    evens = digits[1::2]
    m4 = len([x for x in odds if x>4])
    total = 2 * sum(odds) + sum(evens) + m4
    return 10 - (total % 10)



print(check(314159265358979))
