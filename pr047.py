"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""


def is_prime(num):
    if num == 1:
        return False

    if num == 2:
        return False

    value = int(num ** 0.5) + 1

    for i in range(2, value):
        if num % i == 0:
            return False

    return True


def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number ** 0.5 or number == 1:
        if number % i == 0:
            number = number / i
            a.add(i)
            i -= 1
        i += 1
    return len(a) + 1


def sol(t):
    num_com = t
    a = []
    i = 2
    while len(a) != num_com:
        if npf(i) == num_com:
            if len(a) != 0 and i - a[-1] != 1:
                a = []

            a.append(i)

        i += 1
    return a
