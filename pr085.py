"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""
# Project Euler Problem 85

from math import sqrt

L, x, min_diff = 2000000, 2, float("Inf")
y = L // 6

while x <= y:
    diff = abs(x * (x + 1) * y * (y + 1) // 4 - L)
    if diff < min_diff:
        area, min_diff, xx, yy = x * y, diff, x, y
    x += 2
    y = int(sqrt(L * 4 / (x * x + x)))

print("Area of grid:", xx, "x", yy, "=", area)
