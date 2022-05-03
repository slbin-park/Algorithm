import sys
import heapq


def dijkstra(start):
    heap = []
    dis = [INF for i in range(n + 1)]
    heapq.heappush(heap, [0, start])
    while heap:
        cost, idx = heapq.heappop(heap)
        if dis[idx] < cost:
            continue
        for nxt, cst in arr[idx]:
            if dis[nxt] > cost + cst:
                dis[nxt] = cost + cst
                heapq.heappush(heap, [cost + cst, nxt])
    return dis


input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
s, t = map(int, input().split())
distance = dijkstra(s)
print(distance[t])