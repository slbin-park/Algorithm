import sys
from collections import deque

input = sys.stdin.readline


def bfs(startx, starty):
    global res
    dq.append((startx, starty))
    while dq:
        x, y = dq.popleft()
        visited[x][y] = 1
        flag = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dq.append((nx, ny))

                if arr[nx][ny] == 0:
                    flag = 0
        if flag == 0:
            dq2.append((x, y, 0))
    flag2 = 1
    visited0 = [[0 for i in range(n)] for i in range(n)]
    while dq2 and flag2:
        x, y, cnt = dq2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0 and visited0[nx][ny] == 0:
                    dq2.append((nx, ny, cnt + 1))
                    visited0[nx][ny] = 1
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    flag2 = 0
                    res = min(res, cnt)
                    break


def bfs1(startx, starty):
    dq.append((startx, starty))
    while dq:
        x, y = dq.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dq.append((nx, ny))


n = int(input())
dq = deque()
visited = [[0 for i in range(n)] for i in range(n)]
res = 1e9
dq2 = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] == 1:
            bfs(i, j)
        if visited[i][j] == 1 and arr[i][j] == 1:
            bfs1(i, j)
print(res)
