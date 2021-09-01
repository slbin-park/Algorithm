import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, rgb):
    global cnt
    dq.append((x, y))
    visited[x][y] = 1
    while dq:
        x1, y1 = dq.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] == rgb:
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
    cnt += 1


def bfsg(x, y, rgb):
    global cnt
    dq.append((x, y))
    visited[x][y] = 1
    while dq:
        x1, y1 = dq.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if rgb == 'R' or rgb == 'G':
                        if arr[nx][ny] != 'B':
                            dq.append((nx, ny))
                            visited[nx][ny] = 1
                    elif arr[nx][ny] == rgb:
                        dq.append((nx, ny))
                        visited[nx][ny] = 1
    cnt += 1


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
n = int(input())
arr = [input() for i in range(n)]
dq = deque()
visited = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, arr[i][j])
print(cnt, end=' ')
cnt = 0
visited = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfsg(i, j, arr[i][j])
print(cnt)
