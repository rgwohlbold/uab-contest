#!/usr/bin/python3

import random

def distance(w1, w2):
    d = 0
    assert(len(w1) == len(w2))
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            d += 1
    return d

def visit(word, close, visited):
    if word in visited:
        return False
    visited.append(word)
    for w in close[word]:
        if visit(w, close, visited):
            return True

    if len(visited) == len(close):
        return True
    visited.pop()
    return False


def chain(l):
    # Create a dict with words as keys and a list of their close words as values
    close = {}
    for w in l:
        close[w] = []
    for w1 in l:
        for w2 in l:
            if w1 != w2 and distance(w1, w2) == 1 and w1 not in close[w2]:
                close[w1].append(w2)
                close[w2].append(w1)

    # Do a DFS with every word as the starting word
    for w in close.keys():
        visited = []
        if visit(w, close, visited):
            return visited
    return None

    
c = ["cord","ward","cold","warm","card"]
c2=["stone","shone","aloof","chine","chins","coins"]
c3 = ["coins","chine","chins","shone","shine","stone"]
print(chain(c))

