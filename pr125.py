

def is_palindromic(n): n=str(n); return n==n[::-1]

def pe125(L):
   pal = set()
   sqrt_L = int(L ** 0.5)
   for i in range(1, sqrt_L):
      sos = i*i
      while sos < L:
         i += 1
         sos += i*i
         if is_palindromic(sos): 
            pal.add(sos)
   return sum(pal)

print("PE125: Sum of unique palindromes:", pe125(10**8))