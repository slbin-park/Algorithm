from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
M, N, H = map(int, input().split())
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dq = deque()
CNT = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                CNT += 1
            elif arr[i][j][k] == 1:
                dq.append([i, j, k, 0])
res = 0
allCnt = 0
while dq:
    h, x, y, cnt = dq.popleft()
    res = max(res, cnt)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nh = h + dh[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H:
            if arr[nh][nx][ny] == 0:
                arr[nh][nx][ny] = 1
                dq.append([nh, nx, ny, cnt + 1])
                allCnt += 1
if CNT == allCnt:
    print(res)
else:
    print(-1)
