C = 0

for line in open('p102_triangles.txt'):
    ax, ay, bx, by, cx, cy = map(int, line.split(','))
    a = ax*by - ay*bx > 0
    b = bx*cy - by*cx > 0
    c = cx*ay - cy*ax > 0

    C+= a==b==c

print("Number of triangles that contain the origin:", C)