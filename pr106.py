import math


def binomial(n, k):
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def compute():
	SET_SIZE = 12
	
	def catalan(n):
		return binomial(n * 2, n) // (n + 1)
	
	ans = sum(binomial(SET_SIZE, i * 2) * (binomial(i * 2, i) // 2 - catalan(i))
		for i in range(2, SET_SIZE // 2 + 1))
	return str(ans)


if __name__ == "__main__":
	print(compute())