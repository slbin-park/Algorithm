import sys
import heapq
import math

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dv(x, y, n):
    list = []
    if n == 2:
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                list.append(arr[i][j])
        list.sort()
        return list[2]
    else:
        n = n // 2
        list.append(dv(x, y, n))
        list.append(dv(x, y + n, n))
        list.append(dv(x + n, y, n))
        list.append(dv(x + n, y + n, n))
        list.sort()
        return list[2]


n = int(input())
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
print(dv(0, 0, n))
