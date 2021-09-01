import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def bfs():
    cnt = 0
    while dq:
        cnt += 1
        x, y = dq.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    dq.append((nx, ny))
                    arr[nx][ny] = arr[x][y]+1


n, m = map(int, input().split())
arr = [[0]*n for i in range(m)]

dq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(m):
    arr[i] = list(map(int, input().split()))
    for j in range(n):
        if arr[i][j] == 1:
            dq.append((i, j))

bfs()
if any(0 in l for l in arr):
    print(-1)
else:
    print(max(map(max, arr))-1)
