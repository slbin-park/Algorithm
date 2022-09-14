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
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4,101):
    dp[i] = dp[i-2]+dp[i-3]
n = int(input())
for i in range(n):
    m = int(input())
    print(dp[m])