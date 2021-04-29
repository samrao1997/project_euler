"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""


def pent_n(num):
    return (num * (3 * num - 1)) / 2


import math


def is_pent(num):
    r = math.sqrt(1 + 24 * num)
    return r % 6 == 5


def sol():
    nums = [1, 5, 12]

    Pn = 22
    n = 10

    while True:
        nums.append(Pn)

        for i in range(len(nums)):
            a = Pn - nums[i]
            b = nums[i]

            if is_pent(a) and is_pent(abs(a - b)):
                print(abs(a - b))
                return

        n += 3
        Pn += n
