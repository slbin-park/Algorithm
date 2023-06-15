from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10**5)


input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
visited = [[0 for i in range(m)] for i in range(n)]
dq = deque()
for i in range(n):
    a = input().rstrip()
    for j in range(m):
        arr[i][j] = a[j]
        if a[j] == "I":
            dq.append([i, j])
            visited[i][j] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = 0
while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and arr[nx][ny] != "X":
                visited[nx][ny] = 1
                dq.append([nx, ny])
                if arr[nx][ny] == "P":
                    res += 1

print("TT" if res == 0 else res)
