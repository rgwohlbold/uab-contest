#!/usr/bin/python3

def greatest(thelist):
    maxvalue = 0
    runningsum = 0
    for number in thelist:
        if runningsum < 0:
            runningsum = 0
        runningsum += number
        if runningsum > maxvalue:
           maxvalue = runningsum
    return maxvalue 

print(greatest([1,2,-2,4]))


