from itertools import permutations, combinations, chain


def find_primes_less_than(n):
    not_p = set()
    primes = []
    for i in range(2, n):
        if i not in not_p:
            primes.append(i)
            for j in range(i * 2, n, i):
                not_p.add(j)
    return primes
 
primes = find_primes_less_than(32000)
 
def is_prime(n):
    if n == 1:
        return False
    limit = int(n ** 0.5)
    for p in primes:
        if p > limit:
            return True
        if n % p == 0:
            return False
    return True
 
len_key = {}
len_dig_key = {}
 
def generator(length, used, prev_p):
    if length == 9:
        return []
    complete_set = len_key[length].copy()
    for i in used:
        complete_set -= len_dig_key[length][i]
    return filter(lambda x: x > prev_p, complete_set)   
 
def solver(min_l, used=set(), prev_p=0):
    accum = 9 - len(used)
    result = sum(1 for i in generator(accum, used, prev_p))
    for l in range(min_l, accum // 2 + 1):
        for p in generator(l, used, prev_p):
            new_used = used | set(map(int, str(p)))
            result += solver(l, new_used, p)
    return result
 
def populate_dicts():
 
    def filt_func(i):
        if len(i) == 1:
            return True
        if i[-1] & 1 == 0 or i[-1] == 5:
            return False
        return True
 
    for i in range(1, 9):
        len_key[i] = set()
        temp = {}
        for dig in range(1, 10):
            temp[dig] = set()
        comb = (c for c in combinations(range(1, 10), i) if sum(c) % 3 > 0)
        permut = filter(filt_func, 
                        chain.from_iterable(permutations(c, i) for c in comb)
                        )
        for perm in permut:
            p = int(''.join(map(str, perm)))
            if not is_prime(p):
                continue
            len_key[i].add(p)
            for dig in perm:
                temp[dig].add(p)
        len_dig_key[i] = temp
    len_key[1].add(3)
    len_dig_key[1][3].add(3)
 
if __name__ == '__main__':
    populate_dicts()
    result = solver(1)
    print("The result is:", result)