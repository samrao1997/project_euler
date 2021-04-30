"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


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


def gen_perms(num):
    num_str = str(num)

    if len(num_str) == 0:
        return []

    if len(num_str) == 1:
        return [num_str]

    l = []

    for i in range(len(num_str)):
        ele = num_str[i]

        remaining = num_str[:i] + num_str[i + 1 :]

        for p in gen_perms(remaining):
            l.append(ele + p)

    return l


# given length and list of digits return all permuations of length n composed of those digits
def gen_comb(list_digits, n):

    if n == 0:
        return [""]

    l = []

    for i in range(0, len(list_digits)):

        m = str(list_digits[i])
        rmlst = list_digits[i + 1 :]

        for p in gen_comb(rmlst, n - 1):
            l.append(m + p)
    return l


def n_length_combo(lst, n):

    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1 :]

        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)

    return l


def check_sub_arithm(lst, l):
    all_sub = n_length_combo(lst, l)

    for seq in all_sub:
        seq = [int(i) for i in seq]
        seq = sorted(seq)

        value = seq[1] - seq[0]
        flag = True
        for i in range(2, len(seq)):
            if seq[i] - seq[i - 1] != value:
                flag = False

        if flag:
            return seq


def sol():
    digs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = 4

    combs = gen_comb(digs, l)
    perms = [gen_perms(i) for i in combs]

    for lst in perms:
        numbers = []
        num_primes = 0
        for value in lst:
            if is_prime(value):
                num_primes += 1
                numbers.append(value)
        if num_primes >= l and (t := check_sub_arithm(numbers, l)) != None:
            return t


# time module
import time

# importing permutations
from itertools import permutations

# time at the start of program execution
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


# create the number
def create(b):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i]) + str(b[j]) + str(b[j] + difference)
    return False


# sieving prime numbers less than 10000
primes = sieve(10000)

# primes greater than 1487
primes = [x for x in primes if x > 1487]

# for loop
for i in primes:
    p = permutations(str(i))
    a = [int("".join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print(create(a))
            break

# time at the end of program execution
end = time.time()

# total time for execution
print(end - start)
