"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""
# list of generalized pentagonal numbers for generating function
k = sum([[i * (3 * i - 1) / 2, i * (3 * i - 1) / 2 + i] for i in range(1, 250)], [])

p, sgn, n, m = [1], [1, 1, -1, -1], 0, 1e6

while p[n] > 0:  # expand generating function to calculate p(n)
    n += 1
    px, i = 0, 0
    while k[i] <= n:
        px += p[int(n - k[i])] * sgn[i % 4]
        i += 1
    p.append(px % m)

print("Project Euler 78 Solution =", n)