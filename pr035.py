"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math


def is_prime(num):
    if num == 1:
        return False

    if num == 2:
        return True

    value = math.ceil(math.sqrt(num)) + 1

    for i in range(2, value):
        if num % i == 0:
            return False

    return True


def check_rotation(num):
    if not is_prime(num):
        return False

    num_str = str(num)

    for i in range(1, len(num_str)):
        rot = num_str[i:] + num_str[:i]
        if not is_prime(int(rot)):
            return False
    return True


def sol():
    total = 0
    for i in range(1, 1000000):
        if check_rotation(i):
            total += 1
    return total


print(sol())
