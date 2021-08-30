def compute():
    LIMIT = 10**6
    solutions = [0] * LIMIT
    for m in range(1, LIMIT * 2):
        for k in range(m // 5 + 1, (m + 1) // 2):
            temp = (m - k) * (k * 5 - m)
            if temp >= LIMIT:
                break
            solutions[temp] += 1
    ans = solutions.count(10)
    return str(ans)

if __name__ == "__main__":
    print(compute())