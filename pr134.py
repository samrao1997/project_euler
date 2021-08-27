import itertools

# Given integer x, this returns the integer floor(sqrt(x)).
def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y

# Tests whether the given integer is a prime number.
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True


# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.
def list_primality(n):
	# Sieve of Eratosthenes
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


# Returns all the prime numbers less than or equal to n, in ascending order.
# For example: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].
def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

# Returns x^-1 mod m. Note that x * x^-1 mod m = x^-1 * x mod m = 1.
def reciprocal_mod(x, m):
	assert 0 <= x < m
	
	# Based on a simplification of the extended Euclidean algorithm
	y = x
	x = m
	a = 0
	b = 1
	while y != 0:
		a, b = b, a - x // y * b
		x, y = y, x % y
	if x == 1:
		return a % m
	else:
		raise ValueError("Reciprocal does not exist")

def compute():
	ans = 0
	primes = list_primes(2000000)
	for i in itertools.count(2):
		p = primes[i]
		q = primes[i + 1]
		if p > 1000000:
			break
		k = 1
		while k < p:
			k *= 10
		m = (q - p) * reciprocal_mod(k % q, q) % q
		ans += m * k + p
	return str(ans)


if __name__ == "__main__":
	print(compute())