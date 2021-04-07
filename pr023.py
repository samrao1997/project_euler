"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

list_of_abundant_nums = {}


def get_divisors(num):
    # gets divisors of nums
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def check_abundant_num(num):
    if num in list_of_abundant_nums.keys() and list_of_abundant_nums[num]:
        return True

    elif num in list_of_abundant_nums.keys() and not list_of_abundant_nums[num]:
        return False

    elif sum(get_divisors(num)) > num:
        list_of_abundant_nums[num] = True
        return True

    else:
        list_of_abundant_nums[num] = False
        return False


def check_if_sum_of_two_abundant_nums(num):
    for i in range(1, num + 1):
        check_abundant_num(i)

    for abun_num in list_of_abundant_nums:
        if num - abun_num in list_of_abundant_nums:
            return True
    return False


def sol():
    total = 0
    for i in range(30000, 1, -1):
        print("i: ", i)
        if not check_if_sum_of_two_abundant_nums(i):
            print(i, " is a sum of two abundant nums.")
            print("total before add: ", total)
            total += i
            print("total after add: ", total)

    return total


# def is_abundant(n):
#     max_divisor = int(n / 2) + 1
#     sum = 0
#     for x in range(1, max_divisor):
#         if n % x == 0:
#             sum += x
#     return sum > n


# abundants = list(x for x in range(1, 28123) if is_abundant(x))

# sums = 0
# for i in range(12, 28123):
#     for abundant in abundants:
#         if abundant >= i and is_abundant(i + abundant):
#             sums += i
# print(sums)

import math


def divisors(n):
    """
    Returns all nontrivial divisors of an integer, but makes no guarantees on the order.
    """
    # "1" is always a divisor (at least for our purposes)
    yield 1

    largest = int(math.sqrt(n))

    # special-case square numbers to avoid yielding the same divisor twice
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i


def is_abundant(n):
    if n < 12:
        return False
    return sum(divisors(n)) > n


abundants = [x for x in range(1, 28123 + 1) if is_abundant(x)]
abundants_set = set(abundants)


def is_abundant_sum(n):
    for i in abundants:
        if i > n:  # assume "abundants" is ordered
            return False
        if (n - i) in abundants_set:
            return True
    return False


sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))
print(sum_of_non_abundants)