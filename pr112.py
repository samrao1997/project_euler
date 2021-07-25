def is_bouncy(n):
  inc, dec, s = False, False, str(n)
  for i in range(len(s)-1):
    if s[i+1] > s[i]: inc = True
    elif s[i+1] < s[i]: dec = True
    if inc and dec: return True
  return False

n, p = 21780, 0.90
b = n * p
while p != 0.99:
  n += 1
  if is_bouncy(n): b += 1
  p = b / n
 
print("Project Euler 112 Solution =", n)




        
            