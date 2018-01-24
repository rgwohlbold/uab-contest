#!/usr/bin/python

dic = ["alabama","blue","birmingham","color","story","street","world", "knowledge"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
enc = "zcdlatsvt iwpi lxaa rwpcvt ndjg ldgas"

def shift(s, k):
    new = ""
    for i in s:
        new += alphabet[(alphabet.index(i) + k) % len(alphabet)]
    return new

def test(s):
    words = s.split(" ")
    k = -1
    for i in range(len(alphabet)):
        if shift(words[0], i) in dic:
            k = i
            break
    assert(k >= 0)
    dec = list(map(lambda x: shift(x, k), words))
    return " ".join(dec), len(alphabet) - k

print(test(enc))
