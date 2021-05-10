"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""


def sieve_of_erat(n):
    primes = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:

        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

        p += 1

    result = []
    for i in range(len(primes)):
        if i in [0, 1]:
            continue

        if primes[i]:
            result.append(i)

    return result


def is_prime(num):
    num = int(num)

    if num == 1:
        return False

    if num == 2:
        return True

    value = int(num ** 0.5) + 1

    for i in range(2, value):
        if num % i == 0:
            return False

    return True


def prop(*args):
    lst = [i for i in args]

    for i in lst:
        for j in lst:
            if i == j:
                continue

            check1 = str(i) + str(j)
            check2 = str(j) + str(i)

            if (int(check1) not in primes) or (int(check2) not in primes):
                return False

    return True


def sol():

    min_sum = 0

    for a in primes:
        for b in primes:
            if b <= a:
                continue

            if prop(a, b):
                for c in primes:
                    if c <= b:
                        continue

                    if prop(a, b, c):
                        for d in primes:
                            if d <= c:
                                continue

                            if prop(a, b, c, d):
                                for e in primes:
                                    if e <= d:
                                        continue

                                    if prop(a, b, c, d, e):
                                        print("a: ", a)
                                        print("b: ", b)
                                        print("c: ", c)
                                        print("d: ", d)
                                        print("e: ", e)
                                        if sum([a, b, c, d, e]) < min_sum:
                                            min_sum = sum([a, b, c, d, e])
    return min_sum


# time, random, math modules
import time, random, math

# start of program
start = time.time()

# Sieve of Erotosthenes
# One of the best algorithm to generate prime numbers
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


# Miller–Rabin primality test
# One of the best algorithm to check if the given number if prime
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Algorithm: http://bit.ly/2drtk0x
def is_prime(n, k=3):
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        # A for loop with a random sample of numbers
        for a in random.sample(range(2, n - 2), k):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop


# A function to find all the combinations of the given two numbers
# and check if they are prime using the Rabin miller
def comb(a, b):
    len_a = math.floor(math.log10(a)) + 1
    len_b = math.floor(math.log10(b)) + 1
    if is_prime(int(a * (10 ** len_b) + b)) and is_prime(int(b * (10 ** len_a) + a)):
        return True
    return False


# finding out the primes upto 10000
primes = sieve(10000)

# problem solution
def prime_pairs():
    # a is first number
    for a in primes:
        # b is second number
        for b in primes:
            # check if b is less than a
            if b < a:
                continue
            # check if a and b satisfy the condition
            if comb(a, b):
                # c is the third number
                for c in primes:
                    # check if c is less than b
                    if c < b:
                        continue
                    # check if a,c and b, c satisfy the condition
                    if comb(a, c) and comb(b, c):
                        # d is the fourth number
                        for d in primes:
                            # check if d is less than c
                            if d < c:
                                continue
                            # check if (a,d), (b,d) and (c,d) satisfy the condition
                            if comb(a, d) and comb(b, d) and comb(c, d):
                                # e is the fifth prime
                                for e in primes:
                                    # check if e is less than d
                                    if e < d:
                                        continue
                                    # check if (a, e), (b, e), (c, e) and (d, e) satisfy condition
                                    if (
                                        comb(a, e)
                                        and comb(b, e)
                                        and comb(c, e)
                                        and comb(d, e)
                                    ):
                                        return a + b + c + d + e


# run the function and print the output
print(prime_pairs())

# end of program
end = time.time()

# total time for program execution
print(end - start)