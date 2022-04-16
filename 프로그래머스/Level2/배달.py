import heapq


def dijkstra(start, arr):
    INF = 1e9
    heap = []
    distance = [INF for i in range(len(arr))]
    distance[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        cost, idx = heapq.heappop(heap)
        if distance[idx] < cost:
            continue
        for next, cst in arr[idx]:
            if distance[next] > cost + cst:
                distance[next] = cost + cst
                heapq.heappush(heap, [cost + cst, next])
    return distance


def solution(N, road, K):
    answer = 0
    arr = [[] for i in range(N + 1)]
    for i in range(len(road)):
        arr[road[i][0]].append([road[i][1], road[i][2]])
        arr[road[i][1]].append([road[i][0], road[i][2]])
    a = dijkstra(1, arr)
    for i in range(1, N + 1):
        if a[i] <= K:
            answer += 1
    return answer