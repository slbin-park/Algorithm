import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, [start, 0])
    while heap:
        idx, cost = heapq.heappop(heap)
        if distance[idx] < cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [next, cost + cst])


n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
distance = [INF for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
dijkstra(1)
print(distance[-1])