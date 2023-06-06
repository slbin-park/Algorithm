from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
res = 0
arr = list(map(int, input().split()))
maxN = max(arr)
for i in range(n):
    res += arr[i] / maxN * 100
print(res / n)
