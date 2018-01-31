#!/usr/bin/python3

def valid(s):
    prev = ""
    for c in s:
        if not (c.islower() or c.isdigit() or c=='_'):
            return False
        if c == '_' == prev:
            return False
        prev = c
    if not c[0].isalpha():
        return False
    if c[-1] == '_':
        return False
    return True

print(valid("ajgkqj124u8_278jh"))
print(valid("qkgj__qjkjwklj"))
print(valid("141jwkj"))
