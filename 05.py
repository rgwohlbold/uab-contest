#!/usr/bin/python3

# Input: Coordinates of diagonal endpoints: [x1, y1, x2, y2]
def area(diags):
    # Width of rectangle
    x = abs(diags[0] - diags[2])
    # Height of rectangle
    y = abs(diags[1] - diags[3])
    return x * y


print(area([2, 5, 5, 2]))
