"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
"""
import time


def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a


def findIntegerSidedRightAngleTriangles(max_length):
    numOfTriangles, rightTriangles = 0, [0] * (max_length + 1)

    for m in range(1, int(max_length ** 0.5)):
        for n in range(1, m):  # m > n
            # (m − n) odd and with m and n co-prime
            if (m - n) % 2 == 1 and 1 == gcd(m, n):
                a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
                length = a + b + c

                if a > b:
                    a, b = b, a  # a < b

                if length <= max_length and 1 == gcd(c, gcd(b, a)):
                    for s in range(length, max_length + 1, length):
                        rightTriangles[s] += 1

    numOfTriangles = len(
        [s for s in range(1, max_length + 1) if 1 == rightTriangles[s]]
    )
    return numOfTriangles


def main():
    start = time.process_time()

    assert 13 == findIntegerSidedRightAngleTriangles(120)

    L = 1500000
    print("For L <= %d," % L, findIntegerSidedRightAngleTriangles(L), end="")
    print(" exactly one integer sided right angle triangles can be formed.")

    end = time.process_time()

    print("CPU processing time :", end - start)


if __name__ == "__main__":
    main()
