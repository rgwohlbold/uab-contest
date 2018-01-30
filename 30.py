#!/usr/bin/python3

def cups(heights):
    # the running count of filled 'water tiles'
    filled = 0
    # the highest cup tower hit so far 
    maxheight = 0
    # the running count of 'water tiles' that might be filled
    potentialfill = 0

    for x in heights:
        # if the cup tower im at currently is larger than my previous maxheight
        # then i should add all of my potential fill to my filled becuase i 
        # have confirmed the valley is blocked off and holds water
        if x >= maxheight:
            maxheight = x
            filled += potentialfill
            potentialfill = 0
        # else i should add the distance from the max height to the valley floor
        # to simulate what the water level would be if it is indeed filled with water
        else:
            potentialfill += (maxheight - x)

    # i then repeat all of this but approaching from the opposite side so that
    # i get the valleys to the left of the highest cup tower.
    maxheight = 0
    potentialfill = 0
    for x in heights[::-1]:
        if x >= maxheight:
            maxheight = x
            filled += potentialfill
            potentialfill = 0
        else:
            potentialfill += (maxheight - x)
    # all the top cups will be filled regardless of the cups height or arrangement
    # so the length is added to represent one unit of water filled for each cup.
    filled += len(heights)

    return filled

print(cups([3,1,2,1,4]))
