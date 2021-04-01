"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(num):
    memo = [1]

    if num < 1:
        return memo[0]

    i = 0

    while i != num:
        memo.append(memo[i] * (i + 1))
        i += 1
    return memo[-1]


def sol(value):
    num = factorial(value)
    num_str = str(num)
    result = 0
    for digit in num_str:
        result += int(digit)
    return result
