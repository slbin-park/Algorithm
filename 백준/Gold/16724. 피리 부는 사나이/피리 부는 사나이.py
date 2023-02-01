import sys
import heapq
import math
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = 1e9


def mip():
    return map(int, input().split())


def lip():
    return list(map(int, input().split()))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dir(x, y):
    if arr[x][y] == "D":
        return [x + 1, y]
    if arr[x][y] == "L":
        return [x, y - 1]
    if arr[x][y] == "R":
        return [x, y + 1]
    if arr[x][y] == "U":
        return [x - 1, y]


def dfs(cnt):
    while dq:
        x, y = dq.popleft()
        nx, ny = dir(x, y)
        if visited[nx][ny] == 0:
            visited[nx][ny] = cnt
            dq.append([nx, ny])
        elif visited[nx][ny] == cnt:
            return True
        elif visited[nx][ny] != cnt:
            return False


n, m = mip()
arr = [['' for i in range(m)] for i in range(n)]
visited = [[0 for j in range(m)] for i in range(n)]
dq = deque()

for i in range(n):
    a = input().strip()
    for j in range(m):
        arr[i][j] = a[j]
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dq.append([i, j])
            cnt += 1
            visited[i][j] = cnt
            if dfs(cnt):
                ans += 1
print(ans)