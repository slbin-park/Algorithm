import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline


def bfs(x, y):
    dq.append((x, y))
    visited[x][y] = 1
    icearr = []
    while dq:
        x1, y1 = dq.popleft()
        c = 0
        for i in range(4):
            nx = x1+dx[i]
            ny = y1+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    c += 1
                if arr[nx][ny] > 0 and visited[nx][ny] == 0:
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
        icearr.append((x1, y1, c))
    return icearr


dq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
arr = [[0 for i in range(m)]for i in range(n)]
maxyears = 1
years = 0
cnt = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))
while 1:
    visited = [[0]*m for i in range(n)]
    ice = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cnt > 1:
                print(years)
                exit()
            if visited[i][j] == 0 and arr[i][j] != 0:
                ice.extend(bfs(i, j))
                cnt += 1
    if cnt == 0:
        years = 0
        break
    while ice:
        a, b, c = ice.popleft()
        arr[a][b] = max(0, arr[a][b]-c)
    years += 1
print(years)
