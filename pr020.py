"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


import math


def sol(value):
    num = math.factorial(value)
    num_str = str(num)
    result = 0
    for digit in num_str:
        result += int(digit)
    return result