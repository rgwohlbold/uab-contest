#!/usr/bin/python3

import sys

def operation(op, stack):
    p = op.split(" ")
    if p[0] == "P":
        stack.append(int(p[1]))
    elif p[0] == "R":
        print(stack[-1])
    elif p[0] in ["A", "S", "M", "D"]:
        b = stack.pop()
        a = stack.pop()
        if p[0] == "A":
            stack.append(a+b)
        elif p[0] == "S":
            stack.append(a-b)
        elif p[0] == "M":
            stack.append(a*b)
        elif p[0] == "D":
            stack.append(a//b)
        else:
            raise RuntimeException("Invalid operation: " + p[0])

def execute(p):
    prog = p.split("\n")
    stack = []
    for line in prog:
        operation(line, stack)

def load(s):
    f = open(s, 'r')
    execute(f.read())
    f.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<filename>")
        exit(-1)
    load(sys.argv[1])
