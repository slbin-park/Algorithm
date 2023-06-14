from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10**5)


input = sys.stdin.readline
n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][i] == 1 and arr[i][k]:
                arr[j][k] = 1
for i in range(n):
    for k in range(n):
        print(arr[i][k], end=" ")
    print()
