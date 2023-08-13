from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
R, C, m = map(int, input().split())
arr = [[[0, 0, 0] for i in range(C)] for i in range(R)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
for i in range(m):
    # r,c
    # s 속력  , d 이동 방향 , z 크기
    r, c, s, d, z = map(int, input().split())
    arr[r - 1][c - 1] = [z, s, d]


def moveShark():
    tmpArr = [[[0, 0, 0] for i in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j][0] != 0:
                cs = arr[i][j][1]
                nx = i
                ny = j
                d = arr[i][j][2]
                z = arr[i][j][0]
                while cs:
                    if 0 <= nx + dx[d] < R and 0 <= ny + dy[d] < C:
                        cs -= 1
                        nx += dx[d]
                        ny += dy[d]
                    else:
                        d = nextDir(d)
                if tmpArr[nx][ny][0] < z:
                    tmpArr[nx][ny] = [arr[i][j][0], arr[i][j][1], d]
    return tmpArr


def nextDir(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    return 3


# print(arr[0])
# print(arr[1])
# print("========")
res = 0
for i in range(C):
    # for j in range(R):
    #     for k in range(C):
    #         print(arr[j][k][0], end=" ")
    #     print()
    # print("==========")
    for j in range(R):
        if arr[j][i][0] != 0:
            res += arr[j][i][0]
            arr[j][i] = [0, 0, 0]
            break
    arr = moveShark()

print(res)
