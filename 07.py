#!/usr/bin/python3

def check(number):
    digits = list(map(lambda x: int(x), str(number)))
    odds = [ digits[x] for x in range(0, 15, 2) ]
    evens = [ digits[x] for x in range(1, 15, 2) ]
    m4 = len(list(filter(lambda x: x > 4, odds)))
    total = 2 * sum(odds) + sum(evens) + m4
    return 10 - (total % 10)



print(check(314159265358979))
