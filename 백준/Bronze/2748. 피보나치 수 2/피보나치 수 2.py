from copy import deepcopy
import heapq
from re import A
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline


dp = [0 for i in range(101)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3,101):
    dp[i] = dp[i-1]+dp[i-2]
n = int(input())
print(dp[n])