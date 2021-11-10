import sys
from collections import deque

input = sys.stdin.readline


def bfs(x1, y1):
    dq = deque()
    visited = [[0 for i in range(m)] for i in range(n)]
    visited[x1][y1] = 1
    dq.append((x1, y1, 0))
    res = 0
    flag2 = 0
    prevcnt = 0
    while dq:
        x, y, cnt = dq.popleft()
        if prevcnt != cnt:
            prevcnt = cnt
            fire_bfs()
        if x == n - 1 or x == 0:
            if arr[x][y] != 'F':
                flag2 = 1
                res = cnt
                break
        if y == m - 1 or y == 0 and arr[x][y] != 'F':
            if arr[x][y] != 'F':
                flag2 = 1
                res = cnt
                break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == '.':
                    visited[nx][ny] = 1
                    dq.append((nx, ny, cnt + 1))

    if flag2 == 1:
        return res + 1
    else:
        return -1


def fire_bfs():
    global cur
    while fire:
        x, y, cnt = fire.popleft()
        if cur < cnt:
            cur = cur + 1
            fire.append((x, y, cnt))
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == '.':
                        arr[nx][ny] = 'F'
                        fire.append((nx, ny, cnt + 1))
    # print(arr)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
flag = 0
cur = 0
n, m = map(int, input().split())
fire = deque()
arr = [['' for i in range(m)] for j in range(n)]
start = 0
end = 0
for i in range(n):
    a = input()
    for j in range(m):
        if a[j] == 'F':
            fire.append((i, j, 0))
        if a[j] == 'J':
            start = i
            end = j
        arr[i][j] = a[j]
# 탈출 공간이 있는지 확인
for i in range(m):
    if arr[0][i] == '.' or arr[0][i] == 'J':
        flag = 1
        break
    if arr[n - 1][i] == '.' or arr[n - 1][i] == 'J':
        flag = 1
        break
for i in range(n):
    if arr[i][0] == '.' or arr[i][0] == 'J':
        flag = 1
        break
    if arr[i][m - 1] == '.' or arr[i][m - 1] == 'J':
        flag = 1
        break
if flag == 1:
    a = bfs(start, end)
    if a == -1:
        print('IMPOSSIBLE')
    else:
        print(a)
else:
    print('IMPOSSIBLE')
