import sys
import heapq

INF = 1e9


def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0
    while heap:
        cost, index = heapq.heappop(heap)
        if distance[index] < cost:
            continue
        for end, c in graph[index]:
            if distance[end] > cost + c:
                distance[end] = cost + c
                heapq.heappush(heap, (cost + c, end))


n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF for i in range(n + 1)]
for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])