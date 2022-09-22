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

def dijkstra(start):
    dis = [INF for i in range(n+1)]
    heap = []
    dis[start] = 0
    heapq.heappush(heap,[0,start])
    while heap:
        cost,idx = heapq.heappop(heap)
        if dis[idx] < cost:
            continue
        for next,cst in arr[idx]:
            if dis[next] > cost+cst:
                dis[next] = cost+cst
                heapq.heappush(heap,[cost+cst,next])
    return dis
        

T = int(input())
for i in range(T):
    # 교차로 도로 목적지 후보
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    arr = [[]for i in range(n+1)]
    des = []
    for i in range(m):
        a,b,d = map(int,input().split())
        if a==g and b==h:
            arr[a].append([b,d-0.1])
            arr[b].append([a,d-0.1])
        elif b==g and a==h:
            arr[a].append([b,d-0.1])
            arr[b].append([a,d-0.1])
        else:
            arr[a].append([b,d])
            arr[b].append([a,d])
    dis2 = dijkstra(s)
    result = []
    for i in range(t):
        c = int(input())
        if dis2[c] !=INF and type(dis2[c]) is float:
            result.append(c)
    result.sort()
    print(*result)
    