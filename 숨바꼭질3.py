import sys
from collections import deque

input = sys.stdin.readline

Max = 100001
n, m = map(int, input().split())
dq = deque()
dq.append(n)
dis = [-1 for _ in range(Max)]
dis[n] = 0
res = 0
if n == m:
    res = 1
while dq:
    a = dq.popleft()
    if a * 2 < Max:
        if dis[a * 2] == -1:
            dq.append(a * 2)
            dis[a * 2] = dis[a] + 1
        elif dis[a * 2] == dis[a] + 1:
            dq.append(a * 2)
        if a * 2 == m and dis[a] + 1 == dis[m]:
            res += 1
    if a + 1 < Max:
        if dis[a + 1] == -1:
            dq.append(a + 1)
            dis[a + 1] = dis[a] + 1
        elif dis[a + 1] == dis[a] + 1:
            dq.append(a + 1)
        if a + 1 == m and dis[a] + 1 == dis[m]:
            res += 1
    if a - 1 >= 0:
        if dis[a - 1] == -1:
            dq.append(a - 1)
            dis[a - 1] = dis[a] + 1
        elif dis[a - 1] == dis[a] + 1:
            dq.append(a - 1)
        if a - 1 == m and dis[a] + 1 == dis[m]:
            res += 1
print(dis[m])
print(res)
