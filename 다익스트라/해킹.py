import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def dijkstra(start, arr, n):
    heap = []
    distance = [INF for i in range(n + 1)]
    distance[start] = 0
    heapq.heappush(heap, [start, 0])
    while heap:
        idx, cost = heapq.heappop(heap)
        if cost > distance[idx]:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [next, cost + cst])
    max_dis = 0
    res_cnt = 0
    for i in range(1, n + 1):
        if distance[i] != INF:
            max_dis = max(max_dis, distance[i])
            res_cnt += 1
    return [res_cnt, max_dis]


n = int(input())
for i in range(n):
    n, d, c = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    for j in range(d):
        a, b, s = map(int, input().split())
        arr[b].append([a, s])
    a, b = dijkstra(c, arr, n)
    print(a, b)
