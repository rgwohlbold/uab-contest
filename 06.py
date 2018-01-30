#!/usr/bin/python3
import math

# Calculate distance between two poins of form (x,y)
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Get if a triangle of form (x1, y1, x2, y2, x3, y3) is pythagoran
def pythagoran(v):

    # Get points from list
    p1 = (v[0], v[1])
    p2 = (v[2], v[3])
    p3 = (v[4], v[5])

    # Calculate distances between points
    d1 = distance(p1, p2)
    d2 = distance(p1, p3)
    d3 = distance(p2, p3)

    # If one of a^2 + b^2 == c^2, the triangle is pythagoran
    res = d1 ** 2 + d2 ** 2 == d3 ** 2
    res |= d1 ** 2 + d3 ** 2 == d2 ** 2
    res |= d2 ** 2 + d3 ** 2 == d1 ** 2

    return res


print(pythagoran([0,0,0,3,4,0]))
print(pythagoran([1,3,4,5,6,7]))


    
