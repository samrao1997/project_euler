L, q, s = 100000, pow(10, 20), 2+3

def sieve(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5 + 1)):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = []
    for i in range(n):
        if is_prime[i] == True:
            prime.append(i)
    return prime


def is_prime(n):
    """function to check if the number
    is prime or not"""
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

s += sum(p for p in sieve(L)[2:] if pow(10, q, p) != 1)
 
print("Project Euler 133 Solution = ", s)