"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

# stores all amicable nums

list_amicable_nums = []


def amicable_check(num):
    # if we already stored it in list
    if num in list_amicable_nums:
        return True

    divisors_num = get_divisors(num)
    amicable_pair = sum(divisors_num)
    divisors_pair = get_divisors(amicable_pair)

    if num == sum(divisors_pair):
        list_amicable_nums.extend([num, amicable_pair])
        return True
    return False


def get_divisors(num):
    # gets divisors of nums
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def sol():
    for i in range(1, 10000):
        amicable_check(i)
    return sum(list_amicable_nums)


print(sol())
