"""

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def count(arr, m, n):

    # sum is 0
    if n == 0:
        return 1

    # sum is less than 0
    if n < 0:
        return 0

    # we have no more numbers left but sum is above 0
    if m <= 0 and n >= 1:
        return 0

    # adds the sum of two set the set that used mth coin and the set that doesn't use the mth coin
    return count(arr, m - 1, n) + count(arr, m, n - arr[m - 1])


arr = [1, 2, 5, 10, 20, 50, 100, 200]
m = len(arr)
n = 200

print(count(arr, m, n))
