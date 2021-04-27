"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import math


def is_N_pandigital(num):
    digits = "123456789"

    num_str = str(num)

    for digit in digits:
        if digit not in num_str:
            return int(digit) - 1
    return 9


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
    max_value = 0
    max_n_digital = 0
    for i in range(1234, 7654321):
        if len(str(i)) not in [4, 7]:
            continue

        if is_prime(i):
            n = is_N_pandigital(i)
            if n >= max_n_digital and i > max_value:
                print(f"{i} : {n} ")
                max_value = i
                max_n_digital = n
    return (max_value, max_n_digital)


print(sol())