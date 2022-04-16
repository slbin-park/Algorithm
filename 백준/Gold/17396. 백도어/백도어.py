import heapq
import sys

input = sys.stdin.readline
INF = 50000000000


def dijkstra(start):
    distance = [INF for i in range(n)]
    heap = []
    heapq.heappush(heap, [start, 0])
    distance[start] = 0
    while heap:
        idx, cost = heapq.heappop(heap)
        if cost > distance[idx]:
            continue
        if idx != n - 1 and ward[idx] == 1:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [next, cost + cst])
    return distance[n - 1]


n, m = map(int, input().split())
arr = [[] for i in range(n)]
ward = list(map(int, input().split()))

for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
res = dijkstra(0)
if res == INF:
    print(-1)
else:
    print(res)
