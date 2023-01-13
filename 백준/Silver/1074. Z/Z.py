import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def dfs(x, y, nn):
    global cnt
    if nn == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == r and ny == c:
                print(cnt)
                exit()
            cnt += 1
    else:
        nn = nn // 2
        nx = x
        ny = y
        if nx + nn >= r and ny + nn >= c:
            dfs(x, y, nn)
        else:
            cnt += nn**2
        nx = x
        ny = y + nn
        if nx + nn >= r and ny + nn >= c:
            dfs(x, y + nn, nn)
        else:
            cnt += nn**2

        nx = x + nn
        ny = y
        if nx + nn >= r and ny + nn >= c:
            dfs(x + nn, y, nn)
        else:
            cnt += nn**2

        nx = x + nn
        ny = y + nn
        if nx + nn >= r and ny + nn >= c:
            dfs(x + nn, y + nn, nn)
        else:
            cnt += nn**2


n, r, c = map(int, input().split())
cnt = 0
dfs(0, 0, 2**n)
