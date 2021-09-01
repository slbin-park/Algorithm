import sys
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0 for i in range(f+1)]
dq = deque()
dq.append((s, 0))
cnt = -1
while dq:
    a, b = dq.popleft()
    if a == g:
        cnt = b
        break
    if a+u <= f:
        if visited[a+u] == 0:
            dq.append((a+u, b+1))
            visited[a+u] = 1
    if a-d >= 1:
        if visited[a-d] == 0:
            dq.append((a-d, b+1))
            visited[a-d] = 1

if cnt == -1:
    print('use the stairs')
else:
    print(cnt)
