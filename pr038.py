"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(num):
    digits = "123456789"

    num_str = str(num)

    for digit in digits:
        if digit not in num_str:
            return False
    return True


def concat_multiply(num, arr):
    result = ""

    for value in arr:
        result += str(num * value)

    return int(result)


def sol():
    max = 0

    x = 9487

    while x >= 9234:
        res = 100002 * x

        if is_pandigital(res):
            if res > max:
                max = res

        x -= 1
    return max


print(sol())
