"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import getcontext, Decimal

getcontext().prec = 102
L, d, s = 100, 100, 0
p = pow(10, d - 1)

for z in range(2, L):
    q = Decimal(z).sqrt()
    s += sum(int(c) for c in str(q * p)[:d]) if q % 1 != 0 else 0

print("Project Euler 80 Solution =", s)