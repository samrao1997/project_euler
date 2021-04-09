"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

memo = [1, 1]


def fast_fib(n):

    if n <= 2:
        return memo[0]

    i = 2

    while i != n:
        memo.append(memo[i - 1] + memo[i - 2])
        i += 1

    return memo[-1]


def check_digits(num):
    num_str = str(num)
    return len(num_str)


def dumb_sol():
    # There is def a smarter way of doing this
    i = 0
    while check_digits(fast_fib(i)) != 1000:
        i += 1
    return fast_fib(i)


import math


def sol(n):
    return math.ceil(4.78497 * n - 3.1127)


print(sol(1000))
