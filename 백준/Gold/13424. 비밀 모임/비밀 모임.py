import sys
import heapq


def dijkstra(start, arr, n):
    heap = []
    heapq.heappush(heap, [0, start])
    dis = [1e9 for i in range(n + 1)]
    dis[start] = 0
    while heap:
        cost, idx = heapq.heappop(heap)
        if cost > dis[idx]:
            continue
        for nxt, cst in arr[idx]:
            if dis[nxt] > cost + cst:
                dis[nxt] = cost + cst
                heapq.heappush(heap, [cost + cst, nxt])
    return dis


input = sys.stdin.readline
a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    for j in range(m):
        u, v, w = map(int, input().split())
        arr[u].append([v, w])
        arr[v].append([u, w])
    k = int(input())
    distance = []
    people = map(int, input().split())
    for person in people:
        distance.append(dijkstra(person, arr, n))
    res = 1e9
    answer = 0
    for j in range(n + 1):
        cur = 0
        for p in range(k):
            cur += distance[p][j]
        if res > cur:
            res = cur
            answer = j
    print(answer)
