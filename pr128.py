import itertools

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

def compute():
	TARGET = 2000  # Must be at least 3
	count = 2  # Because n = 1 and 2 satisfy PD(n) = 3
	for ring in itertools.count(2):
		if all(map(is_prime, (ring * 6 - 1, ring * 6 + 1, ring * 12 + 5))):
			count += 1
			if count == TARGET:
				return str(ring * (ring - 1) * 3 + 2)
		if all(map(is_prime, (ring * 6 - 1, ring * 6 + 5, ring * 12 - 7))):
			count += 1
			if count == TARGET:
				return str(ring * (ring + 1) * 3 + 1)


if __name__ == "__main__":
	print(compute())