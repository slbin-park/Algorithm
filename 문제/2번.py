from math import *

res = []
for i in range(1, 51):
    for j in range(1, 51):
        b = sqrt(i * i + j * j)
        if b == int(b) and b < 50:
            a = [i, j, int(b)]
            a.sort()
            # print(a)
            if (a[0], a[1], a[2]) not in res:
                res.append((i, j, int(b)))
# res = set(res)
for i in res:
    print(i)
