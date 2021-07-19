def return_factors(factors_of_input_val):
    num_factors = 1
    for tuple in factors_of_input_val:
        num_factors *= (2*tuple[-1] + 1) # iterate over the tuple & grab the exponent of si
        # the math is d(n) = (s1 + 1)*(s2 + 1)* ... *(sn + 1) where d(n) returns the count of divisors
        # D(n^2) + 1 = (2s1 + 1)*(2s2 + 1)* ... *(2sn + 1)
    return num_factors/2 - 1 # divide by 2 and subtract 1 to get number of unique solutions


def prime_product(factors_of_input_val):
    prime_product = 1
    for tuple in factors_of_input_val:
        prime_product *= (tuple[0]**tuple[1]) # iterate over the tuple & return prime product
    return prime_product

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
exponents = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

prime_tuples = zip(primes, exponents)

print("Answer n =", prime_product(prime_tuples), "has", return_factors(prime_tuples), "unique factors")