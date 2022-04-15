import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [start, 0])
    distance[start] = 0
    while heap:
        idx, cost = heapq.heappop(heap)
        if cost > distance[idx]:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [next, cost + cst])


n = int(input())
m = int(input())
distance = [INF for i in range(n + 1)]
arr = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
