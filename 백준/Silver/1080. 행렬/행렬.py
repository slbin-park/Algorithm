from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n , m = map(int,input().split())
arr1 = [[0 for i in range(m)]for i in range(n)]
arr2 = [[0 for i in range(m)]for i in range(n)]
for i in range(n):
    a = input().strip()
    for j in range(m):
        arr1[i][j] = int(a[j])
for i in range(n):
    a = input().strip()
    for j in range(m):
        arr2[i][j] = int(a[j])
cnt = 0
for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j] and (i+3 <= n and j+3<=m):
            cnt+=1
            for k in range(i,min(i+3,n)):
                for l in range(j,min(j+3,m)):
                    if arr1[k][l] == 1:
                        arr1[k][l] = 0
                    else:
                        arr1[k][l] = 1
for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]:
            print(-1)
            exit(0)
print(cnt)