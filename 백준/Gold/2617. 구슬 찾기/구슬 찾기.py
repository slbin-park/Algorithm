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


def dfs(idx):
    cnt = 0
    for next in arr1[idx]:
        if visited[next]==0:
            visited[next] = 1
            cnt+=1
            cnt+=dfs(next)
    return cnt

def dfs2(idx):
    cnt = 0
    for next in arr2[idx]:
        if visited[next]==0:
            visited[next] = 1
            cnt+=1
            cnt+=dfs2(next)
    return cnt
    
n , m = map(int,input().split())
# 자신보다 무거운 구슬
arr1 = [[] for i in range(n+1)]
# 자신보다 가벼운 구슬
arr2 = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    arr1[u].append(v)
    arr2[v].append(u)
result = 0
for i in range(1,n+1):
    visited = [0 for i in range(n+1)]
    h_cnt  = dfs(i)
    if h_cnt >=(n+1)//2:
        result+=1
        continue
    visited = [0 for i in range(n+1)]
    l_cnt = dfs2(i)
    
    if l_cnt >=(n+1)//2:
        result+=1
        continue
print(result)