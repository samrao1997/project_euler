"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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


def sol():
    n = 9
    while True:
        # skips prime odd number so just composite nums
        if is_prime(n):
            n += 2
            continue

        # if one of the n - 2 * k ^ 2 is prime then skip this n
        # However if all numbers of that form are not prime then we know that
        # that n cannot be the sum of a prime and twice a
        flag = False
        for k in range(1, math.floor(math.sqrt(n))):
            t = n - (2 * (k ** 2))

            if t <= 0:
                continue

            if is_prime(t):
                n += 2
                flag = True
                break

        if flag:
            continue

        return n


print(sol())
