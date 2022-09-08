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

def dijkstra(start):
    dis = [INF for i in range(n+1)]
    dis[start] = 0
    heap = []
    heapq.heappush(heap,[0,start])
    while heap:
        cost , idx = heapq.heappop(heap)
        if dis[idx] < cost:
            continue
        for next,cst in arr[idx]:
            if cost+cst < dis[next]:
                dis[next] = cost+cst
                heapq.heappush(heap,[cost+cst,next])
    return dis
                
n = int(input())
a,b,c = map(int,input().split())
arr = [[]for i in range(n+1)]
m = int(input())
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
    arr[v].append([u,w])
a_dis = dijkstra(a)
b_dis = dijkstra(b)
c_dis = dijkstra(c)
result = 0
answ = 0
for i in range(1,n+1):
    cur_min = min(a_dis[i],b_dis[i],c_dis[i])
    if result < cur_min:
        result = cur_min
        answ = i
print(answ)