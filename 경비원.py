n, m = map(int, input().split())
a = int(input())
arr = []


def res_sum(x1, y1, x2, y2):
    if x1 == 1:
        if x2 == 1:
            return abs(y1 - y2)
        if x2 == 2:
            return min((y1 + y2 + m), ((2 * n) + m - y1 - y2))
        if x2 == 3:
            return y1 + y2
        if x2 == 4:
            return n - y1 + y2
    if x1 == 2:
        if x2 == 1:
            return min((y1 + y2 + m), ((2 * n) + m - y1 - y2))
        if x2 == 2:
            return abs(y1 - y2)
        if x2 == 3:
            return y1 + m - y2
        if x2 == 4:
            return n + m - y1 - y2
    if x1 == 3:  #서쪽
        if x2 == 1:  #북
            return y1 + y2
        if x2 == 2:  #남
            return m - y1 + y2
        if x2 == 3:  #서
            return abs(y1 - y2)
        if x2 == 4:  #동
            return min((y1 + y2 + n), ((2 * m) + n - y1 - y2))
    if x1 == 4:  #동
        if x2 == 1:  #북
            return n + y1 - y2  #
        if x2 == 2:  #남
            return m - y2 + n - y1
        if x2 == 3:  #서
            return min((y1 + y2 + n), ((2 * m) + n - y1 - y2))
        if x2 == 4:  #동
            return abs(y1 - y2)


for i in range(a):
    b, c = map(int, input().split())
    arr.append((b, c))
x, y = map(int, input().split())
res = 0
for i in arr:
    res += res_sum(x, y, i[0], i[1])
print(res)