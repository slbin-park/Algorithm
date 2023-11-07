import heapq
import sys

input = sys.stdin.readline
INF = 1e9
n, m = map(int, input().split())

arr = [[] for i in range(n + 1)]
heap = []
dis = [1e9 for i in range(n + 1)]

start = int(input())
dis[start] = 0
for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
heapq.heappush(heap, [0, start])
while heap:
    cost, idx = heapq.heappop(heap)
    if dis[idx] < cost:
        continue
    for next, cst in arr[idx]:
        if dis[next] > cost + cst:
            dis[next] = cost + cst
            heapq.heappush(heap, [cost + cst, next])
for i in range(1, n + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])
