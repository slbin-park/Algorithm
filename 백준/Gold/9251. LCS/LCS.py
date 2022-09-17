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

a = input().strip()
b = input().strip()
if len(a) > len(b):
    tmp = b
    b = a
    a = tmp
arr = [[0 for i in range(len(a)+1)]for i in range(len(b)+1)]
for i in range(1,len(b)+1):
    cur_v = b[i-1]
    for j in range(1,len(a)+1):
        if cur_v == a[j-1]:
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i-1][j],arr[i][j-1])
print(max(arr[len(b)]))