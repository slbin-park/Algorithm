import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0


def bfs(sx, sy):
    dq = deque()
    dq.append((sx, sy))
    visited[sx][sy] = 1
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))


dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]
visited = [[0 for i in range(m)] for i in range(n)]
arr = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and arr[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)
