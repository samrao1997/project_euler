"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


def generate_perm(num):
    num_str = str(num)

    if len(num_str) == 0:
        return []

    if len(num_str) == 1:
        return [num_str]

    l = []

    for i in range(len(num_str)):
        ele = num_str[i]

        remain_lst = num_str[:i] + num_str[i + 1 :]

        for p in generate_perm(remain_lst):
            l.append(ele + p)
    return l


def check_prop(num):
    num_str = str(num)

    if int(num_str[1] + num_str[2] + num_str[3]) % 2 != 0:
        return False

    if int(num_str[2] + num_str[3] + num_str[4]) % 3 != 0:
        return False

    if int(num_str[3] + num_str[4] + num_str[5]) % 5 != 0:
        return False

    if int(num_str[4] + num_str[5] + num_str[6]) % 7 != 0:
        return False

    if int(num_str[5] + num_str[6] + num_str[7]) % 11 != 0:
        return False

    if int(num_str[6] + num_str[7] + num_str[8]) % 13 != 0:
        return False

    if int(num_str[7] + num_str[8] + num_str[9]) % 17 != 0:
        return False

    return True


def sol():
    total = 0

    for p in generate_perm("0123456789"):
        if check_prop(p):
            total += int(p)
    return total
