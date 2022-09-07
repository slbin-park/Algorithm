from copy import deepcopy
import heapq
from re import A
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e11
input = sys.stdin.readline

def dijkstra():
    heap = []
    heapq.heappush(heap,[0,1,0])
    while heap:
        cost,idx,cnt = heapq.heappop(heap)
        if dis[idx][cnt] < cost:
            continue
        for next,cst in arr[idx]:
            if dis[next][cnt] > cost+cst:
                dis[next][cnt] = cost+cst
                heapq.heappush(heap,[cost+cst,next,cnt])
            if cnt < k and dis[next][cnt+1] > cost:
                dis[next][cnt+1] = cost
                heapq.heappush(heap,[cost,next,cnt+1])
n,m,k = map(int,input().split())
arr = [[]for i in range(n+1)]
dis = [[INF for i in range(k+1)]for i in range(n+1)]
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
    arr[v].append([u,w])
dijkstra()
print(min(dis[n]))