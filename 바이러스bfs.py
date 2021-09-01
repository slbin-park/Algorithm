import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    dq.append(x)
    visited = [0]*n
    visited[x] = 1
    while dq:
        x = dq.popleft()
        for i in v[x]:
            if not visited[i]:
                visited[i] = 1
                dq.append(i)
    return visited


n = int(input())
m = int(input())
v = [[] for i in range(n)]
dq = deque()
cnt = 0
for i in range(m):
    a,b = map(int,input().split())
    v[a-1].append(b-1)
    v[b-1].append(a-1)

res = bfs(0)
for i in res:
    if i>0:
        cnt+=1
print(cnt-1)