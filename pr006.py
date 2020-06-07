## The sum of the squares of the first ten natural numbers is,

## 12+22+...+102=385
## The square of the sum of the first ten natural numbers is,

## (1+2+...+10)2=552=3025
## Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# We can use the geometric sum as well as guasses equations for sum of first n numbers squared


def diff(n):
    """
        n is the number that you want to calculate up to
    """

    square_of_sum = ((n * (n + 1))/2) ** 2
    sum_of_square = (n * (n+1) * (2*n+1)) / 6

    return square_of_sum - sum_of_square

print(diff(100))
