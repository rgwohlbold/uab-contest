#!/usr/bin/python3

def phone(numbers):

    # How many numbers for each region
    dallas, tallahassee, birmingham, nashville, other = 0,0,0,0,0

    for number in numbers:

        # The tail of the number is the last 7 digits, so a floor division removes it and leaves the area code
        area = number // 10000000

        # Increment locations based on area code
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

    # Return total number of repective area codes
    return [dallas, tallahassee, birmingham, nashville, other]


print(phone([2057281628, 4692581647, 1234567890]))
