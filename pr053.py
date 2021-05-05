"""
"""

import math


def nCr(n, r):
    num = math.factorial(n)
    dem = math.factorial(r) * math.factorial(n - r)
    return num / dem


def sol():
    result = 0

    for n in range(1, 101):
        for r in range(0, n + 1):
            if nCr(n, r) > 1000000:
                result += 1

    return result