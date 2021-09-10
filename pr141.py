
"""Solution for problem 141."""
def gcd(a, b):
    """Computes gcd for 2 numbers."""
    while b:
        a, b = b, a % b
    return a


import itertools
import math
# m^2 = n = d*q + r with 0 <= r < d
# Values can ke written c, c*k, c*k*k with k > 0 (values are all positive)
# We can assume k > 1 (or we take 1/k)
# We have different possible orders :
# d, q, r and q, d, r are not possible because r < d
# d, r, q and q, r, d are not possible because it leads to r*r = q*d which means n = r*(r+1), not a square
# r, q, d and r, d, q are somewhat symetric cases as q and d have similar roles
# Consecutives terms will be : r, rk, rkk
# k is rational because a and a*k are both integers
# k can be expressed in an irreductible form k = a/b with a > b > 0 and gcd(a, b) == 1
# Consecutives terms will be : r, r*a/b, r*a^2/b^2
# Because all terms (especially the last one) are integers, we must have b^2 dividing r
# So r = c*b*b and other terms are a*b*c and a*a*c
# And we have :
# m^2 = n = dq + r = a^3*b*c^2 + b^2*c
sol = set()
lim=10 ** 12
for a in itertools.count(2):
    a3 = a * a * a
    if a3 >= lim:
        break
    for b in range(1, a):
        b2 = b * b
        if a3 * b + b2 >= lim:
            break
        if gcd(a, b) == 1:
            for c in itertools.count(1):
                n = a3 * b * c * c + b2 * c
                if n >= lim:
                    break
                sqrt = int(math.sqrt(n))
                if sqrt * sqrt == n:
                    sol.add(n)
print(sum(sol))