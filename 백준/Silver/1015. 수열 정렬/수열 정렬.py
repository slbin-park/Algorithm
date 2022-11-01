import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    arr[i] = [arr[i],i]
arr.sort(key=lambda x:x[0])
res = [0 for i in range(n)]
for i in range(n):
    res[arr[i][1]] = i
print(*res)