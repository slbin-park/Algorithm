import sys
import heapq

INF = 1e9
input = sys.stdin.readline


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, [start, 0])
    distance = [INF for i in range(n + 1)]
    distance[start] = 0
    while heap:
        idx, cost = heapq.heappop(heap)
        if distance[idx] > cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [next, cost + cst])
    return distance[end]


n, e = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(e):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
start, end = map(int, input().split())

res1 = dijkstra(1, start) + dijkstra(start, end) + dijkstra(end, n)
res2 = dijkstra(1, end) + dijkstra(end, start) + dijkstra(start, n)
res = min(res1, res2)
res = res if res < INF else -1
print(res)
