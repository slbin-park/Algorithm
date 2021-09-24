import sys
import collections
from collections import deque

input = sys.stdin.readline
graph = collections.defaultdict(list)
n, m, k, x = map(int, input().rstrip().split())
visited = [0 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
res = [0 for i in range(n + 1)]
dq = deque()
dq.append(x)
visited[x] = 1
while dq:
    a = dq.popleft()
    if b == k:
        res[a] == b
    elif b < k:
        for i in graph[a]:
            if visited[i] == 0:
                dq.append(i)
                visited[i] = 1
if len(res) == 0:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)
