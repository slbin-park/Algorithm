import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(1, n // 2 + 1):
    if n % i == 0:
        arr.append(i)
arr.append(n)
if len(arr) < m:
    print(0)
else:
    print(arr[m - 1])
