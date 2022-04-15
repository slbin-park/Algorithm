import sys
import heapq

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))  # 가중치 , 간선
    distance[start] = 0
    while heap:
        cost, index = heapq.heappop(heap)
        if distance[index] < cost:
            continue
        for next, c in arr[index]:
            if distance[next] > cost + c:
                distance[next] = cost + c
                heapq.heappush(heap, [cost + c, next])


n, m = map(int, input().split())
start = int(input())
arr = [[] for i in range(n + 1)]
distance = [INF for i in range(n + 1)]
for i in range(m):
    u, v, w = map(int, input().split())
    # u에서 v로 가는 가중치는 w이다.
    arr[u].append([v, w])
dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])