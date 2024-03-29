"""

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""


def sol(num):
    fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = ""

    num -= 1
    for i in range(len(arr) - 1, -1, -1):
        t = int(num // fac[i]) or 0
        print(t)
        num %= fac[i]
        result += str(arr[t])
        arr.remove(arr[t])
    return result


print(sol(1e6))