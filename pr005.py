## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 

# This reduces to finding the least common multiple.

def least_common_mult(arr):
    m = max(arr)
    p = list_primes(m)

    N = 1

    for i in range(len(p)):
        mult = p[i]
        # print(mult)
        # print(N)
        while (mult * p[i] < m):
            mult = mult * p[i]
        # print(mult)
        N = N * mult
        # print(N)

    
    return N


def list_primes(n):
    """
    This returns a list of the prime numbers less than n
    """

    if n == 1: return []

    arr = []

    for i in range(2,n+1):
        if (is_prime(i)):
            arr.append(i)

    return arr


def is_prime(num):
    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            return False
    return True


test = range(1,11)
print(least_common_mult(test))
