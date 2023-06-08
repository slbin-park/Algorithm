from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
isSosu = [0 for i in range(1001)]
isSosu[0] = 1
isSosu[1] = 1
for i in range(2, 501):
    if isSosu[i] == 0:
        for j in range(i + i, 1001, i):
            isSosu[j] = 1
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    if isSosu[arr[i]] == 0:
        ans += 1
print(ans)
