import heapq
import sys

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    heap = []
    distance = [[INF for i in range(k)] for i in range(n + 1)]
    heapq.heappush(heap, [0, start])
    distance[1][0] = 0
    while heap:
        cost, idx = heapq.heappop(heap)
        for next, cst in arr[idx]:
            if distance[next][k - 1] > cost + cst:
                distance[next][k - 1] = cost + cst
                distance[next].sort()
                heapq.heappush(heap, [cost + cst, next])
    return distance


n, m, k = map(int, input().split())

arr = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])


res = dijkstra(1)

for i in range(1, n + 1):
    if res[i][k - 1] == INF:
        print(-1)
    else:
        print(res[i][k - 1])
