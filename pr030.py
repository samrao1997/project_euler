"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def power_sum(num, power):
    # given num sum all digits of num to a power of pow

    num_str = str(num)
    result = 0

    for digit in num_str:
        result += int(digit) ** power

    return result


def sol():
    result = 0

    for i in range(10, 354295):
        if i == power_sum(i, 5):
            result += i

    return result


print(sol())
