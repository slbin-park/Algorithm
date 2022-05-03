import sys
from collections import deque

n, m = map(int, input().split())
arr = [0 for i in range(101)]
for i in range(n):
    x, y = map(int, input().split())
    arr[x] = y
for i in range(m):
    x, y = map(int, input().split())
    arr[x] = y
dq = deque()
dq.append([1, 0])
deque = 0
visited = [0 for i in range(101)]
while dq:
    cur_x, cnt = dq.popleft()
    if cur_x == 100:
        res = cnt
        break
    for i in range(1, 7):
        if cur_x + i <= 100 and visited[cur_x + i] == 0:
            if arr[cur_x + i] != 0:
                visited[cur_x + 1] = 1
                dq.append([arr[cur_x + i], cnt + 1])
            else:
                visited[cur_x + 1] = 1
                dq.append([cur_x + i, cnt + 1])
print(res)
