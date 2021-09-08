L, sqrt_5, f = 30, 5**0.5, [7, 14, 50, 97]

for i in range(L-4):
    f.append(7*f[-2] - f[-4])

print("Sum of the first", L, "golden nuggets:", )
print(sum(int(x/sqrt_5) - 1 for x in f))