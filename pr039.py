"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

a^2 + b ^2 = c^2  and a + b + c = p while p <= 1000


"""


def sol(n):
    max = 0
    maxp = 0

    p = 2
    while p <= n:
        c = 0
        a = 2

        while a < p / 3:
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                c += 1

            if c > max:
                max = c
                maxp = p

            a += 1

        p += 2
    return maxp


print(sol(1000))
