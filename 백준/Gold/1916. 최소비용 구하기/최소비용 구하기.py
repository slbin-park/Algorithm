import sys
from collections import deque
import heapq

INF = 1e9
input = sys.stdin.readline


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    dis = [INF] * (n + 1)
    dis[start] = 0

    while heap:
        cos, index = heapq.heappop(heap)
        if dis[index] < cos:
            continue
        for e, c in bus[index]:
            if dis[e] > cos + c:
                dis[e] = cos + c
                heapq.heappush(heap, (cos + c, e))
    return dis[end]


n = int(input())
m = int(input())
bus = [[] for i in range(n + 1)]
for i in range(m):
    s, e, c = map(int, input().split())
    bus[s].append((e, c))
start, end = map(int, input().split())
print(dijkstra(start, end))
