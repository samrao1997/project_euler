from math import sqrt

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True

def gcd(a, b):
    """
    Compute the greatest common divisor of a and b. Examples:
    
    >>> gcd(14, 15)    #co-prime
    1
    >>> gcd(5*5, 3*5)
    5
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a

def A(n):
  if is_prime(n) or gcd(n, 10) != 1: return None
  x, k = 1, 1
  while x != 0:
    x = (x*10 + 1) % n
    k += 1
  return k

L = 1000001
n = L
while A(n) == None or A(n) < L: n += 2

print("Project Euler 129 Solution =", n)
    
    