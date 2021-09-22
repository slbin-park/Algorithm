import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    global res
    while dq:
        x, y, cnt, dr = dq.popleft()
        if x == n - 1 and y == m - 1:
            res = min(res, cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][dr] == 0:
                    visited[nx][ny][dr] = 1
                    dq.append((nx, ny, cnt + 1, dr))
                elif arr[nx][ny] == 1 and dr == 0:
                    visited[nx][ny][1] = 1
                    dq.append((nx, ny, cnt + 1, 1))


n, m = map(int, input().split())
dq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = [[0 for i in range(m)] for i in range(n)]
visited = [[[0, 0] for i in range(m)] for i in range(n)]
dq.append((0, 0, 0, 0))
res = 10000000
for i in range(n):
    a = input()
    for j in range(m):
        arr[i][j] = int(a[j])
bfs()
if res == 10000000:
    print(-1)
else:
    print(res + 1)
