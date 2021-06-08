"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

 
(
131	673	
234
103
18
201
96
342
965	150	630	803	746	422	111	537	699	497	121	956	805	732	524	37	331 
)
Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

file_url = open("./p082_matrix.txt")
matrix = [list(map(int, row.split(","))) for row in file_url.readlines()]
n, m = len(matrix), len(matrix[0])
cost = [matrix[i][-1] for i in range(n)]

for i in range(m - 2, -1, -1):
    cost[0] += matrix[0][i]
    for j in range(1, n):
        cost[j] = min(cost[j], cost[j - 1]) + matrix[j][i]
    for j in range(n - 2, -1, -1):
        cost[j] = min(cost[j], cost[j + 1] + matrix[j][i])

print("Minimum path in", n, "by", m, "matrix =", min(cost))
