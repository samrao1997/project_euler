"""
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

"""


def sol():
    result = 0

    p = 1
    q = 1

    for i in range(1001):
        a = p + 2 * q
        b = p + q

        if len(str(a)) > len(str(b)):
            result += 1

        p = a
        q = b

    return result