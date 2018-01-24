#!/usr/bin/python3
import random

def distance(w1, w2):
    d = 0
    assert(len(w1) == len(w2))
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            d += 1
    return d

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

    # Find a start word which ideally has one close word, if one does not exist, choose a random word that has close words
    start = -1
    for k in close:
        if len(close[k]) == 1:
            start = k
            break
        elif len(close[k]) == 0:
            del close[k]
    if start == -1:
        start = random.randint(0, len(close))

    # Create the chain list by looking for close words that not already in the chain in the dictionary
    chain = [start]
    while len(close) > 0:
        if len(close[chain[-1]]) == 1 and close[chain[-1]][0] in chain:
            break
        for child in close[chain[-1]]:
            if child != chain[-1::] and child not in chain:
                del close[chain[-1]]
                chain.append(child)

    return chain
    
c = ["cord","ward","cold","warm","card"]
c2=["stone","shone","aloof","chine","chins","coins"]
c3 = ["coins","chine","chins","shone","shine","stone"]
print(chain(c3))

