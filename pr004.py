# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(number):
    number_as_str = str(number)
    n = len(number_as_str)
    mid = n // 2

    for i in range(0, mid):
        if  number_as_str[i] != number_as_str[n - i - 1]:
            return False

    return True


## print(check_palindrome(9009))

def solution():
    largest_pal = 0

    for i in range(999,99,-1):
        for j in range(i,99,-1):
            prod = i * j
            
            if prod <= largest_pal:
                break
            
            if check_palindrome(prod):
                largest_pal = prod
    
    return largest_pal

print(solution())


