"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sum_primes(n):
    """
    This returns a list of the prime numbers less than n
    """

    if n == 1: return 0

    total = 0

    for i in range(2,n+1):
        if (is_prime(i)):
            total += i

    return total


def is_prime(num):
    if (num == 1):
        return False

    if (num == 2):
        return True

    if (num % 2 == 0):
        return False


    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            return False
    return True

n = 2000000
print(sum_primes(n))