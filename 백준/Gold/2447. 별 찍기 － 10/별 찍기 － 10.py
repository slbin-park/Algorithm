import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def dc(x, y, n):
    if n == 3:
        for i in range(x, x + n):
            for j in range(y, y + n):
                if i == x + 1 and j == y + 1:
                    continue
                arr[i][j] = "*"
    else:
        n = n // 3
        dx = [0, 0, 0, n, n, 2 * n, 2 * n, 2 * n]
        dy = [
            0,
            n,
            2 * n,
            0,
            2 * n,
            0,
            n,
            2 * n,
        ]
        for i in range(len(dx)):
            dc(x + dx[i], y + dy[i], n)


n = int(input())
arr = [[" " for i in range(n)] for i in range(n)]
dc(0, 0, n)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end="")
    print()