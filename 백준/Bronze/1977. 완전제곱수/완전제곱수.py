import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

n = int(input())
m = int(input())
i = 1
answer = 0
res = 0
while i**2 <= m:
    if n <= i**2 <= m:
        if answer == 0:
            answer = i**2
        res += i**2
    i += 1
if answer == 0:
    print(-1)
    exit()
print(res)
print(answer)