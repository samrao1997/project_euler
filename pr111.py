
import math

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


def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True

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



def compute():
	DIGITS = 10
	
	primes = list_primes(sqrt(10**DIGITS))
	
	# Only valid if 1 < n <= 10^DIGITS.
	def is_prime(n):
		end = sqrt(n)
		for p in primes:
			if p > end:
				break
			if n % p == 0:
				return False
		return True
	
	
	ans = 0
	# For each repeating digit
	for digit in range(10):
		
		# Search by the number of repetitions in decreasing order
		for rep in range(DIGITS, -1, -1):
			sum = 0
			digits = [0] * DIGITS
			
			# Try all possibilities for filling the non-repeating digits
			for i in range(9**(DIGITS - rep)):
				
				# Build initial array. For example, if DIGITS=7, digit=5, rep=4, i=123, then the array will be filled with 5,5,5,5,1,4,7.
				for j in range(rep):
					digits[j] = digit
				temp = i
				for j in range(DIGITS - rep):
					d = temp % 9
					if d >= digit:  # Skip the repeating digit
						d += 1
					if j > 0 and d > digits[DIGITS - j]:  # If this is true, then after sorting, the array will be in an already-tried configuration
						break
					digits[-1 - j] = d
					temp //= 9
				
				else:
					digits.sort()  # Start at lowest permutation
				
					while True:  # Go through all permutations
						if digits[0] > 0:  # Skip if the number has a leading zero, which means it has less than DIGIT digits
							num = int("".join(map(str, digits)))
							if is_prime(num):
								sum += num
						if not next_permutation(digits):
							break
			
			if sum > 0:  # Primes found; skip all lesser repetitions
				ans += sum
				break
	
	return str(ans)


if __name__ == "__main__":
	print(compute())
    