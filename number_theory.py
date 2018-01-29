"""
UAB Competition Programs
by Tenniel Miao

Number Theory
"""


def euclidean_gcd(a: int, b: int):
    """
    compute the greatest common divisor of two positive integers, a and b, using the Euclidean algorithm
    """
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    """
    return the least common multiple of two integers, a and b.
    """
    return a * b // euclidean_gcd(a, b)


def extended_euclidean_gcd(a: int, b: int):
    """
    extended euclidean algorithm, returning the gcd and two bezout coefficients
    """
    alpha, s, beta, t = 1, 0, 0, 1
    while b > 0:
        a, (q, b) = b, divmod(a, b)
        alpha, s = s, alpha - q * s
        beta, t = t, beta - q * t
    return a, alpha, beta


def modular_inverse(a: int, b: int):
    """
    return the modular inverse of a mod b; NEED extended euclidean algorithm
    """
    d, alpha, beta = extended_euclidean_gcd(a, b)
    # a * alpha + b * beta ==  d
    return alpha % b if d == 1 else None
