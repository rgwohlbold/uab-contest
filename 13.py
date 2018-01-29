#!/usr/bin/python3

s = "abbcbbcdbccbd"
prev = ""

def rem(s):
    prev = ""
    new = ""
    j = 0
    for i in range(len(s)):
        if prev != s[i]:
            j = 0

        if j == 0 and s[i+1] != s[i]:
            new += s[i]
        elif j != 0 and prev != s[i]:
            new += s[i]

        prev = s[0]
        for i in s[1::]:
            if i == prev:
                return rem(new)
        return new

print(rem(s))
