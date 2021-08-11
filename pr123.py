def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


prime = [0] + prime_sieve(345000)    # base prime number array from one

L, n = 10**10, 1
while 2*n*prime[n] < L: n+= 2

print("First n for remainder to exceed limit:", n)