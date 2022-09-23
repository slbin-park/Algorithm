from copy import deepcopy
import heapq
from operator import truediv
from re import A
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
# type(123.4) is float
INF = 1e9
input = sys.stdin.readline

def dijkstra(mid):
    heap = []
    dis = [INF] * (n+1)
    heapq.heappush(heap,[0,1])
    dis[1] = 0
    while heap:
        cost,idx = heapq.heappop(heap)
        if cost > dis[idx]:
            continue;
        for next,cst in arr[idx]:
            cur_cost = cost
            if cst > mid:
                cur_cost +=1
            if cur_cost < dis[next]:
                heapq.heappush(heap,[cur_cost,next])
                dis[next] = cur_cost
    return dis[n] <= k

n,m,k = map(int,input().split())
arr = [[]for i in range(n+1)]
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
    arr[v].append([u,w])
result = -1
left = 0
right = 1000000
while left<=right:
    mid = (left+right)//2
    if dijkstra(mid):
        result = mid
        right = mid-1
    else:
        left = mid+1
print(result)