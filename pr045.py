"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
import math


def is_tri(num):
    r = math.sqrt(8 * num + 1)
    return r == int(r)


def is_pent(num):
    r = math.sqrt(1 + 24 * num)
    return r % 6 == 5


def is_hex(num):
    # notice if hex number then is tri number
    r = math.sqrt(8 * num + 1)
    return (r + 1) % 4 == 0


def sol():
    m = 144
    while True:
        res = 2 * m * m - m
        if is_pent(res):
            return res
        m += 1
