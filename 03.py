#!/usr/bin/python3

def phone(numbers):
    dallas, tallahassee, birmingham, nashville, other = 0,0,0,0,0
    for number in numbers:
        area = number // 10000000
        if area == 469:
            dallas += 1
        elif area == 850:
            tallahassee += 1
        elif area == 205:
            birmingham += 1
        elif area == 615:
            nashville += 1
        else:
            other += 1
    return [dallas, tallahassee, birmingham, nashville, other]


print(phone([2057281628, 4692581647, 1234567890]))
