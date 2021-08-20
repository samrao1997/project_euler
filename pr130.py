
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



dnp = set()    # set of deceptive non-primes
L = 25
n = 91    # start with first valid n given in the problem description

while len(dnp) < L:
    if not is_prime(n) and pow(10, n-1, 9*n) == 1:
        dnp.add(n)
    n += 2

print("Project Euler 130 Solution =", sum(dnp))