from copy import deepcopy
import heapq
import sys
from collections import deque
from itertools import combinations
from xml.dom.minicompat import NodeList
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

def dijkstra():
    heap = []
    heapq.heappush(heap,[0,start])
    dis[start] = 0
    while heap:
        cost,idx = heapq.heappop(heap)
        if dis[idx] < cost : 
            continue
        for next,cst in arr[idx]:
            if dis[next] > cost+cst:
                dis[next] = cost+cst
                heapq.heappush(heap,[cost+cst,next])
    

n, m = map(int,input().split())
arr = [[]for i in range(n+1)]
dis = [INF] * (n+1)
start = int(input())
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
dijkstra()
for i in range(1,n+1):
    if dis[i] == INF:
        print('INF')
        continue
    print(dis[i])