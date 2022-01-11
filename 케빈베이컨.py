import sys
from collections import deque


def bfs(start):
    visited = [0 for i in range(n + 1)]
    dq = deque()
    dq.append((start, 0))
    visited[start] = 1
    while dq:
        a, cnt = dq.popleft()
        for i in arr[a]:
            if visited[i] == 0:
                dq.append((i, cnt + 1))
                visited[i] = cnt + 1
    return sum(visited) - 1


n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
#res = [0 for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
cur = 1e9
idx = 0
for i in range(1, n + 1):
    a = bfs(i)
    if cur > a:
        idx = i
        cur = a

print(idx)
