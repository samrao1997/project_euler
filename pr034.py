"""

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math


def check_curious(num):
    if num in [1, 2]:
        return False

    total = 0
    num_str = str(num)

    for digit in num_str:
        total += math.factorial(int(digit))

    if total == num:
        return True

    return False


def sol():
    total = 0

    for i in range(1, 10000000):
        if check_curious(i):
            print(i)
            total += i

    return total


print(sol())
