import sys
import heapq

INF = 1e9


def dijkstra(start, end):
    heap = []
    dis = [INF for i in range(n + 1)]
    dis[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        cost, index = heapq.heappop(heap)
        if cost > dis[index]:
            continue
        for i, c in graph[index]:
            if dis[i] > dis[index] + c:
                dis[i] = dis[index] + c
                heapq.heappush(heap, (dis[i], i))
    return dis[end]


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))
start, end = map(int, input().split())
ans1 = dijkstra(1, start) + dijkstra(start, end) + dijkstra(end, n)
ans2 = dijkstra(1, end) + dijkstra(end, start) + dijkstra(start, n)
if ans1 >= INF and ans2 >= INF:
    print(-1)
else:
    print(min(ans1, ans2))
