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

N = int(input())
arr = lip()
dq = deque()
answer = []
for i in range(N):
    dq.append([i + 1, arr[i]])
while dq:
    # print(dq)
    i, v = dq.popleft()
    answer.append(i)
    if len(dq) == 0:
        break
    if v < 0:
        v = -v
        for _ in range(v):
            dq.appendleft(dq.pop())
    else:
        for _ in range(v - 1):
            dq.append(dq.popleft())
print(*answer)