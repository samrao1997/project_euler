"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def next_num(num):
    if (num == 1): return 1

    if (num % 2 == 0):
        return num // 2
    else:
        return 3*num + 1

def steps_collatz(num):
    steps = 1
    while(num != 1):
        num = next_num(num)
        steps += 1
    return steps

# print(steps_collatz(13))


# This is very slow. Optimize! (with memory)
def solution(size):
    num = 1
    while (steps_collatz(num) < size):
        num += 1
    return num


# size = 1000000
# print(solution(size))

# idea keep memory that stores the size of previous calculated sequence then just add

# collatz_memo = {}


            


#time module for calculating execution time
import time

#time at the start of program execution
start = time.time()

num = 1
limit = 1000000
seq_list = []
while num < limit:
    sequence_num = 0
    n = num
    if n == 1:
        sequence_num = 1
    else:
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                sequence_num += 1
            else:
                n = 3 * n + 1
                sequence_num += 1

        sequence_num += 1
    seq_list.append(sequence_num)
    num += 1

k = seq_list.index(max(seq_list))
print(k + 1)

#time at the end of execution
end = time.time()

#printing the total time of execution
print(end-start)