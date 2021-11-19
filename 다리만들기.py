import sys

sys.setrecursionlimit(10**5)
from collections import deque

input = sys.stdin.readline


def bfs(startx, starty):
    global var
    dq.append((startx, starty))
    visited[startx][starty] = var
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dq.append((nx, ny))
                    visited[nx][ny] = var
                if arr[nx][ny] == 0:
                    visited[x][y] = -var
    var += 1


def bfs2(m):
    dq2 = deque()
    dist = [[-1 for _ in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if -m == visited[i][j]:
                dq2.append((i, j))
                dist[i][j] = 0
    while dq2:
        x, y = dq2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] != 0 and visited[nx][ny] != m and visited[
                        nx][ny] != -m:
                    return dist[x][y]
                if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dq2.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1


n = int(input())
dq = deque()
visited = [[0 for i in range(n)] for i in range(n)]
res = 100000
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = [[0 for i in range(n)] for i in range(n)]
var = 2
for i in range(n):
    arr[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] == 1:
            bfs(i, j)
for i in range(var - 2):
    res = min(res, bfs2(i + 2))
print(res)
