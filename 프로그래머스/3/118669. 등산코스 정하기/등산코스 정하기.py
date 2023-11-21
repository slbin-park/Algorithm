import heapq
def solution(n, paths, gates, summits):
    answer = [0,1e9]
    dis = [1e9 for i in range(n+1)]
    arr = [[]for i in range(n+1)]
    dic = {}
    heap = []
    for i,j,w in paths:
        arr[i].append([j,w])
        arr[j].append([i,w])
    for idx in summits:
        dic[idx] = 1
    for idx in gates:
        dis[idx] = 0
        heapq.heappush(heap,[0,idx])
    while heap:
        cost,idx = heapq.heappop(heap)
        if idx in dic or cost > dis[idx]:
            continue
        for nxt,cst in arr[idx]:
            if dis[nxt] > max(cost,cst):
                dis[nxt] = max(cost,cst)
                heapq.heappush(heap,[max(cost,cst),nxt])
    summits.sort()
    for idx in summits:
        if answer[1] > dis[idx]:
            answer = [idx,dis[idx]]
    return answer