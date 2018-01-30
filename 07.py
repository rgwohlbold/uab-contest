#!/usr/bin/python3

# Return the check digit of a 15-digit credit card number
def check(number):
    # Get number as a list of digits
    digits = list(map(int, str(number)))

    # Get the digits at odd positions (positions start as one)
    odds = digits[0::2]

    # Get the digits at even positions (positions start as one)
    evens = digits[1::2]

    # Get the number of odd-positioned numbers greater than 4
    m4 = len(list(filter(lambda x: x > 4, odds)))

    # Calculate sum of doubled odd positions, sum of evens and the number of odd-positioned numbers greater than 4
    total = 2 * sum(odds) + sum(evens) + m4

    # Return the check digit
    return 10 - (total % 10)



print(check(314159265358979))
