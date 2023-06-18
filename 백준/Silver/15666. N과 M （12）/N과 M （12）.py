from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10**5)


def dfs(idx):
    global res
    if len(curArr) == m:
        for i in range(m):
            print(curArr[i], end=" ")
        print()
    else:
        for i in range(idx, len(arr)):
            curArr.append(arr[i])
            dfs(i)
            curArr.pop()


input = sys.stdin.readline
n, m = map(int, input().split())
arr = set()
curArr = []
res = []
a = list(map(int, input().split()))
for i in range(n):
    arr.add(a[i])
arr = list(arr)
arr.sort()
dfs(0)
