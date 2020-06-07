"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                   a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

## maybe find a multiple of 3,4,5 such that they add up to 1000?
# so 
# c(3+4+5) = 1000 => c(12) = 1000
# NOPE DOES NOT WORK

def check_py_trip(a,b,c):
    return a**2 + b**2 == c**2

def find_py_trip_sum(n):
    """
    return pythagorean triplet that adds up to n
    """
    
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                if (check_py_trip(a,b,c) and (a+b+c == n)):
                    return (a,b,c)
    return False

n = 1000
a,b,c = find_py_trip_sum(n)
print(a,b,c)
prod = a * b * c
print(prod)