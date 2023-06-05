from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = []
visited = [[1e9 for i in range(m)] for i in range(m)]
dq = deque()
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 2:
            dq.append([i, j, 1])
            visited[i][j] = 0
    arr.append(a)
while dq:
    x, y, cnt = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 1e9 and arr[nx][ny] != 0:
                visited[nx][ny] = cnt
                dq.append([nx, ny, cnt + 1])
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1e9:
            if arr[i][j] == 1:
                print(-1, end=" ")
                continue
            print(0, end=" ")
            continue
        print(visited[i][j], end=" ")
    print()
