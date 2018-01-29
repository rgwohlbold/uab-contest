#!/usr/bin/python3

def flow(source, target, cups):
    # If there is no valley, no additional cups are filled
    if cups[source] >= cups[target]:
        return 0
    # Get the direction by the sign of the difference 
    direction = (target - source) // abs(target - source)

    level = cups[target]
    current = target - direction
    total = 0
    while cups[current] < level:
        # Add the difference between the current and the target cup to the total
        total += (level - cups[current])
        # Set the current cup to the target water level
        cups[current] = level
        current -= direction
    return total


def cups(list):
    first = list.index(max(list))
    total = len(list)
    
    i = first + 1
    while i < len(list) - 1:
        total += flow(i, i+1, list)
        i += 1

    i = first - 1
    while i > 0:
        total += flow(i, i-1, list)
        i -= 1
    return total

print(cups([3,1,2,1,4]))
