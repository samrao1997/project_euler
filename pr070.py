"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""


def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if is_coprime(x, y)]
        return len(n)


def check_perm(num1, num2):
    # checks if num2 is a perm of num1

    num1_str = str(num1)
    num2_str = str(num2)

    num1_dict = make_digit_dict(num1_str)
    num2_dict = make_digit_dict(num2_str)

    return num1_dict == num2_dict


def make_digit_dict(num_str):
    result = {}

    for digit in num_str:
        if digit in result.keys():
            result[digit] += 1
        else:
            result[digit] = 1

    return result


def sol():
    min_n = 0
    min_value = 999999999999999

    for n in range(1, 10 ** 7 + 1):
        phi_value = phi_func(n)
        if check_perm(n, phi_value):
            value = n / phi_value
            if value < min_value:
                min_value = value
                min_n = n

    return min_n


from math import sqrt
from operator import mul
from itertools import *


def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    sieve = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n + 1) // 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if sieve[i]:
            j = (m * m - 3) // 2
            sieve[j] = 0
            while j < half:
                sieve[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [p for p in sieve if p]


def main():
    pairs = combinations(primes(2 * int(sqrt(1e7))), 2)
    minimum = (100, 0)
    for n, t in ((a * b, (a - 1) * (b - 1)) for a, b in pairs if a * b < 1e7):
        ratio = float(n) / t
        if ratio < minimum[0] and sorted(str(n)) == sorted(str(t)):
            minimum = (ratio, n)

    print(minimum[1])


if __name__ == "__main__":
    main()
