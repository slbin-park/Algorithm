import heapq
import sys

input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    heap = []
    distance = [INF for i in range(n + 1)]
    distance[start] = 0
    res = 0
    heapq.heappush(heap, [start, 0])
    while heap:
        idx, cost = heapq.heappop(heap)
        if distance[idx] < cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [next, cost + cst])
    for i in range(1, n + 1):
        if distance[i] <= m:
            res += item[i]
    return res


n, m, r = map(int, input().split())
# 지역개수 , 수색범위 , 길의 개수
arr = [[] for i in range(n + 1)]
item = [0]
inp_item = list(map(int, input().split()))

for i in range(n):
    item.append(inp_item[i])

for i in range(r):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
res = 0
for i in range(1, n + 1):
    res = max(res, dijkstra(i))
print(res)