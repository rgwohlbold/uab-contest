#!/usr/bin/python3


# this is the simple solution that runs in O(n)
def missing(lst, length):
    for x,y in enumerate(lst, 1):
        if (x != y):
           return  x
    return x + 1


# this is the more complex solution that runs in O(log(n))
def logMissingHelper(lst,bottom,top):
    
    # if the length of period is 1, then we have the place where
    # the lst skips, so return what the value there wouldve been if it 
    # didnt skip
    if top - bottom == 1:
        return top + 1
    
    # mid is the middle of the period, we check here to see if we are too
    # high or too low.
    mid = (bottom + top) // 2
    
    # if the list isnt what we expected then the skip is before mid
    if lst[mid] != mid + 1:
        return logMissingHelper(lst,bottom,mid)

    # else it is what we expected, and the skip is after
    else:
        return logMissingHelper(lst,mid,top)

def logMissing(lst,length):
    # call the helper function with the bounds of the list and the lst itself
    # [0] is added to lst so that we dont get a indexOutOfBounds exception,
    # the length we are passed is one longer than the lst
    return logMissingHelper(lst+[0],0,length)
    

print(logMissing([1, 2, 3, 4], 5))
