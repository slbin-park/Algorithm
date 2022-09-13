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

def dijkstra():
    heap = []
    heapq.heappush(heap,[0,1])
    dis[1] = 0
    while heap:
        cost,idx = heapq.heappop(heap)
        if dis[idx] < cost:
            continue
        for next,cst in arr[idx]:
            if dis[next] > cost+cst:
                dis[next] = cost+cst
                con[next] = idx
                heapq.heappush(heap,[cost+cst,next]) 

n , m = map(int,input().split())
arr = [[]for i in range(n+1)]
dis = [INF] * (n+1)
con = [i for i in range(n+1)]
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
    arr[v].append([u,w])
dijkstra()
result = set()
for i in range(2,n+1):
    if con[i] > i:
        result.add((i,con[i]))
    else:
        result.add((con[i],i))
reuslt = list(result)
print(len(result))
for cur,next in result:
    print(cur , next)

