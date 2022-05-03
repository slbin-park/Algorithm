import sys
import heapq

INF = 1e9


def dijkstra(start):
    heap = []
    dis = [INF for i in range(v + 1)]
    heapq.heappush(heap, [0, start])
    while heap:
        cost, idx = heapq.heappop(heap)
        if dis[idx] < cost:
            continue
        for nxt, cst in arr[idx]:
            if dis[nxt] > cost + cst:
                heapq.heappush(heap, [cost + cst, nxt])
                dis[nxt] = cost + cst
    return dis


input = sys.stdin.readline
v, e, p = map(int, input().split())
if p == 1:
    print('SAVE HIM')
    exit(0)
arr = [[] for i in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
f_dijk = dijkstra(1)
s_dijk = dijkstra(p)

if f_dijk[v] == f_dijk[p] + s_dijk[v]:
    print('SAVE HIM')
else:
    print('GOOD BYE')