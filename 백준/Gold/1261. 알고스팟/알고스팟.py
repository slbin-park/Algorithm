import sys
from collections import deque


def bfs():
    dq = deque()
    dq.append([0, 0, 0])
    visited[0][0] = 0
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] > cnt + 1:
                    dq.append([nx, ny, cnt + 1])
                    visited[nx][ny] = cnt + 1
                elif arr[nx][ny] == 0:
                    if visited[nx][ny] > cnt:
                        dq.append([nx, ny, cnt])
                        visited[nx][ny] = cnt


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
visited = [[1e9 for i in range(m)] for i in range(n)]
for i in range(n):
    a = input().strip()
    for j in range(m):
        arr[i][j] = int(a[j])
bfs()
print(visited[-1][-1])