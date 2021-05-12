"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def sol():

    result = 0

    power = 1
    while power < 1000:
        num = 1

        t = len(str(num ** power))
        while t <= power:
            num += 1

            if t == power:
                result += 1

            t = len(str(num ** power))

        power += 1

    return result
