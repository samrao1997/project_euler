"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import time
import math

start = time.time()


def truncate(n):
    lst = []
    n = str(n)
    for i in range(0, len(n)):
        lst.append(int(n[i:]))
        lst.append(int(n[: i + 1]))
    del lst[0]
    return lst


def check(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_list_prime(n):
    lst = truncate(n)
    for i in lst:
        if not check(i):
            return False
    return True


truncs = []
j = 11
while len(truncs) < 11:
    if is_list_prime(j):
        truncs.append(j)
        print(len(truncs))
    j += 1
    print(j)

print(truncs)
print(sum(truncs))
print(f"In {time.time() - start} seconds")
