#Project Euler Problem 100

b, n, L = 3, 4, 10**12
while n <= L:
    b, n = 3*b + 2*n - 2, 4*b + 3*n - 3

print("Total disks =", L)
print("Number of Blue disks, number of total disks =", b, n)