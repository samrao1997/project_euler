

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
  
n = 50000000
result = 2
primes = sieve(n)

i = 1
while i < len(primes):
    if primes[i] < n / 4:
        result+=1
    
    if primes[i] < n / 16:
        result+=1
    
    if ((primes[i] - 3) % 4 == 0):
        result+=1
    
    
    i += 1
print(result)