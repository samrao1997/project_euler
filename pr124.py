L, k = 100000, 10000

E = [[1,_] for _ in range(L+1)]

for i in range(2, L+1):
    if E[i][0] == 1:
        for j in range(i, L+1, i):
           E[j][0] *= i

print("kth element in sorted list of radicals", sorted(E)[k][1])