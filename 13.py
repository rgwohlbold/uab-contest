#!/usr/bin/python3

# This method recursively removes characters that have the same adjacent character
def rem(s):
    new = ""

    # Add first character if different from second one
    if s[0] != s[1]:
        new = s[0]

    # Add characters if different from adjacent ones
    for i in range(1, len(s) - 1):
        if s[i] != s[i-1] and s[i] != s[i+1]:
            new += s[i]

    # Add last character if different from second-last one
    if s[-1] != s[-2]:
        new += s[-1]

    # If adjacent characters are the same, call itself again
    prev = new[0]
    for c in new[1::]:
        if c == prev:
            return rem(new)
        prev = c
    return new


print(rem("acbbcdbccb"))
