import sys
from collections import deque

input = sys.stdin.readline

Max = 100001
n, m = map(int, input().split())
dq = deque()
dq.append(n)
dis = [-1 for _ in range(Max)]
dis[n] = 0
while dq:
    a = dq.popleft()
    if a == m:
        break
    if a * 2 < Max and dis[a * 2] == -1:
        dq.appendleft(a * 2)
        dis[a * 2] = dis[a]
    if a + 1 < Max and dis[a + 1] == -1:
        dq.append(a + 1)
        dis[a + 1] = dis[a] + 1
    if a - 1 >= 0 and dis[a - 1] == -1:
        dq.append(a - 1)
        dis[a - 1] = dis[a] + 1
print(dis[m])
