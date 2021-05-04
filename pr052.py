"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


# Brute force
def sol():
    num = 1
    while not prop(num):
        num += 1
    return num


def prop(num):
    digit_set = set(str(num))

    for i in range(2, 7):

        if digit_set != set(str(i * num)):
            return False

    return True