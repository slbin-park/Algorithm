import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def fpow(v, n):
    if n == 1:
        return v % c
    else:
        x = fpow(v, n // 2)
        if n % 2 == 0:
            return x * x % c
        else:
            return x * x * v % c


a, b, c = map(int, input().split())
print(fpow(a, b))
