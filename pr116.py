#Project Euler Problem 116

n = 50
def F(m, n):
    ways = [1] * m + [0] * (n-m+1)
    for j in range(m, n+1):
        ways[j] += ways[j - 1] + ways[j - m]
    return ways[n] - 1

print("Space size =", n, "units")
print("Number of ways to fill:", F(2, n) + F(3, n) + F(4, n))