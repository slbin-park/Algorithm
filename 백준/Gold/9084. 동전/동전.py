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

t = int(input())
for i in range(t):
    n = int(input())
    knap = list(map(int,input().split()))
    m = int(input())
    arr = [0 for i in range(m+1)]
    arr[0] = 1
    for coin in knap:
        for k in range(m+1):
            if k >= coin:
                arr[k] += arr[k-coin]
    print(arr[-1])