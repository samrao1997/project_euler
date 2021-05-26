"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""
import math


def factorial_digits(num):
    value = 0
    num_str = str(num)
    for digit in num_str:
        value += math.factorial(int(digit))
    return value


def check_fact_prop(num):
    previous_num = []

    while num not in previous_num:
        previous_num.append(num)

        num = factorial_digits(num)
    return len(previous_num)


def sol():
    result = 0

    for i in range(1000000):
        if check_fact_prop(i) == 60:
            print(f"{i} produces a 60 chain")
            result += 1

    return result