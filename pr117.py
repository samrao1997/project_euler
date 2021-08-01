#Project Euler Problem 117: Tetranacci numbers

a, b, c, d, n = 0, 0, 0, 1, int(input('Units in row?'))
for _ in range(n):
	a, b, c, d = b, c, d, (a+b+c+d)

print("Number of way to be tiled is", d)