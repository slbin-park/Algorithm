from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
N = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
arr = [["" for i in range(N)] for i in range(N)]
CNT = 0
for i in range(N):
    a = input()
    for j in range(N):
        arr[i][j] = a[j]


def bfs():
    global arr, CNT
    for i in range(N):
        for j in range(N):
            checkHang(i, j)
            checkYeol(i, j)


def checkHang(x, y):
    global CNT
    cnt = 1
    nx = x - 1
    while nx >= 0:
        if arr[x][y] == arr[nx][y]:
            cnt += 1
            nx -= 1
        else:
            break
    nx = x + 1
    while nx < N:
        if arr[x][y] == arr[nx][y]:
            cnt += 1
            nx += 1
        else:
            break
    CNT = max(CNT, cnt)


def checkYeol(x, y):
    global CNT
    cnt = 1
    ny = y - 1
    while ny >= 0:
        if arr[x][y] == arr[x][ny]:
            cnt += 1
            ny -= 1
        else:
            break
    ny = y + 1
    while ny < N:
        if arr[x][y] == arr[x][ny]:
            cnt += 1
            ny += 1
        else:
            break
    CNT = max(CNT, cnt)


for i in range(N):
    for j in range(N):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != arr[i][j]:
                    tmp = arr[nx][ny]
                    tmp2 = arr[i][j]
                    arr[nx][ny] = tmp2
                    arr[i][j] = tmp
                    bfs()
                    # for l in range(N):
                    #     print(arr[l])
                    arr[nx][ny] = tmp
                    arr[i][j] = tmp2
print(CNT)
