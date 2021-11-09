from math import *

res = []
for i in range(1, 51):
    for j in range(1, 51):
        b = sqrt(i * i + j * j)
        if b == int(b) and b <= 50:
            a = [i, j, int(b)]
            a.sort()
            # print(a)
            if (a[0], a[1], a[2]) not in res:
                res.append((i, j, int(b)))
# res = set(res)
print("세 변의 길이가 50이하의 정수인 직각 삼각혀의 세변의 쌍 ", len(res), "개 입니다.")
for i in res:
    print(i)
