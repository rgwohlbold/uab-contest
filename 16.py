#!/usr/bin/python3

def rev(s):
    words = s.split(" ")
    res = ""
    while len(words) > 0:
        res += words.pop() + " "
    return res[:-1:]

print(rev("bob is your uncle"))
