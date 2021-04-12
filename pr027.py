def is_prime(num):
    if num > 0:
        num = -1 * num

    if num == 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def count_primes(a, b):
    n = 0
    t = n * n + a * n + b
    while is_prime(t):
        t = n * n + a * n + b
        n += 1
    print(f"When a is ${a} and b is ${b} it can produce ${n} number of primes")
    return n


def sol():
    max_a = 0
    max_b = 0
    max_n = 0

    for a in range(-1001, 1000):
        for b in range(-1001, 1000):
            n = count_primes(a, b)
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b
    return (max_a, max_b)


# time module for calculating execution time
import time

# time at the start of execution
start = time.time()

# sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# used from problem 7 solution
# http://bit.ly/24bPJV6
def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5 + 1)):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = []
    for i in range(n):
        if is_prime[i] == True:
            prime.append(i)
    return prime


def is_prime(n):
    """function to check if the number
    is prime or not"""
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# primes below 1000
primes1000 = sieve(1000)

# copy of primes1000 variable
primes = primes1000[:]

# assume the largest value is 0 at start
largest = 0

# looping through a quadratic equation
for b in primes1000:
    for a in primes1000:
        i = 0
        # positive a and b
        while True:
            quadratic = i ** 2 + a * i + b
            if quadratic not in primes:
                if is_prime(quadratic):
                    primes.append(quadratic)
                else:
                    if i - 1 > largest:
                        largest = i - 1
                        axb = a * b
                    break
            i += 1
        i = 0
        # negative a and positive b
        while True:
            quadratic = i ** 2 - a * i + b
            if quadratic not in primes:
                if is_prime(quadratic) and quadratic > 0:
                    primes.append(quadratic)
                else:
                    if i - 1 > largest:
                        largest = i - 1
                        axb = -1 * a * b
                    break
            i += 1

# printing the largest value of a*b
print(axb)

# printing the total time of execution
print(time.time() - start)