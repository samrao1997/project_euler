"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

c = ""

for i in range(1, 1000005):
    c += str(i)


def sol():
    return (
        int(c[0])
        * int(c[9])
        * int(c[99])
        * int(c[999])
        * int(c[9999])
        * int(c[99999])
        * int(c[999999])
    )


print(sol())
