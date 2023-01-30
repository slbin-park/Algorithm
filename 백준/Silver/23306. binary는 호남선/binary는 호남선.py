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
print("? 1")
sys.stdout.flush()
a = int(input())
print("?", N)
sys.stdout.flush()
b = int(input())
if a == 1 and b == 0:
    print("! -1")
elif a == 0 and b == 1:
    print("! 1")
else:
    print("! 0")