import sys
from collections import deque


def bfs():
    r_dq = deque()
    while dq:
        x, y, idx = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = idx
                    r_dq.append([nx, ny, idx])
    return r_dq


n, m = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr = [[0 for i in range(n)] for i in range(n)]
visited = [[0 for i in range(n)] for i in range(n)]
dq = deque()
for i in range(n):
    arr[i] = list(map(int, input().split()))
for i in range(1, m + 1):
    for j in range(n):
        for k in range(n):
            if arr[j][k] == i:
                dq.append([j, k, i])
                visited[j][k] = i

cnt, resx, resy = map(int, input().split())
for i in range(cnt):
    dq = bfs()

print(visited[resx - 1][resy - 1])
