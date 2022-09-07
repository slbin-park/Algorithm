from copy import deepcopy
import heapq
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap,[start,0])
    dis[start][0] = 0
    dis[start][1] = start
    while heap :
        idx , cost = heapq.heappop(heap)
        if cost > dis[idx][0]:
            continue
        for next,cst in arr[idx]:
            if dis[next][0] > cost+cst:
                dis[next][0] = cost+cst
                dis[next][1] = idx
                heapq.heappush(heap,[next,cost+cst])

def parent(x):
    if x==dis[x][1]:
        return
    else:
        result.append(dis[x][1])
        parent(dis[x][1])
n = int(input()) # 도시 개수
arr = [[]for i in range(n+1)]
dis = [[1e9,-1] for i in range(n+1)]
m = int(input()) # 버스 개수
for i in range(m):
    u,v,w = map(int,input().split())
    arr[u].append([v,w])
start,end = map(int,input().split())
dijkstra(start)
result = []
result.append(end)
parent(end)
result.reverse()
print(dis[end][0])
print(len(result))
print(*result)
