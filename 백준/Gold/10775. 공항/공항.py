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


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
answer = 0
for i in range(P):
    g = int(input())
    a = find(g)
    if a == 0:
        break
    parent[a] = find(a - 1)
    answer += 1
print(answer)