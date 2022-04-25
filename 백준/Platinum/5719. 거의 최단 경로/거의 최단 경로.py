import heapq
import sys
import collections
from collections import deque

input = sys.stdin.readline
INF = 9876543210


def dijkstra(start, arr, n):
    heap = []
    dis = [INF for i in range(n)]
    heapq.heappush(heap, [0, start])
    dis[start] = 0
    while heap:
        cost, idx = heapq.heappop(heap)
        if idx == end:
            continue
        for next, cst in arr[idx].items():
            if dis[next] > cost + cst:
                dis[next] = cost + cst
                heapq.heappush(heap, [cost + cst, next])
    return dis


def bfs(distance, start):
    dq = deque()
    dq.append(end)
    remove_list = []
    while dq:
        cur = dq.popleft()
        if cur == start:  # 시작점 도달
            continue  #       break하면 다른 최단 경로를 확인할 수 없다.
        for prev, cost in arr2[cur]:
            if distance[prev] + cost == distance[cur]:
                if [prev, cur] not in remove_list:
                    remove_list.append([prev, cur])
                    dq.append(prev)
    return remove_list


while 1:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    start, end = map(int, input().split())
    arr = [dict() for i in range(n)]
    arr2 = [[] for i in range(n)]
    for i in range(m):
        u, v, p = map(int, input().split())
        arr[u][v] = p
        arr2[v].append([u, p])
        # 경로 역추적 하기위해서
    # 최단경로 구하기
    distance = dijkstra(start, arr, n)
    # 최단경로들 다 뽑음

    rm_ls = bfs(distance, start)

    for cur, next in rm_ls:
        del arr[cur][next]
    res = dijkstra(start, arr, n)
    if res[end] == INF:
        print(-1)
    else:
        print(res[end])
