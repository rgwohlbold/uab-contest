#!/usr/bin/python3


def check(s):
    stack = []
    pushc = "({["
    popc = ")}]"
    for c in s:
        if c in pushc:
            stack.append(pushc.index(c))
        elif c in popc:
            last = stack.pop()
            if popc[last] != c:
                return False
    return len(stack) == 0

print(check("()([)]"))
