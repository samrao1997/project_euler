"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""
import math


def digit_sum(num):

    result = 0
    num_str = str(num)

    for digit_str in num_str:
        result += int(digit_str)
    return result


def sol():
    result = 0

    for a in range(100):
        for b in range(100):
            num = a ** b
            check = digit_sum(num)

            if check > result:
                print("a: ", a)
                print("b: ", b)
                print("check: ", check)
                result = check

    return result
