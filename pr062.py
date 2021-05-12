"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def gen_perms(num):
    num_str = str(num)

    if len(num_str) == 0:
        return []

    if len(num_str) == 1:
        return [num_str]

    l = []

    for i in range(len(num_str)):
        ele = num_str[i]

        remaining = num_str[:i] + num_str[i + 1 :]

        for p in gen_perms(remaining):
            l.append(ele + p)

    return l


def sol():
    number = 5

    cubes = set()

    check_num = 1

    while True:
        value = check_num ** 3

        cubes.add(str(value))

        l = cubes.intersection(set(gen_perms(value)))
        if len(l) >= number:
            return l

        check_num += 1


# import time
import time

# time at the start of program
start = time.time()

# list to store cubes
cubes = []

# iterator
i = 0

# while loop
while True:
    # cube of the number
    cube = sorted(list(str(i ** 3)))
    # appending the cube to cubes list
    cubes.append(cube)
    # check if it occured 5 times
    if cubes.count(cube) == 5:
        # print the cube of the smallest such cube
        print((cubes.index(cube)) ** 3)
        break
    i += 1

# time at the end of program
end = time.time()

# total time taken
print(end - start)


# import pdb

# pdb.set_trace()
# sol()
