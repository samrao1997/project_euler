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

s = set()
n, L = 5, 10**9

while len(s) < 40:
    if is_prime(n) and pow(10, L, n) == 1: s.add(n)
    n += 2

print("Project Euler 132 Solution =", sum(s))