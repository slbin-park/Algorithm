import sys
from collections import deque

input = sys.stdin.readline


def bfs(x1, y1):
    dq = deque()
    dq.append((x1, y1))
    while dq:
        x, y = dq.popleft()


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
arr = [['' for i in range(m)] for j in range(n)]
print(arr)
for i in range(n):
    a = input()
    for j in range(m):
        arr[i][j] = a[j]
# 탈출 공간이 있는지 확인
for i in range(n):
    if arr[0][i] == '.':
        break
    if arr[n - 1][i] == '.':
        break
    if arr[i][0] == '.':
        break
    if arr[i][m - 1] == '.':
        break
