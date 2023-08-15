from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)


def dragonCurve(x, y, d, g):
    dragon = []
    arr[y][x] = 1
    nx = x + dx[d]
    ny = y + dy[d]
    arr[ny][nx] = 1
    dragon.append(d)
    for i in range(g):
        for j in range(len(dragon) - 1, -1, -1):
            nd = (dragon[j] + 1) % 4
            nx += dx[nd]
            ny += dy[nd]
            arr[ny][nx] = 1
            dragon.append(nd)


input = sys.stdin.readline
arr = [[0 for i in range(101)] for i in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
n = int(input())
for i in range(n):
    x, y, d, g = map(int, input().split())
    dragonCurve(x, y, d, g)

res = 0
for i in range(100):
    for j in range(100):
        if (
            arr[i][j] == 1
            and arr[i + 1][j] == 1
            and arr[i][j + 1] == 1
            and arr[i + 1][j + 1] == 1
        ):
            res += 1
print(res)
