#Project Euler Problem 115

L, m, ways = 1000000, 50, [1]

while ways[-1] < L:
    ways += [sum(ways[:-m]) + ways[-1]]

print ("Fixed block size:", m, "units")
print (len(ways)-2, "minimum units to first exceed", L, "combinations.")