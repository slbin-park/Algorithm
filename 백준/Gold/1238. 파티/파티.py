import heapq
import sys

input = sys.stdin.readline
INF = 1e9


def dijkstra(start, end):
    heap = []
    distance = [INF for i in range(n + 1)]
    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        cost, idx = heapq.heappop(heap)
        if distance[idx] < cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [cost + cst, next])
    return distance[end]


def dijkstra2(start):
    heap = []
    distance = [INF for i in range(n + 1)]
    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        cost, idx = heapq.heappop(heap)
        if distance[idx] < cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [cost + cst, next])
    return distance


n, m, x = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
res = 0

x_arr = dijkstra2(x)

for i in range(1, n + 1):
    if i != x:
        cur = dijkstra(i, x)
        cur += x_arr[i]
        res = max(res, cur)
print(res)
