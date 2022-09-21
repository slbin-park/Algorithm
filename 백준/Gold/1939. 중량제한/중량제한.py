from copy import deepcopy
import heapq
from operator import truediv
from re import A
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

def bfs(mid):
    visited = [0 for i in range(n+1)]
    visited[start] = 1
    dq = deque()
    dq.append(start)
    while dq:
        idx = dq.popleft()
        for v,w in arr[idx]:
           if w >= mid and visited[v] == 0:
               dq.append(v)
               visited[v] = 1 
    if visited[end]:
        return True
    else:
        return False
n , m = map(int,input().split())
arr = [[]for i in range(n+1)]
result = 1000000
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
    arr[v].append([u,w])
start,end = map(int,input().split())
left = 1
right = 1000000001
while left<=right:
    mid = (left+right)//2
    if bfs(mid):
        result = mid
        left = mid+1
    else:
        right = mid-1
print(result)