"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

import time


start_time = time.time()


with open("p067_triangle.txt") as f:
    # All the numbers in the file
    number = f.read()


number = number.strip().split("\n")


for i in range(len(number)):
    number[i] = number[i].strip().split(" ")
    number[i] = [int(i) for i in number[i]]


number[0] = [59]


counter = 0


for i in range(len(number) - 2, -1, -1):
    for j in range(len(number[i])):
        number[i][j] = number[i][j] + max(number[i + 1][j], number[i + 1][j + 1])
        counter += 1
    number.pop()


print(f"Found {number[0][0]} in {counter} iterations")

end_time = time.time()

print(f"took {end_time - start_time}")
