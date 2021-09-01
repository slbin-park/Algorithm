from itertools import combinations
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline


def bfs(dcpyarr, virus):
    visited = [[0]*m for i in range(n)]

    for v in virus:
        dq.append(v)
        visited[v[0]][v[1]] = 1
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0:
                        if dcpyarr[nx][ny] == 0:
                            visited[nx][ny] = 1
                            dq.append((nx, ny))
                            dcpyarr[nx][ny] = 2
    count = 0
    for i in range(n):
        for j in range(m):
            if dcpyarr[i][j] == 0:
                count += 1
    return count


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
arr = [[]*m for i in range(n)]
zero = []
virus = []
cnt = 0
dq = deque()
for i in range(n):
    arr[i] = list(map(int, input().split()))
    for j in range(m):
        if arr[i][j] == 0:
            zero.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
zerocombi = list(combinations(zero, 3))
for zcombi in zerocombi:
    dcpyarr = deepcopy(arr)
    first = zcombi[0]
    second = zcombi[1]
    third = zcombi[2]
    dcpyarr[first[0]][first[1]] = 1
    dcpyarr[second[0]][second[1]] = 1
    dcpyarr[third[0]][third[1]] = 1
    cnt = max(bfs(dcpyarr, virus), cnt)
print(cnt)
