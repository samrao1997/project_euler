"""

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

"""
Idea: Given date return back day of the week. 

result = 0
while 1901 != 2000
    for month in months:
        if day_of_week(first of month, year) == 'sunday':
            result += 1
    year += 1
return result
        

"""
import math


def zeller_cong(day, month, year):
    K = year % 100
    J = math.floor(year / 100)

    return (
        day
        + math.floor((13 * (month + 1)) / 5)
        + K
        + math.floor(K / 4)
        + math.floor(J / 4)
        - 2 * J
    ) % 7


def sol():
    n = 0
    dow = 2
    months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1901

    while year != 2001:

        months[1] = 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

        for month in months:
            dow += month % 7
            if dow % 7 == 0:
                n += 1

        year += 1
    return n
