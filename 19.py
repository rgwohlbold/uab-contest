#!/usr/bin/python
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# If distance is shorter than outer circle radius, c1 contains c2
def isin(inner, outer):
    return distance(inner[0], outer[0]) < outer[1] and outer[1] > inner[1]

# Circle is passed as ((x, y), r)
def intersect(c1, c2):
    # If circles are the same
    if c1 == c2:
        return math.inf
    d = distance(c1[0], c2[0])
    if isin(c2, c1):
        print("c2 is in c1")
        c1, c2 = c2, c1
    # Check if center of c1 is in c2
    if isin(c1, c2):
        # Inner circle is fully contained, no intersections
        if d + c1[1] < c2[1]:
            return 0
        # Inner circle touches outer circle
        elif d + c1[1] == c2[1]:
            return 1
        else:
            return 2
    else:
        # Circles don't intersect
        if d > c1[1] + c2[1]:
            return 0
        # Circles touch
        elif d == c1[1] + c2[1]:
            return 1
        else:
            return 2

c1 = ((3, 0), 3)
c2 = ((0, 0), 5)
print(intersect(c1, c2))
