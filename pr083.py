"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

 
(
131
673	
234
103
18
201
96
342
965	
150
630	803	746	
422
111
537	699	497	
121
956	805	732	524	
37
331
 
)
Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""
import networkx as nx

file_url = open("./p082_matrix.txt")
matrix = [list(map(int, row.split(","))) for row in file_url.readlines()]
n, m = len(matrix), len(matrix[0])

s = [(-1, 0), (0, -1), (1, 0), (0, 1)]

G = nx.DiGraph()
for i in range(n):
    for j in range(m):
        neighbors = [
            (i + x, j + y) for x, y in s if (0 <= i + x < n) and (0 <= j + y < m)
        ]
        for ix, jy in neighbors:
            G.add_edge((i, j), (ix, jy), weight=matrix[ix][jy])

path_length = nx.dijkstra_path_length(G, source=(0, 0), target=(n - 1, m - 1))

print("Minimum path sum in", n, "by", m, "matrix =", path_length + matrix[0][0])