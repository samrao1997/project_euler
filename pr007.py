"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

# we can use previous problems code to list the first 10001 primes then select this but this probably coud be optimized using other algorithms


## TO IMPLEMENT:
##      -- 1 is not prime DONE
##      -- All primes except 2 are odd DONE
##      -- All primes greater than 3 can be written in the form 6k +- 1
##      -- Any nuber n can have only one primmefactor greather than sqrt(n)

def n_prime(n):
    """
    This returns the nth prime number
    """

    if n <= 0: return 0

    arr = []
    i = 2
    while (len(arr) != n):
        if (is_prime(i)):
            arr.append(i)
        i += 1

    return arr[-1]




def is_prime(num):
    if (num == 1):
        return False

    if (num == 2):
        return True

    if (num % 2 == 0):
        return False


    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            return False
    return True

test1 = 6
print(n_prime(6))
test2 = 10001
print(n_prime(test2))