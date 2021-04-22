"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import math


def check_pali(num):
    num_str = str(num)

    if num_str == num_str[::-1]:
        return True

    return False


def sol():
    result = 0
    for i in range(1000000):
        if check_pali(i) and check_pali(int(bin(i)[2:])):
            result += i

    return result


print(sol())