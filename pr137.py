L=15

f1, f2 = 1, 1
for i in range(2*L - 1):
    f1, f2 = f2, f1+f2

print("The", L, "golden nugget =", f1*f2)