#!/usr/bin/python3

def pairs(l, sum):
    permuts = [ (l[i], l[j]) for i in range(len(l)) for j in range(len(l)) if i != j ]
    return len(list(filter(lambda x: x[0] + x[1] == sum, permuts)))



print(pairs([1,2,2,4,5], 6))
