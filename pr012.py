"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

# triangle numbers are essentially numbers that can be expressed as n*(n+1)/2
# we are looking for the value of n s.t. n*(n+1)/2 has > 500 divisors


# This is very slow there must be a better way to solve this!
def solve(num_div):
    divisors = []
    i = 1
    while (len(divisors) < num_div):
        divisors = []
        tri_num = (i * (i+1)) // 2
        print(tri_num)
        for j in range(1, tri_num + 1):
            if tri_num % j == 0:
                divisors.append(j)
        i += 1

    return tri_num

# num_div = 500
# print(solve(num_div))

# Prime factorization then use the number of combinations to combined the primes is the total number of divisors


def num_divisor(num):
    n = num
    i = 2
    p = 1

    if (num == 1): return 1

    while (i * i <= n):
        c = 1
        while (n % i == 0):
            n /= i
            c += 1
        i += 1
        p *= c

    if (n == num or n > 1):
        p *= 1 + 1
    
    return p

def sol(x):
    n = 1
    d = 1

    while (num_divisor(d) <= x):
        n += 1
        d += n
    
    return d

x = 500
print(sol(500))

