from math import log

file_url = open('./p099_base_exp.txt')
pairs = file_url.read().split('\n')
mv, ml = 0, 0 

for ln, line in enumerate(pairs, start=1):
    b, e = line.split(',') 
    v = int(e) * log(int(b)) 
    if v > mv: 
        mv, ml = v, ln 

print("Project Euler 99 Solution =", ml)