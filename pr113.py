def is_bouncy(n):
  inc, dec, s = False, False, str(n)
  for i in range(len(s)-1):
    if s[i+1] > s[i]: inc = True
    elif s[i+1] < s[i]: dec = True
    if inc and dec: return True
  return False

def binomial(n, k):
    """
    Calculate C(n,k), the number of ways can k be chosen from n. Example:
    
    >>>binomial(30,12)
    86493225
    """
    nt = 1
    for t in range(min(k, n-k)):
        nt = nt * (n-t) // (t+1)
    return nt

n = 100
print(binomial(n+10, n) + binomial(n+9, n) - (n*10 + 2))