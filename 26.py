#!/usr/bin/python3

def palindrome(s):
    palindromes = []
    for i in range(len(s) - 1):
        if s[i] not in s[i+1::]:
            continue
        start = i
        ends = [s.index(s[i], i+1)]
        while s[i] in s[ends[-1]+1::]:
            ends.append(s.index(s[i], ends[-1] + 1))
        for end in ends:
            back = end
            result = True
            while start < end:
                if s[start] != s[end]:
                    result = False
                    break
                end -= 1
                start += 1
            if result:
                palindromes.append(s[i:back+1:])
    lengths = list(map(lambda x: len(x), palindromes))
    return palindromes[lengths.index(max(lengths))]

print(palindrome("anna"))



        
