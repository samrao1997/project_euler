# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.



def fast_fib_sum_even(n):
    memo = [None] * n
    memo[0] = 1
    memo[1] = 2
    total = 2


    for i in range(2,n):
        memo[i] = memo[i-1] + memo[i-2]
        if (memo[i] % 2 == 0):
            total += memo[i]

    print("the nth fib number is: ", memo[n-1])
    if (memo[n-1] < 4000000):
        total = fast_fib_sum_even(n+1)
    return total



print(fast_fib_sum_even(20))

