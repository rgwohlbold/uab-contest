#!/usr/bin/python3

def rotate(s):
    return s[-2::] + s[:-2:]

def check_rotate(orig, new):
    return rotate(orig) == new


print(check_rotate("math", "thma"))
