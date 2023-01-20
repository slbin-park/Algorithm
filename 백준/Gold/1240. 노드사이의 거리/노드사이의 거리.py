import sys
import heapq
import math
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = 1e9


def mip():
    return map(int, input().split())


def lip():
    return list(map(int, input().split()))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def get_dis(start, end):
    dq = deque()
    dq.append([start, 0])
    visited = [INF for i in range(n + 1)]
    visited[start] = 0
    while dq:
        idx, cost = dq.popleft()
        for next, cst in arr[idx]:
            if next == end:
                return cost + cst
            if visited[next] > cost + cst:
                visited[next] = cost + cst
                dq.append([next, cost + cst])


n, m = mip()
arr = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v, w = mip()
    arr[u].append([v, w])
    arr[v].append([u, w])

for j in range(m):
    u, v = mip()
    print(get_dis(u, v))
