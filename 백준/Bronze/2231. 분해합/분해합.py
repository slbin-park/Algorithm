import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

n = int(input())
for i in range(1, n):
    cur_v = i
    a = str(i)
    for j in range(len(a)):
        cur_v += int(a[j])
    if cur_v == n:
        print(i)
        exit()
print(0)