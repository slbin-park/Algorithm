import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    global maxlen
    dq.append((x, y, 1))
    visited = [[0 for i in range(m)] for i in range(n)]
    visited[x][y] = 1
    max1 = 0
    while dq:
        x1, y1, cnt = dq.popleft()
        if cnt > max1:
            max1 = cnt
        for i in range(4):
            nx = x1+dx[i]
            ny = y1+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                    dq.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1
    if maxlen < max1:
        maxlen = max1


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dq = deque()
llist = []
n, m = map(int, input().split())
arr = [[[] for i in range(m)] for i in range(n)]
maxlen = 0
for i in range(n):
    a = input()
    for j in range(m):
        arr[i][j] = a[j]
        if arr[i][j] == 'L':
            llist.append((i, j))
for i in llist:
    a, b = i
    bfs(a, b)

print(maxlen-1)
