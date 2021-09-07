#Project Euler Problem 139

L = 100000000
x, y, c = 1, 1, 0

while (x + y) < L:
    x, y = 3*x + 4*y, 2*x + 3*y
    c += (L-1) // (x+y)

print("Pythagorean triangles for tiling \na perimeter <",L, "=", c)