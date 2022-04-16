import heapq
import sys

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    heap = []
    distance = [INF for i in range(n + 1)]
    res = [0 for i in range(n + 1)]
    distance[start] = 0
    heapq.heappush(heap, [start, 0])
    while heap:
        idx, cost = heapq.heappop(heap)
        if distance[idx] < cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                if start == idx: res[next] = next
                else: res[next] = res[idx]
                heapq.heappush(heap, [next, cost + cst])
    return res


n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
for i in range(1, n + 1):
    dis = dijkstra(i)
    for j in range(1, n):
        if j == i:
            print('-', end=' ')
        else:
            print(dis[j], end=' ')
    if i == n:
        print('-')
    else:
        print(dis[-1])
