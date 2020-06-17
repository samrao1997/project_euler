"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

import math

# This is basically the coefficients of the binomial aka 2n choose n

def nCr(n, r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 
  
# Driver code 
n = 5
r = 3
print(int(nCr(n, r)))

n = 40
r = 20
print(int(nCr(n, r)))