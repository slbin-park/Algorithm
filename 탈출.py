import sys
from collections import deque

input = sys.stdin.readline


def bfss():
    global prevs
    bfsw()
    res = 1e9
    while dqs:
        x, y, cnt = dqs.popleft()
        if prevs != cnt:
            prevs = cnt
            bfsw()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'D':
                    res = min(res, cnt + 1)
                    break
                if arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dqs.append((nx, ny, cnt + 1))
    return res


def bfsw():
    global prevw
    while dqw:
        x, y, cnt = dqw.popleft()
        if prevw != cnt:
            dqw.appendleft((x, y, cnt))
            prevw = cnt
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    arr[nx][ny] = '*'
                    visited[nx][ny] = 1
                    dqw.append((nx, ny, cnt + 1))


n, m = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr = [['' for i in range(m)] for j in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
dqs = deque()  # 고슴도치 위치
dqw = deque()  # 물
prevw = 0  #물 위치
prevs = 0  #고슴도치

for i in range(n):
    a = input().strip()
    for j in range(m):
        if a[j] == 'S':
            dqs.append((i, j, 0))
            visited[i][j] = 1
        if a[j] == '*':
            dqw.append((i, j, 0))
            visited[i][j] = 1
        arr[i][j] = a[j]

res = bfss()
if res == 1e9:
    print('KAKTUS')
else:
    print(res)